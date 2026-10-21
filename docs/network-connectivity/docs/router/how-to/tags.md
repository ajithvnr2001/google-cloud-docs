---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/tags/
title: Create and manage tags \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:21.814971+00:00
---

# Create and manage tags  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage tags

You can attach tags to the following Cloud Router resources:

  * Router



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

To attach tags to Cloud Router resources, you need the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`). 

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding a tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Add tags during resource creation

You can add tags at the time of creating regional secrets. Adding tags lets you instantly provide essential metadata for your regional secrets and also helps with better organization, cost tracking, and automated policy application.

### gcloud

To attach a tag to a resource during resource creation, add the `--resource-manager-tags` flag with the respective `create` command—for example, to attach a tag to a router, use the following command:
    
    
    gcloud compute routers create ROUTER_NAME \
        --resource-manager-tags=tagKeys/TAGKEY_ID=tagValues/TAGVALUE_ID
    

Replace the following:

  * `ROUTER_NAME`: the name of your router
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`

### API

Send a `POST` request to the following URL:
    
    
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/{region}/routers

Provide the following JSON in the request body:
    
    
          
        {
          "name": "ROUTER_NAME",
          "params": {
            "resourceManagerTags": {
              "tagKeys/TAGKEY_ID": "tagValues/TAGVALUE_ID",
            },
          }
          // Other fields omitted
        }

Replace the following:

  * `ROUTER_NAME`: the name of your router
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



## Add tags to existing resources

To add a tag to existing Cloud Router resources, follow these steps:

### Console

  1. Go to the **Cloud Router** page in the Google Cloud console.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers)

  2. Select the Cloud Router resource for which you would like to attach a tag.
  3. Click label_important**Tags**.
  4. If your organization doesn't appear in the **Tags** panel, click **Select scope**. Select your organization and click **Open**.
  5. Click **Add tag**.
  6. Select the key for the tag you want to attach from the list. You can filter the list by typing keywords.
  7. Select the value for the tag you want to attach from the list. You can filter the list by typing keywords.
  8. Click **Save**.
  9. In the **Confirm** dialog, click **Confirm** to attach the tag.

A notification confirms that your tags updated.




### gcloud

To attach a tag to a Cloud Router resource, you must create a tag binding resource by using the `gcloud resource-manager tags bindings create` command:
    
    
          gcloud resource-manager tags bindings create \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that you attach to a resource—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for the resources, not their names. For example, a resource ID of a router in `projects/7890123456`, is as follows: `//compute.googleapis.com/projects/7890123456/regions/REGION/routers/{resource-id}`
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the Cloud Router resource.

### Console

  1. Go to the **Cloud Router** page in the Google Cloud console.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers)

  2. Select the resource to see its details. Tags are displayed in the **Tags** row. 



### gcloud

To get a list of tag bindings attached to a resource, use the `gcloud resource-manager tags bindings list` command:
    
    
          gcloud resource-manager tags bindings list \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for the resources, not their names. For example, a resource ID of a router in `projects/7890123456`, is as follows: `//compute.googleapis.com/projects/7890123456/regions/REGION/routers/{resource-id}`
  * `LOCATION`: the location of your resource. If you're viewing a tag attached to a global resource, such as a folder or a project, omit this flag. If you're viewing a tag attached to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



You should get a response similar to the following:
    
    
    name: tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
              tagValue: tagValues/567890123456
              resource: 
    //compute.googleapis.com/projects/7890123456/regions/REGION/routers/{resource-id}
    
          

## Detach tags from resources

You can detach tags that have been directly attached to a Cloud Router resource. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

### Console

  1. Go to the **Cloud Router** page in the Google Cloud console.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers)

  2. Select the Cloud Router resource from which you want to remove a tag.
  3. Click label_important**Tags**.
  4. In the **Tags** panel, next to the tag you want to detach, click delete**Delete item**.
  5. Click **Save**.
  6. In the **Confirm** dialog, click **Confirm** to detach the tag.



A notification confirms that your tags updated.

### gcloud

To delete a tag binding, use the `gcloud resource-manager tags bindings delete` command:
    
    
          gcloud resource-manager tags bindings delete \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID`: the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for the resources, not their names. For example, a resource ID of a router in `projects/7890123456`, is as follows: `//compute.googleapis.com/projects/7890123456/regions/REGION/routers/{resource-id}`
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the Cloud Router resource. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. To delete tag keys and tag values, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
