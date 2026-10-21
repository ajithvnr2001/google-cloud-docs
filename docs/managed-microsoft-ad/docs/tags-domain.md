---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/tags-domain/
title: Attach and manage tags with domains \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:24.726058+00:00
---

# Attach and manage tags with domains  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/tags-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Attach and manage tags with domains Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to attach a tag to your existing domain in Managed Service for Microsoft Active Directory (Managed Microsoft AD), list tags attached to a domain, and remove tags from a domain.

## Overview

A tag is a key-value pair that can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant IAM roles based on whether a Managed Microsoft AD domain has a specific tag. For more information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).   


Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Before you begin

Before you begin, do the following:

  * [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).
  * Create tag keys and add tag values. For more information about creating tag keys and adding tag values, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * Get the permanent ID of tag values. Permanent ID is a unique identifier that is displayed when a tag value is added to the tag key. For more information, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * Make sure that you have the following Tag User role: `roles/resourcemanager.tagUser`. For more information about the role, see [Resource Manager roles](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager).



## Attach tags to a domain

You must create a tag binding resource to attach a tag to your Managed Microsoft AD domain.

Run the following gcloud CLI command:
    
    
    gcloud alpha resource-manager tags bindings create --tag-value=TAG_VALUE_ID --parent=DOMAIN_NAME
    

Replace the following:

  * TAG_VALUE_ID: The permanent ID or namespaced name of the tag value to be attached. For example, `tagValues/1234567890`.
  * DOMAIN_NAME: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your Managed Microsoft AD domain, in the form of: `//managedidentities.googleapis.com/projects/PROJECT_ID/locations/global/domains/DOMAIN-NAME`.



You receive the details of the tag binding created as a response.
    
    
    done: true
    response:
      '@type': type.googleapis.com/google.cloud.resourcemanager.v3.TagBinding
      name: TAG_BINDING_NAME
      parent: DOMAIN_NAME
      tagValue: TAG_VALUE_ID
    

After you create the tag binding, you can configure organization policies for these tags using conditions that define when the policy must be enforced. For more information, see [Setting an organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

## List tags attached to a domain

You can get the list of tag binding resources attached to your Managed Microsoft AD domain.

Run the following gcloud CLI command:
    
    
    gcloud alpha resource-manager tags bindings list --parent=DOMAIN_NAME
    

Replace the following:

  * DOMAIN_NAME: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your Managed Microsoft AD domain, in the form of: `//managedidentities.googleapis.com/projects/PROJECT_ID/locations/global/domains/DOMAIN-NAME`.



You receive the list of tag binding resources attached to your domain as a response.
    
    
    tagBindings:
      name: TAG_BINDING_NAME
      parent: DOMAIN_NAME
      tagValue: TAG_VALUE_ID
    

## Detach tags from a domain

You must delete the tag binding resource to detach a tag from your Managed Microsoft AD domain.

Run the following gcloud CLI command:
    
    
    gcloud alpha resource-manager tags bindings delete --tag-value=TAG_VALUE_ID --parent=DOMAIN_NAME
    

Replace the following:

  * TAG_VALUE_ID: The permanent ID or namespaced name of the tag value to be attached. For example, `tagValues/1234567890`.
  * DOMAIN_NAME: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your Managed Microsoft AD domain, in the form of: `//managedidentities.googleapis.com/projects/PROJECT_ID/locations/global/domains/DOMAIN-NAME`.



## What's next

  * Learn how to [control access with tags](https://docs.cloud.google.com/iam/docs/tags-access-control).
  * Learn how to [set an organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
