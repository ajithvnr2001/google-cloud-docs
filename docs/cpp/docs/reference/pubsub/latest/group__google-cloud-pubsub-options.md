---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/group__google-cloud-pubsub-options/
title: Pub/Sub Client Library Configuration Options (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:35.288725+00:00
---

# Pub/Sub Client Library Configuration Options (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/group__google-cloud-pubsub-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Pub/Sub Client Library Configuration Options (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

# Pub/Sub Client Library Configuration Options

The Pub/Sub client library uses the same mechanism as all other C++ client libraries for configuration. As usual for the C++ client libraries, it adds a number of unique options only applicable for the Pub/Sub library.

###### See Also

[Client Library Configuration](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options.html) \- for an overview of client library configuration. 

### Classes

  * [`google::cloud::pubsub_admin::SubscriptionAdminRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1SubscriptionAdminRetryPolicyOption)
  * [`google::cloud::pubsub_admin::SubscriptionAdminBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1SubscriptionAdminBackoffPolicyOption)
  * [`google::cloud::pubsub_admin::SubscriptionAdminConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1SubscriptionAdminConnectionIdempotencyPolicyOption)
  * [`google::cloud::pubsub_admin::TopicAdminRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1TopicAdminRetryPolicyOption)
  * [`google::cloud::pubsub_admin::TopicAdminBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1TopicAdminBackoffPolicyOption)
  * [`google::cloud::pubsub_admin::TopicAdminConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub__admin_1_1TopicAdminConnectionIdempotencyPolicyOption)
  * [`google::cloud::pubsub::RetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1RetryPolicyOption)
  * [`google::cloud::pubsub::BackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1BackoffPolicyOption)
  * [`google::cloud::pubsub::MaxHoldTimeOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxHoldTimeOption)
  * [`google::cloud::pubsub::MaxBatchMessagesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxBatchMessagesOption)
  * [`google::cloud::pubsub::MaxBatchBytesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxBatchBytesOption)
  * [`google::cloud::pubsub::MaxPendingMessagesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxPendingMessagesOption)
  * [`google::cloud::pubsub::MaxPendingBytesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxPendingBytesOption)
  * [`google::cloud::pubsub::MessageOrderingOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MessageOrderingOption)
  * [`google::cloud::pubsub::FullPublisherActionOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1FullPublisherActionOption)
  * [`google::cloud::pubsub::CompressionThresholdOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1CompressionThresholdOption)
  * [`google::cloud::pubsub::CompressionAlgorithmOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1CompressionAlgorithmOption)
  * [`google::cloud::pubsub::MaxOtelLinkCountOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxOtelLinkCountOption)
  * [`google::cloud::pubsub::MaxDeadlineTimeOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxDeadlineTimeOption)
  * [`google::cloud::pubsub::MaxDeadlineExtensionOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxDeadlineExtensionOption)
  * [`google::cloud::pubsub::MinDeadlineExtensionOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MinDeadlineExtensionOption)
  * [`google::cloud::pubsub::MaxOutstandingMessagesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxOutstandingMessagesOption)
  * [`google::cloud::pubsub::MaxOutstandingBytesOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxOutstandingBytesOption)
  * [`google::cloud::pubsub::MaxConcurrencyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxConcurrencyOption)
  * [`google::cloud::pubsub::ShutdownPollingPeriodOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1ShutdownPollingPeriodOption)
  * [`google::cloud::pubsub::SubscriptionOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1SubscriptionOption)
  * [`google::cloud::pubsub::SchemaServiceRetryPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1SchemaServiceRetryPolicyOption)
  * [`google::cloud::pubsub::SchemaServiceBackoffPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1SchemaServiceBackoffPolicyOption)
  * [`google::cloud::pubsub::SchemaServiceConnectionIdempotencyPolicyOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1SchemaServiceConnectionIdempotencyPolicyOption)



### Functions

  * [`IAMPolicyOptions(Options)`](about:invalid#zCSafez)



### Types

  * [`SubscriptionAdminPolicyOptionList`](about:invalid#zCSafez)
  * [`TopicAdminPolicyOptionList`](about:invalid#zCSafez)
  * [`SubscriberOptionList`](about:invalid#zCSafez)
  * [`SchemaServicePolicyOptionList`](about:invalid#zCSafez)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
