---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/dp-receive-pubsub-messages/
title: Receive and parse Pub/Sub messages about data profiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:13.778925+00:00
---

# Receive and parse Pub/Sub messages about data profiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/dp-receive-pubsub-messages/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Receive and parse Pub/Sub messages about data profiles Stay organized with collections  Save and categorize content based on your preferences. 

This document provides examples that demonstrate how to receive and parse notifications about changes to your data profiles. Sensitive Data Protection sends these updates in the form of [Pub/Sub messages](https://docs.cloud.google.com/pubsub/docs/overview#core_concepts "Pub/Sub core concepts").

## Overview

You can configure Sensitive Data Protection to automatically generate profiles about data across an organization, folder, or project. [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) contain metrics and metadata about your data and help you determine where [sensitive and high-risk data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation) reside. Sensitive Data Protection reports these metrics at various levels of detail. For information about the types of data you can profile, see [Supported resources](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources). 

When configuring the data profiler, you can turn on the option to publish Pub/Sub messages whenever significant changes in your data profiles occur. The messages help you take immediate action in response to those changes. The following are the events that you can listen for:

  * A data asset is profiled for the first time.
  * A profile is updated.
  * The risk or sensitivity score of a profile increases.
  * There is a new error related to your data profiles.



The Pub/Sub messages that the data profiler publishes contain a [`DataProfilePubSubMessage`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfilePubSubMessage "Documentation for the DataProfilePubSubMessage object") object. These messages are always sent in binary format, so you need to write code that receives and parses them.

## Pricing

When you use Pub/Sub, you are billed according to [Pub/Sub pricing](https://docs.cloud.google.com/pubsub/pricing "Pub/Sub pricing").

## Before you begin

This page assumes the following:

  * You are familiar with using Pub/Sub. For an introduction, see the quickstart [Publish and receive messages in Pub/Sub by using the console](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console "Publish and receive messages in Pub/Sub by using the console").
  * You already have a scan configuration at the [organization, folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder "Profile data in an organization or folder") or [project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project "Profile data in a single project") level.
  * You are familiar with configuring Google Cloud client libraries.



Before you start working on the examples, follow these steps:

  1. [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic "Create a topic") and add a subscription for it. Don't assign a schema to the topic.

For simplicity, the examples on this page listen to only one subscription. However, in practice, you can create a topic and subscription for each event that Sensitive Data Protection supports.

  2. If you haven't already done so, configure the data profiler to publish Pub/Sub messages:

     1. [Edit](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config "Edit a scan configuration") your scan configuration.

     2. On the **Edit scan configuration** page, turn on the **Publish to Pub/Sub** option and select the events that you want to listen for. Then, [configure the settings](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#publish-pubsub "Publish to Pub/Sub") for each event.

     3. Save the scan configuration.

  3. [Grant the Sensitive Data Protection service agent publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console "Controlling access through the Google Cloud console") on the Pub/Sub topic. An example of a role that has publishing access is the Pub/Sub Publisher role (`roles/pubsub.publisher`). The Sensitive Data Protection service agent is an email address in the format:
         
         service-PROJECT_NUMBER@dlp-api.iam.gserviceaccount.com
         

If you're working with an organization- or folder-level scan configuration, the PROJECT_NUMBER is the numerical identifier of the [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container "Service agent container and service agent"). If you're working with a project-level scan configuration, the PROJECT_NUMBER is the numerical identifier of your project.

**Note:** If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 
  4. Install and set up the [Sensitive Data Protection client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries "Sensitive Data Protection client libraries") for Java or Python.




## Examples

The following examples demonstrate how to receive and parse Pub/Sub messages that the data profiler publishes. You can repurpose these examples and deploy them as Cloud Run functions that are triggered by Pub/Sub events. For more information, see [Pub/Sub tutorial (2nd gen)](https://docs.cloud.google.com/functions/docs/tutorials/pubsub "Pub/Sub tutorial \(2nd gen\)").

In the following examples, replace the following:

  * PROJECT_ID: the ID of the project that contains the Pub/Sub subscription.
  * SUBSCRIPTION_ID: the ID of the Pub/Sub subscription.



### Java
    
    
    import com.google.api.core.[ApiService](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiService.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.privacy.dlp.v2.[DataProfilePubSubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfilePubSubMessage.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DataProfilePubSubMessageParser {
    
      public static void main(String... args) throws Exception {
        String projectId = "PROJECT_ID";
        String subscriptionId = "SUBSCRIPTION_ID";
        int timeoutSeconds = 5;
    
        // The `ProjectSubscriptionName.of` method creates a fully qualified identifier
        // in the form `projects/{projectId}/subscriptions/{subscriptionId}`.
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage pubsubMessage, AckReplyConsumer consumer) -> {
              try {
                DataProfilePubSubMessage message = DataProfilePubSubMessage.parseFrom(
                    pubsubMessage.getData());
                System.out.println(
                    "PubsubMessage with ID: " + pubsubMessage.getMessageId()
                        + "; message size: " + pubsubMessage.getData().size()
                        + "; event: " + message.getEvent()
                        + "; profile name: " + message.getProfile().getName()
                        + "; full resource: " + message.getProfile().getFullResource());
                consumer.ack();
              } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
              }
            };
    
        // Create subscriber client.
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver).build();
        try {
          [ApiService](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiService.html) apiService = subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)();
          apiService.[awaitRunning](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiService.html#com_google_api_core_ApiService_awaitRunning__)();
          System.out.printf("Listening for messages on %s for %d seconds.%n", subscriptionName,
              timeoutSeconds);
          subscriber.awaitTerminated(timeoutSeconds, TimeUnit.SECONDS);
        } catch (TimeoutException ignored) {
        } finally {
          subscriber.stopAsync();
        }
      }
    }
    
    

### Python
    
    
    from google.cloud import pubsub_v1
    from concurrent.futures import TimeoutError
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    
    project_id = "PROJECT_ID"
    subscription_id = "SUBSCRIPTION_ID"
    timeout = 5.0
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        print(f"Received {message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}.")
        dlp_msg = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DataProfilePubSubMessage](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataProfilePubSubMessage.html)()
        dlp_msg._pb.ParseFromString(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
        print("Parsed message: ", dlp_msg)
        print("--------")
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path} for {[timeout](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html#google_cloud_pubsub_v1_types_PublisherOptions_timeout)} seconds...")
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.
            print("Done waiting.")
    

## What's next

  * Learn more about [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles "Data profiles for BigQuery data").
  * Learn how to create a scan configuration at the [organization, folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder "Profile data in an organization or folder") or [project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project "Profile data in a single project") level.
  * Work through a [tutorial that demonstrates how to write, deploy, and trigger a simple event-driven Cloud Run function with a Pub/Sub trigger](https://docs.cloud.google.com/functions/docs/tutorials/pubsub "Pub/Sub tutorial \(2nd gen\)").



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
