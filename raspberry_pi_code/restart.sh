#!/bin/bash
./image_capture "$@"
while [ $? -eq 42 ]; do
	sleep 60
	./image_capture "$@"
done
