---
url: https://docs.cloud.google.com/composer/docs/composer-1/create-and-manage-tags/
title: Create and manage Google Cloud tags \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:14.482037+00:00
---

# Create and manage Google Cloud tags  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/create-and-manage-tags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Create and manage Google Cloud tags Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/create-and-manage-tags "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/create-and-manage-tags "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes Google Cloud tags and how to use them with Managed Service for Apache Airflow.

If you want to add labels to your Managed Airflow environment instead, see [Manage environment labels and break down environment costs](https://docs.cloud.google.com/composer/docs/composer-1/manage-environment-labels).

## About tags

A tag is a key-value pair that can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles: 

  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization 
  * Create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for 
  * Attach and remove tags from resources: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you are attaching or removing the tag value to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To attach tags to Managed Airflow environments, you need the [Composer Administrator](https://docs.cloud.google.com/composer/docs/composer-1/access-control) role (`roles/composer.admin`). 

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding a tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Add tags to existing resources

To add a tag to existing environments, follow these steps:

### gcloud

To attach a tag to an environment, you must create a tag binding resource by using the `gcloud resource-manager tags bindings create` command:
    
    
          gcloud resource-manager tags bindings create \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that you attach to a resource—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//composer.googleapis.com/`). 

The full ID format for Managed Airflow environments is:
        
        //composer.googleapis.com/projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME
        

Replace the following:

    * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project where the environment is located.
    * `LOCATION`: the region where the environment is located.
    * `ENVIRONMENT_NAME`: the name of the environment.

Example: `//composer.googleapis.com/projects/7890123456/locations/us-central1/environments/example-environment`.

  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the environment.

### gcloud

To get a list of tag bindings attached to a resource, use the `gcloud resource-manager tags bindings list` command:
    
    
          gcloud resource-manager tags bindings list \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//composer.googleapis.com/`). 

The full ID format for Managed Airflow environments is:
        
        //composer.googleapis.com/projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME
        

Replace the following:

    * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project where the environment is located.
    * `LOCATION`: the region where the environment is located.
    * `ENVIRONMENT_NAME`: the name of the environment.

Example: `//composer.googleapis.com/projects/7890123456/locations/us-central1/environments/example-environment`.

  * `LOCATION`: the location of your resource. If you're viewing a tag attached to a global resource, such as a folder or a project, omit this flag. If you're viewing a tag attached to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



You should get a response similar to the following:
    
    
    name: tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
              tagValue: tagValues/567890123456
              resource: //composer.googleapis.com/projects/7890123456/locations/us-central1/environments/example-environment
          

## Detach tags from resources

You can detach tags that have been directly attached to an environment. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

### gcloud

To delete a tag binding, use the `gcloud resource-manager tags bindings delete` command:
    
    
          gcloud resource-manager tags bindings delete \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//composer.googleapis.com/`). 

The full ID format for Managed Airflow environments is:
        
        //composer.googleapis.com/projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME
        

Replace the following:

    * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project where the environment is located.
    * `LOCATION`: the region where the environment is located.
    * `ENVIRONMENT_NAME`: the name of the environment.

Example: `//composer.googleapis.com/projects/7890123456/locations/us-central1/environments/example-environment`.

  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the environment. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. To delete tag keys and tag values, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
