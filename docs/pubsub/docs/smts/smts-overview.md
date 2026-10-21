---
url: https://docs.cloud.google.com/pubsub/docs/smts/smts-overview/
title: Single Message Transforms (SMTs) overview \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:58.643815+00:00
---

# Single Message Transforms (SMTs) overview  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/smts-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Single Message Transforms (SMTs) overview Stay organized with collections  Save and categorize content based on your preferences. 

Most streaming data pipelines require data transformations. Some users prefer transforming data after it reaches its destination in an extract, load, transform (ELT) pipeline, while others opt for transforming data before its ingestion in an extract, transform, and load (ETL) pipeline. Traditionally, this architecture required complex pipelines with tools like Dataflow or Apache Flink to perform data transformations.

Pub/Sub offers **Single Message Transforms** (SMTs) to simplify data transformations for streaming pipelines. SMTs enable lightweight modifications to message data and attributes directly within Pub/Sub. SMTs eliminate the need for additional data processing steps or separate data transformation products.

When an SMT is run, it takes the Pub/Sub message as input, including the message data and attributes. The output is a transformed Pub/Sub message, with modifications to the data or attributes. SMTs are integrated into the Pub/Sub API, so you can manage them as part of your topic or subscription configurations.

## SMTs use cases

Consider designing an online store that wants to give customers personalized product recommendations as they browse the website. To do this, you can use Pub/Sub to collect real-time data about customer activity on the site. This includes data about the products viewed, the products added to the cart, and the ratings given to products.

However, this raw data often needs some adjustments before it can be used to generate recommendations. For example, the raw data might contain extraneous details which are irrelevant for your use case. Examples of such details are the customer's browser type or the time they visited the site. The data might also not be in the required format for the recommendation system. For example, timestamps might be in different formats, or product IDs might need to be converted to a different type.

You can use Pub/Sub SMTs to make data transformations such as the following:

  * Remove personally identifiable information (PII), such as full names and addresses, to protect customer privacy.

  * Retain only recommendation-relevant events, such as product views and purchases, and discard others, such as customer profile changes.

  * Ensure all timestamps, currency values, and product IDs adhere to a consistent format and type compatible with the recommendation system.

  * Generate new data fields from raw data, such as shopping cart total value or product page dwell time.

  * Add inferences from Gemini Enterprise Agent Platform models to event data, such as classifications, predictions, sentiments, or embeddings.




In summary, SMTs enable a wide range of use cases, including the following:

  * **Data masking and redaction** : Protect sensitive data by masking or redacting fields like credit card numbers or PII, aiding compliance with data privacy regulations.

  * **Data format conversion** : Transform data between different formats to ensure compatibility with downstream systems.

  * **Message filtering** : Process only relevant messages by filtering out unwanted messages based on content or attributes. SMTs allow for more complex filtering conditions than Pub/Sub's [built-in filters](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter).

  * **Simple data transformations** : Perform basic data manipulation tasks, such as string manipulation, date formatting, or mathematical operations.

  * **AI Inferences** : Integrate AI models seamlessly into your Pub/Sub pipelines, by using the [AI Inference](https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt) SMT.




## Types of SMTs

Pub/Sub supports the following SMTs:

  * [AI Inference](https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt): Gets inferences on Pub/Sub messages from an Agent Platform model.
  * [User Defined Functions](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview): Calls a JavaScript user-defined function (UDF) to perform custom transformations on Pub/Sub messages.



## Sample message flow for SMTs

The image shows an example Pub/Sub system with SMTs applied at both the topic and subscription levels. ![Figure showing how
  messages are impacted with topic SMT and subscription SMT.](https://docs.cloud.google.com/static/pubsub/images/smt-message-flow.png)**Figure 1** How messages are transformed with SMTs.

The following procedure shows how the messages flow in the Pub/Sub system:

  1. The publisher applications **Publisher 1** and **Publisher 2** publish messages **A** and **B** respectively to the Pub/Sub topic.

  2. The topic's SMTs transform messages **A** and **B** into messages **A'** and **B'** , respectively.

  3. If a schema is attached to the topic, the transformed messages **A'** and **B'** are validated against the schema. If, for example, **A'** does not match the schema, the publish of message **A** fails with an error.

  4. The transformed messages **A'** and **B'** are written to Pub/Sub storage.

  5. Pub/Sub delivers messages **A'** and **B'** to all attached subscriptions, which are **Subscription 1** and **Subscription 2** as shown in the image.

  6. If **Subscription 1** has a filter configured, messages **A'** and **B'** are evaluated against the filter. Only messages matching the filter proceed to the next step. Other messages are automatically acknowledged by Pub/Sub.

  7. If **Subscription 2** has a filter configured, messages **A'** and **B'** are evaluated against the filter. Only messages matching the filter proceed to the next step. Other messages are automatically acknowledged by Pub/Sub.

  8. **Subscription 1** 's SMTs transform messages **A'** and **B'**. **A'** becomes **A''** and **B'** becomes **B''**.

  9. **Subscription 2** 's SMTs transform messages **A'** and **B'**. **A'** remains as **A'** and **B'** is filtered out.

  10. If **Subscription 1** is a push subscription with payload unwrapping enabled, messages **A''** and **B''** are unwrapped. If **Subscription 2** is a push subscription with payload unwrapping enabled, **A'** is unwrapped.

  11. **Subscriber 1** receives message **B''** , **Subscriber 2** receives message **A''** , and **Subscriber 3** receives message **A'**.

  12. Subscribers acknowledge the received messages.

  13. Pub/Sub deletes the acknowledged messages from storage.




## Limitations

  * Up to 5 SMTs can be enabled on a topic or subscription.

  * SMTs operate on a single Pub/Sub message. They can't aggregate multiple Pub/Sub messages.




## What's next

  * [Choose between topic and subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/choose-smts)

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)

  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
