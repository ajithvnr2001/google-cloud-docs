---
url: https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger/
title: Configure an Eventarc trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:10.406039+00:00
---

# Configure an Eventarc trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure an Eventarc trigger

**Private Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure an Eventarc trigger in Application Integration. 

An Eventarc trigger lets you run integrations based on events routed through [Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/overview). Using an Eventarc trigger, you can build integration flows triggered by events from various Google Cloud services, third-party services, and custom event sources. For example, you can use the trigger to initiate an integration when a new object is uploaded to a Cloud Storage bucket. 

In the Google Cloud console, you can create and configure an Eventarc trigger in the following ways:

  * Using Application Integration
  * Using Eventarc



## Before you begin

Before configuring the Eventarc trigger, enable the Eventarc API and the Pub/Sub API:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,pubsub.googleapis.com)

## Considerations

Consider the following when configuring an Eventarc trigger: 

  * If creating the Eventarc trigger fails during integration publication due to configuration errors, your integration will still publish, but the trigger won't be active. 

To fix this, unpublish the integration, carefully review and correct the Eventarc trigger configuration, and then republish the integration. You can check the Eventarc trigger creation status by clicking notifications_none (Notification) in the [Google Cloud console](https://console.cloud.google.com) tool bar.

  * Publishing a new version of your integration with a modified Eventarc trigger configuration automatically replaces the old trigger with a new one. This ensures your integration always uses the latest trigger configuration and deletes any obsolete triggers. 
  * If you publish a new version of your integration and use the same Eventarc trigger and its configuration, a new trigger isn't created. Instead, the existing Eventarc trigger is reused for your new integration version.



## Create an Eventarc trigger from Application Integration

To create an **Eventarc trigger** from Application Integration, do the following steps: 

  1. Add the Eventarc trigger in Application Integration
  2. Configure the Eventarc trigger in the integration editor



### Add the Eventarc trigger

To add an Eventarc trigger to your integration, complete the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Drag and drop the **Eventarc** element in the integration editor.



### Configure the Eventarc trigger

To configure an Eventarc trigger, click the **Eventarc Trigger** element in the integration editor. The **Eventarc Trigger** configuration pane appears showing the following fields:

  * **Label:** (optional) the visible name of the Eventarc trigger in your integration. You can change the label to a name of your choice. 
  * **Notes:** (optional) you can add notes to provide additional information about the trigger.
  * Click **Configure Eventarc trigger** and provide the following inputs in the **Eventarc trigger editor** : 
    * **Trigger name** : enter a name for the trigger.
    * **Trigger type** : select one of the following trigger types: 
      * **Google source** : select this option to create a trigger for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.
      * **Custom** : select this option to create a trigger for a custom event source.
      * **Third-party** : select this option to create a trigger for non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview).
    * **Event provider** : select the event provider for the trigger. The list of event providers depends on the trigger type. For more information, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets).
    * **Event type** : select the event type for the trigger. Your trigger configuration varies based on the event provider you select. For more information, see [Event types](https://docs.cloud.google.com/eventarc/standard/docs/event-types).
    * **Region** : select the region for the trigger. **Tip:** For optimal performance and to minimize latency, ensure that your Eventarc trigger, the monitored Google Cloud resource, and your service are all located in the same Google Cloud region. 
    * **Filters** : (optional) add filters to select the APIs that match your criteria. For example, if you filter the APIs by a specific name, the event is triggered only if the APIs matching the filter criteria are updated.
    * **Service account** : select the service account to use for the trigger. If you don't select a service account, the trigger uses the Compute Engine default service account as its identity when invoking your service. The service account associated with the trigger must have the required permissions to invoke your service. 
    * **Retry on failure** : select to enable trigger retries if the destination fails to process the event.
    * **Network attachment** : select the network attachment to use for the trigger. This list is generated based on the network attachments created in your project. 

Network attachments facilitate communication between service producer Virtual Private Cloud (VPC) networks and consumer VPC networks. Eventarc uses the configured network attachment to establish a connection to an internal HTTP endpoint hosted within the consumer's VPC network, enabling delivery of event data. For more information about creating and managing network attachments, see [Create and manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments). 

  * To save the trigger configuration, click **Save trigger**.
**Note:** Saving your Eventarc trigger configuration defines the rules that determine when and how Eventarc responds to events. This configuration is stored as part of your trigger definition in Application Integration. However, these rules are not immediately applied. You must publish the integration to deploy these rules and activate the Eventarc trigger. Until published, the trigger remains inactive and doesn't process events. For information about publishing integrations, see [Publish integrations](https://docs.cloud.google.com/application-integration/docs/publish-integrations). 


## Create an Eventarc trigger using the Eventarc console

To create an Eventarc trigger from the Eventarc console page, do the following steps: 

  1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

The **Triggers** page lists all the triggers in your project. 

  2. Click add_box **Create trigger**. 
  3. In the **Create trigger** page, provide the following inputs: 
     1. **Trigger name** : enter a name for the trigger.
     2. **Trigger type** : select one of the following trigger types: 
        * **Google sources** : select this option to create a trigger for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.
        * **Custom** : select this option to create a trigger for a custom event source.
        * **Third-party** : select this option to create a trigger for non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview).
     3. **Event provider** : select the event provider for the trigger. The list of event providers depends on the trigger type. For more information, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).
     4. **Event type** : select the event type for the trigger. Your trigger configuration varies based on the event provider you select. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).
     5. **Event data content type** : select the data type for the event content. Select either **application/json** or **application/protobuf**.
     6. **Region** : select the region for the trigger. **Tip:** For optimal performance and to minimize latency, ensure that your Eventarc trigger, the monitored Google Cloud resource, and your service are all located in the same Google Cloud region. 
     7. **Service account** : select the service account to use for the trigger. If you don't select a service account, the trigger uses the Compute Engine default service account as its identity when invoking your service. The service account associated with the trigger must have the required permissions to invoke your service. 
     8. **Event destination** : select **Application Integration**.
     9. **Select an Integration** : select the integration for which you want to create the trigger. If the integration is published, Application Integration creates a new [draft version](https://docs.cloud.google.com/application-integration/docs/integration-versions) of the integration to add the Eventarc trigger to.
     10. **Network attachment** : select the network attachment to use for the trigger. This list is generated based on the network attachments created in your project. 

Network attachments facilitate communication between service producer Virtual Private Cloud (VPC) networks and consumer VPC networks. Eventarc uses the configured network attachment to establish a connection to an internal HTTP endpoint hosted within the consumer's VPC network, enabling delivery of event data. For more information about network attachments, see [About network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments). 

  4. Click **Open integration**. 

The Application Integration editor page opens with the integration selected and the new **Eventarc trigger** element added to the integration. 

  5. Click the **Eventarc trigger** element and open the trigger configuration pane.
  6. Review and verify the trigger configuration in the **Eventarc trigger editor** page.
  7. Connect the new **Eventarc trigger** to your integration flow and publish the integration.
**Note:** You must publish the integration to deploy and activate the **Eventarc trigger**. Until published, the trigger remains inactive and will not process events. For information about publishing integrations, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations). 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
