#!/bin/bash
# record stdin, stdout, stderr of command, usage: add ./wrap_io.sh before call origin command
dir=.
stdin=stdin.json
stdout=stdout.json
stderr=stderr
cd $dir
# save it's stdin, stdout, and stderr to file
tee $stdin|$@ 2>$stderr 1>$stdout
# save exit status
status=$?
# output stdin, stderr 
cat $stdout
cat $stderr >/dev/stderr
# replay is't exit status
exit $status
