---
url: https://docs.cloud.google.com/datastream/docs/access-control-with-tags/
title: Access control with tags \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:19.498523+00:00
---

# Access control with tags  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/access-control-with-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Access control with tags Stay organized with collections  Save and categorize content based on your preferences. 

You can organize your Datastream private connectivity configurations, connection profiles, and streams by using [Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). Referencing inherited or directly attached tags in [Identity and Access Management (IAM) policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) lets you grant conditional access across the Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

Tags work independently of [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels), which let you filter Datastream resources such as [connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles) and [streams](https://docs.cloud.google.com/datastream/docs/create-a-stream). You can apply both to the same resource. To attach, detach, and list tags on your Datastream resources using the Google Cloud CLI, see [Manage tags](https://docs.cloud.google.com/datastream/docs/manage-tags).

## What are tags?

Tags are key-value pairs you can apply to your Datastream resources for fine-grained access control.

A tag key could be a property, such as `environment`, and the tag value could be an attribute, such as `development` or `production`. A tag can have only one value for a given key on a particular resource.

Tags are created at the organization level. Tags are attached to resources, such as a project or a Datastream private connectivity configuration, connection profile, or stream, through the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview), which is used across Google Cloud.

## Grant permissions based on conditional tag bindings

After a tag is attached to or inherited by a Datastream resource, you can [use the tag](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags) with IAM Conditions to grant access to Datastream resources conditionally. IAM Conditions let you impose fine-grained access control on Datastream resources. To use IAM Conditions, you reference the tag in IAM policy bindings.

## Restrictions

Tags have the following restrictions:

  * [Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) can conditionally reference tags inherited from the project level and higher, but don't support tags that are directly attached to Datastream resources.
  * [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) show the creation and deletion of tags, but entries aren't generated for attaching tags and viewing tag bindings on Datastream resources.



## What's next

  * Learn how to use Resource Manager to [create and manage tags for your Datastream resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * See specific `gcloud` commands to attach, detach, and list tags on your Datastream resources in [Manage tags](https://docs.cloud.google.com/datastream/docs/manage-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
