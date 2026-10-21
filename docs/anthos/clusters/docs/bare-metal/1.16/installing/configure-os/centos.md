---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-os/centos/
title: Configure CentOS \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:11.353721+00:00
---

# Configure CentOS  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-os/centos/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure CentOS Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/configure-os/centos)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-os/centos)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



You must configure the base operating system of your node machines to use Distributed Cloud. This page contains the steps you need to take to complete the needed configuration.  
For more information about troubleshooting Distributed Cloud requirements, see the [troubleshooting guides](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues).

**Caution:** CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs)) from Google Distributed Cloud. **All support for CentOS is removed from the upcoming release of Google Distributed Cloud (December 2023) and subsequent releases.**

## Before you begin

Ensure you are using a supported version of your operating system. Anthos on bare metal supports the following versions for CentOS:

  * CentOS 8.2
  * CentOS 8.3
  * CentOS 8.4
  * CentOS 8.5



Ensure you have root access to the machines you are configuring. Validate Package manager with the following steps:

  1. Check for updates:
         
         sudo dnf check-update

  2. Ensure the output has no errors and includes the last metadata expiration check. For example:
         
         # Last metadata expiration check: ...
         ...
         google-cloud-sdk.x86_64 ...
         




## Configure or disable firewalld

Firewalld can be configured for use with Google Distributed Cloud or disabled. For information on configuring firewalld, see [Configuring firewalld ports](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs#configuring_firewalld_ports) on the Network requirements page.

The following instructions disable firewalld.

  1. Disable firewalld:
         
         sudo systemctl stop firewalld
         sudo systemctl disable firewalld

  2. Check the status of firewalld to ensure it is disabled:
         
         sudo systemctl status firewalld | grep "Active"
         # Output
         # Active: inactive (dead)




## Configure Docker 19.03+ on your workstation

**Note:** The workstation running `bmctl` needs non-root user access to Docker to start the temporary bootstrap cluster during installation. To enable non-root user access to Docker, go to [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

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

  2. Remove podman-manpages
         
         sudo dnf remove podman-manpages
         

  3. Install Docker 19.03+:
         
         sudo dnf install -y yum-utils
         sudo yum-config-manager \
             --add-repo \
             https://download.docker.com/linux/centos/docker-ce.repo
         sudo dnf install -y docker-ce docker-ce-cli containerd.io
         sudo systemctl start docker

  4. Verify you are now running version 19.03+:
         
         sudo docker version

  5. Compare your output with the following example to ensure the Client and Server versions are 19.03+ :
         
         Client: Docker Engine - Community
          Version:           19.03.13
          ...
          Server: Docker Engine - Community
           Engine:
           Version:          19.03.13
         




## Set up time synchronization

Time synchronization consists of setting the clocks on your node machines, using a designated external time reference. Time synchronization is important for time-sentive cluster activities, such as event logging and metrics collection. The kernel of your node machine controls the clock in containers that run on the node. To ensure proper time synchronization, install a network time protocol (NTP) service on your machines, using any of the available services: [`chrony`](https://chrony.tuxfamily.org/), [`systemd- timesyncd`](https://wiki.archlinux.org/index.php/systemd-%0Atimesyncd), `ntp`, or `ntpdate`. Run `timedatectl` to verify that the system clock is synchronized. The output of `timedatectl` should contain the following status:
    
    
    System clock synchronized: yes
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
