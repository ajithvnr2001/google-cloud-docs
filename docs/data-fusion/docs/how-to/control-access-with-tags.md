---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-with-tags/
title: Control access with tags \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:44.786253+00:00
---

# Control access with tags  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-with-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Control access with tags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use tags to manage resources in Cloud Data Fusion.

You can attach tags to Cloud Data Fusion instances. Adding tags provides essential metadata for your resources and it helps with organization, cost tracking, and automated policy application.

## About tags

A tag is a key-value pair that you can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Before you begin

To get permissions for the following use cases, ask your administrator to grant the suggested role at the appropriate level of the [resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). For more information about IAM in Cloud Data Fusion, see [Access control with IAM](https://docs.cloud.google.com/data-fusion/docs/access-control).

### Required roles and permissions

To get the permissions that you need to use tags to manage instances in Cloud Data Fusion, ask your administrator to grant you the following IAM roles on the Cloud Data Fusion service account, and Compute Engine default service account or custom service account: 

  * To view tag definitions and tags that are attached to instances: [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) 
  * To create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) 
  * To administer tags at the organization level: Organization Viewer (`roles/resourcemanager.organizationViewer`) - on the organization resource 
  * To add and remove tags that are attached to instances: Tag User (`roles/resourcemanager.tagUser`) - on both the tag value and the resources that you attach the tag value to 
  * To attach tags to Cloud Data Fusion instances: [Cloud Data Fusion Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use tags to manage instances in Cloud Data Fusion. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use tags to manage instances in Cloud Data Fusion:

  * resourcemanager.tagKeys.get 
  * resourcemanager.tagKeys.list 
  * resourcemanager.tagValues.get 
  * resourcemanager.tagValues.list 
  * `listTagBindings` for the appropriate resource type. For example, for viewing tags attached to Cloud Data Fusion instances: `datafusion.instances.listTagBindings`
  * `listEffectiveTags` for the appropriate resource type. For example, for viewing all tags attached to or inherited by Cloud Data Fusion instances: `datafusion.instances.listEffectiveTags`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** `datafusion.instances.listTagBindings` and `datafusion.instances.listEffectiveTags` permissions are inherited through the Cloud Data Fusion Admin (`roles/datafusion.admin`), Cloud Data Fusion Viewer (`roles/datafusion.viewer`), or Cloud Data Fusion Accessor (`roles/datafusion.accessor`) IAM roles.

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Create a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Add tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#add_tag_values).

## Attach tags to Cloud Data Fusion instances

You can attach tags to a Cloud Data Fusion instance both during and after creating the instance.

### Attach tags during instance creation

You can attach tags when you create a Cloud Data Fusion instance.

### gcloud

Use the [`gcloud beta data-fusion instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create) command with the [`--tags`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create#--tags) flag:
    
    
    gcloud beta data-fusion instances create INSTANCE_ID \
        --tags=tagKeys/TAGKEY_ID=tagValues/TAGVALUE_ID
    

[Multiple tags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create#--tags) can be added at once.

Replace the following:

  * `INSTANCE_ID`: the name of your Cloud Data Fusion instance.
  * `TAGKEY_ID`: the numeric ID of the tag key, without a namespace, for example, `123456789012`.
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value. For example, `4567890123`.



###  REST 

Send a `POST` request to the following URL:
    
    
    POST https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instanceID=INSTANCE_ID
    

Provide the following JSON in the request body:
    
    
    {
        "tags": {
            "tagKeys/TAGKEY_ID": "tagValues/TAGVALUE_ID"
        }
        // Other fields omitted
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `INSTANCE_ID`: the name of your Cloud Data Fusion instance.
  * `TAGKEY_ID`: the numeric ID of the tag key.
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value. For example, `4567890123`.



For more information, see the [v1](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create) and [v1beta1](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/create) API references.

You can add [Multiple tags](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Instance) at once.

### Attach tags after creating the instance

You can attach tags to a Cloud Data Fusion instance after you create the instance.

### gcloud

To attach a tag to an instance, you must create a tag binding resource by using the `create` command:
    
    
    gcloud resource-manager tags bindings create \
      --tag-value=TAGVALUE_NAME \
      --parent=RESOURCE_ID \
      --location=LOCATION
    

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespace name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name, identifying the type of resource (`//datafusion.googleapis.com/`). For example, to attach a tag to an instance in `projects/7890123456` located in `us-central1`, use the following resource ID: `//datafusion.googleapis.com/projects/7890123456/locations/us-central1/instances/instance-ID`.
  * `LOCATION`: the location of your resource. For example: `us-central1`.



A notification confirms that your tags are created.

This action doesn't cause an instance restart.

## List tags attached to an instance

You can view a list of tag bindings directly attached to or inherited by the Cloud Data Fusion instance.

### gcloud

To get a list of tag bindings attached to an instance, use the `list` command:
    
    
    gcloud resource-manager tags bindings list \
      --parent=RESOURCE_ID \
      --location=LOCATION
    

Replace the following:

  * `RESOURCE_ID`: the full ID of the resource, including the API domain name, identifying the type of resource (`//datafusion.googleapis.com/`). For example, to list tags in an instance in `projects/7890123456` located in `us-central1`, use the following resource ID: `//datafusion.googleapis.com/projects/7890123456/locations/us-central1/instances/instance-ID`.
  * `LOCATION`: the location of your resource. For example: `us-central1`.



The response comes in the following form:
    
    
    tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
      tagValue: tagValues/567890123456
      resource: //datafusion.googleapis.com/projects/7890123456/locations/us-central1/instances/instance-ID
    

## Detach tags from an instance

You can detach tags that have been directly attached to a Cloud Data Fusion instance. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached. Before you can delete a tag, you must detach its key and values from every instance to which it is attached.

### gcloud

To delete a tag binding, use the `delete` command:
    
    
    gcloud resource-manager tags bindings delete \
      --tag-value=TAGVALUE_NAME \
      --parent=RESOURCE_ID \
      --location=LOCATION
    

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespace name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name, identifying the type of resource (`//datafusion.googleapis.com/`). For example, to attach a tag to an instance in `projects/7890123456` located in `us-central1`, use the following resource ID: `//datafusion.googleapis.com/projects/7890123456/locations/us-central1/instances/instance-ID`.
  * `LOCATION`: the location of your resource. For example: `us-central1`.



A notification confirms that your tags are updated.

## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the instance. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. To delete tag keys and tag values, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to an instance can remove user access to that instance if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * To learn how to use tags with IAM, see [Tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
