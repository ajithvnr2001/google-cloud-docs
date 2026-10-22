---
url: https://docs.cloud.google.com/iam/docs/tags-access-control/
title: Tags and conditional access \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:02.609500+00:00
---

# Tags and conditional access  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/tags-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Tags and conditional access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use tags with Identity and Access Management (IAM) to help you control access to your Google Cloud resources.

To learn more about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Overview of tags

A tag is a key-value pair that is attached to a [Google Cloud resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services#supported_service_resources). You can [conditionally grant IAM roles](https://docs.cloud.google.com/iam/docs/conditions-overview) or [conditionally deny IAM permissions](https://docs.cloud.google.com/iam/docs/deny-overview) based on whether a resource has a specific tag.

Resources [inherit tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance) from their parent organization, folders, and project. As a result, you can use tags to manage access to any Google Cloud resource.

These are some common use cases for managing access with tags:

  * **Development, staging, and production environments.** For example, you could add the tags `environment: dev` to your development environment and `environment: prod` to your production environment.
  * **Component types.** For example, you could add the tags `component: frontend` to front-end resources and `component: batch` to resources for batch processing.
  * **Project names.** For example, if your team is working on a project with the codename Atlas, you could add the tag `project: atlas` to the team's development resources.



**Important:** Do not include sensitive information in tags. Sensitive information includes personally identifiable information (PII), such as an individual's name or job title. Tags are not intended to contain sensitive information. 

## Tag definitions and identifiers

Before you attach tags to resources, you must define the key for the tag, as well as the values that the tag allows. You can create these definitions at the organization or project level. You use [Resource Manager](https://docs.cloud.google.com/resource-manager/docs) to manage tag definitions. To learn more, see [Creating and defining a new tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating).

Each tag key and value has a few different identifiers:

  * A _permanent ID_ , which is globally unique and can never be reused. For example, a tag key could have the permanent ID `tagKeys/123456789012`, and a tag value could have the permanent ID `tagValues/567890123456`. 
  * A _short name_. The short name for each key must be unique within the project or organization under which the key is defined, and the short name for each value must be unique for its associated key. For example, a tag key could have the short name `env`, and a tag value could have the short name `prod`. 
  * A _namespaced name_ , which adds your organization's numeric ID or project's ID to the short name of a tag key. For example, a tag key created for an organization could have the namespaced name `123456789012/env`. To learn how to get your organization ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). A tag key created for a project could have the namespaced name `myproject/env`. To learn how to get your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 



As explained on this page, after you attach tags to a resource, you can write conditions to grant access based on tags. To write a condition, you must choose which type of identifier to use in the condition. Follow these guidelines to choose between them:

  * **To experiment with tags,** consider using the namespaced name (for keys) and the short name (for values). These identifiers are easier to understand and remember, especially as you get started.
  * **If you manage your configuration declaratively,** using a tool such as Terraform, consider using the namespaced name (for keys) and the short name (for values). You can reuse these identifiers over time, which means that a declarative tool can delete and recreate them, and your conditions will continue to work.

This approach comes with a tradeoff: Suppose you delete a tag key or value, then create a new key or value with the same name but a different meaning. If your condition refers to the namespaced name or short name, then the condition continues to apply to the new key or value.

In some cases, this behavior might cause principals to get access that you did not intend for them to have.

  * **To help minimize risk,** consider using permanent IDs, which can never be reused.

Here's why permanent IDs help minimize risk: Suppose you delete a tag key or value, then create a new key or value with the same name but a different meaning. If your condition refers to the permanent ID, then the condition does not apply to the new key or value. As a result, principals are less likely to get access that you did not intend for them to have.

One drawback is that if you delete and recreate keys and values, and you want to preserve principals' access, you must also update your allow policies to refer to the new permanent IDs.




## Access to tagged resources

You can use tags with IAM Conditions to grant a role conditionally, depending on the tags that are attached to or inherited by a resource. If a condition evaluates to `true`, then access is granted; otherwise, access is not granted. To learn more, see the [overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

Certain areas of the Google Cloud console don't recognize allow policy role bindings with tag-based conditions. As a result, if you have a role with a tag-based condition, then the Google Cloud console might incorrectly prevent you from performing certain actions. If you encounter this issue, then use an alternate method, such as the gcloud CLI, to perform the action. 

The following sections show examples of condition expressions that check the tags on a resource. The condition calls different functions depending on whether it checks the permanent ID or the short name. To learn more about these functions, see [Resource tags](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags).

### Conditions that use permanent IDs

This condition grants a role on resources with the tag `tagKeys/123456789012: tagValues/567890123456`:
    
    
    resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')
    

This condition grants a role on resources that have any tag with the key `tagKeys/123456789012`, regardless of its value:
    
    
    resource.hasTagKeyId('tagKeys/123456789012')
    

This condition grants a role on resources that have both the tag `tagKeys/123456789012: tagValues/567890123456`, and any tag that uses the key `tagKeys/987654321098`:
    
    
    resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456') &&
        resource.hasTagKeyId('tagKeys/987654321098')
    

### Conditions that use namespaced names and short names

This condition grants a role on resources with the tag `env: prod`, indicating that the resource is in a production environment:
    
    
    resource.matchTag('123456789012/env', 'prod')
    

This condition grants a role on resources that have any tag with the key `env`, regardless of its value:
    
    
    resource.hasTagKey('123456789012/env')
    

This condition grants a role on resources that have both the tag `env: prod` and any tag that uses the key `project`:
    
    
    resource.matchTag('123456789012/env', 'prod') &&
        resource.hasTagKey('123456789012/project')
    

## What's next

  * Learn how to [manage tags and attach tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * Get details about [checking tags in a condition](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
