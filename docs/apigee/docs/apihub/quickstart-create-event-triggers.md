---
url: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-create-event-triggers/
title: Create an Eventarc trigger \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:11.096202+00:00
---

# Create an Eventarc trigger  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-create-event-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create an Eventarc trigger Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub supports [Eventarc triggers](https://docs.cloud.google.com/eventarc/docs/overview#eventarc-triggers). By using this feature, you can trigger executions based on the events occurring in API hub. For example, you can execute a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service when an API is created in API hub.

This quickstart shows you how to create and configure an Eventarc trigger that executes a Cloud Run service when an API is updated in API hub.

## Before you begin

  1. API hub must be provisioned in a Google Cloud project to which you have access. See [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision).
  2. In the Google Cloud console, on the project selector page, select the project in which API hub is provisioned.

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  3. You must have a valid Cloud Run service running. You will use the Cloud Run service details when configuring the Eventarc trigger. This is the service that will be executed when the configured event occurs.



## Create an Eventarc trigger

  1. In the Google Cloud console, go to the Eventarc **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**.
  3. Enter a **Trigger name**. For example, `cloudrun-trigger-1`.
  4. In the **Trigger type** list, select **Google sources**. 

This filters events sent from Google Cloud providers (directly or through Cloud Audit Logs entries), or providers using Pub/Sub messages.

  5. In the **Event provider** list, select **API hub**.
  6. In the **Event type** list, select **google.cloud.apihub.v1.updated**.
  7. In the **Event content data type** list, select either `JSON` or `Protobuf`.
  8. Select a **Region**.
  9. Optionally, **Add filters** to select the APIs that match your criteria. For example, if you filter the APIs by a specific name, the event is triggered only if the APIs matching the filter criteria are updated.
  10. If prompted, grant the following: 
     * `iam.serviceAccountTokenCreator` role to Pub/Sub service account
     * `pubsub.publisher` role to Cloud Storage service account
  11. Use the **Default compute service account** as the service account that invokes your service.
  12. In the **Event destination** list, select **Cloud Run**.
  13. Select a Cloud Run service that should be executed when the `google.cloud.apihub.v1.updated` event occurs in API hub.
  14. Optionally, enter the **Service URL path**.
  15. Click **Create**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
