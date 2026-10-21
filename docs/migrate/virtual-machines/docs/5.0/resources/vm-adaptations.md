---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations/
title: Adapt VM instances to run on Google Cloud \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:58.235784+00:00
---

# Adapt VM instances to run on Google Cloud  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Resources ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources)



Send feedback 

#  Adapt VM instances to run on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

To function properly on Google Cloud, migrated VMs and imported images require changes to their configuration. These changes are referred to as _OS adaptations_. Migrate to Virtual Machines performs OS adaptations automatically at the end of each replication cycle and during the image import process.

OS adaptations are made to both Linux and Windows VMs. At a high level, these adaptations include changes to:

  * Enable booting on Google Cloud
  * Enable the serial console
  * Configure network settings
  * Install packages required by the VM to enable Google Cloud features and functionality



The specific changes for both Linux and Windows VMs are described below.

## Linux adaptations

At the end of each replication cycle for a Linux VM, Migrate to Virtual Machines performs OS adaptations on the replicated VM. These adaptations include:

  * Configuring NIC to use DHCP

    * If it exists, remove persistent network `udev` rules.
  * If the [VMware Tools/open-vm-tools](https://github.com/vmware/open-vm-tools) service is already installed, disable and try to uninstall it. Note: You can safely uninstall the VMware Tools/open-vm-tools service manually post migration, or leave it disabled.

  * Set the bootloader to print console logs to serial port 1.

  * Validate virtio drivers:

    * If virtio drivers are not available in the default kernel, choose an existing kernel which is compatible with virtio driver.

    * If virtio drivers are missing from `initrd` then rebuild `initrd` with virtio drivers.

  * Add Google Cloud repositories to the repository list. These repositories include:

    * <https://packages.cloud.google.com/yum/>
    * <https://packages.cloud.google.com/apt/>
  * Install the following Google packages:

    * `google-compute-engine` packages for [Compute Engine](https://docs.cloud.google.com/compute) support

    * `google-osconfig-agent` package for the [OS Config agent](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management)

    * `google-cloud-sdk` package for the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs)

  * Set `systemd.target` to multiuser.

  * Where applicable, set `fstab` to use volume UUIDs.

  * If target instance license is PAYG:

    * Red Hat - Install the `google-rhui-client-rhel` package specific to the Red Hat version.

    * SLES - Install Google's region service client packages.

  * If the OS is Oracle Linux with a Unbreakable Enterprise Kernel Release 7 (UEK7) kernel, install the `kernel-uek-modules-extra` package for [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) support.




These adaptations require free space on the following partitions:

  * Up to 640 MiB in `/root`
  * Up to 128 MiB in `/boot`
  * Up to 64 MiB in `/var`
  * Up to 32 MiB in `/tmp`



## Windows adaptations

At the end of each replication cycle for a Windows VM, Migrate to Virtual Machines performs OS adaptations on the replicated VM. These adaptations include:

  * Set bootloader to print console logs to serial port 2.

  * Enable RDP.

  * Configure the power scheme:

    * Disable hibernation mode.

    * Set power scheme to balanced.

    * Disable `display turn off` in power configurations.

  * Disable startup animation.

  * Disable CTRL-ALT-DEL.

  * If the [VMware Tools/open-vm-tools](https://github.com/vmware/open-vm-tools) service is already installed, disable and try to uninstall it. Note: You can safely uninstall the VMware Tools/open-vm-tools service manually post migration, or leave it disabled.

  * Set the time:

    * Change timezone to UTC.

    * Configure NTP.

  * Add access to instance metadata:

    * Add allow access rule to instance metadata server IP address in Windows firewall.

    * Add instance metadata server to hosts file.

  * On first boot:

    * If target instance license is PAYG (default), then register KMS and Windows activation.

    * Configure DHCP settings.

    * Install Google [guest packages](https://docs.cloud.google.com/compute/docs/images/guest-environment#windows)




These adaptations may require up to 1.25 GiB of free space on drive `C`.

**Note:** Windows first boot might take a while. If Windows was not gracefully shut down, it may invoke a Check Disk (`chkdsk`) scan before starting. Additionally, setting up network devices for the first time might take several minutes.

## Adaptation reports

Migrate to Virtual Machines generates adaptation reports during your replication cycles, clones, and cut-over cycles for you to use for troubleshooting, problem solving, and deeper insight into your migration process.

For more information about adaptation reports, see [Adaptation reports](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#adaptation_report).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
