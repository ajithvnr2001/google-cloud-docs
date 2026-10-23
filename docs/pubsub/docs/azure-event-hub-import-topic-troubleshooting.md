---
url: https://docs.cloud.google.com/pubsub/docs/azure-event-hub-import-topic-troubleshooting/
title: Troubleshooting an Azure Event Hubs import topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:53.654969+00:00
---

# Troubleshooting an Azure Event Hubs import topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/azure-event-hub-import-topic-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting an Azure Event Hubs import topic Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some common troubleshooting tips for Azure Event Hubs import topics.

After you configure the import topic and start ingesting messages, you can check the relevant Cloud Monitoring metrics to see if data is ingested. Perform the following steps:

  1. In the console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the Azure Event Hubs import topic that you want to troubleshoot.

  3. In the topic details page, click the **Metrics** tab.

  4. Check the chart for the metric **Ingestion byte count**.

  5. If no data is being ingested, in the topic details page, check to see if there is an error for the **Topic state** field.

  6. You can also check the metric **Ingestion data source state**. To do so, in the topic details page, click the **Metrics** tab.

  7. Here is a list of errors that you might encounter:

Error Code | Description | Fix  
---|---|---  
`EVENT_HUBS_PERMISSION_DENIED` | Error consuming data from Azure Event Hubs due to permission issues. | Verify the roles assigned to the registered Azure app[ and ensure the necessary permissions are granted](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#grant_role_assignments).   
Ensure that a service account exists and that it is correctly configured as described in the procedure [Create an App registration with identity federation.](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#create_id) For more information about how to create a service account, see [Create a service account in Google Cloud.](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#create-service-account)  
Verify that the Pub/Sub service account has the `iam.serviceAccounts.getOpenIdToken` permission. For more information, see [Add the Service Account Token Creator role to the Pub/Sub service account.](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#add-service-account-token-creator)  
Verify that you have added the service account user role to the service account. For more information, see [Add the service account user role to the service account.](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#add-service-account-role)  
`PUBLISH_PERMISSION_DENIED` | Error publishing to the topic due to permission issues. |  Grant the Pub/Sub service account the [necessary publish permissions](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher). For more information, see [Add the Pub/Sub publisher role to the Pub/Sub service account.](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#add-publisher-role)  
`EVENT_HUB_NOT_FOUND ` | The provided Azure event hub couldn't be found. | Verify the Azure event hub for accuracy. Ensure that the Azure event hub exists and is accessible.  
`SUBSCRIPTION_NOT_FOUND ` | The provided Azure Event Hubs subscription couldn't be found. | Verify the subscription for accuracy. Ensure that the subscription exists.  
`RESOURCE_GROUP_NOT_FOUND ` | The provided Azure Event Hubs resource group couldn't be found. | Verify the resource group for accuracy. Ensure that the resource group exists within the specified subscription.  



If there are no errors till this point, check the best practices in [Maintain a healthy publisher](https://docs.cloud.google.com/pubsub/docs/monitoring#keeping_publishers_healthy).

You can also enable [platform logs](https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub) for an import topic. These logs help you troubleshoot issues when you have issues ingesting objects into Pub/Sub import topics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
