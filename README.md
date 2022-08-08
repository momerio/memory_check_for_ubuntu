# memory_check_for_ubuntu

## USAGE

STEP1: You write "memory_check.py path(full path)" and "discord webhook url" in "memory_check.sh".

```
EXECUTE_PATH=<<PYTHON FILE PATH>>
DISCORD_WEBHOOK_URL=<<WEBHOOK_URL>>
```

STEP2: If you want to use cron, you can write the execute command in crontab.(Which using ubuntu)

You can bellow execute command to open crontab.

`crontab -e`

You write bellow line(example).

`0 6 * * * bash <<COMMAND>>`

Finally, You save crontab.

## RUN EXAMPLE

<img src="https://github.com/momerio/memory_check_for_ubuntu/blob/31682b7ef9934b61ad948c64e4a6bf825d826e78/example.png" width=500px>
