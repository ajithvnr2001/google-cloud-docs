---
url: https://docs.cloud.google.com/bare-metal/docs/bms-planning/
title: Plan for Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:13.546752+00:00
---

# Plan for Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-planning/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Plan for Bare Metal Solution

This document explains the key components of Bare Metal Solution to help you decide how to deploy servers, networking, and storage in your own Bare Metal Solution environment.

To run SAP HANA, see [Bare metal machines for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana).

## Regional availability

Bare Metal Solution is available in the following Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions):

Region | Location  
---|---  
`asia-northeast1` | Tokyo, Japan, APAC  
`asia-northeast3` | Seoul, South Korea, APAC  
`asia-southeast1` | Jurong West, Singapore, APAC  
`europe-west2` | London, England, Europe  
`europe-west3` | Frankfurt, Germany, Europe  
`europe-west4` | Eemshaven, Netherlands, Europe  
`northamerica-northeast1` | Montréal, Québec, Canada, North America  
`northamerica-northeast2` | Toronto, Ontario, Canada, North America  
`southamerica-east1` | Osasco, São Paulo, Brazil, South America  
`us-central1` | Council Bluffs, Iowa, USA, North America  
`us-east4` | Ashburn, Virginia, USA, North America  
`us-west2` | Los Angeles, California, USA, North America  
  
If you don't see the region that you need in the preceding table, then contact [Google Cloud Sales](https://cloud.google.com/contact/?form=SAP).

## Server configurations

Bare Metal Solution offers servers in pre-configured sizes, as shown in the following table.

Each Bare Metal Solution server comes with 200 GB of network attached storage for the boot disk.

By default, CPU hyper-threading is disabled in Bare Metal Solution servers. If you need hyper-threading, let your sales representative know or, if you already have Bare Metal Solution, open a service request.

Server name | CPU cores | vCPUs | Sockets | Memory | CPU platform | Ethernet ports  
---|---|---|---|---|---|---  
**General-purpose servers**  
`o2-standard-16-metal` | 8 | 16 | 2 | 192 GB | Intel Xeon Gold, 5200 series, 3.8 GHz | 4 port 25GbE NIC  
`o2-standard-32-metal` | 16 | 32 | 2 | 384 GB | Intel Xeon Gold, 6200 series, 3.2 GHz | 4 port 25GbE NIC  
`o2-standard-48-metal` | 24 | 48 | 2 | 768 GB | Intel Xeon Gold, 6200 series, 3.0 GHz | 4 port 25GbE NIC  
`o2-standard-112-metal` | 56 | 112 | 2 | 1.5 TB | Intel Xeon Platinum, 8200 series, 2.2 GHz | 4 port 25GbE NIC  
**High-memory general-purpose servers**  
`o2-highmem-224-metal` | 112 | 224 | 4 | 3 TB | Intel Xeon Platinum, 8200 series, 2.7 GHz | 4 port 25GbE NIC  
**Memory-optimized servers**  
`o2-ultramem-672-metal` | 336 | 672 | 12 | 18 TB | Intel Xeon Platinum, 8200 series, 2.7 GHz | 6 port 25GbE NIC  
`o2-ultramem-896-metal` | 448 | 896 | 16 | 24 TB | Intel Xeon Platinum, 8200 series, 2.7 GHz | 8 port 25GbE NIC  
  
## Firmware

We recommend that you install the latest version of Bare Metal Solution firmware on your servers: [`TS54`](https://docs.cloud.google.com/bare-metal/docs/bms-planning#features).

Using an outdated firmware version can cause issues including the following:

  * Delayed and limited Google Cloud support.
  * Loss of critical Google Cloud features.
  * Security, compliance, and performance issues.



To learn how to upgrade firmware, see [Upgrade firmware](https://docs.cloud.google.com/bare-metal/docs/bms-planning#upgrade_firmware).

### Identify your firmware version

To identify the current firmware version of your Bare Metal Solution server, run the following command:
    
    
    sudo dmidecode -s bios-version
    

#### Available firmware versions

The following table provides details for the firmware versions available for Bare Metal Solution.

### General information

Firmware version | Machine series | Machine type | Lifecycle stage | EOL and firmware deprecation date  
---|---|---|---|---  
BIOS_PUR043.45.00.002 (TS54) | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | To be determined  
BIOS_PUR043.37.14.021 (TS24.02) | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | April 2024  
BIOS_PUR043.37.16.023 (TS24.05) | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | April 2024  
3.50.58 | 

  * `o2-ultramem-672-metal`
  * `o2-ultramem-896-metal`

| Memory-optimized servers | GA | March 2024  
3.80.24 | 

  * `o2-ultramem-672-metal`
  * `o2-ultramem-896-metal`

| Memory-optimized servers | GA | To be determined  
  
### Features

Firmware version | Features  
---|---  
BIOS_PUR043.45.00.002 (TS54) | 

  1. Support for interactive serial console.
  2. Reliability, availability, and serviceability (RAS) features: 
     * Adaptive Double Device Data Correction (ADDDC)
     * Post Package Repair (PPR) to reduce DIMM errors, repair DIMM issues, reduce maintenance downtime
  3. Better reliability when a server shuts down or starts up.
  4. Bug fixes for the following: 
     * Unified Extensible Firmware Interface (UEFI) security issue
     * Reboot issues linked to loading the initial RAM disk
     * Baseboard Management Controller (BMC) issues related to the IPMI internal client
     * False alarms for fan status and CPU voltage

  
  
### Upgrade firmware

To upgrade your server to the latest firmware version, contact [Customer Care](https://cloud.google.com/support-hub).

We need a 5-day notice to schedule the upgrade. The upgrade requires approximately 10 hours to complete. We can upgrade three servers concurrently in a 10 hour window.

**Note:** If you are running OVM on your Bare Metal Solution server, the firmware upgrade requires some OVM configuration changes. For more information, contact [Customer Care](https://cloud.google.com/support-hub). Also, see known issue [OVM server can't connect to OVM Manager after TS54 firmware upgrade](https://docs.cloud.google.com/bare-metal/docs/known-issues#ovm-issues-after-ts54-upgrade). 

## Interactive serial console

Bare Metal Solution provides an interactive serial console to access your servers. You can use it to perform configuration and troubleshooting tasks. You can directly run commands and respond to prompts in the serial console.

To learn how to configure and use the serial console, see [Configure the serial console](https://docs.cloud.google.com/bare-metal/docs/configure-serial-console).

## Operating systems

When you place an order for Bare Metal Solution, you can specify the operating system (OS) that you need installed on your servers. If you need an OS that does not appear in the following tables, contact [Google Cloud Sales](https://cloud.google.com/contact).

**Note:**

  * The [available OS images](https://docs.cloud.google.com/bare-metal/docs/bms-planning#available_os_images) receive monthly patch updates that include the latest versions of RPM packages and the kernel. 

Additionally, the OS minor version is incremented when the OS vendor (such as, Red Hat or Oracle) releases a new minor version in the upstream repository. For example, when Red Hat releases `RHEL 8.10`, the existing `RHEL 8.9` OS image is updated to `RHEL 8.10` as part of the patch process. Consequently, the OS image you previously used may differ from the one available when reimaging or provisioning a new Bare Metal Solution server.

For enterprises that certify OS images across multiple phases, such as development, staging, and production, typically over several months, we recommend to use an OS image explicitly marked with `Minor version locked`. This ensures consistency throughout all phases as the OS images marked with `Minor version locked` are excluded from receiving the OS patches updates.

  * You must obtain all necessary OS licenses from the OS vendor. Bare Metal Solution uses a bring-your-own-license (BYOL) licensing model.
  * After your Bare Metal Solution environment is delivered to you, you are responsible for the configuration and management of your OS, including applying updates and security patches and obtaining support.



### Available OS images

You can request the installation of the following OS images on your Bare Metal Solution servers. This section provides general details for the OS images.

OS version | OS image code | Machine series | Machine type | Lifecycle stage | EOL and image deprecation date  
---|---|---|---|---|---  
RHEL 7.7 for SAP | `LAMBRHEL77SAP` | 

  * `o2-ultramem-672-metal`
  * `o2-ultramem-896-metal`

| Memory-optimized servers | End of Life | August 2023  
RHEL 7.9 | `RHEL7x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | June 2024  
RHEL 8.4 (Minor version locked) | `RHEL84` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | May 2023  
RHEL 8 (Latest minor release) | `RHEL8x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | May 2029  
RHEL 8.0 for SAP | `RHEL80SAP` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | December 2020  
RHEL 8.1 for SAP | `RHEL81SAP` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | November 2023  
RHEL 9.4 (Minor version locked) | `RHEL94` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | May 2023  
RHEL 9 (Latest minor release) | `RHEL9x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | May 2032  
OEL 7.9 | `OEL7x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | July 2024  
OEL 8 (Latest minor release) | `OEL8x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | July 2029  
OEL 8.8 (Minor version locked) | `OEL88` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | July 2029  
OEL 9 | `OEL9x` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | GA | June 2032  
SLES 15 SP1 | `SLES15SPx` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | January 2024  
SLES 12 SP4 for SAP | `SLES12SP4SAP` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`
  * `o2-ultramem-896-metal`

| General-purpose & Memory-optimized servers | End of Life | June 2023  
SLES 12 SP5 for SAP | `SLES12SP5SAP` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`
  * `o2-ultramem-896-metal`

| General-purpose & Memory-optimized servers | End of Support | October 2027  
SLES 15 for SAP | `SLES15SAP` | 

  * `o2-standard-48-metal`
  * `o2-standard-32-metal`
  * `o2-standard-112-metal`
  * `o2-standard-16-metal`
  * `o2-highmem-224-metal`

| General-purpose | End of Life | December 2022  
SLES 15 SP1 for SAP | `SLES15SPxSAP` | 

  * `o2-standard-16-metal`
  * `o2-standard-32-metal`
  * `o2-standard-48-metal`
  * `o2-standard-112-metal`
  * `o2-highmem-224-metal`
  * `o2-ultramem-896-metal`

| General-purpose & Memory-optimized servers | End of Support | January 2024  
SLES 15 SP2 for SAP | `LAMBSLES15SP2SAP` | 

  * `o2-ultramem-672-metal`
  * `o2-ultramem-896-metal`

| Memory-optimized servers | GA | December 2024  
  
### Bring Your Own Image (BYOI)

The Bare Metal Solution servers are certified to run only the OS images of the following distributions:

  * Red Hat Enterprise Linux (RHEL)
  * Oracle Linux (OL)
  * SUSE Linux Enterprise Server (SLES)



Any other OS hasn't been tested or certified to run on the Bare Metal Solution servers.

If the OS image you want use is not listed in the [available OS images list](https://docs.cloud.google.com/bare-metal/docs/bms-planning#available_os_images), you can use your own image. However, you must keep the following things in mind:

  * [Our technical support](https://docs.cloud.google.com/bare-metal/docs/bms-support#bms-support-scope) primarily focuses on infrastructure-related issues. We don't provide support for issues related to OS, drivers, and compatibility. For the best assistance with these issues, we recommend contacting your OS vendor directly. They have the most in-depth knowledge to help you troubleshoot.

  * Your OS image must comply with all the [OS image technical specifications](https://docs.cloud.google.com/bare-metal/docs/bms-planning#os_image_technical_specifications).




#### Installing BYOI OS image

To install your BYOI OS image on Bare Metal Solution, do the following:

  1. Ensure that your OS image meets all the [OS image technical specifications](https://docs.cloud.google.com/bare-metal/docs/bms-planning#os_image_technical_specifications).
  2. Remove any personally identifiable information (PII) from the OS image.
  3. [Open a Google Cloud support case](https://docs.cloud.google.com/bare-metal/docs/bms-support) requesting the use of your OS image. In the support case, provide a secure download link to your OS image.



Once we receive your request, we evaluate your OS image and provide technical guidance regarding its installation on the Bare Metal Solution. It is your responsibility to adhere to the guidance and install the OS image on your server.

#### OS image technical specifications

The OS image you want to use must comply with the following guidelines:

  * The OS image must support UEFI boot type.
  * The OS image must contain EFI partition and GPT partition type.
  * The OS image must have a size equal to or smaller than 200 GiB.
  * The disk format for the OS image must be `raw`.
  * The OS image must have the multipath package installed and the multipath daemon enabled during boot.
  * The `initramfs` must contain the multipath module.
  * The Linux LVM must be configured to scan only the multipath device nodes, and specifically not scan the raw device nodes which represent individual paths to the SAN (`/dev/sd*`). It is the LVM filter, found in `/etc/lvm/lvm.conf`, that determines the devices to be scanned.
  * The `fstab` entries must use UUIDs or file system labels to mount the file system and not device files as they may contain the SAN Disk WWID or the device names change when deployed in a multipath environment.
  * The GRUB must be configured to send the console output to the serial port ttyS0 at a baud rate of `115200` as well as sending the output to the regular console or "screen" tty0.



## Hypervisors

When you place an order for Bare Metal Solution, you can request that a hypervisor be installed on your servers. If you request a hypervisor, you must install any guest operating system yourself.

**Note:**

  * You must obtain all necessary licenses from the vendor of the hypervisor. Bare Metal Solution uses a bring-your-own-license (BYOL) licensing model.
  * After Google Cloud delivers your Bare Metal Solution environment to you, you are responsible for maintaining your hypervisor and any guests, including applying updates and security patches.



You can request the following hypervisor:

  * Oracle VM
    * 3.4.6



To use Oracle Linux Virtualization Manager (OLVM - a KVM-based hypervisor), request a compatible Linux OS such as Oracle Linux 7.

## Storage

For storage in a Bare Metal Solution environment, you need to select the type of storage you need, know how to maximize the performance, and decide if you want to enable snapshots.

### Storage choices

Storage devices in the regional extension provide local storage to Bare Metal Solution servers. There are three types of local storage you can request:

  * Fibre Channel-based block storage presented as logical unit numbers (LUNs) and accessible by only one Bare Metal Solution server.
  * Fibre Channel-based block storage presented as multipath LUNs and shared with multiple Bare Metal Solution servers. This option is good for high-availability applications, such as Oracle Database RAC.
  * Network File System (NFS) storage. With NFS, you mount a shared storage directory on one or more Bare Metal Solution servers and access the directory like any other file system. For information on how to implement NFS, see [Add NFS file storage to a Bare Metal Solution environment](https://docs.cloud.google.com/bare-metal/docs/bms-nfs).



For Fibre Channel-based block storage, you can choose the following storage options in 1 TiB increments up to a maximum of 16 TiB for regular SSD and HDD and to a maximum of 8 TiB for Performance SSD. For NFS, you can choose the following storage options with a minimum of 100 GiB and a maximum of 16 TiB.

Storage type | Snapshot support | Common Workloads  
---|---|---  
SSD (solid-state drive) | Yes | Mission-critical production workloads  
HDD (hard drive) | Yes | Local backups or archival workloads  
  
Here are some additional storage volume considerations that you need to understand:

  * We don't recommended using hard disk drives (HDDs) to run mission-critical Oracle production workloads, because performance guidance is not available for HDD storage.
  * When you provision any Fibre Channel or NFS storage volume, the volume size becomes fixed and you can't expand the volume. Also, the type and the performance tier of the of the storage volume remains fixed and can't be changed without ordering new storage and performing host-based data migration.
  * If you need additional storage space, you need to purchase additional storage volumes.
  * You cannot expand the existing LUNs in a storage volume. Instead, you need to order new LUNs and a new storage volume, migrate the old LUNs to the new storage volume, and decommission the old LUNs.
  * When you migrate the LUNs to a new storage volume, you also need to migrate the data.
  * If you run Oracle Automatic Storage Management (ASM), the following options are available:

    * When you need to expand an ASM disk group, you can order another storage volume, rescan the SCSI hosts to discover the new LUNs, and use ASM to add the new storage capacity into the disk group.

You can use the following command to perform an SCSI rescan on Red Hat Linux or Oracle Linux:
          
          sudo rescan-scsi-bus.sh -a
          

    * When you add, drop, or resize disks, ASM automatically initiates a rebalance to prevent an unnecessary load on the production database.

  * When you remove a storage volume from service in a Bare Metal Solution environment, the Bare Metal Solution server reboots. The length of the outage can last from 20 minutes to an hour, depending on the size of your Bare Metal Solution server and the amount of storage attached to the server.

  * You can attach a maximum of 200 LUNs (including the boot LUN) to a Bare Metal Solution server.




### Storage performance

#### Standard SSD Storage

For Fibre Channel and NFS storage, Bare Metal Solution provides throughput and input/output operations per second (IOPS) performance calculated according to the following formula for an 8 KiB block size on an SSD drive:
    
    
    Calculated IOPS = 7200 * Volume Size in TiB
    Maximum Throughput (MiBps) = Calculated IOPS * 8 / 1024
    

The following table shows the IOPS and the throughput for common volume sizes:

**Volume size** | **Read/Write IOPS** | **Throughput (MiBps)** | **Read/Write latency**  
---|---|---|---  
**200 GiB (0.2 TiB)** | 1400 | 10.9 | < 1 ms  
**1 TiB** | 7200 | 56 | < 1 ms  
**4 TiB** | 28800 | 225 | < 1 ms  
**8 TiB** | 57600 | 450 | < 1 ms  
**12 TiB** | 86400 | 675 | < 1 ms  
**16 TiB** | 115200 | 900 | < 1 ms  
  
#### Performance SSD Storage

For Fibre Channel storage, Bare Metal Solution provides throughput and input/output operations per second (IOPS) performance calculated according to the following formula for a 32 KiB block size on a Performance SSD drive:
    
    
    Calculated IOPS = 8192 * Volume Size in TiB
    Maximum Throughput (MiBps) = Calculated IOPS * 32 / 1024
    

The maximum volume size for a Performance SSD volume is 8 TiB.

The following table shows the IOPS and the throughput for common volume sizes:

**Volume size** | **Read/Write IOPS** | **Throughput (MiBps)** | **Read/Write latency**  
---|---|---|---  
**1 TiB** | 8192 | 256 | < 1 ms  
**2 TiB** | 16384 | 512 | < 1 ms  
**4 TiB** | 32768 | 1024 | < 1 ms  
**8 TiB** | 65536 | 2048 | < 1 ms  
**Note:** We don't provide performance guidance for hard drives (HDD). 

Use the following storage recommendations to improve the performance of your databases and applications in your Bare Metal Solution environment:

  * When you deploy multiple storage volumes, use consistent volume sizes to get consistent performance for databases and applications.
  * When you add a new storage volume, always remember to rescan the LUNs to detect the new storage capacity.



### Storage volume snapshots

The Bare Metal Solution provides options to save snapshots of your storage volumes to use for recovery purposes. Snapshots are available as follows:

  * **OS boot volume:** Google Cloud takes a daily snapshot by default.
  * **Data volume:** You can request daily snapshots when you place your initial order for Bare Metal Solution. You can also contact [Customer Care](https://cloud.google.com/support-hub) to request data volume snapshots for existing storage volumes.

**Note:** Consider the following when requesting data volume snapshots: 

  * Google Cloud reserves 20% of the volume for snapshots. This leaves you with only 80% of the total volume to store data. For example, if you request 10 TiB of storage and enable snapshots, you receive 8 TiB of data storage and 2 TiB for the snapshot reserve.
  * When you place your order for data volume snapshots, you need to tell Google Cloud which action we should take when the snapshot reserve fills up: 
    * Delete the oldest snapshot first (recommended)
    * Delete the newest snapshot first
    * Take the volume offline



Google Cloud takes snapshots of the boot OS volume automatically every day at 12:10 AM in the region where your Bare Metal Solution servers are located. We also take a snapshot of your data volume if you have ordered this. We retain the snapshots for 7 days, and you cannot modify the schedule for these snapshots.

The following diagram shows the default process of how snapshots fill up a storage volume.

![Visual representation of how snapshots fill up a storage volume and need to be
deleted to allow new snapshots](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-snapshots.svg)

  * When Google Cloud enables snapshots on a data volume, we reserve 80% of the volume for regular data and 20% of the volume for snapshots. The latter is called the _snapshot reserve_.
  * When the snapshot reserve fills its original 20% space, the volume grows automatically by an additional 20%. This increases both the data area and the snapshot reserve proportionally.
  * If the snapshot reserve becomes 100% full, snapshots spill over into the data area.
  * If both the data area and snapshot reserve become 100% full, the volume goes offline to prevent corruption of the LUNs. Write operations are suspended.
  * To bring the volume back online, you need to reclaim sufficient space in the volume by deleting prior snapshots.



Your data volume might fill up as the result of a high rate of data change within the LUN(s). For example, an application might write and delete large amounts of data within a 24-hour period.

To delete data volume snapshots and bring a data volume back online, or restore an OS boot volume snapshot, contact [Customer Care](https://cloud.google.com/support-hub).

**Note:** We do not recommend taking snapshots of volumes that you use for Oracle database files. Instead, take appropriate backups of your Oracle database with tools such as RMAN or solutions such as Actifio to meet your recovery point objective (RPO).

## Networking

Each Bare Metal Solution environment resides in a secure region extension that is connected to the corresponding Google Cloud region by a [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) connection that is provided and managed by Google Cloud.

VLAN attachment pairs are used to connect your Bare Metal Solution environment to Google Cloud project and to on-premises network.

### Choose standard networking or explore advanced networking options

The standard networking configuration for Bare Metal Solution offers a basic network topology that is appropriate for most small-scale deployments. The standard networking configuration includes:

  * Four physical interfaces for each Bare Metal Solution server. We bundle the interfaces into two logical interfaces called bonds. These bonded interfaces use a standard networking template to provide basic redundancy and load balancing.

    * There are two `25 Gbps` physical interfaces per bond interface.
    * The first bond interface `bond0` connects a single _client network_ to the Google Cloud.
    * The second bond interface `bond1` connects a single _private network_ to services and applications running locally in your Bare Metal Solution environment.
    * By default, `bond0` is mapped to a _client network_ and `bond1` to a _private network_ created through the Google Cloud console intake form. However, in a multi-network configuration you can create _client_ and _private_ networks in any combinations.

    * A single Partner Interconnect VLAN attachment pair connects your Virtual Private Cloud to the _client network_ in your Bare Metal Solution environment

  * You create a Cloud Router before provisioning VLAN attachment pair.

    * Cloud Router is a distributed, highly available, software defined router in Google Cloud.
    * You can create and use a single Cloud Router for both VLAN attachments in the pair or separate Cloud Router for each VLAN attachment in the pair depending on your design. The diagrams in this document uses a single Cloud Router option.



In the following diagram, VRF is an interface connecting a _client network_ to a VLAN attachment pair. Learn more about [VRF](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_vrfs) in Bare Metal Solution.

![Standard Bare Metal Solution network configuration-1.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-single-vlan-networking.png)

We recommend using the following Bare Metal Solution standard networking configuration for small scale deployments:

![Standard Bare Metal Solution network configuration-2.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-standard-networking.png)

The standard networking configuration consist of the following:

  * A single _client network_ connects Bare Metal Solution servers to the Google Cloud using a single Partner Interconnect VLAN attachment pair.
  * A single _private network_ connects Bare Metal Solution servers to the local environment with other Bare Metal Solution servers.



If the standard networking configuration does not meet your needs, you can consider implementing some advanced networking capabilities. If you already have a Bare Metal Solution environment and would like to migrate to an advanced networking configuration, contact [Customer Care](https://cloud.google.com/support-hub). If you are a new customer and would like to implement an advanced networking configuration, contact [Google Cloud Sales](https://cloud.google.com/contact).

When your order an advanced networking configuration, the following options become available for more complex network deployments:

  * Multiple VLANs
  * Multiple VLAN attachments
  * Multiple VPC connections
  * Maximum transmission unit
  * Network templates



#### Multiple VLANs

Instead of a single _client network_ and single _private network_ for each bonded interface, you can add multiple _client networks_ and _private networks_ on server bond interfaces.

  * The additional networks can be the client or private, or a combination of both. 
    * You can add both client networks and private networks on `bond1` or on `bond0` interface.
  * You can add up to 10 Networks per bonded interface and a total of 20 networks per server.



![Advanced Bare Metal Solution network configuration-1.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-multi-vlan-networking.png)

  * Before adding multiple networks contact Cloud Customer Care and request a quota for additional networks. If you already have a quota for additional networks, skip this step.
  * After you [create and attach a network to a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#create-network) through the Google Cloud console you have the following two options to apply a new network configuration on the server: 
    * Manual configuration 
      * This option lets you configure your server manually with new network interfaces, IP addressing and the IP routing.
      * Follow [creating and attaching a network to a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#create-network) for instructions.
    * Through re-imaging 
      * The re-imaging will apply a network configuration to a server. No manual configuration needed. For instructions, follow:
      * Click the server
      * On the **Server details** page click **EDIT**
      * On **Edit Server** page select **Reimage server**
      * Specify the **OS image**.
      * Specify SSH keys if you are using Public Key Authentication to access the server.

**Warning:** Reimaging operation can take several hours to complete and it erases the boot LUN of your server.

#### Multiple VLAN attachments

You can configure multiple VLAN attachment pairs over a Partner Interconnect connection to your Bare Metal Solution environment.

  * This provides more bandwidth between your VPC and the Bare Metal Solution environment than the bandwidth offered by a single VLAN Attachment pair in a standard networking configuration.
  * To configure multiple VLAN attachment pairs, see [Create the VLAN attachments for the Partner Interconnect connection in Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-vlan-attachments).



![Advanced Bare Metal Solution network configuration-2.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-multi-vlan-attachment-networking.png)

#### Multiple VPC connections

You can connect the Bare Metal Solution environment to more than one Virtual Private Cloud (VPC) in your Google Cloud project.

**Note:** You cannot use the Bare Metal Solution environment as a transit path for routing between multiple Google VPC networks.

![Advanced Bare Metal Solution network configuration-3.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-multi-vpc-networking.png)

#### Maximum transmission unit

We recommend you to use the same maximum transmission unit (MTU) for every network to ensure consistent packet switching.

**Note:** BMX does not support Jumbo frame on VLAN attachments.

Following is the recommendation for setting up the MTUs for BMS environment:

  * Setting up the same standard MTU (1500) for every network segments on the traffic path 
    * Segments: Client Network, VLAN attachment, VPC network, on-premises network.
  * Configure the MTU on your Bare Metal Solution servers by using your server's operating system. 
    * For example, to configure MTU on a Linux server, issue the `ip link set INTERFACE_NAME mtu 1500` command on all server interfaces.
    * To verify the current MTU settings in a Linux server, issue the `ip link show | grep mtu` command.



#### Network templates

You can use network templates to enable a flexible network design of your choice, such as active/active and active/backup, to meet your needs for high availability, redundancy, and load balancing.

  * Templates allow for different combinations of connections between server interfaces, bonds, and switch ports.
  * To learn more about templates and request them for your Bare Metal Solution network, contact [Google Cloud Sales](https://cloud.google.com/contact).

**Note:** When you implement an advanced networking topology, network status might not appear correctly in the Google Cloud console or in the output of [`gcloud bms networks`](https://docs.cloud.google.com/sdk/gcloud/reference/bms/networks) and networking API commands.

#### Connecting Bare Metal Solution to Google Cloud project

We recommend that you create VLAN attachments in redundant pairs so they can be covered by the [SLA (Service Level Agreement))](https://cloud.google.com/network-connectivity/docs/interconnect/sla). Each VLAN attachment in the pair is provisioned in a different [EAD (Edge Availability Domain)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) for high availability.

![Bare Metal Solution network interconnect attachment-1.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-edge-availability-domain.png)

You can use the VLAN attachments in the pair in the following modes depending on how you configure your Cloud Router.

  * Active-Standby VLAN attachment mode
  * Active-Active VLAN attachment mode



In Active-Standby mode, you can use the primary VLAN attachment for traffic between Bare Metal Solution servers and the Google Cloud project while the secondary VLAN attachment as a standby.

Active-Standby mode can be configured by configuring higher [base route priority](https://docs.cloud.google.com/router/how-to/updating-priority) value on the secondary BGP session and the lower base route priority value on the primary BGP session.

Following example diagram shows the Active-Standby mode with `1 Gbps` bandwidth VLAN Attachment.

![Bare Metal Solution network interconnect attachment-2.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-active-standby-networking.png)

In Active-Active mode, you can configure to load share between both VLAN attachments in the pair for BMS traffic.

By default, the base route priority value on Cloud Router is 100 for all BGP sessions. This means that all VLAN attachment pairs will be used in Active-Active mode without any additional configuration.

Following example shows the Active-Active mode with `1 Gbps` bandwidth VLAN Attachment.

![Bare Metal Solution network interconnect attachment-2.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-active-active-networking.png)

We recommend you not to put a traffic more than the bandwidth of a single VLAN attachment when using in Active-Active mode. For example: If you create a VLAN attachment with `1 Gbps` bandwidth, then the total throughput you can get using Active-Active mode is `2 Gbps` (including the redundant pair). But you need to keep in mind that putting more traffic than `1 Gbps` could be risky in this case. In this example, you put `1.5 Gbps` traffic on your VLAN attachment pair and when one of the VLAN attachment goes under maintenance or networking event, you end up with `1 Gbps` bandwidth available and `1.5 Gbps` traffic which will result a congestion and a packet loss. Following diagram shows the issue where you put more traffic than single VLAN attachment bandwidth.

![Bare Metal Solution network interconnect attachment-2.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-active-active-networking-congestion.png)

#### Setting up a Google Cloud project for Bare Metal Solution (Internet, secure access)

You can optionally launch the following VMs on their Google Cloud project project for their Bare Metal Solution.

  * NATVM 
    * A Virtual Machine for providing Internet access to Bare Metal Solution servers. See [Internet Access solution for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet) for configuring the internet access for Bare Metal Solution servers.
  * JumpVM 
    * A Virtual Machine for providing secure remote access to Bare Metal Solution servers from the public internet
    * If you have a Cloud Interconnect (Partner or Dedicated interconnect) or a Cloud VPN connecting your on-premises network directly to Google Cloud project, you can connect from on-premises network to BMS directly without jumpVMs.
  * The following diagram shows an example setup of NATVMs and JumpVMs. 
    * For redundancy, the regional Instance groups have been used with multi-zonal deployment along with internal passthrough load balancers. For more information about regional resources, see [Global, regional, and zonal resources](https://docs.cloud.google.com/docs/regions-zones/global-regional-zonal-resources).
    * If you don't need highly available and scalable NATVMs or JumpVMs then a single instance for jumpVM and NATVM services can be launched and used. This will eliminate the need for Load Balancers.
    * NATVMs and JumpVMs are placed in their own subnets.
    * The diagram shows three different traffic flows: 
      * Green flow 
        * On-premises network -> Cloud Interconnect ( or cloud VPN) -> Partner Interconnect to BMS -> BMS server
      * Red flow 
        * BMS server -> Partner Interconnect -> NATVM -> Internet
      * Blue flow 
        * Remote or Home offices -> Public Internet -> JumpVMs -> BMS server



![Bare Metal Solution project setup-1.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-gcp-project-network-setup.png)

### Partner Interconnect for Bare Metal Solution

The connection between your Google Cloud environment and your Bare Metal Solution environment uses the Partner Interconnect framework.

For more information about the Partner Interconnect framework, see the [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) documentation, but keep in mind the following differences applicable in the context of Bare Metal Solution:

  * This connection to the Bare Metal Solution environment is not subject to the pricing model that the Partner Interconnect product uses. For more information about the pricing model, talk to your Google Cloud Sales representative.

**Note:** You do not have to order or manage physical connections to your Bare Metal Solution instances. Google Cloud manages them for you.

### Define your own IP address spaces

You can use your own IP subnets in the Bare Metal Solution environment. This lets you to fit your Bare Metal Solution into any existing IP address schema that your enterprise might have.

When you place an order for Bare Metal Solution, you provide two internal IP address ranges: a _client_ IP address range for communication between your Google Cloud and Bare Metal Solution environments, and a _private_ IP address range used for accessing services and devices within the Bare Metal Solution environment.

You can also select the specific IP addresses to use with each server. Consider the following guidelines:

  * Make sure that no existing IP addresses in your VPC network or your extended on-premises network conflict with the IP ranges that you use for Bare Metal Solution environment.
  * For every subnetwork that you request for Bare Metal Solution, Google Cloud reserves five IP addresses from the subnet range for administration purposes. These include the network address, the broadcast address, and the last three usable addresses in the range. For example, if you request the **100.64.0.0/27** subnet range, we reserve the following addresses:

    * **100.64.0.0** : Network address
    * **100.64.0.28** , **100.64.0.29** , and **100.64.0.30** : Last three usable addresses in the range.
    * **100.64.0.31** : Broadcast address
  * Request subnet ranges with at least a /27 subnet, so that you can assign the /28 subnet for Bare Metal Solution services. Subnets using /29 to /32 do not contain enough usable addresses for either Bare Metal Solution services or your Bare Metal Solution servers.

  * In an auto mode VPC network, **10.128.0.0/9** CIDR block is reserved. See [Auto mode IPv4 ranges](https://cloud.google.com/vpc/docs/subnets#ip-ranges). If you want to connect to an auto mode VPC network, use IP ranges outside of **10.128.0.0/9** for your Bare Metal Solution environment.

  * Bare Metal Solution does not support **Class E** IP addresses (**240.0.0.0** to **255.255.255.254**).




### Multi-region networking considerations

For any outside communication, including communication with services or your on-premises environments, the communication from your Bare Metal Solution environment must pass through the VPC network that you are using to connect to your Bare Metal Solution environment.

Consider using a single VPC network with [global_dynamic routing](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) enabled if your Bare Metal Solution environment will require access to other Google Cloud regions to connect to any of the following resources:

  * Other Bare Metal Solution environments
  * VMs in other regions
  * Other Google Cloud services
  * Your on-premises sites in other geographical locations



Using a VPC network with global dynamic routing and [custom advertisement mode](https://docs.cloud.google.com/router/docs/concepts/advertised-routes), you can set up a routed environment to connect your Bare Metal Solution instances directly to your Google Cloud and extended on-premises environments in other regions, without any additional configuration in Google Cloud.

Our recommendation is to advertise a default route on the BGP sessions to Bare Metal Solution. This enables you to:

  * Avoid having to make change to routes to the Bare Metal Solution environment even if things change in your VPC subnets or your on-premises environments.
  * Keep the routing table to Bare Metal Solution small and allow it to contain only one prefix.

**Note:** Your Cloud Router can terminate multiple BGP sessions from different environments, including your on-premises and Bare Metal Solution environments. If you set up custom advertisement mode, and want them to apply only to your Bare Metal Solution environment, use custom advertised routes at the BGP session level instead of the Cloud Router level, as detailed in [Setting up the Bare Metal Solution environment](https://docs.cloud.google.com/bare-metal/docs/bms-setup).

### Network services and your Bare Metal Solution environment

As described earlier, Google Cloud recommends that you advertise a single default route to your Bare Metal Solution environment to keep the routing table simple. However, if your circumstances don't allow that, the routes that you need to expose to your Bare Metal Solution environment are determined by networks and services in your Google Cloud or on-premises environments that need access to the devices or applications in your Bare Metal Solution environment and vice-versa.

Some services that might require routes include NTP servers, DNS servers, LDAP servers, logging services, monitoring services, and so forth, as well as any other workloads and applications that need to communicate with the Bare Metal Solution environment.

Bare Metal Solution does not come with internet access. If you need to, you can setup routing to access the internet through any existing internet gateways that you have, either on Google Cloud or on premises.

### Keeping routing simple

Outside of the other servers in the same Bare Metal Solution region, your servers likely need to communicate with one or more of the following:

  * Your endpoints in your Google Cloud environment
  * Your extended on-premises environment through your Google Cloud environment
  * Your servers in Bare Metal Solution environments in other regions through your Google Cloud environment
  * The internet through your Google Cloud environment

**Note:**

  * For simplicity and flexibility, we recommend configuring [custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) with a default route (0.0.0.0/0). 
  * Your Cloud Router can terminate multiple BGP sessions from different environments, including your on-premises and Bare Metal Solution environments. To apply custom advertised routes only to your Bare Metal Solution environment, use them at the BGP session level. 



### Firewalls and the Bare Metal Solution environment

When planning your firewall implementation for the Bare Metal Solution environment, there are a couple things to consider.

If you need to control traffic between the servers or applications within the Bare Metal Solution environment (east-west traffic), ask your Google Cloud sales representative for the available options.

In your VPC network on Google Cloud, you need to create firewall rules that allow incoming connections from the Bare Metal Solution environment.

**Note:** VPC firewalls do not apply to any traffic that transits your Google Cloud environment between, for example, your Bare Metal Solution environments and your other Bare Metal Solution or extended on-premises environments.

### Required networking information for your Bare Metal Solution order

When you submit a Bare Metal Solution order, include the following networking information:

  * The Google Cloud project ID that you are using with your Bare Metal Solution environment.
  * The IP ranges that you intend to use in your Bare Metal Solution environment. For example, the client IP address range used for communication between your Google Cloud and Bare Metal Solution environments, and the private IP address range used for services and devices within the Bare Metal Solution environment.
  * The number of VLANs you need in your Bare Metal Solution environment. Keep in mind that you need at least 2 VLANs for each Partner Interconnect.
  * The bandwidth, in `1 Gbps` increments, that you need between your Google Cloud environment and your Bare Metal Solution environment.



## Backup, restore, and disaster recovery

To protect against potential disruptions, we recommend that you plan and implement your solutions for backup, restore, high availability, and disaster recovery. For more information, see [Plan for disaster recovery](https://docs.cloud.google.com/bare-metal/docs/plan-for-dr).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
