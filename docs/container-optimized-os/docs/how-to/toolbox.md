---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox/
title: Debugging node issues using toolbox \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:52.305678+00:00
---

# Debugging node issues using toolbox  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Debugging node issues using toolbox Stay organized with collections  Save and categorize content based on your preferences. 

You might need to install additional packages or tools on Container-Optimized OS for certain tasks, such as debugging. For example, debug node connectivity issues by [installing `tcpdump` in toolbox](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/connectivity-issues-in-cluster#toolbox-commands). Although Container-Optimized OS does not include a package manager, you can use the pre-installed [toolbox](https://cos.googlesource.com/cos/tools/+/refs/heads/master/src/cmd/toolbox/) utility to install any additional packages or tools you require. Using `/usr/bin/toolbox` is the preferred method for installing and running one-off debugging tools.

**Note:** toolbox is a debugging utility and not intended for production use.**Note:** For some small machine types, such as e2-micro, extracting large container images like the default toolbox base image might be slow. It might be better to use a smaller base image with only the specific tools you need installed. See Customize toolbox for your deployment for more details.

`/usr/bin/toolbox` essentially provides you a shell in a Debian chroot-like environment. When you invoke `/usr/bin/toolbox`, it runs following commands:

  1. `docker pull` and `docker create` to set up the environment. These are only run the first time you invoke `/usr/bin/toolbox`.
  2. `systemd-nspawn` to run the given command or (in absence of any command) provides you a shell



`toolbox` has some other properties to keep in mind:

  * Invoking `toolbox` after the first invocation does not require a working Docker daemon, nor does it incur any network or disk overhead.
  * The `toolbox` environment is set up once for each user invoking it. Running `sudo toolbox` sets it up for `root` user.
  * The `toolbox` environment is created under `/var/lib/toolbox` and is persistent across reboots.
  * You can access sections of the root file system, such as user home directories, from inside the `toolbox` environment.



## Customize toolbox for your deployment

In the following examples, we assume that your username is `USER` and your Container-Optimized OS instance name is `cos-dev`.

You can customize the Docker image that `toolbox` uses, as well as the paths available to `toolbox` in the root file system. These settings are located in the file `/etc/default/toolbox`. The default `/etc/default/toolbox` file typically resembles the following:
    
    
    USER@cos-dev ~ $ cat /etc/default/toolbox
    # Copyright 2016 The Chromium OS Authors. All rights reserved.
    # Use of this source code is governed by a BSD-style license that can be
    # found in the LICENSE file.
    
    TOOLBOX_DOCKER_IMAGE="gcr.io/cos-cloud/toolbox"
    TOOLBOX_DOCKER_TAG="v20220722"
    TOOLBOX_BIND="--bind=/:/media/root/ --bind=/mnt/disks/:/media/root/mnt/disks/ --bind=/var/:/media/root/var/ --bind=/home:/media/root/home/ --bind=/etc/resolv.conf:/etc/resolv.conf"
    : ${USER:=root}
    

  * The `TOOLBOX_DOCKER_IMAGE` and `TOOLBOX_DOCKER_TAG` variables specify the Docker image to be used. The default `gcr.io/cos-cloud/toolbox` comes with some of the common tools like the Google Cloud CLI pre-installed.
  * The `TOOLBOX_BIND` variable specifies the paths from rootfs to be made available inside the toolbox environment.



To change the default settings, modify the `/etc/default/toolbox` file, or specify new values for the variables in `${HOME}/.toolboxrc` for the appropriate user. For example, assuming that you want `toolbox` to use `fedora:latest` as its container, you can run the following commands:
    
    
    USER@cos-dev ~ $ echo "TOOLBOX_DOCKER_IMAGE=docker.io/library/fedora" > "${HOME}/.toolboxrc"
    USER@cos-dev ~ $ echo "TOOLBOX_DOCKER_TAG=latest" >> "${HOME}/.toolboxrc"
    USER@cos-dev ~ $ toolbox
    

The `/etc/default/toolbox` file can be modified as shown in the following.
    
    
    USER@cos-dev ~ $ cat /etc/default/toolbox
    # Copyright 2016 The Chromium OS Authors. All rights reserved.
    # Use of this source code is governed by a BSD-style license that can be
    # found in the LICENSE file.
    
    TOOLBOX_DOCKER_IMAGE="gcr.io/cos-cloud/toolbox"
    TOOLBOX_DOCKER_TAG="v20220722"
    TOOLBOX_DOCKER_IMAGE_TARBALL=<var>[location/to/tarball]</var>
    TOOLBOX_BIND="--bind=/:/media/root/ --bind=/mnt/disks/:/media/root/mnt/disks/ --bind=/var/:/media/root/var/ --bind=/home:/media/root/home/"
    : ${USER:=root}
    USER@cos-dev ~ $ toolbox
    

## Install and run tools from toolbox

Once you've invoked the `toolbox` utility to start the shell, you can use `apt-get` inside the resulting container to install packages. For example:
    
    
    # Inside the toolbox shell
    USER@cos-dev ~ $ toolbox
    root@cos-dev:~# apt-get update && apt-get install -y htop psmisc
    root@cos-dev:~# htop
    root@cos-dev:~# pstree -p
    root@cos-dev:~# exit
    

You don't always have to enter `toolbox` to run commands in it. You can prefix your commands with `toolbox`. For example, to install and run the `strace` utility to trace the execution of the Docker daemon, you can do the following:
    
    
    USER@cos-dev ~ $ toolbox apt-get install -y strace
    USER@cos-dev ~ $ toolbox strace -p `pidof dockerd`
    

The Google Cloud CLI is pre-installed in toolbox:
    
    
    USER@cos-dev ~ $ toolbox
    root@cos-dev:~# which gcloud
    /google-cloud-sdk/bin/gcloud
    # View installed components
    root@cos-dev:~# gcloud components list
    
    Your current gcloud CLI version is: 287.0.0
    The latest available version is: 295.0.0
    ...
    

Keep in mind that the gcloud CLI can only access resources that the VM instance is authorized to access. Read the [Compute Engine](https://docs.cloud.google.com/compute/docs/access) documentation to learn more about provisioning VM instances with access to other resources.

Read the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) documentation to learn more about using the gcloud CLI.

## Get files into and out of toolbox

The root file system of the host is accessible inside `toolbox` through the `/media/root` path. On the host, the root directory of `toolbox` is accessible through the following path: `/var/lib/toolbox/USER-gcr.io_cos-cloud_toolbox-VERSION/root` where `USER` is your username and `VERSION` is the `toolbox` version number (for example, `v20220722`).

The following examples show how to get files into and out of `toolbox`:
    
    
    # Access the host filesystem inside the toolbox
    USER@cos-dev ~ $ toolbox
    root@cos-dev:~# ls /media/root
    bin  boot  dev  etc  home  lib  lib64  ...
    root@cos-dev:~# cp /media/root/home/USER/some-file .
    
    # Access toolbox directory from the host
    USER@cos-dev ~ $ sudo cp some-file /var/lib/toolbox/USER-gcr.io_cos-cloud_toolbox-v20220722/root
    
    # Run a command inside toolbox and save its output in your home directory
    USER@cos-dev ~ $ toolbox strace -o /media/root/$HOME/ls.strace ls
    USER@cos-dev ~ $ more $HOME/ls.strace
    

## Clean up disk space used by toolbox

The toolbox installation consumes approximately 2-3 GB of disk space in `/var` (disk usage varies with the Container-Optimized OS version). To free disk space used by toolbox, perform the following tasks depending on your Container-Optimized OS version:
    
    
    # remove files in /var/lib/toolbox
    sudo rm -rf /var/lib/toolbox/*
    
    # remove container artifacts
    sudo ctr images rm $IMAGE_NAME
    

You can run `sudo ctr images ls -q` to determine this value. For example, `IMAGE_NAME=gcr.io/cos-cloud/toolbox:v20220722`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
