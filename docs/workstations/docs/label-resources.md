---
url: https://docs.cloud.google.com/workstations/docs/label-resources/
title: Label Cloud Workstations resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:57.460585+00:00
---

# Label Cloud Workstations resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/label-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Label Cloud Workstations resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use labels with Cloud Workstations resources. 

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




\+ **Virtual machine labels** : A label can be attached to a virtual machine. Virtual machine tags that you defined in the past appear as a label without a value. 

**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

For more information about Google Cloud labels, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources#filter).

For more information about tagging Cloud Workstations resources, see [Tag Cloud Workstations resources](https://docs.cloud.google.com/workstations/docs/tags).

## Cloud Workstations resource labels

Cloud Workstations automatically applies the following labels to all resources:

  * `workstation_cluster_id`
  * `workstation_config_id`
  * `workstation_id`
  * `workstation_location`
  * `goog-drz-workstation-location`
  * `goog-drz-workstation-uuid`
  * `goog-workstations`



## Custom Cloud Workstations labels

You can also add your custom labels to workstation clusters, workstation configurations and workstations, which recursively applies them to all underlying Compute Engine resources, although not to the underlying Cloud Workstations API resources. To label Compute Engine resources for individual workstations, be sure to add labels for each individual workstation.

Use the `labels` field when calling the [Cloud Workstations API](https://docs.cloud.google.com/workstations/docs/apis).

For example, in the sample `config.json` file that follows, `webserver` is a key and `backend` is the corresponding value. Similarly, `media` is a key and `images` is the corresponding value.
    
    
        {
          "idleTimeout": "7200s",
          "host": {
            "gce_instance": {
              "machine_type": "e2-standard-8",
              "pool_size": 1
            }
          },
          "persistentDirectories": [
            {
            "mountPath": "/home",
            "gcePd": {
              "sizeGb": 200,
              "fsType": "ext4"
            }
          }
          ],
          "labels": {
            "webserver": "backend",
            "media": "images"
          }
        }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
