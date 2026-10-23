---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/network-attached-storage/
title: Network-attached storage \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:43.990216+00:00
---

# Network-attached storage  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/network-attached-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Network-attached storage Stay organized with collections  Save and categorize content based on your preferences. 

NetApp Volumes shares file systems, or volumes, to network-attached storage (NAS) clients. NAS clients are usually virtual machines (VMs) that run on Windows or Linux operating systems, using the industry-standard [Network File System (NFS)](https://en.wikipedia.org/wiki/Network_File_System) and [Server Message Block (SMB)](https://en.wikipedia.org/wiki/Server_Message_Block) protocols.

Both NFS and SMB use a client-server model, in which a client sends requests to a server to act on the file system. Such actions include operations like creating or deleting files or folders, modifying files, and browsing and reading files.

Volumes can be shared between many clients. Windows, Linux, and UNIX operating systems include built-in SMB and NFS client software.

All file system objects must have an owner, but you can grant other users and groups access permissions for objects.

For NFS, ownership is specified by user ID (UID) and group IDs (GIDs), which use standard [UNIX-style user and group permissions](https://en.wikipedia.org/wiki/File-system_permissions#Permissions). [NFSv4](https://www.rfc-editor.org/rfc/rfc8881) can use UID and GIDs or security principals. When you use NFSv4.1 with Kerberos, UID access gets replaced by the usage of Kerberos principals, which are authenticated user identities. In addition to standard UNIX permissions, NFSv4 also offers [NFSv4 ACLs](https://linux.die.net/man/5/nfs4_acl) as an alternative method of managing access.

For SMB, ownership is specified by Windows [security identifiers (SIDs)](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers). Access to objects is managed by NTFS-style access control lists (ACLs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
