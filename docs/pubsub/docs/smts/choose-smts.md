---
url: https://docs.cloud.google.com/pubsub/docs/smts/choose-smts/
title: Choose topic or subscription SMTs \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:05.386327+00:00
---

# Choose topic or subscription SMTs  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/choose-smts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Choose topic or subscription SMTs Stay organized with collections  Save and categorize content based on your preferences. 

Single message transforms (SMTs) can be set as properties of topics or subscriptions.

  * A topic SMT applies transformations to the messages before the messages are persisted for a topic.

  * A subscription SMT applies transformations to the messages before the messages are delivered to a subscription.




The following are some reasons for applying an SMT to a topic instead of a subscription:

  * **You want multiple subscriptions on the same topic to receive the transformed message**. If all subscriptions on a topic are supposed to receive the transformed message, then it is better to apply the transformation one time on the publish side.

  * **You want to minimize storage, inter-region delivery, and subscriber delivery costs**. If you remove unnecessary fields from a message using an SMT defined on a topic, then all subsequent data processing and delivery operations benefit from the reduced message footprint.

  * **You want to handle invalid messages at publish time.** If you use an SMT on a topic to validate messages, then any publish with an invalid message is going to fail. You can decide in the publisher how to handle these failures.




The following are some reasons for applying an SMT to a subscription instead of a topic:

  * **You only need transformations for a single subscription.** A subscription SMT is useful when you only need transformations for a single subscription.

  * **You want to write invalid messages to a dead-letter topic.** You can also use subscription SMTs with dead-letter topics to archive failed transformations. The errors result in messages being routed to the designated dead-letter topic.




You can combine topic and subscription SMTs to perform independent transformations on a single message.

## What's next

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)

  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
