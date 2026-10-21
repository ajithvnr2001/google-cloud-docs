---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images/
title: Mount images in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:02.847624+00:00
---

# Mount images in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount images in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Once an application or VM is captured in the appliance management console, its data can be mounted.

A mount operation can be performed for local images or remote images.

The appliance management console supports two types of mounts:

  * **Standard Mounts** : Standard mounts let you mount just the data captured from an application. The mounted data can then be used by its associated application type. A mounted image can be used directly from the mounted host, or you can restore selected files or directories from it. The original image is never modified, even if the mounted image is modified or deleted.
  * **Application Aware Mounts** : This lets you mount captured databases as virtual applications. It lets you quickly access a database without having to import mounted data to the application. Consistency groups that contain databases can be mounted together in an application aware mount. Application aware mounts allow you to address the unique challenges associated with creating and managing copies of production databases for non-production use. Application aware mounts are performed from the backup/recovery appliance and don't require manual intervention by database, server, or storage administrators. Application aware mounts can be used for such things as database reporting, analytics, integrity testing, and test and development.



Each backup/recovery appliance lets you mount one or more active images from:

  * A VM to the same VM, to another VM, or to any other host. The mounted image is displayed as a new drive on the mounted VM or host.
  * An application to the same host, to another host, or to a VM.



A backup/recovery appliance mounts images transparently to a host or VM and does not require additional zoning (if that was done originally) or shutdown and restart of the host. Multiple active images can be mounted to the same host or VM. Any mounted image can be unmounted individually or unmounted and deleted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
