---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxDeadlineExtensionOption/
title: Struct MaxDeadlineExtensionOption (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:32.977598+00:00
---

# Struct MaxDeadlineExtensionOption (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxDeadlineExtensionOption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Struct MaxDeadlineExtensionOption (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The maximum time by which the deadline for each incoming message is extended. 

While waiting for an ack or nack, The Cloud Pub/Sub C++ client library will extend the deadline by at most this amount. The default extension time is 10 minutes. An application may wish to reduce this extension time so the Pub/Sub service will resend a message sooner when it does not hear back from a [Subscriber](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1Subscriber). With at-least-once semantics, making the time too short may increase the number of duplicate messages delivered by the service.

The value is clamped between 10 seconds and 10 minutes. Note that this option also affects the effective range for [`MinDeadlineExtensionOption`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MinDeadlineExtensionOption). 

## Type Aliases 

### Type

**Alias Of** : `std::chrono::seconds`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
