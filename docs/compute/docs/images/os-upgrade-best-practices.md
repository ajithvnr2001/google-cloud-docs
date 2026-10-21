---
url: https://docs.cloud.google.com/compute/docs/images/os-upgrade-best-practices/
title: Operating system upgrade best practices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:00:12.338458+00:00
---

# Operating system upgrade best practices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/os-upgrade-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Operating system upgrade best practices Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes best practices and strategies for upgrading operating systems on Compute Engine instances. Learn how to upgrade major OS versions by using immutable infrastructure, re-creation of instances, or in-place workflows, and how to automate routine security patching.

When an operating system version approaches its end of support (EOS) or end of life (EOL), you must upgrade to a supported OS version to maintain security updates, software compatibility, and Google Cloud platform integration. For more information about support phases, see [Operating systems lifecycle](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle).

## Risks of in-place major OS version upgrades

If you perform a major in-place upgrade of the operating system—such as upgrading Debian 12 to 13, RHEL 9 to 10, or Ubuntu 24.04 to 26.04 on a running compute instance—then you introduce significant operational risks in cloud environments. Unlike on-premises physical servers, your compute instances depend on specialized packages for the guest environment to communicate with the hypervisor and Compute Engine metadata server.

When you upgrade an operating system in place, you risk the following failure modes:

  * **Loss of SSH and RDP connectivity:** Configuration formats for network services, guest-level firewall rules, such as ufw or firewalld, or SSH daemon settings can change between OS versions, cutting off remote administrative access.
  * **Disruption of the guest environment:** The [`google-guest-agent`](https://docs.cloud.google.com/compute/docs/images/guest-agent) and [`google-oslogin`](https://docs.cloud.google.com/compute/docs/oslogin) packages manage SSH keys, user accounts, network interfaces, and synchronization with metadata. If package repositories or dependencies break during a distribution upgrade, the guest agent might stop running, preventing further sign-ins or network configuration.
  * **Incompatibilities with storage and kernel drivers:** Changes to the kernel, `initramfs`, or drivers for disk controllers (such as virtio-scsi or NVMe) can cause boot failures or prevent the compute instance from recognizing attached Persistent Disk volumes.
  * **Inconsistent configurations for repositories:** Operating system vendors often deprecate or replace legacy package repositories and signing keys, which can cause package managers to fail mid-upgrade and leave the operating system in an unrecoverable, half-installed state.



To avoid these risks, use an immutable infrastructure model rather than upgrading major OS versions in place on your production compute instances.

## Choose the right upgrade strategy

Depending on whether your workloads are stateless or stateful, choose one of the following strategies:

Strategy | Recommended for | Downtime risk | Rollback mechanism  
---|---|---|---  
Immutable infrastructure | Stateless workloads, managed instance groups (MIGs), microservices, container hosts | Zero downtime with rolling replacement | Revert the instance template to an earlier image  
Re-create compute instances with Persistent Disk | Stateful standalone compute instances, databases with attached secondary storage, legacy application hosts | Minimal with a planned maintenance window | Reattach disks to the original compute instance or restore snapshots  
In-place upgrade of the OS | Standalone compute instances where you cannot automate or extract local configurations | High, requiring downtime and manual recovery planning | Restore from a Persistent Disk snapshot  
  
## Immutable infrastructure

The safest and most reliable way to upgrade your operating systems is by using the immutable infrastructure model. Instead of modifying running compute instances, you build new compute instances from updated public or custom OS images and replace your legacy instances.

If your workloads run in [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) (MIGs), then you can automate this rollout with zero service downtime.

### Create an updated image

  1. Select the latest public OS image from the supported [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) list, or create a custom base image using [Image Builder](https://docs.cloud.google.com/compute/docs/images/image-builder/overview) or automated tools such as Packer or Ansible.
  2. Verify that your application and dependencies install and run successfully on the new OS version in a non-production test environment.
  3. Create a custom OS image or reference the new public image family. For more information, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).



### Create an updated instance template

Create a new instance template that references the updated OS image:
    
    
    gcloud compute instance-templates create NEW_TEMPLATE_NAME \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --machine-type=MACHINE_TYPE \
        --region=REGION
    

Replace the following:

  * `NEW_TEMPLATE_NAME`: the name for the new instance template.
  * `IMAGE_FAMILY`: the image family of the target OS, such as `debian-12` or `ubuntu-2404-lts`.
  * `IMAGE_PROJECT`: the project hosting the image, such as `debian-cloud` or `ubuntu-os-cloud`.
  * `MACHINE_TYPE`: the machine type for your instances.
  * `REGION`: the Compute Engine region where you create the template.



### Perform a rolling replacement in the MIG

Apply the updated template to your managed instance group and initiate a rolling replacement:
    
    
    gcloud compute instance-groups managed rolling-action replace MIG_NAME \
        --max-surge=20% \
        --max-unavailable=0 \
        --region=REGION
    

Replace the following:

  * `MIG_NAME`: the name of your managed instance group.
  * `REGION`: the region where your MIG is located. For zonal MIGs, replace `--region=REGION` with `--zone=ZONE`.

**Note:** Setting `--max-unavailable=0` ensures that Compute Engine creates and verifies new instances before terminating older instances, maintaining continuous application availability.

## Re-create compute instances with Persistent Disk

If you run stateful standalone compute instances where applications store configuration and data on Persistent Disk volumes, then you can upgrade your operating system by re-creating the compute instance with a fresh boot disk while preserving your data disks.

### Back up all disks

Before modifying infrastructure, create standard or regional snapshots of the boot disk and all attached Persistent Disk volumes:
    
    
    gcloud compute disks snapshot BOOT_DISK_NAME \
        --snapshot-names=SNAPSHOT_NAME \
        --zone=ZONE
    

Replace the following:

  * `BOOT_DISK_NAME`: the name of the boot disk to back up.
  * `SNAPSHOT_NAME`: the name for the new Persistent Disk snapshot.
  * `ZONE`: the zone where the disk is located.



For more information, see [Create and manage snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

### Separate application data from the boot disk

Make sure that application data, database files, and transaction logs reside on secondary Persistent Disk volumes or external services, such as Cloud Storage or Cloud SQL, rather than on the boot disk.

### Create the replacement compute instance

  1. Stop the legacy compute instance to make sure that data remains consistent:
         
         gcloud compute instances stop LEGACY_INSTANCE_NAME --zone=ZONE
         

  2. Detach the secondary data disks from the legacy compute instance:
         
         gcloud compute instances detach-disk LEGACY_INSTANCE_NAME \
             --disk=DATA_DISK_NAME \
             --zone=ZONE
         

  3. Create a new compute instance with the target OS version:
         
         gcloud compute instances create NEW_INSTANCE_NAME \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE
         

  4. Attach the existing secondary data disks to the new compute instance:
         
         gcloud compute instances attach-disk NEW_INSTANCE_NAME \
             --disk=DATA_DISK_NAME \
             --zone=ZONE
         

  5. Connect to the new compute instance, mount the filesystems on the data disks, and start your application services.

  6. If necessary, reassign any static external IP addresses or DNS records to point to the new compute instance.




Replace the following:

  * `LEGACY_INSTANCE_NAME`: the name of the existing compute instance you are upgrading.
  * `DATA_DISK_NAME`: the name of the secondary Persistent Disk volume to detach and reattach.
  * `NEW_INSTANCE_NAME`: the name for the new replacement compute instance.
  * `IMAGE_FAMILY`: the image family for the target OS version, such as `debian-13` or `ubuntu-2604-lts`.
  * `IMAGE_PROJECT`: the project that provides the image, such as `debian-cloud` or `ubuntu-os-cloud`.
  * `MACHINE_TYPE`: the machine type for the new compute instance.
  * `ZONE`: the zone where your compute instances are located.



## In-place OS upgrades

If you cannot re-create your compute instance because of complex manual configurations, and you must perform an in-place upgrade, then complete these pre-upgrade checks and follow the distribution-specific instructions carefully.

### Pre-upgrade checklist

Complete every step in this checklist before starting an in-place upgrade:

  1. Take a snapshot of the boot disk before running any upgrade commands. This is your primary recovery mechanism if the upgrade fails.
  2. Update all current packages and the guest environment for Google Cloud to the latest versions available for your current OS release:

     * For Debian and Ubuntu: `sudo apt update && sudo apt dist-upgrade -y`
     * For RHEL, CentOS, and Rocky Linux: `sudo dnf upgrade -y`
     * For SLES: `sudo zypper update`

Make sure that the `google-guest-agent` and `google-oslogin` packages are active:
    
    sudo systemctl status google-guest-agent
    

  3. Enable the interactive serial console on your compute instance so you can troubleshoot and sign in if SSH or networking stops working during the upgrade:
         
         gcloud compute instances add-metadata INSTANCE_NAME \
             --metadata=serial-port-enable=TRUE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of your compute instance.
     * `ZONE`: the zone where your compute instance is located.

For more information, see [Interacting with the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console).

  4. If you use OS Login or SSH keys managed by the guest agent, then set a password for a local user account with administrative privileges, such as with `sudo passwd USERNAME`, so you can sign in through the serial console if OS Login is temporarily unavailable during the upgrade. Replace `USERNAME` with the name of your local user account.

  5. Make sure that the root partition `/` and boot partition `/boot` have sufficient free space, with at least 5 GB recommended, to download and unpack new packages:
         
         df -h / /boot
         

  6. Verify that third-party agents for security, backup, or monitoring (including the Google Cloud Ops Agent) support the target version of the operating system.




### In-place upgrade procedures

The following sections provide high-level workflows for common operating systems. Always consult the official upgrade documentation for your operating system before upgrading.

###  Debian 

You can upgrade Debian between consecutive major releases. Don't skip major versions—for example, upgrade Debian 11 to 12 first, and then upgrade Debian 12 to 13.

  1. Update the existing Debian package repositories:
         
         sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y
         

  2. Update package sources in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/` by replacing the current release codename, such as `bullseye`, with the target release codename, such as `bookworm`. Make sure that the Google Cloud package repository URLs match the new release.

  3. Perform a minimal upgrade to update core packaging tools:
         
         sudo apt update
         sudo apt upgrade --without-new-pkgs -y
         

  4. Run the full distribution upgrade:
         
         sudo apt full-upgrade -y
         

  5. Verify that `google-guest-agent` is active and enabled:
         
         sudo systemctl enable --now google-guest-agent
         

  6. Reboot the compute instance:
         
         sudo systemctl reboot
         




###  Ubuntu 

To manage LTS-to-LTS upgrades on Ubuntu, use the `do-release-upgrade` tool.

  1. Update all current packages:
         
         sudo apt update && sudo apt dist-upgrade -y
         

  2. Install the core package for the update manager:
         
         sudo apt install update-manager-core -y
         

  3. Start the tool for release upgrades:
         
         sudo do-release-upgrade
         

  4. Follow the interactive prompts to confirm repository updates and package replacements. If prompted about modified configuration files, review the differences carefully before overwriting.

  5. Reboot the compute instance when prompted.




###  RHEL 

To upgrade between major RHEL versions, use the supported Red Hat `leapp` utility.

  1. Verify your Red Hat subscription status and make sure that the compute instance connects to the Compute Engine Red Hat Update Infrastructure (RHUI).
  2. Install the Leapp utility and the packages that contain migration data.
  3. Run the pre-upgrade assessment:
         
         sudo leapp preupgrade
         

  4. Review the report in `/var/log/leapp/leapp-report.txt` and resolve all inhibitor issues that Leapp identifies.

  5. Execute the upgrade:
         
         sudo leapp upgrade
         

  6. Reboot the instance to let Leapp perform the OS upgrade in an isolated environment:
         
         sudo reboot
         




###  SLES 

To perform major version service pack migrations and distribution upgrades on SLES, use `zypper`:

  1. Update the existing system:
         
         sudo zypper patch
         

  2. Run `zypper migration` to perform an online migration, or follow the distribution upgrade workflow, using `zypper dup`, specified in the [SLES upgrade documentation](https://documentation.suse.com/).




###  Windows 

For Windows Server compute instances, you can use installation media with Compute Engine volume licensing and PowerShell scripts to automate upgrades without manual intervention.

To perform an in-place upgrade on Windows Server, follow the tutorial to [perform an in-place upgrade of Windows Server](https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server).

## Automate patch management for minor updates

Distinguish major OS version upgrades from routine minor updates and security patches. For regular maintenance of software, package updates, and patching of CVEs, use [VM Manager Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch) to automate the deployment of patches across your fleet of compute instances.

Follow these best practices to manage patches automatically:

  * **Organize instances with labels:** Assign labels with metadata, such as `env:dev`, `env:prod`, and `tier:frontend`, to target specific groups of compute instances for patches.
  * **Deploy zone by zone:** Stagger patch jobs across zones and regions. Never apply patch jobs to all zones simultaneously in production environments.
  * **Use pre-patch and post-patch scripts:** Configure pre-patch scripts to safely drain connections or pause services, and configure post-patch scripts to run health checks before returning instances to service.
  * **Monitor patch compliance:** Use the dashboard for VM Manager in the Google Cloud console to track compliance with patches and the status of vulnerabilities across your fleet of compute instances.



For more information, see [Create patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).

## Post-upgrade verification and troubleshooting

After completing an upgrade, perform the following verification steps:

  1. Confirm that SSH or RDP connects normally.
  2. Make sure that the guest agent and the service for OS Login are active and reporting healthy status:
         
         sudo systemctl status google-guest-agent
         sudo systemctl status google-oslogin-cache
         

  3. Verify that the compute instance can query the instance metadata server:
         
         curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/id
         

  4. Confirm that your application services started and that health checks from load balancers report healthy instances.




### Troubleshoot connection loss

If you lose SSH or RDP access to the compute instance after an in-place upgrade, then complete the following troubleshooting steps:

  1. Check the console log for kernel panics, errors during service startup, or failures during network initialization:
         
         gcloud compute instances tail-serial-port-output INSTANCE_NAME \
             --zone=ZONE
         

  2. If you enabled the interactive serial console before the upgrade, then connect directly to the terminal:
         
         gcloud compute connect-to-serial-port INSTANCE_NAME \
             --zone=ZONE
         

Sign in using your local user credentials, inspect system logs with `journalctl -xe`, and restart networking or the `google-guest-agent` service.

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance you are troubleshooting.
     * `ZONE`: the zone where the compute instance is located.
  3. If the operating system cannot boot or recover, then create a new Persistent Disk volume from the snapshot that you took before the upgrade and attach it as the boot disk of the compute instance. For detailed recovery steps, see [Restore a snapshot into a new disk](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).




## What's next

  * [Learn about operating system lifecycle stages and deprecation policies](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle).
  * [Review image management best practices](https://docs.cloud.google.com/compute/docs/images/image-management-best-practices).
  * [Understand the guest environment components and daemons](https://docs.cloud.google.com/compute/docs/images/guest-environment).
  * [Set up automated patch jobs by using VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Perform an in-place upgrade of Windows Server](https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
