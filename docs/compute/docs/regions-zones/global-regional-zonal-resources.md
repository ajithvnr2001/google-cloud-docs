---
url: https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources/
title: Global, regional, and zonal resources \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:12.658655+00:00
---

# Global, regional, and zonal resources  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Global, regional, and zonal resources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes global, regional, and zonal Compute Engine resources.

Google Cloud resources are hosted in [multiple locations](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) worldwide. These locations are composed of regions with zones within those regions. Putting resources in different zones in a region provides isolation from many types of infrastructure, hardware, and software failures. Putting resources in different regions provides an even higher degree of failure independence. You can design robust systems by spreading resources across different failure domains.

All Compute Engine resources are either global, regional, or zonal in scope. For example, images are a global resource, but regional static IPs are regional, and Persistent Disks can be either regional or zonal resources.

The scope of the resource determines how accessible the resource is to other resources:

**Global resources** are accessible by resources in any region or zone, For example, virtual machine (VM) instances from different zones can use the same global image.

**Regional resources** are accessible only to resources within the same region. For example, a regional static external IP address is accessible only by resources within the same region. For a VM instance to use a specific static external IP, the VM must be in a zone that is in the same region as the address.

**Zonal resources** are accessible only to resources within the same zone. Zonal resources can also access regional and global resources. For example, a VM instance can access a global image and regional network resources.

Scope | Accessibility | Naming uniqueness | Examples  
---|---|---|---  
Global | Any region or zone in the project | Project-wide | Images, VPC networks, instance templates  
Regional | Any zone within the same region | Region-wide | Subnets, regional static IPs, regional disks, instance templates  
Zonal | Same zone only | Zone-wide | VM instances, zonal disks and  
Hyperdisk Storage Pools, machine types |  |  |   
  
Within a project, a zonal resource must have a unique name within its zone. For example, you can have a VM named `my-instance` in zone `us-central1-a` and another VM named `my-instance` in zone `us-central1-b` within the same project.

## Global resources

Global resources are accessible by any resource in any zone within the same project. When you create a global resource, you don't need to provide a scope specification.

**Note:** Although all Compute Engine resources are classified as global, regional, or zonal in scope, some global resources, like custom images, disk snapshots, and machine images, allow you to choose a **multi-region** or **region** storage location for their underlying data. Even when stored in a multi-region, the resource itself behaves as a global resource.

Global resources include:

Addresses
    The Addresses collection contains any global static external IP addresses that you have reserved for your project. Global static external IP addresses are a global resource and are used for global load balancers.
Images
    Images are used by any instance or disk resource in the same project as the image. Google provides preconfigured images that you can use to boot your instance. You can customize one of these images, or you can build your own image. Optionally, you can [share images across projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects).
Snapshots
    Hyperdisk and Persistent Disk standard and archive snapshots are global resources that can be used to create a disk in other projects. Optionally, you can [share snapshots across projects](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#sharing_snapshots).
Global instance templates
    A global instance template can be used to create compute instances and managed instance groups. Instance templates can be global or regional resources. However, if you specify zonal resources in a global instance template, then you can use that template only in the same zone as the specified zonal resources, and if you specify regional resources in a global instance template, then you can use that template only in the same region as the specified regional resources. Read about [Regional and global instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates).
Cloud Interconnects
    A Cloud Interconnect is a highly available connection from your on-premises network to Google's network. This connection is a global resource. However, interconnect attachments, which run inside of this connection, are regional resources.
Cloud Interconnect locations
    A Cloud Interconnect location is a physical connection point for Cloud Interconnect near your network. There is one Cloud Interconnect location for every available colocation facility and edge availability domain. Cloud Interconnect locations are read-only, global resources.
VPC network
    A VPC network is a global resource, but individual subnets are regional resources.
Firewalls
    Firewalls apply to a single VPC network and are considered a global resource because packets can reach them from other networks.
Routes
    Routes let you create complex networking scenarios. You can manage how traffic is routed for a specific IP range. Routes are similar to how a router directs traffic within a local area network. Routes apply to VPC networks within a Google Cloud project and are considered global resources.
Global operations
    

An operation is a per-zone resource, a per-region resource, or a global resource. If you are performing an operation on a global resource, the operation is considered a global operation. For example, inserting an image is considered a global operation because images are a global resource.

**Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

### Regional views of global resources

To enhance reliability for services and applications that depend on the metadata of global resources, you can access some global resource metadata through regionalized read-only endpoints. These endpoints let you fetch resource metadata through the control plane for a specific Google Cloud region, isolating your API calls from potential issues in the global control plane or in other regions. For more information, see [Regional views of global resources](https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources).

## Regional resources

Regional resources are accessible by any resources within the same region. For example, if you reserve a static external IP address in a specific region, that static external IP address can only be assigned to instances within that region. Each region also has one or more zones. For a list of available regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

Regional resources include:

Addresses
    The Addresses collection contains any regional static external IP addresses that you have reserved for your project. Static external IP addresses are a regional resource that are used by instances that are in the same region as the address, by regional forwarding rules for regional load balancers, and for protocol forwarding.
Cloud Interconnect attachments
    A VLAN attachment allocates a VLAN on your Cloud Interconnect and connects that VLAN to a VPC network. An attachment is a regional resource, but a Cloud Interconnect connection is a global resource.
Subnets
    Subnets regionally segment the network IP space into prefixes (subnets) and control which prefix an instance's internal IP address is allocated from.
Placement policies
    A [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) controls how closely to place VMs in relation to one another. This can help reduce the impact of host system failures or network latency.
Regional instance templates
    A regional instance template can be used to create VMs and managed instance groups. A regional instance template is accessible only by resources within the same region. If you specify zonal resources in a regional instance template, then you can use that template only in the same zone as the specified zonal resources.
Regional managed instance groups
    Regional managed [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) are collections of identical instances that span multiple zones. Regional managed instance groups let you spread app load across multiple zones, rather than confining your app to a single zone or having to manage multiple instance groups across different zones.
Regional disks
    [Regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) provide durable storage and replication of data between two zones within the same region. In a failover situation, you can force-attach a regional disk to another instance within the same region. You cannot force attach a zonal disk to an instance. Optionally, you can [copy a disk to another project](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd), which lets other projects make images and snapshots from these disks but doesn't let instances in other projects attach the disks. To protect disk data in the unlikely event of a regional outage, you can enable Asynchronous Replication.
Instant snapshots
    Instant [snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of regional disks are regional resources. They are only accessible within the same region as the disk.
Regional operations
    

An operation is a per-zone resource, a per-region resource, or a global resource. If you are performing an operation on a regional resource, the operation is considered a per-region operation. For example, reserving an address is considered regional operation because addresses are a region-specific resource.

**Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

## Zonal resources

Resources that are hosted in a zone are called _per-zone resources_. Zone-specific resources, or per-zone resources, are unique to that zone and are only usable by other resources in the same zone. For example, an instance is a per-zone resource. When you create an instance, you must provide the zone where the instance is located. The instance can access other resources within the same zone, and can access global resources, but it can't access other per-zone resources in a different zone, such as a disk resource or a VPC subnet.

For a list of available zones and the machine series available in each zone, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

**Note:** One exception is that instances in one zone can communicate with instances in another zone if both instances belong to the same [VPC network](https://docs.cloud.google.com/compute/docs/vpc).

Per-zone resources include:

Instances
    A compute instance is located within a zone and can access global resources or resources within the same zone.
Zonal Google Cloud Hyperdisks and Persistent Disks
    Zonal disks are accessed by other compute instances within the same zone. You can attach a disk only to instances in the same zone as the disk. You can't attach a disk to an instance in another zone. Optionally, you can [share disk resources across projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects), which lets other projects make images and snapshots from these disks but doesn't let instances in other projects attach the disks.
Hyperdisk pools
    Hyperdisk [pools](https://docs.cloud.google.com/compute/docs/disks/pools) are zonal resources. Disks in a pool must be in the same zone as the pool.
Instant snapshots
    Instant [snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of zonal disks are zonal resources. They are only accessible within the same zone as the disk.
Machine types
    Machine types are per-zone resources. Instances and disks can only use machine types that are in the same zone.
Zonal managed instance groups
    A zonal managed [instance group](https://docs.cloud.google.com/compute/docs/instance-groups) uses an instance template to create a group of identical instances within a single zone. You manage compute instances in a managed instance group as a single entity, rather than managing individual instances.
GPUs
    GPUs are zonal resources. For information about the zones in which GPUs are available, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
Cloud TPUs
    TPUs are zonal resources. For information about the zones in which TPUs are available, see [Availability](https://docs.cloud.google.com/tpu/docs/tpus#availability).
Per-zone operations
    

An operation is a per-zone resource, a per-region resource, or a global resource. If you are performing an operation on a zone-specific resource, the operation is considered a per-zone operation. For example, inserting an instance is considered a per-zone operation because the operation is being performed on a zone-specific resource, an instance.

**Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

## Aggregate lists

By default, a request to return a list of resources is scoped to a particular control plane. For example, when you query the API for a list of instances, you must provide the zone for which you want to list instances. To list resources across all zones or regions, you can perform an aggregate list query. Each per-region and per-zone resource has an aggregate list URI that can be queried to list all resources of that type. For example, to list all compute instances across all zones that were created in a project, you can make a request to the following URI:
    
    
    https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/aggregated/instances
    

Similarly, to list all IP addresses across all regions, make a request to the following URI:
    
    
    https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>>/aggregated/addresses
    

For more information, see the [`aggregateList`](https://docs.cloud.google.com/compute/docs/reference/latest/addresses/aggregatedList) method for that resource.

## What's next

  * Learn more about [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [geographical management of data](https://docs.cloud.google.com/docs/geography-and-regions#geographic_management_of_data).
  * Learn about [instances](https://docs.cloud.google.com/compute/docs/instances).
  * Work through [Linux Getting Started](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).
  * Work through [Windows Getting Started](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance).
  * Learn how to [set a default project, zone, or region](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
