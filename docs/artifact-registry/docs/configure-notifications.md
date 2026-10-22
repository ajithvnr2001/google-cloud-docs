---
url: https://docs.cloud.google.com/artifact-registry/docs/configure-notifications/
title: Configuring Pub/Sub notifications \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:50.292767+00:00
---

# Configuring Pub/Sub notifications  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/configure-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configuring Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can receive notifications from [Pub/Sub](https://docs.cloud.google.com/pubsub) for the changes to a Docker repository. Notifications apply to any container image stored in the repository, including [Helm 3 charts](https://docs.cloud.google.com/artifact-registry/docs/helm) packaged in OCI format.

Pub/Sub publishes messages about your repositories to named resources called _topics_. Applications that _subscribe_ to Pub/Sub topics receive these messages and receive notifications when a repository's state changes.

Artifact Registry publishes messages for the following changes:

  * Image uploads
  * New tags added to images
  * Image deletion



Additionally, you can configure roles and permissions for publishing or subscribing to notifications.

For information about configuring Artifact Analysis notifications for activity such as new vulnerability scan results, see the [Artifact Analysis documentation](https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications). 

## Overview

Artifact Registry publishes messages about changes to repositories in a topic named `gcr`.

To receive notifications, you must:

  1. Create a topic named `gcr` in the project with Artifact Registry.
  2. Create a subscription to the topic.
  3. Set up your subscriber application to receive messages about repository changes.
  4. If appropriate, configure permissions to control access to your topic and subscription.



## Creating the Artifact Registry topic

To create the `gcr` topic with Google-owned and Google-managed encryption keys:

### Console

  1. Go to the Pub/Sub topics page in the Google Cloud console.

[Go to the Pub/Sub topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click **Create Topic**.

  3. Enter the topic ID `gcr`.

  4. Click **Create Topic**.




### gcloud

Run the following command:
    
    
        gcloud pubsub topics create gcr --project=PROJECT-ID
    

Replace PROJECT-ID with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). If you omit the `--project` flag, the command uses the current project.

**Note:** If this command returns a "Resource already exists in the project" error, the topic `gcr` already exists in the project.

To learn more about the `gcloud pubsub topics` command, see the [`topics` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics).

To create the `gcr` topic with CMEK encryption, see the Pub/Sub [instructions for encrypting topics](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek).

After you have created the `gcr` topic or verified that it exists, you can create a subscription to the topic.

## Creating a subscription

After you have created a topic for repository changes, you can configure a subscription to it that uses either [push delivery](https://docs.cloud.google.com/pubsub/docs/push) or [pull delivery](https://docs.cloud.google.com/pubsub/docs/pull). We recommend using pull delivery since CI/CD systems can generate numerous changes to stored artifacts, and pull delivery is more effective for a large volume of messages.

To create a subscription with pull delivery:

### Console

  1. Go to the Pub/Sub topics page in the Google Cloud console.

[Go to the Pub/Sub topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click your project's topic.

  3. Click **Create Subscription**.

  4. Enter a subscription name:
         
         projects/PROJECT/subscriptions/[SUBSCRIPTION-NAME]
         

Leave **Delivery Type** set to **Pull**.

  5. Click **Create**.




### gcloud

Run the following command:
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION-NAME --topic=gcr
    

Replace SUBSCRIPTION-NAME with a name for the subscription

**Note:** Use the optional flag `--ack-deadline` to configure how many seconds the system will wait for acknowledgement from the subscriber before re-attempting delivery. Without this flag, the default deadline is 10 seconds.

To learn more about the `gcloud pubsub subscriptions` command, see the [`subscriptions` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).

You now have a subscription to the `gcr` topic. The next step is configuring permissions for the identities that trigger changes in repositories.

## Configuring your subscriber application

After you have created a topic and a subscription to that topic, you can set up your subscriber application, the application that receive messages about changes to repositories. Subscriber applications fulfill tasks like event notifications, system logging, and communication between applications.

When a repository user pushes or deletes an image, the following steps occur:

  1. The Artifact Registry service account publishes the change to your `gcr` topic. The service account is **service- PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com**, where PROJECT-NUMBER is your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). The Artifact Registry service account has the `pubsub.topics.publish` permission by default so that it can publish changes to your topic.

If an administrator has revoked the `pubsub.topics.publish` permissions for the Artifact Registry service account, Artifact Registry attempts to publish the message as the repository user. In this situation, the repository user's account must have the `pubsub.topics.publish` permission to successfully publish the message.

  2. Pub/Sub forwards the message from the topic to your subscription.

  3. When your subscriber application makes a request for messages, it pulls the new message from the subscription.

The identity that pulls messages on behalf of the subscriber must have permissions to access the subscription. You can use the [Pub/Sub Subscriber role](https://docs.cloud.google.com/pubsub/docs/access-control#roles) to grant this permission.




To learn about setting up a subscriber to receive messages from a subscription with pull delivery, see [Receiving messages using Pull](https://docs.cloud.google.com/pubsub/docs/pull).

## Configuring permissions

You can use Pub/Sub permissions to control access to your topics and subscriptions.

For more information about Pub/Sub permissions and granting access to topics and subscriptions, see the Pub/Sub [access control documentation](https://docs.cloud.google.com/pubsub/docs/access-control).

## Notification examples

Pub/Sub sends notifications as JSON-formatted strings. Review the following examples to learn what to expect when receiving Artifact Registry notifications from Pub/Sub.

When an image is pushed to Artifact Registry, the notification payload might look like this:
    
    
    {
      "action":"INSERT",
      "digest":"us-west1-docker.pkg.dev/my-project/my-repo/hello-world@sha256:6ec128e26cd5..."
    }
    

When a new image tag is pushed to Artifact Registry, the notification payload looks like this:
    
    
    {
      "action":"INSERT",
      "digest":"us-west1-docker.pkg.dev/my-project/my-repo/hello-world@sha256:6ec128e26cd5...",
      "tag":"us-west1-docker.pkg.dev/my-project/my-repo/hello-world:1.1"
    }
    

The message identifies the relevant image using either a `digest` or `tag` key.

When an image tag is deleted from Artifact Registry, the notification payload might look like this:
    
    
    {
      "action":"DELETE",
      "tag":"us-west1-docker.pkg.dev/my-project/my-repo/hello-world:1.1"
    }
    

The message might contain either `DELETE` or `INSERT` as values for the `action` key.

## What's next

  * Read the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs).
  * For an in-depth explanation of Pub/Sub, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview)
  * Learn more about [Pub/Sub access control roles](https://docs.cloud.google.com/pubsub/docs/access-control#roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
