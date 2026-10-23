---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/create-tags/
title: Create and manage Tags on EKS attached clusters \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:50.913514+00:00
---

# Create and manage Tags on EKS attached clusters  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/create-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/concepts/overview)



Send feedback 

#  Create and manage Tags on EKS attached clusters Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to create and manage Tags in your GKE attached clusters.

## Overview

A _tag_ is a key-value pair that can attach to a resource within Google Cloud. You can use Tags to conditionally allow or deny policies based on whether a resource has a specific tag.

As a platform administrator, a use case for Tags might be to conditionally grant Identity and Access Management (IAM) roles based on whether a cluster has a specific tag. For example, you can configure GKE to automatically grant Identity and Access Management roles to users who are contractors so that they can access specific clusters that are normally available only to full-time employees.

After creating a tag, you can attach the tag to a Google Cloud resource as a key-value pair using a _tag binding_. For each key, you can attach one value to a resource. For example, if you attached `env:dev` to your cluster, you can't also attach `env:prod` or `env:test`. You can attach up to 50 tags to each resource.

In GKE attached clusters, there are several methods to annotate your resources, as outlined in the following table:

Annotation type | Level | Description | Example  
---|---|---|---  
Tags | GKE cluster |  Conditionally allow or deny policies based on the tag. To learn more, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) in the Resource Manager documentation. | Automatically grant users who are contractors access to specific clusters that are normally available only to full-time employees.  
GKE cluster labels | GKE cluster |  Organize GKE resources to track usage and billing. To learn more, see [Cluster labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels). | Differentiate between clusters owned by specific cost centers or teams in your organization.  
Kubernetes labels | GKE cluster |  Associate cluster components and resources with one another and manage resource lifecycles. To learn more, see [Kubernetes labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). | Require that workloads are scheduled on nodes with specific labels.  
  
## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have the following IAM roles to work with Tags:

    * `roles/resourcemanager.tagAdmin`
    * `roles/resourcemanager.tagUser`

For information on the permissions granted by these roles, see [Required permissions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing?cloudshell=false#required-permissions-attach).




## Create tag keys and values

Before you can attach a tag to your GKE resources, you need to create the tag and configure its values. To create tag keys and values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values) in the Resource Manager documentation.

## Attach Tags to a cluster

You can attach Tags to a new or existing cluster if you have the correct permissions.

### Attach Tags when you create a cluster

To create a tag binding while you create a new cluster, run the following command:
    
    
    gcloud container attached clusters register CLUSTER_NAME \
        --tags=TAG_ID
    ...
    

Replace the following:

  * CLUSTER_NAME: the name of your cluster. The CLUSTER_NAME must be compliant with the [RFC 1123 Label Names standard](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).

  * `TAG_ID`: the permanent ID or namespaced name of the tag value to attach—for example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).




For more information, see [Attach your GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster).

### Attach Tags when you update a cluster

To create a tag binding to attach a tag to an existing cluster, use one of the following methods:

### gcloud

To create a tag binding to attach a tag to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE_ID \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to attach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/attachedClusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.
  * `CLUSTER_LOCATION`: the name of the Google Cloud location from where your cluster is managed.




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[ Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. In the **Metadata** section, next to **Tags** , click edit **Edit tags**.

  4. If your organization doesn't appear in the **Tags** panel, click **Select scope**. Select your organization and click **Open**.

  5. In the **Tags** panel, select **Add tag**.

  6. Select the key for the tag you want to attach from the list. You can filter the list by typing keywords.

  7. Select the value for the tag you want to attach from the list. You can filter the list by typing keywords.

  8. Click **Save**.

  9. In the **Confirm** dialog, click **Confirm** to attach the tag.

A notification confirms that your tags updated.




### API

To attach a tag to a resource, you must first create a JSON representation of a tag binding that includes the permanent IDs of the tag value and the resource. For more information about the format of a tag binding, see the [TagBinding reference](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings).

Use the `tagBindings.create` method with the endpoint where your cluster is located.
    
    
    POST https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings
    

Replace `LOCATION` with the Google Cloud location where your cluster is located, such as `us-central1`.

JSON request body:
    
    
    {
      "parent": "RESOURCE_ID",
      "tagValue": "TAG_VALUE_ID"
    }
    

Replace the following:

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/attachedClusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.
  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to attach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).




The output is similar to the following:
    
    
    {
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.TagBinding",
        "name": "tagBindings///container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/attachedClusters/CLUSTER_NAME/tagValues/TAG_VALUE_ID",
        "parent": "//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/attachedClusters/CLUSTER_NAME",
        "tagValue": "TAG_VALUE_ID"
      }
    }
    

## List Tags attached to a cluster

You can list the Tags attached to a cluster by using the gcloud CLI, the Google Cloud console, or the Tags API.

### gcloud

To get a list of tag bindings attached to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings list \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/attachedClusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.

    * `CLUSTER_NAME`: The name of your cluster.

  * `CLUSTER_LOCATION`: The Google Cloud location where your cluster is located.




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to view.

  3. In the **Metadata** section, next to **Tags** , look for the currently attached tag values.




### API

To get a list of tag bindings for a cluster, use the `tagBindings.list` method with the endpoint where your cluster is located.
    
    
    GET https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings
    

JSON request body:
    
    
    {
      "parent": RESOURCE_ID,
    }
    

Replace the following:

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/attachedClusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.



The output is similar to the following:
    
    
    "tagBindings": [
      {
        "name": "tagBindings/%2F%2Fcontainer.googleapis.com%2Fprojects%2Ftags-bugbash-project%2Flocations%2Fus-central1%2Fclusters%2Ftestcluster/tagValues/758072120217",
        "parent": "//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/attachedClusters/CLUSTER_NAME",
        "tagValue": "TAG_VALUE_ID"
      }
    ]
    

## Detach Tags from a cluster

You can detach a tag from a cluster by deleting the tag binding resource attached to the cluster by using the gcloud CLI, the Google Cloud console, or the Tags API. If you need to delete a tag, you must first detach from all attached resources.

### gcloud

To detach a tag binding attached to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE_ID \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to detach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/attachedClusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.

    * `CLUSTER_NAME`: The name of your cluster.

  * `CLUSTER_LOCATION`: The Google Cloud location where your cluster is located.




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[ Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. In the **Metadata** section, next to **Tags** , click edit **Edit tags**.

  4. In the **Tags** panel, next to the tag you want to detach, click delete **Delete item**.

  5. Click **Save**.

  6. In the **Confirm** dialog, click **Confirm** to detach the tag.

A notification confirms that your tags updated.




### API

To delete tag bindings for a cluster, use the `tagBindings.delete` method with the endpoint where your cluster is located.
    
    
    DELETE https://LOCATION-cloudresourcemanager.googleapis.com/v3/TAG_BINDING_NAME
    

Replace `TAG_BINDING_NAME` with the [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of the `tagBinding` object you want to detach. For example, `tagBindings/container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/tagValues/TAG_VALUE_ID`.

## Delete tag keys and tag values

Before you delete tag keys and values, ensure that the tags are detached from all resources. Then, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting) to delete the keys and values.

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your project hierarchy. When you change or delete the tag attached to a cluster that has an IAM policy with conditional role bindings, GKE re-evaluates access permissions based on the updated conditions.

Authorization to list and create GKE clusters is checked at the project level, not at the individual cluster level. If you use conditional IAM role bindings with cluster-level tags to restrict access to specific clusters, those users might experience errors when attempting to list or create clusters in the project. To avoid these errors, attach a tag to the parent project and use a conditional role binding to grant the list or create access. For information about roles and permissions, see the [IAM roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/container).

For more information about conditional access grants in IAM, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * [Learn how to set an organization policy with Tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).
  * Learn more about how to [manage tags and attach tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).
  * [See the other services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * [Learn how to use tags with IAM](https://docs.cloud.google.com/iam/docs/tags-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
