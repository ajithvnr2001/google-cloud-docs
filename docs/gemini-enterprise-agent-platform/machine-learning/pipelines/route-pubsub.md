---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/route-pubsub/
title: Route logs to a Cloud Pub/Sub sink \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:41.389717+00:00
---

# Route logs to a Cloud Pub/Sub sink  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/route-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Route logs to a Cloud Pub/Sub sink Stay organized with collections  Save and categorize content based on your preferences. 

You can route pipeline logs to a Cloud Pub/Sub sink to build an event-driven architecture. You can also sync pipeline logs into your observability tools. For more information about routing logs to a Cloud Pub/Sub sink, see [View logs routed to Pub/Sub](https://docs.cloud.google.com/logging/docs/export/pubsub).

This section describes how you can create a Pub/Sub topic, route (or sink) pipeline job logs to the Pub/Sub topic, and verify the logs published to the Pub/Sub topic. You can then subscribe downstream applications to the Pub/Sub topic to power event-driven architectures, or sync pipeline logs with your observability tools in near real-time.

Use the following instructions to set up a Pub/Sub sink and view the logs routed to it on the Google Cloud console:

  1. Create a Pub/Sub topic. For more information, see [Create a topic in the Cloud Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic).

  2. On the **Subscriptions** page of the Google Cloud console, create a pull subscription for the Pub/Sub topic. For more information, see [Create pull subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription).

  3. Select **Logging** from the navigation menu, then click **Go to Log Router** :  


[Go to Log Router](https://console.cloud.google.com/logs/router)

  4. In your project containing the logs you want to route, click **Create Sink**.

  5. Enter a name and description for the sink, and then click **Next**.

  6. In the **Service** list, select **Cloud Pub/Sub topic**.

  7. In the **Destination** list, select the Pub/Sub topic that you created, and then click **Next**.

  8. Under **Choose logs to include in sink** , specify the following inclusion filter:
         
         resource.type="aiplatform.googleapis.com/PipelineJob"
         

  9. Click **Create Sink**.

  10. On the **Subscriptions** page, click the subscription ID.

[Go to Subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription/list)

  11. Click the subcription ID that you created.

  12. On the subscription details page, click the **Messages** tab.

  13. To pull and view the pipeline job logs, click **Pull**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
