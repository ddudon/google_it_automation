#!/usr/bin/env python3
import paramiko


def ssh_test(hosts):
    port = 22
    username = 'root'
    # hosts = ["192.168.10.100", "192.168.10.110", "192.168.10.111"]
    commands = ["hostname", "curl ipinfo.io| grep ip", "ifconfig enp1s0", "poweroff"]

    for host in hosts:
        for command in commands:
            paramiko.util.log_to_file('paramiko.log')
            s = paramiko.SSHClient()
            s.load_system_host_keys()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            s.connect(host, port, username)
            stdin, stdout, stderr = s.exec_command(command)
            output = ""
            for line in stdout.readlines():
                output = output + line
            print(output)
            # if output != "":
            #     print(output)
            # else:
            #     print("There was no output for this command")
        print("###########################################################################\n")

# hosts = ["192.168.10.100", "192.168.10.110", "192.168.10.111"]
hosts = ["master-1", "data-1", "data-2"]
ssh_test(hosts)
