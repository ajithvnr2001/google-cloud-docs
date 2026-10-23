---
url: https://docs.cloud.google.com/pubsub/docs/bigquery-troubleshooting/
title: Troubleshooting BigQuery subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:11.116563+00:00
---

# Troubleshooting BigQuery subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/bigquery-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting BigQuery subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides some common troubleshooting tips for BigQuery subscriptions.

## Check the state of a BigQuery subscription

To check the state of a subscription, perform the following steps:

  1. In the Google Cloud console, go to the Pub/Sub subscription page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Check the icon for **State** for your BigQuery subscription.

If the icon is a green check mark, the subscription is healthy.

If the icon is a red exclamation mark, the subscription is in an error state.

  3. Click the BigQuery subscription.

The subscription details page opens.

  4. Check **Subscription state** for the error message.

  5. Depending on the error message, go to the relevant section in this page for troubleshooting the issue.




After the issue is resolved, the subscription eventually returns to a healthy state.

## Unable to create or update subscription

These are some of the common issues you could face if you're having trouble creating or updating a BigQuery subscription.

### Table not found error

If the table that you specify in the create or update subscription workflow does not exist, then the workflow returns a table not found error. In the Google Cloud console, the message is similar to the following:
    
    
    The BigQuery table or dataset specified cannot be found.
    

To resolve the issue, [create](https://docs.cloud.google.com/bigquery/docs/tables) the table and make sure you can check its [state](https://docs.cloud.google.com/bigquery/docs/tables#get_table_information) before using it with a BigQuery subscription.

### Schema mismatch error

If the schemas of the table and the topic are not compatible, then the create or update subscription workflow returns a schema mismatch error. In the Google Cloud console, the message is similar to the following:
    
    
    Incompatible schema type for field project_ids: expected INT64, got STRING
    

The specified error message is for schema mismatch for a field called `project_ids`. Depending on the type of schema mismatch that you have, you might see a different variation of the error message.

To resolve the issue, check if the schema mappings are [compatible](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

### Service account error

If you have not configured the Pub/Sub service account with the right permissions, then the create or update subscription workflow returns an error. In the Google Cloud console, the message is similar to the following:
    
    
    Service account service-1234234234@gcp-sa-pubsub.iam.gserviceaccount.com
    is missing permissions required to write to the BigQuery table:
    bigquery.tables.get, bigquery.tables.updateData.
    

To resolve the issue, check if the service account has the [correct permissions](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#service-account-roles).

## Subscription state shows a red exclamation

If you edit the table after creating a subscription, it can affect how Pub/Sub writes messages to the table. If a change results in an issue, then the state field of the subscription is set to an error state.

In the subscription details page, check the state of the field `Subscription state`. The `Subscription state` field provides a more specific error, which may be one of the following:

  * **table not found** : The table is deleted. [Create](https://docs.cloud.google.com/bigquery/docs/tables) a table and check the state of the table. See [Get table information](https://docs.cloud.google.com/bigquery/docs/tables#get_table_information).

  * **table permission denied** : The Pub/Sub service account no longer has permission to write to the table. Check if the service account has the [correct permissions](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#service-account-roles).

  * **table schema mismatch** : The table schema is no longer compatible with the BigQuery subscription settings. Check if the schema mappings are [compatible](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).




While a Pub/Sub subscription is in the error state, messages are not written to the BigQuery table and remain in the subscription backlog. Note that messages are not delivered to an attached [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic), if configured. Unacknowledged messages are retained for the period set in [`message_retention_duration`](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.Subscription.FIELDS.bool.google.pubsub.v1.Subscription.message_retention_duration)(7d, by default).

## A backlog is building up

If you see a backlog of messages building up in the subscription or messages going to a subscription's dead-letter topic, review the following possible causes.

### INVALID_ARGUMENT error message

This error happens when the message supplied is in a format that Pub/Sub considers valid but the BigQuery destination table schema does not. This means one or more fields in the message have values that are not permissible by the BigQuery table schema. Review the [schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility) to verify that the data types and formats are correct. Some of the most common errors include:

  * An empty string (`""`) is not a valid JSON. When sending data to a nullable JSON BigQuery table column, provide either an empty JSON object `({})`, `null`, or an empty JSON string `("\"\"")` to represent missing values. Sending an empty string results in an error.

  * If a message field value exceeds the BigQuery field's maximum length, the message fails due to size limitations.




To troubleshoot `INVALID_ARGUMENT` errors, add a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) to the subscription of interest. The dead-letter topic captures messages that couldn't be written to BigQuery, along with an attribute called [`CloudPubSubDeadLetterSourceDeliveryErrorMessage`](https://docs.cloud.google.com/pubsub/docs/bigquery#handle_message_failures) that explains the failure reason.

These delivery failures can also be seen in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). Select the metric `pubsub.googleapis.com/subscription/push_request_count` and filter by `response_code=invalid_argument`.

### RESOURCE_EXHAUSTED error message

If messages are being written to BigQuery slowly, you might need to increase your project's Pub/Sub push quota or BigQuery storage write throughput quota. To check if you're encountering quota limitations, examine the push requests metric ([`subscription/push_request_count`](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions)) for any `resource_exhausted` errors.

Another way to diagnose quota issues is to check the project's quota. Navigate to **IAM & Admin** > **Quotas** within the project containing your Pub/Sub resource or BigQuery instance. Search for the relevant quota, either `pubsub.googleapis.com/regionalpushsubscriber` or `bigquerystorage.googleapis.com/write/append_bytes`. If either quota needs an increase, you can [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Hourly partitioned table showing `__UNPARTITIONED__` in partition ID column

When a BigQuery destination table is partitioned by hour, rows initially land in a special partition labeled `__UNPARTITIONED__` within the [`INFORMATION_SCHEMA.PARTITIONS` view](https://docs.cloud.google.com/bigquery/docs/information-schema-partitions). This is expected behavior for tables using [ingestion-time partitioning](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery#ingestion-time_partitioning).

BigQuery employs a streaming buffer to optimize the writing process. Data might reside in the `__UNPARTITIONED__` partition until enough volume accumulates or at least an hour has passed. After these conditions are met, BigQuery re-partitions the data into its appropriate hourly partition.

You can monitor data within the `__UNPARTITIONED__` partition using the `INFORMATION_SCHEMA.PARTITIONS` view.

## What's next

  * If you still have issues with your BigQuery subscription, see [Getting support](https://docs.cloud.google.com/pubsub/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
