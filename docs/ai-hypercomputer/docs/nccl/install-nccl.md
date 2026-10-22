---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl/
title: Install gIB NCCL plugins \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:06.468199+00:00
---

# Install gIB NCCL plugins  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Install gIB NCCL plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install [NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) with either Debian Software Packages (`.deb`) or the Red Hat Package Manager (`.rpm`). This installation lets you run NCCL workloads on A4X Max, A4X, A4, and A3 Ultra instances.

**Note:** Don't install older NCCL implementations like NCCL/FastSocket (A2), NCCL/TCPX (A3), NCCL/TCPXO (A3 Mega) or RxDM packages or their related environment variables on your A4X Max, A4X, A4, or A3 Ultra instances.

## (For A4X Max) Update userspace libraries

On A4X Max, you must install the latest userspace libraries before running your NCCL workloads. If you're logged in as a root user, then omit `sudo` where it occurs to run the commands directly.

### Debian 12+/Ubuntu 20.04+ (.deb package)
    
    
    sudo apt update
    sudo apt install curl
    
    # Fetch DOCA OFED userspace libraries
    export DOCA_URL="https://linux.mellanox.com/public/repo/doca/latest/ubuntu22.04/arm64-sbsa/"
    export BASE_URL="https://linux.mellanox.com/public/repo/doca"
    curl "${BASE_URL}/GPG-KEY-Mellanox.pub" | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/GPG-KEY-Mellanox.pub
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/GPG-KEY-Mellanox.pub] ${DOCA_URL} ./" | sudo tee /etc/apt/sources.list.d/doca.list
    
    sudo apt update
    sudo apt install doca-ofed-userspace
    
    # Upgrade to latest NCCL for best compatibility
    sudo apt install --only-upgrade --allow-change-held-packages libnccl2 libnccl-dev

## Install NCCL/gIB

Depending on where you run your workloads, you install NCCL/gIB in either the compute instance or the container image.

The `nccl-gib` package is bundled with an unmodified NVidia NCCL library (`libnccl2.so`) and headers. All NCCL/gIB content is installed to the `/usr/local/gib` directory, and the plugin libraries are also installed into system folder (under `/usr/lib`). Some dependencies are also fetched through the distribution's repositories.

### Debian 12+/Ubuntu 20.04+ (.deb package)
    
    
    # If on an image not from Google, trust the Google Cloud signing key
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/cloud.google.gpg
    
    # Add gpudirect-gib-apt repo
    echo 'deb https://packages.cloud.google.com/apt gpudirect-gib-apt main' | sudo tee /etc/apt/sources.list.d/nccl-gib.list
    
    sudo apt update
    sudo apt install nccl-gib

### RockyLinux/CentOS/RHEL 9+ (.rpm package)
    
    
    # Add gpudirect-gib-rpm repo
    sudo tee -a /etc/yum.repos.d/nccl-gib.repo << EOL
    [gpudirect-gib-rpm]
    name=NCCL/gIB
    baseurl=https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm
    enabled=1
    repo_gpgcheck=0
    gpgcheck=0
    
    sudo dnf makecache
    sudo dnf install nccl-gib

## Install NCCL plugins

To install only the gIB NCCL plugins (without the bundled NCCL library), install the `nccl-gib-plugins` package. If you're using the version of NCCL that comes with gIB, you don't need to install the package separately. However, if you're supplying your own custom version of NCCL, then you must use this option to install the plugins.

### Debian 12+/Ubuntu 20.04+ (.deb package)
    
    
    # If on an image not from Google, trust the Google Cloud signing key
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/cloud.google.gpg
    
    # Add gpudirect-gib-apt repo
    echo 'deb https://packages.cloud.google.com/apt gpudirect-gib-apt main' | sudo tee /etc/apt/sources.list.d/nccl-gib.list
    
    sudo apt update
    sudo apt install nccl-gib-plugins

### RockyLinux/CentOS/RHEL 9+ (.rpm package)
    
    
    # Add gpudirect-gib-rpm repo
    sudo tee -a /etc/yum.repos.d/nccl-gib.repo << EOL
    [gpudirect-gib-rpm]
    name=NCCL/gIB
    baseurl=https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm
    enabled=1
    repo_gpgcheck=0
    gpgcheck=0
    
    sudo dnf makecache
    sudo dnf install nccl-gib-plugins

**Note:** When you use `nccl-gib-plugins`, you must ensure that your separately installed NCCL version is compatible. For more information, see [Check NCCL and gIB version](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand#check_version).

If you are using standard OS images, you must also install the latest [NVIDIA DOCA-OFED driver](https://developer.nvidia.com/doca-downloads?deployment_platform=Host-Server&deployment_package=DOCA-Host&target_os=Linux&Architecture=x86_64&Profile=doca-ofed). You don't need to install this driver if you are using Google's accelerator optimized images, such as [Container OS](https://docs.cloud.google.com/container-optimized-os/docs) or [accelerator optimized Ubuntu or Rocky Linux OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images).

To avoid compute instances running different versions of the NCCL/gIB package, we recommend that you update NCCL/gIB before you run your NCCL workloads or disable automatic package updates, for example `unattended-upgrades` on Ubuntu or Debian.

## Enable NCCL/gIB

Starting from NCCL/gIB v1.1.2, if you installed `nccl-gib` or `nccl-gib-plugins`, NCCL/gIB should be automatically enabled in your workloads.

In previous versions, to enable NCCL/gIB in your workloads, ensure the following:

  * `/usr/local/gib/scripts/set_nccl_env.sh` is sourced in your runtime environment. The source file includes all the necessary environment variables for NCCL/gIB and Google expects to update them in future NCCL/gIB releases.
  * The `/usr/local/gib/lib64` directory is in your `LD_LIBRARY_PATH`.



To verify NCCL/gIB is enabled, check that the following NCCL INFO level log entries are present:
    
    
    # A sample log entry from NCCL core
    vm-0:606:642 [6] NCCL INFO Using network gIB
    
    # A sample log entry from the gIB network plugin
    vm-0:606:642 [6] NCCL INFO NET/gIB : Initializing gIB v1.1.2
    

## What's next

  * [Use gIB NCCL plugins in NVIDIA NGC containers](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/ngc-containers).
  * [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms).
  * [Collect and understand NCCL Logs for troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
