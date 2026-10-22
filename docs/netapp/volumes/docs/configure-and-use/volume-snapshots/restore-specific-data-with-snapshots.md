---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/restore-specific-data-with-snapshots/
title: Restore specific data with snapshots \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:46.641778+00:00
---

# Restore specific data with snapshots  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/restore-specific-data-with-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Restore specific data with snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details about restoring specific data you select from a snapshot.

## About snapshot-based data restoration

You can use snapshots to restore deleted or corrupted files and directories using file access operations based on your operating system.

## Restore data using a Linux client

Snapshots are accessible using the UNIX-like file system on Linux operating systems. To restore data using a Linux client, enable the **Make snapshot directory visible** option in the volume snapshot schedule section. A `.snapshot` directory appears in the mount point of the volumes.

### Example of data restoration on a Linux client

The following example shows a sequence of file operations on a volume mounted to a Linux client. The volume contains two files and one snapshot. In this example, the user deletes a file and uses the snapshot to restore the latest version of the file from the newest snapshot:
    
    
        $ df -h .
    
        Filesystem                      Size  Used  Avail Use%  Mounted on
        10.31.240.4:/example-volume-1   1.0T  4.5M  1.0T    1%  /netapp
    
        $ ls
    
        chinook.db  readme.txt
    
        $ rm chinook.db
    
        $ ls -la .
    
        total 12
        drwxrwxrwx  2 root    root    4096 May 31 15:02 .
        drwxr-xr-x 20 root    root    4096 May 31 13:42 ..
        drwxrwxrwx  3 root    root    4096 May 31 14:35 .snapshot
        -rw-rw-r--  1 ubuntu  ubuntu    14 May 31 14:24 readme.txt
    
        $ ls .snapshot
    
        hourly.2022-05-31_1435
    
        $ ls .snapshot/hourly.2022-05-31_1435
    
        chinook.db  readme.txt
    
        $ cp .snapshot/hourly.2022-05-31_1435/chinook.db .
    
        $ ls
    
        chinook.db  readme.txt
    

## Restore data using a Windows client

To restore data using a Windows client, enable the **Make snapshot directory visible** option in the volume snapshot schedule section. You can then access snapshots using the **Previous Versions** tab of the File Explorer property window. To restore a file, drag it from a snapshot folder to its original location.

### Example of data restoration on a Windows client

The following example shows you how to access snapshots using the `~snapshot` file path:
    
    
        Z:\dir z:\~snapshot
        Volume in drive Z is restore-example-1
        Volume Serial Number is 8080-F15D
    
        Directory of z:\~snapshot
    
        05/31/2022  04:08 PM    <DIR>        ..
        05/31/2022  03:59 PM    <DIR>        hourly.2022-05-31-1600
        05/31/2022  04:02 PM    <DIR>        hourly.2022-05-31_1605
                      0 File(s)            0 bytes
                      3 Dir(s)             0 bytes free
    
        Z:\>
    

## What's next

[About backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
