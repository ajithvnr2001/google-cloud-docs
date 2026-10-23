---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel/
title: Configure RHEL \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:06.966625+00:00
---

# Configure RHEL  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure RHEL Stay organized with collections  Save and categorize content based on your preferences. 

You must configure the base operating system of your node machines to use Google Distributed Cloud. This page contains the steps you need to take to complete the needed configuration. For more information about troubleshooting Google Distributed Cloud, see the [troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues).

## Before you begin

Ensure you are using a supported version of your operating system. For a list of supported versions, see [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).

## Enable cgroupsv2

Google Distributed Cloud software-only for bare metal version 1.35 and later requires `cgroupsv2`. Your operating system must support `cgroupsv2` in order to create or upgrade clusters.

Google Distributed Cloud prevents creating or upgrading clusters if `cgroupsv1` is detected during preflight checks. For instructions on how to migrate your operating system to `cgroupsv2`, see [Migrating to cgroup v2](https://%0Akubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2) in the Kubernetes documentation.

For instructions on how to enable `cgroupsv2` on RHEL, see [Enabling cgroup v2](https://access.redhat.com/articles/3735611) in the Red Hat knowledge base.

## Validate the Python version

Before you initialize or upgrade a node with Google Distributed Cloud software only for bare metal version 1.35 and higher, run the command: `python3 --version` to validate the current Python version.

If the Python version is 3.8 or lower, you must install Python 3.9 on that node.

To install Python 3.9 or higher and ensure your node initializes or updates as expected, do the following:

  1. Install Python 3.9:
         
         sudo dnf install -y python39
         

  2. Check that the Python 3.9 file resides at the path `/usr/bin/python3.9`.




## Enable BPF Just In Time compiler

The kernel for your operating system must have the BPF Just In Time compiler option enabled (`CONFIG_BPF_JIT=y`).

  * To find out whether this option is enabled, run the following command:
        
        grep CONFIG_BPF_JIT /boot/config-$(uname -r)
        




## Validate the package manager

Ensure that you have your RedHat username and password, and that you have root access to the machines you're configuring. Validate Package manager with the following steps:

  1. If you haven't registered your operating system, register with RedHat using your RedHat username and password to download updates:
         
         sudo subscription-manager register
         
         sudo subscription-manager refresh
         
         sudo subscription-manager attach --auto
         

  2. Check for updates:
         
         sudo dnf check-update
         

Ensure the output has no errors and includes the last metadata expiration check. For example:
         
         Updating Subscription Management repositories.
         ...
         # Last metadata expiration check: ...
         ...
         




## Configure or disable firewalld

Firewalld can be configured for use with Google Distributed Cloud or disabled. For information on configuring firewalld, see [Configure firewalld ports](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#configuring_firewalld_ports) on the Network requirements page.

The following instructions disable firewalld.

  1. Disable firewalld:
         
         sudo systemctl stop firewalld
         
         sudo systemctl disable firewalld
         

  2. Check the status of firewalld to ensure it is disabled:
         
         sudo systemctl status firewalld | grep "Active"
         # Output
         # Active: inactive (dead)
         




## Configure Docker on your workstation

**Note:** The workstation running `bmctl` needs non-root user access to Docker to start the temporary bootstrap (kind) cluster during installation. To enable non-root user access to Docker, go to [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

Follow these steps to manually install Docker:

  1. Remove any previous Docker version:
         
         sudo dnf remove docker \
             docker-client \
             docker-client-latest \
             docker-common \
             docker-latest \
             docker-latest-logrotate \
             docker-logrotate \
             docker-engine
         

  2. Remove podman-manpages:
         
         sudo dnf remove podman-manpages
         

  3. Install Docker 20.10.0+:
         
         sudo dnf install -y yum-utils
         
         sudo yum-config-manager \
             --add-repo \
             https://download.docker.com/linux/rhel/docker-ce.repo
         
         sudo dnf install -y --allowerasing docker-ce docker-ce-cli containerd.io
         
         sudo systemctl start docker
         

  4. Verify that you are now running version 20.10.0+:
         
         sudo docker version
         

  5. Compare your output with the following example to ensure the Client and Server versions are 20.10.0+:
         
         Client: Docker Engine - Community
         Version:           25.0.3
         ...
         Server: Docker Engine - Community
         Engine:
         Version:          25.0.3
         

  6. Verify Docker runs:
         
         docker run hello-world
         

You should see something similar to this:
         
         Hello from Docker!
         

This message shows that your installation appears to be working correctly.




## Set up time synchronization

Time synchronization consists of setting the clocks on your node machines, using a designated external time reference. Time synchronization is important for time-sentive cluster activities, such as event logging and metrics collection. The kernel of your node machine controls the clock in containers that run on the node. To ensure proper time synchronization, install a network time protocol (NTP) service on your machines, using any of the available services: [`chrony`](https://chrony.tuxfamily.org/), `systemd-timesyncd`, `ntp`, or `ntpdate`. Run `timedatectl` to verify the system clock is synchronized. The output of `timedatectl` should contain the following status:
    
    
    System clock synchronized: yes
    

## Ensure Linux kernel `inotify` limits are at or higher than minimum

For machines running RHEL 9 and 8.10, Linux kernel `inotify` limits for maximum user instances and user watches must be greater than or equal to the following:

  * `fs.inotify.max_user_instances`: `8192`
  * `fs.inotify.max_user_watches`: `524288`



Ensure these values are set correctly on your node machines:

  1. Check the value of `max_user_instances`:
         
         cat /proc/sys/fs/inotify/max_user_instances
         

  2. If needed, update `max_user_instances` to the minimum value:
         
         echo 'fs.inotify.max_user_instances=8192' | sudo tee --append /etc/sysctl.conf
         

  3. Check the value of `max_user_watches`:
         
         cat /proc/sys/fs/inotify/max_user_watches
         

  4. If needed, update `max_user_watches` to the minimum value:
         
         echo 'fs.inotify.max_user_watches=524288' | sudo tee --append /etc/sysctl.conf
         

  5. If you updated either value, reboot the machine.




## Best Practices

To simplify installation, we recommend that you configure RHEL using a minimal installation with headless management. Also, be sure to enable your [network connection](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_configuring-and-managing-network-access_configuring-basic-system-settings) and either use the default DHCP or provide a valid, static IP address and network information. Ensure that the machine can connect to [the required external resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy#prerequisites), such as `cloud.google.com`.

If Docker fails to run, check that the Docker daemon is running with the following command:
    
    
    sudo systemctl start docker
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
