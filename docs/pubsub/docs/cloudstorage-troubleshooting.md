---
url: https://docs.cloud.google.com/pubsub/docs/cloudstorage-troubleshooting/
title: Troubleshooting Cloud Storage subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:05.935853+00:00
---

# Troubleshooting Cloud Storage subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/cloudstorage-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting Cloud Storage subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides some common troubleshooting tips for Cloud Storage subscriptions.

## Check the state of a Cloud Storage subscription

To check the state of a subscription, perform the following steps:

  1. In the Google Cloud console, go to the Pub/Sub subscription page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Check the icon for **State** for your Cloud Storage subscription.

     * If the icon is a green check mark, the subscription is healthy.

     * If the icon is a red exclamation mark, the subscription is in an error state.

  3. Click the Cloud Storage subscription.

The subscription details page opens.

  4. Check **Subscription state** for the error message.

  5. Depending on the error message, go to the relevant section in this page for troubleshooting the issue.




After the issue is resolved, the subscription eventually returns to a healthy state.

## Unable to create or update subscription

These are some of the common issues you could face if you're having trouble creating or updating a Cloud Storage subscription.

### Bucket not found error

If the bucket that you specify in the create or update subscription workflow does not exist, then the workflow returns a `bucket not found` error. In the Google Cloud console, the message is similar to the following:
    
    
    The Cloud Storage bucket specified cannot be found.
    

To resolve the issue, [create](https://docs.cloud.google.com/storage/docs/creating-buckets) the bucket or update your Cloud Storage subscription to use an existing bucket.

### Service account error

If you have not configured the Pub/Sub service account with the right permissions, then the create or update subscription workflow returns an error. In the Google Cloud console, the message is similar to the following:
    
    
    Cloud Pub/Sub did not have the necessary permissions configured to access
    the provided bucket my-bucket (or the bucket may not exist).
    Please verify that the service account
    service-112233445566@gcp-sa-pubsub.iam.gserviceaccount.com
    was granted the Storage Legacy Bucket Reader and Storage Object Creator
    roles for the provided bucket.
    

To resolve the issue, check if the service account has the [correct permissions](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription#service-account-roles).

## Subscription state shows a red exclamation

If you edit the bucket after creating a subscription, it can affect how Pub/Sub writes messages to the bucket. If a change results in an issue, then the state field of the subscription is set to an error state.

In the subscription details page, check the state of the field `Subscription state`. The `Subscription state` field provides a more specific error, which may be one of the following:

  * **Bucket not found** : The bucket was deleted. [Create](https://docs.cloud.google.com/storage/docs/creating-buckets) the bucket again or update the subscription to use an existing bucket.

  * **Bucket permission denied** : The Pub/Sub service account no longer has permission to write to the bucket. Check if the service account has the [correct permissions](https://docs.cloud.google.com/pubsub/docs/create-subscription#service-account-roles).




While a Pub/Sub subscription is in the error state, messages are not written to the bucket and remain in the subscription backlog. Note that messages are not delivered to an attached [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic), if configured. Unacknowledged messages are retained for the period set in [`message_retention_duration`](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.Subscription.FIELDS.bool.google.pubsub.v1.Subscription.message_retention_duration) (7 days by default).

## Subscription processes messages very slowly

Some subscription settings can slow down message processing.

For example, enabling message ordering on your Cloud Storage subscription might cause messages to write to Cloud Storage but not be finalized, delaying subsequent messages with the same ordering key. For better performance, consider using a wider spectrum of ordering keys when publishing messages, or disabling message ordering if your use case does not require it.

Setting too low of a maximum file size for your Cloud Storage subscription can also negatively impact performance. Too low of a maximum file size might cause Pub/Sub to create many Cloud Storage objects with only a small number of messages in each object. The additional overhead of creating and finalizing objects slows down message processing. For better performance, consider increasing the maximum file size setting for your Cloud Storage subscription or removing the file size restriction.

### Quota limitations

Another possibility is that your project has reached its Pub/Sub push throughput quota ([`pubsub.googleapis.com/regionalpushsubscriber`](https://docs.cloud.google.com/pubsub/quotas#:%7E:text=regionalpushsubscriber)). To check if you're encountering quota limitations, examine the push requests metric ([`subscription/push_request_count`](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions)) for any `resource_exhausted` errors.

Review your project's quotas and verify that you have sufficient quota remaining. Navigate to **IAM & Admin** > **Quotas** within the project containing your Pub/Sub subscription. Search for the `pubsub.googleapis.com/regionalpushsubscriber` quota. If you are reaching the quota limit, you can [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Subscription creates more files than expected

To allow for improved scalability, your Cloud Storage subscription might be handled by multiple Pub/Sub backends. Each backend writes to a separate Cloud Storage file, so you might observe your Cloud Storage creating more files than expected, especially for low throughput workloads.

This is normal behavior. If you want to reduce the number of files created by the subscription, you can consider increasing the file batching settings on your subscription to allow for larger files. You can also post-process the files by [composing](https://docs.cloud.google.com/storage/docs/composing-objects) them into a smaller number of larger files.

## What's next

  * If you still have issues with your Cloud Storage subscription, see [Getting support](https://docs.cloud.google.com/pubsub/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
