---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos/
title: Label repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:31.768011+00:00
---

# Label repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Label repositories Stay organized with collections  Save and categorize content based on your preferences. 

Use labels to identify and group related repositories. You can specify multiple labels for a repository.

To group repositories and other resources across Google Cloud for reporting, auditing, and access control in your Google Cloud organization, use [tags](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos). Tags and labels work independently of each other, and you can apply both to the same repository. 

## What are labels?

A label is a key-value pair that you can assign to Google Cloud repositories. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

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

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish repositories owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Adding and updating labels

You can add one or more labels to a repository. You can also edit the value of an existing label.

To label a repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Select a repository.

  3. If the info panel next to the repository list is not open, click **Show Info Panel**.

  4. In the info panel, click the **Labels** tab.

  5. Add or edit labels:

     1. To add a label, click **Add Label**. Specify the key and value pair for the label, then click **Save**.
     2. To edit an existing label, change the value for the label, then click **Save**.



###  gcloud 

You can specify one or more labels to add or edit.

  * If a label exists, the corresponding value is updated.
  * If a label does not exist, the label is created.
  * If the command also includes the `--clear-labels` flag, all existing labels are removed before adding new labels.



Run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY [--project=PROJECT] \
    [--location=LOCATION] --update-labels="KEY=VALUE,..."
    

Replace the following:

  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.
  * `PROJECT` is the Google Cloud project ID. If this flag is omitted, then the current or default project is used.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. You can omit the `--location` flag to use the default.
  * `KEY=VALUE,...` is a list of comma-separated labels specified as key-value pairs. For example: `team=team-1,product=example_product,stage=development`.



For more information about the command, run the following command:
    
    
    gcloud artifacts repositories update --help
    

## Filtering repositories by label

You can filter repository lists by label in Google Cloud console or using Google Cloud CLI.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the **Filter** field, select **Labels** as the filter criteria and then enter your key, value, or key-value pair.

For example, to show only repositories with the label `env:dev`, you can enter any of the following:

     * Enter the key: `env`
     * Enter the value: `dev`
     * Enter the key-value pair: `env:dev`



###  gcloud 

To filter based on labels, use the `--filter` flag with the [gcloud artifacts repositories list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list) command.

The value of `--filter` flag must be in the `labels.KEY=VALUE` format. For example, if you wanted to filter repositories in the active project on a label with `env` as the key and `dev` as the value, you can run this command:
    
    
    gcloud artifacts repositories list --filter labels.env=dev
    

For more information about the filter syntax in the gcloud CLI, see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

## Deleting labels

To delete labels:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Select a repository**.

  3. If the info panel next to the repository list is not open, click **Show Info Panel**.

  4. In the info panel, click the **Labels** tab.

  5. Click **Delete Item** next to the label that you want to remove.




###  gcloud 

You can delete specific labels or remove all labels for a repository.

To remove specific labels, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY [--project=PROJECT] \
    [--location=LOCATION] --remove-labels="LABEL,..."
    

To remove all labels, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY \
    [--project=PROJECT] [--location=LOCATION] --clear-labels
    

Replace the following:

  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.
  * `PROJECT` is the Google Cloud project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.
  * `LABEL`,... is a list of comma-separated labels, the keys from each `KEY=VALUE` pair. For example: `team,product`.



For more information about the command, run the following command:
    
    
       gcloud artifacts repositories update --help
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
