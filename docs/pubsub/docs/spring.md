---
url: https://docs.cloud.google.com/pubsub/docs/spring/
title: Using Pub/Sub in Spring applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:10.561411+00:00
---

# Using Pub/Sub in Spring applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/spring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Using Pub/Sub in Spring applications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Pub/Sub in Java applications built with the [Spring Framework](https://spring.io/projects/spring-framework).

[Spring Cloud GCP](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html) has several modules for sending messages to Pub/Sub topics and receiving messages from Pub/Sub subscriptions using the Spring Framework. You can use these modules independently or combine them for different use cases:

  * **Spring Cloud GCP Pub/Sub Starter** lets you send and receive messages using helper classes and call the Pub/Sub Java client library for more advanced scenarios.
  * **Spring Integration Channel Adapters for Pub/Sub** let you connect Spring Integration [Message Channels](https://docs.spring.io/spring-integration/reference/channel.html) with Pub/Sub.
  * **Spring Cloud Stream Binder for Pub/Sub** lets you use Pub/Sub as messaging middleware in Spring Cloud Stream applications.

**Note:** The [Spring Cloud GCP](https://github.com/GoogleCloudPlatform/spring-cloud-gcp/tree/main/spring-cloud-gcp-pubsub/src) library does not provide access to [AckReplyConsumerWithResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumerWithResponse), which is a required module to implement the exactly-once feature using the Java client library.

## Using Spring Cloud GCP Pub/Sub Starter

Follow [Spring Framework on Google Cloud reference guide - Cloud Pub/Sub](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html#cloud-pubsub) for further details on the Spring Cloud GCP Pub/Sub Starter and instructions on how to use it.

## Using Spring Integration channel adapters

Follow [Spring Framework on Google Cloud reference guide - Channel Adapters for Cloud Pub/Sub](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html#channel-adapters-for-cloud-pubsub) for further details on the Spring Integration channel adapters and instructions on how to use them.

## Using Spring Cloud Stream Binder

Follow [Spring Framework on Google Cloud reference guide - Spring Cloud Stream Binder for Cloud Pub/Sub](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html#spring-cloud-stream) for further details on the Spring Cloud Stream Binder and instructions on how to use it. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
