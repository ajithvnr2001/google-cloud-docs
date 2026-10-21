---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/enable-replication/
title: Enable Replication in an instance \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:54:54.756472+00:00
---

# Enable Replication in an instance  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/enable-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Enable Replication in an instance Stay organized with collections  Save and categorize content based on your preferences. 

Replication in Cloud Data Fusion lets you stream real-time data changes from operational databases. You can enable Replication on an existing instance to deploy continuous change data capture (CDC) pipelines.

For more information, see [Replication overview](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).

## Enable Replication

### cURL

  1. Enable the Replication accelerator in your instance:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://datafusion.googleapis.com/v1/projects/PROJECT_NAME/locations/LOCATION/instances/INSTANCE_NAME?updateMask=accelerators \
             -X PATCH \
             -d '{ "accelerators":[{"accelerator_type":"CDC", "state":"ENABLED"}]} '
         

**Caution:** If your instance has labels when you enable the Replication accelerator, attach the labels in the request body to prevent them from being overwritten.

This sample command shows how to include labels that are already applied to an instance:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://datafusion.googleapis.com/v1/projects/PROJECT_NAME/locations/LOCATION/instances/INSTANCE_NAME?updateMask=accelerators \
             -X PATCH \
             -d '{ "accelerators":[{"accelerator_type":"CDC", "state":"ENABLED"}], "labels":{"KEY_1":"VALUE_1","KEY_2":"VALUE_2"}}'
         

Replace the following:

     * `PROJECT_NAME`: the Google Cloud project name
     * `LOCATION`: the location—for example, `us-east1`
     * `INSTANCE_NAME`: the Cloud Data Fusion instance name
     * `KEY_1` and `VALUE_1`: keys and values of your labels
  2. Optional: To verify the change was successful, click **System Admin**. **Delta Assessor** appears in the list of services.

The Replication tile appears on the Cloud Data Fusion home page.

  3. Click **System Admin** to check the status of the **Delta Assessor** service. When the status is green, you can create replication jobs.




## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication) in Cloud Data Fusion.
  * Refer to the [Replication API reference](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
