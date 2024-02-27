# SSH Notify

SSHのログイン/ログアウト通知をDiscordに送信するためのPythonスクリプトです。

## Requirements

```
python: 3.12.2
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
netifaces==0.11.0
requests==2.31.0
urllib3==2.2.1
```

## Usage

1. `$ python -m venv .env`
2. `$ pip install -r requirements.txt`
3. notify_discord.pyを実行するシェルスクリプトを作成(以下は例)

```bash
#!/bin/bash

cd /home/username/ssh-notify
source .env/bin/activate
python notify_discord.py
```

4. `/etc/pam.d/sshd`に以下を追加

```
session optional pam_exec.so type=open_session /home/username/ssh-notify/notify_discord.sh
```

## Reference

[UbuntuへのSSHログインをDiscordに通知してみる](https://zenn.dev/myuki/articles/4324ab701fe5ab)

## Licence

Copyright (c) 2024 MnyaCat  
Released under the MIT license  
see [LICENSE file](./LICENSE)
