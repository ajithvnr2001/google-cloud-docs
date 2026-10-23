---
url: https://docs.cloud.google.com/storage-transfer/docs/data-integrity/
title: Data integrity \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:37.779084+00:00
---

# Data integrity  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/data-integrity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Data integrity Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service uses metadata available from the source storage system, such as checksums and file sizes, to ensure that data written to Cloud Storage is the same data read from the source.

## When checksum metadata is available

If checksum metadata is available on the source, Storage Transfer Service uses end-to-end checksum validation. If the checksum metadata on the source storage system indicates that the data Storage Transfer Service received doesn't match the source data, Storage Transfer Service records a failure for the transfer operation. Examples of storage systems that include checksum metadata include most Amazon Simple Storage Service (Amazon S3) and Microsoft Azure Blob Storage objects (with some exceptions) and HTTP transfers (checksum metadata are provided by the user).

## When checksum metadata is unavailable

### When agents can run near the source

If checksum metadata isn't available from the underlying source storage system but [agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) can be run locally near the source storage system, Storage Transfer Service attempts to read the source data and compute a checksum before sending the data to Cloud Storage. This occurs when moving data from file systems to Cloud Storage.

### When agents can't run near the source

If checksum metadata isn't available from the underlying source storage system, and agents can't be run locally near the source storage system, Storage Transfer Service uses available metadata, such as file size, to validate that the file copied to Cloud Storage matches the source file.

Storage Transfer Service also computes a checksum of the data "on-the-fly" as it's being transferred. Once the data is stored in Cloud Storage, Storage Transfer Service compares the checksum it computed against the final checksum reported by Cloud Storage. If the checksums don't match, the task fails with a `DATA_LOSS` error.

On-the-fly checksumming is used for transfers from sources that may not provide checksums, such as:

  * [Amazon S3 multi-part objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html)

  * [Amazon S3 objects stored with server-side encryption with keys stored in AWS Key Management Service (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html)

  * [Microsoft Azure Blob Storage Put Block List](https://docs.microsoft.com/en-us/rest/api/storageservices/put-block-list)




## After transfer checks

After your transfer is complete, we recommend performing additional data integrity checks to validate that:

  * The correct version of the files are copied, for files that change at the source.
  * The correct set and number of files are copied, to verify that you've set up the transfer jobs correctly.
  * The files were copied correctly, by verifying the metadata on the files, such as file checksums, file size, and so forth.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
