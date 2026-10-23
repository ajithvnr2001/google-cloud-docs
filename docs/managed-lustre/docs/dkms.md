---
url: https://docs.cloud.google.com/managed-lustre/docs/dkms/
title: Dynamic Kernel Module Support (DKMS) for Compute Engine clients \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:29.989454+00:00
---

# Dynamic Kernel Module Support (DKMS) for Compute Engine clients  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/dkms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Dynamic Kernel Module Support (DKMS) for Compute Engine clients Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses custom kernels, or requires specific environment configurations, the [standard Lustre packages](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine#install_the_lustre_client_packages) may not be compatible.

In these situations, Managed Lustre supports [Dynamic Kernel Module Support](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) (DKMS). DKMS is a framework used to manage Linux kernel modules whose source code exists outside the main kernel tree. Its core function is to automatically rebuild and install these modules when a new kernel is installed, ensuring compatibility without manual intervention.

While prebuilt kernel modules remain the recommended installation path for most users, DKMS provides an alternative for those using custom Linux kernels.

## Considerations

Using Dynamic Kernel Module Support (DKMS) for the Managed Lustre client is intended specifically for advanced users who require compatibility with custom kernels and are prepared to manage client-side issues on their own. Unlike prebuilt modules, DKMS requires the installation of a full compiler toolchain and specific kernel headers, which increases the system's security attack surface and disk footprint. Furthermore, because modules are compiled on-demand, users must account for significantly longer client VM startup times and the potential for compilation failures during kernel updates.

## Supported platforms

Managed Lustre supports DKMS client packages for:

  * Ubuntu 22.04 LTS
  * Ubuntu 24.04 LTS, for [Arm VMs only](https://docs.cloud.google.com/compute/docs/instances/arm-instances/overview).



## Requirements

To use DKMS, your system must include:

  * All of the compiler packages needed to compile a kernel module. This is distro-specific.

  * The headers for your specific kernel. For custom kernels, you must manually point the DKMS service to the header location.




DKMS is not supported on [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).

### Install DKMS and headers

Before installing the Managed Lustre DKMS packages, you must install the `dkms` package and the correct Linux kernel headers for your system. The version of the kernel headers must exactly match the version of the kernel you are running.

#### For standard Ubuntu kernels

If you're using a standard kernel provided by Ubuntu, you can typically install the necessary packages by running:
    
    
    sudo apt update
    sudo apt install dkms linux-headers-$(uname -r)
    

#### For non-standard or custom kernels

If you're using a custom kernel, you're responsible for obtaining and installing the correct kernel headers.

The process for installing headers for a custom kernel varies depending on its source. You may need to:

  * Consult your OS vendor's documentation: Your vendor may provide a specific package or repository for the kernel headers.
  * Build from source: If you compiled the kernel yourself, you may need to build and install the headers from the kernel source tree.



#### Custom header locations

DKMS expects to find the kernel headers in the directory `/usr/src/linux-headers-$(uname -r)`. It runs the `uname -r` command to obtain the kernel version string and construct the path. For example: `/usr/src/linux-headers-5.15.0-101-generic`.

If your kernel headers are not installed in the expected location, you must manually point the DKMS service to that location by creating a symbolic link from your custom header directory to the location where DKMS expects to find them.

For example, if your headers are located in `/opt/custom-kernel/headers/`, run the following command:
    
    
    sudo ln -s /opt/custom-kernel/headers/ /usr/src/linux-headers-$(uname -r)
    

It's your responsibility to ensure that the correct kernel headers are properly installed and accessible to DKMS. If the headers cannot be found, the DKMS package will fail to build the Lustre kernel module.

## Install the Managed Lustre DKMS packages

To install the Managed Lustre DKMS packages, follow these steps.

### Configure access to the repository

The DKMS client packages are hosted in the `lustre-client-modules-dkms` project in Artifact Registry.

To configure your VM to install from Artifact Registry, follow these instructions.

### Ubuntu 22.04 LTS

  1. Install the Apt repository signing keys:
         
         curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg
         curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/lustre-client.gpg
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' \
           | sudo tee /etc/apt/sources.list.d/artifact-registry.list
         

  3. Update Apt and install the `apt-transport-artifact-registry` package:
         
         sudo apt update && sudo apt install apt-transport-artifact-registry
         

  4. Configure Apt to fetch packages from the repository:
         
         echo "deb [signed-by=/usr/share/keyrings/lustre-client.gpg] ar+https://us-apt.pkg.dev/projects/lustre-client-modules-dkms lustre-client-ubuntu-jammy main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

  5. Update your repository sources:
         
         sudo apt update
         

If the command returns an error, ensure that your Compute Engine VM was created with the access scope allowing full access to all Cloud APIs. See [Granting access to Compute Engine instances](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) for more details.




More information about these commands is available in the Artifact Registry documentation: [Configure VMs to install Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

### Ubuntu 24.04 LTS

  1. Install the Apt repository signing keys:
         
         curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg
         curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/lustre-client.gpg
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' \
           | sudo tee /etc/apt/sources.list.d/artifact-registry.list
         

  3. Update Apt and install the `apt-transport-artifact-registry` package:
         
         sudo apt update && sudo apt install apt-transport-artifact-registry
         

  4. Configure Apt to fetch packages from the repository:
         
         echo "deb [signed-by=/usr/share/keyrings/lustre-client.gpg] ar+https://us-apt.pkg.dev/projects/lustre-client-modules-dkms lustre-client-ubuntu-noble main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

  5. Update your repository sources:
         
         sudo apt update
         

If the command returns an error, ensure that your Compute Engine VM was created with the access scope allowing full access to all Cloud APIs. See [Granting access to Compute Engine instances](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) for more details.




More information about these commands is available in the Artifact Registry documentation: [Configure VMs to install Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

### Install the Lustre client packages

Follow the instructions to install the Lustre client packages.

### Ubuntu 22.04 LTS

Run the following commands.
    
    
    sudo apt install lustre-client-modules-dkms/lustre-client-ubuntu-jammy
    sudo apt install lustre-client-utils/lustre-client-ubuntu-jammy
    

### Ubuntu 24.04 LTS

Run the following commands.
    
    
    sudo apt install lustre-client-modules-dkms/lustre-client-ubuntu-noble
    sudo apt install lustre-client-utils/lustre-client-ubuntu-noble
    

This step compiles the client packages and can take a while.

## Mount and access your Managed Lustre instance

Follow the instructions in [Mount a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine#mount-a-managed-lustre-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
