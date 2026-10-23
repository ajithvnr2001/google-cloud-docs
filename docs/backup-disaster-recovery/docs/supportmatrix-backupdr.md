---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr/
title: Support matrix for appliance-managed backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:45.125903+00:00
---

# Support matrix for appliance-managed backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Support matrix for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

## Backup and DR end-of-support-life policy

The Backup and DR End-of-Support-Life ("EOSL") Policy covers the process and details regarding the end of support from Backup and DR for third-party systems and software, as well as Backup and DR software and hardware.

Third-party hardware and software include hardware platforms, operating systems, and application software protected by backup/recovery appliances. When a third-party hardware, operating system, or application software configuration reaches EOSL from the vendor, Backup and DR support for such configurations will be limited to commercially reasonable assistance.

Backup and DR won't issue any more hotfixes or updates to support software and hardware systems that are beyond the end of support life from their respective vendors.

## Supported network protocols

Backup and DR supports data movement over:

  * Network Block Device (NBD): This transport mode is used to back up Google Cloud VMware Engine virtual machines.

  * NFS: Backup and DR supports NFS V3 (only) for capturing and presenting data in following deployment configurations:

    * Presenting any backups to Google Cloud VMware Engine hosts using a NFS datastore

    * Presenting a staging disk for agent-based data capture within a Compute Engine or Google Cloud VMware Engine VM




## Supported environments for backups

The agent is supported in these environments.

### Agent based backups

The Backup and DR agent can back up and recover supported databases and file systems of supported Microsoft Windows & Linux operating systems in the following environments.

Application Type | Running on Compute Engine instances | Running on Google Cloud VMware Engine VMs  
---|---|---  
Databases | Yes | Yes  
File Systems | Yes | Yes  
**Note:** CBT on Compute Engine instances and Google Cloud VMware Engine VMs requires UEFI Secure Boot to be disabled.

### Agentless backups

Backup and DR supports VM backups in the following environments without needing an agent inside the VM:

  * Compute Engine and Cloud SQL instances (leverages Persistent Disk snapshot APIs)
  * SAP HANA and IBM Db2 databases that are backed up to Persistent Disk
  * Google Cloud VMware Engine VMs (leverages VMware vSphere Storage APIs - Data Protection (formerly known as vStorage APIs for Data Protection or VADP))



## Object storage compatibility for OnVault

OnVault supports the following Google Cloud storage:

  * Standard storage
  * Nearline storage
  * Coldline storage
  * Archive storage



## Application data virtualization with the Backup and DR agent

Backup and DR agent (commonly also known as connector) is a lightweight executable that delivers the following advanced capabilities during the data capture and recovery processes.

  * **Application Discovery** : Backup and DR agent enables deep discovery of databases and file systems configured on a production host

  * **API integration** : Where possible, Backup and DR agents integrate with the application specific APIs/commands for efficient capture of application data

  * **Change Block Tracking** : In situations where the production applications don't have a built-in change block tracking, Backup and DR introduces change block tracking on select platforms

  * **Application aware recovery/mount** : Backup and DR agents have built in application awareness. The Backup and DR agent lets you instantiate usable instances of applications during recovery mount operations thereby eliminating the need for performing manual scripted actions post mount.

  * **Generic Application (LVM) Data Capture framework** : Backup and DR agents provide a generic framework to capture data from any application running on supported Linux operating systems. This framework provides hooks to call custom scripts to achieve application consistent data capture and application instantiation from backup data.




### Microsoft Windows Server support

The Backup and DR agent supports the following Microsoft Windows operating systems.

Operating System Version | Basic Backup and DR agent Support | Change Block Tracking Support for SQL Server  
---|---|---  
Windows Server 2025 Datacenter | Yes | Yes  
Windows Server 2025 Datacenter Core | Yes | Yes  
Windows Server 2022 Datacenter | Yes | Yes  
Windows Server 2022 Datacenter Core | Yes | Yes  
Windows Server 2019 Datacenter | Yes | Yes  
Windows Server 2019 Datacenter Core | Yes | Yes  
Windows Server 2016 Datacenter | Yes | Yes  
Windows Server 2016 Datacenter Core | Yes | Yes  
  
### Linux operating system support

Backup and DR agent supports the following Linux (x86) operating systems.

Basic support includes support for file systems and Oracle databases.

Change Block Tracking (CBT) support includes incremental forever backup capability for other databases.

OS | Version | Basic Backup and DR agent Support | Change Block Tracking Support | Min required Backup and DR agent Version  
---|---|---|---|---  
RHEL1,4 / Rocky Linux | 8.10 | Yes | Yes | V11.0.16  
| 9.4 | Yes | Yes | V11.0.16  
| 9.6 | Yes | Yes | V11.0.16  
| 9.8 | Yes | Yes | V11.0.17  
RHEL1,4 | 10 | Yes | Yes | V11.0.17  
| 10.2 | Yes | Yes | V11.0.17  
RHEL for SAP 1 | 8.8 | Yes | Yes | V11.0.16  
| 8.10 | Yes | Yes | V11.0.16  
| 9.2 | Yes | Yes | V11.0.16  
| 9.4 | Yes | Yes | V11.0.16  
| 9.6 | Yes | Yes | V11.0.16  
SLES 1, 3 | 12 SP5 | Yes | Yes | V11.0.16  
| 15 SP5 | Yes | Yes | V11.0.16  
| 15 SP6 | Yes | Yes | V11.0.16  
| 15 SP7 | Yes | Yes | V11.0.16  
SLES for SAP 1, 3 | 12 SP5 | Yes | Yes | V11.0.16  
| 15 SP5 | Yes | Yes | V11.0.16  
| 15 SP6 | Yes | Yes | V11.0.16  
| 15 SP7 | Yes | Yes | V11.0.16  
Rocky Linux optimized for Google Cloud | 8.x | Yes | No | V11.0.16  
| 9.x | Yes | No | V11.0.16  
Ubuntu | 20.04 LTS | Yes | No | V11.0.16  
| 22.04 LTS | Yes | No | V11.0.16  
| 24.04 LTS | Yes | No | V11.0.16  
Oracle Linux 1, 2 | 8.105 | Yes | No | V11.0.16  
| 9.65 | Yes | No | V11.0.16  
  
1 Symantec (Veritas) Dynamic Multi Pathing (DMP) is NOT supported.

2 Supported only on Google Cloud VMware Engine VMs and not on Compute Engine instances/VMs

3 During "offline" upgrade of SuSE (upgrade from ISO), the SuSE installer does not run a reconfigure on external packages, including the CBT module and DLKM. As a result, when the system boots up with the updated kernel, the dlkm is unable to load because the old configuration files still point to the older kernel module. Upgrade of OS from ISO is not supported.

4 Backup and DR does not support RHEL HA.

5 Supported on both Red Hat Compatible Kernel (RHCK) and Unbreakable Enterprise Kernel (UEK) versions.

#### Supported Linux OS kernels

See the list of [supported kernels](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/backupdr-supported-os-kernels).

### Microsoft SQL Server

Backup and DR agents version 11.0.16 and later support database consistent data capture (snapshots) from Microsoft SQL Server.

SQL Server Version | Windows Server Version  
---|---  
SQL Server 2022 Standalone | Windows Server 2025  
| Windows Server 2022  
| Windows Server 2019  
| Windows Server 2016  
SQL Server 2022 Web | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
| Windows Server 2019 Datacenter  
SQL Server 2022 Standard | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
| Windows Server 2019 Datacenter  
SQL Server 2022 Enterprise | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
| Windows Server 2019 Datacenter  
SQL Server 2019 Web | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
SQL Server 2019 Standalone | Windows Server 2025  
SQL Server 2019 Standard | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
| Windows Server 2019 Datacenter  
SQL Server 2019 Enterprise | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
| Windows Server 2019 Datacenter  
SQL Server 2017 Standalone | Windows Server 2025  
SQL Server 2017 Web | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
SQL Server 2016 Web | Windows Server 2025 Datacenter  
| Windows Server 2022 Datacenter  
**Note:** 1\. No support for app-aware mounts into a SQL Server instance running on a Microsoft Failover Cluster if any of its nodes have been discovered as a Google Cloud VMware Engine VM.

  1. Application consistent protection of SQL Server Instance hosted on Windows SMB shares is not supported.



### IBM Db2

Backup and DR supports the following data capture methods:

  * Db2 on Linux can be captured at the volume level in an incremental-forever fashion with instant access and virtual clone creation for Test Data Management (TDM). This leverages Linux LVM and Backup and DR's Changed Block Tracking capabilities and is the recommended alternative.

  * For customers not using LVM or who cannot use volume level capture, Db2 on Linux can alternatively be captured using full + incremental backup. This uses the database's own dump-based backup.


Supported IBM Db2 versions | Supported OSes | Min required Backup and DR agent version  
---|---|---  
10.5 | SLES 12 | V11.0.16  
11.1.0 | SLES 12 | V11.0.16  
11.5.0 | SLES 12 | V11.0.16  
11.5.8.0 | RHEL 8.x  
SLES 12 and 15 | V11.0.16  
11.5.9 | RHEL 8.8, 8.10, RHEL 9.x | V11.0.16  
12.1 | RHEL 9.x   
SLES 15 SP6, SLES 15 SP7 | V11.0.17  
  
### Oracle

Backup and DR agents enable database consistent data capture of Oracle databases. Oracle must be run in ARCHIVELOG mode. Data capture supports capturing data to staging disks formatted as file systems or presented as ASM disk group targets.

Oracle database protection is the same for databases running on Bare Metal Solution servers or inside a Compute Engine instance.

Data can also be captured from Oracle Non Active Data Guard and Active Data Guard configurations.

Oracle family | Config types | Supported OSes | Min required Backup and DR agent version  
---|---|---|---  
Oracle 21c  
All Versions | Standalone | RHEL 8.4  
Rocky Linux 8.7  
Windows 2016, 2019 | V11.0.16  
| RAC | RHEL 8.4  
Rocky Linux 8.7  
Windows 2016, 2019 | V11.0.16  
| Exadata 1 | RHEL 8.4  
Rocky Linux 8.7  
Windows 2016, 2019 | V11.0.16  
| Non Active Data Guard 2 | RHEL 8.4  
Rocky Linux 8.7  
Windows 2016, 2019 | V11.0.16  
| Active Data Guard 2 | RHEL 8.4  
Rocky Linux 8.7  
Windows 2016, 2019 | V11.0.16  
Oracle 19c 3  
All Versions | Standalone | OEL 7.x, 8.x, 9.0, 9.6  
RHEL 8.x, SLES 12, 15  
Windows 2016, 2019  
RHEL 8.10   
RHEL 9.5 with kernel 5.14.0-503.23.1 | V11.0.16  
| ASM Standalone | OEL 9.6 | V11.0.17  
|  | Rocky Linux 8.7 | V11.0.16  
| RAC | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
|  | Rocky Linux 8.7 | V11.0.16  
| Exadata 1 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
|  | Rocky Linux 8.7 | V11.0.16  
| Non Active Data Guard 2 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
|  | Rocky Linux 8.7 | V11.0.16  
| Active Data Guard 2 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
|  | Rocky Linux 8.7 | V11.0.16  
Oracle 18c 3  
All Versions | Standalone | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
| RAC | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
| Exadata 1 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
| Non Active Data Guard 2 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
| Active Data Guard 3 | OEL 7.x, 8.x, 9.0  
RHEL 8.x  
SLES 12, 15  
Windows 2016, 2019 | V11.0.16  
  
1 Oracle Exadata system is supported with iSCSI and NFS

2 Oracle database RMAN change block tracking is available on Active Data Guard only

3 Data capture of Oracle 18c and later is at container level (that includes all PDBs). App-aware mount on a target is at container level. Virtual PDBs to an existing container is supported using custom scripts.

#### Supported data capture and data presentation methods

Backup and DR supports a variety of capture and presentation methods for Oracle databases under various configurations. This includes backup, recovery and App aware mount operations of Oracle database with TDE (Transparent Data Encryption). For Oracle databases with TDE, the wallet for TDE can be captured by setting the Oracle Configuration file location advanced setting for the Oracle app. App aware mounts for TDE enabled databases requires the wallet to be copied to the appropriate location on the mount host.

**Note:** Recovery of Oracle data captured from a big-endian machine onto a little-endian machine and the other way around are not supported.

Also note that dNFS with Oracle is supported on Linux operating systems.

Production DB Configuration | Capture Format1 | Presentation Format  
---|---|---  
DB files on ASM/RAC | File system (Block Device) | Standalone file system  
| File system (NFS) | Standalone file system (NFS)  
| File system (NFS) | RAC File system (NFS)  
| ASM Disk Group 3, 5 | Standalone ASM  
| ASM Disk Group 3, 5 | ASM RAC (one or more nodes)  
DB files on file system | File system (Block Device) | Standalone file system  
| File system (NFS) | Standalone file system (NFS)  
| ASM Disk Group 3, 4, 5 | Standalone ASM  
| ASM Disk Group 3, 4, 5 | ASM RAC (one or more nodes)  
  
1  Capture Format is the resulting format of the copy managed by Backup and DR.

3 Capture from ASM to ASM and presentation of backups in ASM format not supported on Windows operating systems

4 Oracle ASM instance required on the source system for this capture method

5 The combination of ASM Disk (capture format) is not supported when data is captured over NFS

Supported Data Capture formats | Using File System | Using ASM Disk Group  
---|---|---  
Backup support | HCC or Non HCC Data |   
Oracle Recovery using RMAN | HCC or non HCC |   
App-Aware Mount 1 | Exadata to non Exadata |   
  
1 Accessing data from virtual copies of HCC compressed data will require the data to be uncompressed before access

#### Oracle exadata support

Backup and DR supports the following configurations of Oracle Exadata.

  * Exadata Database Machine versions: X4 and higher

  * Oracle versions: 18c and 19c


**Note:** Support is limited to Exadata machines running Oracle Enterprise Linux version 6.0 and later.

### PostgreSQL

Backup and DR supports the following data capture methods:

  * PostgreSQL on Linux can be captured at the volume level in an incremental-forever fashion with instant access and virtual clone creation for TDM. This leverages Linux LVM and Backup and DR's Changed Block Tracking capabilities and is the recommended alternative.

  * For customers not using LVM or who cannot use volume level capture, PostgreSQL on Linux can alternatively be captured using full + incremental backup. This uses the database's "pg_dump" command, that does not support incremental backup, so each backup will be a full database dump backup.

  * Due to limitations with PostgreSQL, the roll forward recovery is not supported for full+incremental backups restore operation.


Supported PostgreSQL versions | Supported OSes | Min required Backup and DR agent version  
---|---|---  
10.23 | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
11.x | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
12.x | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
13.x | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
14.x | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
| RHEL 8.8, 8.10  
Rocky Linux 9 | V11.0.16  
15.x | RHEL 8.4 | V11.0.16  
| RHEL 8.6 | V11.0.16  
| RHEL 8.8, 8.10, RHEL 9.x  
SLES 15 SP7 | V11.0.16  
16.x | RHEL 8.10 | V11.0.16  
| RHEL 8.10, RHEL 9.x  
Rocky Linux 9, SLES 15 SP7 | V11.0.16  
  
### SAP

Backup and DR supports SAP on all the databases supported in this document.

### SAP ASE (formerly Sybase ASE)

Backup and DR supports the following data capture methods:

  * SAP ASE on Linux can be captured at the volume level in an incremental-forever fashion with instant access and virtual clone creation for TDM. This leverages Linux LVM and Backup and DR's Changed Block Tracking capabilities and is the recommended alternative.

  * For customers not using LVM or who cannot use volume level capture, SAP ASE on Linux can alternatively be captured using full + incremental backup. This uses the database's own dump-based backup and typically runs as a weekly full and daily incremental. Recovery involves reconstructing the incrementals on top of the latest full backup.


Supported SAP ASE versions | Supported OSes | Min required Backup and DR agent version  
---|---|---  
16.0.x | SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| SLES 15 SP4 | V11.0.16  
| SLES 15 SP5 | V11.0.16  
| SLES 15 SP6 | V11.0.17  
| SLES 15 SP7 | V11.0.17  
| RHEL 8.8, 8.10, RHEL 9.x | V11.0.16  
  
### SAP HANA

Backup and DR agent supports capturing SAP HANA in the following configurations.

Supported Configuration | SAP HANA SavePoint API 2 | SAP file-based (HDBSQL/Backint) 3 | Supported OSes | Min required Backup and DR agent version  
---|---|---|---|---  
Scale-out HANA 2.0, non shared storage | Yes (preferred) 1 | Yes | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 8.6  
SLES 15 SP4 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 8.8 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 8.10 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 9.2 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 9.4 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 9.5 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 9.6 | V11.0.16  
| Yes (preferred) 1 | Yes | SLES 15 SP5 | V11.0.16  
| Yes (preferred) 1 | Yes | SLES 15 SP7 | V11.0.16  
Scale-out HANA 2.0, shared storage 4 | Not Supported | Yes | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| Not Supported | Yes | RHEL 8.6  
SLES 15 SP4 | V11.0.16  
| Yes (preferred) 1 | Yes | SLES 15 SP5 | V11.0.16  
SAP HANA 2.0 Standalone or HA (1+1) | Yes (preferred) 1 | Yes | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| Yes (preferred) 1 | Yes | RHEL 8.6  
SLES 15 SP4 | V11.0.16  
| Yes (preferred) 1 | Yes | SLES 15 SP5 | V11.0.16  
Single Container System (HANA 1.0) 5 | Yes (preferred) | Yes | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| Yes (preferred) | Yes | RHEL 8.6  
SLES 15 SP4 | V11.0.16  
| Yes (preferred) 1 | Yes | SLES 15 SP5 | V11.0.16  
  
1 Requires SAP HANA 2.0 SPS 04 or later

2 In this table, 'SAP HANA SavePoint API' is referring to SAP HANA backup leveraging Backup and DR CBT and its supporting incremental-forever and app-aware instant mount feature with log roll-forward option. It is not referring to SAP HANA backup leveraging Persistent Disk snapshots. When using the SAP HANA SavePoint API with Persistent Disk snapshots, scale-out HANA configurations are not supported.  
Backup and DR supports CBT with HANA on RHEL 7.2 and later. For a full list of CBT qualified RHEL versions, see Linux Operating System Support.

3 SAP HANA Backint mode only supports weekly full with daily incrementals. Supports HANA recovery using HANA HDBSQL/Backint commands. Also App-aware instant mount capability is not supported with HANA File-based (HDBSQL/Backint) API.

4 Supports only Backup and DR NFS disk mapping option. NFS disk is always mapped to all HANA nodes

5 Supports both Backup and DR block and NFS disk mapping options

**Note:** HANA log backup is integrated with database backup policies and is handled automatically in all of these configurations.

### SAP MaxDB

Backup and DR supports the following data capture methods:

  * SAP MaxDB on Linux can be captured at the volume level in an incremental-forever fashion with instant access and virtual clone creation for TDM. This leverages Linux LVM and Backup and DR Changed Block Tracking capabilities and is the recommended alternative.

  * For customers not using LVM or who cannot use volume level capture, MaxDB on Linux can alternatively be captured using full + incremental backup. This uses the database's own dump-based backup and typically runs as a weekly full and daily incremental. Recovery involves reconstructing the incrementals on top of the latest full backup.


Supported SAP MaxDB versions | Supported OSes | Min required Backup and DR agent version  
---|---|---  
7.9.09 | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
7.9.10 | RHEL 8.4 | V11.0.16  
| RHEL 8.6  
SLES 15 SP4 | V11.0.16  
| RHEL 8.8, 8.10, RHEL 9.x | V11.0.16  
| SLES 15 SP5 | V11.0.16  
  
### SAP IQ (formerly Sybase IQ)

Backup and DR supports capturing SAP IQ at the volume level in an incremental-forever fashion with instant access and virtual clone creation for TDM. This leverages Linux LVM and Backup and DR Changed Block Tracking capabilities and is the recommended alternative.

Supported SAP IQ versions | Supported OSes | Min required Backup and DR agent version  
---|---|---  
SAP IQ 16.x (Full + Incremental) | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
SAP IQ 16.x (LVM, CBT) | RHEL 8.4  
SLES 12 SP5  
SLES 15 SP3 | V11.0.16  
| RHEL 8.6  
SLES 15 SP4 | V11.0.16  
SAP IQ 16.x (Full + Incremental, LVM) | RHEL 8.8, 8.10, RHEL 9.x | V11.0.16  
| SLES 15 SP5 | V11.0.16  
  
### File systems

Backup and DR agents discover each volume on a network mount point as a protectable application. For each of these discovered applications, Backup and DR agent orchestrates the process of achieving consistency (through VSS/LVM snapshots), presents a staging disk which will be formatted with a file system of the same type as source or a compatible file system type as documented here.

Operating System | Source FS | Staging Disk FS | Min required Backup and DR agent Version  
---|---|---|---  
Windows | NTFS | NTFS | V11.0.16  
| SMB | NTFS | V11.0.16  
| ReFS | ReFS | V11.0.16  
Linux1 | EXT2 | EXT2 or NFS4 | V11.0.16  
| EXT3 | EXT3 or NFS4 | V11.0.16  
| EXT4 | EXT4 or NFS4 | V11.0.16  
| XFS | XFS or NFS4 | V11.0.16  
| ReiserFS | ReiserFS or NFS4 | V11.0.16  
| NFS | EXT3 or NFS4 | V11.0.16  
| BTRFS | EXT3 or NFS4 | V11.0.16  
  
1 LVM snapshot is used as source, if present. LVM mount back to same server is supported

2 Built in versions only

3 Encryption not supported

4 Only V3 of NFS protocol is supported

## Test data management with containers

Backup and DR leverages NFS volumes to make captured application data available as NFS shares to containers. This allows for creating virtual clones of supported databases that's accessible from within the containerized environment.

**Note:** Only PostgreSQL databases on supported Linux OS are eligible for Test Data Management with containers.

## Data virtualization for virtual environments

Backup and DR supports data virtualization for virtual environments using the following methods:

### Google Cloud VMware Engine

Backup and DR supports capturing data from VMware virtual machines by using VMware vSphere Storage APIs - Data Protection (formerly known as vStorage APIs for Data Protection or VADP) calls to capture an entire virtual server. Specifically, the API calls can:

  * Perform change block tracking: Makes an initial full snapshot of a database, then afterward only snapshots the changes to the database, enabling Backup and DR's incremental forever capture strategy.

  * Quiesce applications: Ensures application consistency during capture.


**Note:** Protection of VMware View virtual machines not supported.vCenter 1, 6 | 7.0, 7.0 U1, 7.0 U2, 7.0 U3, 8.0, 8.0 U3  7  
---|---  
ESX Server 6 | 7.0, 7.0 U1, 7.0 U2, 7.0 U3, 8.0.3 starting with Backup and DR V11.0.17  
Virtual Hardware 2 | 7 to 15 and 17 to 19  
Guest OS | All Google Cloud VMware Engine supported OSs  
Quiesce applications 3 | Yes, based on VMware Tools  
vSAN Support 4 | vSAN 7.0 U1, vSAN 7.0 U2, vSAN 7.0 U3  
Change Block Tracking5 | Leverages VMware vSphere Storage APIs - Data Protection (formerly known as vStorage APIs for Data Protection or VADP)  
  
1 This leverages VMware VDDK version 7.0. VDDK 8.0.3 is supported in Backup and DR 11.0.17 and later. 2 NVME Controller types (found on ESX 7.0 and later) are not supported. Virtual hardware version 14 and later are supported only with ESX 7.0 (and later)

3 Capability applicable to any application with a VSS Writer or pre and post scripts to achieve application consistent capture.

4 Since VMware vSAN does not support RDM device access features, mounting of a VM is not supported by Backup and DR when using RDMs. Restores and Clones of VMs are supported. However, mounting of a VM is supported on Backup and DR when using NFS transport instead of RDM.

5 Not supported for disks presented to production VMs as pRDM.

6 Configuring SAN transport mode to backup staging disk (agent based backups) and mounting and restoring backups using iSCSI is not supported.

7 VMware vCenter Server 8.0 is supported on Backup and DR 11.0.16 and later, and 8.0.3 is supported in 11.0.17 and later.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
