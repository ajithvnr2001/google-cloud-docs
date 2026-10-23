---
url: https://docs.cloud.google.com/vpc/docs/using-legacy/
title: Manage legacy networks \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:53.226574+00:00
---

# Manage legacy networks  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/using-legacy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage legacy networks

Legacy networks are not recommended and can no longer be created. Many newer Google Cloud features are not supported in legacy networks. Instead, use [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc). For more information about replacing legacy networks, see [Replace legacy networks](https://docs.cloud.google.com/vpc/docs/legacy#replacing-legacy).

This page describes modifying Google Cloud [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy). Use this page only if you have an existing setup that has a legacy network.

**Note:** The [IPv4Range](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) field for creating legacy networks is deprecated and is no longer available for any Google Cloud project. You cannot create new legacy networks. However, existing legacy networks are not affected and continue to operate normally.

## Restrictions

Legacy networks do not support the following Google Cloud features. To use these features, you must use [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) instead.

  * [VPC subnets](https://docs.cloud.google.com/vpc/docs/vpc)
  * [Alias IP](https://docs.cloud.google.com/vpc/docs/alias-ip)
  * [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * All [private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options)



Single-region legacy networks can be converted into VPC networks using [Convert a single region to a VPC network](https://docs.cloud.google.com/vpc/docs/using-legacy#convert). If you have multi-regional legacy networks, you must migrate resources to a single region before you use the conversion tool.

## Create a legacy network

You can no longer create a legacy network.

If you try to create a legacy network, this error is displayed:
    
    
    Creation of legacy mode networks is deprecated. Please create a subnet mode
    network instead by removing the IPv4Range field and adding the
    autoCreateSubnetworks field to your network insert request.
    

## Migrate VMs out of a legacy network

You can migrate your virtual machine (VM) instances out of your legacy network to a VPC network. For instructions, see [Migrating a VM between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).

## Delete a legacy network

For a legacy network, you can explicitly delete the network only if the network is not in use by any resources.

To delete the network:
    
    
    gcloud compute networks delete LEGACY_NETWORK_NAME
    

Replace the following:

  * `LEGACY_NETWORK_NAME`: the name of the legacy network that you want to delete.



## Convert a single-region legacy network to a VPC network

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use the single-region conversion tool to convert a legacy network to a custom mode VPC network in the same project. All resources in the legacy network must be located in a _single region_. See [Single-region conversion details](https://docs.cloud.google.com/vpc/docs/legacy#single-region-conversion) for more information.

### Limitations of the single-region conversion tool

  * After the conversion has started, it cannot be canceled.

  * All resources must exist in a single region before you can convert a legacy network to a VPC network. If you have resources in multiple regions, the conversion fails and Google Cloud takes no action. You must manually [move resources](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) to a single region or remove them from regions other than the one you're migrating. You can't, for example, convert resources region by region into multiple VPC networks.

  * During the conversion, the network continues to pass traffic, and communication is not interrupted. However, changes to network resources are limited. Network resources can be deleted, but certain deletions are blocked until the conversion is complete. Network resources cannot be created during the conversion.

  * You can't revert a converted VPC network back to a legacy network.

  * If your legacy network contains Google Kubernetes Engine clusters, your GKE clusters must be upgraded _after_ you convert the legacy network to ensure that components operate correctly. For more information, see Converting a legacy network that contains GKE clusters.




### Prepare to convert a legacy network

  1. Consider performing the conversion when user activity on the network is low.

  2. To use the conversion too, all resources in the legacy network must be in one region. If you have resources in multiple regions, decide which region you want to use, and [move your instances](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) to that region. Other resources not in that region must be manually moved or deleted.

  3. Ensure the last two internal IP addresses in the network CIDR range are not in use. These IP addresses are [unusable addresses](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) in VPC network subnets.

For example, for a network with an IP address range of `10.240.0.0/16`, verify that `10.240.255.254` and `10.240.255.255` are not assigned to any resources.

  4. Manually scale up any instance groups to cover any expected need during the conversion and [disable autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler).

If an autoscaler is enabled during the conversion, and the autoscaler attempts to create a new instance, you might see an [error](https://docs.cloud.google.com/vpc/docs/using-legacy#trouble-create-vms).

  5. If your legacy network contains GKE clusters, see Converting a legacy network that contains GKE clusters.




### Convert a legacy network

Using the tool to convert from a legacy network to a VPC network does not disrupt network traffic; your resources continue to operate normally. If the network conversion fails for any reason, the network conversion is automatically rolled back. If you run into errors, see the troubleshooting section for solutions.

  1. Convert the legacy network to a VPC network.

The conversion is a long-running operation. The time it takes depends on the number of resources on the network. Converting a network takes at least seven minutes to complete. Large networks can take over 20 minutes per 1,000 VMs. During the conversion, no changes to the network are allowed.

###  gcloud 
         
         gcloud beta compute networks update LEGACY_NETWORK_NAME \
             --switch-to-custom-subnet-mode
         

Replace the following:

     * `LEGACY_NETWORK_NAME`: the name of the legacy network that you want to convert.

###  API 
    
    POST https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/networks/LEGACY_NETWORK_NAME/switchToCustomMode
    

Replace the following:

     * `PROJECT_ID`: the project that contains the legacy network that you want to convert.

     * `LEGACY_NETWORK_NAME`: the name of the legacy network that you want to convert.

You can monitor the status of the operation using the [`globalOperations.get`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalOperations/get) method or the [`globalOperations.wait`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalOperations/wait) method.

  2. After the operation is complete, check that the network's subnet mode is `CUSTOM`.

List your networks to see their subnet mode:
         
         gcloud compute networks list
         

  3. If you previously disabled any autoscalers, [re-enable the autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler).

  4. In the VPC network, [add subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you want to create new resources.

  5. Recreate any resources that weren't included in the conversion.




### Convert a legacy network that contains GKE clusters

If your legacy network contains GKE clusters, your GKE clusters must be upgraded _after_ the conversion to ensure that components operate correctly.

Use the [GKE network conversion script](https://github.com/GoogleCloudPlatform/gke-network-conversion) to perform network, cluster, and node pool upgrades.

If you have converted a legacy network to a VPC network without using the script, you can use the script to make the necessary cluster and node pool upgrades.

### Update resources after a single-region conversion

Legacy networks do not have subnetworks, so any scripts or commands used to create or modify resources on a legacy network do not specify a subnetwork. VPC networks do contain subnetworks; therefore, scripts and commands that manage resources in VPC networks normally require that you specify a subnetwork.

However, to ensure scripts and commands that were used to manage the legacy network still work after converting to a VPC network, the following applies:

  * If you run a gcloud CLI command or make an API request that specifies the _same region_ that the legacy network was using at the time of the conversion, the subnetwork is automatically set to the subnetwork that was created during the conversion operation.

  * If you run a gcloud CLI command or make an API request that specifies a _different region_ from the region that the legacy network was using at the time of the conversion, you must specify a subnetwork.




### Troubleshooting a single-region conversion

#### Conversion attempt: Cannot convert network with VMs in multiple regions

When you try to convert my network, you get this error:
    
    
      ERROR: (gcloud.compute.networks.switchToCustomMode) ResponseError: code=400, message=Only single-region legacy networks are supported. This network has at least one resource in us-central1 and at least one resource in asia-east1.

Solution: Converting the mode of a network from legacy to custom mode only works when all of these resources exist in a single region:

  * instances, including stopped instances
  * instance group
  * managed instance groups
  * forwarding rules
  * routers



To proceed, either migrate all resources to one region or delete them before converting.

#### Conversion attempt: Cannot convert network due to rate limit exceeded

When you try to convert my network, you get this error:
    
    
      Error 403: Rate Limit Exceeded, rateLimitExceeded
      

Solution: The conversion operation has a global quota for concurrent operations. If you see this error, wait five minutes and try again.

#### During conversion: Cannot create VMs in a network that is switching mode

When you try to create, delete or update VMs, you get this error:
    
    
      ERROR: (gcloud.compute.instances.create) ResponseError: code=400, message="Resource not ready".
      

Solution: Switching the mode of a network locks down the network so that no new VMs can be created in it until the operation is complete. You can create, delete, and update VMs after the conversion is complete.

#### After conversion: Cannot create resources without specifying subnetwork

When you try to create new resources on the network, you get this error:
    
    
      gERROR: (gcloud.compute.instances.create) ResponseError: code=400, message=Subnetwork should be specified for custom subnetmode network.

Solution: Update resource creation scripts to specify the subnetwork of the resource.

#### After conversion: Cannot delete subnetwork

When you try to delete the converted network, or the subnetwork that was created during the conversion operation, you get this error:
    
    
      ERROR: (gcloud.compute.networks.subnets.delete) Could not fetch resource:
       - Cannot delete subnetwork created during legacy network to custom-mode conversion for a day. Please try again tomorrow.
       

Solution: Wait for a day, then try deleting the network or subnetwork.

## Manually migrate to a VPC network

In cases where you can't do a single-region conversion, you can recreate all resources in your legacy network in a VPC network. There is no automated solution to convert multiple regions in a legacy network to a VPC network.

  1. [Create a custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks), and then add a subnet in every region that you're using.

  2. In your legacy network, record the details of your existing resources. You need this information so that you can recreate them in the VPC network.

To help you get started, the following items are some common resources that you might need to recreate.

**Note:** This list is not exhaustive. Your environment might have other resources that you need to record and recreate.
     * [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network)
     * [Load balancers](https://docs.cloud.google.com/load-balancing/docs/how-to)
     * [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls)
     * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates)
     * [Routes](https://docs.cloud.google.com/vpc/docs/using-routes)
     * [VM instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
     * [VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to)
     * [Protocol forwarding](https://docs.cloud.google.com/compute/docs/protocol-forwarding)
  3. Recreate your resources with the same configurations that you recorded. Some resources, like VM instances, require additional planning and steps to recreate. For some examples, see the Special considerations section.

If possible, recreate your resources before removing the existing ones. That way, you can test and verify that the new resources operate as expected before you remove the existing ones. Recreating might not be possible for all resources; you might exceed a quota or might not be able to reuse an existing naming convention.

  4. Delete your old resources and legacy network.




### Special considerations for manual migration

Simply recreating resources can result in disruptions to your services. To avoid disruptions, you might need to take additional actions before you migrate. For example, you might need to duplicate your service's infrastructure so that you can redirect traffic from the old network to the new one. Or, you might need to take snapshots of existing VM instances to preserve and move their data to new instances.

The following scenarios are examples that you might want to plan for before you migrate:

**Note:** This list is not exhaustive. Your environment might have different resources or configurations that you might need to consider. For more information, view the relevant product guides.

  * If you're using an ephemeral external IP address and you want to keep using it, promote it to a [reserved static IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address).
  * If you need to move VM instances, you can [manually recreate them](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones), or use Google Cloud to [create a similar instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) from an existing one. If you create a similar instance, Google Cloud doesn't copy existing data, but you can use [snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) and [boot disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) to do that.
  * If you have a load balanced service and want to keep it running, add a duplicate backend in the VPC network. You can start directing traffic to the backend in the VPC before you remove the backend in the legacy network.



## What's next

  * For information about routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).
  * For information about firewall rules, see [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
