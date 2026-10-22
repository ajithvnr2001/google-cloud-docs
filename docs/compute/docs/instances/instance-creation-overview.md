---
url: https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview/
title: Overview of creating Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:05.680767+00:00
---

# Overview of creating Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of creating Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine lets you create and run [instances](https://docs.cloud.google.com/compute/docs/instances) on Google infrastructure. This document provides an overview of the various configuration parameters that are available to you during a Compute Engine instance creation. If you are creating an instance for the first time, then this document provides a starting point for understanding the process.

The terms _Compute Engine instance_ , _compute instance_ or _instance_ are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

  * If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
  * Otherwise, an instance is a VM instance. The terms _virtual machine instance_ , _VM instance_ , and _VM_ are synonymous.



Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

## Before you begin

  * Review the basics about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances). 
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




## Ways to create and configure instances

You can create instances in multiple ways, each with its own method of configuration, as follows:

  * **[Create your instance by manually specifying a custom configuration](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents).** Choose this option if you're creating an instance from the scratch and are facing any of the following scenarios:

    * You know the specific configuration that is required for your workload.
    * You want to create an instance with a complicated configuration.
    * You want to create an instance by using the Google Cloud CLI or REST.

If you choose this method, then also review the list of all configuration options available during instance creation.

  * **[Create a workload-optimized instance](https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance).** In this method, you select your workload type while creating your instance and Google automatically populates a preset configuration that suits your workload. Choose this option if you're starting out with Compute Engine and don't know which configuration best suits your intended workload. This option is available only in the Google Cloud console.

  * **[Create your instance by using an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).** An instance template is a resource that defines configuration settings for instances. Choose this option if you have a defined configuration template and want to create a lot of VMs with the same configuration.

  * **[Create your instance by making copies of a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image).** A machine image contains most of the information and data needed for cloning an instance. Choose this option if you want to make multiple copies of an existing source instance.




After you create your compute instance, Compute Engine automatically starts the instance.

## Configuration options available during instance creation

When you create a Compute Engine instance, you specify the configuration that you want for your instance. Compute Engine uses this configuration to create your instance. The following table lists the various parameters that you configure when you create a Compute Engine instance. To get AI-powered assistance when you evaluate which configurations best fit your workload requirements, comparing pricing trade-offs, you can interact with Gemini in the Google Cloud console. For more information, see [Design compute infrastructure with Compute Advisor](https://docs.cloud.google.com/compute/docs/design-with-gemini).

Machine configurationOperating system (OS) and storageData protectionNetworkingObservabilitySecurityAdvanced configuration

Clear all

**Parameter** | **What you can configure**  
---|---  
Machine configuration | 

  * **Hardware** : You specify a [machine family, series, and type](https://docs.cloud.google.com/compute/docs/machine-resource), which determines the number of vCPUs, memory, and the [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms) that Compute Engine allocates for your instance. If the machine type is available on multiple CPU platforms, you can choose the earliest CPU platform to use when creating the instance. For the machine type, you can choose either a predefined machine type or create a [custom machine type](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types) for some machine series. 


  * **Location** : You can choose the [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to create your instance. 


  * **Instance name** : Specify a [name](https://docs.cloud.google.com/compute/docs/naming-resources) for the instance that is unique within your project and the selected zone. 


  * You can also configure more specific and advanced machine configuration settings such as: 
    * [ Simultaneous multi-threading (SMT)](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core)
    * The [ number of visible cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores)
    * For C4 instances only: whether the instance runs in [ all-core-max turbo mode](https://docs.cloud.google.com/compute/docs/cpu-platforms#frequency_behavior).

  
Operating system (OS) and storage | 

  * **Boot disk and OS** : Every instance comes with a boot disk for which you can specify a disk name, size, and [disk type](https://docs.cloud.google.com/compute/docs/disks). You also select the [OS image](https://docs.cloud.google.com/compute/docs/images) to install on the boot disk in one of the following ways: 
    * If you want to use a preconfigured OS image to create your instance, then use a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). Public images have all the drivers that are necessary to run the instance in Google Cloud. Compute Engine offers many preconfigured public OS images that have compatible Linux or Windows operating systems. 
    * If you are creating an instance for an application, you can use a [custom image](https://docs.cloud.google.com/compute/docs/images/create-custom) or a [ shared image](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images) to which you added additional drivers and software that support your application. 
    * You can also use a [snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots) or an existing disk as the source for creating the OS image on the boot disk. 


  * **Additional disks** : You can create and attach one or more non-boot disks to the new instance in the following ways: 
    * You can choose to create and attach new, blank disks.
    * You can choose to create and attach new disks from an existing source image or an existing disk. 
    * You can choose to attach existing disks.
    * For some machine types, Local SSD disks are [ automatically attached during instance creation](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed). For a few other machine types, you can choose to [ attach Local SSD disks during instance creation](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options). 
    * For Local SSD disks, you can optionally configure the [ Local SSD recovery timeout](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#local-ssd-timeout), and which interface to use - [ NVMe or SCSI](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface)


  * **Disk configuration** : Whether you're configuring a boot disk or an additional data disk, you can specify the following configuration details: 
    * Disk name (and optionally a custom device name)
    * Disk size
    * [Encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption)
    * For [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) and [ Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk) volumes only: the IOPS and throughput performance limits 
    * For Hyperdisk Balanced and Hyperdisk Throughput volumes only: whether the disk is created using resources in a [ Hyperdisk Storage Pool](https://docs.cloud.google.com/compute/docs/disks#storage_pools)
    * The [ disk attachment mode](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attachment_mode) (Read-only or Read-write) 
    * A [label](https://docs.cloud.google.com/compute/docs/labeling-resources) or [tag](https://docs.cloud.google.com/compute/docs/tag-resources) for the disk 
    * You can also enable a setting that prevents your disk from being deleted if the attached instance is deleted. 


  * **Container** : You can run containers such as Docker or Kubernetes on any of the following images: 
    * Linux public VM images
    * Windows Server public VM images
    * A [ Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) image. 
You specify a container image name and other [ container configuration details](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers). You can also specify mount directories to add `tmpfs` storage and additional disks to the container. **Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

  
Data protection | 

  * **Data backup** : You can automate recurring backups of your disk and instance data and prepare for disaster recovery in the following ways: 
    * Use [ Backup and DR Service backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup_plans) to back up your entire instance. 
    * Use [ snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to automate your disk data backup. 
To learn how to choose the correct data protection option for your use case, see [ Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection). You can also configure a project-wide default backup setting. This setting specifies which backup method is preselected by default every time you create an instance in the Google Cloud console. To learn more, see [ Configure the default backup setting for the console](https://docs.cloud.google.com/compute/docs/disks/default-backup)


  * **Data replication** : You can continuously replicate your disk data for disaster protection using [ cross-zone synchronous replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) or [cross-region asynchronous replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about). 
  * **Protect non-boot disks only** : You can also enable an option that applies your snapshot schedules and data replication settings only to non-boot disks. Choosing this setting can help you reduce costs. However, this setting doesn't apply to backup plans. 

  
Networking | 

  * **Firewall rules** : You can set up a [firewall](https://docs.cloud.google.com/firewall/docs/firewalls) and configure the type of network traffic that you want to allow from the internet. You can also specify a [network tag for the firewall rules](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags). 


  * **Custom hostname** : You can specify that Google Cloud should use a [ custom name for the instance](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#requirements) other than the internal DNS name. If you choose this option, then you must manually configure an internal DNS record for the custom hostname. 


  * **IP forwarding** : You can choose whether to [configure IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) for the new instance. 


  * **Network performance** : You can configure the instance to use [ per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for higher network performance at additional cost. 


  * **Network interfaces** : By default, a new instance is configured with a single interface that uses the [ default auto mode Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/compute/docs/networking/network-overview#subnets). Alternatively, you can specify a [custom mode VPC network and subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) that you created previously. You can also configure [additional network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) and Dynamic NICs for the instance. For each network interface, you can configure the following properties:
    * The network interface type
    * The IP stack type (IPv4 only, IPv6 only, or dual-stack) 
    * The [type of IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) for the internal and optional external IP addresses (ephemeral address or a reserved, static address)
    * An alias IP range for the network interface
    * The [Network Service Tier](https://docs.cloud.google.com/network-tiers) that the network interface uses
    * Whether a public DNS [PTR record](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record) is associated with the external IP address for the network interface

  
Observability | 

  * **Ops agent** : You can choose to install [Ops agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on your instance to collect logs and metrics and [monitor instance activity](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms). 


  * **Virtual displays** : You can [ enable virtual displays](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) on your instance to run screen capturing or remote system management tools on your VM. 

  
Security | 

  * **Service account** : You can attach a [ service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) to your instance. Service accounts allow applications that run on an instance to make authorized Google Cloud API calls and access Google Cloud resources. You can also select the type and level of API access to grant the VM. 
  * **Confidential computing** : You can prevent your data from being accessed while you use an instance by using [ Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview) to encrypt your data. 
  * **Shielded VM features** : You can make your instance more secure against boot- or kernel-level malware and rootkits by enabling [ Shielded VM features](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm). 
  * **VM access** : You can [control the users who have access](https://docs.cloud.google.com/compute/docs/access) to an instance by setting up [IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam) and [SSH keys for authentication](https://docs.cloud.google.com/compute/docs/instances/ssh). 

  
Advanced configuration | 

  * **Tags and Labels** : To assist with resource organization, you can add [ Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and [Labels](https://docs.cloud.google.com/compute/docs/labeling-resources) to the instance. 


  * **Deletion protection** : You can protect your instances from being [ accidentally deleted](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion). 


  * **Placement policy** : You can control instance placement in a data center by applying a [ placement policy to your instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview). 


  * **Reservations** : You can configure your instance to consume any [ reserved zonal resource capacity](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation) to ensure better resource availability. 


  * **Automation** : You can specify a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts) that runs each time the instance starts or reboots. 


  * **Metadata** : You can set [ custom metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#custom-metadata-keys) for your instance to store unique information about the instance. 


  * **Encryption** : You can choose the encryption method and keys to use to protect disk data, memory contents, and metadata when the instance is suspended. This can be different from the encryption used to protect the disk data while the instance is running. You can also configure how the instance behaves if a specified [ Cloud KMS key is revoked](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#vm-shutdown). 


  * **Provisioning model** : You can choose among the standard, spot, flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)), or reservation-bound provisioning model. For more information, see [ Compute Engine instances provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). 


  * **Sole-tenancy** : You can opt for having dedicated physical servers for your instances and specify a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) or [node group](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) to create the instance in. For general-purpose N series machine types, you can specify whether to [ enable CPU overcommit](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) for instances running on sole tenant nodes. 

  
  
## What's next

  * Learn how to [create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * If you're creating an instance for the first time, then try one of the following tutorials for a basic configuration: 
    * [Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance)
    * [Create a Windows Server VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance)
  * Learn how to [design compute infrastructure with Compute Advisor](https://docs.cloud.google.com/compute/docs/design-with-gemini).
  * Learn about [what happens to an instance after creation](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
