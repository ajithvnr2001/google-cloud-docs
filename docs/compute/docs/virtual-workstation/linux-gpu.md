---
url: https://docs.cloud.google.com/compute/docs/virtual-workstation/linux-gpu/
title: Create a virtual GPU-accelerated Linux workstation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:02.249991+00:00
---

# Create a virtual GPU-accelerated Linux workstation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/virtual-workstation/linux-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a virtual GPU-accelerated Linux workstation Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to create a virtual Linux workstation running Ubuntu 22.04 with an attached display-capable [GPU](https://docs.cloud.google.com/compute/docs/gpus). Google Cloud offers three display-capable GPUs: NVIDIA L4, NVIDIA T4, and NVIDIA P4.

To create a Windows workstation, see the tutorial for [Creating a virtual GPU accelerated Windows workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation/windows-gpu).

**Note:** This tutorial helps you create a virtual workstation that can take advantage of hardware graphics acceleration. For information about other types of virtual workstations that you can create on Google Cloud, see [Creating a virtual workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation).

After you create the virtual workstation, you learn how to remotely access it using [HP Anyware](https://anyware.hp.com/) (formerly Teradici CAS), using [PC-over-IP (PCoIP®)](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA8-3293ENW) technology, a remote desktop protocol widely used in the media and entertainment, game development, architecture, and engineering industries. PCoIP offers features essential to these types of workloads, such as color accuracy, support for multiple monitors, lossless display, and tablet pressure sensitivity.

This tutorial assumes you are familiar with the Linux command line.

## Objectives

  * Create a Compute Engine instance with a GPU. This instance serves as the foundation for a virtual workstation.
  * Install NVIDIA drivers on the virtual workstation.
  * Install HP Anyware software on the virtual workstation.
  * Connect to the virtual workstation using a PCoIP software client.

**Note:** This tutorial does not include advanced security features such as fine-grained SSH key management, certificate issuance, or multi-factor authentication (MFA). A full deployment requires a [connection broker](https://wikipedia.org/wiki/Connection_broker) and [domain controller](https://wikipedia.org/wiki/Domain_controller_\(Windows\)), which help enable a stronger security profile for connecting to virtual workstations.

## Costs

This tutorial uses the following billable component of Google Cloud:

  * [Compute Engine](https://cloud.google.com/compute/all-pricing)



You can use the [pricing calculator](https://cloud.google.com/products/calculator/estimate-preview/CiQ5YTYwNWVjNC04NTI3LTQ5MzgtOTk5Ni05ZThhN2UxMGQ0M2IQAQ==) to generate a cost estimate based on your projected usage.

The resources that make up the virtual workstation and the factors that affect cost in this tutorial are:

  * 8 vCPUs, 32 GB RAM [G2 standard machine type](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized) which includes an [NVIDIA L4 Virtual Workstation GPU](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).
  * 100 GB SSD [persistent boot disk](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk)
  * [Internet outbound data transfer costs](https://docs.cloud.google.com/vpc/network-pricing#internet_egress)



Internet data transfer represents data that streams from your virtual workstation to your local display client and is billed at [internet outbound data transfer costs](https://docs.cloud.google.com/vpc/network-pricing#internet_egress). Variables that affect data transfer during a PCoIP session are bandwidth, screen resolution, number of display monitors, applications used, and the type of activity on each monitor. The HP Anyware [Session Planning Guide](https://anyware.hp.com/products/hp-anyware/2025.03/documentation/session-planning-guide) can help you understand different workload requirements.

**Note:** Costs differ depending on region and connection method. These estimated costs are based on connection over the public internet, with resources located in the `us-central1` region (Iowa).

## Before you begin

This tutorial uses the Google Cloud CLI, which you can run from a [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) instance launched from the [](https://console.cloud.google.com/)[Google Cloud console](https://console.cloud.google.com/). If you want to use gcloud CLI on your local workstation, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). The tutorial shows you how to run commands in Cloud Shell; if you use the gcloud CLI on your workstation, adjust the instructions accordingly.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




In addition, make sure you have the following:

  * A Google Cloud project with quota for [NVIDIA L4 Virtual Workstation GPUs](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) in your selected [zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones). You can get a listing of GPU availability using the `gcloud compute accelerator-types list` command.
  * A [Google Chrome](https://www.google.com/chrome/) browser to access the Google Cloud console.
  * The latest [PCoIP Client software](https://anyware.hp.com/find/product/hp-anyware) for Windows, Mac, or Linux to access the virtual workstation.
  * An account on [help.teradici.com](https://help.teradici.com/) to download the HP Anyware software. Account registration is free.
  * An HP Anyware software license. You can [request a trial license](https://reinvent.hp.com/Anyware-Demo), or contact your HP representative and ask for a trial registration code to use for this virtual workstation.



## Architecture

The following diagram shows the components used in this tutorial to deploy a single virtual workstation. Optional components shown in the diagram include different ways to connect to your virtual workstation, shared storage, an additional instance for serving third-party licenses, and additional infrastructure representing a render or compute farm.

![Virtual workstation architecture.](https://docs.cloud.google.com/static/compute/docs/virtual-workstation/img/creating-a-virtual-gpu-accelerated-workstation-architecture.svg)

## Choose a region

An important factor when you deploy a virtual workstation is the latency between your location and the instance you create. The lower the latency, the better the experience. Therefore, you want to work in a region that's geographically closest to you. To learn more about where the different GPUs are available, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  1. Open Cloud Shell. (If you're using the gcloud CLI, open a terminal window on your computer.)

[Go to Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Get a list of the zones in which GPUs are available:
         
         gcloud compute accelerator-types list

Take note of the region and zone that's physically closest to you.

  3. Set the zone that you want to work with:
         
         gcloud config set compute/zone ZONE

Replace `ZONE` with the name of the [zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) you're using, such as `us-west1-b`.




## Choose a machine type

NVIDIA L4 GPUs are attached to the [G2 machine type](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized). Virtual machines with one or more GPUs have a maximum number of vCPUs for each GPU you add to the instance. For example, each NVIDIA L4 GPU lets you have up to 32 vCPUs and up to 128 GB of memory in your instance machine type. To see the available vCPU and memory ranges for different GPU configurations, see the [GPUs list](https://docs.cloud.google.com/compute/docs/gpus).

The example in this tutorial consists of an 8 vCPU G2 virtual workstation, which is well under the limit of 32 vCPUs for a single NVIDIA L4 GPU.

## Create the virtual workstation

**Note:** There are some [restrictions](https://docs.cloud.google.com/compute/docs/gpus#restrictions) to keep in mind when creating a virtual workstation with attached GPUs. Restrictions that apply to this tutorial have been addressed, but it's a good idea to familiarize yourself with these restrictions before you create your virtual workstation.

  1. In Cloud Shell, create the Compute Engine virtual workstation instance:
         
         gcloud compute instances create VM_NAME \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=ACCELERATOR,count=NUM-GPUS \
             --maintenance-policy="TERMINATE" \
             --image-project=ubuntu-os-cloud \
             --image-family=ubuntu-2204-lts \
             --boot-disk-size=SIZE \
             --boot-disk-type=TYPE \
             --network=NETWORK
         

Replace the following:

     * `VM_NAME` is the name of your workstation.
     * `ZONE` is the zone in which to create the VM.
     * `MACHINE_TYPE` is the predefined or custom machine configuration.
     * `ACCELERATOR` is the type of GPU you want to attach, such as `nvidia-l4-vws`.
     * `NUM-GPUS` is the number of GPUs to attach to the VM.
     * `SIZE` is the size of the boot disk, in gigabytes.
     * `TYPE` is the type of boot disk. To get a list of available disk types, run `gcloud compute disk-types list`.
     * `NETWORK` is the network in which to create the VM.

For example:
    
    gcloud compute instances create test-workstation \
        --zone=us-west1-b \
        --machine-type=g2-standard-8 \
        --accelerator=type=nvidia-l4-vws,count=1 \
        --maintenance-policy="TERMINATE" \
        --image-project=ubuntu-os-cloud \
        --image-family=ubuntu-2204-lts \
        --boot-disk-size=100 \
        --boot-disk-type=pd-ssd \
        --network=default
    

After the virtual workstation is created, the machine status is displayed. The output looks similar to the following:
    
    NAME: test-workstation
    ZONE: us-west1-b
    MACHINE_TYPE: g2-standard-8
    PREEMPTIBLE:
    INTERNAL_IP: 10.138.XX.XXX
    EXTERNAL_IP: XX.XXX.XXX.XXX
    STATUS: RUNNING
    

Note the virtual workstation's external IP address. You will use it later in the tutorial.

You can retrieve the external IP address of your virtual workstation at any time using the [Google Cloud console](https://console.cloud.google.com/compute/instances).




## Sign in to your virtual workstation

After you create the virtual workstation, you sign in to the machine so that you can configure it.

  1. In Cloud Shell, connect to the new virtual workstation:
         
         gcloud compute ssh VM_NAME

  2. Set your account password. Logging into a virtual workstation using the PCoIP software client requires a user password.
         
         sudo passwd `whoami`

When you're prompted, enter a password. You will use this password later in the tutorial to log on to your virtual workstation with the HP Anyware PCoIP Client.




## Install the base libraries

The default Google Cloud Ubuntu 22.04 image is a minimal installation of Ubuntu. The next step is to install libraries that are necessary to run your virtual workstation as a graphics workstation.

  1. Update the software repositories:
         
         sudo apt update

  2. Install the base components:
         
         sudo apt install -y build-essential
         sudo apt install -y libvulkan1
         

  3. Update the `gcc` version for the NVIDIA driver:
         
         sudo apt install -y gcc-12
         sudo apt install -y linux-headers-$(uname -r)
         sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
         sudo update-alternatives --config gcc
         




## Install the NVIDIA driver

NVIDIA L4, NVIDIA T4, and NVIDIA P4 GPUs work on Google Cloud only with qualified NVIDIA RTX Virtual Workstation drivers for visualization workloads. These drivers can be downloaded from a public Google Cloud storage bucket.

  1. To install the latest NVIDIA RTX Virtual Workstation driver, follow the [instructions (Steps 3 and 4, only)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers#debianubuntu).

  2. Reboot the workstation:
         
         sudo reboot




## Install the desktop environment

A desktop environment is necessary to run your virtual workstation as a graphics workstation. For this tutorial, you install the KDE Plasma Desktop.

  1. Install the desktop environment:
         
         sudo apt update
         sudo apt -y install kubuntu-desktop
         sudo apt -y install dialog
         

  2. Reboot the workstation:
         
         sudo reboot




## Install HP Anyware software

HP Anyware software provides a graphics agent that runs on your virtual workstation, delivering the desktop to your hardware or software client.

**Note:** Installation may differ if you choose a different Linux distribution. For more information, see [HP Anyware Graphics Agent for Linux Installation Guide](https://anyware.hp.com/components/graphics-agent-for-linux/current/documentation/administrators-guide).

  1. When the virtual workstation has restarted, in Cloud Shell, reconnect to the virtual workstation:
         
         gcloud compute ssh VM_NAME

  2. Add the Teradici software repository:
         
         curl -1sLf \
             https://dl.anyware.hp.com/TOKEN/pcoip-agent/cfg/setup/bash.deb.sh \
             | sudo -E distro=ubuntu codename=jammy bash
         

Replace the following:

     * `TOKEN` is the download token you can retrieve from the [HP Anyware Graphics Agent for Linux](https://anyware.hp.com/find/product/hp-anyware) page under **Downloads and scripts**.
  3. Update the software repositories:
         
         sudo apt update

  4. Optional: Install USB dependencies, if you need to support USB devices other than keyboards, mice, and pointer devices.

**Note:** If you skip this step, USB redirection is disabled. That means you can't use bridged USB devices.
         
         sudo apt -y install usb-vhci-dkms

  5. Install the HP Anyware software:
         
         sudo apt -y install pcoip-agent-graphics




## Register the Anyware Graphics Agent

To use the Anyware Graphics Agent, you must have an HP Anyware license.

  1. In Cloud Shell, activate your HP Anyware software license:
         
         pcoip-register-host --registration-code=REGISTRATION-CODE

Replace `REGISTRATION-CODE` with the code provided to you by HP Teradici in the form `ABCDEFGHIJKL@0123-4567-89AB-CDEF`.

  2. Reboot the virtual workstation:
         
         sudo reboot




## Create a firewall rule

The PCoIP client communicates with your virtual workstation using several ports. You must set firewall rules that allow traffic to your virtual workstation.

  * In Cloud Shell (not on the virtual workstation), create a firewall rule that opens the required ports:
        
        gcloud compute firewall-rules create allow-pcoip \
            --action=ALLOW \
            --rules=tcp:443,tcp:4172,udp:4172 \
            --source-ranges=0.0.0.0/0
        

**Note:** This firewall rule allows traffic from anywhere on the internet to access your VM instance. Always follow [best practices for firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#best_practices_for_firewall_rules) to restrict traffic to your instance.



## Sign in to your virtual workstation using the PCoIP client

  1. On your local computer, go to the **PCoIP Clients** section on the [HP Anyware support page](https://anyware.hp.com/find/product/hp-anyware), and then download, install, and launch the PCoIP Software Client application for your operating system.

  2. In the **Host Address or Registration Code** field, enter the external IP address of your virtual workstation. If you want, you can enter a name for the connection.

**Note:** By default, PCoIP traffic is encrypted using AES-256. However, HP Anyware Software uses a self-signed certificate that's issued by Teradici. This might trigger a verification warning when you connect. You can remove this warning by creating and installing your own [custom security certificates](https://anyware.hp.com/components/graphics-agent-for-linux/current/documentation/administrators-guide/security-guide#using_custom_security_certificates). Or, you can suppress the warning by changing the [client security mode](https://anyware.hp.com/components/software-client-for-macos/current/documentation/administrators-guide/security-guide/security-modes) for your client OS. For the purposes of this tutorial, you can ignore this warning by clicking **Connect Insecurely** in the dialog.
  3. When you are connected, authenticate by entering the username and password that you created earlier for the virtual workstation.

In a few seconds, your Linux desktop appears.




## Test your virtual workstation

After you've deployed your virtual workstation, you can test performance and interactivity using a number of tools:

  * Run GPU benchmark tools, such as [glxgears](https://wiki.archlinux.org/index.php/benchmarking#glxgears), [glmark2](https://github.com/glmark2/glmark2), or [UNIGINE](https://benchmark.unigine.com/), which are programs to test graphics performance on a Linux workstation.
  * Install [Unreal Engine](https://www.unrealengine.com/), [Unity Editor](https://unity3d.com/), [Blender](https://www.blender.org/), or any content creation application.
  * Run render benchmarking tools for popular renderers such as [V-Ray](https://www.chaos.com/vray/benchmark), [Octane](https://render.otoy.com/octanebench/), or [Maxon](https://www.maxon.net/cinebench).
  * Use [Google Chrome](https://www.google.com/chrome/) to browse your favorite sites or play [YouTube](https://www.youtube.com/) videos.



You can also learn more about [PCoIP performance optimization](https://anyware.hp.com/products/hp-anyware/current/documentation/session-planning-guide/pcoip-performance-optimization) based on your workload.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, clean up the resources you created on Google Cloud so you won't be billed for them in the future.

### Stop your virtual workstation

Stopped virtual workstations incur [costs for persistent disk](https://docs.cloud.google.com/persistent-disk), but can be restarted at any time. To stop your virtual workstation, run the following command in Cloud Shell:
    
    
    gcloud compute instances stop VM_NAME

### Delete all the components

  1. [Delete the virtual workstation](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#delete_an_instance).
  2. [Delete the firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#deleting_firewall_rules).



### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [create a virtual GPU-accelerated Windows workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation/windows-gpu).
  * Learn more about [NVIDIA RTX Virtual Workstations](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) on Google Cloud.
  * Learn more about [NVIDIA RTX Virtual Workstation technology](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/).
  * Learn more about [HP Anyware software](https://www.hp.com/us-en/services/workforce-solutions/workforce-computing/digital-workspaces.html).
  * Learn more about how [PCoIP](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA8-3293ENW) differs from other remote desktop software.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
