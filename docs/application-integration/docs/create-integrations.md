---
url: https://docs.cloud.google.com/application-integration/docs/create-integrations/
title: Create a new integration \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:33:43.791995+00:00
---

# Create a new integration  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/create-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a new integration

This page describes how to create a new blank integration by using the Google Cloud console. If you are new to creating integrations, you can try the following quickstarts:

  * [Retrieve API payload and send an email](https://docs.cloud.google.com/application-integration/docs/retrieve-api-payload-send-email).
  * [Listen to Pub/Sub topic and send an email](https://docs.cloud.google.com/application-integration/docs/listen-pub-sub-topic-send-email).
  * [Invoke a sub-integration using a For Each Loop task](https://docs.cloud.google.com/application-integration/docs/invoke-sub-int-for-each-loop).

**Tip:** You can also build integrations by using Google's generative AI. For more information, see [Build integrations with Gemini](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini). 

## Create a new integration

After you Set up Application Integration, you can create a new integration: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter a name for your integration. For example, `example-integration`.
     2. **Description:** Optionally, enter a description for your integration. For example, `Demo integration created for tutorial`.
     3. **Region:** Select the region `us-central1` from the list of provisioned regions. If the region that you want to select is not provision, see [Provision a new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#provision-new-region). To see a list of supported regions, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).
     4. **Service account** : This field appears if you have enabled governance for your region. Select the service account for your integration. To learn how to enable governance for your region, see [Edit region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region).
     5. Click **Create**. This opens the integration editor page in which you can add the [tasks](https://docs.cloud.google.com/application-integration/docs/tasks) and the [triggers](https://docs.cloud.google.com/application-integration/docs/triggers) to build your integration. For more information about this page, see [Explore the integration editor layout](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout#explore-integration-designer-layout).



## What's next

  * Explore the [integration editor](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout).
  * Try the [sample integration](https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce)
  * Learn about [tasks](https://docs.cloud.google.com/application-integration/docs/tasks) and [triggers](https://docs.cloud.google.com/application-integration/docs/triggers)
  * Learn how to [view and edit integration details](https://docs.cloud.google.com/application-integration/docs/view-integration-details)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
