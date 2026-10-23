---
url: https://docs.cloud.google.com/filestore/docs/snapshots/
title: Snapshots overview \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:49.532198+00:00
---

# Snapshots overview  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Snapshots overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes what a snapshot is, how it works, and discusses limitations and best practices.

To see how to use snapshots, see the following guides:

  * [Preserve the state of your data with snapshots](https://docs.cloud.google.com/filestore/docs/create-snapshots)
  * [Restore a file from a snapshot](https://docs.cloud.google.com/filestore/docs/restore-file)
  * [Revert a file share to a prior snapshot](https://docs.cloud.google.com/filestore/docs/revert-snapshot)
  * [Schedule Filestore snapshots](https://docs.cloud.google.com/filestore/docs/schedule-filestore-enterprise-snapshots)



## What is a snapshot?

A Filestore snapshot is the preserved state of your file share data at the time that the snapshot is created. The instance maintains the state of files that are modified after the snapshot is created. If you want to restore a file to the preserved state in the snapshot, you can overwrite the current file with the file from the relevant snapshot directory.

Snapshots are stored within the Filestore instance and are child resources of the instance. They don't replicate any data or consume capacity until the data on the instance is modified. All snapshots of an instance share in-common data, meaning that the instance preserves only the differences between the snapshots.

While snapshots do offer cost efficiency when compared to other Filestore data recovery operations, available instance capacity continuously decreases as file modifications are made.

### Supported tiers

The following table shows which Filestore service tiers support snapshots and the [`revert instance`](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/revert) operation:

Tier | Create snapshot | Revert instance  
---|---|---  
Basic HDD | No | No  
Basic SSD | No | No  
Zonal | Yes | Yes  
Regional | Yes | Yes  
Enterprise | Yes | Yes  
  
Snapshots and related `revert` operations are also supported in the formerly available high scale SSD [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#former-tiers).

While snapshots are supported in the enterprise service tier, they can't be combined with the [Filestore multishares](https://docs.cloud.google.com/filestore/docs/multishares) feature.

## Snapshot creation

Every directory of a file share contains a hidden `.snapshot` directory. Each `.snapshot` directory contains the snapshots of its parent directory that you create, for example:
    
    
    volume1/
    │   genomics-file.txt
    │
    └───.snapshot
        │
        ├───snap1/
        │        genomics-file.txt
        │
        ├───snap2/
        │        genomics-file.txt
        │
        └───snap3/
                 genomics-file.txt
    

The snapshots contain a read-only view of all files and subdirectories that exist within its parent directory at the time of snapshot creation. All file attributes such as `atime`, `ownership`, and read and write permissions are preserved.

Snapshot creation usually takes no longer than two minutes to complete because it doesn't involve the copying of data, and it doesn't affect instance performance.

You can have up to 240 snapshots per instance at a time. The file share name and snapshot name can have a combined length of up to 78 characters.

## Snapshot consistency

Filestore snapshots have NFSv3 consistency semantics. Before a snapshot is initiated, any write that the Filestore instance acknowledges as written to stable storage or that is followed by an acknowledged `COMMIT` is included in the snapshot. For details, see [NFSv3 RFC-1813 section 3.3.7](https://tools.ietf.org/html/rfc1813#section-3.3.7).

## Prepare your file share for the best snapshot consistency

The quality of a snapshot depends on the ability of your application to recover from snapshots that are created during heavy write workloads. In most situations, you can create snapshots that have good consistency even while your applications write data to the file share. However, if your applications require strict consistency, we recommend doing one or more of the following:

  * Use the [**sync**](https://linux.die.net/man/5/nfs) mount option or open files with the [`O_DIRECT|O_SYNC`](https://linux.die.net/man/2/open). Either of these methods improves consistency but does not guarantee it.
  * Pause applications or operating system processes that write data to the file share and cause them to flush their changes to the file share before initiating the snapshot. For more information, see [fsync(2)](https://linux.die.net/man/2/fsync).
  * If your applications require consistency between multiple shares, pause all applications on all instances that are writing to all file shares and create snapshots of all file shares before resuming your applications.
  * If you require application level consistency, stop your applications and unmount the file share before creating a snapshot.



## NFS semantics of the `.snapshot` directory

The `.snapshot` directories are special hidden directories that contains the snapshots taken for its parent directory. All NFS and bash commands work for these directories with the following exceptions:

  * You cannot create a file or directory named `.snapshot` because it is reserved for snapshots.
  * The `.snapshot` directory is not listed in the outputs of `READDIR` or `READDIRPLUS` commands, and is also not listed in the `ls -a` bash command.
  * To change to a `.snapshot` directory, you must explicitly type out the `.snapshot` string. Example: `cd somedir/.snapshot/`
  * Auto complete for shell commands won't list `.snapshot` as an option.



## Delete files that are captured in a snapshot

When a file is captured in a snapshot, deleting it does not increase free disk space on your instance.

## Revert to a snapshot state

Reverting an instance to a snapshot state is [generally available](https://cloud.google.com/products#product-launch-stages) for zonal, regional, and enterprise instances only.

When an instance is reverted to the state captured in a snapshot, all new data written since the creation of the target snapshot is deleted and can't be recovered. Snapshots that are created after the target snapshot are also deleted by the revert process.

### Feature limitations

  * The revert snapshot feature is an irreversible operation, deleting data from the live file system and deleting each subsequent, newer snapshot in the chain. Therefore, it has a higher risk of accidental data loss. This is significantly different behavior when compared to restoring from a backup, where the backup will remain in its present state after use, allowing you attempts to restore from multiple backups to find the best one. Use the revert feature carefully.

  * All data written after the creation of the target snapshot is deleted at the beginning of the revert process and cannot be recovered. All snapshots that are newer than the target snapshot are also deleted. For example, `snapshot1`, `snapshot2`, and `snapshot3` are created sequentially. Reverting the instance to the state captured in `snapshot2` means that all data written after `snapshot2`, as well as all snapshots taken after the creation of `snapshot2`, are deleted in the revert process.

Cleanup of this deleted data can take between six hours to ten days. Instance capacity and performance may be impacted during this time.

  * Reverting an instance to a snapshot state updates the NFS file system ID (fsid). Attempts to access clients using existing mounts will return stale file handle errors. As a best practice, unmount all clients from the instance prior to the revert operation, and remount them after it is complete.

  * A revert operation can take up to two minutes to complete.

    * Any related cleanup associated with the revert operation, such as deleting subsequent snapshots in the chain, can take between six hours to ten days to complete, depending on the number of files involved.
    * You can run other operations while the revert operation is running and while cleanup is completing.
    * You must wait for the revert operation to complete before starting another revert operation.
  * Snapshots and their related `revert` operations are available for most service tiers. Snapshots aren't available in the basic SSD and basic HDD service tiers.

  * Only instances with a single share can revert to a snapshot state.

  * While snapshots are supported in the enterprise service tier, they can't be combined with the [Filestore multishares](https://docs.cloud.google.com/filestore/docs/multishares) feature.




## What's next

  * Learn how to [create and manage snapshots](https://docs.cloud.google.com/filestore/docs/create-snapshots).
  * Learn about [backups](https://docs.cloud.google.com/filestore/docs/backups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
