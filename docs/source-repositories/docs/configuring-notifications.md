---
url: https://docs.cloud.google.com/source-repositories/docs/configuring-notifications/
title: Configuring Pub/Sub notifications \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:08.411638+00:00
---

# Configuring Pub/Sub notifications  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/configuring-notifications/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Configuring Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can receive notifications of changes to your Google Cloud repositories by using Pub/Sub. These notifications inform you when a user creates a new repository, deletes a repository, or pushes a change to an existing repository. You can choose to configure notifications for specific repositories or across an entire Google Cloud project.

To learn more about Pub/Sub, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview)

## Before you begin

  * If you haven't already done so, [create a repository](https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository).
  * Verify that you have the appropriate permissions to create topics and subscriptions. For more information, see [Access control](https://docs.cloud.google.com/source-repositories/docs/configure-access-control).
  * Ensure you have a service account that can publish to your topic. By default, Cloud Source Repositories uses the Compute Engine default service account to publish messages. For more information, see [Pub/Sub notifications for Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications).



## Create a Pub/Sub topic

For each Cloud Source Repositories project or repository for which you'd like notifications, you need to create a Pub/Sub topic. You can create a topic using either the Google Cloud console or the `gcloud` command-line tool.

When you create a topic, you need to use a qualified URI for your repository. The qualified URI is:
    
    
    projects/[PROJECT_ID]/topics/[TOPIC_NAME]
    

Where:

  * `[PROJECT_ID]` is your Google Cloud project ID.
  * `[TOPIC_NAME]` is the name of the topic.



To create a topic, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to the Topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click **Create Topic**.

  3. Enter a topic name with the URI:
         
         projects/[PROJECT_ID]/topics/[TOPIC_NAME]
         

Where:

     * `[PROJECT_ID]` is your Google Cloud project ID.
     * `[TOPIC_NAME]` is the name of the topic.
  4. Click **Create**.

The **Topic details** page opens.




###  gcloud 

In a terminal window, run the following command:
    
    
    gcloud pubsub topics create projects/[PROJECT_ID]/topics/[TOPIC_NAME]
    

Where:

  * `[PROJECT_ID]` is your Google Cloud project ID.
  * `[TOPIC_NAME]` is the name of the topic.

**Note:** If this command returns a `Resource already exists in the project` error, you might already have a Cloud Source Repositories topic.

To learn more about the `gcloud pubsub topics` command, see the [`topics` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics).

## Create a Pub/Sub subscription

To receive events published to a topic, you need to create a [Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/subscriber#create).

A [subscriber app](https://docs.cloud.google.com/pubsub/docs/subscriber) receives messages from your repository's topic. Subscribers can respond to your repository events by sending notifications or triggering a build.

To create a subscription, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to the Topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click the name of your project's topic.

  3. Click **Create Subscription**.

The **Add subscription to topic** page opens.

  4. Enter a subscription name:
         
         projects/[PROJECT_ID]/subscriptions/[SUBSCRIPTION_NAME]
         

Where:

     * `[PROJECT_ID]` is your Google Cloud project ID.
     * `[SUBSCRIPTION_NAME]` is the name of the Pub/Sub subscription.
  5. Leave **Delivery type** set to **Pull**.

  6. Click **Create**.




###  gcloud 

In a terminal window, run the following command:
    
    
    gcloud pubsub subscriptions create [SUBSCRIPTION_NAME] --topic=[TOPIC_NAME]
    

Where:

  * `[SUBSCRIPTION_NAME]` is the name of the Pub/Sub subscription.
  * `[TOPIC_NAME]` is the name of the topic.

**Note:** Use the optional flag `--ack-deadline` to configure how many seconds the system waits for acknowledgement from the subscriber before re- attempting delivery. Without this flag, the default deadline is 10 seconds.

To learn more about the `gcloud pubsub subscriptions` command, see the [`subscriptions` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).

## Add a topic

You can associate a Pub/Sub topic with a Google Cloud project or repository by using the Google Cloud CLI.

To associate a topic with an entire project, enter the following command:
    
    
    gcloud source project-configs update --add-topic=[TOPIC_NAME] --service-account=[SERVICE_ACCOUNT_NAME]
    

Where:

  * `[TOPIC_NAME]` is the name of the Pub/Sub topic.
  * `[SERVICE_ACCOUNT_NAME]` is the name of your Cloud Build service account.



To associate a topic with a specific repository, enter the following command:
    
    
    gcloud source repos update [REPOSITORY_NAME] --add-topic=[TOPIC_NAME] --service-account=[SERVICE_ACCOUNT_NAME]
    

Where:

  * `[REPOSITORY_NAME]` is the name of your Google Cloud repository.
  * `[TOPIC_NAME]` is the name of the Pub/Sub topic.
  * `[SERVICE_ACCOUNT_NAME]` is the name of your Cloud Build service account.



The service account must be in the same project as the repository, and it must have `pubsub.topics.publish` permission to publish a message on the specified topic. You must have `iam.serviceAccounts.actAs` permission on the service account. If the service account isn't specified, it defaults to the Compute Engine default service account.

**Note:** For information on how to delete a Pub/Sub topic, see [Managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic).

## Remove a topic

You can remove an association between a project or repository and a Pub/Sub topic by using the Google Cloud CLI.

To remove a topic from an entire project, enter the following command:
    
    
    gcloud source project-configs update --remove-topic=[TOPIC_NAME]
    

To remove a topic from a specific repository, enter the following command:
    
    
    gcloud source repos update [REPOSITORY_NAME] --remove-topic=[TOPIC_NAME]
    

**Note:** For information on how to delete a Pub/Sub topic, see [Managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin#delete_a_topic).

## Set the topic format

Notifications for Cloud Source Repositories can use either the JSON or Protocol Buffers format. To set the format for a topic, you can use the `--message-format` parameter when you add the topic:
    
    
    gcloud source project-configs update --add-topic=[TOPIC_NAME] --message-format=[json|protobuf]
    

You can also use the `set-format` command:
    
    
    gcloud source project-configs update --update-topic=[TOPIC_NAME] --message-format=[json|protobuf]
    

## What's next

  * Learn more about [Pub/Sub notifications for Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications).
  * Read the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs).
  * For an in-depth explanation of Pub/Sub, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview).
  * Learn more about [Pub/Sub access control roles](https://docs.cloud.google.com/pubsub/docs/access_control#tbl_roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
