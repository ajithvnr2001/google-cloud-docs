---
url: https://docs.cloud.google.com/datastream/docs/access-control-with-tags/
title: Access control with tags \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:57.097269+00:00
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

This page describes tags and how to use them with Datastream. To use the Google Cloud CLI to attach, detach, and list tags on your Datastream resources, see [Manage tags](https://docs.cloud.google.com/datastream/docs/manage-tags).

Tags are a way to organize your Datastream resources. These resources include private connectivity configurations, connection profiles, and streams.

Tags are applied at higher levels of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) across Google Cloud. Datastream and other resources inherit the tags. They are managed using [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). You can add a reference to tags in [Identity and Access Management (IAM) policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) to grant conditional access to resources.

Tags are different from [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels), which are another way to organize and filter your resources in Datastream. Tags and labels work independently of each other, and you can use both on the same resource. You can learn about using labels with Datastream resources, including [connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles) and [streams](https://docs.cloud.google.com/datastream/docs/create-a-stream).

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
