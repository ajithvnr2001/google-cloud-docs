---
url: https://docs.cloud.google.com/transcoder/docs/how-to/create-pub-sub/
title: Pub/Sub notifications for job updates \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:57.889096+00:00
---

# Pub/Sub notifications for job updates  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/create-pub-sub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Pub/Sub notifications for job updates Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure a Pub/Sub topic that you can use to receive job status updates from the Transcoder API.

## Configure job status updates

To receive job status updates, do the following:

  1. If you don't have an existing Pub/Sub topic, create a topic. To learn how to create a Pub/Sub topic, see [Managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin).

  2. Make sure to configure the [`pubsubDestination`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.pubsub_destination) field in the job configuration.
         
         {
           "config": {
             "pubsubDestination": {
               "topic": "projects/PROJECT_ID/topics/my-topic-id"
             }
           }
         }
         

  3. [Create a job](https://docs.cloud.google.com/transcoder/docs/how-to/jobs) to enable the [Google-managed Transcoder service account](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed).

  4. Find the `service-PROJECT_NUMBER@gcp-sa-transcoder.iam.gserviceaccount.com` service account in the Google Cloud console, where PROJECT_NUMBER is the project number of the project you enabled the Transcoder API in and you plan to create the feed from.

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam/project)

     2. Select the **Include Google-provided role grants** checkbox.

  5. Make sure the service account has the `pubsub.topics.publish` permission enabled.




## Job status reporting

Job status is reported once the job fails or finishes successfully. No other state changes are reported. Job status is reported using the `JobResult` message format:
    
    
    Resource PubSubMessage
    {
      job: {
        object (JobResult)
      }
    }
    
    JobResult
    {
      name: string;
      state: string;
      error: {
        object (Status)
      }
    }
    

For more information, refer to the following:

  * [Job state](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#processingstate)
  * [Job status](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#status)
  * [Troubleshooting job errors](https://docs.cloud.google.com/transcoder/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
