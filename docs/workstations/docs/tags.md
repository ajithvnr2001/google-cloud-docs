---
url: https://docs.cloud.google.com/workstations/docs/tags/
title: Tag Cloud Workstations resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:09.807615+00:00
---

# Tag Cloud Workstations resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Tag Cloud Workstations resources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use tags to conditionally apply [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/tags-access-control) policies to Cloud Workstations clusters.

A tag is a key-value pair that you can attach directly to a Cloud Workstations cluster. A Cloud Workstations cluster can also [inherit](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance) a tag from other Google Cloud resources. You can conditionally apply policies based on whether a resource has a specific tag. For example, you might conditionally grant the Cloud Workstations Creator role to a principal on any Cloud Workstations cluster with `environment:dev` tag.

For more information about using tags across the Google Cloud resource hierarchy, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Before you begin

You need to grant IAM roles that give users the necessary [permissions](https://docs.cloud.google.com/workstations/docs/access-control) to perform each task in this document. You also need to create tag keys and values to attach to resources.

### Required roles

The following roles provide the necessary permissions to tag Cloud Workstations resources:

#### Attach a tag to a Cloud Workstations cluster

To get the permissions that you need to attach a tag to a Cloud Workstations cluster, ask your administrator to grant you the following IAM roles: 

  * To create Cloud Workstations cluster: [Cloud Workstations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`) on your project 
  * To create tags: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on your project 
  * To manage tags: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and Cloud Workstations cluster 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to attach a tag to a Cloud Workstations cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to attach a tag to a Cloud Workstations cluster:

  * `workstations.workstationClusters.createTagBinding` on the cluster
  * `resourcemanager.tagValueBindings.create` on the tag value
  * `workstations.workstationClusters.create` on the cluster to attach a tag when creating a cluster
  * `workstations.workstationClusters.update` on the cluster to attach a tag when updating a cluster



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Remove a tag from a Cloud Workstations cluster

To get the permissions that you need to remove a tag from a Cloud Workstations cluster, ask your administrator to grant you the following IAM roles: 

  * To remove a tag from a Cloud Workstations cluster: [Cloud Workstations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`) on your project 
  * To manage tags: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value andCloud Workstations cluster 
  * To delete tags: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on your project 



These predefined roles contain the permissions required to remove a tag from a Cloud Workstations cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to remove a tag from a Cloud Workstations cluster:

  * `workstations.workstationClusters.deleteTagBinding` on the cluster
  * `resourcemanager.tagValueBindings.delete` on the tag value
  * `workstations.workstationClusters.update` on the cluster to remove a tag when updating a cluster



#### List tags attached to a Cloud Workstations cluster

To get the permissions that you need to list tags attached to a Cloud Workstations cluster, ask your administrator to grant you the following IAM roles: 

  * To list tags attached to a Cloud Workstations cluster: [Cloud Workstations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`) on your project 
  * To list tags: [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the tag value andCloud Workstations cluster 



These predefined roles contain the permissions required to list tags attached to a Cloud Workstations cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list tags attached to a Cloud Workstations cluster:

  * `resourcemanager.tagKeys.list` on the tag key's parent
  * `resourcemanager.tagKeys.get` on the tag key
  * `resourcemanager.tagValues.list` on the tag value parent
  * `resourcemanager.tagValues.get` on the tag value
  * `workstations.workstationClusters.listTagBindings` on the cluster
  * `workstations.workstationClusters.listEffectiveTags` on the cluster



### Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Tag Cloud Workstations clusters

The following sections describe how to attach tags to new and existing Cloud Workstations clusters, list tags attached to a Cloud Workstations cluster, and detach tags from a Cloud Workstations cluster.

### Attach tags when you create a new Cloud Workstations cluster

After you create a tag, you can attach it to a new Cloud Workstations cluster. For each tag key, you can attach one tag value to a Cloud Workstations cluster. For each Cloud Workstations cluster, you can attach at most 50 tags.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Workstations** page.

[Go to Workstations](https://console.cloud.google.com/workstations)

  2. Click on the **Cluster management** section.

  3. Click on **Create**.

  4. Enter the information for your new Cloud Workstations cluster. For more details, see [Create a workstation cluster](https://docs.cloud.google.com/workstations/docs/create-cluster).

  5. In the **Tags** section, select the tags that you want to add to the new Cloud Workstations cluster.

  6. Click **Create**.




###  gcloud 

Use the [`gcloud workstations clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/clusters/create) with the `--tags` flag:
    
    
    gcloud workstations clusters create WORKSTATIONS_CLUSTER_NAME \
        --region=LOCATION \
        --tags=TAG \
        --project=WORKSTATIONS_PROJECT_ID

Replace the following:

  * `WORKSTATIONS_CLUSTER_NAME`: the name of your Cloud Workstations cluster.
  * `LOCATION`: the region for your cluster.
  * `TAG`: the tag that you are attaching to the new Cloud Workstations cluster. Multiple tags are separated by commas. For example, `556741164180/env:prod,myProject/department:sales`. Each tag must have the [namespaced key name and value short name](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * `WORKSTATIONS_PROJECT_ID`: the ID of your workstation project.



###  API 

Call the [`workstationClusters.create` method](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters/create). Include the tags in the `tags` field of `WorkstationCluster`.

### Attach tags to an existing Cloud Workstations cluster

After you create a tag, you can attach it to an existing Cloud Workstations cluster. For each tag key, you can attach one tag value to a Cloud Workstations cluster. For each Cloud Workstations cluster, you can attach at most 50 tags.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Workstations** page.

[Go to Workstations](https://console.cloud.google.com/workstations)

  2. Click on the **Cluster management** section.

  3. Click on the Cloud Workstations cluster that you want to attach the tag to.

  4. Click **Edit**.

  5. In the **Tags** section, select the tags that you want to add to the Cloud Workstations cluster.

  6. Click **Save**.




###  gcloud 

To attach a tag to a Cloud Workstations cluster using the command line, create a tag binding resource by using the [`gcloud resource-manager tags bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create):
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAGVALUE_NAME \
        --parent=RESOURCE_ID \
        --location=LOCATION
    

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value to be attached, such as `tagValues/4567890123` or `1234567/my_tag_key/my_tag_value`.
  * `RESOURCE_ID`: the full ID of the Cloud Workstations cluster, including the API domain name (`//workstations.googleapis.com/`) to identify the type of resource. For example, `//workstations.googleapis.com/projects/my_project/locations/us-central1/workstationClusters/my_cluster`
  * `LOCATION`: the region of the Cloud Workstations cluster.



###  API 

Call the [`workstationClusters.patch` method](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters/patch). Include the tags in the `tags` field of `WorkstationCluster`.

### List tags attached to a Cloud Workstations cluster

You can list tags that are attached directly to a Cloud Workstations cluster. This process doesn't list tags that are inherited from parent resources.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Workstations** page.

[Go to Workstations](https://console.cloud.google.com/workstations)

  2. Click on the **Cluster management** section.

  3. Click on the Cloud Workstations cluster that you want to list the tags for.

  4. The tags are visible in the **Tags** section.




###  gcloud 

To get a list of tag bindings attached to a resource, use the [`gcloud resource-manager tags bindings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/list):
    
    
    gcloud resource-manager tags bindings list \
        --parent=RESOURCE_ID \
        --location=LOCATION
    

Replace the following:

  * `RESOURCE_ID`: the full ID of the Cloud Workstations cluster, including the API domain name (`//workstations.googleapis.com/`) to identify the type of resource. For example, `//workstations.googleapis.com/projects/my_project/locations/us-central1/workstationClusters/my_cluster`.

  * `LOCATION`: the region of the Cloud Workstations cluster.




###  API 

Call the [`v3.tagBindings.list` method](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list). Include the Cloud Workstations cluster in the parent field. For example, `//cloudresourcemanager.googleapis.com/projects/my-project/regions/us-central1/workstationClusters/my-cluster`.

### Detach tags from a Cloud Workstations cluster

You can remove a tag association from a Cloud Workstations cluster by deleting the tag binding. If you need to delete a tag, you should take the following steps to detach the tag from your Cloud Workstations cluster first.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Workstations** page.

[Go to Workstations](https://console.cloud.google.com/workstations)

  2. Click on the **Cluster management** section.

  3. Click on the Cloud Workstations cluster that you want to detach the tag from.

  4. Click **Edit**.

  5. In the **Tags** section, remove the tags that you want to detach from the Cloud Workstations cluster.

  6. Click **Save**.




###  gcloud 

To remove a tag association from a Cloud Workstations cluster using the command line, delete the tag binding by using the [`gcloud resource-manager tags bindings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete):
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAGVALUE_NAME \
        --parent=RESOURCE_ID \
        --location=LOCATION
    

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value to be attached, such as `tagValues/4567890123` or `1234567/my_tag_key/my_tag_value`.
  * `RESOURCE_ID`: the full ID of the Cloud Workstations cluster, including the API domain name (`//workstations.googleapis.com/`) to identify the type of resource. For example, `//workstations.googleapis.com/projects/my_project/locations/us-central1/workstationClusters/my_cluster`
  * `LOCATION`: the region of the Cloud Workstations cluster.



###  API 

Call the [`workstationClusters.patch` method](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters/patch). Remove the tags in the `tags` field of `WorkstationCluster`.

## What's next

  * For an overview of tags in Google Cloud, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).
  * For more information about how to use tags, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * For information about how to control access to Cloud Workstations resources with IAM Conditions, see [Access control with IAM Conditions](https://docs.cloud.google.com/workstations/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
