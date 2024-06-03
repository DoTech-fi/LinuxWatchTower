# CHANGELOG



## v1.0.1 (2024-06-03)

### Fix

* fix(check_tool): fix code to return both installation and version status ([`b494fee`](https://github.com/DoTech-fi/LinuxWatchTower/commit/b494fee97030b2fedec09f08fb67c8af21bde6c9))

### Refactor

* refactor(check_state): a tiny change ([`11d97c4`](https://github.com/DoTech-fi/LinuxWatchTower/commit/11d97c4f37b7d92da85c88ce06e7fc507b00b931))


## v1.0.0 (2024-05-28)

### Breaking

* feat(ui): switch form command line to gui

BREAKING CHANGE: switch form command line to gui ([`19e8093`](https://github.com/DoTech-fi/LinuxWatchTower/commit/19e809349f0a4e3465935e5fb98d9317dc58c340))


## v0.9.0 (2024-05-21)

### Chore

* chore(requirments.txt/tools): adding new package and some modification ([`0c6dee8`](https://github.com/DoTech-fi/LinuxWatchTower/commit/0c6dee866a1edf2d8d6e6206be4374a993496ed8))

### Feature

* feat(tools): change the way of checking db/remote state and add functionality to install missing pckages while checking status ([`6787a9b`](https://github.com/DoTech-fi/LinuxWatchTower/commit/6787a9b14b07f5f03b2e9a10aa7360155b6dd214))

### Refactor

* refactor(ssh): refactor code of set_target to force user set a value for mandatory parameters ([`b66a4cb`](https://github.com/DoTech-fi/LinuxWatchTower/commit/b66a4cb54247ffed657bdfde1312ae52a6c61c73))


## v0.8.0 (2024-05-20)

### Feature

* feat(rich): add rich library functionality to have more stunning console ([`0a122c8`](https://github.com/DoTech-fi/LinuxWatchTower/commit/0a122c88d82bf627f16017e12e381ae38586560c))


## v0.7.0 (2024-05-20)

### Chore

* chore(roles): add some versions ([`fdbb6b6`](https://github.com/DoTech-fi/LinuxWatchTower/commit/fdbb6b6da2343508574adc930e30137b53d0b466))

### Feature

* feat(tools): add check_state function/option ([`a509779`](https://github.com/DoTech-fi/LinuxWatchTower/commit/a509779b68b58cdcb9c98cd7d8f4dfd1ba7ae3a9))

### Fix

* fix(check_tool): fix bug ([`fd3c052`](https://github.com/DoTech-fi/LinuxWatchTower/commit/fd3c05211d480e97d2e89414700c291d487282e6))


## v0.6.0 (2024-05-20)

### Feature

* feat(tools): add install_ansible_role function to check if our ansble galaxt roles are installed or not and refactor code ([`2f5affe`](https://github.com/DoTech-fi/LinuxWatchTower/commit/2f5affe254518b9732eacb68e604e9aa8b70b413))


## v0.5.0 (2024-05-20)

### Feature

* feat(get_host_nicknames): add config_path paramater to get_host_nicknames function which allow us to define which path we want to be checked during installation ([`9be9ed1`](https://github.com/DoTech-fi/LinuxWatchTower/commit/9be9ed1a08a8c56e44cf0b806bf8bd67b8899af5))


## v0.4.1 (2024-05-19)

### Fix

* fix(check_tool): disable console verbosity and fix bug for checking service existance part on target machine ([`86046d3`](https://github.com/DoTech-fi/LinuxWatchTower/commit/86046d335a5f4e0534f50021717bd12f3c434ad2))

### Refactor

* refactor(tools): some modification on checking service existance ([`cbf89a7`](https://github.com/DoTech-fi/LinuxWatchTower/commit/cbf89a75e7343d990e4bee83d2fdd2644de0f131))

* refactor(README.md): some modification ([`919c7ca`](https://github.com/DoTech-fi/LinuxWatchTower/commit/919c7cabaefc650b2be904e4da55d834dec129fe))


## v0.4.0 (2024-05-19)

### Feature

* feat(db): add update_installation function ([`f2a7667`](https://github.com/DoTech-fi/LinuxWatchTower/commit/f2a7667b06d6f074d41a7db41a8e41760e576b30))

* feat(check_tools): add check_tools module which currently contains a function to check if our package is available on remote host ([`4a6e9ac`](https://github.com/DoTech-fi/LinuxWatchTower/commit/4a6e9ac6d656fd56ecce05f94b284b53269d26a4))


## v0.3.0 (2024-05-19)

### Feature

* feat(ssh): add port option to ssh/config and refactor some texts ([`2d54e45`](https://github.com/DoTech-fi/LinuxWatchTower/commit/2d54e454433243911d9f4c6db9b347a64da84ce1))


## v0.2.0 (2024-05-19)

### Feature

* feat(main): add main file to run app ([`e63510b`](https://github.com/DoTech-fi/LinuxWatchTower/commit/e63510b5f8909657cb83f6af078d91eeb297b26f))

* feat(tools): add tools module ([`fc65863`](https://github.com/DoTech-fi/LinuxWatchTower/commit/fc658632de05ca5b644f0a3c864439f772816599))

* feat(ssh): add ssh module ([`52bf52a`](https://github.com/DoTech-fi/LinuxWatchTower/commit/52bf52ad6195f4f710cc706c3a97bba12bf897b0))

* feat(db): add db module ([`2d6d25a`](https://github.com/DoTech-fi/LinuxWatchTower/commit/2d6d25a12a4e9150b594f42d6862a157fa3e8d62))

* feat(ansible_utils): add ansible_utils module ([`8b1058d`](https://github.com/DoTech-fi/LinuxWatchTower/commit/8b1058df6cbfb7159a56d44a57e56cb093a65d90))

* feat(requirements.txt): add requirements.txt ([`e01a218`](https://github.com/DoTech-fi/LinuxWatchTower/commit/e01a218fa56c131dbea70a0a3634e257725879bc))

* feat(README): add README.md ([`15a8a90`](https://github.com/DoTech-fi/LinuxWatchTower/commit/15a8a9092e53cb98585f7502e133ded1ce8db4ac))

* feat(.gitignore): update .gitignore ([`9552921`](https://github.com/DoTech-fi/LinuxWatchTower/commit/9552921d6a788c31c66ceadb7e6d422b0a5c8831))


## v0.1.0 (2024-05-17)

### Feature

* feat(.gitignore): add .gitignore ([`a4e8b48`](https://github.com/DoTech-fi/LinuxWatchTower/commit/a4e8b4881ce5e371b625eb22ea071ae52780dc28))

* feat(.github): add versioning (semantic) action ([`f6bbfe4`](https://github.com/DoTech-fi/LinuxWatchTower/commit/f6bbfe403d43d2a60562f05772bf046cb0308049))

### Unknown

* Initial commit ([`9851722`](https://github.com/DoTech-fi/LinuxWatchTower/commit/98517229de96ff711147895cce6f75a8185a12dc))
