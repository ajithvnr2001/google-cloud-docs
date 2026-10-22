---
url: https://docs.cloud.google.com/filestore/docs/tags-and-labels/
title: Tags and labels \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:56.590077+00:00
---

# Tags and labels  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/tags-and-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Tags and labels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the tags and labels you can set on Filestore resources.

## Overview

Google Cloud _tags_ and _labels_ are two ways to organize your Filestore resources.

  * Tags can be used at higher levels of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and across Google Cloud. They are managed using the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and can be referenced in [IAM policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) to grant conditional access to resources.

  * Labels are [managed](https://docs.cloud.google.com/filestore/docs/managing-labels) using Filestore tools.




Tags and labels work independently of each other, and you can use both on the same resource.

## Tags

Tags are key-value pairs you can apply to your resources for fine-grained access control and granular cost data at the bucket level.

Tags are created at the organization or project level and managed through the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview), which is used across Google Cloud. Once you attach a tag to a Filestore resource, you can [use the tag](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags) with IAM Conditions to grant access to resources or with [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) to enforce constraints on resources. You can also use the tag to analyze [detailed usage cost data exported to Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags).

You can apply tags to Filestore instances and [backups](https://docs.cloud.google.com/filestore/docs/backups).

When using tags, note the following restrictions:

  * Tags can only be attached to a resource after the resource has been created.

  * Tags cannot be applied directly to [snapshots](https://docs.cloud.google.com/filestore/docs/snapshots), but snapshots inherit any tags set on their associated instance.

  * You can have a maximum of 50 tag bindings per resource.




Notice: Tags are immutable and cannot be edited.

If you are managing your resources with Terraform, note that Terraform destroys a resource and recreates it when trying to update an immutable parameter—the re-creation consists of deleting the resource and then creating the resource with the immutable parameter—which can result in data loss.

You are advised to enable [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection) when managing Filestore through Terraform

### Required permissions

Although tags are managed through the Resource Manager, you need the following IAM permissions to set and manage tags on Filestore resources:

  * `file.RESOURCE_TYPE.listTagBindings`
  * `file.RESOURCE_TYPE.listEffectiveTags`
  * `file.RESOURCE_TYPE.createTagBinding`
  * `file.RESOURCE_TYPE.deleteTagBinding`



`RESOURCE_TYPE` is `instances` for managing tags on instances and `backups` for managing tags on backups.

These permissions can be inherited through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions), such as the Tag User (`roles/resourcemanager.tagUser`) role or the Cloud Filestore Editor (`roles/file.editor`) role.

### Examples for attaching tags to Filestore resources

Once you've [created and defined](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) a tag, you can attach the tag to your Filestore resources.

Consider the following scenario:

  * The tag value has a namespaced name of `815471563813/color/blue`.
  * You have an instance named `my-instance`.
  * Your instance is located in `us-central1`, in a project named `my-project`.



The following `gcloud` command attaches the tag to `my-instance`:
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=815471563813/color/blue \
    --parent=//file.googleapis.com/projects/my-project/locations/us-central1/instances/my-instance \
    --location=us-central1

The following `gcloud` command detaches the tag from `my-instance`:
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=815471563813/color/blue \
    --parent=//file.googleapis.com/projects/my-project/locations/us-central1/instances/my-instance \
    --location=us-central1

The following `gcloud` command lists all tags directly attached to `my-instance`, except tags that `my-instance` has inherited:
    
    
    gcloud resource-manager tags bindings list \
    --parent=//file.googleapis.com/projects/my-project/locations/us-central1/instances/my-instance \
        --location=us-central1

For more detailed instructions, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching)

## Labels

## What are labels?

A label is a key-value pair that you can assign to Google Cloud Filestore instances. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

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

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish Filestore instances owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## What's next

  * Learn how to [use Filestore labels](https://docs.cloud.google.com/filestore/docs/managing-labels).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
