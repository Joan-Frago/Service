# Service

In this repository I will learn about system services and I will make a script that creates a service

There is an example of a service file here [```example-service```](https://vscode.dev/github/Joan-Frago/Service/blob/main/example-service.service)

## Create a systemd service
To create a systemd service you have to:
1. Create a service file in the ```/etc/systemd/system/``` directory
2. It's name must be ```[name_of_service].service```

**Optional**
You can create a symlink to the ```/etc/systemd/system```.

To create this symlink you can use the following command
```sudo ln -s [abs_path of source] [abs_path of destination]```
