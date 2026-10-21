---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices/
title: Best practices for Vertex AI Feature Store (Legacy) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:20:19.747743+00:00
---

# Best practices for Vertex AI Feature Store (Legacy)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Best practices for Vertex AI Feature Store (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

The following best practices will help you plan and use Vertex AI Feature Store (Legacy) in various scenarios. This guide is not intended to be exhaustive.

## Model features that jointly describe multiple entities

Some features might apply to multiple entity types. For example, you might have a calculated value that records clicks per product by user. This feature jointly describes product-user pairs.

The best practice, in this case, is to create a separate entity type to group shared features. You can create an entity type, such as `product-user`, to contain shared features.

For the entity IDs, concatenate the IDs of the individual entities, such as the entity IDs of the individual product and user. The only requirement is that the IDs must be strings. These combined entity types are referred to as _composite entity types_.

For more information, see [creating an entity type](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-entity-types#create).

## Use IAM policies to control access across multiple teams

Use IAM roles and policies to set different levels of access to different groups of users. For example, ML researchers, data scientists, DevOps, and site reliability engineers all require access to the same featurestore, but their level of access can differ. For example, DevOps users might require permissions to manage a featurestore, but they don't require access to the contents of the featurestore.

You can also restrict access to a particular featurestore or entity type by using [resource-level IAM policies](https://docs.cloud.google.com/vertex-ai/docs/featurestore/resource-policy).

As an example, imagine that your organization includes the following personas. Because each persona requires a different level of access, each persona is assigned a different [predefined IAM role](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#predefined-roles). You can also create and use your own custom roles.

Persona | Description | Predefined role  
---|---|---  
ML researcher or business analyst | Users who only view data on specific entity types | `roles/aiplatform.featurestoreDataViewer` (can be granted at the project or resource level)  
Data scientists or data engineers | Users who work with specific entity type resources. For the resources they own, they can delegate access to other principals. | `roles/aiplatform.entityTypeOwner` (can be granted at the project or resource level)  
IT or DevOps | Users who must maintain and tune the performance of specific featurestores but don't require access to the data. | `roles/aiplatform.featurestoreInstanceCreator` (can be granted at the project or resource level)  
Automated data import pipeline | Applications that write data to specific entity types. | `roles/aiplatform.featurestoreDataWriter` (can be granted at the project or resource level)  
Site reliability engineer | Users who manage particular featurestores or all featurestores in a project | `roles/aiplatform.featurestoreAdmin` (can be granted at the project or resource level)  
Global (any Vertex AI Feature Store (Legacy) user) | Allow users to view and search for existing features. If they find a feature they want to work with, they can request access from the feature owners. For Google Cloud console users, this role is also required to view the Vertex AI Feature Store (Legacy) landing page, import jobs page, and batch serving jobs page. | Grant the `roles/aiplatform.featurestoreResourceViewer` role at the project level.  
  
## Monitor and tune resources accordingly to optimize batch import

Batch import jobs require workers to process and write data, which can increase the CPU utilization of your featurestore and affect online serving performance. If preserving online serving performance is a priority, start with one worker for every ten online serving nodes. During import, monitor the CPU usage of the online storage. If CPU usage is lower than expected, increase the number of workers for future batch import jobs to increase throughput. If CPU usage is higher than expected, increase the number of online serving nodes to increase CPU capacity or lower the batch import worker count, both of which can lower CPU usage.

If you do increase the number of online serving nodes, note that Vertex AI Feature Store (Legacy) takes roughly 15 minutes to reach optimal performance after you make the update.

For more information, see [update a featurestore](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#update) and [batch import feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch).

For more information about featurestore monitoring, see [Cloud Monitoring metrics](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics).

## Use the `disableOnlineServing` field when backfilling historical data

Backfilling is the process of importing historical feature values and don't impact the most recent feature values. In this case, you can disable online serving, which skips any changes to the [online store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#storage). For more information, see [Backfill historical data](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch#backfill).

## Use autoscaling to reduce costs during load fluctuations

If you use Vertex AI Feature Store (Legacy) extensively and encounter frequent load fluctuations in your traffic patterns, use autoscaling to optimize costs. Autoscaling lets Vertex AI Feature Store (Legacy) review traffic patterns and automatically adjust the number of nodes up or down depending on CPU utilization, instead of maintaining a high node count. This option works well for traffic patterns that encounter gradual growth and decline.

**Caution:** Autoscaling is not effective for managing sudden bursts of traffic. For more information, see [Additional considerations for autoscaling](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#additional_considerations).   
If you are expecting sudden bursts of traffic, set the `minNodeCount` flag to a threshold that is high enough to handle the bursts. For more information, see [Scaling](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores#scaling) in the [API reference](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores#scaling).

For more information about autoscaling, see [Scaling options](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#scaling_options).

## Test the performance of online serving nodes for real-time serving

You can verify the performance of your featurestore during real-time online serving by testing the performance of your online serving nodes. You can perform these tests based on various benchmarking parameters, such as QPS, latency, and API. Follow these guidelines to test the performance of online serving nodes:

  * **Run all test clients from the same region, preferably on Compute Engine or Google Kubernetes Engine** : This prevents discrepancies due to network latency resulting from hops across regions.

  * **Use the gRPC API in the SDK** : The gRPC API performs better than the REST API. If you need to use the REST API, enable the HTTP keep-alive option to reuse HTTP connections. Otherwise, each request results in the creation of a new HTTP connection, which increases the latency.

  * **Run longer duration tests** : Run tests with longer duration (15 minutes or more) and a minimum of 5 QPS to calculate more accurate metrics.

  * **Add a "warm-up" period** : If you start testing after a period of inactivity, you might observe high latency while connections are reestablished. To account for the initial period of high latency, you can designate this period as a "warm-up period", when the initial data reads are ignored. As an alternative, you can send a low but consistent rate of artificial traffic to the featurestore to keep the connection active.

  * **If required, enable autoscaling** : If you anticipate gradual growth and decline in your online traffic, enable autoscaling. If you choose autoscaling, Vertex AI automatically changes the number of online serving nodes based on CPU utilization.




For more information about online serving, see [Online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online). For more information about online serving nodes, see [Online serving nodes](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#onlineservingnodes).

## Specify a start time to optimize offline storage costs during batch serve and batch export

To optimize offline storage costs during batch serving and batch export, you can specify the a `startTime` in your `batchReadFeatureValues` or `exportFeatureValues` request. The request runs a query over a subset of the available feature data, based on the specified `startTime`. Otherwise, the request queries the entire available volume of feature data, resulting in high offline storage usage costs.

## What's next

Learn Vertex AI Feature Store (Legacy) [best practices for implementing custom-trained ML models on Vertex AI](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-vertex-feature-store-with-structured-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
