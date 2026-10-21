---
url: https://docs.cloud.google.com/pubsub/docs/labels/
title: Reporting usage with labels \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:09.476197+00:00
---

# Reporting usage with labels  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Reporting usage with labels Stay organized with collections  Save and categorize content based on your preferences. 

Labels in Pub/Sub help you with cost management and resource organization. For example, imagine you have multiple subscriptions for different types of news updates. You can label each subscription with a relevant category, such as `news_category=sports` or `news_category=entertainment`.

**Note:** Reporting usage with labels is not supported for fees related to Pub/Sub data transfer costs. For cost management of data transfer costs, consider using [tags](https://docs.cloud.google.com/pubsub/docs/tags), which support [detailed usage cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## What are labels?

A label is a key-value pair that you can assign to Google Cloud resources. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

## Requirements for labels

The labels applied to a resource must meet the following requirements:

  * Each resource can have up to 64 labels.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. Keys must start with a lowercase letter or international character.
  * The key portion of a label must be unique within a single resource. However, you can use the same key with multiple resources.



These limits apply to the key and value for each label, and to the individual Google Cloud resources that have labels. There is no limit on how many labels you can apply across all resources within a project.

## Common uses of labels

Here are some common use cases for labels:

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish resources owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Managing labels in Pub/Sub

In Pub/Sub, labels are often used to organize [fees](https://cloud.google.com/pubsub/pricing) for a given billing account. Fees are associated with the billing account of the project that contains the requested resource, but you might want to establish additional associations. For example, a subscription that belongs to one project might be created for a topic that belongs to a different project. You can use labels to associate that topic and subscription with a common cost center.

**Note:** While you can use labels to organize fees by billing account, no additional fees are charged for the use of Pub/Sub labels.

Pub/Sub resources don't inherit labels from each other. In the preceding example, you would set the same label on both the topic and the subscription in order to associate those charges.

You can use the following features to apply labels to Pub/Sub resources:

  * The [Google Cloud console](https://console.cloud.google.com/cloudpubsub): Select a resource and change to the **LABELS** tab.
  * [Pub/Sub Client Libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) (specifically [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview) and [Python](https://docs.cloud.google.com/python/docs/reference/pubsub/latest)).
  * The [Google Cloud CLI for Pub/Sub](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub). For example, see the [create topic](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
