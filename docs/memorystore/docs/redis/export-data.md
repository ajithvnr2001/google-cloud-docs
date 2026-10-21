---
url: https://docs.cloud.google.com/memorystore/docs/redis/export-data/
title: Export data from a Redis instance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:54.512316+00:00
---

# Export data from a Redis instance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/export-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Export data from a Redis instance Stay organized with collections  Save and categorize content based on your preferences. 

Follow the instructions on this page to export an RDB backup of your Memorystore for Redis instance.

Exporting your Redis instance creates an RDB backup file of your data. The export operation stores the RDB backup in a Cloud Storage bucket. Your instance's performance may be temporarily slower for the duration of the export.

## Before you begin

  1. Have a Cloud Storage bucket. We recommend that you export to a bucket located in the same region as your Redis instance.

To create a Cloud Storage bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-cli).

  2. Have [sufficient permissions](https://docs.cloud.google.com/memorystore/docs/redis/import-export-restricted-permissions) to perform the export.




## Export an RDB backup file to a Cloud Storage bucket

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click your instance ID to view the instance details page.

  3. Click the **Export** button in the top bar.

  4. Click the **Browse** button and navigate to the Cloud Storage bucket to which you want to export your RDB file.

  5. Use the default export file name, or enter your own file name that includes the`.rdb` file extension. For example:

`myexport.rdb`

  6. Click the **Select** button.

  7. Click the **Export** button.

  8. Confirm that you want to export, and click the **Export** button.




### Gcloud

  1. Export an RDB file to the Cloud Storage bucket referred to in step one of [Before you begin](https://docs.cloud.google.com/memorystore/docs/redis/import-data#before_you_begin) by executing the following command: 
         
         gcloud redis instances export gs://[BUCKET_NAME]/[FILE_NAME].rdb [INSTANCE_ID] --region=[REGION] --project=[PROJECT_ID]
         




## Stop an ongoing export operation

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the Instance ID to view its information.

  3. Click the **Stop export** button.




### Gcloud

To stop an export operation, first you need to find the operation ID by running the following command:
    
    
    gcloud redis operations list --region=[REGION] -project=[PROJECT]

Once you have the operation ID, run the following command:
    
    
    gcloud redis operations cancel [OPERATION_ID] --region=[REGION] --project=[PROJECT]

## Instance availability and behavior while exporting

  * During the export process you can read and write to your Redis instance, however you cannot run admin operations on your instance such as scaling or upgrading.

  * Your instance may experience increased latency during the export operation.

  * The export can take anywhere from a few minutes to a few hours. For example, if you export a 10 GB instance with 8 GB of used memory, the export can take 5 minutes, and if you export a 120 GB instance with 100 GB of used memory, the export can take an hour. To monitor the progress of the export, check the instance details page, which displays the status of the operation.




## What's next

  * Learn about import and export feature behavior and best practices with [Import and export overview](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
