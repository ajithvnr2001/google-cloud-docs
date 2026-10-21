---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/overview/
title: Introduction to Vertex AI Feature Store (Legacy) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:50:49.774824+00:00
---

# Introduction to Vertex AI Feature Store (Legacy)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/overview/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Introduction to Vertex AI Feature Store (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

Vertex AI Feature Store (Legacy) provides a centralized repository for organizing, storing, and serving ML features. Using a central featurestore enables an organization to efficiently share, discover, and re-use ML features at scale, which can increase the velocity of developing and deploying new ML applications.

Vertex AI Feature Store (Legacy) is a fully managed solution, which manages and scales the underlying infrastructure such as storage and compute resources. This solution means that data scientists can focus on the feature computation logic instead of worrying about the challenges of deploying features into production.

Vertex AI Feature Store (Legacy) is an integrated part of Vertex AI. You can use Vertex AI Feature Store (Legacy) independently or as part of Vertex AI workflows. For example, you can fetch data from Vertex AI Feature Store (Legacy) to train custom or AutoML models in Vertex AI.

Vertex AI Feature Store (Legacy) is the predecessor of Vertex AI Feature Store. To learn more about Vertex AI Feature Store, see the [Vertex AI Feature Store documentation](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).

## Overview

Use Vertex AI Feature Store (Legacy) to create and manage _featurestores_ , _entity types_ , and _features_. A featurestore is a top-level container for your features and their values. When you set up a featurestore, permitted users can add and share their features without additional engineering support. Users can define features and then import (ingest) feature values from various data sources. [Learn more about Vertex AI Feature Store (Legacy) data model and resources](https://docs.cloud.google.com/vertex-ai/docs/featurestore/concepts).

Any permitted user can search and retrieve values from the featurestore. For example, you can find features and then do a batch export to get training data for ML model creation. You can also retrieve feature values in real time to perform fast online predictions.

## Benefits

Before using Vertex AI Feature Store (Legacy), you might have computed feature values and saved them in various locations such as tables in BigQuery and as files in Cloud Storage. Moreover, you might have built and managed separate solutions for storage and the consumption of feature values. In contrast, Vertex AI Feature Store (Legacy) provides a unified solution for batch and online storage as well as the serving of ML features. The following sections details the benefits that Vertex AI Feature Store (Legacy) provides.

### Share features across your organization

If you produce features in a featurestore, you can quickly share them with others for training or serving tasks. Teams don't need to re-engineer features for different projects or use cases. Also, because you can manage and serve features from a central repository, you can maintain consistency across your organization and reduce duplicate efforts, particularly for high value features.

Vertex AI Feature Store (Legacy) provides search and filter capabilities so that others discover and reuse existing features. For each feature, you can view relevant metadata to determine the quality and usage patterns of the feature. For example, you can view the fraction of entities that have a valid value for a feature (also known as _feature coverage_) and the statistical distribution of feature values.

### Managed solution for online serving at scale

Vertex AI Feature Store (Legacy) provides a managed solution for online feature serving (low-latency serving), which is critical for making timely online predictions. You don't need to build and operate low-latency data serving infrastructure; Vertex AI Feature Store (Legacy) does this for you and scales as needed. You code the logic to generate features but offload the task of serving features. All of this included management reduces the friction for building new features, enabling data scientists to do their work without worrying about deployment.

### Mitigate training-serving skew

_Training-serving skew_ occurs when the feature data distribution that you use in production differs from the feature data distribution that was used to train your model. This skew often results in discrepancies between a model's performance during training and its performance in production. The following examples describe how Vertex AI Feature Store (Legacy) can address potential sources of training-serving skew:

  * Vertex AI Feature Store (Legacy) ensures that a feature value is imported once into a featurestore and that same value is reused for both training and serving. Without a featurestore, you might have different code paths for generating features between training and serving. So, feature values might differ between training and serving.
  * Vertex AI Feature Store (Legacy) provides point-in-time lookups to fetch historical data for training. With these lookups, you can mitigate data leakage by fetching only the feature values that were available before a prediction and not after.



For more information about how to detect training-serving skew, see [View feature value anomalies](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#view_feature_value_anomalies).

### Detect drift

Vertex AI Feature Store (Legacy) helps you detect significant changes to your feature data distribution over time, also known as _drift_. Vertex AI Feature Store (Legacy) constantly tracks the distribution of feature values that are imported into the featurestore. As feature drift increases, you might need to retrain models that are using the affected features. For more information about how to detect drift, see [View feature value anomalies](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#view_feature_value_anomalies).

## Quotas and limits

Vertex AI Feature Store (Legacy) enforces quotas and limits to help you manage resources by setting your own usage limits and to protect the community of Google Cloud users by preventing unforeseen spikes in usage. To prevent you from hitting unplanned constraints, review Vertex AI Feature Store (Legacy) quotas on the [Quotas and limits](https://docs.cloud.google.com/vertex-ai/quotas#featurestore) page. For example, Vertex AI Feature Store (Legacy) sets a quota on the number of online serving nodes and a quota on the number of online serving requests that you can make per minute.

## Data retention

Vertex AI Feature Store (Legacy) keeps feature values up to the [data retention limit](https://docs.cloud.google.com/vertex-ai/quotas#featurestore). This limit is based on the timestamp associated with the feature values, not when the values were imported. Vertex AI Feature Store (Legacy) schedules to delete values with timestamps that exceed the limit.

## Pricing

Vertex AI Feature Store (Legacy) pricing is based on several factors, such as how much data you store and the number of featurestore online nodes you use. Charges start right after you create a featurestore. For more information, see [Vertex AI Feature Store (Legacy) pricing](https://docs.cloud.google.com/vertex-ai/pricing#featurestore).

## What's next

  * Learn about the Vertex AI Feature Store (Legacy) [data model and its resources](https://docs.cloud.google.com/vertex-ai/docs/featurestore/concepts).
  * Learn [how to set up a project and set Identity and Access Management permissions for Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup).
  * View Vertex AI Feature Store (Legacy) quotas on the [Quotas and limits page](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
