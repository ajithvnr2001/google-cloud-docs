---
url: https://docs.cloud.google.com/pubsub/docs/push-troubleshooting/
title: Troubleshooting a push subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:11.833390+00:00
---

# Troubleshooting a push subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/push-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting a push subscription Stay organized with collections  Save and categorize content based on your preferences. 

Push subscribers are a type of Pub/Sub subscriber where messages are sent from Pub/Sub to a user-specified HTTPS endpoint. The user acknowledges a pushed message by returning an HTTP 200 response to the push server's request. This document provides some common troubleshooting tips for Pub/Sub push subscriptions. Read more about push subscriptions in the [Push subscriber guide](https://docs.cloud.google.com/pubsub/docs/push).

To effectively monitor your Pub/Sub subscription, it is recommended to first look at the [delivery latency health score](https://docs.cloud.google.com/pubsub/docs/monitoring#delivery_latency_health) ([`subscription/delivery_latency_health_score`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/delivery_latency_health_score)) to check which factors could be contributing to an unexpected latency.

## Failing or slow push endpoints

If the endpoint returns an error response code, then the message delivery is considered to have failed and is retried later. This can potentially lead to the endpoint receiving duplicate messages.

There are multiple metrics that you can use to [monitor push subscriptions](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions). The [`subscription/push_request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/push_request_count) metric in Cloud Metrics categorizes responses from the push endpoint by `response_code` and `response_class`. The responses are useful for the identification of potential endpoint malfunctions. If this metric has data with a `response_class` other than `ack`, this indicates that the push endpoint is returning errors to Pub/Sub. Some of the most common errors include:

  * A `deadline_exceeded` response class indicates that the push endpoint didn't respond within the required acknowledgment (ack) deadline. The [`subscription/push_request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/push_request_latencies) metric helps to track push ack latency.

  * An `invalid` response class indicates that the endpoint sent back a response that Pub/Sub couldn't understand or process correctly.

  * A `remote_server_4xx` response class usually indicates authentication or permission issues. These are HTTP response codes returned by the endpoint, so look at the scenarios under which this response code is returned. If authentication is enabled, confirm your account has the right permission on the endpoint. Learn more about how [authentication](https://docs.cloud.google.com/pubsub/docs/create-push-subscription#authentication) works in push subscriptions.

  * A `remote_server_5xx` response class indicates a server-side problem on the endpoint side. The endpoint is unable to process the request. This might be due to an ongoing maintenance or outage. Review the status of the server hosting the endpoint.

  * An `unreachable` response class indicates that the endpoint server cannot be reached at all. Verify the endpoint URL for typos.




Learn more about the most common [error codes](https://docs.cloud.google.com/pubsub/docs/reference/error-codes) of the Pub/Sub API.

## Restrictions on push subscriptions inside a VPC-SC perimeter

If VPC Service Controls (VPC-SC) protection is enabled in a project, there are limitations on creating push subscriptions. Existing push subscriptions continue to work, but when you create a new push subscription, you see the error: `Request is prohibited by organization's policy`. Specifically, new push subscriptions can only be created if the push endpoint is a Cloud Run service using the default `run.app` URL. For more details and specific limitations, see [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs/create-push-subscription#vpc-service-control) and [VPC-SC documentation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_pubsub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
