---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/known-limitations/
title: Known limitations \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:06.839831+00:00
---

# Known limitations  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page documents known limitations of Transfer Appliance. If you anticipate ordering many appliances for a large transfer and cannot follow the limitations listed below, you must perform an initial proof-of-concept transfer with a single Transfer Appliance and representative data to ensure performance is suitable before you order multiple appliances.

## Single file share protocol support

Each Transfer Appliance can be configured to use a single file sharing protocol at a time. You cannot run multiple protocols concurrently or switch between them once the appliance is configured. Attempting to change the configured file sharing protocol after data transfer has begun requires resetting the appliance, which will erase any data already transferred to it. If you need to transfer data using multiple file sharing protocols, such as NFS and SMB, order separate appliances.

## Maximum file size

Cloud Storage supports a maximum single-object size of [5 tebibytes](https://docs.cloud.google.com/storage/quotas#objects). Transfers from Transfer Appliance to Cloud Storage fail for objects larger than 5 TiB.

## Maximum files per directory

Cloud Storage supports a maximum of 500,000 files or directories in a single directory to avoid poor ingest performance.

## Maximum path length

The [maximum object name length](https://docs.cloud.google.com/storage/quotas#objects) for data copied to Cloud Storage is 1024 bytes. The object prefix for the destination object is included in the length limitation because the object prefix is incorporated in the object's name in Cloud Storage.

## Minimum file size

The minimum file size for files copied onto the appliance is 1MB. To copy many smaller files, we recommend that you archive the files before copying them.

## Supported file metadata

Transfer Appliance preserves symlinks, numeric MODE and the last modified time (`mtime`) from Transfer Appliance file system to copy into the corresponding Cloud Storage destination object. Other file metadata are not preserved in the transfer.

## Supported file names

File names should be Unicode-compatible and not contain newlines. If your source directory contains file names with newlines, the copy from the appliance to Cloud Storage for that directory fails.

We strongly recommend that you replace newlines in your file names before copying data to Transfer Appliance.

For more information, see Cloud Storage's requirements for [object naming](https://docs.cloud.google.com/storage/docs/objects#naming).

## Supported file types

Transfer Appliance supports transferring regular files. Non-regular files, such as devices, named pipes, or sockets are not supported.

Transfer Appliance does not create empty directories in Cloud Storage when we transfer from the appliance to your Cloud Storage bucket, because objects don't reside within subdirectories within a bucket. For more information, see [Object namespace](https://docs.cloud.google.com/storage/docs/objects#namespace).

## Object Versioning

Using Transfer Appliance with a bucket where object versioning is enabled may result in multiple versions of the same object being created and storage costs associated with these versions. We recommend that you disable object versioning for the bucket you specified as the destination at the time of ordering your Transfer Appliance.

To learn more, see [Object versioning](https://docs.cloud.google.com/storage/docs/object-versioning). Follow [these instructions](https://docs.cloud.google.com/storage/docs/using-object-versioning#set) to disable object versioning for your bucket.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
