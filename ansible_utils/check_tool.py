from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict

def check_tool_remote(nickname, tool_name):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[nickname + ','])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    context.CLIARGS = ImmutableDict(
        connection='ssh',
        module_path=None,
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        remote_user=None,
        verbosity=3
    )

    play_source = dict(
        name="Check Tool",
        hosts=nickname,
        gather_facts='no',
        tasks=[
            dict(name=f"Check if {tool_name} is installed",
                 action=dict(module='command', args=dict(cmd=f'which {tool_name}')),
                 register='tool_check',
                 failed_when="tool_check.rc != 0",
                 ignore_errors=True)
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    tqm = None
    result = False
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords=dict(),
        )
        results = tqm.run(play)
        if results:
            result = True
    finally:
        if tqm is not None:
            tqm.cleanup()
    return result