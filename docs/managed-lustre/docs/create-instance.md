---
url: https://docs.cloud.google.com/managed-lustre/docs/create-instance/
title: Create a Managed Lustre instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:56.730187+00:00
---

# Create a Managed Lustre instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Create a Managed Lustre instance Stay organized with collections  Save and categorize content based on your preferences. 

A Google Cloud Managed Lustre instance is a complete Lustre file system in the cloud. It can be mounted to a Compute Engine VM or to a Google Kubernetes Engine (GKE) cluster. You access data on the instance using standard POSIX terminology.

When creating a Managed Lustre instance, you must define the following properties:

  * The instance's name, used by Google Cloud.
  * The file system name, used by client-side tools such as `lfs`.
  * The storage capacity in gibibytes (GiB). Capacity can range from 9,000 GiB to 84,016,000 GiB (80.1 PiB). The maximum size of an instance depends on its performance tier.
  * The performance tier. Managed Lustre offers performance tiers ranging from 125 MBps per TiB to 1000 MBps per TiB, as well as a Dynamic tier that optimizes performance based on data access patterns, with an aggregate throughput of 25 MBps per TiB.
  * The location. For best performance, locate your instance in the same zone as your client VMs or GKE cluster.
  * The VPC network for this instance. This must be the same network as used for your VMs or clusters.



## Performance tiers and maximum storage capacities

Managed Lustre offers 4 set-performance tiers, and a Dynamic tier. Performance tiers affect the minimum and maximum instance size, and the step size between acceptable capacity values. You cannot change an instance's performance tier after it has been created.

See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for details.

You can increase the storage capacity of an instance after it's been created, up to the maximum value allowed for its performance tier and step size.

## Capacity calculator

Select a performance tier and enter your target capacity to find the nearest valid size. Valid sizes are rounded up based on the tier's minimum and step size.

## Quotas

Your project has quotas for throughput and capacity that are consumed when you create an instance. If you don't have enough quota in the instance's zone and VPC network for the instance size and performance tier that you select, the creation request fails. For more information, see [Quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas).

## Required permissions

To create a new Managed Lustre instance, you must have Managed Lustre Admin (`roles/lustre.admin`) IAM permissions for your project.

See [Access control with IAM](https://docs.cloud.google.com/managed-lustre/docs/access-control) for details.

You must also have [enabled the Managed Lustre API](https://docs.cloud.google.com/managed-lustre/docs/enable-api).

## Create an instance

You can create a new Managed Lustre instance from the following interfaces.

###  gcloud 

To create a new Managed Lustre instance, use the `gcloud lustre instances create` command:
    
    
    gcloud lustre instances create INSTANCE_ID \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY_GIB \
      --filesystem=FILESYSTEM \
      --location=LOCATION \
      --network=NETWORK_PATH
    

The following values must be specified:

  * INSTANCE_ID is the name of this Managed Lustre instance. It must:

    * Contain only lowercase letters, numbers, and hyphens.
    * Start with a letter.
    * Be between 1-63 characters.
    * End with a number or a letter.
    * Be unique within the project and location.
  * `--per-unit-storage-throughput` is the maximum throughput of the instance in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. Your choice of throughput affects the minimum and maximum storage capacity of the instance.

To specify the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier), set this to `0` and include the `--dynamic-tier-options-mode=DEFAULT_CACHE` flag. For example:
        
        gcloud lustre instances create my-dynamic-tier-instance \
          --per-unit-storage-throughput=0 \
          --dynamic-tier-options-mode=DEFAULT_CACHE \
          ...
        

  * `--capacity-gib` is the storage capacity of the instance in gibibytes (GiB). Allowed values depend on the storage throughput tier you specify. See the Performance tiers and maximum storage capacities section for details.

  * `--filesystem` is the name to assign to this Lustre file system. This name is used by client-side commands, including `mount` and `lfs`. It must be 8 characters or less in length, can only contain letters and/or numbers, and is case-sensitive.

It is recommended to choose a name that is unique across all Managed Lustre instances in the VPC. This allows multiple instances to be used from a single GKE node.

  * `--location` must be a valid Google Cloud zone that is supported by Managed Lustre. See [Supported locations](https://docs.cloud.google.com/managed-lustre/docs/locations) for a full list.

  * `--network` is the full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).

  * `--project` is your Google Cloud project ID.




Optional flags are the following:

  * `--dynamic-tier-options-mode` specifies the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) for this instance. Set the value of this flag to `DEFAULT_CACHE` and set `--per-unit-storage-throughput=0` to enable the Dynamic tier.

  * `--kms-key-name` specifies a customer-managed encryption key with which to encrypt this instance. See [Customer-managed encryption keys for Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/cmek) for details.

  * `--maintenance-policy-weekly-windows` and `--maintenance-policy-exclusion-window` define maintenance policies for this instance. See [Maintenance events and policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance) for details.

  * `--async` (optional) runs the command asynchronously. Instead of waiting for instance creation to complete, Google Cloud CLI returns an operation ID that can be used to query the command's status.




A successful request returns an operation ID:
    
    
    Create request issued for: [$INSTANCE_ID]
    Waiting for operation [projects/$PROJECT_ID/locations/us-central1-a/operations/
    operation-1234567890-609d21deae6f0-befaf0bc-867b1aa1] to complete...
    

Instance creation takes approximately 15 minutes for an instance with 9,000 GiB capacity, up to several hours for an instance with 84,016,000 GiB (80.1 PiB) capacity. See Query instance creation status for instructions on checking the status of your request.

###  REST 

To create an instance using the REST API, send a request to the following endpoint:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances?instanceId=INSTANCE_ID
    Authorization: Bearer AUTH_TOKEN
    {
      "filesystem": string,
      "perUnitStorageThroughput": int64,
      "capacityGib": int64,
      "network": string
    }
    

The following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.

  * ZONE must be a valid Google Cloud zone that is supported by Managed Lustre. See [Supported locations](https://docs.cloud.google.com/managed-lustre/docs/locations) for a full list.

  * INSTANCE_ID is the name of this Managed Lustre instance. It must:

    * Contain only lowercase letters, numbers, and hyphens.
    * Start with a letter.
    * Be between 1-63 characters.
    * End with a number or a letter.
    * Be unique within the project and location.
  * `filesystem` is the name to assign to this Lustre file system. This name is used by client-side commands, including `mount` and `lfs`. It must be 8 characters or less in length, can only contain letters and/or numbers, and is case-sensitive.

It is recommended to choose a file system name that is unique across all Managed Lustre instances in the VPC. This allows multiple instances to be used from a single GKE node.

  * `perUnitStorageThroughput` is the maximum throughput of the instance in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. Your choice of throughput affects the minimum and maximum storage capacity of the instance.

To specify the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier), set this to `0` and include the `dynamicTierOptions` object. For example:
        
        "perUnitStorageThroughput": 0,
        "dynamicTierOptions": {
          "mode": "DEFAULT_CACHE"
        }
        

  * `capacityGib` is the storage capacity of the instance in gibibytes (GiB). Allowed values depend on the storage throughput tier you specify. See the Performance tiers and maximum storage capacities section for details.

  * `network` is the full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).




The following fields are optional:

  * `dynamicTierOptions` enables the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) for this instance. The `mode` field within the `dynamicTierOptions` object must be set to `DEFAULT_CACHE` and `perUnitStorageThroughput` must be `0` to enable the Dynamic tier.

  * `kmsKey` specifies a customer-managed encryption key with which to encrypt this instance. See [Customer-managed encryption keys for Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/cmek) for details.




The API supports additional optional fields for instances. See the [`Instance` resource reference documentation](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances#Instance) for a full list and descriptions.

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click **Create**. The **Create an instance** page is displayed.

  3. Enter a unique **Instance name** and, optionally, a description. The instance name is used by Google Cloud to identify this instance.

  4. Enter a **Filesystem** name. This is the name that is used by client-side tools such as `lfs`. It must be 8 characters or less in length, can only contain letters and/or numbers, and is case-sensitive.

  5. Select a region and zone in which to create this instance. You should place your instance in the same region and zone as the Compute Engine VMs or Google Kubernetes Engine clusters that will connect to it.

  6. Select the performance tier for this instance.

  7. Specify the storage capacity in gibibytes (GiB) of your instance. Valid values depend on the storage throughput tier you select. See the Performance tiers and maximum storage capacities section for details.

  8. From the **Encryption** section, select either **Google-managed encryption key** or **Cloud Key Management Service key**. For information about the Cloud Key Management Service key option, see [Customer-managed encryption keys for Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/cmek).

  9. Optional: To control when maintenance can occur on this instance, expand the **Maintenance policy** section and configure a maintenance window or exclusion window. See [Maintenance events and policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance) for details.

  10. Select the **Network** that you created in [Create a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).




The **Summary** section of the page updates to show a cost estimate based on your selections.

Click **Submit** to continue. The instance creation process takes from 15 minutes to one hour, depending on the instance capacity.

## Query instance creation status

You can query the status of a create request from the following interfaces.

###  gcloud 

To query the status of a create operation, you can get either the operation or the instance.

To get the instance:
    
    
    gcloud lustre instances describe INSTANCE_NAME \
      --location=ZONE
    

The creation status is the value of `state`.

To get the operation, use the operation ID from the instance creation response. The operation ID has the following format:

  * `operation-1234567890123-6127783ad26ea-88913969-02748053`


    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=LOCATION
    

The creation status is the value of `done`.

When the instance has been created, the result of a get request on the instance is similar to the following response.

Note the IP address in the `mountPoint` field and your file system name; you'll need these values when mounting your instance.
    
    
    capacityGib: '27000'
    createTime: '2025-03-14T00:07:34.308574307Z'
    filesystem: lustre-fs
    mountPoint: 10.115.0.3@tcp:/testfs
    name: projects/$PROJECT/locations/us-central1-a/instances/$INSTANCE_NAME
    network: projects/$PROJECT/global/networks/default
    state: ACTIVE
    updateTime: '2025-03-14T00:15:37.101024263Z'
    

###  REST 

To query the status of a create operation, use the operation ID from the response. The operation ID has the following format:

  * `operation-1234567890123-6127783ad26ea-88913969-02748053`



Send a request to the following endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/operations/OPERATION_ID
    Authorization: Bearer
    

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations).

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click the instance name in the list. The **Instance Details** page appears, which includes the current status of your instance creation request.




## Troubleshooting

### IP address range exhausted

If instance creation fails with an IP address range exhausted error:
    
    
    FAILED_PRECONDITION: Invalid resource state for "NETWORK_RANGES_NOT_AVAILABLE": IP address range exhausted
    

or:
    
    
    Private Service Access IP address range exhausted or does not exist.
    

Follow the instructions in [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection) to modify the existing private connection to add IP address ranges.

We recommend a prefix length of at least /20 (4096 addresses).

### Network has not been peered

If instance creation fails with a network peering error:
    
    
    INVALID_ARGUMENT: the network has not been peered with Google managed services.
    

This error occurs when the VPC network specified in `--network` has not been peered with Google-managed services using Private Services Access.

To resolve this issue, follow the instructions in [Create and configure the VPC](https://docs.cloud.google.com/managed-lustre/docs/vpc#create_and_configure_the_vpc) to allocate an IP address range and establish the VPC peering connection.

## What's next

  * [Connect from a Compute Engine client](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine)
  * [Connect from Google Kubernetes Engine](https://docs.cloud.google.com/managed-lustre/docs/connect-from-kubernetes-engine-existing-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
