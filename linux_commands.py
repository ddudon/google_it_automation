#!/usr/bin/env python3

import subprocess


def uname():
    command = "uname"
    command_arg = "-a"
    print("Gathering system info with \"uname\" command...")
    subprocess.call([command, command_arg])
    print()


def df():
    command = "df"
    command_arg = "-h"
    print("Gathering disk info with \"df\" command...")
    subprocess.call([command, command_arg])
    print()


def w():
    command = "w"
    print("Here is some quick info...")
    subprocess.call([command])
    print()


def ifconfig_wlan():
    command = "ifconfig"
    command_arg = "wlp82s0"
    print("Network info:", command_arg)
    subprocess.call([command, command_arg])
    print()


def ifconfig_lan():
    command = "ifconfig"
    command_arg = "enp0s31f6"
    print("Network info:", command_arg)
    subprocess.call([command, command_arg])
    print()


def ip_info():
    command = "curl"
    command_arg = "ipinfo.io"
    print("Info about your IP...")
    subprocess.call([command, command_arg])
    print()


def main():
    uname()
    w()
    df()


if __name__ == "__main__":
    main()
