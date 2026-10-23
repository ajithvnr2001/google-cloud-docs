---
url: https://docs.cloud.google.com/pubsub/docs/troubleshoot-bigtable-subscriptions/
title: Troubleshoot Bigtable subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:04.692328+00:00
---

# Troubleshoot Bigtable subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/troubleshoot-bigtable-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshoot Bigtable subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides troubleshooting tips for [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions).

## Unable to create or update subscription

When you try to create or update a Bigtable subscription, you might encounter the following errors.

### Permission denied error

If the Bigtable instance or table doesn't exist, or the configured service account doesn't have access to either, you receive a permission denied error.

To resolve the issue:

  * Check that the instance and table exist. For more information, see the following documents:

    * [Get instance information](https://docs.cloud.google.com/bigtable/docs/get-instance-information)
    * [View information about a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#view_information_about_a_table)
  * If they don't exist, create them and retry creating your subscription. For an example of this step, see [Write from Pub/Sub to Bigtable](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription#example).

  * If you still get this error, check whether the service account has the correct permissions. For more information, see [Grant IAM roles to the service account](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription#service-account-roles).




### Missing column families

If the Bigtable table doesn't have the correct column families, you receive an `INCOMPATIBLE_BIGTABLE_SCHEMA` error.

This error can be caused by the following issues:

  * The table doesn't have a `data` column family.
  * [Writing metadata](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription#message-metadata) is enabled, and the table doesn't have a `pubsub_metadata` column family.



To resolve the issue, create the necessary column families. For more information, see [Add column families](https://docs.cloud.google.com/bigtable/docs/managing-tables#add-column-families).

## The subscription isn't writing data

If a Bigtable subscription is not writing data, check the subscription state by running the [`gcloud beta pubsub subscriptions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/describe) command:
    
    
    gcloud beta pubsub subscriptions describe SUBSCRIPTION_ID
    

Replace SUBSCRIPTION_ID with the name of the subscription.

The `bigtableConfig.state` field contains the state. If the subscription is ready to write messages to Bigtable, the state is `ACTIVE`. Otherwise, there is an error in the configuration that prevents the subscription from writing messages to the Bigtable table.

Configuration issues might include the following:

  * The app profile isn't configured for [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster).

  * Permission errors. See Permission denied error.

  * The Bigtable table is missing a required column family. See Missing column families.

  * The subscription can't write to the Bigtable table due to a [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). This error occurs if `enforceInTransit` is `True` and the table location is not in an allowed region.




While a subscription is in an error state, it doesn't write messages to the Bigtable table. The messages remain in the subscription backlog; they aren't delivered to the [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic), if one is configured. Unacknowledged messages are retained for the subscription's [message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration).

After the issue is resolved, the subscription eventually returns to a healthy state.

## Increasing backlog

If your subscription state is `ACTIVE` but there is an increasing backlog of messages in the subscription, or messages are going to the subscription's dead letter topic, look for the following issues.

### Publish rate exceeds capacity

If the rate of publishing messages to your topic exceeds the capacity of your Bigtable cluster, backlogs might build up in the subscription.

[Message ordering](https://docs.cloud.google.com/pubsub/docs/ordering) comes with performance tradeoffs. Using Bigtable subscriptions with ordering might lead to lower throughput or higher message delivery latency. If you see performance problems with ordering enabled, make sure to use adequately granular ordering keys to avoid hot keys, or modify your application to not require ordering. For more information, see [Considerations when using ordered messaging](https://docs.cloud.google.com/pubsub/docs/ordering#considerations_when_using_ordered_messaging).

Monitor the performance of your cluster and consider increasing your cluster size. For more information, see the following topics in the Bigtable documentation:

  * [Monitoring Bigtable](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)
  * [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance)



### Cross-region traffic

If your application publishes to your topic from a different region than the Bigtable cluster, it takes longer for each message to get published, compared to publishing from the same region. The longer publishing time reduces the rate at which your subscription writes messages to Bigtable, reducing total throughput.

To minimize how long it takes for messages to get published, you should publish them in the same region as your Bigtable cluster.

## What's next

  * If you still have issues with your Bigtable subscription, see [Getting support](https://docs.cloud.google.com/pubsub/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
