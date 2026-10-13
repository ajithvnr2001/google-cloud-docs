---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags/
title: Manage GKE resources using Tags \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:58.481130+00:00
---

# Manage GKE resources using Tags  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manage GKE resources using Tags Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to use Tags to manage your Google Kubernetes Engine (GKE) clusters and conditionally apply Identity and Access Management policies to nodes.

## About Tags

Tags are key-value pairs that let you annotate and manage your Google Cloud resources at the organization or project level. You can use Tags to organize your resources and to conditionally apply policies like firewalls or IAM policies. Tags support IAM access control, which lets you define who can attach, create, update, or delete Tags.

### Use cases for Tags in GKE

You might use Tags in GKE for situations like the following:

  * Conditionally apply network firewall policies to specific nodes. For example, deny ingress traffic from the public internet to all nodes of a cluster in staging or testing environments. For instructions, see [Selectively enforce network firewall policies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies).
  * Conditionally grant IAM roles based on Tags. For example, automatically grant contractors access to specific environments that would normally only be available to full-time employees. For instructions, see the rest of this document.
  * Audit and analyze billing information based on applied Tags at the project or organization level.



### How it works

For network firewall policy enforcement specifically, you create a tag and explicitly designate the tag for firewall use. For all other purposes, you create a tag without setting a firewall designation.

After creating the tag, you attach the tag to your GKE resources as a key-value pair. How you attach the tag depends on the target resource:

  * **Cluster resources** : To attach non-firewall tags directly to a GKE cluster resource, use the Tags API. You can attach up to 50 non-firewall Tags to each cluster resource. Tags attached directly to a cluster resource aren't propagated to the underlying Compute Engine VMs.
  * **Node pools and nodes** : To attach tags to GKE node pools (and automatically propagate them to the underlying Compute Engine VMs), use the GKE API. You can attach both firewall and non-firewall Tags to node pools by using the GKE API, up to a maximum total of five tags (combined firewall and non-firewall) per node pool.



For each key, you can attach one value to a resource. For example, if you attached `env:dev` to a GKE cluster or node pool, you can't also attach `env:prod` or `env:test`.

### Resource annotation methods in GKE

In GKE, there are several methods to annotate your resources, as outlined in the following table:

Annotation type | Description | Example  
---|---|---  
Tags (non-firewall) | 

  * Apply directly to a cluster resource by using the Tags API (up to 50 non-firewall tags)
  * Apply to node pools and their underlying Compute Engine VMs by using the GKE API (up to five tags total per node pool, combined with firewall tags)
  * Organize resources to track usage and billing
  * Conditionally apply IAM policies
  * Control access to specific Tags with IAM

**Caution:** You can optionally attach tags directly to the Compute Engine VMs that back your GKE nodes by using Compute Engine or Resource Manager APIs. We don't recommend this method, because GKE overwrites these VM tags when you use the GKE API to manage tags on the node pool.To learn more, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). | Conditionally grant IAM roles to control access to resources that have specific Tags  
Tags (firewall) | 

  * Apply to cluster or node pool by using GKE API (up to five tags total per node pool, combined with non-firewall tags)
  * Conditionally apply Cloud Next Generation Firewall network firewall policies.
  * Control access to specific Tags with IAM
  * GKE attaches the key-value pairs to the underlying Compute Engine VMs.

To learn more, see [Selectively apply network firewall policies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies). | Automatically deny ingress traffic from public internet to all staging or testing environments  
Network tags | 

  * Apply to cluster or node pool using GKE API
  * Simple strings with no IAM access control
  * Use to conditionally apply VPC firewall rules
  * GKE attaches the key-value pairs to the underlying Compute Engine VMs

To learn more, see [Use network tags to apply firewall rules to nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-network-tags). | Automatically deny ingress traffic from public internet to all staging or testing environments  
GKE cluster labels | 

  * Apply to cluster or node pool using GKE API
  * Organize resources to track usage and billing

To learn more, see [Cluster labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels). | Differentiate between clusters owned by specific cost centers or teams in your organization.  
Kubernetes labels | 

  * Apply to Kubernetes API objects
  * Associate cluster components and resources with one another and manage resource lifecycles.

To learn more, see [Kubernetes labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). | Require that workloads are scheduled on nodes with specific labels.  
  
## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have the following IAM roles:

    * `roles/resourcemanager.tagAdmin`
    * `roles/resourcemanager.tagUser`

For information on the permissions granted by these roles, see [Required permissions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing?cloudshell=false#required-permissions-attach).

  * [Ensure that you have a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) running.




## Attach Tags to a cluster

You can attach Tags to an existing cluster if you have the correct permissions by using the Google Cloud CLI, the Google Cloud console, the Tags API, or Terraform.

### gcloud

Before you can attach a tag to your GKE resources using gcloud CLI, you must create the tag and configure its values. To create tag keys and values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

To create a tag binding to attach a tag to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE_ID \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to attach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * `CLUSTER_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available). For zonal clusters, specify the compute zone.
  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.



### Console

Before you can attach a tag to your GKE resources using the Google Cloud console, you must create the tag and configure its values. To create tag keys and values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

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

Use the `tagBindings.create` method with the regional or zonal endpoint where your cluster is located.
    
    
    POST https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings
    

Replace `LOCATION` with the region or zone where your cluster is located.

JSON request body:
    
    
    {
      "parent": "RESOURCE_ID",
      "tagValue": "TAG_VALUE_ID"
    }
    

Replace the following:

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.
  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to attach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).




The output is similar to the following:
    
    
    {
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.TagBinding",
        "name": "tagBindings///container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/tagValues/TAG_VALUE_ID",
        "parent": "//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME",
        "tagValue": "TAG_VALUE_ID"
      }
    }
    

### Terraform

To create a tag, configure its values, and attach a tag to a resource using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-tag"
      location = "us-central1"
    
      enable_autopilot = true
    }
    
    data "google_project" "default" {}
    
    resource "google_tags_tag_key" "default" {
      parent      = "projects/${data.google_project.default.project_id}"
      short_name  = "env"
      description = "Environment tag key"
    }
    
    resource "google_tags_tag_value" "default" {
      parent      = "tagKeys/${google_tags_tag_key.default.name}"
      short_name  = "dev"
      description = "Development environment tag value."
    }
    
    resource "google_tags_location_tag_binding" "default" {
      parent    = "//container.googleapis.com/${google_container_cluster.default.id}"
      location  = google_container_cluster.default.location
      tag_value = "tagValues/${google_tags_tag_value.default.name}"
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## List Tags attached to a cluster

You can list the Tags attached to a cluster by using the gcloud CLI, the Google Cloud console, or the Tags API.

### gcloud

To get a list of tag bindings attached to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings list \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `CLUSTER_LOCATION`: For regional clusters, specify the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available). For zonal clusters, specify the compute zone.

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.

    * `CLUSTER_NAME`: The name of your cluster.




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to view.

  3. In the **Metadata** section, next to **Tags** , look for the attached tag values.




### API

To get a list of tag bindings for a cluster, use the `tagBindings.list` method with the regional or zonal endpoint where your cluster is located.
    
    
    GET https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings
    

JSON request body:
    
    
    {
      "parent": RESOURCE_ID,
    }
    

Replace the following:

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.
    * `CLUSTER_NAME`: The name of your cluster.



The output is similar to the following:
    
    
    "tagBindings": [
      {
        "name": "tagBindings/%2F%2Fcontainer.googleapis.com%2Fprojects%2Ftags-bugbash-project%2Flocations%2LOCATION%2Fclusters%2Ftestcluster/tagValues/758072120217",
        "parent": "//container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME",
        "tagValue": "TAG_VALUE_ID"
      }
    ]
    

## Detach tags from a cluster

You can detach a tag from a cluster by deleting the tag binding resource attached to the cluster by using the gcloud CLI, the Google Cloud console, or the Tags API. If you need to delete a tag, you must first detach from all attached resources.

### gcloud

To detach a tag binding attached to a cluster, run the following command:
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE_ID \
        --parent=RESOURCE_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `TAG_VALUE_ID`: The permanent ID or namespaced name of the tag value to detach. For example, `tagValues/4567890123`. For details about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

  * `CLUSTER_LOCATION`: For regional clusters, specify the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available). For zonal clusters, specify the compute zone.

  * `RESOURCE_ID`: The [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of your cluster, such as `//container.googleapis.com/projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME`.

In the resource ID:

    * `PROJECT_ID`: Your Google Cloud project ID.

    * `CLUSTER_NAME`: The name of your cluster.




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

To delete tag bindings for a cluster, use the `tagBindings.delete` method with the regional or zonal endpoint where your cluster is located.
    
    
    DELETE https://LOCATION-cloudresourcemanager.googleapis.com/v3/TAG_BINDING_NAME
    

Replace `TAG_BINDING_NAME` with the [full resource name](https://docs.cloud.google.com/apis/design/resource_names#full_resource_name) of the `tagBinding` object you want to detach. For example, `tagBindings/container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/tagValues/TAG_VALUE_ID`.

## Attach Tags to a node pool

You can attach both non-firewall and firewall Tags to GKE node pools by using the GKE API. When you attach tags to a node pool, GKE automatically propagates those tags to the underlying Compute Engine VMs in that node pool.

  * Non-firewall tags on node pools are supported in GKE version 1.34 and later.
  * Non-firewall tags with custom ComputeClasses are supported in GKE version 1.35.0-gke.2398000 and later.

**Note:** Each node pool supports a maximum total of five tags (combined firewall and non-firewall) when attached by using the GKE API.

### Attach tags to a Standard node pool

You can attach tags when you create a new node pool or update an existing node pool by using the `--resource-manager-tags` flag:

  * To attach tags when creating a new node pool, run the following command:
        
        gcloud container node-pools create NODE_POOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=CLUSTER_LOCATION \
            --resource-manager-tags=TAG1,TAG2,...
        

  * To attach or overwrite tags on an existing node pool, run the following command:
        
        gcloud container node-pools update NODE_POOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=CLUSTER_LOCATION \
            --resource-manager-tags=TAG1,TAG2,...
        




Replace the following:

  * `NODE_POOL_NAME`: The name of the node pool.
  * `CLUSTER_NAME`: The name of the cluster.
  * `CLUSTER_LOCATION`: The Compute Engine region or zone of the cluster.
  * `TAG1,TAG2,...`: A comma-separated list of up to five key-value pairs to attach. Each key-value pair can use either permanent IDs (for example, `tagKeys/123456789012=tagValues/987654321098`) or namespaced names (for example, `example-project/env=dev,123456789012/team=sre`).



### Attach tags to Autopilot clusters or auto-provisioned node pools

To attach tags to nodes in an Autopilot cluster or to new auto-provisioned node pools in a Standard cluster with node auto-provisioning enabled, use the `--autoprovisioning-resource-manager-tags` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CLUSTER_LOCATION \
        --autoprovisioning-resource-manager-tags=TAG1,TAG2,...
    

To remove all tags attached to a node pool by using the GKE API, pass an empty value to the flag (for example, `--resource-manager-tags=""` or `--autoprovisioning-resource-manager-tags=""`). For more information about node pool tag syntax and inheritance, see [Selectively enforce network firewall policies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies#attach-tags-standard).

## Delete tag keys and tag values

Before you delete tag keys and values, ensure that the tags are detached from all resources. Then, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting) to delete the keys and values.

## Identity and Access Management conditions and Tags

You can use [Tags and IAM conditions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags) to conditionally grant role bindings to users in your project hierarchy. When you change or delete the tag attached to a cluster, GKE can remove user access to that cluster if an IAM allow policy with conditional role bindings has been applied. You can use IAM deny policies with tags to achieve goals like [protecting critical clusters from deletion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#prevent-deletion-deny-policies).

Authorization to list and create GKE clusters is checked at the project level, not at the individual cluster level. If you use conditional IAM role bindings with cluster-level Tags to restrict access to specific clusters, those users might experience errors when attempting to list or create clusters in the project. To avoid these errors, attach a tag to the parent project and use a conditional role binding to grant the list or create access. For information about roles and permissions, see the [IAM roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/container).

## What's next

  * [Learn how to set an organization policy with Tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).
  * Learn more about how to [manage tags and attach tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).
  * [See the other services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * [Learn how to use tags with IAM](https://docs.cloud.google.com/iam/docs/tags-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
