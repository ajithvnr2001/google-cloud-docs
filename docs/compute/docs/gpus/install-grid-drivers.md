---
url: https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers/
title: Install drivers for NVIDIA RTX Virtual Workstations (vWS) \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:20.686006+00:00
---

# Install drivers for NVIDIA RTX Virtual Workstations (vWS)  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install drivers for NVIDIA RTX Virtual Workstations (vWS) Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

If you need GPUs for hardware accelerated graphics on a remote desktop or for gaming, you can create virtual workstations that use [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/) (formerly known as NVIDIA GRID).

NVIDIA RTX Virtual Workstations are ideal for running workloads that use APIs such as Vulkan, OpenGL, or Direct3D on a cloud remote desktop.

When you select a [GPU that supports visualization](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) for a virtual workstation, you can add an NVIDIA RTX Virtual Workstation license to your VM. For more information about pricing, see [GPU pricing](https://cloud.google.com/compute/gpus-pricing).

To set up an NVIDIA RTX Virtual Workstation, you need to do the following:

  1. Create a VM that has a visualization-capable GPU attached and virtual workstation enabled. 
     * For G2 and G4 VMs, see [Create a GPU VM for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).
     * For N1 VMs, see [Create an N1 VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose).
  2. Install a driver for the virtual workstation.



After you create your virtual workstation, you can connect to it using a remote desktop protocol such as Windows Remote Desktop Protocol (RDP), HP Anyware®, or VMware® Horizon View.

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




## Recommended minimum NVIDIA virtual GPU software

NVIDIA RTX Virtual Workstations (vWS) are supported on the following machine series.

  * **G4** : you can enable NVIDIA RTX PRO 6000 vWS on these machine types.
  * **G2** : you can enable NVIDIA L4 vWS on these machine types.
  * **N1** : you can enable NVIDIA T4 or V100 vWS GPUs on these machine types.



The following table provides the recommended [NVIDIA virtual GPU software](https://docs.nvidia.com/grid/) software for these machine types.

**NVIDIA vGPU software version** | **Supported machine series and GPU model** | **Recommended NVIDIA driver (Linux)** | **Recommended NVIDIA driver (Windows)** | **[vGPU branch type](https://docs.nvidia.com/vgpu/news/vgpu-software-lifecycle-policy)** | **vGPU software EOS date**  
---|---|---|---|---|---  
20 | 

  * G4 (RTX PRO 6000)
  * G2 (L4)
  * N1 (T4)

| Latest R595 driver | Latest R595 driver | Production Branch | March 2027  
19 | 

  * G4 (RTX PRO 6000)
  * G2 (L4)
  * N1 (T4, V100)

| Latest R580 driver | Latest R580 driver | Long-Term Support Branch | July 2028  
  
## Limitations

For Ubuntu 24.04 NVIDIA RTX Virtual Workstations, the available NVIDIA GRID driver versions might not fully support [Direct Rendering Infrastructure 3 (DRI3)](https://wikipedia.org/wiki/Direct_Rendering_Infrastructure). This lack of full support can affect GPU acceleration for certain desktop applications and virtual desktop environments, such as [Virtual Network Computing (VNC)](https://wikipedia.org/wiki/Virtual_Network_Computing) and [Chromium](https://wikipedia.org/wiki/Chromium_\(web_browser\)). If you need to run these applications, use Ubuntu 22.04.

## Automated driver installation

You can use an open source script from [GitHub](https://github.com/GoogleCloudPlatform/compute-gpu-installation) to automate the installation of RTX Virtual Workstation drivers. This is the same script used for regular driver installation. It automatically detects that your instance has RTX Virtual Workstation enabled and installs the correct driver.

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
         
         sudo python3 cuda_installer.pyz install_driver 

The script takes several minutes to run. It might restart your compute instance. When the compute instance restarts, run the script again with the same parameters to continue the installation.

  5. Verify the installation. See Verify the GPU driver install.

  6. You can also use this tool to install the CUDA Toolkit. To install the CUDA Toolkit, run the following command:
         
         sudo python3 cuda_installer.pyz install_cuda 

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

## Manual driver installation

Manual installation is an alternative to using the automated installation script. You might choose this method if you need to use a specific driver version required by your application, if you are operating in a restricted network environment with limited outbound connectivity, or if you require more granular control over the installation process for troubleshooting.

Complete the following steps on your VM.

  1. For Linux operating systems, install the build tools for your Linux version.

###  CentOS or RHEL 
         
         sudo yum group install "Development Tools"

###  Debian or Ubuntu 

     1. Install the build tools.
            
            sudo apt update
            
            sudo apt install -y build-essential
            
            sudo apt install -y libvulkan1

     2. If you are using Ubuntu 22.04, update the `gcc` version for the NVIDIA driver.
            
            sudo apt install -y gcc-12
            
            sudo apt install -y linux-headers-$(uname -r)
            
            sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
            
            sudo update-alternatives --config gcc

###  SLES 

     * **SLES 12**
           
           sudo zypper install -t pattern devel_basis
           
           sudo zypper install gcc8

     * **SLES 15**
           
           sudo SUSEConnect -p sle-module-development-tools/15/x86_64
           
           sudo zypper install gcc8

  2. For Linux operating systems, install the Linux kernel headers. See [Pre-installation Actions](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/pre-installation-actions.html) for your operating system in the NVIDIA documentation.

  3. For all operating systems, install drivers.

**Caution:** The drivers provided in this section are for use with Compute Engine only. If you need drivers for other platforms, see the [NVIDIA Driver Download](http://www.nvidia.com/Download/index.aspx) page.

###  Linux 

     1. Identify the driver version that you need to download. For a full list of NVIDIA RTX Virtual Workstation drivers that you can use on Compute Engine, see [Drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/grid-drivers-table). From this table, copy the **Filename** for your required driver.

     2. Download the driver by running the following command.
            
            gcloud storage cp gs://nvidia-drivers-us-public/GRID/FILENAME .
            

Replace `FILENAME` with the filename that you identified in the previous step.

For example, to download the `vGPU 20.2` driver, run the following command: 
            
            gcloud storage cp gs://nvidia-drivers-us-public/GRID/vGPU20.2/NVIDIA-Linux-x86_64-595.91.07-grid.run .
            

     3. Start the installer by running the following command.
            
            sudo bash DRIVER_NAME

Replace `DRIVER_NAME` with the driver that you downloaded in the previous step.

For example, to start the installer for the `vGPU 20.2` driver, run the following command: 
            
            sudo bash NVIDIA-Linux-x86_64-595.91.07-grid.run

     4. During the installation, choose the following options:

        * If you are prompted to install 32-bit binaries, select **Yes**.
        * If you are prompted to modify the `x.org` file, select **No**.

###  Windows Server 

     1. Identify the driver version that you need to download. For a full list of NVIDIA RTX Virtual Workstation drivers that you can use on Compute Engine, see [Drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/grid-drivers-table). From this table, copy the **Filename** for your required driver.

     2. Download the driver by opening a PowerShell and running the following command. In this command, replace `FILENAME` with the filename that you identified in the previous step.
            
            gcloud storage cp gs://nvidia-drivers-us-public/GRID/FILENAME .
            

For example, to download the `vGPU 20.2` driver installer, open PowerShell and run the following command:
            
            gcloud storage cp gs://nvidia-drivers-us-public/GRID/vGPU20.2/596.86_grid_win10_win11_server2022_server_2025_dch_64bit_international.exe .
            

     3. Run the installer, and choose the **Express installation**.

     4. After the installation is complete, restart the VM. When you restart, you are disconnected from your session.

     5. Reconnect to your instance using RDP or a PCoIP client.

  4. This step is only required for Linux-based NVIDIA RTX Virtual Workstation with attached T4 or L4 GPUs.

If you installed an NVIDIA 510 or later driver, you need to disable the GSP firmware. See [Disabling GSP Firmware](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#disabling-gsp) in the Nvidia documentation. When completing this step, keep the following in mind:

     * Use `sudo` to run the commands to create and update the configuration file.
     * To reboot the VM, you can use `sudo reboot` or [stop and start the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).



## Verify that the driver is installed

###  Linux 

After you install the drivers, verify that the driver is installed and that the NVIDIA RTX Virtual Workstation license is active.

  1. To verify the driver installation, run the following command:
         
         nvidia-smi

The output of the command looks similar to the following:
         
         +-----------------------------------------------------------------------------------------+
         | NVIDIA-SMI 595.91.07              Driver Version: 595.91.07      CUDA Version: 13.2     |
         +-----------------------------------------+------------------------+----------------------+
         | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
         |                                         |                        |               MIG M. |
         |=========================================+========================+======================|
         |   0  NVIDIA L4                      On  |   00000000:00:03.0 Off |                    0 |
         | N/A   43C    P8             13W /   72W |       1MiB /  23034MiB |      0%      Default |
         |                                         |                        |                  N/A |
         +-----------------------------------------+------------------------+----------------------+
         
         +-----------------------------------------------------------------------------------------+
         | Processes:                                                                              |
         |  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
         |        ID   ID                                                               Usage      |
         |=========================================================================================|
         |  No running processes found                                                             |
         +-----------------------------------------------------------------------------------------+
         

  2. To verify the NVIDIA RTX Virtual Workstation license, run the following command:
         
         nvidia-smi -q

To validate GPU acceleration for desktop applications, look for the `vGPU Software Licensed Product` section in the output. On a properly licensed NVIDIA RTX Virtual Workstation VM, you should see the following:
         
         vGPU Software Licensed Product
          Product Name                      : NVIDIA RTX Virtual Workstation
          License Status                    : Licensed (Expiry: Permanent)
          

This output indicates that the driver is functioning and able to provide accelerated graphics.

If you see a different output, the driver is not licensed for NVIDIA RTX Virtual Workstation and you won't get GPU acceleration.

For example, if the VM wasn't created with the correct `--accelerator-type` that enables vWS, you might see the following output:
         
         vGPU Software Licensed Product
          Product Name                      : NVIDIA Virtual Applications
          License Status                    : Licensed (Expiry: N/A)
         

This can happen if the VM was not created with the NVIDIA RTX Virtual Workstation license enabled. To resolve this issue, you must recreate your VM using a GPU model that supports [NVIDIA RTX Virtual Workstation](https://docs.cloud.google.com/compute/docs/gpus#gpu-models) and make sure to enable the virtual workstation when you attach the GPUs. For detailed instructions, review the [Create an instance](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#create_a_vm_that_has_attached_gpus) instruction for your machine type.




###  Windows Server 

  1. Connect to your Windows instance using RDP or a PCoIP client.

  2. Right-click the desktop, and select **NVIDIA Control Panel**.

  3. In the NVIDIA Control Panel, from the Help menu, select **System Information**. The information shows the GPU that the VM is using, and the driver version.




## What's next?

  * To monitor GPU performance, see [Monitor GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).


  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
