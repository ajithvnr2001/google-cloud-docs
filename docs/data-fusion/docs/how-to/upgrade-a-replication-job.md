---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-a-replication-job/
title: Upgrade a Replication job \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:42.469479+00:00
---

# Upgrade a Replication job  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-a-replication-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Upgrade a Replication job Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upgrade a replication job after [upgrading a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#upgrade-instances). The process differs when you upgrade to version 6.6.0 and earlier.

### Version 6.7.0 and later

To upgrade a replication job to version 6.7.0 or later, perform the replication job upgrade using the same steps as you would to [upgrade batch pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#upgrade-batch-pipelines).

### Version 6.6.0 and earlier

To back up and upgrade the replication job to version 6.6.0 or earlier, follow these steps:

  1. [Stop the replication job](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref#stop-a-replication-job).

  2. Get the generation ID by making an HTTP `GET()` request in the Cloud Data Fusion web interface or REST API. The path is similar to the following:
         
         namespaces/NAMESPACE_ID/apps/REPLICATION_JOB_ID</workers/DeltaWorker
         

Replace the following:

     * `NAMESPACE_ID`: the string name of the namespace for the replication job. If your pipeline belongs to a Basic edition instance, the ID is always `default`.

     * `REPLICATION_JOB_ID`: the string name of the replication job.

### Interface

To make the HTTP `GET()` request in the Cloud Data Fusion interface, follow these steps:

     1. Go to your instance: 
        1. In the Google Cloud console, go to the Cloud Data Fusion page.

        2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

     2. Click **System Admin** > **Configuration**.
     3. Click **Make HTTP calls**.
     4. Select **GET** and enter the path described previously in step 2.
     5. Click **Send** and find generation ID in the call response.

### REST API

To make the `GET()` request in the API, see the [CDAP API reference](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference).

  3. Back up the existing Cloud Storage directory.

     1. To edit the directory in the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click the bucket name to open the **Bucket details** page. The bucket name is the generation ID number.

The Cloud Storage bucket path in the Google Cloud console has a format similar to the following:

**Buckets** > `OFFSET_BASE_PATH` > `NAMESPACE_ID` > `REPLICATION_JOB_ID`

You can find the bucket by the `offsetBasePath` value for the job. To get the value, make a `GET()` request in Cloud Data Fusion with the following path:
    
    namespaces/NAMESPACE_ID/apps/REPLICATION_JOB_ID
    

  4. Perform the upgrade using the same steps as you would to [upgrade batch pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#upgrade-batch-pipelines).

  5. The upgraded job has a new generation ID. Use the new ID as the Cloud Storage directory name.

  6. [Start the replication job](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref#start-a-replication-job).




## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).
  * Refer to the [Replication API](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
