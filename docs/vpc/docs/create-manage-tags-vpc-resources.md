---
url: https://docs.cloud.google.com/vpc/docs/create-manage-tags-vpc-resources/
title: Create and manage tags for VPC resources \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:11.527110+00:00
---

# Create and manage tags for VPC resources  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-manage-tags-vpc-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage tags for VPC resources

VPC networks use the following resources that support Resource Manager tags:

  * [Networks](https://docs.cloud.google.com/vpc/docs/vpc)
  * [Subnetworks](https://docs.cloud.google.com/vpc/docs/subnets)
  * [Routes](https://docs.cloud.google.com/vpc/docs/routes)
  * [Network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments)
  * [Service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments)
  * [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring)
  * [Regional IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses)
  * [Global IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses)
  * [Bring your own IP (BYOIP) public delegated prefix](https://docs.cloud.google.com/vpc/docs/create-pdp)



[Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are different from [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags). In this document, the term _tags_ is used to refer to Resource Manager tags.

For a list of all services that support tags, see [Services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).

For information about attaching tags to firewall policy resources for control plane governance, see [Create and manage tags for firewall resources](https://docs.cloud.google.com/firewall/docs/tags). For information about using tags to filter VM network traffic, see [Manage VM traffic by using secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).

## About tags

A tag is a key-value pair that can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

To group VPC resources within Virtual Private Cloud for automation and billing purposes, use [labels](https://docs.cloud.google.com/compute/docs/labeling-resources). Tags and labels work independently of each other, and you can apply both to resources. 

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles: 

  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization 
  * Create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for 
  * Attach and remove tags from resources: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you are attaching or removing the tag value to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To attach tags to VPC resources, you need the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) role (`roles/compute.networkAdmin`). 

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding a tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Add tags during resource creation

You can add tags at the time of creating networks, subnetworks, or routes. Adding tags lets you instantly provide essential metadata for your networks, subnetworks, or routes and also helps with better organization, cost tracking, and automated policy application.

### gcloud

To attach a tag to a resource during resource creation, add the `--resource-manager-tags` flag with the respective `create` command—for example, to attach a tag to a network, use the following command:
    
    
    gcloud compute networks create NETWORK_NAME \
        --resource-manager-tags=tagKeys/TAGKEY_ID=tagValues/TAGVALUE_ID
    

Replace the following:

  * `NETWORK_NAME`: the name of your network
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`

### API

Send a `POST` request to the following URL:
    
    
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT/global/networks

Provide the following JSON in the request body:
    
    
          
        {
          "name": "NETWORK_NAME",
          "params": {
            "resourceManagerTags": {
              "tagKeys/TAGKEY_ID": "tagValues/TAGVALUE_ID",
            },
          }
          // Other fields omitted
        }

Replace the following:

  * `NETWORK_NAME`: the name of your network
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



## Add tags to existing resources

To add a tag to existing VPC resources, follow these steps:

### gcloud

To attach a tag to a VPC resource, you must create a tag binding resource by using the `gcloud resource-manager tags bindings create` command:
    
    
          gcloud resource-manager tags bindings create \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that you attach to a resource—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for resources, not their names. For example, a subnet ID has a format similar to this: `//compute.googleapis.com/projects/123/regions/us-central1/subnetworks/456`. A network ID has a format similar to this: `//compute.googleapis.com/projects/123/global/networks/789`
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the VPC resource.

### gcloud

To get a list of tag bindings attached to a resource, use the `gcloud resource-manager tags bindings list` command:
    
    
          gcloud resource-manager tags bindings list \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for resources, not their names. For example, a subnet ID has a format similar to this: `//compute.googleapis.com/projects/123/regions/us-central1/subnetworks/456`. A network ID has a format similar to this: `//compute.googleapis.com/projects/123/global/networks/789`
  * `LOCATION`: the location of your resource. If you're viewing a tag attached to a global resource, such as a folder or a project, omit this flag. If you're viewing a tag attached to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



You should get a response similar to the following:
    
    
    name: tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
              tagValue: tagValues/567890123456
              resource: //compute.googleapis.com/projects/7890123456/subnetworks/subnetwork-ID
          

## Detach tags from resources

You can detach tags that have been directly attached to a VPC resource. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

### gcloud

To delete a tag binding, use the `gcloud resource-manager tags bindings delete` command:
    
    
          gcloud resource-manager tags bindings delete \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID \
              --location=LOCATION
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//compute.googleapis.com/`). You must use the numeric IDs for resources, not their names. For example, a subnet ID has a format similar to this: `//compute.googleapis.com/projects/123/regions/us-central1/subnetworks/456`. A network ID has a format similar to this: `//compute.googleapis.com/projects/123/global/networks/789`
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or a project, omit this flag. If you're attaching a tag to a regional or a zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the VPC resource. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. To delete tag keys and tag values, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
