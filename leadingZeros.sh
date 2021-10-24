#!bash

awk 'match($0, /[0-9]+/){ x = substr( $0, RSTART, RLENGTH )
printf("%s %03d\n", $1, x)
}'

