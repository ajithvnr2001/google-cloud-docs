---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/install-nvidia-drivers-win/
title: Install NVIDIA GPU drivers on Windows VMs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:58.920669+00:00
---

# Install NVIDIA GPU drivers on Windows VMs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/install-nvidia-drivers-win/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install NVIDIA GPU drivers on Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install NVIDIA graphics processing unit (GPU) drivers on a Windows-based virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

In Distributed Cloud, you can use NVIDIA GPUs to configure GPU-accelerated Windows VMs. NVIDIA GPUs let VM instances efficiently run graphics-intensive applications or heavy GPU-compute workloads that require a Windows operating system.

This document is for developers in platform administrator or application operator groups that manage Windows VMs in a Google Distributed Cloud (GDC) air-gapped environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

### Request IAM roles

To install NVIDIA drivers on a Windows VM instance, contact your IAM Project Admin to request the **Virtual Machine Project Admin** (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Download the CUDA Toolkit

Distributed Cloud operates in an air-gapped environment. This means you can't download files directly from the internet to your VM. You must first download the standalone CUDA Toolkit installer, which includes the required NVIDIA graphics drivers, on a machine with internet access.

  1. On an internet-connected workstation, go to the official NVIDIA CUDA Toolkit downloads page: <https://developer.nvidia.com/cuda-downloads>.
  2. Select the target platform options to match your Windows VM: 
     * In the **Operating System** section, select **Windows**.
     * For **Architecture** , select **x86_64**.
     * In the **Version** section, select your Windows Server version, for example, **Server 2019** or **Server 2022**.
     * For the **Installer Type** , select **exe (local)**. 
       * The **exe (local)** installer is a self-contained package that includes both the NVIDIA display driver and the CUDA development libraries.
  3. Click **Download** to retrieve the local installer executable, typically named `cuda_[VERSION]_windows.exe`.

**Note:** If you don't see the Windows Server version the VM uses in the latest CUDA download page, visit <https://developer.nvidia.com/cuda-toolkit-archive> and download an earlier version of CUDA that supports your Windows Server version.

## Transfer the installer to the Windows VM

After you download the driver installer on your workstation, transfer it directly to the Windows VM using the Remote Desktop (RDP) client's built-in clipboard sharing.

  1. On your workstation, locate the downloaded `cuda_[VERSION]_windows.exe` file.
  2. Right-click the file and select **Copy** , or press **Ctrl+C** on your keyboard.
  3. [Connect to your Windows VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm#connect-to-a-windows-vm) using an RDP client.
  4. Inside the RDP session, open **Windows File Explorer** and navigate to a temporary folder, for example, `C:\Windows\Temp`.
  5. Right-click inside the folder and select **Paste** , or press **Ctrl+V** on your keyboard.
  6. Wait for the file transfer to finish.



## Install the CUDA Toolkit and drivers

After you successfully copy the installer to the Windows VM, proceed with the installation.

  1. Inside the RDP session, double-click the copied `cuda_[VERSION]_windows.exe` file to start the **NVIDIA Installer** wizard.
  2. Click **AGREE AND CONTINUE** to accept the license agreement.
  3. For **Installation options** , select **Express (Recommended)** > click **NEXT**. This option automatically installs the CUDA Toolkit, the required NVIDIA GPU drivers, and system integration tools.
  4. Follow the on-screen prompts to complete the installation.
  5. After the installation wizard finishes, restart the Windows VM.



## Verify the installation

Verify that the Windows OS recognizes the NVIDIA GPU and that the driver is fully functional.

  1. Connect to the Windows VM using an RDP client.
  2. Open **Command Prompt** or **PowerShell** as an Administrator.
  3. Verify the GPU status and driver version:
         
         nvidia-smi
         

Check that the output displays the correct GPU model, driver version, and that there are no reported errors. The output looks similar to the following:
         
         C:\Users\username>nvidia-smi
         Wed May 27 10:58:00 2026
         +-----------------------------------------------------------------------------------------+
         | NVIDIA-SMI 550.54.14             Driver Version: 550.54.14      CUDA Version: 12.4      |
         |-----------------------------------------+------------------------+----------------------+
         | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
         |                                         |                        |               MIG M. |
         |=========================================+========================+======================|
         |   0  NVIDIA L4                      Off | 00000000:00:03.0   Off |                    0 |
         | N/A   44C    P8             15W /  72W  |      0MiB / 23040MiB   |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         
         +-----------------------------------------------------------------------------------------+
         | Processes:                                                                              |
         |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
         |        ID   ID                                                               Usage      |
         |=========================================================================================|
         |  No running processes found                                                             |
         +-----------------------------------------------------------------------------------------+
         

  4. Optional: Verify the CUDA Compiler version:
         
         nvcc --version
         




## What's next

  * [Use a startup script on a Windows VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/windows-startup-script)
  * [Monitor VM metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/monitor/monitor-metrics)
  * Check [VM resiliency](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/config-resiliency)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
