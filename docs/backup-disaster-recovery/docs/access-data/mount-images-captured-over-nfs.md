---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images-captured-over-nfs/
title: Use NFS in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:13.729866+00:00
---

# Use NFS in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images-captured-over-nfs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Use NFS in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

You can use the NFS protocol to present a staging disk to a server for data capture in the appliance management console. NFS protocol can also be used to present virtual clones of point-in-time captured images.

Whether an application is captured to an NFS staging disk is determined when the application host is added, see [Manage hosts and their connected applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications) for details. If a host is set to NFS, then all applications on that host is captured to an NFS staging disk.

The required open bidirectional TCP/UDP ports to utilize NFS transport are:

TCP/UDP Port Number | Description  
---|---  
111 | portmapper/rpcbind  
756 | status/statd  
4001 | mounted  
2049 | nfs/nfsd  
4045 | nlockmgr/lockd  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
