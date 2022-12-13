ls -al
ps
ps -ax
rabbitmqctl --version
rabbitmq-plugins --version
rabbitmq-plugins enable rabbitmq_management
ls -al
exit
rabbitmqctl --version
rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin administrator
exit
