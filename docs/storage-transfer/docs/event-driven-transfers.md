---
url: https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers/
title: Event-driven transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:30.072877+00:00
---

# Event-driven transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Event-driven transfers Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can listen to event notifications in AWS, Azure, or Google Cloud to automatically transfer data that has been added or updated in the source location. Event-driven transfers are supported from AWS S3, Azure, or Cloud Storage, and always use a Cloud Storage bucket as the destination.

Event-driven transfers listen to:

  * Amazon S3 Event Notifications sent to Amazon SQS for AWS S3 sources.
  * Azure Storage Queues for Azure sources.
  * Pub/Sub subscriptions for Cloud Storage sources.



Object deletions are not detected; deleting an object at the source does not delete the associated object in the destination bucket.

## Benefits of event-driven transfers

Because event-driven transfers listen for changes to the source bucket, updates are copied to the destination in near-real time. Storage Transfer Service doesn't need to execute a list operation against the source, saving time and money.

Use cases include:

  * **Event-driven analytics** : Replicate data from AWS or Azure to Cloud Storage to perform analytics and processing.

  * **Cloud Storage replication** : Enable automatic, asynchronous object replication between Cloud Storage buckets.

Event-driven transfers with Storage Transfer Service differ from [typical Cloud Storage replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy) by creating a copy of your data in a different bucket.

This provides benefits such as:

    * Keeping development and production data in separate namespaces.
    * Sharing data without providing access to the original bucket.
    * Backing up to a different continent, or to an area not covered by dual-region and multi-region storage.
  * **DR/HA setup** : Replicate objects from source to backup destination in order of minutes:

    * Cross-cloud backup: Create a copy of an AWS S3 or Azure backup on Cloud Storage.
    * Cross-region or cross-project backup: Create a copy of Cloud Storage bucket in a different region or project.
  * **Live migration** : Event-driven transfer can power low-downtime migration, on the order of minutes of downtime, as a follow up step to one-time batch migration.




## Learn how

  * [Set up event-driven transfers from Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/event-driven-google)
  * [Set up event-driven transfers from AWS S3](https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws)
  * [Set up event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2](https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
