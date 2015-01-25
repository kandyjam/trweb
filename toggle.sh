#!/bin/bash

LIMIT=$1

if [ "$LIMIT" = "true" ]; then
    transmission-remote 9091 -n username:123456 -as
else 
    transmission-remote 9091 -n username:123456 -AS
fi
