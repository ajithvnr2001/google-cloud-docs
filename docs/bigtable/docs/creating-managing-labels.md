---
url: https://docs.cloud.google.com/bigtable/docs/creating-managing-labels/
title: Create and manage instance labels \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:40.293801+00:00
---

# Create and manage instance labels  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/creating-managing-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage instance labels

Bigtable provides the option to add labels to your instances. Labels are key-value pairs that you can use to group related instances and store metadata about an instance.

This page explains how you can use labels with your Bigtable instances. It also describes how to add, update, and remove the labels for an instance.

## What are labels?

A label is a key-value pair that you can assign to Google Cloud instances. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

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

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish instances owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Add or updating an instance's labels

After you [create a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance), you can use the Google Cloud console to add labels to the instance and update existing labels. You can also use the [RPC Admin API](https://docs.cloud.google.com/bigtable/docs/reference/admin/rpc) or the [REST Admin API](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest) to add or update labels.

To add or update labels for a Bigtable instance using the Google Cloud console:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Check the box next to each instance whose labels you want to modify.

  3. If the **Labels** panel is not visible, click **Show info panel** in the upper right corner to open it.

  4. Add and update labels as needed.

To add a new label, click **Add label** , then type the key and value for the label.

To modify an existing label, update its value. You cannot change the key for an existing label.

  5. Click **Save** to save your changes.




## Remove a label from an instance

To remove a label from a Bigtable instance using the Google Cloud console:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Check the box next to each instance whose labels you want to remove.

  3. If the **Labels** panel is not visible, click **Show info panel** in the upper right corner to open it.

  4. Click the X next to each label that you want to remove.

  5. Click **Save** to save your changes.




## What's next

  * Learn how to [modify other properties of a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance).
  * View per-instance Bigtable usage in the [Cloud Billing detailed export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
