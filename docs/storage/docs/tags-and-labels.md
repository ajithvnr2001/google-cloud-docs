---
url: https://docs.cloud.google.com/storage/docs/tags-and-labels/
title: Tags and labels \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:13.445557+00:00
---

# Tags and labels  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/tags-and-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Tags and labels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the tags and labels you can set on Cloud Storage resources.

## Overview

Google Cloud _tags_ and Cloud Storage _bucket labels_ are two ways to organize your Cloud Storage resources.

  * Tags can be used at higher levels of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and across Google Cloud. They are managed using the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and can be referenced in [IAM policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) to grant conditional access to resources.

  * Bucket labels are [managed](https://docs.cloud.google.com/storage/docs/using-bucket-labels) using Cloud Storage tools.




Tags and labels work independently of each other, and you can use both on the same bucket.

## Tags

Tags are key-value pairs you can apply to your resources for fine-grained access control and granular cost data at the bucket level.

Tags are created at the organization or project level and managed through the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview), which is used across Google Cloud. Once you attach a tag to a Cloud Storage bucket, you can [use the tag](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags) with [IAM Conditions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam) to grant access to resources or with [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) to enforce constraints on resources. You can also use the tag to analyze [detailed usage cost data exported to Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags).

When using tags, note the following restrictions:

  * Tags can be attached to a bucket only after the bucket has been created.

  * Tags cannot be applied to objects.

  * You can have a maximum of 50 tag bindings per bucket.




### Required permissions

Although tags are managed through the Resource Manager, you need the following IAM permissions to set and manage tags on buckets:

  * `storage.buckets.listTagBindings`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.deleteTagBinding`



These permissions can be inherited through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions), such as the Tag User (`roles/resourcemanager.tagUser`) role or the Storage Admin (`roles/storage.admin`) role.

### Examples for attaching tags to Cloud Storage buckets

Once you've [created and defined](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) a tag, you can attach the tag to your bucket.

Consider the following scenario:

  * The tag value has a namespaced name of `815471563813/color/blue`.
  * Your bucket is named `my-bucket`.
  * Your bucket is located in `us-central1`.



The following gcloud command attaches the tag to `my-bucket`:
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=815471563813/color/blue \
    --parent=//storage.googleapis.com/projects/_/buckets/my-bucket \
    --location=us-central1

The following gcloud command detaches the tag from `my-bucket`:
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=815471563813/color/blue \
    --parent=//storage.googleapis.com/projects/_/buckets/my-bucket \
    --location=us-central1

The following gcloud command lists all tags directly attached to `my-bucket`, except tags that `my-bucket` has inherited:
    
    
    gcloud resource-manager tags bindings list \
        --parent=//storage.googleapis.com/projects/_/buckets/my-bucket \
        --location=us-central1

For more detailed instructions, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).

### Pricing details for tags

Tags attached to buckets are [subject to monthly charges](https://docs.cloud.google.com/storage/pricing#tags).

## Bucket labels

Bucket _labels_ allow you to create arbitrary key:value pairs that are stored as part of the bucket's metadata. You can use labels to organize your buckets along with other Google Cloud resources such as [virtual machine instances](https://docs.cloud.google.com/compute/docs/instances). For example, say you want a key named `team` that has the values `alpha`, `beta`, and `delta`, which you will use to indicate which team is associated with certain Google Cloud resources. You can [apply the labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels) `team:alpha`, `team:beta`, and `team:delta` to the resources to achieve this.

Keep in mind the following when working with bucket labels:

  * Keys and values cannot be longer than 63 characters each.
  * Keys and values can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed.
  * Label keys must start with a lowercase letter and international characters are allowed.
  * Label keys cannot be empty.
  * Each bucket can have a maximum of 64 labels actively applied to it.
  * As is generally the case for bucket metadata, bucket labels are not associated with individual objects or object metadata.



For a general example of using labels to organize your resources in billing, see [Billing Export to BigQuery Query Examples](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

### Pricing details for labels

Labels set on buckets are not subject to monthly charges.

## What's next

  * Learn how to [use bucket tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * Learn how to [use bucket labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
