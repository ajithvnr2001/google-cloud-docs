---
url: https://docs.cloud.google.com/filestore/docs/troubleshooting/
title: Troubleshoot slow performance \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:56.146583+00:00
---

# Troubleshoot slow performance  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot slow performance Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address slow performance issues you might encounter while using Filestore.

## Slow read or write performance

  1. Ensure that you are using the [recommended machine type](https://docs.cloud.google.com/filestore/docs/performance#client-machine) for the client VM.

  2. If your client VM is running Linux, confirm that you're using the [default mount options](https://docs.cloud.google.com/filestore/docs/performance#linux_client_mount_options).

**Note:** Using the `sync` client mount option significantly reduces performance.
  3. Ensure that the client VM is located in the same region as the Filestore instance. Mounting across regions not only reduces performance, it also incurs a [networking cost](https://cloud.google.com/vpc/network-pricing).

  4. Ensure that your Filestore instance isn't at or near full capacity. When capacity is nearly full, any remaining space is highly fragmented, causing read and write operations to slow down. The amount of free space needed to avoid this scenario is case-dependent. We recommend setting up [low disk space alerts](https://docs.cloud.google.com/filestore/docs/monitoring-instances#low-disk-space).

For more information, see [Troubleshoot capacity issues](https://docs.cloud.google.com/filestore/docs/capacity-issues).

  5. [Test the performance](https://docs.cloud.google.com/filestore/docs/performance#testing_performance) of your Filestore instance using the `fio` tool.

If the test results show abnormally slow performance, contact your account representative. If the test results show similar or greater performance than expected, continue to the next section.




## Use cases that cause slow performance

Here are some use cases and scenarios that cause poor performance:

### Workloads involving high volumes of small files

  * Filestore file shares use the `sync` export option for data safety and NFS protocol compliance. For most data-modifying operations, the Filestore instance waits for the data to be committed to storage before replying to requests from the client VM. When many files are involved in an operation, the client makes a long series of synchronous operations and the cumulative latency adds up.

An example of this scenario is when you extract an archive on the file share, like tar files. TAR makes many synchronous operations in a series when extracting an archive containing many files. As a result, performance is reduced.

If you're trying to copy many small files to a file share, try parallelizing file creation with a tool like the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync):
        
        mkdir -p /mnt/nfs/many_files_rsync/
        time gcloud storage rsync many_files /mnt/nfs/many_files_rsync/ --recursive
        

  * Each file stored on the file share consumes one inode. If the file system runs out of inodes, you won't be able to store more files on the file share even if you haven't reached the maximum allocated capacity. However, reaching the maximum number of inodes is rare and is only a concern if you need to store numerous small files.

For more information, see [Inode usage](https://docs.cloud.google.com/filestore/docs/scale#inode-usage).




### Copying data between Cloud Storage and Filestore

Copying data from Cloud Storage to a Filestore instance using the gcloud CLI is known to be slow. For detailed information on how to improve performance, see [Improve performance across Google Cloud resources](https://docs.cloud.google.com/filestore/docs/performance#across-resources).

## What's next

  * [Troubleshoot capacity issues](https://docs.cloud.google.com/filestore/docs/capacity-issues)
  * [Improve performance across Google Cloud resources](https://docs.cloud.google.com/filestore/docs/performance#across-resources).
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
