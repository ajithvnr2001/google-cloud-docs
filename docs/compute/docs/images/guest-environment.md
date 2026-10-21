---
url: https://docs.cloud.google.com/compute/docs/images/guest-environment/
title: Guest environment \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:56.103274+00:00
---

# Guest environment  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/guest-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Guest environment Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document provides an overview of the guest environment, which contains scripts, daemons, and binaries that instances need to run on Compute Engine.

The guest environment communicates with the metadata server, which is a per-instance HTTP server that runs alongside every Compute Engine instance. The metadata server provides the instance with essential configuration and operational data. For more information about the types of metadata that's stored on the metadata server, see [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

The guest environment is automatically installed on Compute Engine instances that are created by using most of the Google-provided public operating system (OS) images. Each OS image requires specific guest environment packages. These packages are built either by Google or the operating system distributor. Updates to guest environment packages are rolled out region by region. These updates can take up to two weeks to reach all locations globally. For more information, see Guest environment package repository rollouts.

For a full list of OS images that include the guest environment, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#user-space-features).

## Guest environment components

The following section describes the packages and services that enable an instance to communicate with Compute Engine.

### The guest agent

The central component of the guest environment is the guest agent, which handles tasks like account management, OS Login integration, and network interface management. The guest agent is available for both Linux and Windows operating systems, with the following package names:

  * Linux: `google-guest-agent`
  * Windows: `google-compute-engine-windows`



For detailed information about the guest agent, including its features, architecture, and how to manage the agent, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

### Linux components

The base components of a Linux guest environment are `deb` or `rpm` packages. Compute Engine creates these packages with the appropriate configurations for the supported distribution. To see the list of installed packages on your Linux instance, connect to the instance, and run the command provided for your OS version in the [Installed packages by operating system version](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages) table.

The Linux guest environment includes the following key packages.

Package name | Description | Key interactions | Link to source code on GitHub  
---|---|---|---  
`google-guest-agent` | This package is the guest agent for the Linux environment. The Linux guest agent contains the scripts that run on the guest OS to support Compute Engine features. For detailed information about the guest agent, including its features, architecture, and how to manage the agent, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent). | 

  * Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Sends logs to the serial port and optionally [Cloud Logging](https://cloud.google.com/products/operations)

| [guest-agent](https://github.com/GoogleCloudPlatform/guest-agent)  
`google-compute-engine` | Contains the scripts and files required for system initialization and configuration. This package contains the following:

  * System init scripts for `systemd`
  * System configurations, such as `udev` rules, `sysctl` rules, `rsyslog` configs, and `dhcp` configs, that are used for hostname setting 
  * Bash scripts that run during instance boot
  * A `gce-resolved.conf` file, introduced in October 2024, that ensures that domain lookups for `.local` Cloud DNS domains route to the metadata server. Without this file, domain lookups route through `systemd-resolved`, which frequently fails. If your environment doesn't use `.local` domains, you can remove the `gce-resolved.conf` file if it conflicts with your existing configurations.

| Works with the following packages to configure instances. 

  * `google-guest-agent`
  * `google-compute-engine-oslogin`

| [guest-configs](https://github.com/GoogleCloudPlatform/guest-configs)  
`google-compute-engine-oslogin` | Contains the necessary binaries, modules, and scripts to manage instance access using OS Login. OS Login lets you manage access to instances by using IAM roles. For more information about OS Login, see [OS Login](https://docs.cloud.google.com/compute/docs/oslogin). This package contains the following:

  * [Authorized Keys Command](https://github.com/GoogleCloudPlatform/guest-oslogin#authorized-keys-command): a command that uses the public SSH keys to authenticate users at login. 
  * [Name Service Switch (NSS) Modules](https://github.com/GoogleCloudPlatform/guest-oslogin#nss-modules): a service that provides the OS Login user and group information to the system. 
  * [Pluggable Authentication Modules (PAM)](https://github.com/GoogleCloudPlatform/guest-oslogin#pam-modules): a module that provides authorization (and authentication if two-factor support is enabled) support. This module lets the system use Google Cloud IAM permissions to control whether the system can log into an instance or perform operations as root (with `sudo`). 
  * `google_oslogin_nss_cache`: a utility for updating the local user and group cache. 
  * [`selinux`](https://github.com/GoogleCloudPlatform/guest-oslogin#selinux-policy): a package that contains SELinux policy definition files and a compiled policy package for configuring SELinux to support OS Login. 

| 

  * Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Send logs to the serial port and optionally [Cloud Logging](https://cloud.google.com/products/operations)

| [guest-oslogin](https://github.com/GoogleCloudPlatform/guest-oslogin)  
`gce-disk-expand` | Contains the components required for resizing a boot disk. | Sends logs to the serial port | [gce-disk-expand](https://github.com/GoogleCloudPlatform/guest-diskexpand)  
`google-osconfig-agent` | Contains the OS Config agent, which VM Manager uses to manage OS inventory, patches, and policies. For more information about the OS Config agent, see [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager).  |  Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) By default, the OS Config agent doesn't collect or send any information until you [enable the OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata). After you enable the agent, the agent communicates with the OS Config API service. To review the operations completed by the agent, see [VM Manager audit logging](https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging). | [guest-osconfig](https://github.com/GoogleCloudPlatform/guest-osconfig)  
  
### Windows components

All Google-provided Windows OS images are preconfigured with the `GooGet` tool and Google Cloud repositories. `GooGet` installs and maintains the guest environment for Windows instances. If you need to install `GooGet` and set up repositories, see [Packaging and package distribution](https://github.com/GoogleCloudPlatform/compute-image-windows#packaging-and-package-distribution) in the `compute-image-windows` GitHub repository. To see the list of installed packages on your Windows instance, connect to the instance and run `googet installed`.

The Windows guest environment includes the following key packages:

Package name | Description | Key interactions | Link to source code on GitHub  
---|---|---|---  
`google-compute-engine-windows` | This package is the guest agent for the Windows environment. The Windows guest agent contains the scripts that run on the guest OS to support Compute Engine features. For detailed information about the guest agent, including its features, architecture, and how to manage the agent, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent). | 

  * Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Sends logs to the Windows Application Event Log, serial port, and [Cloud Logging](https://cloud.google.com/products/operations)

| [guest-agent](https://github.com/GoogleCloudPlatform/guest-agent)  
`google-compute-engine-sysprep` | Contains scripts for [generalizing a Windows instance](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11) in preparation for creating an OS image. The package also includes the `instance_setup.ps1` script that runs on first boot to configure the new instance.  | 

  * Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Sends logs to the Windows Application Event Log and serial port

| [sysprep](https://github.com/GoogleCloudPlatform/compute-image-windows/tree/master/sysprep)  
`google-compute-engine-metadata-scripts` | Contains scripts and binaries that run `sysprep-specialize`, [startup](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows), and [shutdown](https://docs.cloud.google.com/compute/docs/shutdownscript#provide_a_shutdown_script_on_windows_instances) scripts. | 

  * Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Reads data from Cloud Storage locations when the `sysprep-specialize-script-url` and `windows-startup-script-url` are used 
  * Sends logs to the Windows Application Event Log, serial port, and [Cloud Logging](https://cloud.google.com/products/operations)

| [google_metadata_script_runner](https://github.com/GoogleCloudPlatform/guest-agent/tree/main/google_metadata_script_runner)  
`google-compute-engine-powershell` | Contains a PowerShell module. This module provides common functions that PowerShell scripts in the other Windows guest environment scripts use. | Sends logs to the Windows Application Event Log and the serial port | [PowerShell](https://github.com/GoogleCloudPlatform/compute-image-windows/tree/master/powershell)  
`google-compute-engine-auto-updater` | Contains scripts that update the Compute Engine packages daily. This package isn't installed by default. This approach lets you maintain the stability of your environment by controlling the update process. If your environment can tolerate updates without disruption, you can install this package to ensure your guest environment packages are updated automatically. To install this package, use the following command: `googet -noconfirm install google-compute-engine-auto-updater` | 

  * Reads data from [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Calls the `GooGet` agent to send logs to the Windows Application Event Log and console

| [auto_updater](https://github.com/GoogleCloudPlatform/compute-image-windows/tree/master/auto_updater)  
`google-compute-engine-diagnostics` | Contains a binary that [collects diagnostic information](https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-diagnostic-information) from the instance and saves the information to a Cloud Storage bucket. The Windows guest agent executes the binary. | Saves data to a Cloud Storage bucket | [diagnostics](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/cli_tools/diagnostics)  
`certgen` | Contains a binary that creates a certificate on the instance. |  | [certgen](https://github.com/GoogleCloudPlatform/compute-image-windows/tree/master/certgen/)  
`GooGet` | Contains a binary that installs and maintains the guest environment for Windows instances. | Reads data from the Google Cloud repositories located at `packages.cloud.google.com` | [GooGet](https://github.com/google/googet)  
`google-compute-engine-vss` | Installs the Compute Engine VSS agent and provider that takes [persistent disk snapshots](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) using Microsoft's [Volume Shadow Copy Service (VSS)](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) | Communicates with the Google Cloud snapshot service | [vss](https://github.com/GoogleCloudPlatform/compute-image-windows/tree/master/third_party/vss)  
`google-osconfig-agent` | Contains the OS Config agent, which VM Manager uses to manage OS inventory, patches, and policies. For more information about the OS Config agent, see [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager).  |  Reads data from and writes data to the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) By default the OS Config agent doesn't collect or send any information until you [enable the OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata). After you enable the agent, the agent communicates with the OS Config API service. To review the operations the agent completes, see [VM Manager audit logging](https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging). | [guest-osconfig](https://github.com/GoogleCloudPlatform/guest-osconfig)  
Compute Engine Windows drivers |  Contains several drivers to ensure proper functionality and performance of instances. The [`GooGet`](https://github.com/google/googet) package manager manages these drivers and publishes them to Google Cloud repositories. The following Compute Engine drivers are maintained for Windows OS images: | Driver type | Driver package name  
---|---  
Ethernet adapter | `google-compute-engine-driver-netkvm`  
[SCSI disk](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface) | `google-compute-engine-driver-vioscsi`  
[Display adapter](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) | `google-compute-engine-driver-gga`  
[Crash handler](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows) | `google-compute-engine-driver-pvpanic`  
[Virtio memory balloon driver](https://docs.cloud.google.com/compute/docs/dynamic-resource-management) | `google-compute-engine-driver-balloon`  
[Google virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) | `google-compute-engine-driver-gvnic`  
  
To install or upgrade a specific driver, run the following command: 
    
    
            googet install DRIVER_PACKAGE_NAME
            

| [compute-windows-drivers](https://github.com/GoogleCloudPlatform/compute-windows-drivers)  
  
## Guest environment package repository rollouts

Starting September 3, 2026, Compute Engine is transitioning the deployment of Guest Environment package repositories from a global rollout to a regional rollout framework for Linux and Windows compute instances.

### Key changes

  * **Regional rollout framework:** Updates to the default stable repository track are made available on a region-by-region basis, rather than globally all at once.
  * **Staged delivery window:** Package updates may take up to two weeks to reach all locations globally.
  * **Global repository track:** A dedicated global repository track is available for workloads requiring multi-region version consistency. Package updates published to the global repository track continue to deploy simultaneously across all regions worldwide after the regional repositories have all been updated.



### Potential impact

  * **Version variations:** During the two-week regional rollout window, multi-region workload deployments using the default stable repository might see different guest environment package versions across active regions.
  * **Automation adjustments:** If you have automations, CI/CD pipelines, or patching processes that expect multi-region package consistency, you might need to update those systems to use the global repository track.



### Decide whether to use the regional rollouts or the global repository track

  * **If your workloads can tolerate regional version variations during updates:** No action is required.
  * **If your workflows require multi-region package consistency:** Update your package manager configuration (APT, YUM/DNF, Zypper, or GooGet) before September 3, 2026, to point to the new global repository.



### Package manager configuration changes

To switch your package manager from the default regional track to the global repository track, update the repository configuration for your package manager to point to the global track (`-global`).

  * **APT (Debian)**

In `/etc/apt/sources.list.d/google-cloud.list`, change the repository name from `google-compute-engine-${VERSION_CODENAME}-stable` to `google-compute-engine-${VERSION_CODENAME}-global`:
        
        deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-compute-engine-${VERSION_CODENAME}-global main
        

  * **YUM and DNF (RHEL, CentOS, Rocky Linux)**

In your repository file (such as `/etc/yum.repos.d/google-cloud.repo`), update the repository entry to use the global track name:
        
        [google-cloud-compute-global]
        name=Google Cloud Compute Engine Global
        baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-compute-${DISTRO}-${ARCH}-global
        enabled=1
        gpgcheck=1
        

  * **GooGet (Windows)**

Add or update the GooGet repository to point to `google-compute-engine-global`:
        
        googet addrepo google-compute-engine-global https://packages.cloud.google.com/yuck/repos/google-compute-engine-global
        




## What's next

  * Learn how to [Install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment).
  * Learn about the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
