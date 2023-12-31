#!/bin/sh
echo "starting"
echo "Getting this party started"
python /Scripts/container_start.py

echo "Checking Variables"
echo "Manager is set to:" $Manager
echo "Starting Celery"

if [ $Manager = "Yes" ]; then
    echo "Running Manager" 
    celery -A tasks_manager worker -B -l INFO -c 1 -Q manager -n manager@%n -l info &
    celery --broker=amqp://celery:celery@192.168.1.110:31672/celery flower
elif [ $Manager = "No" ]; then
    echo "Running Worker" 
    celery -A tasks_worker worker -l INFO -c 1 -Q worker -n worker@%n -l info
else
    echo "Everything is fucked"
fi
