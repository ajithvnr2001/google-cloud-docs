---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot/
title: Troubleshoot Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:17:11.626118+00:00
---

# Troubleshoot Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Data Fusion.

## Retrieve error information for a failed pipeline run

When a pipeline run fails, you can retrieve detailed error information. Cloud Data Fusion 6.11.0 classifies pipeline errors by category, reason, and message. This classification speeds up resolution and reduces the need to examine complex logs.

To get error details, follow these steps:

###  Console 

  1. In the Google Cloud console, open your Cloud Data Fusion instance and go to your pipeline on the **Studio** page.

  2. On the node where the error occurred, click **View errors**.

  3. Review the error details, which include the error category, error reason, and error message.

  4. Optional: To download raw logs for further analysis, click **Download raw logs**.

  5. Optional: To view raw logs, click **View logs**.




###  REST 

Send a `POST` request to the following endpoint:
    
    
     curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
     -H "Content-Type: application/json" 
     ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/apps/PIPELINE_NAME/workflows/DataPipelineWorkflow/runs/RUN_ID/classify -X POST
    

Replace the following:

  * `NAMESPACE_ID`: the ID of the namespace
  * `PIPELINE_NAME`: the name of the pipeline
  * `RUN_ID`: the run ID of the pipeline



The following is a sample response for a plugin error:
    
    
     [
        {
           "stageName": "Stage Name",
           "errorCategory": "Plugin-x",
           "errorReason": "Input path gs://x does not exist",
           "errorMessage": "Input path gs://x does not exist",
           "errorType": "SYSTEM/USER/UNKNOWN",
           "dependency": "true/false"
        }
     ]
     ```
    You can also [view advanced logs for your pipelines](/data-fusion/docs/how-to/viewing-stackdriver-logs).
    

## Resolve issues with creating Cloud Data Fusion instance

When you create a Cloud Data Fusion instance, you might encounter the following issue:
    
    
    Read access to project PROJECT_ID was denied.
    

To resolve this issue, disable and re-enable the [Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service), and then create the instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
