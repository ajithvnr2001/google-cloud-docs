---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions/
title: Supported customization actions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:37:36.930329+00:00
---

# Supported customization actions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Supported customization actions Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

To customize your virtual machine images, such as running terminal scripts, updating boot parameters, transferring binaries, or installing GPU drivers, you can define specific helper actions inside the `spec.steps` block of your customization recipe ([`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema)). 

## Overview

During the execution phase of an Image Builder build, the orchestrator runs the steps declared in your customization recipe (`spec.steps`) sequentially on the temporary worker VM.

Each step must specify a `name`, an `action`, and an `inputs` block tailored to that action type. Image Builder supports the following customization actions:

  * `Shell`: Executes inline terminal scripts or commands on the worker guest OS.
  * `UpdateKernelCommandLine`: Modifies boot parameters and kernel command-line flags.
  * `FileCopy`: Transfers configuration files, scripts, or assets from Cloud Storage or local workspaces onto the VM.
  * `InstallGPU`: Downloads, compiles, and registers NVIDIA GPU drivers.



## Shell action

The `Shell` action lets you execute inline terminal scripts or single shell commands on the guest OS of the temporary worker VM to perform customizations like updating packages, configuring user accounts, or compiling software.

Specify either of the following inputs under `steps.inputs`:

  * `inlineScript` (string): Raw multiline shell commands to execute.
  * `command` (string): A single system command string or relative path to a binary file executable.



### Sample configurations

The following tabs show sample step configurations for running an inline script versus running a single command:

###  Run an inline script 

The following configuration runs a multiline script that updates packages using `apt`:
    
    
    - name: "Update guest packages and configure groups"
      action: Shell
      inputs:
        inlineScript: |
          #!/bin/bash
          apt-get update -y
          apt-get install -y fail2ban build-essential
          groupadd -r adminusers
    

###  Run a single command 

The following configuration runs a single shell command to verify the active operating system kernel version:
    
    
    - name: "Log kernel identifier"
      action: Shell
      inputs:
        command: "uname -a"
    

### Special behaviors

When you run `Shell` actions, the customization provisioner manages security auditing and automated system reboots as described in the following sections:

#### Security auditing

To prevent sensitive tokens, secrets, or proprietary code from leaking into execution logs, the customization provisioner doesn't print the raw lines of your scripts unless interactive debugging is enabled (`debug: true`). Instead, it logs the SHA-256 integrity hash of your script payload to the build logs. This hash provides an immutable audit trace of exactly what code ran on the image.

#### System reboots (Exit Code 3010)

Some shell actions, such as kernel patch updates or storage partition adjustments, require a system reboot before subsequent steps can run.

To request a system reboot during customization, your shell script must end with the command `exit 3010`. When the customization provisioner receives exit code `3010`, it handles the reboot lifecycle as follows:

  1. The provisioner detects exit code `3010`, pauses execution, and marks the step progress index.
  2. The provisioner reboots the worker VM.
  3. After the VM restarts, the provisioner mounts the workspace and automatically resumes the pipeline at the next step in the queue.



##### Reboot example:

The following example shows a step configuration that updates packages and requests a reboot:
    
    
    - name: "Install core updates and request reboot"
      action: Shell
      inputs:
        inlineScript: |
          #!/bin/bash
          echo "Applying configuration package upgrades..."
          apt-get dist-upgrade -y
          # Terminate with return code 3010 to trigger a system reboot
          exit 3010
    - name: "Post-reboot verification"
      action: Shell
      inputs:
        command: "uname -r"
    

## UpdateKernelCommandLine action

The `UpdateKernelCommandLine` action locates, replaces, inserts, or removes command-line flags passed to the kernel at system boot, such as when you configure console logs or adjust kernel parameters.

Specify the following properties under the `steps.inputs` map:

  * `oldArguments` (string, Required): The exact command-line arguments to locate, remove, or replace inside the bootloader config.
  * `newArguments` (string, Optional): The replacement arguments to write in place of the target flags. If you omit the `newArguments` property, Image Builder removes the parameters configured in the `oldArguments` property entirely from the boot line.

**Caution:** You can include the `UpdateKernelCommandLine` action only once inside the `steps` list of a customization recipe.

### Sample configurations

The following tabs show sample step configurations for replacing or removing kernel boot arguments:

###  Replace boot arguments 

The following configuration locates the kernel log level key `loglevel=4` and replaces it with more verbose parameters `loglevel=6 console=ttyS0`:
    
    
    - name: "Configure detailed boot logging"
      action: UpdateKernelCommandLine
      inputs:
        oldArguments: "loglevel=4"
        newArguments: "loglevel=6 console=ttyS0"
    

###  Remove boot arguments 

The following configuration searches for the parameter `quiet` and removes it from the boot arguments to enable verbose logging during startup check phases:
    
    
    - name: "Enable verbose startup diagnostics"
      action: UpdateKernelCommandLine
      inputs:
        oldArguments: "quiet"
    

### OS-specific execution details

The following tabs describe how the customization provisioner handles image modifications depending on the source guest operating system:

###  Container-Optimized OS (COS) 

Because COS features a read-only partition layout, it omits standard configuration tools. The customization provisioner does the following:

  1. Determines the active boot device path.
  2. Mounts partition 12, the EFI partition, of the boot device.
  3. Directly updates bootloader parameters inside `/efi/boot/grub.cfg`.
  4. Safely unmounts partition 12.



###  Ubuntu 

On Ubuntu images, the customization provisioner does the following:

  1. Opens `/etc/default/grub` and files under `/etc/default/grub.d/*.cfg`.
  2. Inserts, modifies, or deletes the target arguments under the `GRUB_CMDLINE_LINUX` block.
  3. Runs the package command `update-grub` to regenerate the bootloader configurations.



## FileCopy action

The `FileCopy` action copies configuration files, binaries, or certificates from a remote bucket or your local repository to your custom image. The customization provisioner downloads or reads the source file, writes it to your specified guest path on the worker VM, and configures the permissions.

Specify the following inputs under `steps.inputs`:

  * `destination` (string, Required): The absolute path in the guest OS where the file is created.
  * `permissions` (string, Required): The octal representation of the target configuration permissions, such as `"0755"` or `"0644"`.
  * Specify either of the following source properties: 
    * `gcsSourcePath` (string): The Cloud Storage URI of the source file, which must follow the format `gs://BUCKET_NAME/OBJECT_NAME`.
    * `localSourcePath` (string): The relative path to the file inside the local workspace repository folder. Path traversal using `../` is blocked for security.



### Sample configurations

The following tabs show sample step configurations for copying a file from Cloud Storage versus copying from your local workspace:

###  Cloud Storage 

The following configuration copies a configuration template from a Cloud Storage bucket onto the guest VM image:
    
    
    - name: "Import licensing configuration"
      action: FileCopy
      inputs:
        gcsSourcePath: "gs://enterprise-configs-bucket/licensing/license.key"
        destination: "/etc/app/license.key"
        permissions: "0600"
    

###  Local workspace 

The following configuration copies an application script compiled during previous Cloud Build steps:
    
    
    - name: "Deploy setup automation daemon"
      action: FileCopy
      inputs:
        localSourcePath: "bin/setup-daemon"
        destination: "/usr/local/bin/setup-daemon"
        permissions: "0755"
    

### OS-specific guidelines

The following tabs describe file location guidelines depending on the target guest operating system:

###  Container-Optimized OS (COS) 

COS images contain a read-only partition layout for security purposes. Some standard system targets, such as `/usr/` or `/bin/`, are write-protected.

When configuring file destinations on COS:

  * Specify files only inside writable stateful locations, such as `/var` or `/home`.
  * Refer to the official [Container-Optimized OS Disks and file system reference](https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem) to identify appropriate paths.



###  Ubuntu 

Ubuntu images feature a standard Linux read-write root partition layout (`/`). You can specify file destinations inside any standard system path, such as `/etc`, `/usr/local/bin`, `/var`, or `/home`, provided the user profile or destination folder has appropriate configuration permissions on the worker VM.

## InstallGPU action

Use the `InstallGPU` action to build VM images optimized for machine learning, data science, or scientific workloads. Image Builder downloads, compiles, and registers NVIDIA GPU drivers on your custom images. Depending on your base image type and target hardware, you can choose between installing precompiled drivers or compiling custom driver `.run` files.

Specify one of the following inputs under `steps.inputs`:

  * `version` (string): The target NVIDIA driver version number, such as `"595.129.03"`. If you specify only `version`, the orchestrator downloads the driver from the official NVIDIA repository (`https://us.download.nvidia.com/tesla/<version>`).
  * `gcsRunfile` (string): The Cloud Storage path of a custom NVIDIA driver installer file, which must use the format `gs://BUCKET_NAME/OBJECT_NAME.run`.
  * `sourceRunfile` (string): The relative path to an installer `.run` file inside the local workspace repository folder.

**Caution:** You can include the `InstallGPU` action only once inside the `steps` list of a customization recipe.

### Sample configurations

The following tabs show sample step configurations for installing a specific pre-packaged driver version versus installing a custom runfile:

###  Standard version download 

The following configuration downloads and installs a specified NVIDIA driver version from the official repository:
    
    
    - name: "Configure default NVIDIA drivers"
      action: InstallGPU
      inputs:
        version: "<var>DRIVER_VERSION</var>"
    

###  Cloud Storage runfile 

The following configuration deploys a custom NVIDIA driver `.run` installer directly from a Cloud Storage bucket:
    
    
    - name: "Deploy custom GPU driver from Cloud Storage"
      action: InstallGPU
      inputs:
        gcsRunfile: "gs://<var>BUCKET_NAME</var>/drivers/NVIDIA-Linux-aarch64-<var>DRIVER_VERSION</var>.run"
    

###  Local workspace runfile 

The following configuration deploys a custom NVIDIA driver `.run` installer from your local repository workspace:
    
    
    - name: "Deploy custom GPU driver from workspace"
      action: InstallGPU
      inputs:
        sourceRunfile: "drivers/NVIDIA-Linux-x86_64-<var>DRIVER_VERSION</var>.run"
    

### Configuration methods

The following tabs describe the supported methods for configuring NVIDIA GPU drivers on your custom images:

###  Precompiled drivers 

We recommend using pre-packaged driver versions to avoid the compute overhead and build time of compiling drivers from scratch.

  * **Container-Optimized OS (COS)** : If you specify a driver version pre-packaged by Google, the customization provisioner runs the guest tool `cos-extensions install gpu` to activate it.

To see the list of supported precompiled driver versions for your COS release, run `sudo cos-extensions list` on a running COS instance, or refer to [Identify the GPU driver version](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-gpus#identify-driver).

  * **Ubuntu** : To save build time on Ubuntu, we recommend selecting pre configured base images from the public `ubuntu-os-accelerator-images` project where NVIDIA drivers are preinstalled.

To list available accelerator images, run the following command in the `gcloud` CLI:
        
        gcloud compute images list \
            --project=ubuntu-os-accelerator-images \
            --no-standard-images
        




###  Custom runfiles 

If you must install a custom driver version that isn't precompiled by Google or Canonical, you can specify direct installer run files for compilation as follows:

  * **Ubuntu** : Performs in-guest compilation. The customization provisioner automatically installs the matching kernel headers (`linux-headers-$(uname -r)`), compiles the NVIDIA driver `.run` file on the worker VM, and registers it with Dynamic Kernel Module Support (DKMS). Registering with DKMS ensures the drivers remain active across minor kernel updates.
  * **Container-Optimized OS (COS)** : The compilation behavior varies depending on the CPU architecture of your source base VM image: 
    * **ARM64 Images** : Because ARM64 COS VMs don't support in-guest header compilation, Image Builder automatically cross-compiles your custom driver `.run` utility inside the build container and installs the resulting bundle into `/var/lib/nvidia` on the worker VM.
    * **x86-64 Images** : Performs in-guest compilation directly on the worker VM.



## What's next

  * Review top-level schema blocks in the [Image customization file schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema).
  * Configure pipeline orchestration parameters in the [Cloud Build configuration file schema](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema).
  * Follow the tutorial to [Create an Image Builder pipeline](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
