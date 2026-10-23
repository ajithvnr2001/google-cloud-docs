---
url: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations/
title: Known issues and limitations \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:19.970601+00:00
---

# Known issues and limitations  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Known issues and limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known limitations of Google Cloud NetApp Volumes.

## General issues

This section describes common known issues of NetApp Volumes.

### Non-RFC 1918 (PUPI) client IP address support issues with Flex Unified service level

**Issue** : The Flex Unified service level doesn't support non-RFC 1918 (PUPI) client IP addresses.

**Reason** : This limitation is due to firewall rule constraints within the VSA tenant project.

**Solution** : To resolve this issue, consider the following options:

  * **Assign RFC 1918 IP addresses** : Configure your clients to use [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) private IP addresses.

  * **Use a different service level** : Use a service level that supports PUPI client IP addresses, such as Standard, Premium, Extreme, or Flex File.

  * **Request a manual firewall configuration** : As a temporary workaround, you can contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) to manually set up firewall ingress rules for your PUPI client range. Note that manual configuration might require ongoing support efforts. To proceed with this option, submit a support request with the following information:

    * Your client PUPI IP range (for example, `100.64.0.0/10`)

    * Required protocol ports (NFS, SMB, or iSCSI)

    * The target region and storage pool name




### `Not found` errors when running backup operations after volume creation

**Issue** : If you run backup operations such as `CreateBackup`, `RestoreVolume`, or `UpdateBackupConfig` immediately after you create an ONTAP mode volume, the operations can fail with a `Not found` error.

**Reason** : After you create a volume, the volume and its resources related to backup can take a short time to become fully available to the backup service. During this propagation period, the backup service might route backup requests before the volume is discoverable, which results in a `Not found` error.

**Solution** : Wait at least three minutes after you create the volume before running backup-related operations.

### Flex File volumes don't respond to ping

For more information about this issue, see [Test connectivity to NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/test-connectivity-netapp-volumes).

### Intermittent connectivity loss when using overlapping Private Services Access connections

When [configuring](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking) the `netapp.servicenetworking.goog` connection, if the CIDR range overlaps with the CIDR range used by another private services access connection on the same VPC, it can result in intermittent connectivity loss of the volume mount connection. Use non-overlapping ranges to avoid this problem.

### Possible disruption of client access to volumes transitioned from Cloud Volumes Service to NetApp Volumes when updating settings of an NFS volume

**Issue** : There is a disruption of client access to volumes when you update any settings on either the source or destination volume of an active volume replication with a mirrored transfer status.

**Reason** : Updating a volume can lead to synchronization of its export policy with the replication partner volume. If the updated volume has an incorrect or missing export policy, the clients mounted to the production source volume might lose access, potentially causing an outage.

**Background** : When a replication is in a mirrored state, NetApp Volumes automatically synchronizes the export policies of the source and destination volumes. This ensures consistent client access without manual intervention of the administrator, as any policy change on one volume is automatically applied on the other volume.

In CVS, the administrator needs to manually synchronize the source and destination volume settings. During the volume transition from CVS to NetApp Volumes, the existing export policies were transferred without modifications, which can lead to inconsistent export policies in replicated volumes. When you update the export policy of either the source or destination volume in a volume replication relationship automatically synchronizes the policies on both volumes.

**Affected volumes**

This issue applies to volumes that meet all of the following criteria:

  * Volumes that are in an active, mirrored volume replication. Resuming the replication after it's stopped can cause the issue.

  * All NFS-enabled volumes that have an export policy.

  * Volumes where the export policy differs between the source and destination.




**Solution** : To resolve this issue, the export policy of source and destination volumes must be synchronized once. Complete the following steps:

  1. Examine and compare the export policies of both the source and destination volumes.

     * If the export policies are identical, no action is required.

     * If the export policies are different, merge the export rules to create an export policy that allows all hosts specified in both policies.

  2. Apply the merged export policy to the source volume. This policy is also automatically applied to the destination volume.




By synchronizing the export policies, you can ensure consistent access and prevent potential disruptions to clients.

### Error message when using Cloud Volumes Service (CVS) and NetApp Volumes resources together

You might get an error message about using CVS and NetApp Volumes resources together within a VPC, project, or region. This issue can occur when you try to create resources such as pools and policies if either of the following is true for the project:

  * The project was previously used for CVS.

  * A CVS resource list operation was performed in a project that has no NetApp Volumes resources.




The following are the common error messages:

  * `Host project and service project must be using the same service`.

  * `Resources from CVS and NetApp Volumes may not be used together in a single region`.

  * `Cannot share VPC between 3P and 1P networks`.




To resolve this issue, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) and request a reset of your specific projects or regions to exclusively use NetApp Volumes resources.

### File creation fails with `No space left on device` or `File too large` errors in a specific directory

**Issue** : When attempting to write, copy, or create new files or subdirectories on a mounted volume, the operation fails with either a `No space left on device` (`errno 28` / `ENOSPC`) or a `File too large` (`errno 27` / `EFBIG`) error.

This occurs even when client-side disk space queries (such as `df -h`) and the Google Cloud console show that the volume has plenty of available logical capacity. The error is localized to a specific directory; file creation succeeds in other directories on the same volume.

**Reason** : This issue occurs when a single directory grows excessively large and hits internal limits, preventing the storage system from indexing more files or subdirectories in that specific location.

**Verification** :

Verify if you have hit directory size limits by performing the following diagnostic steps on a mounted client:

  1. **Test localized file creation** : Attempt to create a file in a completely different, newly created directory on the exact same volume: `bash mkdir /mount_point/test_dir && touch /mount_point/test_dir/test_file.txt` If this succeeds but writing to the original directory fails, the directory limit has likely been reached.
  2. **Estimate directory entry counts** : Count the number of entries inside the offending directory: `bash find /mount_point/offending_directory -maxdepth 1 | wc -l`
  3. **Inspect directory index file size** : Check the directory's metadata footprint: `bash ls -ld /mount_point/offending_directory` An exceptionally large directory file size indicates massive directory metadata bloat.



**Solution** :

To resolve this issue and keep your directory structures healthy, implement the following methods:

  * **Implement directory sharding** : Restructure your application or workload to distribute files across nested, hierarchical subdirectories (such as `/aa/bb/filename.txt` instead of keeping massive numbers of files in a single flat directory).
  * **Rebuild bloated directories** : Simply deleting files from an over-limit directory removes their names but does not automatically shrink the physical size of the directory index file in the underlying file system. To fully reclaim the directory's space, copy or move the active files into a new directory, then delete the old, bloated directory.



## Active Directory integration issues

The following sections contains known issues of Active Directory integration.

### Connectivity issues

Connections to on-premise domain controllers fail due to the following limitations:

  * **[VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions)** : NetApp Volumes can only reach domain controllers that are on the storage pool's Virtual Private Cloud (VPC) or are connected to it by VPN. NetApp Volumes can't reach domain controllers in any other VPC, including those that are peered to the storage pool's VPC and that connect to the storage pool.

  * **Firewalls** : The on-premise connection fails if you don't allow NetApp Volumes to contact your domain controllers. For more information, [Firewall rules for Active Directory access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#firewall_rules_for_active_directory_access).




Modifying the Active Directory site setting of an Active Directory policy doesn't affect Flex File service level storage pools. This setting works for Flex Unified pools.

### NetApp Volumes can't join Windows 2025 based domain controllers

Due to a regression in Windows 2025, NetApp Volumes can't join a domain using a Windows 2025 domain controller.

As of September 9, 2025, Microsoft has released [KB5065431](https://support.microsoft.com/en-gb/topic/september-9-2025-kb5065431-os-builds-22621-5909-and-22631-5909-c428cf71-e28d-490f-b0d7-a587ebab0667) and [KB5065426](https://support.microsoft.com/en-us/topic/september-9-2025-kb5065426-os-build-26100-6584-77a41d9b-1b7c-4198-b9a5-3c4b6706dea9) to address this issue. Windows 2025 doesn't support RC4 encryption, so you must [Enable AES Encryption for Active Directory authentication](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy).

For more information, see Domain controller communication with Windows 2025 or earlier versions can fail due to enforcement of SMB 3.1.1.

### Domain controller communication with Windows 2025 or earlier versions can fail due to enforcement of SMB 3.1.1

Windows 2025 domain controllers enforce SMB 3.1.1 for communication with Active Directory clients. The [Center for Internet Security (CIS) Policy 18.6.7.6](https://www.tenable.com/audits/items/CIS_Microsoft_Windows_11_Stand-alone_v5.0.0_L1.audit:2e26c6ad69e147013d428054de7c57e3) also recommends using SMB 3.1.1 for earlier Windows versions.

Although NetApp Volumes supports SMB 3.1.1 for communication between SMB clients and the NetApp Volumes SMB server, it supports only SMB 2.1 and SMB 3.0 when connecting to Active Directory as a client.

If domain controllers allow only SMB 3.1.1 connections, NetApp Volumes can't connect to Active Directory, which causes service disruptions.

To maintain compatibility, we recommend setting SMB 2.1 as the minimum supported SMB version on your domain controllers. You must apply this setting to all domain controllers, or to every domain controller in the Active Directory site if you use site-based Active Directory policies.

The following example shows how to set the minimum supported SMB version to 2.1:
    
    
     Set-SmbServerConfiguration -Smb2DialectMax SMB311 -Smb2DialectMin SMB210
    

For more information about modifying SMB settings using PowerShell or group policies, see [Manage SMB dialects in Windows and Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/storage/file-server/manage-smb-dialects?tabs=powershell).

## CMEK issues

The following sections contains known issues of customer-managed encryption key (CMEK) operations.

### `ListKmsConfigs` returns `Invalid value for enum type` error

While a volume migrates from system-managed to customer-managed encryption, the `ListKmsConfigs` command occasionally returns an `Invalid value for enum type` error during migration. After the migration finishes, the `ListKmsConfigs` command returns to working normally.

### `KmsConfig` policy creation fails

Occasionally, `KmsConfig` policy creation fails and blocks you from creating another policy. If this occurs, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/).

## Volume replication issues and limitations

The following sections provide details about known issues and limitations of the volume replication feature.

### Destination volume quota settings might fail in an active replication

When modifying settings on a volume in an active replication, the [settings are applied to both the source and destination volumes](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#settings_modifications). However, quota changes specifically for destination volumes are staged and get applied to the destination volume once the replication is stopped. Occasionally, this quota setting might fail, and you will receive an error message at the end of the operation. While the _Stop_ operation succeeds, all of the quotas might not have been applied to the destination volume. If you receive a quota error during a _Stop_ operation, compare the quota rules on both the source and destination volumes and then update any missing quota rules on the destination to match the source volume settings.

### Google Cloud console displays storage pools without associated Active Directory policies

In the Google Cloud console, when you create a volume replication for a source volume, the list of storage pools to choose from to create the destination volume contains storage pools that don't have an Active Directory policy. Selecting a storage pool without an Active Directory policy leads to replication failure.

## Large capacity volumes known issues

The following section describes known issues of the large capacity volumes feature.

### Incompatible pools displayed

When changing the storage pool (service level), the Google Cloud console might show incompatible pools. If you try to change to an incompatible storage pool, the attempt fails and you receive an error message.

### CMEK migration not blocked

CMEK migration isn't blocked by the Google Cloud console and is allowed even when large capacity volumes are present. If you try CMEK migration when large capacity volumes are configured, the attempt will fail.

## FlexCache issues

This section describes known issues of the FlexCache feature.

### FlexCache volume modifications in Google Cloud console might fail

FlexCache volumes can only be modified using the API or the Google Cloud CLI. While FlexCache volumes are displayed in the Google Cloud console after creation, they can be viewed or deleted, and attempts to update them using the Google Cloud console might fail. In such cases, use the Google Cloud CLI for modifications.

### FlexCache volume creation fails with `snapshot-directory` set to true

FlexCache volumes don't support the `snapshot-directory` option. While the API defaults this parameter to `false`, the Google Cloud CLI defaults it to `true`. Therefore, when creating a FlexCache volume using Google Cloud CLI, you must explicitly include `--snapshot-directory false` to prevent creation failure.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
