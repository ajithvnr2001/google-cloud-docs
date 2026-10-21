---
url: https://docs.cloud.google.com/pubsub/lite/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:08.343451+00:00
---

# Access control with IAM  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document describes the access control options for Pub/Sub Lite. Pub/Sub Lite uses [Identity and Access Management](https://docs.cloud.google.com/iam/docs) for access control.

To give a user or application access to Pub/Sub Lite resources, grant at least one predefined or custom role to the user or the service account that the application uses. The roles include permissions to perform specific actions on Pub/Sub Lite resources.

## Predefined roles

The following table lists the predefined roles that give you access to Pub/Sub Lite resources:

Role | Title | Description | Permissions  
---|---|---|---  
`roles/pubsublite.admin` |  Pub/Sub Lite Admin  |  Full access to Lite topics and Lite subscriptions.  |  `pubsublite.*` |   
`roles/pubsublite.editor` |  Pub/Sub Lite Editor  |  Modify Lite topics and Lite subscriptions, publish message to Lite topics, and receive messages from Lite subscriptions.  |  `pubsublite.*`  
`roles/pubsublite.publisher` |  Pub/Sub Lite Publisher  |  Publish messages to Lite topics.  | 
* `pubsublite.topics.getPartitions`
* `pubsublite.topics.publish`
* `pubsublite.locations.openKafkaStream`  
`roles/pubsublite.subscriber` |  Pub/Sub Lite Subscriber  |  Receive messages from Lite subscriptions.  | 

  * `pubsublite.operations.get`
  * `pubsublite.subscriptions.getCursor`
  * `pubsublite.subscriptions.seek`
  * `pubsublite.subscriptions.setCursor`
  * `pubsublite.subscriptions.subscribe`
  * `pubsublite.topics.computeHeadCursor`
  * `pubsublite.topics.computeMessageStats`
  * `pubsublite.topics.computeTimeCursor`
  * `pubsublite.topics.getPartitions`
  * `pubsublite.topics.subscribe`
  * `pubsublite.locations.openKafkaStream`

  
`roles/pubsublite.viewer` |  Pub/Sub Lite Viewer  |  View Lite topics and Lite subscriptions.  | 

  * `pubsublite.operations.get`
  * `pubsublite.operations.list`
  * `pubsublite.subscriptions.get`
  * `pubsublite.subscriptions.getCursor`
  * `pubsublite.subscriptions.list`
  * `pubsublite.topics.get`
  * `pubsublite.topics.getPartitions`
  * `pubsublite.topics.list`
  * `pubsublite.topics.listSubscriptions`

  
  
## Custom roles

Custom roles can include any permissions that you specify. You can create custom roles that include permissions to perform specific administrative operations, like updating Lite topics or deleting Lite subscriptions. To create custom roles, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

The following table lists examples of custom roles:

Description | Permissions  
---|---  
Create and manage Lite reservations. | 

  * `pubsublite.reservations.create`
  * `pubsublite.reservations.update`
  * `pubsublite.reservations.get`
  * `pubsublite.reservations.list`
  * `pubsublite.reservations.delete`

  
Create and manage Lite topics. | 

  * `pubsublite.topics.create`
  * `pubsublite.topics.update`
  * `pubsublite.topics.get`
  * `pubsublite.topics.getPartitions`
  * `pubsublite.topics.list`
  * `pubsublite.topics.listSubscriptions`
  * `pubsublite.topics.delete`

  
Create and manage Lite subscriptions. | 

  * `pubsublite.subscriptions.create`
  * `pubsublite.topics.subscribe`
  * `pubsublite.subscriptions.update`
  * `pubsublite.subscriptions.get`
  * `pubsublite.subscriptions.list`
  * `pubsublite.subscriptions.delete`

  
Create Lite topics and Lite subscriptions. | 

  * `pubsublite.topics.create`
  * `pubsublite.subscriptions.create`
  * `pubsublite.topics.subscribe`

  
Modify Lite topics and Lite subscriptions. | 

  * `pubsublite.topics.update`
  * `pubsublite.subscriptions.update`

  
Delete Lite topics and Lite subscriptions. | 

  * `pubsublite.topics.delete`
  * `pubsublite.subscriptions.delete`

  
  
## Granting roles

You can grant roles to access Pub/Sub Lite resources at the project level. For example, you can give a service account access to view any Lite topic in a project, but you can't give a service account access to view a single Lite topic.

To grant a role on a project, you can use the Google Cloud console or the Google Cloud CLI.

### Console

To grant a role to a user, service account, or other member, follow these steps:

  1. In the Google Cloud console, go to the IAM page.



[Go to IAM](https://console.cloud.google.com/iam-admin)

  1. Click **Add**.

  2. Enter the email address of a user, service account, or other member.

  3. Select a role.

  4. Click **Save**.




### gcloud

To grant a role to a user, service account, or other member, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=MEMBER \
    --role=ROLE_ID

Replace the following:

  * MEMBER: an [identifier for the member](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding), like `serviceAccount:test123@example.domain.com`
  * ROLE_ID: the name of the predefined or custom role



You can also get a JSON or YAML file with the current IAM policy, add multiple roles or members to the file, and then update the policy. To read and manage the policy, use the Google Cloud CLI, the IAM API, or the IAM. For details, see [Controlling access programmatically](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#programmatic).

## What's next

  * Get an [overview of IAM](https://docs.cloud.google.com/iam/docs/overview).
  * Refer to the [authentication methods that Pub/Sub Lite supports](https://docs.cloud.google.com/pubsub/lite/docs).
  * Learn more about [managing access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
