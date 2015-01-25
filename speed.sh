#!/bin/bash
transmission-remote 9091 -n username:123456 -l|grep Sum:|tr -s '  '|cut -d' ' -f 5
