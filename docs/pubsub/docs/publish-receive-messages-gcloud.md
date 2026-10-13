---
url: https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud/
title: Quickstart: Publish and receive messages in Pub/Sub by using the gcloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:46.215189+00:00
---

# Quickstart: Publish and receive messages in Pub/Sub by using the gcloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish and receive messages in Pub/Sub by using the gcloud CLI

This page shows you how to do the following operations in Pub/Sub using the Google Cloud CLI:

  * Create a topic and subscription.
  * Publish messages to the topic.
  * Receive messages from the subscription.



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?tutorial=pubsub_quickstart_gcloud)

* * *

## Before you begin

Complete the following steps before running your quickstart.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. Set up a Google Cloud console project.

Set up a project

Click to:

     * Create or select a project.
     * Enable the Pub/Sub API for that project, if it is not already enabled. 

You can view and manage these resources at any time in the [Google Cloud console](https://console.cloud.google.com/).

  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  4. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  5. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  6. Set up a Google Cloud console project.

Set up a project

Click to:

     * Create or select a project.
     * Enable the Pub/Sub API for that project, if it is not already enabled. 

You can view and manage these resources at any time in the [Google Cloud console](https://console.cloud.google.com/).

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




### Required roles

To complete this quickstart, you need the following Identity and Access Management (IAM) (IAM) roles.

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a topic

Create a topic with the ID `my-topic`:
    
    
    gcloud pubsub topics create my-topic

## Create a subscription

Create a subscription with the ID `my-sub` and attach it to `my-topic`:
    
    
    gcloud pubsub subscriptions create my-sub --topic=my-topic

## Publish messages

Publish a message to `my-topic`:
    
    
    gcloud pubsub topics publish my-topic --message="hello"

## Receive messages

Receive the message from `my-sub`:
    
    
    gcloud pubsub subscriptions pull my-sub --auto-ack

The gcloud CLI prints the message to the command line.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## What's next

  * See all the available [gcloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub) for Pub/Sub

  * Learn more about the Pub/Sub [concepts](https://docs.cloud.google.com/pubsub/docs/overview) discussed in this page.

  * Read the [basics of the Pub/Sub service](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

  * Work through an [end-to-end example](https://docs.cloud.google.com/pubsub/docs/building-pubsub-messaging-system) of a Pub/Sub system.

  * Try another Pub/Sub quickstart that uses [client libraries](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-client-library) or the [console](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console).

  * Learn how to create [topics](https://docs.cloud.google.com/pubsub/docs/create-topic) and publish [messages](https://docs.cloud.google.com/pubsub/docs/publisher).

  * [Choose](https://docs.cloud.google.com/pubsub/docs/subscriber) a subscription type.

  * Learn more about [Pub/Sub APIs](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
