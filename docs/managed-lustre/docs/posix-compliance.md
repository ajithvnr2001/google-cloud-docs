---
url: https://docs.cloud.google.com/managed-lustre/docs/posix-compliance/
title: POSIX compliance \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:26.988019+00:00
---

# POSIX compliance  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/posix-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  POSIX compliance Stay organized with collections  Save and categorize content based on your preferences. 

The following are exceptions to Google Cloud Managed Lustre's POSIX compliance:

  * **`atime` updates**: By default, `atime` is enabled in Lustre, but for performance reasons, its updates might be deferred. This means that the access time of a file might not be updated immediately after every read operation.

  * **`flock`/`lockf`**: These refer to two main file-locking APIs: `flock(2)` and `fcntl(2)`.

    * **`flock`** : This is a BSD-style, whole-file advisory lock that is not defined by POSIX. Lustre fully supports BSD-style `flock` semantics across the cluster by default.
    * **`fcntl`** : This is the POSIX-defined locking API, supporting byte-range locks. Lustre's implementation of `fcntl` locks is nearly POSIX-compliant and works as expected for most applications. However, since `fcntl` was originally designed for local filesystems, no distributed file system can 100% match all of POSIX's `fcntl` requirements, including Lustre. For example, `fcntl()` specifies that locks must be released immediately when the owning process exits, but Lustre lock release may be delayed if the client crashes.



See the [Lustre FAQ](https://wiki.lustre.org/Frequently_Asked_Questions#Is_Lustre_%22POSIX_compliant%22?_Are_there_any_exceptions?) for details.

## Inode number changes due to metadata migration

A file's inode number in a Lustre file system is not an immutable identifier.

A metadata rebalancing operation, such as one initiated by `lfs migrate`, involves migrating some files' metadata from one MDT to another. As a direct consequence of this migration to a new MDT, those files are assigned a new inode number.

While this behavior is compliant with the POSIX standard, it can violate the assumptions of many common Unix/Linux applications and services that are built to expect a persistent inode number for the lifetime of a file. This includes, but is not limited to:

  * NFS and SMB frontends: These services often derive file handles from inode numbers. A change can lead to `Stale file handle` errors for clients.

  * Archiving and backup utilities: Tools like `tar` that track files by their device + inode number may treat a migrated file as a new file, leading to inefficient incremental backups.

  * Log aggregators, intrusion detection systems, and custom applications using `stat()` and storing `st_ino` may also be affected.




Administrators should be aware of this behavior and its potential impact on applications before initiating any manual metadata rebalancing.

### Mitigation strategies

Metadata rebalancing should be treated as a planned, disruptive maintenance event.

  1. Schedule a maintenance window. Communicate a planned outage to all users and application owners. If possible, don't perform large-scale `lfs migrate` operations on a live production system.

  2. If required, unmount and remount the file system after the migration.

  3. Some applications may need to be flushed or restarted after a migration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
