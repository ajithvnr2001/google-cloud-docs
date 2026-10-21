---
url: https://docs.cloud.google.com/compute/docs/tag-resources/
title: Manage tags for resources \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:24.077939+00:00
---

# Manage tags for resources  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tag-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage tags for resources Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to create and manage tags for Compute Engine resources. A tag is a key-value pair that can be attached to a Google Cloud resource. Tags are used for several purposes, including:

  * Conditionally allow or deny policies based on whether a resource has a specific tag.
  * Define sources and targets in global network [firewall policies](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) and regional network firewall policies.
  * Organizing resources in a logical manner.



After creating a tag and granting appropriate access to both the tag and the resource, you can attach the tag as a key-value pair. You can attach exactly one value to a resource for a given key. For example, if you attach the `environment: development` tag, then you cannot attach the `environment: production` or `environment: test` tags. Each resource can have a maximum of 50 key-value pairs attached.

To attach tags to resources, you must create a tag binding resource that links the tag value to the Google Cloud resource. For more information on tags and how they work, review the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) document.

## Before you begin

  * Read the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) on the Resource Manager documentation.
  * Read the [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) on the Resource Manager documentation.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create and manage tags for Compute Engine resources, ask your administrator to grant you the following IAM roles on your organization or project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To create and manage tags: [Tag Administrator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) 
  * To manage existing tags: [Tag User role ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage tags for Compute Engine resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage tags for Compute Engine resources:

  * View tags: 
    * `resourcemanager.tagKeys.get`
    * `resourcemanager.tagKeys.list`
    * `resourcemanager.tagValues.list`
    * `resourcemanager.tagValues.get`
    * `compute.instances.listTagBindings`
    * `compute.instances.listEffectiveTags`
    * `resourcemanager.projects.get`
  * Create tags: 
    * `resourcemanager.tagKeys.create`
    * `resourcemanager.tagValues.create`
    * `resourcemanager.tagKeys.setIamPolicy`
    * `resourcemanager.tagValues.setIamPolicy`
  * Manage tags: 
    * `resourcemanager.tagKeys.update`
    * `resourcemanager.tagValues.update`
    * `resourcemanager.tagKeys.delete`
    * `resourcemanager.tagValues.delete`
    * `resourcemanager.tagKeys.getIamPolicy`
    * `resourcemanager.tagValues.getIamPolicy`
    * `resourcemanager.tagKeys.setIamPolicy`
    * `resourcemanager.tagValues.setIamPolicy`
  * Add or remove tags for a compute instance: 
    * `compute.instances.createTagBinding`
    * `compute.instances.deleteTagBinding`
    * `resourcemanager.tagValueBindings.create`
    * `resourcemanager.tagValueBindings.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported resources

Compute Engine supports tagging for the following resources:

  * **Only after resource creation** :

    * Managed instance groups (MIGs)
    * Health checks
  * **Both during and after resource creation** :

    * Virtual machine (VM) instances
    * Disks
    * Images
    * Snapshots
    * VPC networks
    * VPC subnetworks
    * VPC firewall rules
    * VPC routes
    * Cloud Routers



## Adding tags to a resource

You can attach existing tags to certain resources. After the resource is created, attach tags to that resource by using the following instructions.

###  Console 

Depending on the resource type, the exact steps might vary. For example, the following steps attach a tag to a VM: 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. In the **Name** column, click the name of the VM for which you want to add tags.

  4. From the **VM instance** details page, complete the following steps:

     1. Click **Edit**.
     2. In the **Basic information** section, click **Manage tags** and add the tags that you want for the instance.
     3. Click **Save**.



###  gcloud 

For information about how to use these flags, read [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#gcloud_8) in the Resource Manager documentation.

For example, the following command attaches a tag to a VM:
    
    
    gcloud resource-manager tags bindings create \
        --location=LOCATION_NAME \
        --tag-value=tagValues/TAGVALUE_ID \
        --parent=FULL_RESOURCE_NAME
    

Replace the following:

  * `LOCATION_NAME`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance is located. For a global resource, omit the `--location` flag.
  * `TAGVALUE_ID`: the numeric ID of the tag value
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the VM instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [VM instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)



###  REST 

To attach a tag to a resource, you must first create a JSON representation of a tag binding that includes the permanent ID or namespace name of the tag value and the permanent ID of the resource. For more information about the format of a tag binding, see the [tagBindings reference](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings).

To attach the tag to a zonal resource, such as a VM instance, use the `tagBindings.create` method with the regional endpoint where your resource is located. For example:
    
    
    POST https://LOCATION_NAME-cloudresourcemanager.googleapis.com/v3/tagBindings

The request body can be one of the following two options:
    
    
    {
      "parent": "FULL_RESOURCE_NAME",
      "tagValue": "tagValue/TAGVALUE_ID"
    }
    
    
    
    {
      "parent": "FULL_RESOURCE_NAME",
      "tagValueNamespacedName": TAGVALUE_NAMESPACED_NAME
    }

Replace the following:

  * `LOCATION_NAME`: the zonal or regional [location of the resource](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). For a VM instance, specify the zone. For a global resource, omit the `LOCATION_NAME-` parameter
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the VM instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [VM instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * `TAGVALUE_ID`: the permanent ID of the tag value that is attached—for example: `4567890123`

  * `TAGVALUE_NAMESPACED_NAME`: the namespace name of the tag value that is attached and is of the format: `parentNamespace/tagKeyShortName/tagValueShortName`




## Adding tags to a resource during resource creation

In certain scenarios, you might want to tag resources during resource creation, rather than after the resource is created.

###  Console 

Depending on the resource type, the exact steps might vary. The following steps are for a VM:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create instance**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  4. In the navigation menu, click **Advanced**. In the **Advanced** pane that appears, do the following:

     1. Expand the expand_more**Manage tags and labels** section.
     2. Click add**Add tags**.
     3. In the **Tags** pane that opens, follow the instructions to add a tag to the instance.
     4. Click **Save**.
  5. Specify other configuration options for your instance. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the VM, click **Create**.




###  gcloud 

To attach a tag to a resource during resource creation, add the `--resource-manager-tags` flag with the respective `create` command. For example, to attach a tag to a VM, use the following command:
    
    
      gcloud compute instances create INSTANCE_NAME \
          --zone=ZONE \
          --resource-manager-tags=tagKeys/TAGKEY_ID=tagValues/TAGVALUE_ID

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance
  * `ZONE`: the zone that contains the VM instance
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`.

###  REST 

Make a `POST` request to the following URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances

Include the following request JSON body:
    
    
    {
      "name": INSTANCE_NAME,
      "params": {
        "resourceManagerTags": {
          "tagKeys/TAGKEY_ID": "tagValues/TAGVALUE_ID",
        },
      }
      // other fields omitted
    }

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



## Use tags with firewall rules

To securely enable network traffic to a specific Compute Engine instance, you can apply a network tag or a secure tag to the instance. Then, you can create a firewall rule that targets that tag. This is helpful for managing access to your instances at scale.

**Note:** Network tags are different from secure tags. For more information about the differences between secure tags and network tags, see [Comparison of secure tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).

For example, assume you have a compute instance that runs a web server, and you created a new web application that needs to be accessible to the public on the standard HTTP port (80). You can use a network or secure tag to implement a firewall rule that grants HTTP access only to the compute instance that the web server runs on.

For instructions on how to create tags for use in firewall policies, see the following:

  * To use network tags with VPC firewall rules, see [Add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).
  * To use secure tags with hierarchical firewall policies, global and regional network firewall policies, or for use with sources connected using VPC Network Peering, see [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).



For information about whether to use service accounts or network tags to define targets and sources for network ingress rules, see [Filter by service account versus network tag](https://docs.cloud.google.com/firewall/docs/firewalls#service-accounts-vs-tags).

## Detaching a tag from a resource

You can detach a tag from a resource by deleting the tag binding resource.

To review instructions on how to detach tags, see [Detaching a tag from a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching) in the Resource Manager documentation.

###  Console 

Depending on the resource type, the exact steps might be a bit different. For example, the following steps detaches a tag from a VM instance:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. In the **Name** column, click the name of the instance for which you want to remove tags.

  4. From the **VM instance** details page, complete the following steps:

     1. Click **Edit**.
     2. For resource manager tags, in the **Basic information** section, click **Manage Tags**. Remove the tags that you want for the instance. You can only remove tags that were directly added to the instance.
     3. For network tags, in the **Networking** section, remove the tag from the **Network tags** list.
     4. Click **Save**.



###  gcloud 

To detach a tag from a compute instance, use the [`resource-manager tags bindings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete):
    
    
    gcloud resource-manager tags bindings delete \
        --location=LOCATION_NAME \
        --tag-value=tagValues/TAGVALUE_ID \
        --parent=FULL_RESOURCE_NAME
    

Replace the following:

  * `LOCATION_NAME`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance is located. For a global resource, omit the ``\--location=LOCATION_NAME \`` flag
  * `TAGVALUE_ID`: the numeric ID of the tag value
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)



To update or replace an existing tag binding to another one, detach the old tag binding and attach the new one.

###  REST 

To delete a tag binding attached to a resource, such as a compute instance, use the [`tagBindings.delete` method](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/delete) with the regional endpoint where your resource is located.
    
    
    DELETE https://LOCATION_NAME-cloudresourcemanager.googleapis.com/v3/{name=TAGBINDINGS_NAME}
    

Replace the following:

  * `LOCATION_NAME`: the zonal or regional [location of the resource](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). For an instance, specify the zone. For a global resource, omit the `LOCATION_NAME-` parameter
  * `TAGBINDINGS_NAME`: the permanent ID of the TagBinding; for example: `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F1234567890/tagValues/567890123456`



## Viewing tags attached to a resource

To review detailed instructions on how to list tags, see [Listing all tags attached to a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#listing_tags) in the Resource Manager documentation.

###  Console 

Depending on the resource type, the exact steps might be a bit different. For example, the following steps show how to view tags for a VM instance:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. In the **Name** column, click the name of the instance for which you want to view tags.

  4. From the **VM instance** details page, look for tags under the **Tags** section.




###  gcloud 

To get a list of tag bindings directly attached to a resource, use the `gcloud resource-manager tags bindings list` command. If you add the `--effective` flag, you will also return a list of tags inherited by this resource. For example:
    
    
    gcloud resource-manager tags bindings list \
        --location=LOCATION_NAME \
        --parent=FULL_RESOURCE_NAME
    

Replace the following:

  * `LOCATION_NAME`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance is located. For a global resource, omit the ``\--location=LOCATION_NAME \`` flag
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
          

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)



If you add the `--effective` flag to the `tags bindings list` command, you also return a list of all tags inherited by this resource.

The output is similar to the following:
    
    
    namespacedTagKey: 961309089256/environment
    namespacedTagValue: 961309089256/environment/production
    tagKey: tagKeys/417628178507
    tagValue: tagValues/247197504380
    inherited: true
    

If all tags evaluated on a resource are directly attached, the `inherited` field is false and is omitted.

###  REST 

To list the tag bindings attached to a regional resource, such as Compute Engine instances, use the `tagBindings.list` method with the regional endpoint where your resource is located. For example:
    
    
    GET https://LOCATION_NAME-cloudresourcemanager.googleapis.com/v3/tagBindings
    
    {
        "parent": "FULL_RESOURCE_NAME"
    }
    

Replace the following:

  * `LOCATION_NAME`: the zonal or regional [location of the resource](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). For an instance, specify the zone. For a global resource, omit the `LOCATION_NAME-` parameter
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
          

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)



## What's next

  * [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)
  * [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)
  * [Bind secure tags to VM instances](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind-tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
