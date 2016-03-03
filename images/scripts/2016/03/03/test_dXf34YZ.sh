#!/bin/bash
i=0
while [ "$i" -lt 100 ];do
	echo "hello world ${i} times"
	let i++
done
