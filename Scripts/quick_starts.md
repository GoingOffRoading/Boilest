

docker run --hostname=91adaacc184d --user=boil --env=Manager=Yes --env=Worker=No --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=TZ=US/Pacific --env=FLOWER_FLOWER_BASIC_AUTH=celery:celery --env=FLOWER_persistent=true --env=FLOWER_db=/Boilest/flower_db --env=FLOWER_purge_offline_workers=60 --env=FLOWER_UNAUTHENTICATED_API=true --env=Celery_User=celery --env=Celery_PW=celery --env=RabbitMQ_Server=192.168.1.110 --env=RabbitMQ_Port=31672 --volume=C:\Users\Chase\Boilest:/Boilest --volume=C:\Users\Chase\media\Newfolder\boil_watch:/boil_watch --workdir=/Scripts -p 5000:5000 -p 5555:5555 --runtime=runc -d worker:latest