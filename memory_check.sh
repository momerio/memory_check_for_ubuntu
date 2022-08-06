#!/bin/bash

EXECUTE_PATH=<<PYTHON PATH>>
DISCORD_WEBHOOK_URL=<<WEBHOOK_URL>>

MESSAGE=`python ${EXECUTE_PATH}`
echo "$MESSAGE"

curl -H "Content-Type: application/json" -X POST -d "{\"content\":\"${MESSAGE}\"}" ${DISCORD_WEBHOOK_URL}
