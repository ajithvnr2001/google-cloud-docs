---
url: https://docs.cloud.google.com/resource-manager/docs/labels-overview/
title: Overview \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:09.631029+00:00
---

# Overview  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/labels-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a brief overview of labels and its features.

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




  * **Network labels** : A label can be attached to a virtual machine. [Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) that you defined in the past will appear as a label without a value.

**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Permissions

The following permissions are required when you need to add, modify, and view labels for projects:

  * You can add or modify a label by calling the [`projects.patch()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/patch) method. This requires the `resourcemanager.projects.update` permission. 
  * You can view a project's label by calling the [`projects.get()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get) method. This requires the `resourcemanager.projects.get` permission.



## Understand costs using labels

You can attach a label to a resource and then filter resources based on their labels. Information about labels is forwarded to the billing system that allows you to [break down your billed charges](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) by label.

Here are some ways in which you can use labels to understand costs:

  * You can add labels such as `costcenter=cost_center_name`, `service=service_name`, and `environment=environment_name` to your VMs or Cloud Storage buckets. This allows you to understand where your resources are deployed, for what purpose, and the cost center to which they should be charged.
  * You can enable the [export of billing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) to BigQuery. Labels are exported to BigQuery with the corresponding Google Cloud resources and their usage. This allows you to monitor aspects such as the cost to run the shopping cart service in the application or the cost of developer test machines.
  * You can use BigQuery in combination with labels to understand the cost of all test system resources versus production resources or how much a particular service costs.



### Example

In this example, the cost of `playlist` services for a project is determined by exporting usage and labels to BigQuery. To do this, start by enabling the billing export to BigQuery. `labels-demo-prj` is the source of your resource usage and `labels_demo_bqexport` is the destination dataset where usage data is stored. After you export your usage and labels to BigQuery, you can determine how much your `playlist` service costs are. ![](https://docs.cloud.google.com/static/resource-manager/img/labels-billing-export.png)

![](https://docs.cloud.google.com/static/resource-manager/img/labels-billing-export.png)

Here are the details of the Compute Engine usage and its associated cost in BigQuery.

![](https://docs.cloud.google.com/static/resource-manager/img/labels-gce-usage-cost.png)

![](https://docs.cloud.google.com/static/resource-manager/img/labels-gce-usage-cost.png)

**Note:** When filtering your billing breakdown by label keys, you cannot select labels applied to a project. You can select other user-created labels that you'd set up and applied to Google Cloud services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
