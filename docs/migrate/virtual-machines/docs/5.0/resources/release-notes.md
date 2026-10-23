---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/release-notes/
title: Migrate to Virtual Machines 5.0 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:28.876150+00:00
---

# Migrate to Virtual Machines 5.0 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Resources ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources)



Send feedback 

#  Migrate to Virtual Machines 5.0 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Migrate to Virtual Machines. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/migrategce-release-notes.xml) directly. 

## April 22, 2026

Feature

Migrate to Virtual Machines now lets you use regional disks for the target virtual machine (VM) instance.

## April 20, 2026

Feature

Migrate to Virtual Machines now supports the following operating systems for VMware, AWS, Azure, and image import sources:

  * Red Hat Enterprise Linux 10
  * CentOS 10
  * AlmaLinux 10
  * Oracle Linux 10
  * Rocky Linux 10



CentOS is not supported on ARM architecture.

## November 17, 2025

Feature

You can now use [Hyperdisk Storage Pools](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target) with migrating VMs if you need large-scale storage. Hyperdisk Storage Pools help you manage large-scale storage and can optimize costs and performance.

## October 16, 2025

Feature

Migrate to Virtual Machines now supports all available versions of AlmaLinux EL 8 and 9.

## August 25, 2025

Feature

**Generally available:** The Basic Input/Output System (BIOS) to Unified Extensible Firmware Interface (UEFI) conversion option is now generally available. Migrate to Virtual Machines lets you convert the OS boot type of a VM instance from BIOS to UEFI. This option is useful when you want to securely boot your VM instance, as secure boot is only supported by UEFI. For more information, see the table in [Configure the target for a migrated VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).

## June 20, 2025

Feature

Starting with version Migrate Connector 2.7, throttling is supported for a second NIC.

## May 07, 2025

Feature

Migrate to Virtual Machines now introduces an expiration time for a migrating VM. A migrating VM is a VM that you create during the migration process to migrate your workloads to Google Cloud.

A migrating VM stays active for 100 days from the time that the VM appears in the VM Migrations tab. After 100 days, the VM is moved to the `EXPIRED` state and stays in the `EXPIRED` state for 30 days. If you need more time to complete your migration, you can extend the lifespan of the migrating VM by an additional 100 days. You can only extend the lifespan of a migrating VM two weeks before the VM expires and throughout the expiration period (between 86 to 130 days from the creation of the VM). If you don't extend the lifespan of the VM during this period, the VM expires.

## April 03, 2025

Feature

Migrate to Virtual Machines supports importing Arm disk images to Google Cloud. For information on operating systems supporting this feature, see [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#image-import).

## March 19, 2025

Feature

**Generally available:** Migrate to Virtual Machines support for the Arm64 migration journey is now generally available. This feature lets you migrate Arm virtual machine (VM) instances from [AWS](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#aws-source) and [Azure cloud services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#azure-source) to Arm VM instances on Compute Engine, and it is supported for the following operating systems:

  * Debian 11 and 12
  * RHEL 9
  * Rocky Linux 8 and 9
  * SLES 15 SP5
  * Ubuntu 20.04 and 22.04



## March 12, 2025

Feature

**Experimental:** Migrate to Virtual Machines now supports the migration of VM instances running Amazon Linux 2 to Rocky Linux 8 as part of an open access experimental program. In order to migrate a VM running Amazon Linux 2, Migrate to Virtual Machines first converts Amazon Linux 2 to Rocky Linux 8, and then completes the migration. 

**Note:** Some VM instances can't be automatically converted from Amazon Linux 2 to Rocky Linux 8. In such cases, we recommend that you use the VM Disk Migration feature to first migrate your VM's disks to Google Cloud. You can then rebuild the VM instances using a Google Cloud OS image and the migrated disks.

## November 14, 2024

Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) Migrate to Virtual Machines lets you [migrate Elastic Block Store (EBS) volumes not attached to a VM from AWS to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-unattached-disks), as part of a preview program. Use this feature when you have detached the disks associated with a VM to archive data and need to migrate these disks to Google cloud. 

To participate in the preview, contact us at [**m2vm-independent-disks-migration@google.com**](mailto:m2vm-independent-disks-migration@google.com).

## September 16, 2024

Change

As [Container Registry is deprecated](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr), Migrate to Virtual Machines is transitioning from Container Registry to Artifact Registry to store images running on Migrate Connector. This transition will be completed by October 15, 2025. For the most part, this change should not affect your usage of Migrate Connector or Migrate to Virtual Machines. However, for some configurations, you might have to add [VPC-SC rules](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#step-4) to allow Migrate Connector to access Artifact Registry. If you need help using Artifact Registry with Migrate to Virtual Machines, contact the Migrate to Virtual Machines support team.

## September 04, 2024

Feature

**Experimental:** As CentOS Linux 7 has reached end-of-life (EOL) on June 30, 2024, Migrate to Virtual Machines lets you convert CentOS Linux 7 to Rocky Linux 8 as part of your migration.

**Note:** This product or feature is subject to the **Pre-GA Offerings Terms** in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). Pre-GA products and features are available _as is_ and might have limited support.

## August 21, 2024

Deprecated

On April 30, 2024, the 4.x versions of Migrate for Compute Engine reached end of life, and the product was deprecated on Google Cloud.

To migrate your virtual machines (VMs) to Compute Engine, use [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0).

## July 24, 2024

Feature

**Generally available:** Migrate to Virtual Machines lets you [import a machine image from a virtual appliance](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import). You can use machine images to store the configuration, metadata, permissions, and data from one or more disks for a virtual machine (VM) instance running on Compute Engine.

## July 10, 2024

Security

The [Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector), the virtual appliance used to connect VMware sources to Migrate to Virtual Machines, is exposed to a security vulnerability on SSHD ([CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)). Migrate Connector version 2.6.2497 has been released to mitigate this issue and is being gradually rolled out. For information, see the [GCP-2024-040 security bulletin](https://docs.cloud.google.com/migrate/virtual-machines/docs/security-bulletins#gcp-2024-040).

## July 01, 2024

Feature

**Generally available:** Migrate to Virtual Machines lets you [import a virtual disk image to a Compute Engine image](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import). If you have virtual disk images with software and configurations that you need, you can save time by importing these virtual disk images to [Compute Engine images](https://docs.cloud.google.com/compute/docs/images), and use this image to create virtual machine instances or persistent disks.

## April 30, 2024

Feature

Migrate to Virtual Machines now supports [importing virtual disk image files in the following formats](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import#supported-formats):

  * QEMU copy-on-write (QCOW)
  * QEMU copy-on-write 2 (QCOW2)
  * QEMU enhanced disk format (QED)
  * VPC
  * Virtual disk image (VDI)
  * Virtual hard disk v2 (VHDX)
  * Virtual hard disk (VHD)



In addition to these formats, Virtual machine disk (VMDK), and raw files compressed as a _.tar.gz_ file are also supported.

## March 26, 2024

Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) Migrate to Virtual Machines supports the ARM64 migration journey. This feature lets you migrate ARM virtual machine (VM) instances from [AWS](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#aws-source) and [Azure cloud services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#azure-source) to ARM VM instances on Compute Engine, and it is supported for the following operating systems:

  * Debian 11 and 12
  * RHEL 9
  * Rocky Linux 8 and 9
  * SLES 15 SP5
  * Ubuntu 20.04 and 22.04



## March 04, 2024

Feature

**Generally available:** You can now use [Customer-Managed Encryption Keys (CMEK) in Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/cmek) to do the following:

  * Protect data stored by Migrate to Virtual Machines during the migration process.
  * Protect data of the migrated VMs created by clone and cut-over operations for all sources - [AWS](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-aws-source#create_an_aws_source), [Azure](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source#create-an-azure-source), and [VMware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrate-connector#register).



Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) Migrate to Virtual Machines lets you [import a virtual disk image to a Compute Engine image](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import). If you have virtual disk images with software and configurations that you need, you can save time by importing these virtual disk images to [Compute Engine images](https://docs.cloud.google.com/compute/docs/images), and use this image to create virtual machine instances or persistent disks.

## February 26, 2024

Feature

**Generally available:** Migrate to Virtual Machines lets you [migrate virtual machine (VM) disks to Persistent Disk volumes on Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks). The migrated disks can be attached to a new VM during the migration process, or an existing VM after the migration is complete.

## January 17, 2024

Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) Migrate to Virtual Machines lets you convert the OS boot type of a VM instance from Basic Input/Output System (BIOS) to Unified Extensible Firmware Interface (UEFI). This option is useful when you want to securely boot your VM instance, as secure boot is only supported by UEFI. For more information, see the table in [Configure the target for a migrated VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).

To participate in the preview of this feature, send a request to the email address: [**m2vm-bios-to-uefi@google.com**](mailto:m2vm-bios-to-uefi@google.com).

## December 27, 2023

Feature

**Generally Available:** Migrate to Virtual Machines supports migrating virtual machine instances (VMs) to Compute Engine [1st, 2nd, and 3rd generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). For more information, see [Support for Compute Engine machine series](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/supported-os-versions#migrate-to-machine-series).

## November 14, 2023

Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) You can now use Customer-Managed Encryption Keys (CMEK) in Migrate to Virtual Machines to do the following:

  * Protect data stored by Migrate to Virtual Machines during the migration process.
  * Protect data of the migrated VMs created by clone and cut-over operations for all sources - [AWS](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-aws-source#create_an_aws_source), [Azure](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source#create-an-azure-source), and [VMware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrate-connector#register).



## October 11, 2023

Feature

[**Preview:**](https://cloud.google.com/products/#product-launch-stages) Migrate to Virtual Machines now supports migrating VMs to the C3, H3, and M3 machine types. These machine types support non-volatile memory express (NVMe) and Google Virtual NIC (gVNIC). Before you migrate your VMs to any of these machine types, ensure that source VMs support NVMe and gVNIC. For more information on different machine types that support NVMe and gVNIC, go to the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) section, click **Choose VM properties to compare** , and select **Disk interface type** and **Network interfaces**.

## October 10, 2023

Feature

**Generally Available:** [Migrate to Virtual Machines from an Azure](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source) source lets you migrate VM instances running on Azure to Google Cloud Compute Engine.

## September 26, 2023

Feature

[**Preview**](https://cloud.google.com/products/#product-launch-stages): Migrate to Virtual Machines lets you [migrate the disks of source virtual machine (VM) instances to Persistent Disk volumes on Google Cloud](https://cloud.corp.google.com/migrate/virtual-machines/docs/5.0/how-to/migrating-disks#configure-target) with the following options:

  * Migrate the Persistent Disk volumes without attaching them to a VM instance
  * Create a new VM instance and attach the migrated Persistent Disk volumes to it



## September 14, 2023

Feature

[**Preview**](https://cloud.google.com/products/#product-launch-stages): [Migrate to Virtual Machines from an Azure source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source) is now open to all users. Migrate to Virtual Machines from an Azure source lets you migrate Azure VM instances to Compute Engine.

## August 14, 2023

Feature

[**Preview**](https://cloud.google.com/products/#product-launch-stages): Migrate to Virtual Machines supports the [migration of VMs running Amazon Linux 2 to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrate-aws-linux2) as part of a preview program. In order to migrate a VM running Amazon Linux 2, Migrate to Virtual Machines first converts Amazon Linux 2 to Rocky Linux 8 and then completes the migration. To participate in the preview, contact us at **m2vm-amazon-linux-migration@google.com**.

## August 02, 2023

Feature

[**Preview**](https://cloud.google.com/products/#product-launch-stages): Migrate to Virtual Machines lets you [migrate disks from source virtual machine (VM) instances to Persistent Disk volumes](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrating-disks) on Google Cloud. This feature helps you migrate the workload state (VM disks) from a source VM and attach it as a Persistent Disk volume to a VM on Google Cloud, with minimal interruptions to the workload.

## June 29, 2023

Feature

**Generally Available** : Migrate to Virtual Machines lets you migrate your VM instances running on [Google Cloud VMware Engine to VM instances running on Compute Engine](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-a-gcve-source).

## June 13, 2023

Feature

Migrate to Virtual Machines lets you set up [throttling on the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrate-connector#setting_up_throttling_for_the_migrate_connector) to control the rate at which data is transferred from the Migrate Connector. Throttling ensures that the migration process distributes bandwidth evenly between the migration and any other tasks using the network. In this way, the migration can complete successfully without disrupting any other tasks.

## June 06, 2023

Feature

**Generally available** : The **Estimated cut-over time** field is now generally available. This field gives an estimate of the time it takes to complete a cut-over job for a VM once the cut-over is triggered. This field is populated only for an active VM that has completed a few replication cycles.

## April 29, 2023

Feature

Several updates to Migrate to Virtual Machines:

  * Migrate to Virtual Machines is now available in regions `europe-west12` and `me-central1`. For more information, see [Migrate to Virtual Machines locations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/locations).
  * Migrate to Virtual Machines now supports [VMWare 8.0](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-a-vmware-source#VMware-versions).
  * [**Preview**](https://cloud.google.com/products/#product-launch-stages): Migrate to Virtual Machines introduces a new field, [**Estimated cut-over time**](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrating-vms#step_5_create_a_cut-over), that gives an estimate of the time it takes to complete a cut-over job for a VM once the cut-over is triggered. This field is populated only for an active VM that has completed a few replication cycles.



## February 20, 2023

Feature

**Preview** : Migrate to Virtual Machines from an Azure source lets you [migrate Azure VM instances to Compute Engine](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source).

## January 16, 2023

Feature

**Generally available** : Migrate to Virtual Machines from an AWS source lets you migrate AWS EC2 instances to Compute Engine.

## August 24, 2022

Issue

**Issue:** Linux repositories that use Yum as their package management may have Yum configurations set explicitly to minor versions. For example, a Yum configuration may point to specific repositories holding 7.6 packages. This is not currently supported by Google. Only repositories holding the latest versions are supported. This may cause a failure to install the Google guest environment after the VM is detached. 

**Workaround:** Update your Yum configuration to refer to the available repositories. For RHEL 7.x, verify that the variable `$releasever` holds the value `7Server`, and not a specific release version number (7.6, for example) by running `echo 7Server > /etc/yum/vars/releasever`.

## August 02, 2022

Change

Several updates to Migrate to Virtual Machines:

  * Migrate to Virtual Machines [now available in regions](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/locations) `europe-west8`, `europe-west9`, and `europe-southwest1`.
  * [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/supported-os-versions) have been updated.
  * Migrate to Virtual Machines now [generates adaptation reports](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/concepts/migration-progress-details#adaptation_report) during your replication cycles, clones, and cut-over cycles.



## July 05, 2022

Change

Connector renaming

Includes the following updates:

  * Renamed CLI command from m4c to m2vm
  * Renamed product to Migrate to Virtual Machines
  * Bug fixes



## June 27, 2022

Feature

The maximum amount of active VMs has been increased from 100 to 200 VMs.

## March 17, 2022

Feature

Migrate for Compute Engine allows you to employ a VPC-SC service perimeter and communicate with select services using your migrate connector.

For more information about using a VPC-SC perimeter, see the [secure your migrations in a service perimeter](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-a-service-perimeter) documentation.

## October 26, 2021

Feature

Migrate VMs using UEFI firmware. Using UEFI firmware you can enable Secure Boot migration details.

## October 25, 2021

Fixed

**#199379063** Windows migrated VMs have GooGet installed with a wrong root directory

Windows VMs migrated before October 7th 2021 may have GooGet (Google package manager) installed with the wrong root directory (`C:\Windows\System32\%ProgramData%\GooGet instead of C:\ProgramData\GooGet`).

Workaround: Reinstall GooGet and guest environment by following the instructions to [Install a guest environment in-place](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#in_place). A copy of `googet.exe` can also be found under `C:\Google\Migrate\GooGet`, which allows you to skip the download command in step 1. `C:\Windows\System32\%ProgramData%\GooGet` can be safely deleted if needed.

Following the steps to install a guest environment in place will also update guest environment packages to their latest released versions.

## October 15, 2021

Feature

v.4.11.7 Security updates available. See [Migrate for Compute Engine Downloads](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/resources/downloads) for downloads and upgrade instructions.

## October 03, 2021

Feature

Migrate for Computer Engine now supports the configuration of multiple network interfaces to migrated VMs.

## September 20, 2021

Feature

Migrate for Compute Engine now supports the deployment of migrated workloads to sole-tenant nodes. A sole-tenant node is a Compute Engine server that is dedicated to hosting only your project's VMs.

See [Migrating individual VMs](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/migrating-vms) for more information on sole tenancy.

## September 05, 2021

Feature

Added support for overriding the default license type to explicitly specify a license type of PAYG or BYOL.

See [Configuring the target for a migrated VM](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/migrating-vms#configure-target) for more information.

## June 08, 2021

Feature

Transition the underlying OS used by Migrate for Compute Engine components (Manager, Cloud Extensions, Importers, and Exporters) to use [Ubuntu Advantage](https://ubuntu.com/security/esm).

## April 14, 2021

Feature

**vSphere Source**

Agentless migration of vSphere source environment utilizing Migrate Connector appliance deployed in source.

See [On-premises VMware to Compute Engine migrations](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-report) for more.

Feature

**VM utilization reports**

To help you determine the optimal settings for the Compute Engine target, Migrate for Compute Engine lets you create a _source VM utilization report_. This report displays information about resource allocation and utilization for the source VMs deployed on vCenter.

See [Creating a source VM utilization report](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-report) for more.

Feature

**Seamless OS adaptation**

Seamless OS adaptation of migrating VMs to prepare OS to run in Compute Engine (such as network settings) and deploy Compute Engine agents for seamless day 2 integrations with Compute Engine services.

See [Adapting VMs to run on Google Cloud](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/resources/vm-adaptations) for more.

Feature

**VM groups**

Group migration operations to enable you to manage and execute mass migration sprints.

See [Mass migration with groups](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/concepts/migrating-groups) for more.

Feature

**Google Cloud Console UI**

End-to-end migration experience in Google Cloud Console including: Dashboard, Source inventory, Migrations managements, VM groups, and Targets.

**To access the UI:**

  1. Open the Migrate for Compute Engine page in the [Google Cloud Console](https://console.cloud.google.com/).

  2. In the upper-right corner, select **Try the new version** to open the Google Cloud Console to the 5.0 UI.




Feature

**Compute Engine Targets**

Migration to _n_ Google Cloud target projects and flexible configuration of migrating VM target details (such as instance type, disk type, and network settings).

See [Configuring the target for a migrated VM](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/migrating-vms#configure-target) for more.

Feature

**Migration primitives**

Migration primitives controlling VM migration journey, which includes:

  * _Replication_ \- Initiate replication based migration, control periodical replication cycle schedule.

  * _Test-Clone_ \- Test a clone of migrating VM in Google Cloud with no disruptions on source VM to reduce migration risk.

  * _Cut-Over_ \- Cutting over to Google Cloud process with minimized downtime to migrating VM.




See [VM Migration lifecycle](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/concepts/lifecycle) for more.

## February 09, 2021

Feature

Added support for the `balanced` disk type to the `GcpDiskType` runbook field when migrating in batches with waves. See [Runbook reference](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/reference/runbooks) for more.

## January 12, 2021

Fixed

**#175196444:** Fixed Windows adaptation issue with network interface detection.

Fixed

**#171638373:** General stability improvements.

Fixed

**#171638373:** Fixed Windows adaptation issue when boot partition and Windows partition were on different volumes.

Fixed

Performance improvement during detach phase.

Fixed

**#174330790:** Linux adaptations now archive `ifcfg-*` scripts to avoid Network Manager conflicts with iSCSI boot.

Fixed

Security fixes applied.

## October 12, 2020

Fixed

Support added for migration of VMs from vSphere configured with CSM firmware type setting.

## September 14, 2020

Fixed

There is no longer a requirement that the subnet of the deployment cluster is under the same network as the Cloud Extension.

## August 12, 2020

Feature

Migrate Backend network connectivity requirement to Migrate Manager and Cloud Extensions have been reduced, all traffic on this channel is performed over port 443 (HTTPS and TLS) instead of using port 9111. See [Network access requirements](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/concepts/planning-a-migration/network-access-requirements) for more.

Feature

Usability enhancements in the following flows:

  * Automatic adjustments of VDDK max open sessions when accessing vSphere V6.5 to avoid overloading VDDK max connections limit.
  * Support for vCenter certificate update flow.
  * Enhancement of automatic license assignment feature to offline migration flow.



Issue

**#131532666** : Linux versions running with kernel version 2.6.32 may experience a kernel panic on ephemeral storage access failures; these are more likely while streaming over iSCSI.

**Workaround** : Upgrade your kernel. The issue will also reduce in likelihood after Detach.

Issue

**#131533056** : When migrating RHEL 7.4 from AWS to Google Cloud, Google Cloud agent will not be installed automatically.

**Workaround** : Manually remove the AWS agent and install Google Cloud agent

Feature

V4.11 offers integration with Secret Manager. You can store Migrate for Compute Engine password and encryption key as objects in secret manager to provide a higher level of security and control. See [Configuring the migration manager](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/how-to/configure-manager/configuring-migration-manager) for more.

Issue

**#133137658** : Scenario: No network connection between Migration Manager and VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try again.

Issue

**#131534862** : In rare cases, after running a Workload back on-premises - Workload VMDK's are locked. In certain cases, this is due to network disruptions between the Velostrata management appliance and the ESXi host on which the workload is running.

**Note** : The issue will resolve itself after 1-2 hours.

Issue

**#131647654** : Run on-premises operation succeeded but the status is marked as failed with error "Failed to consolidate snapshots"

**Workaround** : Consolidate snapshots via vCenter, and clear the error manually.

Issue

**#131560126** : Suse12: Due to a bug in SUSE kernel older than 4.2, configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround** : Upgrade to SUSE version with Kernel >=4.2 (SP2).

Issue

**#145644737** : Clones created on Azure or AWS from instances of Linux distributions that use cloud-init may experience issues in booting after installing the Linux prep package.

**Workaround** : Uninstall the package before cloning and reinstall when preparing to migrate.

Issue

**#131605387** : vCenter reboot causes Velostrata tasks in vCenter to disappear from UI. This is a vCenter limitation.

**Workaround** : Use the Velostrata PowerShell module to monitor Velostrata managed VMs or Cloud Extensions tasks that are currently running.

Issue

**#149004085** : Ubuntu 14 from on-premise may fail to start networking post detach.

**Workaround** : Connect through the serial console and manually add the network interface with DHCP.

Issue

**#137082702** : In rare cases, the Cancel detach operation succeeds but the VM instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

Issue

**#131638455** : A Run-in-Cloud operation fails with the error - "Failed to create virtual machine snapshot. The attempted operation cannot be performed in the current state (Powered off)".

**Workaround** : The VMware VM snapshot file may be pointing to a non-existent snapshot. Contact support for assistance in correcting the issue.

Issue

**#131532690** : Run-in-cloud and migration operations may fail for Windows Server 2016 workload when Symantec Endpoint Protection (SEP) is installed. This may also happen when SEP appears to be disabled.

**Workaround** : Modify workload Network interface bindings to remove the SEP option.

  1. Download [Microsoft Network VSP Bind (nvspbind)](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp.
  3. Open a command prompt as an Administrator and run the following:

`nvspbind.exe /d * symc_teefer2`




Issue

**#143262721** : Migration of VM from Azure fails when data disk is greater than 4 terabytes.

At this time, Migrate for Compute Engine does not support migration of Azure VMs with data disks bigger than 4TB.

**Workaround** : Make sure VM has data disk smaller than 4TB.

Issue

**#187887258:** Installing the Linux `prep-package` and then upgrading the kernel will result in failure to boot in cloud.

**Workaround** : If you're upgrading your kernel, install the `prep-package` package after the upgrade.

Issue

**#131614405** : When the Velostrata Prep RPM is installed on SUSE Linux Enterprise Server 11, the VM obtains a DHCP IP address in addition to an existing static IP configuration. This issue occurs when the VM is started on-premises in a subnet that is enabled with DHCP services.

**Note** : The issue does not occur when the subnet has no DHCP services. There is no connectivity impact for communications with the original static IP address.

Issue

**#131555885** : vCenter "Export OVA" operation is available when the VM in cloud is running in cache mode, however, this operation results in a corrupted OVA.

**Workaround** : Only create OVA after the detach.

Issue

**#145086776** : In rare cases, older versions of RHEL7 may stop responding during streaming or reach a Kernel panic. This issues were resolved in later versions of RHEL7.

**Workaround** : Run `sudo yum update` before migrating to update the system.

Issue

**#131532549** : For workloads with a Windows machine using a retail license, when returning from the cloud, the license is not present.

**Workaround** : Reinstall the license.

Issue

**#160405343** : Due to a change in behavior on the activation flow for SUSE, configuring repositories on SUSE Enterprise Linux instances post-detach now fail.

**Workaround** : The following workaround can be used prior to detach (either before migration or before detach).

  1. Follow the instructions described for Situation 4 at <https://www.suse.com/support/kb/doc/?id=000019633> to download the required packages for Compute Engine as a tar.gz file.

  2. **For SLES 12.x** , then run the following commands:
         
         tar -xf late_instance_offline_update_gce_SLE12.tar.gz
         cd x86_64/
         zypper --no-refresh --no-remote --non-interactive in *.rpm```
         



  1. **For SLES 15.x** , then run the following commands:
         
         tar -xf late_instance_offline_update_gce_SLE15.tar.gz
         cd x86_64/
         zypper --no-refresh --no-remote --non-interactive in *.rpm```
         




Issue

**#131558198** : PowerShell client for cloud to cloud Runbook reports errors when running on PowerShell 3.0

**Workaround** : Upgrade to PowerShell 4.0

Issue

**#131650367** : When performing a detach after a cancel detach operation, the action may fail.

**Workaround** : Retry the operation.

Issue

**#131537125** : Cloud Extension high availability does not work for workloads running Ubuntu OS with LVM configuration.

**Workaround** : Update the kernel to 3.13.0-161 or higher.

Issue

**#135664281** : When completing or canceling Azure to Google Cloud migration, if Velostrata Management failed to start the importer, Velostrata-created resources may be left in the original instance's resource group.

Issue

**#143313211** : Customer migrating RHEL 6.8 VM may experience boot issues in the cloud destination.

RHEL 6.x systems using kernel versions 2.6.32-xxx and using LVM may reach a kernel panic when booting in Compute Engine during migration.

**Workaround** : The kernel should be upgraded to 2.6.32-754 or higher before migrating.

Issue

**#131533480** : When using the Create Cloud Extension wizard, using an illegal HTTP proxy address will not generate a warning message.

**Workaround** : Delete the CE and then create the CE with a valid HTTP proxy address.

Issue

**#131637800** : After registering the Velostrata plug-in, running the Cloud Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround** : Un-register the Velostrata plug-in and restart the vSphere Web client service, then re-register the plug-in. Contact support if the issue persists.

Issue

**#131649978** : In the event of certain system failures, Velostrata components disconnect from vCenter. In this case, an event may not be sent, resulting in the alarm either not being set properly or not being cleared properly.

**Workaround** : Clear the alarm manually in vCenter.

Issue

**#131548730** : In some cases, when a VM is moved to Run-in-Cloud while a 3rd party VM-level backup solution holds a temporary snapshot, the Migrate for Compute Engine periodic write-back operations will not complete even after the backup solution deletes the temporary snapshot. The uncommitted writes counter on the VM will show an increasing size and no consistency checkpoint will be created on-premises.

**Workaround** : Select the Run On-Premises action for the VM and wait for the task to complete, which will commit all pending writes. Then select the Run-in-Cloud action again. Note that committing many pending writes may take a while. Do not use the Force option as this will result in the loss of the uncommitted writes.

Feature

V4.11 introduces Windows upgrade with bring-your-own-license (BYOL) feature. Migrating Windows Server 2008R2 with a customer owned license (BYOL) can upgrade to Windows Server 2012R2 using BYOL as part of the migration process. See [Upgrading Windows Server VMs](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/how-to/upgrading-vms/upgrading-windows-vms) for more.

Feature

V4.11 introduces automatic deployment of Google Cloud OS Config agent to migrating VMs. This allows you to get insights on your migrated VM patch status and automate deployment of software patches to migrated VMs. See [Adapting VMs to run on Google Cloud](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/concepts/planning-a-migration/vm-adaptations) for more.

Issue

**#131532882** : In certain cases, initiating Run in Cloud during a Windows update may cause the update to terminate abruptly and cause a failure to boot in the cloud.

**Workaround** : Allow the system to finish Windows update and/or suspend Windows updates before migrating.

Issue

**#131550214** : During Detach, the operation might fail with the following error message: "Operation was canceled".

**Workaround** : Retry the Detach operation.

Issue

**#131647857** : In rare cases, when a cloud component instance is created and system fails before it is tagged, the instance will remain untagged. This will not allow full clean-up or repair of the CE.

**Workaround** : Manually tag the instance, and then run "Repair".

Issue

**#131532846** : Certain firewalls and anti-viruses may cause Windows VMs to fail when moved to cloud by blocking iSCSI traffic.

**Workaround** : Disable the affecting service while migrating and reinstall after Detach.

Issue

**#131532713** : After Offline Migration of Windows 2003R2, if a NIC is manually deleted, it may be impossible to auto-detect and automatically reinstall it.

**Workaround** : The VM storage can be attached to a different VM, and the NIC Registry entry could be imported manually using a similar VM as a reference. Contact support for assistance.

Issue

**#131638716** : With an ESXi host in maintenance mode, if a VM is moved to cloud, the operation will fail and get stuck in the rollback phase.

**Workaround** : Manually cancel the Run-in-Cloud task, migrate the VM to another ESXi host in the cluster and retry the Run-in-Cloud operation.

Issue

**#135573857** : Scenario: When moving a VM back on-prem with "force" flag, failure to consolidate snapshot will cause the VM to remain as managed by Velostrata. RunInCloud on the same VM may fail since it is not allowed on managed VMs.

**Workaround** : Wait a couple of minutes and try again.

## December 20, 2019

Fixed

In some scenarios, migrating a VM from Azure may fail due to missing instance type at Azure region.

Fixed

This release fixes several issues related to preparing Linux VMs for Compute Engine in the migration process. These fixes increase stability and broaden source platform support.

Fixed

Create token API authentication mechanism.

## November 12, 2019

Issue

**#131560126:** Suse12: Due to a bug in SUSE kernel older than 4.2, configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround:** Upgrade to SUSE version with Kernel >=4.2 (SP2).

Issue

**#131637800:** After registering the Velostrata plug-in, running the Cloud Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround:** Un-register the Velostrata plug-in and restart the vSphere Web client service, then re-register the plug-in. Contact support if the issue persists.

Issue

**#131548730:** In some cases, when a VM is moved to Run-in-Cloud while a 3rd party VM-level backup solution holds a temporary snapshot, the Migrate for Compute Engine periodic write-back operations will not complete even after the backup solution deletes the temporary snapshot. The uncommitted writes counter on the VM will show an increasing size and no consistency checkpoint will be created on-premises.

**Workaround:** Select the Run On-Premises action for the VM and wait for the task to complete, which will commit all pending writes. Then select the Run-in-Cloud action again. Note that committing many pending writes may take a while. Do not use the Force option as this will result in the loss of the uncommitted writes.

Issue

**#131650367:** When performing a detach after a cancel detach operation, the action may fail.

**Workaround:** Retry the operation.

Issue

**#131555885:** vCenter "Export OVA" operation is available when the VM in cloud is running in cache mode, however, this operation results in a corrupted OVA.

**Workaround:** Only create OVA after the detach.

Issue

**#131532690:** Run-in-cloud and migration operations may fail for Windows Server 2016 workload when Symantec Endpoint Protection (SEP) is installed. This may also happen when SEP appears to be disabled.

**Workaround:** Modify workload Network interface bindings to remove the SEP option.

  1. Download [Microsoft Network VSP Bind (nvspbind)](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp.
  3. Open a command prompt as an Administrator and run the following:

`nvspbind.exe /d * symc_teefer2`




Issue

**#131647857:** In rare cases, when a cloud component instance is created and system fails before it is tagged, the instance will remain untagged. This will not allow full clean-up or repair of the CE.

**Workaround:** Manually tag the instance, and then run "Repair".

Issue

**#143313211:** Customer migrating RHEL 6.8 VM may experience boot issues in the cloud destination.

RHEL 6.x systems using kernel versions 2.6.32-xxx and using LVM may reach a kernel panic when booting in Compute Engine during migration.

**Workaround:** The kernel should be upgraded to 2.6.32-754 or higher before migrating.

Change

For a list of builds for this release and others, see the [Build History](https://docs.cloud.google.com/migrate/compute-engine/docs/build-history).

#### Requirements and OS Support

See [Requirements](https://docs.cloud.google.com/migrate/compute-engine/docs/4.8/concepts/requirements) and [Supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/4.8/reference/supported-os-versions).

Issue

**#131532549:** For workloads with a Windows machine using a retail license, when returning from the cloud, the license is not present.

**Workaround:** Reinstall the license.

Issue

**#131532846:** Certain firewalls and anti-viruses may cause Windows VMs to fail when moved to cloud by blocking iSCSI traffic.

**Workaround:** Disable the affecting service while migrating and reinstall after Detach.

Issue

**#131532666:** Linux versions running with kernel version 2.6.32 may experience a kernel panic on ephemeral storage access failures; these are more likely while streaming over iSCSI.

**Workaround:** Upgrade your kernel. The issue will also reduce in likelihood after Detach.

Issue

**#131605387:** vCenter reboot causes Velostrata tasks in vCenter to disappear from UI. This is a vCenter limitation.

**Workaround:** Use the Velostrata PowerShell module to monitor Velostrata managed VMs or Cloud Extensions tasks that are currently running.

Issue

**#133137658:** Scenario: No network connection between Migration Manager and VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try again.

Issue

**#131533480:** When using the Create Cloud Extension wizard, using an illegal HTTP proxy address will not generate a warning message.

**Workaround:** Delete the CE and then create the CE with a valid HTTP proxy address.

Issue

**#131614405:** When the Velostrata Prep RPM is installed on SUSE Linux Enterprise Server 11, the VM obtains a DHCP IP address in addition to an existing static IP configuration. This issue occurs when the VM is started on-premises in a subnet that is enabled with DHCP services.

**Note:** The issue does not occur when the subnet has no DHCP services. There is no connectivity impact for communications with the original static IP address.

Issue

**#131638716:** With an ESXi host in maintenance mode, if a VM is moved to cloud, the operation will fail and get stuck in the rollback phase.

**Workaround:** Manually cancel the Run-in-Cloud task, migrate the VM to another ESXi host in the cluster and retry the Run-in-Cloud operation.

Issue

**#131558198:** PowerShell client for cloud to cloud Runbook reports errors when running on PowerShell 3.0

**Workaround:** Upgrade to PowerShell 4.0

Issue

**#143262721:** Migration of VM from Azure fails when data disk is greater than 4 terabytes.

At this time, Migrate for Compute Engine does not support migration of Azure VMs with data disks bigger than 4TB.

**Workaround:** Make sure VM has data disk smaller than 4TB.

Issue

**#135573857** Scenario: When moving a VM back on-prem with "force" flag, failure to consolidate snapshot will cause the VM to remain as managed by Velostrata. RunInCloud on the same VM may fail since it is not allowed on managed VMs.

* **_Workaround:_** * Wait a couple of minutes and try again.

Issue

**#135664281:** When completing or canceling Azure to Google Cloud migration, if Velostrata Management failed to start the importer, Velostrata-created resources may be left in the original instance's resource group.

Issue

**#131534862:** In rare cases, after running a Workload back on-premises - Workload VMDK's are locked. In certain cases, this is due to network disruptions between the Velostrata management appliance and the ESXi host on which the workload is running.

**Note:** The issue will resolve itself after 1-2 hours.

Issue

**#131550214:** During Detach, the operation might fail with the following error message: "Operation was canceled".

**Workaround:** Retry the Detach operation.

Issue

**#131638455:** A Run-in-Cloud operation fails with the error - "Failed to create virtual machine snapshot. The attempted operation cannot be performed in the current state (Powered off)".

**Workaround:** The VMware VM snapshot file may be pointing to a non-existent snapshot. Contact support for assistance in correcting the issue.

Issue

**#131649978:** In the event of certain system failures, Velostrata components disconnect from vCenter. In this case, an event may not be sent, resulting in the alarm either not being set properly or not being cleared properly.

**Workaround:** Clear the alarm manually in vCenter.

Feature

#### Azure to Google Cloud migration (GA)

Version 4.8 promotes Azure to GCP migration to GA level. You can migrate VMs to Compute Engine using [Waves migration](https://docs.cloud.google.com/migrate/compute-engine/docs/4.8/how-to/organizing-migrations/overview). The system now supports migration at scale of instances from Azure to Compute Engine.

Issue

**#131532713:** After Offline Migration of Windows 2003R2, if a NIC is manually deleted, it may be impossible to auto-detect and automatically reinstall it.

**Workaround:** The VM storage can be attached to a different VM, and the NIC Registry entry could be imported manually using a similar VM as a reference. Contact support for assistance.

Issue

**#131537125:** Cloud Extension high availability does not work for workloads running Ubuntu OS with LVM configuration.

**Workaround:** Update the kernel to 3.13.0-161 or higher.

Issue

**#131647654:** Run on-premises operation succeeded but the status is marked as failed with error "Failed to consolidate snapshots"

**Workaround:** Consolidate snapshots via vCenter, and clear the error manually.

Issue

**#131533056:** When migrating RHEL 7.4 from AWS to Google Cloud, Google Cloud agent will not be installed automatically.

**Workaround:** Manually remove the AWS agent and install Google Cloud agent

Feature

#### System upgrade/patch management

Version 4.8 introduces upgrades and patch management. You can [manage system upgrades and patch installation](https://docs.cloud.google.com/migrate/compute-engine/docs/4.8/support/applying-patches-and-upgrades) via the system UI.

Issue

**#137082702:** In rare cases, the Cancel detach operation succeeds but the VM instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

Issue

**#131532882:** In certain cases, initiating Run in Cloud during a Windows update may cause the update to terminate abruptly and cause a failure to boot in the cloud.

**Workaround:** Allow the system to finish Windows update and/or suspend Windows updates before migrating.

Feature

#### Reduced network connectivity requirement

Version 4.8 requires reduced network connectivity between all components. Network connectivity requirement for Cloud Extension and Workers is reduced to single direction to Migrate for Compute Engine Manager. This simplifies system deployment.

## September 06, 2019

Issue

**#131533056:** When migrating RHEL 7.4 from AWS to Google Cloud, Google Cloud agent will not be installed automatically.

**Workaround:** Manually remove the AWS agent and install Google Cloud agent

Issue

**#131649978:** In the event of certain system failures, Velostrata components disconnect from vCenter. In this case, an event may not be sent, resulting in the alarm either not being set properly or not being cleared properly.

**Workaround:** Clear the alarm manually in vCenter.

Issue

**#131533480:** When using the Create Cloud Extension wizard, using an illegal HTTP proxy address will not generate a warning message.

**Workaround:** Delete the CE and then create the CE with a valid HTTP proxy address.

Issue

**#131550214:** During Detach, the operation might fail with the following error message: "Operation was canceled".

**Workaround:** Retry the Detach operation.

Issue

**#131548730:** In some cases, when a VM is moved to Run-in-Cloud while a 3rd party VM-level backup solution holds a temporary snapshot, the Migrate for Compute Engine periodic write-back operations will not complete even after the backup solution deletes the temporary snapshot. The uncommitted writes counter on the VM will show an increasing size and no consistency checkpoint will be created on-premises.

**Workaround:** Select the Run On-Premises action for the VM and wait for the task to complete, which will commit all pending writes. Then select the Run-in-Cloud action again. Note that committing many pending writes may take a while. Do not use the Force option as this will result in the loss of the uncommitted writes.

Issue

**#131558198:** PowerShell client for cloud to cloud Runbook reports errors when running on PowerShell 3.0

**Workaround:** Upgrade to PowerShell 4.0

Issue

**#131637800:** After registering the Velostrata plug-in, running the Cloud Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround:** Un-register the Velostrata plug-in and restart the vSphere Web client service, then re-register the plug-in. Contact support if the issue persists.

Issue

**#131532666:** Linux versions running with kernel version 2.6.32 may experience a kernel panic on ephemeral storage access failures; these are more likely while streaming over iSCSI.

**Workaround** : Upgrade your kernel. The issue will also reduce in likelihood after Detach.

Change

For a list of builds for this release and others, see the [Build History](https://docs.cloud.google.com/migrate/compute-engine/docs/build-history)

Issue

**#135573857** Scenario: When moving a VM back on-prem with "force" flag, failure to consolidate snapshot will cause the VM to remain as managed by Velostrata. RunInCloud on the same VM may fail since it is not allowed on managed VMs.

* **_Workaround:_** * Wait a couple of minutes and try again.

Issue

**#131532882:** In certain cases, initiating Run in Cloud during a Windows update may cause the update to terminate abruptly and cause a failure to boot in the cloud.

**Workaround:** Allow the system to finish Windows update and/or suspend Windows updates before migrating.

Issue

**#131532846:** Certain firewalls and anti-viruses may cause Windows VMs to fail when moved to cloud by blocking iSCSI traffic.

**Workaround:** Disable the affecting service while migrating and reinstall after Detach.

Feature

#### Azure to Google Cloud migration (Beta)

Version 4.5 introduces beta support for Azure to Google Cloud migration. You can migrate VMs to Azure using Waves migration. Please note that in this version, a storage account is used per each VM migrated from Azure to Google Cloud, which, pending on the storage account usage in your subscription, may limit the amount of concurrent migration you can do.

Issue

**#131614405:** When the Velostrata Prep RPM is installed on SUSE Linux Enterprise Server 11, the VM obtains a DHCP IP address in addition to an existing static IP configuration. This issue occurs when the VM is started on-premises in a subnet that is enabled with DHCP services.

**Note:** The issue does not occur when the subnet has no DHCP services. There is no connectivity impact for communications with the original static IP address.

Issue

**#131605387:** vCenter reboot causes Velostrata tasks in vCenter to disappear from UI. This is a vCenter limitation.

**Workaround:** Use the Velostrata PowerShell module to monitor Velostrata managed VMs or Cloud Extensions tasks that are currently running.

Issue

**#131555885:** vCenter "Export OVA" operation is available when the VM in cloud is running in cache mode, however, this operation results in a corrupted OVA.

**Workaround:** Only create OVA after the detach.

Issue

**#131647654:** Run on-premises operation succeeded but the status is marked as failed with error "Failed to consolidate snapshots"

**Workaround:** Consolidate snapshots via vCenter, and clear the error manually.

Issue

**#131537125:** Cloud Extension high availability does not work for workloads running Ubuntu OS with LVM configuration.

**Workaround:** Update the kernel to 3.13.0-161 or higher.

Feature

#### Migration of UEFI VMs to Google Cloud and Shielded VMs

Version 4.5 introduces support for migration of UEFI-based VMs from on-prem to Google Cloud. The system will automatically migrate UEFI-based VMs to Google Cloud UEFI-enabled hosts. In addition, you can enable activation of the Shielded VMs secure boot feature in the runbook specs for waves.

Feature

#### Windows 2019

Version 4.5 introduces support for migrating Windows 2019 OS to Google Cloud.

Note that when migrating Windows 2019 from Azure or AWS to Google Cloud, you will need to explicitly add the license tag of Windows 2019 in the Runbook file.

#### Requirements and OS Support

See [Requirements](https://docs.cloud.google.com/migrate/compute-engine/docs/4.5/concepts/requirements) and [Supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/4.5/reference/supported-os-versions).

Issue

**#131532690:** Run-in-cloud and migration operations may fail for Windows Server 2016 workload when Symantec Endpoint Protection (SEP) is installed. This may also happen when SEP appears to be disabled.

**Workaround:** Modify workload Network interface bindings to remove the SEP option.

  1. Download [Microsoft Network VSP Bind (nvspbind)](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp.
  3. Open a command prompt as an Administrator and run the following:

`nvspbind.exe /d * symc_teefer2`




Issue

**#131560126:** Suse12: Due to a bug in SUSE kernel older than 4.2, configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround:** Upgrade to SUSE version with Kernel >=4.2 (SP2).

Issue

**#131638716:** With an ESXi host in maintenance mode, if a VM is moved to cloud, the operation will fail and get stuck in the rollback phase.

**Workaround:** Manually cancel the Run-in-Cloud task, migrate the VM to another ESXi host in the cluster and retry the Run-in-Cloud operation.

Issue

**#131638455:** A Run-in-Cloud operation fails with the error - "Failed to create virtual machine snapshot. The attempted operation cannot be performed in the current state (Powered off)".

**Workaround:** The VMware VM snapshot file may be pointing to a non-existent snapshot. Contact support for assistance in correcting the issue.

Issue

**#131532549:** For workloads with a Windows machine using a retail license, when returning from the cloud, the license is not present.

**Workaround:** Reinstall the license.

Issue

**#131532713:** After Offline Migration of Windows 2003R2, if a NIC is manually deleted, it may be impossible to auto-detect and automatically reinstall it.

**Workaround** : The VM storage can be attached to a different VM, and the NIC Registry entry could be imported manually using a similar VM as a reference. Contact support for assistance.

Issue

**#137082702:** In rare cases, the Cancel detach operation succeeds but the VM instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

Issue

**#131534862:** In rare cases, after running a Workload back on-premises - Workload VMDK's are locked. In certain cases, this is due to network disruptions between the Velostrata management appliance and the ESXi host on which the workload is running.

**Note:** The issue will resolve itself after 1-2 hours.

Issue

**#135664281:** When completing or canceling Azure to Google Cloud migration, if Velostrata Management failed to start the importer, Velostrata-created resources may be left in the original instance's resource group.

Issue

**#131647857:** In rare cases, when a cloud component instance is created and system fails before it is tagged, the instance will remain untagged. This will not allow full clean-up or repair of the CE.

**Workaround:** Manually tag the instance, and then run "Repair".

Issue

**#133137658:** Scenario: No network connection between Migration Manager and VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try again.

Issue

**#131650367:** When performing a detach after a cancel detach operation, the action may fail.

**Workaround:** Retry the operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
