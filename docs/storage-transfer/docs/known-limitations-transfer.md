---
url: https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer/
title: Known Limitations \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:43.149023+00:00
---

# Known Limitations  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Support ](https://docs.cloud.google.com/storage-transfer/docs/support)



Send feedback 

#  Known Limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page documents known limitations of Cloud Storage and Storage Transfer Service.

## Common limitations

### Cloud Storage 5TiB object size limit

Cloud Storage supports a maximum single-object size up [5 tebibytes](https://docs.cloud.google.com/storage/quotas#objects). If you have objects larger than 5TiB, the object transfer fails for those objects for either Cloud Storage or Storage Transfer Service.

### Cloud Storage object naming requirements

Cloud Storage imposes [object name requirements](https://docs.cloud.google.com/storage/docs/objects#naming) that apply to all Storage Transfer Service transfers.

### Changed objects aren't transferred

Storage Transfer Service does not lock source files during a transfer.

If an object's data is updated during a transfer, the following describes how Storage Transfer Service responds:

  * **Transfers from non-Google clouds to Google Cloud** : If an object's data is updated during a transfer, Storage Transfer Service fails the transfer for that particular object and the object isn't transferred.

  * **Transfers from file systems to Google Cloud** : If an object's data is updated during a transfer, Storage Transfer Service attempts the upload again. If the upload fails multiple times, Storage Transfer Service logs a `FILE_MODIFIED_FAILURE`. For more information, see [Troubleshooting](https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem).

  * **Transfers from Google Cloud to a file system** : If an object's data is updated during a transfer, Storage Transfer Service attempts the download again. If the download fails multiple times, Storage Transfer Service logs a `PRECONDITION_FAILURE`. For more information, see [Troubleshooting](https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem).




To resolve the failure:

  1. Attempt the transfer again.
  2. If the object's transfer continues to fail, ensure that its data cannot be updated during transfer:

     * **Cloud Storage source** \- [Place an object hold](https://docs.cloud.google.com/storage/docs/holding-objects#set-object-hold).
     * **Amazon S3 source** \- [Set an S3 Object lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html).
     * **Microsoft Azure Storage source** \- [Set an immutability policy for Blob storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-immutability-policies-manage).
     * **File-system source** \- Set the files in read-only mode or otherwise limit writes to files being transferred.
  3. After the transfer completes, you can re-enable updates to the object.




### Folders in Cloud Storage

Cloud Storage objects reside within a flat namespace within a bucket. For more information, see [Object namespace](https://docs.cloud.google.com/storage/docs/objects#namespace). Due to this, Storage Transfer Service doesn't create hierarchical namespaces within Cloud Storage. For instance, if you're transferring from Azure Data Lake Storage (ADLS) Gen 2, then Storage Transfer Service does not recreate the ADLS Gen 2 namespaces in Cloud Storage.

### Deleting objects in versioning-suspended Amazon S3 buckets

When using Storage Transfer Service's delete objects from source after transfer feature on a version-suspended Amazon S3 bucket, Storage Transfer Service removes the object with a null version ID, not the current version.

### Location of Storage Transfer Service jobs

Storage Transfer Service chooses its location based on the region of the source Cloud Storage bucket. As of today, we create Storage Transfer Service jobs in the following locations. This list may change as Storage Transfer Service adds support for new regions.

If your source Cloud Storage bucket is located in a region that isn't listed, we'll choose the default region within the source's outer region.

Supported locations |  |   
---|---|---  
africa-south1 | europe-north1 | nam4  
asia-east1 | europe-north2 | northamerica-northeast1  
asia-east2 | europe-southwest1 | northamerica-northeast2  
asia-northeast1 | europe-west1 | northamerica-south1  
asia-northeast2 | europe-west2 | southamerica-east1  
asia-northeast3 | europe-west3 | southamerica-west1  
asia-south1 | europe-west4 | us-central1  
asia-south2 | europe-west6 | us-central2  
asia-southeast1 | europe-west8 | us-east1  
asia-southeast2 | europe-west9 | us-east4  
asia-southeast3 | europe-west10 | us-east5  
asia1 | europe-west12 | us-east7  
australia-southeast1 | me-central1 | us-west1  
australia-southeast2 | me-central2 | us-west2  
| me-west1 | us-west3  
|  | us-west4  
  
## Known limitations of file system transfers

### No real-time support

Storage Transfer Service does not support sub-hourly change detection. Storage Transfer Service is a batch data movement service that can scan the source with a frequency of up to once an hour.

### Supported operating system configurations

Transfer agents require Docker installed, and run on Linux servers or virtual machines (VMs). To copy data on a CIFS or SMB file system, you can [mount the volume on a Linux server or VM](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#cifs-volumes) and then run the agent from the Linux server or VM.

### Memory requirements

The following are memory requirements for Transfer service for on-premises data agents: 

  * Minimum memory: 1GiB
  * Minimum memory to support high-performance uploads: 6GiB



### Scaling limitations

Storage Transfer Service supports individual transfers that are:

  * Hundreds of terabytes in size
  * Up to 1 billion files
  * Several 10s of Gbps in transfer speed



Individual transfers greater than these sizes are reliable, but have not been tested for performance.

If you have a larger data set than these limits, we recommend that you split your data across multiple transfer jobs.

We currently support large directories, as long as every agent has at least 1GB of memory available for every 1 million files in the largest directory, so we can iterate over the directory contents without exceeding memory.

### Agent and agent pool limitations

We support up to 100 agents for a single agent pool. It is unlikely that you'll need more agents to achieve better performance given typical environments.

Up to 800 agent pools are supported per project.

### Single directory per job

We support transferring only the full contents of a file system directory (recursively). You may partition the transfer by creating multiple jobs that transfer different subdirectories of your dataset, but we currently do not support file globbing or filtering support within a single job.

### Supported file names

The following rules apply to all file names that are part of a transfer:

  * File names must use UTF8 encoding.
  * File names must be unicode-compatible.
  * They must not contain newlines (`\n`) or carriage returns (`\r`).



If your source directory contains unsupported file names, the file listing task for that directory fails.

If this occurs, update any unsupported file names and re-run the job.

### Supported file types

Storage Transfer Service supports transferring regular files and Unix-like hidden files. Unix-style hidden files are files that start with a `.` character. When Storage Transfer Service encounters a non-regular file, such as a device, named pipe, or socket, it raises an [`UNSUPPORTED_FILE_MODE`](https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem) error.

Empty directories are not created in Cloud Storage, because objects don't reside within subdirectories within a bucket. For more information, see [Object namespace](https://docs.cloud.google.com/storage/docs/objects#namespace).

### Maximum path length

Storage Transfer Service follows Cloud Storage's maximum path length of 1024 bytes. The object prefix for the destination object is included in the length limitation, as the prefix is incorporated in the object's name in Cloud Storage.

### Supported file metadata

See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details on which metadata is preserved, either by default or optionally.

### Extended job pauses

Jobs that are paused for more than 30 days are considered inactive. When a job is inactive, the paused job is aborted and the job configuration schedule is disabled. No new job runs start unless you explicitly enable the job again.

## File system source security

### Agent access

Users able to create transfer jobs can retrieve data from, and download data to, any file system directory that is accessible by the agent. If agents are run as root and are given access to the entire file system, a malicious actor may be able to take over the host. It is strongly recommended that you [restrict agent access](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access) to only necessary directories.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
