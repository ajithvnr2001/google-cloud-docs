---
url: https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class/
title: Filter source objects by storage class \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:59.817880+00:00
---

# Filter source objects by storage class  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Filter source objects by storage class Stay organized with collections  Save and categorize content based on your preferences. 

For transfers from Amazon S3, you can filter objects by their storage class.

By default, when transferring from Amazon S3:

  * Objects in standard and non-archival storage classes, including Glacier Instant Retrieval (`GLACIER_IR`), are transferred.
  * Objects in Glacier Deep Archive (`DEEP_ARCHIVE`) are transferred only if they are restored.
  * Objects in Glacier Flexible Retrieval (`GLACIER`) are skipped regardless of restore status.



## Specify a storage class list

To specify the storage classes to include:

###  Google Cloud console 

Follow the instructions in [Transfer from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#create_a_transfer).

After you've specified the source and destination for the transfer, select **Filter by storage class** and select the storage classes to include.

###  gcloud CLI 

This feature is not supported in gcloud CLI.

###  REST 

Use the `transferSpec.objectConditions.includeStorageClasses` option to specify the storage classes to include.

For example, to transfer only `STANDARD` and `GLACIER` storage classes:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
      "description": "DESCRIPTION",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
          "awsS3DataSource": {
              "bucketName": "AWS_SOURCE_NAME",
              "awsAccessKey": {
                "accessKeyId": "AWS_ACCESS_KEY_ID",
                "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
              }
          },
          "gcsDataSink": {
              "bucketName": "GCS_SINK_NAME"
          },
          "objectConditions": {
              "includeStorageClasses": ["STANDARD", "GLACIER"]
          }
      }
    }

When `includeStorageClasses` is specified and is not blank, only objects belonging to the specified storage classes are transferred.

For transfers from Amazon S3, valid values are listed in the AWS documentation: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/sc-howtoset.html>.

## Archived objects

Objects in S3 Glacier Deep Archive (`DEEP_ARCHIVE`) and S3 Glacier Flexible Retrieval (`GLACIER`) must be restored before they can be transferred.

Storage Transfer Service provides [counters](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters) to track archived objects that were skipped during the transfer process:

  * **`unrestoredDeepArchiveObjectsSkippedCount`** : The number of Glacier Deep Archive (`DEEP_ARCHIVE`) objects that were skipped because they were not restored.
  * **`unsupportedS3GlacierObjectsSkippedCount`** : The number of Glacier Flexible Retrieval (`GLACIER`) objects skipped because they were not restored, or because `GLACIER` was not specified as an included storage type.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
