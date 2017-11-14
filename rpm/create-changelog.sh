#!/bin/bash

FROM=$1
TO=$2

if [ -z "$TO" ]; then
    TO=$FROM
    FROM=""
fi

git log $TO -1 --pretty=format:"* %ad %an <%ae> $TO" | awk '{$5 = "" ; print $0}'
if [ -n "$FROM" ]; then
    git log $FROM...$TO --no-merges --pretty=format:'- %s' --reverse
else
    git log $TO --no-merges --pretty=format:'- %s' --reverse
fi

echo

