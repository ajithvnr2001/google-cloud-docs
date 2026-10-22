---
url: https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu/
title: Install GPU drivers \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:59.439454+00:00
---

# Install GPU drivers  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install GPU drivers Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

After you create a Compute Engine instance with one or more GPUs, your system requires NVIDIA device drivers so that your applications can access the device. Make sure your GPU instances have enough free disk space. You should choose at least 40 GB for the boot disk when creating the new GPU instance.

To install the drivers, you have two options to choose from:

  * If you need GPUs for hardware accelerated 3D graphics such as remote desktop or gaming, see [Install drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).

  * For other workloads, follow the instructions in this document to install the NVIDIA driver.

**Pro Tip:** Alternatively, you can skip this setup by creating compute instances that use images with drivers installed. See [Choosing an operating system](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system) for more information. 




## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## NVIDIA driver, CUDA toolkit, and CUDA runtime versions

There are different versioned components of drivers and runtime that might be needed in your environment. These include the following components:

  * NVIDIA driver
  * CUDA toolkit
  * CUDA runtime



When installing these components, you have the ability to configure your environment to suit your needs. For example, if you have an earlier version of TensorFlow that works best with an earlier version of the CUDA toolkit, but the GPU that you want to use requires a later version of the NVIDIA driver, then you can install an earlier version of a CUDA toolkit along with a later version of the NVIDIA driver.

However, you must make sure that your NVIDIA driver and CUDA toolkit versions are compatible. For CUDA toolkit and NVIDIA driver compatibility, see the NVIDIA documentation about [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver).

### Understand NVIDIA driver branches

NVIDIA provides the following three driver branches:

  * _Long-Term Support Branch (LTSB):_ this branch prioritizes stability and minimizes maintenance, with an extended support lifecycle of [three years](https://docs.nvidia.com/datacenter/tesla/drivers/driver-lifecycle.html#long-term-support-branch). The latest LTSB tested and verified by Google is **R580** , which has an end of support date in June 2028.
  * _Production Branch (PB):_ this branch provides performance enhancements and support for the latest hardware. It fully supports production workloads but has a shorter support lifecycle of [up to one year](https://docs.nvidia.com/datacenter/tesla/drivers/driver-lifecycle.html#production-branch). The latest PB tested and verified by Google is **R595** , which has a end of support in March 2027.
  * _New Feature Branch (NFB):_ this branch is for early adopters to test new features and is not recommended for production environments.



For production workloads, use either the Production Branch or the Long-Term Support Branch. For more details about the NVIDIA branches, see the [NVIDIA documentation](https://docs.nvidia.com/datacenter/tesla/drivers/index.html#comparison-of-driver-branches).

### Recommended NVIDIA driver branches

Use the table in this section to help you to determine the best NVIDIA driver branch for your GPU machine type.

**Important:** **Supported branches** are provided per [NVIDIA documentation](https://docs.nvidia.com/datacenter/tesla/drivers/cuda-toolkit-driver-and-architecture-matrix.html). However, the **Recommended branch** is tested and verified to work on Compute Engine, provides the longest support window, and requires the least maintenance. The **Recommended branch** is typically a long-term support branch, unless the machine type requires a more recent production branch.

In the following table, `N/A` indicates that the specified operating system (OS) can't run on the machine type.

**Machine type** | **GPU model** | **Supported branches (Per NVIDIA)** | **Recommended branch  
(EOS date)** | **Minimum driver for recommended branch**  
---|---|---|---|---  
A4X Max | NVIDIA Blackwell GB300 Superchip | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: N/A

  
A4X | NVIDIA Blackwell GB200 Superchip | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: N/A

  
A4 | NVIDIA Blackwell B200 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: N/A

  
A3 Ultra | NVIDIA H200 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: N/A

  
A3 Mega, High, Edge | NVIDIA H100 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: N/A

  
G4 | NVIDIA RTX PRO 6000 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: `581.42` or later

  
G4 (fractional GPU) | NVIDIA RTX PRO 6000 | R580 or later | R580 (June 2028) | 

  * Linux: `580.126.09` or later
  * Windows: `582.16` or later

  
G2 | NVIDIA L4 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: `581.42` or later

  
A2 Standard, A2 Ultra | NVIDIA A100 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: `581.42` or later

  
N1 | NVIDIA T4 | R580 or later | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: `581.42` or later

  
N1 | NVIDIA V100, P4 | R5801 | R580 (June 2028) | 

  * Linux: `580.95.05` or later
  * Windows: `581.42` or later

  
  
1NVIDIA announced that R580 is the last driver branch to support the Pascal (P4) and Volta architecture (V100). 

## Install GPU drivers on compute instances by using CUDA Toolkit guides

One way to install the NVIDIA driver on most compute instances is to install the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive).

**Note:** With the exception of Windows, these instructions don't work on compute instances that have [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) enabled. For compute instances that have Secure Boot enabled, see Installing GPU drivers (Secure Boot VMs).

To install the CUDA Toolkit, complete the following steps:

  1. Select a CUDA Toolkit version that supports the driver version that you need.

**Machine type** | **GPU model** | **Recommended CUDA Toolkit**  
---|---|---  
A4X Max | NVIDIA Blackwell GB300 Superchip | CUDA 13.0 or later  
A4X | NVIDIA Blackwell GB200 Superchip | CUDA 13.0 or later  
A4 | NVIDIA Blackwell B200 | CUDA 13.0 or later  
A3 Ultra | NVIDIA H200 | CUDA 13.0 or later  
G4 | NVIDIA RTX PRO 6000 | CUDA 13.1 or later  
G2 | NVIDIA L4 | CUDA 13.0 or later  
A3 Mega, High, Edge | NVIDIA H100 | CUDA 13.0 or later  
A2 Standard, A2 Ultra | NVIDIA A100 | CUDA 13.0 or later  
N1 | NVIDIA T4 | CUDA 13.0 or later  
N1 | NVIDIA V100, P4 | CUDA 12.2.2 to CUDA 12 (final version)1  
  
1CUDA Toolkit 12 is the last to support the Pascal (P4) and Volta architecture (V100). NVIDIA announced that offline compilation and library support for these architectures is removed starting with the CUDA Toolkit 13.0 major version release. For more information, see the [NVIDIA 13.0 driver release notes](https://docs.nvidia.com/cuda/archive/13.0.0/cuda-toolkit-release-notes/index.html#deprecated-architectures). 

  2. [Connect to the GPU instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) where you want to install the driver.

  3. On your GPU instance, download and install the CUDA Toolkit. To find the CUDA Toolkit package and installation instructions, see [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) in the NVIDIA documentation.




## Install GPU drivers on compute instances by using installation script

You can use the following scripts to automate the installation process. To review these scripts, see the [GitHub repository](https://github.com/GoogleCloudPlatform/compute-gpu-installation).

**Note:** These scripts won't work on Linux compute instances that have [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) enabled. For Linux compute instances that have Secure Boot enabled, see Installing GPU drivers (Secure Boot VMs).

###  Linux 

Use these instructions to install GPU drivers on a running compute instance.

**Supported operating systems**

The Linux installation script was tested on the following operating systems:

  * Debian 12 and 13
  * Red Hat Enterprise Linux (RHEL) 8, 9 and 10
  * Rocky Linux 8, 9 and 10
  * Ubuntu 22, 24 and 26



If you use this script on other operating systems, the installation might fail. This script can install NVIDIA driver as well as [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

To install the GPU drivers and CUDA Toolkit, complete the following steps:

  1. If you have version 2.38.0 or later of the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index) collecting GPU metrics on your compute instance, you must stop the agent before you can install or upgrade your GPU drivers using this installation script.

To stop the Ops Agent, run the following command:
         
         sudo systemctl stop google-cloud-ops-agent

  2. Ensure that Python 3 is installed on your operating system.

  3. Download the installation script.
         
         curl -L https://storage.googleapis.com/compute-gpu-installation-us/installer/latest/cuda_installer.pyz --output cuda_installer.pyz

  4. Run the installation script.
         
         sudo python3 cuda_installer.pyz install_driver --installation-mode=INSTALLATION_MODE --installation-branch=BRANCH

Replace the following:

     * `INSTALLATION_MODE`: the installation method. Use one of the following values: 
       * `repo`: (Default) installs the driver from the official NVIDIA package repository. We recommend this mode for compute instances managed by automated OS patching tools because Dynamic Kernel Module Support (DKMS) automatically rebuilds the driver when you update the kernel.
       * `binary`: installs the driver by using the standalone NVIDIA `.run` installer and locks guest OS kernel meta-packages (`apt-mark hold` on Ubuntu and Debian, or `exclude=kernel*` in `/etc/dnf/dnf.conf` on Red Hat Enterprise Linux (RHEL) and Rocky Linux) to prevent unintended kernel updates from breaking the driver. The installer automatically uses `binary` mode when you specify `--installation-branch=lts` or `--force-version`, or when you install the driver on an NVIDIA RTX Virtual Workstation (vWS) compute instance.
     * `BRANCH`: the driver branch that you want to install. Use one of the following values: 
       * `prod`: (Default) the production branch. This branch is qualified for use in production environments for enterprise and data center GPUs.
       * `nfb`: the new feature branch. This branch includes the latest updates for early adopters. We don't recommend this branch for production environments.
       * `lts`: the long-term support branch, which uses `binary` installation mode. NVIDIA maintains this branch for a longer period than a standard production branch.

**Caution:** Enterprise patch management tools, such as OS Config, BigFix, or Ansible, might install explicit versioned kernel packages. These updates can bypass kernel holds from `binary` mode without installing matching kernel headers, which causes the driver to fail after a reboot. If your fleet uses automated patching, then use `repo` mode or configure your patching workflow to install matching kernel headers, such as `linux-headers-$(uname -r)` or `kernel-devel-$(uname -r)`. For recovery steps, see [Troubleshoot `nvidia-smi` failure after OS patching or kernel upgrade](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#troubleshoot-kernel-mismatch).

To see specific versions of the driver available for installation, run the following command:
    
    python3 cuda_installer.pyz list_driver_versions

To install a specific version of the driver, use the `--force-version` option.
    
    sudo python3 cuda_installer.pyz install_driver --force-version DRIVER_VERSION

Replace `DRIVER_VERSION` with the driver version that you want to install. 

The script takes several minutes to run. It might restart your compute instance. When the compute instance restarts, run the script again with the same parameters to continue the installation.

  5. Verify the installation. See Verify the GPU driver install.

  6. You can also use this tool to install the CUDA Toolkit. To install the CUDA Toolkit, run the following command:
         
         sudo python3 cuda_installer.pyz install_cuda --installation-mode=INSTALLATION_MODE --installation-branch=BRANCH

Make sure that you use the same values for INSTALLATION_MODE and BRANCH as you did during driver installation. 

The script takes several minutes to run. It might restart your compute instance. If the compute instance restarts, run the script again to continue the installation.

  7. Verify the CUDA toolkit installation.
         
         python3 cuda_installer.pyz verify_cuda

  8. After you complete the installation, you must reboot the compute instance.




###  Linux (startup script) 

Use these instructions to install GPU drivers during startup of a compute instance.

**Supported operating systems**

The Linux installation script was tested on the following operating systems:

  * Debian 12 and 13
  * Red Hat Enterprise Linux (RHEL) 8, 9 and 10
  * Rocky Linux 8, 9 and 10
  * Ubuntu 22, 24 and 26



If you use this script on other operating systems, the installation might fail. This script can install NVIDIA driver as well as [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

To automate the driver and CUDA Toolkit installation, use the following [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux):
    
    
    #!/bin/bash
    if test -f /opt/google/cuda-installer
    then
      exit
    fi
    
    mkdir -p /opt/google/cuda-installer
    cd /opt/google/cuda-installer/ || exit
    
    if test -f cuda_installation
    then
      exit
    fi
    
    curl -fSsL -O https://storage.googleapis.com/compute-gpu-installation-us/installer/latest/cuda_installer.pyz
    python3 cuda_installer.pyz install_driver
    # Or uncomment the line below to also install CUDA Toolkit
    # python3 cuda_installer.pyz install_cuda
    

To install only the driver without CUDA Toolkit, replace `install_cuda` in the last line of the script with `install_driver`.

You can append the `--installation-mode` INSTALLATION_MODE and `--installation-branch` BRANCH flags to the install command to indicate what installation mode and which driver branch you want installed.

Replace the following:

  * `INSTALLATION_MODE`: the installation method. Use one of the following values: 
    * `repo`: (Default) installs the driver from the official NVIDIA package repository. We recommend this mode for compute instances managed by automated OS patching tools because Dynamic Kernel Module Support (DKMS) automatically rebuilds the driver when you update the kernel.
    * `binary`: installs the driver by using the standalone NVIDIA `.run` installer and locks guest OS kernel meta-packages (`apt-mark hold` on Ubuntu and Debian, or `exclude=kernel*` in `/etc/dnf/dnf.conf` on Red Hat Enterprise Linux (RHEL) and Rocky Linux) to prevent unintended kernel updates from breaking the driver. The installer automatically uses `binary` mode when you specify `--installation-branch=lts` or `--force-version`, or when you install the driver on an NVIDIA RTX Virtual Workstation (vWS) compute instance.
  * `BRANCH`: the driver branch that you want to install. Use one of the following values: 
    * `prod`: (Default) the production branch. This branch is qualified for use in production environments for enterprise and data center GPUs.
    * `nfb`: the new feature branch. This branch includes the latest updates for early adopters. We don't recommend this branch for production environments.
    * `lts`: the long-term support branch, which uses `binary` installation mode. NVIDIA maintains this branch for a longer period than a standard production branch.



**Caution:** Enterprise patch management tools, such as OS Config, BigFix, or Ansible, might install explicit versioned kernel packages. These updates can bypass kernel holds from `binary` mode without installing matching kernel headers, which causes the driver to fail after a reboot. If your fleet uses automated patching, then use `repo` mode or configure your patching workflow to install matching kernel headers, such as `linux-headers-$(uname -r)` or `kernel-devel-$(uname -r)`. For recovery steps, see [Troubleshoot `nvidia-smi` failure after OS patching or kernel upgrade](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#troubleshoot-kernel-mismatch).

To see specific versions of the driver available for installation, run the following command:
    
    
    python3 cuda_installer.pyz list_driver_versions

To install a specific version of the driver, use the `--force-version` option.
    
    
    sudo python3 cuda_installer.pyz install_driver --force-version DRIVER_VERSION

Replace `DRIVER_VERSION` with the driver version that you want to install. 

###  Windows 

This installation script can be used on GPU instances that have secure boot enabled. It supports Windows Server 2019 and later.

This script installs an NVIDIA RTX Virtual Workstation (vWS) compatible driver. If you don't have a vWS license, vWS features won't be available on your instance.

Open a PowerShell terminal **as an administrator** , then complete the following steps:

  1. Download the script.
         
         Invoke-WebRequest https://github.com/GoogleCloudPlatform/compute-gpu-installation/raw/main/windows/install_gpu_driver.ps1 -OutFile C:\install_gpu_driver.ps1

  2. Run the script.
         
         C:\install_gpu_driver.ps1

The script takes several minutes to run. No command prompts are given during the installation process. After the script exits, the driver is installed.

This script installs the drivers in the following default location on your VM: `C:\Program Files\NVIDIA Corporation\`.

  3. Verify the installation. See [Verify the GPU driver install](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-driver-install).




###  Windows (automated) 

To automatically install GPU drivers on Windows machine first boot, set the `sysprep-specialize-script-url` metadata key for the new instance to `https://github.com/GoogleCloudPlatform/compute-gpu-installation/raw/main/windows/install_gpu_driver.ps1`.

For more information about using startup scripts on Windows machines, see [Use startup scripts on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows).

This script installs the drivers in the following default location on your VM: `C:\Program Files\NVIDIA Corporation\`.

## Install GPU drivers (Secure Boot VMs)

These instructions are for installing GPU drivers on Linux VMs that use [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).

You can't use these procedures to install drivers on Secure Boot instances that have [NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers) versions of our GPUs attached.

If you are using either a Windows VM or a Linux VM that doesn't use Secure Boot, review one of the following instructions instead:

  * [Install GPU drivers on VMs](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#no-secure-boot)
  * [Install GPU drivers by using installation script](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#install-script)



Installation of the driver on a Secure Boot VM is different for Linux VMs, because these VMs require all kernel modules to have a trusted certificate signature.

### GPU machine type support

The procedures in this section support [all GPU machine types](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads) that are available on Compute Engine.

### Installation

You can use one of the following options for installing drivers that have trusted certificates:

  * Create a trusted certificate for your drivers. For this option, choose from the following: 
    * Automated method: use an image building tool to create boot images that have trusted certificates for your drivers installed
    * Manual method: generate your own certificate and use it to sign the GPU driver's kernel modules
  * Use pre-signed drivers with an existing trusted certificate. This method only supports Ubuntu.




###  Self-signing (automated) 

**Supported operating systems:**

This automated self-signing method was tested on the following operating systems:

**Supported operating systems**

The Linux installation script was tested on the following operating systems:

  * Debian 12 and 13
  * Red Hat Enterprise Linux (RHEL) 8, 9 and 10
  * Rocky Linux 8, 9 and 10
  * Ubuntu 22, 24 and 26



If you use this script on other operating systems, the installation might fail. This script can install NVIDIA driver as well as [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

**Procedure**

To create an OS image that has self-signed certificates, complete the following steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Download the [cuda_installer tool](https://github.com/GoogleCloudPlatform/compute-gpu-installation/tree/main/linux). To download the latest version of the script, run the following command:
         
         curl -L https://storage.googleapis.com/compute-gpu-installation-us/installer/latest/cuda_installer.pyz --output cuda_installer.pyz
         

  3. Build an image that has Secure Boot enabled by running the following command. The image creation process can take up to 20 minutes.
         
         PROJECT=PROJECT_ID
         ZONE=ZONE
         BASE_IMAGE=BASE_IMAGE_NAME
         SECURE_BOOT_IMAGE=IMAGE_NAME
         
         python3 cuda_installer.pyz build_image \
           --project $PROJECT \
           --vm-zone $ZONE \
           --base-image $BASE_IMAGE $SECURE_BOOT_IMAGE
         

Replace the following:

     * `PROJECT_ID`: ID of the project to create the image in
     * `ZONE`: zone to create a temporary VM used. For example `us-west4-a`.
     * `IMAGE_NAME`: name of the image that will be created.
     * `BASE_IMAGE_NAME`: select from one of the following:

       * `debian-12` or `debian-13`
       * `rhel-8`, `rhel-9` or `rhel-10`
       * `rocky-8`, `rocky-9` or `rocky-10`
       * `ubuntu-22` or `ubuntu-24`

You can also add the `--family NAME` flag to add the new image to an [image family](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

To see all the customization options for the image run `python3 cuda_installer.pyz build_image --help`. You can also [review the documentation for the `cuda_installer` on GitHub](https://github.com/GoogleCloudPlatform/compute-gpu-installation/blob/main/linux/README.md#secure-boot-support).

  4. Verify the image. Use the following steps to verify that the image has Secure Boot enabled and can create GPU instances that have NVIDIA drivers installed.

     1. Create a test VM instance to verify that your image is properly configured and the GPU drivers load successfully. The following example creates an N1 machine type with a single NVIDIA T4 accelerator attached. However, you can use any supported GPU machine type of your choice.
            
            TEST_INSTANCE_NAME=TEST_INSTANCE_NAME
            ZONE=ZONE
            
            gcloud compute instances create $TEST_INSTANCE_NAME \
             --project=$PROJECT \
             --zone=$ZONE \
             --machine-type=n1-standard-4 \
             --accelerator=count=1,type=nvidia-tesla-t4 \
             --create-disk=auto-delete=yes,boot=yes,device-name=$TEST_INSTANCE_NAME,image=projects/$PROJECT/global/images/$SECURE_BOOT_IMAGE,mode=rw,size=100,type=pd-balanced \
             --shielded-secure-boot \
             --shielded-vtpm \
             --shielded-integrity-monitoring \
             --maintenance-policy=TERMINATE
            

Replace the following:

        * `TEST_INSTANCE_NAME`: a name for the test VM instance
        * `ZONE`: a zone that has T4 GPUs or the GPU of your choice. For more information, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
     2. Check that Secure Boot is enabled by running the `mokutil --sb-state` command on the test VM by using `gcloud compute ssh`.
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_INSTANCE_NAME --command "mokutil --sb-state"
            

     3. Verify that the driver is installed by running the `nvidia-smi` command on the test VM by using `gcloud compute ssh`.
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_INSTANCE_NAME --command "nvidia-smi"
            

If you had installed the CUDA Toolkit, you can use the `cuda_installer` tool to verify the install as follows:
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_INSTANCE_NAME --command "python3 cuda_installer.pyz verify_cuda"
            

  5. Clean up. After you verify that the customized image works, there's no need to keep the verification VM around. To delete the VM, run the following command:
         
         gcloud compute instances delete --zone=$ZONE --project=$PROJECT $TEST_INSTANCE_NAME
         

  6. _Optional_ : To delete the disk image you created, run the following command:
         
         gcloud compute images delete --project=$PROJECT $SECURE_BOOT_IMAGE
         




###  Self-signing (manual) 

**Supported operating systems**

This manual self-signing method was tested on the following operating systems:

**Supported operating systems**

The Linux installation script was tested on the following operating systems:

  * Debian 12 and 13
  * Red Hat Enterprise Linux (RHEL) 8, 9 and 10
  * Rocky Linux 8, 9 and 10
  * Ubuntu 22, 24 and 26



If you use this script on other operating systems, the installation might fail. This script can install NVIDIA driver as well as [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

**Overview**

The installation, signing, and image creation process is as follows:

  1. Generate your own certificate to be used for signing the driver.
  2. Create a VM to install and sign the GPU driver. To create the VM, you can use the OS of your choice. When you create the VM, you must disable Secure Boot. You don't need to attach any GPUs to the VM.
  3. Install and sign the GPU driver, and optional CUDA Toolkit.
  4. Create a disk image based on the machine with a self-signed driver, [adding your certificate to the list of trusted certificates](https://docs.cloud.google.com/compute/shielded-vm/docs/creating-shielded-images).
  5. Use the image to create GPU VMs that have Secure Boot enabled.



**Image creation**

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Generate your own certificate by using OpenSSL. With OpenSSL, the signing and verification for Secure Boot is done by using the regular Distinguished Encoding Rules (DER)-encoded X.509 certificates. Run the following command to generate a new self-signed X.509 certificate and an RSA private key file.
         
         openssl req -new -x509 -newkey rsa:2048 -keyout private.key -outform DER -out public.der -noenc -days 36500 -subj "/CN=Graphics Drivers Secure Boot Signing"
         

  3. Create a VM to install the self-signed driver. When you create the VM, you don't need to attach any GPUs or enable Secure Boot. You can use a standard E2 machine type that has at least 40 GB of space available, so that the installation process can succeed.
         
         INSTANCE_NAME=BUILD_INSTANCE_NAME
         DISK_NAME=IMAGE_NAME
         ZONE=ZONE
         PROJECT=PROJECT_ID
         OS_IMAGE=IMAGE_DETAILS
         
         # Create the build VM
         gcloud compute instances create $INSTANCE_NAME \
          --zone=$ZONE \
          --project=$PROJECT \
          --machine-type=e2-standard-4 \
          --create-disk=auto-delete=yes,boot=yes,name=$DISK_NAME,$OS_IMAGE,mode=rw,size=100,type=pd-balanced \
          --no-shielded-secure-boot
         

Replace the following:

     * `BUILD_INSTANCE_NAME`: name of the VM instance used to build the image.
     * `IMAGE_NAME`: name of the disk image.
     * `ZONE`: zone to create the VM in.
     * `PROJECT_ID`: ID of the project you want to use to build the new disk image in.
     * `IMAGE_DETAILS`: the image family and project for your selected base OS image:

       * Debian 12: `"image-family=debian-12,image-project=debian-cloud"`
       * Debian 13: `"image-family=debian-13,image-project=debian-cloud"`
       * RHEL 8: `"image-family=rhel-8,image-project=rhel-cloud"`
       * RHEL 9: `"image-family=rhel-9,image-project=rhel-cloud"`
       * RHEL 10: `"image-family=rhel-10,image-project=rhel-cloud"`
       * Rocky Linux 8: `"image-family=rocky-linux-8,image-project=rocky-linux-cloud"`
       * Rocky Linux 9: `"image-family=rocky-linux-9,image-project=rocky-linux-cloud"`
       * Rocky Linux 10: `"image-family=rocky-linux-10,image-project=rocky-linux-cloud"`
       * Ubuntu 22: `"image-family=ubuntu-2204-lts-amd64,image-project=ubuntu-os-cloud"`
       * Ubuntu 24: `"image-family=ubuntu-2404-lts-amd64,image-project=ubuntu-os-cloud"`
  4. Copy the generated private key file to the VM. To sign the driver file, you need to have the newly generated key pair available on the VM.
         
         gcloud compute scp --zone $ZONE --project $PROJECT private.key $INSTANCE_NAME:~/private.key
         gcloud compute scp --zone $ZONE --project $PROJECT public.der $INSTANCE_NAME:~/public.der
         

  5. Install and sign the driver. The installation and signing of the driver and CUDA Toolkit are handled by the installation script that's also used for installations that don't use Secure Boot. To install and sign the driver, complete the following steps:

     1. Connect with SSH to the VM:
            
            gcloud compute ssh --zone $ZONE --project $PROJECT $INSTANCE_NAME
            

     2. Verify that the private and public keys got properly copied:
            
            ls private.key public.der
            

     3. Download driver installation script:
            
            curl -L https://storage.googleapis.com/compute-gpu-installation-us/installer/latest/cuda_installer.pyz --output cuda_installer.pyz
            

     4. Check that the driver installation is set up with signing configured. The build machine restarts during setup. After the build machine restarts, connect to the VM using SSH and rerun the script to resume installation.
            
            sudo python3 cuda_installer.pyz install_driver --secure-boot-pub-key=public.der --secure-boot-priv-key=private.key --ignore-no-gpu
            

If you want to install CUDA Toolkit at the same time, you can do so with the following command.
            
            sudo python3 cuda_installer.pyz install_cuda --ignore-no-gpu
            

You might see some error or warning messages. These are the result of no GPU being detected and are expected. The system will reboot after completing CUDA Toolkit installation. After reconnecting, you can continue to the next steps.

     5. Remove the certificate files, as they are no longer needed on the temporary machine. For better security, use `shred` instead of the `rm` command. Keys shouldn't be present on the final disk image.
            
            shred -uz private.key public.der
            

     6. Shutdown the VM so that you can use its disk to create the new image.
            
            sudo shutdown now
            

  6. Prepare the base disk image. To create a new disk image that can be used to create instances with Secure Boot enabled, you need to configure the image to trust your newly generated key. The new disk image still accepts the [default certificates](https://docs.cloud.google.com/compute/shielded-vm/docs/creating-shielded-images#default_certificates), used by the operating system. To prepare the base image, complete the following steps.

     1. Download the default certificates. Use the following commands to download the [MicWinProPCA2011_2011-10-19.crt](https://go.microsoft.com/fwlink/p/?linkid=321192) and [MicCorUEFCA2011_2011-06-27.crt](https://go.microsoft.com/fwlink/p/?linkid=321194) certificates:
            
            curl -L https://storage.googleapis.com/compute-gpu-installation-us/certificates/MicCorUEFCA2011_2011-06-27.crt --output MicCorUEFCA2011_2011-06-27.crt
            curl -L https://storage.googleapis.com/compute-gpu-installation-us/certificates/MicWinProPCA2011_2011-10-19.crt --output MicWinProPCA2011_2011-10-19.crt
            
            curl -L https://storage.googleapis.com/compute-gpu-installation-us/certificates/windows_uefi_ca_2023.crt --output windows_uefi_ca_2023.crt
            curl -L https://storage.googleapis.com/compute-gpu-installation-us/certificates/microsoft_uefi_ca_2023.crt --output microsoft_uefi_ca_2023.crt
            

     2. Verify the certificates:
            
            cat <<EOF >>check.sha1
            46def63b5ce61cf8ba0de2e6639c1019d0ed14f3  MicCorUEFCA2011_2011-06-27.crt
            b5eeb4a6706048073f0ed296e7f580a790b59eaa  microsoft_uefi_ca_2023.crt
            580a6f4cc4e4b669b9ebdc1b2b3e087b80d0678d  MicWinProPCA2011_2011-10-19.crt
            45a0fa32604773c82433c3b7d59e7466b3ac0c67  windows_uefi_ca_2023.crt
            EOF
            
            sha1sum -c check.sha1
            

     3. Create an image based on the disk of the temporary VM. You can add `--family=IMAGE_FAMILY_NAME` as an option, so that the image is set as the latest image in a given image family. Creation of the new image might take a couple minutes.

Run the following command in the same directory where your `public.der` file and downloaded certificates are.
            
            SECURE_BOOT_IMAGE=IMAGE_NAME
            
            gcloud compute images create $SECURE_BOOT_IMAGE \
            --source-disk=$DISK_NAME \
            --source-disk-zone=$ZONE \
            --project=$PROJECT  \
            --signature-database-file=MicWinProPCA2011_2011-10-19.crt,MicCorUEFCA2011_2011-06-27.crt,windows_uefi_ca_2023.crt,microsoft_uefi_ca_2023.crt,public.der \
            --guest-os-features="UEFI_COMPATIBLE"
            

You can verify that the public key of your certificate is attached to this new image by running the following command:
            
            gcloud compute images describe --project=$PROJECT $SECURE_BOOT_IMAGE
            

  7. Verify the new image. You can create a GPU VM using the new disk image. For this step, we recommend an N1 machine type with a single T4 accelerator that has Secure Boot enabled. However, the image also supports other types of GPUs and machine types.

     1. Create a test GPU VM:
            
            TEST_GPU_INSTANCE=TEST_GPU_INSTANCE_NAME
            ZONE=ZONE
            
            gcloud compute instances create $TEST_GPU_INSTANCE \
            --project=$PROJECT \
            --zone=$ZONE \
            --machine-type=n1-standard-4 \
            --accelerator=count=1,type=nvidia-tesla-t4 \
            --create-disk=auto-delete=yes,boot=yes,device-name=$TEST_GPU_INSTANCE,image=projects/$PROJECT/global/images/$SECURE_BOOT_IMAGE,mode=rw,size=100,type=pd-balanced \
            --shielded-secure-boot \
            --shielded-vtpm \
            --shielded-integrity-monitoring \
            --maintenance-policy=TERMINATE
            

Replace the following:

        * `TEST_GPU_INSTANCE_NAME`: name of the GPU VM instance that you are creating to test the new image.
        * `ZONE`: zone that has T4 GPUs or other GPU of your choice. For more information, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
     2. Check that Secure Boot is enabled by running the `mokutil --sb-state` command on the test VM using `gcloud compute ssh`.
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_GPU_INSTANCE --command "mokutil --sb-state"
            

     3. Verify that the driver is installed by running the `nvidia-smi` command on the test VM by using `gcloud compute ssh`.
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_GPU_INSTANCE --command "nvidia-smi"
            

If you had installed the CUDA Toolkit, you can use the `cuda_installer` tool to verify the install as follows:
            
            gcloud compute ssh --project=$PROJECT --zone=$ZONE $TEST_GPU_INSTANCE --command "python3 cuda_installer.pyz verify_cuda"
            

  8. Clean up. After you verify that the new image works, there's no need to keep the temporary VM or the verification VM around. The disk image you created doesn't depend on them in any way. You can delete them with the following command:
         
         gcloud compute instances delete --zone=$ZONE --project=$PROJECT $INSTANCE_NAME
         gcloud compute instances delete --zone=$ZONE --project=$PROJECT $TEST_GPU_INSTANCE
         

We don't advise that you store your Secure Boot signing certificate in an unencrypted state on your disk. If you'd like to securely store the keys in a way that they can be shared with others, you can use [Secret Manager](https://cloud.google.com/security/products/secret-manager) to keep your data safe.

When you no longer need the files on your disk, it's best to safely remove them using the `shred` tool. Run the following command:
         
         # Safely delete the key pair from your system
         shred -uz private.key public.der
         




###  Pre-signed (Ubuntu only) 

These instructions are only available for Secure boot Linux VMs that run on Ubuntu 18.04, 20.04, and 22.04 operating systems. Support for more Linux operating systems is in progress.

To install GPU drivers on your Ubuntu VMs that use Secure Boot, complete the following steps:

  1. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) where you want to install the driver.

  2. Update the repository.
         
         sudo apt-get update
         

  3. Search for the most recent NVIDIA kernel module package or the version you want. This package contains NVIDIA kernel modules signed by the Ubuntu key. If you want to find an earlier version, change the number for the tail parameter to get an earlier version. For example, specify `tail -n 2`.

###  Ubuntu PRO and LTS 

For Ubuntu PRO and LTS, run the following command:
         
         NVIDIA_DRIVER_VERSION=$(sudo apt-cache search 'linux-modules-nvidia-[0-9]+-gcp$' | awk '{print $1}' | sort | tail -n 1 | head -n 1 | awk -F"-" '{print $4}')
         

###  Ubuntu PRO FIPS 

For Ubuntu PRO FIPS, run the following commands:

     1. Enable Ubuntu FIPS updates.
            
            sudo ua enable fips-updates
            

     2. Shutdown and reboot
            
            sudo shutdown -r now
            

     3. Get the latest package.
            
            NVIDIA_DRIVER_VERSION=$(sudo apt-cache search 'linux-modules-nvidia-[0-9]+-gcp-fips$' | awk '{print $1}' | sort | tail -n 1 | head -n 1 | awk -F"-" '{print $4}')
            

You can check the picked driver version by running `echo $NVIDIA_DRIVER_VERSION`. The output is a version string like `455`.

  4. Install the kernel module package and corresponding NVIDIA driver.

**Note:** Installing the package might upgrade your kernel.
         
         sudo apt install linux-modules-nvidia-${NVIDIA_DRIVER_VERSION}-gcp nvidia-driver-${NVIDIA_DRIVER_VERSION}
         

If the command failed with the `package not found error`, the latest NVIDIA driver might be missing from the repository. Retry the previous step and select an earlier driver version by changing the tail number.

  5. [Verify](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-linux) that the NVIDIA driver is installed. You might need to reboot the VM.

  6. If you rebooted the system to verify the NVIDIA version. After the reboot, you need to reset the `NVIDIA_DRIVER_VERSION` variable by rerunning the command that you used in step 3.

  7. Configure APT to use the NVIDIA package repository.

     1. To help APT pick the correct dependency, pin the repositories as follows: 
            
            sudo tee /etc/apt/preferences.d/cuda-repository-pin-600 > /dev/null <<EOL
            Package: nsight-compute
            Pin: origin *ubuntu.com*
            Pin-Priority: -1  
            
            Package: nsight-systems
            Pin: origin *ubuntu.com*
            Pin-Priority: -1  
            
            Package: nvidia-modprobe
            Pin: release l=NVIDIA CUDA
            Pin-Priority: 600  
            
            Package: nvidia-settings
            Pin: release l=NVIDIA CUDA
            Pin-Priority: 600  
            
            Package: *
            Pin: release l=NVIDIA CUDA
            Pin-Priority: 100
            EOL
            

     2. Install `software-properties-common`. This is required if you are using Ubuntu minimal images.
            
            sudo apt install software-properties-common
            

     3. Set the Ubuntu version.

###  Ubuntu 18.04 

For Ubuntu 18.04, run the following command:
            
            export UBUNTU_VERSION=ubuntu1804/x86_64

###  Ubuntu 20.04 

For Ubuntu 20.04, run the following command:
            
            export UBUNTU_VERSION=ubuntu2004/x86_64

###  Ubuntu 22.04 

For Ubuntu 22.04, run the following command:
            
            export UBUNTU_VERSION=ubuntu2204/x86_64

     4. Download the `cuda-keyring` package.
            
            wget https://developer.download.nvidia.com/compute/cuda/repos/$UBUNTU_VERSION/cuda-keyring_1.0-1_all.deb

     5. Install the `cuda-keyring` package.
            
            sudo dpkg -i cuda-keyring_1.0-1_all.deb

     6. Add the NVIDIA repository.
            
            sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/$UBUNTU_VERSION/ /"

If prompted, select the default action to keep your current version.

  8. Find the compatible CUDA driver version.

The following script determines the latest CUDA driver version that is compatible with the NVIDIA driver we just installed: 
         
         CUDA_DRIVER_VERSION=$(apt-cache madison cuda-drivers | awk '{print $3}' | sort -r | while read line; do
             if dpkg --compare-versions $(dpkg-query -f='${Version}\n' -W nvidia-driver-${NVIDIA_DRIVER_VERSION}) ge $line ; then
                echo "$line"
                break
             fi
          done)
         

You can check the CUDA driver version by running `echo $CUDA_DRIVER_VERSION`. The output is a version string like `455.32.00-1`.

  9. Install CUDA drivers with the version identified from the previous step. 
         
         sudo apt install cuda-drivers-${NVIDIA_DRIVER_VERSION}=${CUDA_DRIVER_VERSION} cuda-drivers=${CUDA_DRIVER_VERSION}
         

  10. Optional: Hold back `dkms` packages.

After enabling Secure Boot, all kernel modules must be signed to be loaded. Kernel modules built by `dkms` don't work on the VM because they aren't properly signed by default. This is an optional step, but it can help prevent you from accidentally installing other `dkms` packages in the future.

To hold `dkms` packages, run the following command:
         
         sudo apt-get remove dkms && sudo apt-mark hold dkms
         

  11. Install CUDA Toolkit and runtime.

Pick the suitable CUDA version. The following script determines the latest CUDA version that is compatible with the CUDA driver we just installed:
         
         CUDA_VERSION=$(apt-cache showpkg cuda-drivers | grep -o 'cuda-runtime-[0-9][0-9]-[0-9],cuda-drivers [0-9\\.]*' | while read line; do
             if dpkg --compare-versions ${CUDA_DRIVER_VERSION} ge $(echo $line | grep -Eo '[[:digit:]]+\.[[:digit:]]+') ; then
                echo $(echo $line | grep -Eo '[[:digit:]]+-[[:digit:]]')
                break
             fi
          done)
         

You can check the CUDA version by running `echo $CUDA_VERSION`. The output is a version string like `11-1`.

  12. Install the CUDA package.
         
         sudo apt install cuda-${CUDA_VERSION}
         

  13. Verify the CUDA installation.
         
         sudo nvidia-smi
          /usr/local/cuda/bin/nvcc --version
         

The first command prints the GPU information. The second command prints the installed CUDA compiler version.




If the GPU is attached but nvidia-smi fails to communicate with the driver, see [Troubleshoot nvidia-smi failure when Secure Boot is enabled](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#troubleshoot-secure-boot) or [Troubleshoot nvidia-smi failure after OS patching or kernel upgrade](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#troubleshoot-kernel-mismatch).

## Install vGPU drivers (fractional GPUs)

These instructions are for installing vGPU drivers on G4 VMs that have less than one GPU attached (fractional GPUs), which offer 1/2, 1/4, or 1/8 of a standard G4 GPU.

For G4 instances that have fractional GPUs (vGPUs) attached, you must install a specific vGPU driver on the instance, which connects to the physical machine's host driver. The following minimum driver versions are required:

  * **Linux:** 580.126.09
  * **Windows:** 582.16



### GPU machine type support

The procedures in this section support the following G4 machine types:

  * `g4-standard-6`
  * `g4-standard-12`
  * `g4-standard-24`



### Installation

The driver installation script supports fractional GPUs and is the recommended way to install drivers on your machine.

To install vGPU drivers manually on your Linux G4 VM that has less than one GPU attached, complete the following steps:

  1. Connect to your instance by using SSH.
         
         gcloud compute ssh INSTANCE_NAME \
              --zone=us-central1-b
         

Replace `INSTANCE_NAME` with the name of your instance.

  2. Update your system package lists.
         
         sudo apt-get -y update
         

  3. Install the kernel headers and essential build tools.
         
         (sudo apt-get install -y linux-headers-$(uname -r) build-essential gcc g++ make dkms pciutils bison flex libxml2 libncurses5-dev) || \
         (sudo apt-get install -y linux-headers-cloud-amd64 build-essential gcc g++ make dkms pciutils bison flex libxml2 libncurses5-dev)
         

  4. To ensure that the `cc` compiler is available, run the following command:
         
         if ! command -v cc &> /dev/null
         then
              sudo ln -sf /usr/bin/gcc /usr/bin/cc
              echo "'cc' is now linked to 'gcc'."
         else
              echo "'cc' is already available."
         fi
         
         export PATH=$PATH:/usr/sbin
         

  5. Download the specific required driver from Cloud Storage.
         
         gcloud storage cp gs://gce-nvidia-vgpu-drivers/G4_VGPU/NVIDIA-Linux-x86_64-580.126.09-grid-gcp.run .
         

  6. Make the driver executable by running the following command:
         
         chmod +x NVIDIA-Linux-x86_64-580.126.09-grid-gcp.run
         

  7. Install the vGPU driver on your instance.
         
         sudo ./NVIDIA-Linux-x86_64-580.126.09-grid-gcp.run -s
         

  8. Verify the driver installation.
         
         nvidia-smi
         




## Verify the GPU driver install

After completing the driver installation steps, verify that the driver installed and initialized properly.

###  Linux 

[Connect to the Linux instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and use the `nvidia-smi` command to verify that the driver is running properly.
    
    
    sudo nvidia-smi
    

The output is similar to the following:
    
    
    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 580.82.07              Driver Version: 580.82.07      CUDA Version: 13.0     |
    +-----------------------------------------+------------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  Tesla T4                       On  |   00000000:00:04.0 Off |                    0 |
    | N/A   53C    P8             17W /   70W |       0MiB /  15360MiB |      0%      Default |
    |                                         |                        |                  N/A |
    +-----------------------------------------+------------------------+----------------------+
    
    +-----------------------------------------------------------------------------------------+
    | Processes:                                                                              |
    |  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
    |        ID   ID                                                               Usage      |
    |=========================================================================================|
    |  No running processes found                                                             |
    +-----------------------------------------------------------------------------------------+

If this command fails, check if GPUs are attached to the compute instance. To check for any NVIDIA PCI devices, run the following command:
    
    
    sudo lspci | grep -i "nvidia"

###  Windows Server 

[Connect to the Windows Server instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and open a PowerShell terminal, then run the following command to verify that the driver is running properly.
    
    
    nvidia-smi

The output is similar to the following:
    
    
    +---------------------------------------------------------------------------------------+
    | NVIDIA-SMI 581.42                 Driver Version: 581.42       CUDA Version: 12.8     |
    |-----------------------------------------+----------------------+----------------------+
    | GPU  Name                     TCC/WDDM  | Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
    |                                         |                      |               MIG M. |
    |=========================================+======================+======================|
    |   0  NVIDIA L4                    WDDM  | 00000000:00:03.0 Off |                    0 |
    | N/A   66C    P8              17W /  72W |    128MiB / 23034MiB |      0%      Default |
    |                                         |                      |                  N/A |
    +-----------------------------------------+----------------------+----------------------+
    
    +---------------------------------------------------------------------------------------+
    | Processes:                                                                            |
    |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
    |        ID   ID                                                             Usage      |
    |=======================================================================================|
    |    0   N/A  N/A      4888    C+G   ...CBS_cw5n1h2txyewy\TextInputHost.exe    N/A      |
    |    0   N/A  N/A      5180    C+G   ....Search_cw5n1h2txyewy\SearchApp.exe    N/A      |
    +---------------------------------------------------------------------------------------+

## What's next?

  * To monitor GPU performance, see [Monitor GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).


  * To handle GPU host maintenance, see [Handle GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).
  * To troubleshoot GPU VMs, see [Troubleshoot GPU VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
