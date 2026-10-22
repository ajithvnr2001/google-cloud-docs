---
url: https://docs.cloud.google.com/filestore/docs/capacity-issues/
title: Troubleshoot capacity issues \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:40.227492+00:00
---

# Troubleshoot capacity issues  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/capacity-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot capacity issues Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe scenarios where an instance might encounter capacity issues and provides steps to help address the problem.

## "No space left on device"

Check if the Filestore instance has sufficient inodes by running the following command on the client VM:
    
    
    df -i
    

The command returns something similar to the following:
    
    
    Filesystem           Inodes        IUsed      IFree         IUse%  Mounted on
    10.0.0.2:/vol1    134217728        13         134217715     1%     /mnt/test
    

Each file stored on the file share consumes one inode. If `IUse%` reaches 100%, you are not able to store more files on the file share even if you haven't reached the maximum allocated capacity. The number of inodes scales with capacity. If you want to add more inodes, you must add more capacity. However, reaching the maximum number of inodes is rare and is only a concern if you need to store numerous small files.

For more information, see [Inode usage](https://docs.cloud.google.com/filestore/docs/scale#inode-usage) and [Monitoring instances](https://docs.cloud.google.com/filestore/docs/monitoring-instances#anticipating-capacity).

## `df` and `du` commands report different amounts of free disk space

When a file that is open by a running process is deleted, the disk space that the file consumes does not get freed until the file is closed. The `df` commands accounts for the space consumed by deleted open files, whereas the `du` command does not. This difference in calculation is why the `du` command often shows more free space than `df`.

To display the deleted files that are still open by a running process, run:
    
    
    lsof | grep deleted
    

## Number of client connections

You can control the number of client connections with IOPS rather than provisioned instance capacity by using [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance).

For more information, see [Client connection limits](https://docs.cloud.google.com/filestore/docs/limits#number_of_clients).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
