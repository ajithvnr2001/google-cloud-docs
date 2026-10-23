---
url: https://docs.cloud.google.com/architecture/building-a-hybrid-render-farm/
title: Build a hybrid render farm \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:58.056525+00:00
---

# Build a hybrid render farm  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/building-a-hybrid-render-farm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Build a hybrid render farm Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-11-26 UTC

This document provides guidance on extending your existing, on-premises render farm to use compute resources on Google Cloud. The document assumes that you have already implemented a render farm on-premises and are familiar with the basic concepts of visual effects (VFX) and animation pipelines, queue management software, and common software licensing methods.

## Overview

Rendering 2D or 3D elements for animation, film, commercials, or video games is both compute- and time-intensive. Rendering these elements requires a substantial investment in hardware and infrastructure along with a dedicated team of IT professionals to deploy and maintain hardware and software.

When an on-premises render farm is at 100-percent utilization, managing jobs can become a challenge. Task priorities and dependencies, restarting dropped frames, and network, disk, and CPU load all become part of the complex equation that you must closely monitor and control, often under tight deadlines.

To manage these jobs, VFX facilities have incorporated queue management software into their pipelines. Queue management software can:

  * Deploy jobs to on-premises and cloud-based resources.
  * Manage inter-job dependencies.
  * Communicate with asset management systems.
  * Provide users with a user interface and APIs for common languages such as Python.



While some queue management software can deploy jobs to cloud-based workers, you are still responsible for connecting to the cloud, synchronizing assets, choosing a storage framework, managing image templates, and providing your own software licensing.

The following options are available for building and managing render pipelines and workflows in a cloud or hybrid cloud environment:

  * If you don't already have on-premises or cloud resources, you can use a software as a service (SaaS) cloud-based render service such as [Conductor](https://www.conductortech.com/).
  * If you want to manage your own infrastructure, you can build and deploy the cloud resources described in this document.
  * If you want to build a custom workflow based on your specific requirements, you can work with Google Cloud service integrator partners like [Gunpowder](https://gunpowder.tech/) or [Qodea](https://qodea.com/). This option has the benefit of running all the cloud services in your own secure Google Cloud environment.



To help determine the ideal solution for your facility, contact your Google Cloud representative.

**Note:** Production notes appear periodically throughout this document. These notes offer best practices to follow as you build your render farm.

## Connecting to the cloud

Depending on your workload, decide how your facility connects to Google Cloud, whether through a partner ISP, a direct connection, or over the public internet.

### Connecting over the internet

Without any special connectivity, you can connect to Google's network and use our [end-to-end security model](https://cloud.google.com/security/) by accessing Google Cloud services over the internet. Utilities such as the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and resources such as the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) all use secure authentication, authorization, and encryption to help safeguard your data.

### Cloud VPN

No matter how you're connected, we recommend that you use a virtual private network (VPN) to secure your connection.

[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) helps you securely connect your on-premises network to your Google [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) through an IPsec VPN connection. Data that is in transit gets encrypted before it passes through one or more VPN tunnels.

Learn how to [create a VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) for your project.

### Customer-supplied VPN

Although you can set up your own VPN gateway to connect directly with Google, we recommend using Cloud VPN, which offers more flexibility and better integration with Google Cloud.

### Cloud Interconnect

Google supports multiple ways to connect your infrastructure to Google Cloud. These enterprise-grade connections, known collectively as [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect), offer higher availability and lower latency than standard internet connections, along with reduced egress pricing.

[Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) lets you establish high-bandwidth, dedicated connectivity to Google Cloud for your data in another cloud. Doing so reduces network complexity, reduces data transfer costs, and enables high-throughput, multicloud render farms.

### Dedicated Interconnect

[Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) provides direct physical connections and RFC 1918 communication between your on-premises network and Google's network. It delivers connection capacity over the following types of connections:

  * One or more 10 Gbps Ethernet connections, with a maximum of eight connections or 80 Gbps total per interconnect.
  * One or more 100 Gbps Ethernet connections, with a maximum of two connections or 200 Gbps total per interconnect.



Dedicated Interconnect traffic is not encrypted. If you need to transmit data across Dedicated Interconnect in a secure manner, you must establish your own VPN connection. Cloud VPN is _not_ compatible with Dedicated Interconnect, so you must supply your own VPN in this case.

### Partner Interconnect

[Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) provides connectivity between your on-premises network and your VPC network through a supported service provider. A Partner Interconnect connection is useful if your infrastructure is in a physical location that can't reach a Dedicated Interconnect colocation facility or if your data needs don't warrant an entire 10-Gbps connection.

### Other connection types

Other ways to connect to Google might be available in your specific location. For help in determining the best and most cost-effective way to connect to Google Cloud, contact your Google Cloud representative.

## Securing your content

To run their content on any public cloud platform, content owners like major Hollywood studios require vendors to comply with security best practices that are defined both internally and by organizations such as the [MPAA](https://www.mpaa.org/). Google Cloud offers zero-trust security models that are built into products like Google Workspace, Chrome Enterprise Premium, and BeyondProd.

Each studio has different requirements for securing rendering workloads. You can find security whitepapers and [compliance documentation](https://cloud.google.com/security/compliance/ise/) at [cloud.google.com/security](https://cloud.google.com/security/).

If you have questions about the security compliance audit process, contact your Google Cloud representative.

## Organizing your projects

_Projects_ are a core organizational component of Google Cloud. In your facility, you can organize jobs under their own project or break them apart into multiple projects. For example, you might want to create separate projects for the previsualization, research and development, and production phases of a film.

Projects establish an isolation boundary for both network data and project administration. However, you can share networks across projects with [Shared VPC](https://docs.cloud.google.com/compute/docs/shared-vpc), which provides separate projects with access to common resources.

**Production notes:** Create a Shared VPC host project that contains resources with all your production tools. You can designate all projects that are created under your organization as **Shared VPC service projects**. This designation means that any project in your organization can access the same libraries, scripts, and software that the host project provides.

### The Organization resource

You can manage projects under an Organization [resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), which you might have established already. [Migrating](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing) all your projects into an organization provides a number of [benefits](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#benefits_of_the_organization_resource).

**Production notes:** Designate production managers as owners of their individual projects and studio management as owners of the Organization resource.

### Defining access to resources

Projects require secure access to resources coupled with restrictions on where users or services are permitted to operate. To help you define access, Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam), which you can use to manage access control by defining which roles have what levels of access to which resources.

**Production notes:** To restrict users' access to only the resources that are necessary to perform specific tasks based on their role, implement the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) both on premises and in the cloud.

For example, consider a _render worker_ , which is a virtual machine (VM) that you can deploy from a predefined instance template that uses your custom image. The render worker that is running under a service account can read from Cloud Storage and write to attached storage, such as a cloud filer or persistent disk. However, you don't need to add individual artists to Google Cloud projects at all, because they don't need direct access to cloud resources.

You can assign roles to render wranglers or project administrators who have access to all Compute Engine resources, which permits them to perform functions on resources that are inaccessible to other users.

Define a policy to determine which roles can access which types of resources in your organization. The following table shows how typical production tasks map to IAM roles in Google Cloud.

Production task | Role name | Resource type  
---|---|---  
Studio manager | `resourcemanager.organizationAdmin` | Organization  
Project  
Production manager | `owner`, `editor` | Project  
Render wrangler | `compute.admin`, `iam.serviceAccountActor` | Project  
Queue management account | `compute.admin`, `iam.serviceAccountActor` | Organization  
Project  
Individual artist | [no access] | Not applicable  
  
### Access scopes

Access scopes offer you a way to control the permissions of a running instance no matter who is logged in. You can specify scopes when you create an instance yourself or when your queue management software deploys resources from an instance template.

Scopes take precedence over the IAM permissions of an individual user or service account. This precedence means that an access scope can prevent a project administrator from signing in to an instance to delete a storage bucket or change a firewall setting.

**Production notes:** By default, instances can read but not write to Cloud Storage. If your render pipeline writes finished renders back to Cloud Storage, add the scope `devstorage.read_write` to your instance at the time of creation.

## Choosing how to deploy resources

With cloud rendering, you can use resources only when needed, but you can choose from a number of ways to make resources available to your render farm.

### Deploy on demand

For optimal resource usage, you can choose to deploy render workers only when you send a job to the render farm. You can deploy many VMs to be shared across all frames in a job, or even create one VM per frame.

Your queue management system can monitor running instances, which can be requeued if a VM is preempted, and terminated when individual tasks are completed.

### Deploy a pool of resources

You can also choose to deploy a group of instances, unrelated to any specific job, that your on-premises queue management system can access as additional resources. If you use Google Cloud's [Spot VMs](https://cloud.google.com/solutions/spot-vms/), a group of running instances can accept multiple jobs per VM, using all cores and maximizing resource usage. This approach might be the most straightforward strategy to implement because it mimics how an on-premises render farm is populated with jobs.

## Licensing the software

Third-party software licensing can vary widely from package to package. Here are some of the licensing schemes and models that you might encounter in a VFX pipeline. For each scheme, the third column shows the recommended licensing approach.

Scheme | Description | Recommendation  
---|---|---  
Node locked | Licensed to a specific MAC address, IP address, or CPU ID. Can be run only by a single process. | Instance based  
Node based | Licensed to a specific node (instance). An arbitrary number of users or processes can run on a licensed node. | Instance based  
Floating | Checked out from a license server that keeps track of usage. | License server  
Software licensing  
Interactive | Allows user to run software interactively in a graphics-based environment. | License server or instance based  
Batch | Allows user to run software only in a command-line environment. | License server  
Cloud-based licensing  
Usage based | Checked out only when a process runs on a cloud instance. When the process finishes or terminates, the license is released. | Cloud-based license server  
Uptime based | Checked out while an instance is active and running. When the instance is stopped or deleted, the license is released. | Cloud-based license server  
  
### Using instance-based licensing

Some software programs or plugins are licensed directly to the hardware on which they run. This approach to licensing can present a problem in the cloud, where hardware identifiers such as MAC or IP addresses are assigned dynamically.

#### MAC addresses

When they are created, instances are assigned a MAC address that is retained so long as the instance is not deleted. You can [stop or restart](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#state_of_resources_for_stopped_instances) an instance, and the MAC address will be retained. You can use this MAC address for license creation and validation until the instance is deleted.

#### Assigning a static IP address

When you create an instance, it is assigned an internal and, optionally, an external IP address. To retain an instance's external IP address, you can [reserve a static IP address](https://docs.cloud.google.com/compute/docs/configure-ip-addresses#reserve_new_static) and assign it to your instance. This IP address will be reserved only for this instance. Because static IP addresses are a project-based resource, they are subject to [regional quotas](https://docs.cloud.google.com/compute/quotas#ip_addresses).

You can also assign an [internal IP address](https://docs.cloud.google.com/compute/docs/configure-ip-addresses#assigninternalip) when you create an instance, which is helpful if you want the internal IP addresses of a group of instances to fall within the same range.

#### Hardware dongles

Older software might still be licensed through a dongle, a hardware key that is programmed with a product license. Most software companies have stopped using hardware dongles, but some users might have legacy software that is keyed to one of these devices. If you encounter this problem, contact the software manufacturer to see if they can provide you with an updated license for your particular software.

If the software manufacturer cannot provide such a license, you could implement a network-attached USB hub or [USB over IP](http://usbip.sourceforge.net/) solution.

### Using a license server

Most modern software offers a floating license option. This option makes the most sense in a cloud environment, but it requires stronger license management and access control to prevent overconsumption of a limited number of licenses.

To help avoid exceeding your license capacity, you can as part of your job queue process choose which licenses to use and control the number of jobs that use licenses.

#### On-premises license server

You can use your existing, on-premises license server to provide licenses to instances that are running in the cloud. If you choose this method, you must provide a way for your render workers to communicate with your on-premises network, either through a VPN or some other secure connection.

#### Cloud-based license server

In the cloud, you can run a license server that serves instances in your project or even across projects by using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). Floating licenses are sometimes linked to a hardware MAC address, so a small, long-running instance with a static IP address can easily serve licenses to many render instances.

#### Hybrid license server

Some software can use multiple license servers in a prioritized order. For example, a renderer might query the number of licenses that are available from an on-premises server, and if none are available, use a cloud-based license server. This strategy can help maximize your use of permanent licenses before you check out other license types.

**Production notes:** Define one or more license servers in an environment variable and define the order of priority; Autodesk Arnold, a popular renderer, helps you do this. If the job cannot acquire a license by using the first server, the job tries to use any other servers that are listed, as in the following example:
    
    
    export solidangle_LICENSE=5053@x.x.0.1;5053@x.x.0.2

In the preceding example, the Arnold renderer tries to obtain a license from the server at `x.x.0.1`, port `5053`. If that attempt fails, it then tries to obtain a license from the same port at the IP address `x.x.0.2`.

### Cloud-based licensing

Some vendors offer cloud-based licensing that provides software licenses on demand for your instances. Cloud-based licensing is generally billed in two ways: usage based and uptime based.

#### Usage-based licensing

Usage-based licensing is billed based on how much time the software is in use. Typically with this type of licensing, a license is checked out from a cloud-based server when the process starts and is released when the process completes. So long as a license is checked out, you are billed for the use of that license. This type of licensing is typically used for rendering software.

#### Uptime-based licensing

Uptime-based or metered licenses are billed based on the uptime of your Compute Engine instance. The instance is configured to register with the cloud-based license server during the [startup process](https://docs.cloud.google.com/compute/docs/startupscript). So long as the instance is running, the license is checked out. When the instance is stopped or deleted, the license is released. This type of licensing is typically used for render workers that a queue manager deploys.

**Important:** Third-party software licenses might have different requirements for use on a public cloud, so consider working with your corporate counsel to determine if your licenses are compatible with that cloud.

## Choosing how to store your data

The type of [storage](https://cloud.google.com/products/storage) that you choose on Google Cloud depends on your chosen storage strategy along with factors such as durability requirements and cost.

### Persistent disk

You might be able to avoid implementing a file server altogether by incorporating [persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs) (PDs) into your workload. PDs are a type of POSIX-compliant block storage, up to 64 TB in size, that are familiar to most VFX facilities. Persistent disks are available as both standard drives and solid-state drives (SSD). You can attach a PD in read-write mode to a single instance, or in read-only mode to a large number of instances, such as a group of render workers.

Pros | Cons | Ideal use case  
---|---|---  
Mounts as a standard NFS or SMB volume.  
  
Can dynamically resize.  
  
Up to 128 PDs can be attached to a single instance.  
  
The same PD can be mounted as read-only on hundreds or thousands of instances. | Maximum size of 64 TB.  
  
Can write to PD only when attached to a single instance.  
  
Can be accessed only by resources that are in the same [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). | Advanced pipelines that can build a new disk on a per-job basis.  
  
Pipelines that serve infrequently updated data, such as software or common libraries, to render workers.  
  
### Object storage

[Cloud Storage](https://docs.cloud.google.com/storage) is highly redundant, highly durable storage that, unlike traditional file systems, is unstructured and practically unlimited in capacity. Files on Cloud Storage are stored in buckets, which are similar to folders, and are accessible worldwide.

Unlike traditional storage, object storage cannot be mounted as a logical volume by an operating system (OS). If you decide to incorporate object storage into your render pipeline, you must modify the way that you read and write data, either through command-line utilities such as the gcloud CLI or through the [Cloud Storage API](https://docs.cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python).

Pros | Cons | Ideal use case  
---|---|---  
Durable, highly available storage for files of all sizes.  
  
Single API across storage classes.  
  
Inexpensive.  
  
Data is available worldwide.  
  
Virtually unlimited capacity. | Not POSIX-compliant.   
  
Must be accessed through API or command-line utility.  
  
In a render pipeline, data must be transferred locally before use. | Render pipelines with an asset management system that can publish data to Cloud Storage.  
  
Render pipelines with a queue management system that can fetch data from Cloud Storage before rendering.  
  
### Other storage products

Other storage products are available as managed services, through third-party channels such as the [Cloud Marketplace](https://cloud.google.com/marketplace/), or as open source projects through software repositories or GitHub.

Product | Pros | Cons | Ideal use case  
---|---|---|---  
[Filestore](https://cloud.google.com/filestore/) | Clustered file system that can support thousands of simultaneous NFS connections.  
  
Able to synchronize with on-premises NAS cluster. | No way to selectively sync files. No bidirectional sync. | Medium to large VFX facilities with hundreds of TBs of data to present on the cloud.   
[Pixit Media](https://www.pixitmedia.com/), [PixStor](https://pixitmedia.com/pixstor-is/) | Scale-out file system that can support thousands of simultaneous NFS or POSIX clients. Data can be cached on demand from on-premises NAS, with updates automatically sent back to on-premises storage. | Cost, third-party support from Pixit. | Medium to large VFX facilities with hundreds of TBs of data to present on the cloud.  
[Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes) | Fully managed storage solution on Google Cloud.  
  
Supports NFS, SMB, and multiprotocol environments.   
  
Point in time snapshots with instance recovery | Not available in all Google Cloud regions.  | VFX facilities with a pipeline capable of asset synchronization.   
  
Shared disk across virtual workstations.  
[Cloud Storage FUSE](https://github.com/GoogleCloudPlatform/gcsfuse/) | Mount Cloud Storage buckets as file systems. Low cost. | Not a POSIX-compliant file system. Can be difficult to configure and optimize. | VFX facilities that are capable of deploying, configuring, and maintaining an open source file system, with a pipeline that is capable of asset synchronization.  
  
Other storage types are available on Google Cloud. For more information, contact your Google Cloud representative.

### Further reading on data storage options

  * [Storage options available on Google Cloud](https://cloud.google.com/products/storage)
  * [File storage on Compute Engine](https://docs.cloud.google.com/architecture/filers-on-compute-engine)
  * [Design an optimal storage strategy for your cloud workload](https://docs.cloud.google.com/architecture/storage-advisor)



## Implementing storage strategies

You can implement a number of storage strategies in VFX or animation production pipelines by establishing conventions that determine how to handle your data, whether you access the data directly from your on-premises storage or synchronize between on-premises storage and the cloud.

### Strategy 1: Mount on-premises storage directly

![Mounting on-premises storage directly from cloud-based render
workers](https://docs.cloud.google.com/static/architecture/images/render-farm-on-premises-storage.svg)_Mounting on-premises storage directly from cloud-based render workers_

If your facility has connectivity to Google Cloud of at least 10 Gbps and is in close proximity to a Google Cloud [region](https://cloud.google.com/about/locations/), you can choose to mount your on-premises NAS directly on cloud render workers. While this strategy is straightforward, it can also be cost- and bandwidth- intensive, because anything that you create on the cloud and write back to storage is counted as egress data.

Pros | Cons | Ideal use case  
---|---|---  
Straightforward implementation.   
  
Read/write to common storage.  
  
Immediate availability of data, no caching or synchronization necessary. | Can be more expensive than other options.  
  
Close proximity to a Google data center is necessary to achieve low latency.  
  
The maximum number of instances that you can connect to your on-premises NAS depends on your bandwidth and connection type. | Facilities near a Google data center that need to burst render workloads to the cloud, where cost is not a concern.  
  
Facilities with connectivity to Google Cloud of at least 10 Gbps.  
  
### Strategy 2: Synchronize on demand

![Synchronizing data between on-premises storage and cloud-based
storage on demand](https://docs.cloud.google.com/static/architecture/images/render-farm-read-thru-cache.svg)_Synchronizing data between on-premises storage and cloud-based storage on demand_

You can choose to _push_ data to the cloud or _pull_ data from on-premises storage, or vice versa, only when data is needed, such as when a frame is rendered or an asset is published. If you use this strategy, synchronization can be triggered by a mechanism in your pipeline such as a watch script, by an event handler such as [Pub/Sub](https://docs.cloud.google.com/pubsub), or by a set of commands as part of a job script.

You can perform a synchronization by using a variety of commands, such as the gcloud CLI [scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp) command, the gcloud CLI [rsync](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command, or [UDP-based data transfer protocols](https://wikipedia.org/wiki/UDP-based_Data_Transfer_Protocol) (UDT). If you choose to use a third-party UDT such as [Aspera](http://downloads.asperasoft.com/connect2/), [Cloud FastPath](https://www.cloudfastpath.com/), [BitSpeed](http://www.bitspeed.com/), or [FDT](https://github.com/fast-data-transfer/fdt) to communicate with a Cloud Storage bucket, refer to the third party's documentation to learn about their security model and best practices. Google does not manage these third-party services.

#### Push method

You typically use the push method when you publish an asset, place a file in a watch folder, or complete a render job, after which time you push it to a predefined location.

**Examples:**

  * A cloud render worker completes a render job, and the resulting frames are pushed back to on-premises storage.
  * An artist publishes an asset. Part of the asset-publishing process involves pushing the associated data to a predefined path on Cloud Storage.



#### Pull method

You use the pull method when a file is requested, typically by a cloud-based render instance.

**Example:** As part of a render job script, all assets that are needed to render a scene are pulled into a file system before rendering, where all render workers can access them.

Pros | Cons | Ideal use case  
---|---|---  
Complete control over which data is synchronized and when.  
  
Ability to choose transfer method and protocol. | Your production pipeline must be capable of event handling to trigger push/pull synchronizations.  
  
Additional resources might be necessary to handle the synchronization queue. | Small to large facilities that have custom pipelines and want complete control over asset synchronization.  
  
**Production notes:** Manage data synchronization with the same queue management system that you use to handle render jobs. Synchronization tasks can use separate cloud resources to maximize available bandwidth and minimize network traffic.

### Strategy 3: On-premises storage, cloud-based read-through cache

![Using your on-premises storage with a cloud-based, read-through
cache](https://docs.cloud.google.com/static/architecture/images/render-farm-sync-on-demand.svg)_Using your on-premises storage with a cloud-based, read-through cache_

Google Cloud has extended and developed a [KNFSD caching solution](https://cloud.google.com/blog/products/media-entertainment/gunpowder-uses-knfsd-caching-to-help-media-customers-use-cloud) as an open source option. The solution can handle render farm performance demands that exceed the capabilities of storage infrastructure. KNFSD caching offers high-performance, read-through caching, which lets workloads scale to hundreds—or even thousands—of render nodes across multiple regions and hybrid storage pools.

KNFSD caching is a scale-out solution that reduces load on the primary file-sharing service. KNFSD caching also reduces the overload effect when many render nodes all attempt to retrieve files from the file server at the same time. By using a caching layer on the same VPC network as the render nodes, read latency is reduced, which helps render jobs start and complete faster. Depending on how you've configured your caching file server, the data remains in the cache until:

  * The data _ages out_ , or remains untouched for a specified amount of time.
  * Space is needed on the file server, at which time data is removed from the cache based on age.



This strategy reduces the amount of bandwidth and complexity required to deploy many concurrent render instances.

In some cases, you might want to _pre-warm_ your cache to ensure that all job-related data is present before rendering. To pre-warm the cache, read the contents of a directory that is on your cloud file server by performing a `read` or `stat` of one or more files. Accessing files in this way triggers the synchronization mechanism.

You can also add a physical on-premises appliance to communicate with the virtual appliance. For example, NetApp offers a [storage solution](https://cloud.google.com/netapp) that can further reduce latency between your on-premises storage and the cloud.

Pros | Cons | Ideal use case  
---|---|---  
Cached data is managed automatically.  
  
Reduces bandwidth requirements.  
  
Clustered cloud file systems can be scaled up or down depending on job requirements. | Can incur additional costs.  
  
Pre-job tasks must be implemented if you choose to pre-warm the cache. | Large facilities that deploy many concurrent instances and read common assets across many jobs.  
  
### Filtering data

You can build a database of asset types and associated conditions to define whether to synchronize a particular type of data. You might never want to synchronize some types of data, such as ephemeral data that is generated as part of a conversion process, cache files, or simulation data. Consider also whether to synchronize _unapproved_ assets, because not all iterations will be used in final renders.

### Performing an initial bulk transfer

When implementing your hybrid render farm, you might want to [perform an initial transfer](https://docs.cloud.google.com/solutions/transferring-big-data-sets-to-gcp) of all or part of your dataset to Cloud Storage, persistent disk, or other cloud-based storage. Depending on factors such as the amount and type of data to transfer and your connection speed, you might be able to perform a full synchronization over the course of a few days or weeks. The following figure compares typical times for online and physical transfers.

![Comparison of typical times for online and physical transfers](https://docs.cloud.google.com/static/architecture/images/render-farm-online-vs-physical-transfer.svg)_Comparison of typical times for online and physical transfers_

If your transfer workload exceeds your time or bandwidth constraints, Google offers a number of [transfer options](https://docs.cloud.google.com/storage-transfer/docs/transfer-options) to get your data into the cloud, including Google's [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance).

## Archiving and disaster recovery

It's worth noting the difference between archiving of data and disaster recovery. The former is a selective copy of finished work, while the latter is a state of data that can be recovered. You want to [design a disaster recovery plan](https://docs.cloud.google.com/solutions/designing-a-disaster-recovery-plan) that fits your facility's needs and provides an off-site contingency plan. Consult with your on-premises storage vendor for help with a disaster recovery plan that suits your specific storage platform.

## Archiving data in the cloud

After a project is complete, it is common practice to save finished work to some form of long-term storage, typically magnetic tape media such as [LTO](https://wikipedia.org/wiki/Linear_Tape-Open). These cartridges are subject to environmental requirements and, over time, can be logistically challenging to manage. Large production facilities sometimes house their entire archive in a purpose-built room with a full-time archivist to keep track of data and retrieve it when requested.

Searching for specific archived assets, shots, or footage can be time-consuming, because data might be stored on multiple cartridges, archive indexing might be missing or incomplete, or there might be speed limitations on reading data from magnetic tape.

Migrating your data archive to the cloud can not only eliminate the need for on-premises management and storage of archive media, but it can also make your data far more accessible and searchable than traditional archive methods can.

A basic archiving pipeline might look like the following diagram, employing different cloud services to examine, categorize, tag, and organize archives. From the cloud, you can [create](https://github.com/sararob/video-intelligence-demo) an archive management and retrieval tool to search for data by using various metadata criteria such as date, project, format, or resolution. You can also use the Machine Learning APIs to tag and categorize images and videos, storing the results in a cloud-based database such as BigQuery.

![An asset archive pipeline that includes machine learning to categorize content](https://docs.cloud.google.com/static/architecture/images/render-farm-publish-to-cloud-storage.svg)_An asset archive pipeline that includes machine learning to categorize content_

Further topics to consider:

  * Automate the generation of thumbnails or proxies for content that resides within Cloud Storage storage classes that have [retrieval fees](https://cloud.google.com/storage/pricing#retrieval-pricing). Use these proxies within your media asset management system so that users can browse data while reading only the proxies, not the archived assets.
  * Consider using machine learning to categorize live-action content. Use the [Cloud Vision](https://docs.cloud.google.com/vision) to label textures and background plates, or the [Video Intelligence API](https://docs.cloud.google.com/video-intelligence) to help with the search and retrieval of reference footage.
  * You can also use [AutoML on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview#automl) to create a custom image model to recognize any asset, whether live action or rendered.
  * For rendered content, consider saving a copy of the render worker's disk image along with the rendered asset. If you need to re-create the setup, you will have the correct software versions, plugins, OS libraries, and dependencies available if you need to re-render an archived shot.



## Managing assets and production

Working on the same project across multiple facilities can present unique challenges, especially when content and assets need to be available around the world. Manually synchronizing data across private networks can be expensive and resource-intensive, and is subject to local bandwidth limitations.

If your workload requires globally available data, you might be able to use [Cloud Storage](https://docs.cloud.google.com/storage), which is accessible from anywhere that you can access Google services. To incorporate Cloud Storage into your pipeline, you must modify your pipeline to understand object paths, and then pull or push your data to your render workers before rendering. Using this method provides global access to published data but requires your pipeline to deliver assets to where they're needed in a reasonable amount of time.

For example, a texture artist in Los Angeles can publish image files to be used by a lighting artist in London. The process looks like this:

![Publishing assets to Cloud Storage](https://docs.cloud.google.com/static/architecture/images/render-farm-asset-archive-pipeline.svg)_Publishing assets to Cloud Storage_

  1. The publish pipeline pushes files to Cloud Storage and adds an entry to a cloud-based asset database.
  2. An artist in London runs a script to gather assets for a scene. File locations are queried from the database and read from Cloud Storage to local disk.
  3. Queue management software gathers a list of assets that are required for rendering, queries them from the asset database, and downloads them from Cloud Storage to each render worker's local storage.



Using Cloud Storage in this manner also provides you with an archive of all your published data on the cloud if you choose to use Cloud Storage as part of your archive pipeline.

## Managing databases

Asset and production management software depends on highly available, durable databases that are served on hosts capable of handling hundreds or thousands of queries per second. Databases are typically hosted on an on-premises server that is running in the same rack as render workers, and are subject to the same power, network, and HVAC limitations.

You might consider running your MySQL, NoSQL, and PostgreSQL production databases as managed, cloud-based services. These services are highly available and globally accessible, encrypt data both at rest and in transit, and offer built-in replication functionality.

## Managing queues

Commercially available queue management software programs such as [Qube!](https://www.pipelinefx.com/), [Deadline](https://deadline.thinkboxsoftware.com/), and [Tractor](https://renderman.pixar.com/product/tractor) are widely used in the VFX/animation industry. There are also open source software options available, such as [OpenCue](https://github.com/AcademySoftwareFoundation/OpenCue). You can use this software to deploy and manage any compute workload across a variety of workers, not just renders. You can deploy and manage asset publishing, particle and fluid simulations, texture baking, and compositing with the same scheduling framework that you use to manage renders.

A few facilities have implemented general-purpose scheduling software such as [HTCondor](https://research.cs.wisc.edu/htcondor/) from the University of Wisconsin, [Slurm](https://slurm.schedmd.com/) from SchedMD, or [Univa Grid Engine](http://www.univa.com/products/) into their VFX pipelines. Software that is designed specifically for the VFX industry, however, pays special attention to features like the following:

  * Job-, frame-, and layer-based dependency. Some tasks need to be completed before you can begin other jobs. For example, run a fluid simulation in its entirety before rendering.
  * Job priority, which render wranglers can use to shift the order of jobs based on individual deadlines and schedules.
  * Resource types, labels, or targets, which you can use to match specific resources with jobs that require them. For example, deploy GPU-accelerated renders only on VMs that have GPUs attached.
  * Capturing historical data on resource usage and making it available through an API or dashboard for further analysis. For example, look at average CPU and memory usage for the last few iterations of a render to predict resource usage for the next iteration.
  * Pre- and post-flight jobs. For example, a pre-flight job pulls all necessary assets onto the local render worker before rendering. A post-flight job copies the resulting rendered frame to a designated location on a file system and then marks the frame as complete in an asset management system.
  * Integration with popular 2D and 3D software applications such as Maya, 3ds Max, Houdini, Cinema 4D, or Nuke.



**Production notes:** Use queue management software to recognize a pool of cloud-based resources as if they were on-premises render workers. This method requires some oversight to maximize resource usage by running as many renders as each instance can handle, a technique known as bin packing. These operations are typically handled both algorithmically and by render wranglers.

You can also automate the creation, management, and termination of cloud-based resources on an on-demand basis. This method relies on your queue manager to run pre- and post-render scripts that create resources as needed, monitor them during rendering, and terminate them when tasks are done.

### Job deployment considerations

When you are implementing a render farm that uses both on-premises and cloud-based storage, here are some considerations that your queue manager might need to keep in mind:

  * Licensing might differ between cloud and on-premises deployments. Some licenses are node based, some are process driven. Ensure that your queue management software deploys jobs to maximize the value of your licenses.
  * Consider adding unique tags or labels to cloud-based resources to ensure that they get used only when assigned to specific job types.
  * Use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to detect unused or idle instances.
  * When launching dependent jobs, consider where the resulting data will reside and where it needs to be for the next step.
  * If your path namespaces differ between on-premises and cloud-based storage, consider using relative paths to allow renders to be location agnostic. Alternatively, depending on the platform, you could build a mechanism to swap paths at render time.
  * Some renders, simulations, or post-processes rely on random number generation, which can differ among CPU manufacturers. Even CPUs from the same manufacturer but different chip generations can produce different results. When in doubt, use identical or similar CPU types for all frames of a job.
  * If you are using a read-through cache appliance, consider deploying a pre-flight job to pre-warm the cache and ensure that all assets are available on the cloud before you deploy cloud resources. This approach minimizes the amount of time that render workers are forced to wait while assets are moved to the cloud.



## Logging and monitoring

Recording and monitoring resource usage and performance is an essential aspect of any render farm. Google Cloud offers a number of APIs, tools, and solutions to help provide insight into utilization of resources and services.

The quickest way to monitor a VM's activity is to view its [serial port output](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console). This output can be helpful when an instance is unresponsive through typical service control planes such as your render queue management supervisor.

Other ways to collect and monitor resource usage on Google Cloud include:

  * Use [Cloud Logging](https://docs.cloud.google.com/logging) to capture usage and audit logs, and to export the resulting logs to Cloud Storage, BigQuery, and other services.
  * Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to install an agent on your VMs to monitor system [metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent).
  * Incorporate the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/api) into your pipeline scripts to log directly to Cloud Logging by using [client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) for popular scripting languages.
  * Use Cloud Monitoring to create [charts](https://docs.cloud.google.com/monitoring/charts) to understand resource usage.



## Configuring your render worker instances

For your workload to be truly hybrid, on-premises render nodes must be identical to cloud-based render nodes, with matching OS versions, kernel builds, installed libraries, and software. You might also need to reproduce mount points, path namespaces, and even user environments on the cloud, because they are on premises.

### Choosing a disk image

You can choose from one of the [public images](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage) or create your own [custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) that is based on your on-premises render node image. Public images include a collection of [packages](https://docs.cloud.google.com/compute/docs/images/guest-environment) that set up and manage [user accounts](https://docs.cloud.google.com/compute/docs/access/user-accounts) and enable Secure Shell (SSH) key–based authentication.

### Creating a custom image

If you choose to create a custom image, you will need to add more libraries to both Linux and Windows for them to function properly in the Compute Engine environment.

Your custom image must comply with security [best practices](https://docs.cloud.google.com/compute/docs/images/configuring-imported-images#security). If you are using Linux, install the [Linux guest environment for Compute Engine](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) to access the functionality that public images provide by default. By installing the guest environment, you can perform tasks, such as metadata access, system configuration, and optimizing the OS for use on Google Cloud, by using the same security controls on your custom image that you use on public images.

**Production notes:** Manage your custom images in a separate project at the organization level. This approach gives you more precise control over how images are created or modified and lets you apply [versions](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#setting_families), which can be useful when using different software or OS versions across multiple productions.

### Automating image creation and instance deployment

You can use tools such as [Packer](https://www.packer.io/) to make creating images more reproducible, auditable, configurable, and reliable. You can also use a tool like [Ansible](https://www.ansible.com/) to configure your running render nodes and exercise fine-grained control over their configuration and lifecycle.

### Choosing a machine type

On Google Cloud, you can choose one of the [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose) or specify a [custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type). Using custom machine types gives you control over resources so you can customize instances based on the job types that you run on Google Cloud. When creating an instance, you can add GPUs and specify the number of CPUs, the CPU platform, the amount of RAM, and the type and size of disks.

**Production notes:** For pipelines that deploy one instance per frame, consider customizing the instance based on historical job statistics like CPU load or memory use to optimize resource usage across all frames of a shot. For example, you might choose to deploy machines with higher CPU counts for frames that contain heavy motion blur to help normalize render times across all frames.

### Choosing between standard and preemptible VMs

[Preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible) (PVMs) refers to excess Compute Engine capacity that is sold at a much [lower price](https://cloud.google.com/compute/pricing) than standard VMs. Compute Engine might terminate or preempt these instances if other tasks require access to that capacity. PVMs are ideal for rendering workloads that are fault tolerant and managed by a queueing system that keeps track of jobs that are lost to preemption.

Standard VMs can be run indefinitely and are ideal for license servers or queue administrator hosts that need to run in a persistent fashion.

Preemptible VMs are terminated automatically after 24 hours, so don't use them to run renders or simulations that run longer.

Preemption rates run from 5% to 15%, which for typical rendering workloads is probably tolerable given the reduced cost. Some preemptible [best practices](https://docs.cloud.google.com/compute/docs/instances/create-start-preemptible-instance#best_practices) can help you decide the best way to integrate PVMs into your render pipeline. If your instance is preempted, Compute Engine sends a [preemption signal](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption_process) to the instance, which you can use to trigger your scheduler to terminate the current job and requeue.

Standard VM | Preemptible VM  
---|---  
Can be used for long-running jobs.  
  
Ideal for high-priority jobs with hard deadlines.  
  
Can be run indefinitely, so ideal for license servers or queue administrator hosting. | Automatically terminated after 24 hours.  
  
Requires a queue management system to handle preempted instances.  
  
**Production notes:** Some renderers can perform a snapshot of an in-progress render at specified intervals, so if the VM gets preempted, you can pause and resume rendering without having to restart a frame from scratch. If your renderer supports snapshotting, and you choose to use PVMs, enable render snapshotting in your pipeline to avoid losing work. While snapshots are being written and updated, data can be written to Cloud Storage and, if the render worker gets preempted, retrieved when a new PVM is deployed. To avoid storage costs, delete snapshot data for completed renders.

### Granting access to render workers

IAM helps you assign access to cloud resources to individuals who need access. For Linux render workers, you can use [OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) to further restrict access within an SSH session, giving you control over who is an administrator.

## Controlling costs of a hybrid render farm

When estimating costs, you must consider many factors, but we recommend that you implement these common best practices as policy for your hybrid render farm:

  * **Use preemptible instances by default.** Unless your render job is extremely long-running, four or more hours per frame, or you have a hard deadline to deliver a shot, use preemptible VMs.
  * **Minimize egress.** Copy only the data that you need back to on-premises storage. In most cases, this data will be the final rendered frames, but it can also be separate passes or simulation data. If you are mounting your on-premises NAS directly, or using a storage product that synchronizes automatically, write all rendered data to the render worker's local file system, then copy what you need back to on-premises storage to avoid egressing temporary and unnecessary data.
  * **Right-size VMs.** Make sure to create your render workers with optimal resource usage, assigning only the necessary number of vCPUs, the optimum amount of RAM, and the correct number of GPUs, if any. Also consider how to minimize the size of any attached disks.
  * **Consider the one-minute minimum.** On Google Cloud, instances get billed on a per-second basis with a one-minute minimum. If your workload includes rendering frames that take less than one minute, consider chunking tasks together to avoid deploying an instance for less than one minute of compute time.
  * **Keep large datasets on the cloud.** If you use your render farm to generate massive amounts of data, such as deep EXRs or simulation data, consider using a cloud-based workstation that is further down the pipeline. For example, an FX artist might run a fluid simulation on the cloud, writing cache files to cloud-based storage. A lighting artist could then access this simulation data from a virtual workstation that is on Google Cloud. For more information about virtual workstations, contact your Google Cloud representative.
  * **Take advantage of sustained and committed use discounts.** If you run a pool of resources, [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) can save you up to 30% off the cost of instances that run for an entire month. [Committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) can also make sense in some cases.



Extending your existing render farm to the cloud is a cost-effective way to use powerful, low-cost resources without capital expense. No two production pipelines are alike, so no document can cover every topic and unique requirement. For help with migrating your render workloads to the cloud, contact your Google Cloud representative.

## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-11-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-11-26 UTC."],[],[]] 
