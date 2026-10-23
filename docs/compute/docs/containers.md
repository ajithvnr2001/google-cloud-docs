---
url: https://docs.cloud.google.com/compute/docs/containers/
title: Containers on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:55.225875+00:00
---

# Containers on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Containers on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Software containers are a convenient way to run your apps in multiple isolated user-space instances. You can run containers on Linux or Windows Server [public VM images](https://docs.cloud.google.com/compute/docs/images#os-compute-support), or on a [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) image. Containers let your apps run with fewer dependencies on the host virtual machine (VM) and run independently from other containerized apps that you deploy to the same VM instance. These characteristics make containerized apps more portable, easier to deploy, and easier to maintain at scale.

This document describes some of the more common container technologies that you can use to run containers on Compute Engine instances. You can use these technologies on most of the [public VM images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that Compute Engine provides.

Run containers on Compute Engine when you need complete control over your container environment and your container orchestration tools.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

Alternatively, you can use [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) to simplify cluster management and container orchestration tasks so that you don't need to manage the underlying VM instances. GKE provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure.

The GKE environment consists of multiple machines (specifically, [Compute Engine](https://docs.cloud.google.com/compute) instances) grouped together to form a [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). When you run a GKE cluster, you gain the benefit of advanced cluster management features such as load-balancing, node pools, node auto-repair, automatic scaling and upgrades, and logging and monitoring that Google Cloud provides.

Learn how to [create a GKE cluster with node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) running Microsoft Windows Server.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

## Container technologies that run on Compute Engine

In general, Compute Engine instances can run almost any container technology or tool. You can run several different types of containers on modern Linux operating systems. You can also run Docker on Windows Server 2016 or later. The following list includes several common tools that you can use to run and manage containerized apps:

  * [Docker](https://docs.docker.com/) and [Podman](https://podman.io/) are two popular container technologies that let you run containerized apps.
  * [Kubernetes](https://kubernetes.io/) is a container orchestration platform that you can use to manage and scale your running containers across multiple instances or within a hybrid-cloud environment.
  * [Containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) provide an easy way to deploy containers to Compute Engine VM instances or [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * You can convert your existing systems into [LXD images](https://www.ubuntu.com/cloud/lxd) and run them within Compute Engine VM instances for a lift-and-shift migration solution. LXD runs on Ubuntu images.



Additionally, you can use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to manage container image versions. Artifact Registry serves as a central location to store and manage your container images before you deploy those images to Kubernetes on Compute Engine or to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) clusters.

## Container-optimized VM images

Compute Engine provides several [public VM images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that you can use to create instances and run your container workloads. Some of these public VM images have a minimalistic container-optimized operating system that includes newer versions of Docker, Podman, or Kubernetes preinstalled. The following public image families are designed specifically to run containers:

  * [Container-Optimized OS from Google](https://docs.cloud.google.com/container-optimized-os/docs)
    * Includes: Docker, Kubernetes
    * Image project: `cos-cloud`
    * Image family: `cos-stable`
  * [Fedora CoreOS](https://getfedora.org/en/coreos/)
    * Includes: Podman, Docker
    * Image project: `fedora-coreos-cloud`
    * Image family: `fedora-coreos-stable`
  * [Ubuntu](https://www.ubuntu.com/)
    * Includes: LXD
    * Image project: `ubuntu-os-cloud`
    * Image family: `ubuntu-2004-lts`



If you need to run specific container tools and technologies on images that do not include them by default, install those technologies manually.

## Installing container technologies on your instances

To launch a single container on an instance, you can specify a container image when you [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#from-container-image). Compute Engine automatically supplies an up-to-date Container-Optimized OS image with Docker installed and launches your container when the VM starts up. For more information, see [Deploying containers on VMs ](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

Alternatively, you can run your container workloads on Compute Engine using whatever container technologies and orchestration tools that you need. You can [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) from a [public VM image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) and then install the container technologies that you want. For example:

  * Install Docker on Compute Engine instances so that you can run your Docker container images on those instances. 
    * [Install Docker on Linux instances](https://docs.docker.com/engine/installation/linux/)
    * Install Docker on Windows Server instances
  * [Install Podman](https://podman.io/) on Compute Engine instances as an alternative to the Docker container runtime.
  * [Install Kubernetes](https://kubernetes.io/docs/getting-started-guides/kubeadm/) on your instances to provide container orchestration for both Docker and Open Container Initiative (OCI) containers.



In some situations, you might require specific versions of these technologies to ensure that they operate together correctly. For example, Kubernetes usually runs best with specific versions of Docker. Typically, you can install the latest versions of these technologies for the best result.

## Installing Docker on Windows Server images

Windows Server 2016 and later versions include container support. If you plan to run Docker containers on a Windows Server instance, you can either install Docker on a Windows Server base image or use marketplace images [from Mirantis](https://www.mirantis.com/blog/mirantis-container-runtime-for-windows-server-is-now-available-on-google-cloud-marketplace).

If you want to install Docker CE on the Windows Server base image, then follow the steps outlined below.

Start by [creating a Windows Server instance](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances) using a Windows Server 2019 or later [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). For the best container support, we recommend that you use the most recent LTSC version of [Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server). For more information about LTSC, see [Windows Server servicing channels](https://docs.microsoft.com/en-us/windows-server/get-started/servicing-channels-comparison).

### Install Docker

Install Docker on Windows. For more information, see [Prep Windows for containers](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce). Restart the instance after the installation is complete.

### Additional setup steps

At this point you can use Docker to run containers in the instance. For example, the following command downloads the Windows `nanoserver` container image and runs a command prompt inside a `nanoserver` container:
    
    
    PS C:\> docker run -it mcr.microsoft.com/windows/nanoserver:1809 cmd.exe
    

**Note:** VPC networks have a default [maximum transmission unit (MTU)](https://www.wikipedia.org/wiki/Maximum_transmission_unit) of `1460` bytes. However, the network MTU can be set to the standard Ethernet MTU of `1500` bytes, up to `8896` bytes for jumbo frames, or as low as `1300`. For more information about network MTUs, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu). 

Docker's default network MTU is 1500 bytes. If you have configured your VPC network MTU to 1500 bytes as well, you can ignore the rest of this section. However, if you are using the default VPC MTU of 1460 bytes in your network, you have to do some additional configuration on each instance.

Set the MTU for all network interfaces (both Ethernet and vEthernet) to `1460` by running the following commands in a PowerShell terminal on each instance:
    
    
    PS C:\> Get-NetAdapter | Where-Object Name -like "*Ethernet*" | ForEach-Object {
      & netsh interface ipv4 set subinterface $_.InterfaceIndex mtu=1460 store=persistent
    }
    
    
    
    PS C:\> netsh interface ipv4 show subinterfaces
       MTU  MediaSenseState   Bytes In  Bytes Out  Interface
    ------  ---------------  ---------  ---------  -------------
    4294967295            1          0          0  Loopback Pseudo-Interface 1
      1460                1     306804     668688  Ethernet
      1460                1          0       1282  vEthernet (nat)
    

Even after changing the instance's MTU, connectivity from containers to the internet might be unstable because, by default, the container's network interface also uses an MTU of `1500`. For commands to set the MTU correctly for every container, see the container MTU section.

You might need to periodically re-execute these MTU commands as you configure Docker networking. For full details, see the known issues section.

## Running Windows containers

There are many resources available for getting started with Windows containers:

  * Microsoft provides extensive [Windows containers documentation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/).
  * [Docker Hub](https://hub.docker.com/) can be used as a repository for storing and pulling Windows containers.

**Note:** As of November 1, 2020, Docker Hub [ rate limits](https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/) apply to unauthenticated or authenticated pull requests on the Docker Free plan. To avoid disruptions and have greater control over your software supply chain, you can migrate your dependencies to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).




### Known issues with Windows containers

#### Deprecation of Windows Server 2019 for Containers images

Google offered a Windows Server image family with the Mirantis Container Runtime (previously Docker EE) pre-installed:

  * [Windows](https://www.microsoft.com/)
    * Includes: Docker
    * Image project: `windows-cloud`
    * Image family: `windows-2019-core-for-containers`



In early 2023, Microsoft ceased [distributing and supporting](https://techcommunity.microsoft.com/t5/containers/reminder-updates-to-windows-container-runtime-support/ba-p/3620989) the Mirantis Container Runtime for Windows Server. While Google was able to continue publishing this image family until October 30, 2023, the image family is now deprecated, and all images within the family have been marked obsolete.

Virtual machines based on these images created prior to October 30, 2023 will continue to run without interruption. However, instance creation for new instances based on these images will fail after that date.

Custom images derived from these images prior to October 30, 2023 will continue to function. However, custom images will not automatically receive any Patch Tuesday Windows updates, nor will they receive updated versions of the Mirantis Container Runtime.

If you want to continue using images with the Mirantis Container Runtime pre-installed, [Mirantis Inc offers images](https://www.mirantis.com/blog/mirantis-container-runtime-for-windows-server-is-now-available-on-google-cloud-marketplace) on Google Cloud Marketplace. The cost of these VM images includes support and licensing for Mirantis Container Runtime directly from Mirantis. Customers interested in using the standalone Mirantis Container Runtime can also download it directly from the Mirantis website.

If you want to migrate to an alternative container runtime like Docker CE, please follow the instructions above.

#### Containers are incompatible across Windows versions

Containers built on earlier versions of Windows don't work in Compute Engine instances running more recent versions of Windows. Docker pulls the Windows Server 2019 version of a container by default. This means that running the following command in an instance running Windows Server version 1709 or newer results in an error:
    
    
    PS C:\> docker run -it mcr.microsoft.com/windows/nanoserver cmd.exe
    docker: Error response from daemon: container
    9a1eb8bbcba4e91792be65f3c40b5a1aee062f02fbc60a78444b47d043438069 encountered an
    error during CreateContainer: failure in a Windows system call: The operating
    system of the container does not match the operating system of the host.
    (0xc0370101)
    

Microsoft's [Windows container version compatibility](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility) page contains more information. To work around Windows container version incompatibilities, specify the tag corresponding to your Windows version when pulling and running containers. For example, in a Windows Server, version 20H2 instance, use the following command to run a command prompt in the version 20H2 `nanoserver` container instead of the default 2019 LTSC (1809) container:
    
    
    PS C:\> docker run -it mcr.microsoft.com/windows/nanoserver:1809 cmd.exe
    

#### MTU incompatibilities affect instance and container connectivity

When you create a container network on a Windows instance using the `docker network create` or `New-VMSwitch` commands, the MTU of the instance's network interface is typically [forced to `1500`](https://github.com/Microsoft/SDN/issues/84). The default network interface inside of a new Docker container also typically [uses an MTU of `1500`](https://github.com/moby/moby/issues/35683). If your VPC network has an MTU of `1460`, you might experience the following issues:

  * The RDP session can stop and you might be unable to reconnect. This is known to happen when creating a [transparent container network](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/network-drivers-topologies).

  * DNS resolution inside the container might fail.

  * DNS resolution is successful, but establishing an HTTP connection from the container to the internet might fail.




The recommended workaround for these limitations requires two steps: setting the MTU for the instance's network interfaces to `1460` and setting the MTU for the container network interfaces to `1460`. Alternatively, you can [set the MTU for the VPC](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network) to `1500`, but this requires stopping or migrating all of your VMs.

##### 1\. Setting the MTU for the Windows instance's network interfaces

Run the following command in a PowerShell terminal on the Windows instance to set the MTU for all network interfaces (both Ethernet and vEthernet):
    
    
    PS C:\> Get-NetAdapter | Where-Object Name -like "*Ethernet*" | ForEach-Object {
      & netsh interface ipv4 set subinterface $_.InterfaceIndex mtu=1460 store=persistent
    }
    

Check that the instance's Ethernet and vEthernet interface MTUs are set to `1460` using this command:
    
    
    PS C:\> netsh interface ipv4 show subinterfaces
       MTU  MediaSenseState   Bytes In  Bytes Out  Interface
    ------  ---------------  ---------  ---------  -------------
    4294967295            1          0          0  Loopback Pseudo-Interface 1
      1460                1  628295912    2613170  Ethernet
      1460                1      37793     223909  vEthernet (nat)
    

If you are unable to run these commands because you can no longer connect to an instance by using RDP, you can [connect to the instance through the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console), start a `cmd` prompt and run the `netsh` commands there to repair the MTU. To avoid having to do this, we recommend executing any `docker network ...` or `New-VMSwitch` commands as part of a script that also executes the MTU repair command.

##### 2\. Setting the MTU for the Windows container network interfaces

The MTU for a Windows container must be set while the container is running, either from inside the container or from the instance hosting the container. If PowerShell is available in your container, you can run this command interactively or from a script in the container to correctly set the MTU:
    
    
    PS C:\> Get-NetAdapter | Where-Object Name -like "vEthernet*" | ForEach-Object {
      & netsh interface ipv4 set subinterface $_.InterfaceIndex mtu=1460 store=persistent
    }
    

Or, you can run this command on the Windows instance to set the MTU for all running containers:
    
    
    PS C:\> Get-NetIPInterface -IncludeAllCompartments |
      Where-Object InterfaceAlias -like "vEthernet*" |
      Set-NetIPInterface -IncludeAllCompartments -NlMtuBytes 1460
    

#### Hyper-V containers fail to start

[Hyper-V containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container) are not supported on Compute Engine at this time.

## What's next

  * [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) that you can use to run container applications.
  * Learn about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).
  * Learn more about [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine), which you can use to run your containers on Google Cloud without managing Compute Engine instances yourself.
  * Learn more about [Kubernetes](https://kubernetes.io/).
  * Learn how to use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to store your container images privately within Google Cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
