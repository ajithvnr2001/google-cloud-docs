---
url: https://docs.cloud.google.com/application-integration/docs/configuring-pubsub-trigger/
title: Cloud Pub/Sub trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:24.131427+00:00
---

# Cloud Pub/Sub trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configuring-pubsub-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Pub/Sub trigger

The **Cloud Pub/Sub trigger** lets you run your integration based on the events in your **Pub/Sub** middleware. 

Using this trigger, you can execute an integration whenever a publisher writes a message to your chosen topic. The topic can exist in the same Google Cloud project as the integration, or in a different Google Cloud project. When this trigger executes, it also writes the published message to the `CloudPubSubMessage` output variable. Based on your requirements, you can use this variable in your downstream triggers or tasks. 

To learn how to create a sample integration using Application Integration and the Cloud Pub/Sub trigger trigger, see [Listen to Cloud Pub/Sub topic and send an email](https://docs.cloud.google.com/application-integration/docs/listen-pub-sub-topic-send-email).

Using this trigger, you can execute an integration whenever a publisher writes a message to your chosen topic. When this trigger executes, it also writes the published message to the **CloudPubSubMessage** output variable. Based on your requirements, you can use this variable in your downstream triggers or tasks. 

**Note** : The topic that you configure for the trigger must be available in the same Google Cloud project as your integration. Application Integration does not support **Cloud Pub/Sub trigger** executions across different Google Cloud projects. 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Cloud Pub/Sub trigger**. 

  * Assign the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) to the user creating this trigger.
  * Enable the [Pub/Sub API](https://console.cloud.google.com//marketplace/product/google/pubsub.googleapis.com) for the Google Cloud project that has your integration.

If the Pub/Sub API is protected by a service perimeter, ensure that you define the following [IAM roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) to manage these service perimeters:

    * Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)
    * Access Context Manager Editor (`roles/accesscontextmanager.policyEditor`)
    * Access Context Manager Reader (`roles/accesscontextmanager.policyReader`)

  * Confirm that you have a Pub/Sub topic. To create a new Pub/Sub topic: 
    1. Go to the Pub/Sub topics page in the [Cloud console](https://console.cloud.google.com/). 

[ Go to the Pub/Sub topics page](https://console.cloud.google.com//cloudpubsub/topicList)

    2. Click **Create a topic**.
    3. In the **Topic ID** field, provide a unique topic name.
    4. Click **Save**.
**Note:** You don't have to create a subscription for the trigger to work. Application Integration automatically creates a subscription for a topic when you publish your integration, and you can view all your subscriptions in the [Pub/Sub subscription page](https://console.cloud.google.com//cloudpubsub/subscription). 

Starting with the Application Integration [December 01 2023 release](https://docs.cloud.google.com/application-integration/docs/release-notes#December_01_2023), you will be billed for your subscriptions as per the [Pub/Sub billing rates](https://docs.cloud.google.com/pubsub/pricing). Subscriptions for your existing Cloud Pub/Sub trigger will continue to work as before, and they aren't billed. However, if you update the topic of an existing Cloud Pub/Sub trigger, Pub/Sub billing will be applied to the updated Cloud Pub/Sub trigger.


For more information about managing access using IAM roles, see [Access control](https://docs.cloud.google.com/application-integration/docs/access-control). 

For information on granting roles to principals, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

## Add a Cloud Pub/Sub trigger

To add a **Cloud Pub/Sub trigger** to a new or existing integration, follow the steps below: 

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
  5. Click and place the **Cloud Pub/Sub trigger** element to the designer.



## Configure a Cloud Pub/Sub trigger

Click the **Cloud Pub/Sub trigger** element in the integration editor to view the trigger configuration pane, and then do the following tasks:

  1. Specify the topic the trigger should listen to in the **Pub/Sub topic** field in the following format: 
         
         projects/PROJECT_ID/topics/TOPIC_ID

To view all the available topics in your Google Cloud project, see the **Topic name** column in [Topics](https://console.cloud.google.com//cloudpubsub/topic/list). You can also select a topic from a different Google Cloud project. 

Replace the following: 
     * `PROJECT_ID`: the Google Cloud project where your topic is created.
     * `TOPIC_ID`: the ID of your Pub/Sub topic. The topic can be in the same Google Cloud project as that of your integration, or can be present in a different Google Cloud project.
  2. Select the service account which you want to use to invoke the integration. You can also choose a [config variable](https://docs.cloud.google.com/application-integration/docs/variables#config_var) that you have created in the integration. The value of the config variable must be a service account email address with the following format: `SERVICE_ACCOUNT_NAME@project-id.iam.gserviceaccount.com`. For example, `application-integration-invoke@project123.iam.gserviceaccount.com`. 

For information about how to create a config variable, see [create a variable](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable), and about how to create a service account, see [Creating a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

If you choose a config variable, you must grant the required roles to the service account that the config variable refers to. For more information about how to grant roles, see Required IAM roles.

If there are no service accounts, create a service account by clicking **Create new** in the **Service account** list.

**Note:** Starting with the Application Integration [December 01 2023 release](https://docs.cloud.google.com/application-integration/docs/release-notes#December_01_2023), when you configure the Cloud Pub/Sub trigger, you must specify a service account for the trigger. Your existing Pub/Sub triggers, that don't have any service account associated with them, will continue to work as before. However, if you want to modify any of the existing Pub/Sub triggers, you must configure a service account to continue using those triggers.



By default, the [expiration period option](https://docs.cloud.google.com/pubsub/docs/subscription-properties#expiration_periods) for subscriptions is set to `never expire`. If you want to set the expiration to another value, in the Google Cloud console, go to the [Pub/Sub subscription page](https://console.cloud.google.com/cloudpubsub/subscription) and edit the subscription.

### IAM roles required for service accounts

Clicking **Grant** when selecting a service account, automatically provides the following roles to the various service accounts.

Service account | IAM role granted  
---|---  
Application Integration's default service account: `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com` | 

  * Pub/Sub Editor (`roles/pubsub.editor`)
  * Service Account User (`roles/iam.serviceAccountUser`)

If the Pub/Sub topic's Google Cloud project is different from the integration's Google Cloud project, the default service account needs Pub/Sub Editor role in the topic's Google Cloud project.   
Service account that you select for this trigger |  Application Integration Invoker (`roles/integrations.integrationInvoker`)   
  
## Trigger Output

For each event, the **Cloud Pub/Sub trigger** generates a `CloudPubSubMessage` output variable which you can use in your downstream tasks. The variable is in JSON format and has the [`PubsubMessage`](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) structure. 

## Create subscription with filter for your integration

If you want to set a filter for the Pub/Sub subscription to process specific events in your integration, follow these steps:

  1. Publish the integration with the Cloud Pub/Sub trigger configured. This step creates the subscription in the integration project.
  2. In the Google Cloud console, go to the **Subscriptions** page. 

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  3. Open the subscription and copy all the details including the subscription name.
  4. Delete the existing subscription.
  5. Create a new subscription with all the details of the deleted subscription–including the subscription name–that you copied in step 3 and also [add a filter in the new subscription](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter#creating_subscriptions_with_filters). 

The newly created subscription triggers the integration with filtered messages.




## SLA exclusions

The Cloud Pub/Sub trigger is dependent on the [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) product. As this dependency is external to the Application Integration, the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions are applicable only when the Cloud Pub/Sub trigger successfully starts the execution of an `active` integration.

## Use Pub/Sub triggers with VPC Service Controls

When you configure a Pub/Sub trigger in Application Integration and attempt to publish the integration, the creation of the required Pub/Sub subscription fails if the Pub/Sub API is protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in VPC Service Controls.

Service perimeters enforce security boundaries around your Google Cloud resources, and these policies can prevent Application Integration from creating the necessary Pub/Sub subscription during integration publishing.

To successfully configure and publish a Pub/Sub trigger in these scenarios, perform the following steps:

  1. Temporarily remove the Pub/Sub API from the service perimeter: 
     1. In the Google Cloud console, go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

     2. Select the Google Cloud project that contains the Pub/Sub topic to be used in the integration.
     3. (Optional) If no access policy is configured for the selected project, the message **No VPC Service Perimeters found in current scope** will appear. In this case, click **Switch to organization scope** to navigate to the organization level.
     4. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.
     5. On the **Service perimeter details** page, click **Edit**.
     6. In the **Restricted services** pane, filter and select the `pubsub.googleapis.com` service.
     7. Click delete **Remove Selected**.
     8. Click **Save**. In the confirmation dialog, click **Confirm** to remove the Pub/Sub API from your VPC Service Controls service perimeter.
  2. Add and configure the Pub/Sub trigger in your integration.
  3. [Publish the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  4. Add the Pub/Sub API back to the service perimeter: 
     1. Go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

     2. On the **VPC Service Controls** page, in the table, click the same service perimeter that you modified earlier.
     3. On the **Service perimeter details** page, click **Edit**.
     4. In the **Restricted services** pane, click add **Add services**.
     5. Filter and select the `pubsub.googleapis.com` service.
     6. Click **Add selected services**.
     7. Click **Save**. In the confirmation dialog, click **Confirm** to add the Pub/Sub API back to your VPC Service Controls service perimeter.



## Pricing

The Cloud Pub/Sub trigger and Salesforce trigger don't require you to create a [connector](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors). However, if you use the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) to connect to Pub/Sub or Salesforce, then you are billed for the connector usage. For information about pricing, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/docs/pricing).

## Considerations

  * The maximum size of a Pub/Sub message is 10 MB. To understand all the limitations of Pub/Sub, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).
  * It is possible that Pub/Sub writes the same message more than once to a topic. To understand this behavior of Pub/Sub, see [At-Least-Once delivery](https://docs.cloud.google.com/pubsub/docs/subscriber#at-least-once-delivery). Therefore, you must design your integration to be idempotent so that it doesn't allow a message to be written more than once to a topic. 

The `message_id` field in the message header uniquely identifies a Pub/Sub message.

  * Application Integration now lets you publish messages to Pub/Sub topics. You can use ordering keys to achieve First-In, First-Out (FIFO) message processing. When you set an ordering key in the **Publish Pub/Sub Message** task, messages are received in the correct order. This improves reliability for integrations that need ordered message processing. To learn more about how to use ordering keys when you publish messages, see [Using ordering keys](https://cloud.google.com/pubsub/docs/publisher#using-ordering-keys). 
  * If you unpublish an integration, the Pub/Sub subscription is not deleted to prevent loss of messages. However, if you delete the published version or all the integration versions of an integration, then the Pub/Sub subscription is also deleted.



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
