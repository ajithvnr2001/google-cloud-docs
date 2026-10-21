---
url: https://docs.cloud.google.com/workflows/docs/create-manage-labels/
title: Label workflows \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:13.586426+00:00
---

# Label workflows  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/create-manage-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Label workflows Stay organized with collections  Save and categorize content based on your preferences. 

Labels are key-value pairs that you can use to identify and group related workflows and store metadata about a workflow. You can specify multiple labels for a workflow.

This page explains how you can use labels with your workflows. It also describes how to add, update, and remove the labels for a workflow.

**Note:** Workflow labels are inherited by executions of the workflow.

To group workflows and other resources across Google Cloud for reporting, auditing, and access control in your Google Cloud organization, use [tags](https://docs.cloud.google.com/workflows/docs/create-manage-tags). Tags and labels work independently of each other, and you can apply both to the same workflow.

## What are labels?

A label is a key-value pair that you can assign to Google Cloud workflows. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

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

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish workflows owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Add or update labels

You can add one or more labels to a workflow when you [create a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow). You can also add or edit labels when [updating a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#update_a_workflow).

If you update an existing label, or add a new one, it can take up to 10 minutes for the new label to take effect.

## Filter workflows by label

You can search for and list specific workflows by filtering them by label.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. In the filter_list **Filter** field, select **Labels** as the filter criteria and, in the **Values** list, select a key-value pair.




###  gcloud 

Use the `--filter` flag with the [gcloud workflows list](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/list) command:
    
    
    gcloud workflows list \
        --filter labels.KEY=VALUE
    

Replace `KEY` and `VALUE` with a label key-value pair.

For more information about the filter syntax in the Google Cloud CLI, see [`gcloud topic filters`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions).

## Delete labels

You can delete a specific label using the Google Cloud console, or you can use the gcloud CLI to delete all the labels from a workflow.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update.

The **Workflow details** page appears.

  3. Click edit **Edit**.

The **Edit workflow** page appears.

  4. Next to the label that you want to remove, click delete **Delete item**.

  5. Click **Next**.

  6. To redeploy the workflow, click **Deploy**.




###  gcloud 

Use the `--labels` flag with an empty value and the [gcloud workflows deploy](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy) command:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --labels="" \
        --source=YAML_OR_JSON_SOURCE_FILE

Replace the following:

  * `WORKFLOW_NAME`: the name of your workflow.

  * `YAML_OR_JSON_SOURCE_FILE`: the source file for the workflow in either YAML or JSON format. For example: `myFirstWorkflow.yaml`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
