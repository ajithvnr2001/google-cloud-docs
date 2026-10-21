---
url: https://docs.cloud.google.com/pubsub/docs/cloud-storage-import-topic-troubleshooting/
title: Troubleshooting a Cloud Storage import topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:11.542083+00:00
---

# Troubleshooting a Cloud Storage import topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/cloud-storage-import-topic-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting a Cloud Storage import topic Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some common troubleshooting tips for Cloud Storage import topics.

After you configure the import topic and start ingesting messages, you can check the relevant Cloud Monitoring metrics to see if data is ingested. Perform the following steps:

  1. In the console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the Cloud Storage import topic that you want to troubleshoot.

  3. In the topic details page, click the **Metrics** tab.

  4. Check the chart for the metric **Ingestion byte count**.

  5. If no data is being ingested, in the topic details page, check to see if there is an error and a red exclamation mark for the **Topic state** field.

  6. You can also check the metric **Ingestion data source state**. To do so, in the topic details page, click the **Metrics** tab.

For more information about these metrics, see [Metrics to monitor import topics](https://docs.cloud.google.com/pubsub/docs/monitor-topic#metrics-monitor-topic).

  7. Here is a list of errors that you might encounter:

Error Code | Description | Fix  
---|---|---  
`CLOUD_STORAGE_PERMISSION_DENIED` | Error consuming Cloud Storage data due to permission issues. | Verify that the Pub/Sub service account has the necessary permissions to access the Cloud Storage bucket. Ensure the service account has the following permissions:
     * `storage.objects.list`: To list the objects in a bucket.
     * `storage.objects.get`: To read the objects in a bucket. 
     * `storage.buckets.get`: To obtain the bucket location and that the bucket exists.
For more information, see [the prerequisites to creating a Cloud Storage topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#before_you_begin).  
`PUBLISH_PERMISSION_DENIED` | Error publishing to the topic due to permission issues. |  Grant the Pub/Sub service account the [necessary publish permissions](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher). For more information, see [Add the Pub/Sub publisher role to the Pub/Sub service account.](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#add-publisher-role)  
`BUCKET_NOT_FOUND` | The specified Cloud Storage bucket cannot be found. | Verify the bucket name for accuracy.  
`TOO_MANY_OBJECTS` | The Cloud Storage bucket has too many objects, ingestion is paused. Ingestion is resumed after the number of objects in the bucket is fewer than 50 million. | The limit for the objects is 50 million. Reduce the number of objects in the bucket or contact Google Cloud support for assistance.  



If there are no errors until this point, check the best practices in [Maintain a healthy publisher](https://docs.cloud.google.com/pubsub/docs/monitoring#keeping_publishers_healthy).

You can also enable [platform logs](https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub) for a Cloud Storage import topic. These logs help you troubleshoot issues when you have issues ingesting objects into Pub/Sub import topics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
