---
url: https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk/
title: Create VMs in bulk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:53.066768+00:00
---

# Create VMs in bulk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create VMs in bulk Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you want to create a large number of virtual machine (VM) instances that are identical and independent from each other, create VMs in bulk using the Google Cloud CLI or the Compute Engine API. You can create these VMs across all [zones in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) or distributed across certain zones.

For more details and associated limitations, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation). If you want to create instances with attached GPUs, see [Create GPU VMs in bulk](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk) instead.

## Before you begin

  * For VMs and any related resources that you plan to create, [make sure you have enough quota](https://docs.cloud.google.com/compute/resource-usage) and the [required permissions](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#expandable-1). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

To get the permissions that you need to create VMs in bulk, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create VMs in bulk. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs in bulk:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create VMs in bulk in a region

To create VMs in bulk in a region, use the gcloud CLI or the Compute Engine API.

If you specify a machine type or support for additional hardware such as a GPU or a local SSD, Compute Engine places the VMs in a zone within the region that supports the machine type and the additional hardware.

###  gcloud 

To create VMs in bulk in a region, use the following [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create):
    
    
    gcloud compute instances bulk create \
        ( --name-pattern="NAME_PATTERN" | --predefined-names=[PREDEFINED_NAMES] ) \
        --region=REGION \
        --count=COUNT \
        [ --min-count=MIN_COUNT \ ]
        [--location-policy=LOCATION_POLICY \ ]
        [--target-distribution-shape=TARGET_DISTRIBUTION_SHAPE ]
    

Replace the following:

  * NAME_PATTERN: the name pattern for the VMs. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAMES: a list of predefined names for the VMs to create. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * REGION: the region to create the VMs in.

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `--predefined-names`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  
  * LOCATION_POLICY: the zones to include or exclude within a region. Use a list of key-value pairs, with the zone as the key and the policy as the value. Valid values for the policy are `allow`, which is the default, and `deny`. The following is an example value for this flag:
        
        --location-policy=us-east1-b=allow,us-east1-c=deny
        

  * TARGET_DISTRIBUTION_SHAPE: the distribution of the VMs across the specified zones. Use the `--location-policy` flag to specify the zones. The following table shows the valid values for this flag:

Value | Description  
---|---  
`ANY_SINGLE_ZONE` | Enforces VM placement in a single zone, and prioritizes utilization of unused reservations. Use this to avoid cross-zone network egress or to reduce network latency. This is the default value.  
`BALANCED` | Attempts to distribute VMs evenly across all zones in the region.  
`ANY` | Allows distribution of VMs across multiple zones in a region. Chooses zones that have available resources and that maximize unused zonal reservations.  



###  REST 

To create VMs in bulk in a region, use the following [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
    
    {
      ...
      "namePattern": "NAME_PATTERN",
      "perInstanceProperties": {
        "PREDEFINED_NAME_1": {},
        "PREDEFINED_NAME_2": {},
        ...
      },
      "count": COUNT,
      "minCount": MIN_COUNT,
      "locationPolicy": {
        "LOCATION_POLICY"
        },
        "targetShape": "TARGET_DISTRIBUTION_SHAPE"
      ...
    }
    

Replace the following:

  * PROJECT_ID: the project ID.

  * REGION: the region to create the VMs in.

  * NAME_PATTERN: the name pattern for the VMs. Specify either this or `perInstanceProperties`. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAME_1, PREDEFINED_NAME_2, ...: a list of predefined names for the VMs to create. Specify either this or `namePattern`. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `perInstanceProperties`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  
  * LOCATION_POLICY: the zones to include or exclude within a region. Use a list of key-value pairs, with the zone as the key and the policy as the value. Valid values for the policy are `ALLOW`, which is the default, and `DENY`. The following is an example value for this field:
        
        "locations": {
          "zones/us-central1-a": { "preference": "ALLOW" },
          "zones/us-central1-c": { "preference": "DENY"  },
          ...
        },
        

  * TARGET_DISTRIBUTION_SHAPE: the distribution of VMs across the specified zones. Use the `locationPolicy` field to specify the zones. The following table shows the valid values for this field:

Value | Description  
---|---  
`ANY_SINGLE_ZONE` | Enforces VM placement in a single zone, and prioritizes utilization of unused reservations. Use this to avoid cross-zone network egress or to reduce network latency. This is the default value.  
`BALANCED` | Attempts to distribute VMs evenly across all zones in the region.  
`ANY` | Allows distribution of VMs across multiple zones in a region. Chooses zones that have available resources and that maximize unused zonal reservations.  



## Create VMs in bulk in a zone

To create VMs in bulk in a zone, use the gcloud CLI or the Compute Engine API.

###  gcloud 

To create VMs in bulk in a specific zone, use the following [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).
    
    
    gcloud compute instances bulk create \
        ( --name-pattern="NAME_PATTERN" | --predefined-names=[PREDEFINED_NAMES] ) \
        --zone=ZONE \
        --count=COUNT \
        [ --min-count=MIN_COUNT ]
    

Replace the following:

  * NAME_PATTERN: the name pattern for the VMs. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAMES: a list of predefined names for the VMs to create. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * ZONE: the zone to create the VMs in.

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `--predefined-names`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  



###  REST 

To create VMs in bulk in a zone, use the following [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      ...
      "namePattern": "NAME_PATTERN",
      "perInstanceProperties": {
        "PREDEFINED_NAME_1": {},
        "PREDEFINED_NAME_2": {},
        ...
      },
      "count": COUNT,
      "minCount": MIN_COUNT,
      ...
    }
    

Replace the following:

  * PROJECT_ID: the project ID.

  * ZONE: the zone to create the VMs in.

  * NAME_PATTERN: the name pattern for the VMs. Specify either this or `perInstanceProperties`. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAME_1, PREDEFINED_NAME_2, ...: a list of predefined names for the VMs to create. Specify either this or `namePattern`. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `perInstanceProperties`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  



## Create VMs with custom hostnames in bulk

You can create VMs with custom hostnames in bulk in a region or in a zone by using the gcloud CLI or the Compute Engine API.

You must manually configure the DNS record for your custom hostname. For more information, see [limitations](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#limitations).

If you don't specify a hostname, Compute Engine sets the hostname for VMs as one of the following:

  * `VM_NAME.c.PROJECT_ID.internal` when you enable global DNS
  * `VM_NAME.ZONE.c.PROJECT_ID.internal` when you enable zonal DNS



For more information, see [internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).

###  gcloud 

To create VMs in bulk with custom hostnames in a specific region, use the following [`gcloud beta compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/bulk/create).
    
    
    gcloud beta compute instances bulk create \
        ( --name-pattern="NAME_PATTERN" | --predefined-names=[PREDEFINED_NAMES] ) \
        --per-instance-hostnames=[VM_NAME=HOSTNAME,...] \
        --zone=REGION \
        --count=COUNT \
        [ --min-count=MIN_COUNT ]
        [--location-policy=LOCATION_POLICY \ ]
        [--target-distribution-shape=TARGET_DISTRIBUTION_SHAPE ]
    

Replace the following:

  * NAME_PATTERN: the name pattern for the VMs. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAMES: a list of predefined names for the VMs to create. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * [VM_NAME=HOSTNAME, ...]: a list of key-value pairs of predefined names for the VMs and fully qualified domain hostnames that you want to assign for the VMs. Custom hostnames must conform to [RFC 1035](https://tools.ietf.org/html/rfc1035) requirements for valid hostnames.

  * REGION: the zone to create the VMs in.

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `--predefined-names`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  
  * LOCATION_POLICY: the zones to include or exclude within a region. Use a list of key-value pairs, with the zone as the key and the policy as the value. Valid values for the policy are `ALLOW`, which is the default, and `DENY`. The following is an example value for this field:
        
        "locations": {
          "zones/us-central1-a": { "preference": "ALLOW" },
          "zones/us-central1-c": { "preference": "DENY"  },
          ...
        },
        

  * TARGET_DISTRIBUTION_SHAPE: the distribution of VMs across the specified zones. Use the `locationPolicy` field to specify the zones. The following table shows the valid values for this field:

Value | Description  
---|---  
`ANY_SINGLE_ZONE` | Enforces VM placement in a single zone, and prioritizes utilization of unused reservations. Use this to avoid cross-zone network egress or to reduce network latency. This is the default value.  
`BALANCED` | Attempts to distribute VMs evenly across all zones in the region.  
`ANY` | Allows distribution of VMs across multiple zones in a region. Chooses zones that have available resources and that maximize unused zonal reservations.  



###  REST 

To create VMs with custom hostnames in bulk in a specific region, use the following [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
    
    {
      ...
      "namePattern": "NAME_PATTERN",
      "perInstanceProperties": {
        "PREDEFINED_NAME_1": {"hostname": HOSTNAME_1},
        "PREDEFINED_NAME_2": {"hostname": HOSTNAME_2},
        ...
      },
      "count": COUNT,
      "minCount": MIN_COUNT,
      "locationPolicy": {
        "LOCATION_POLICY"
        },
        "targetShape": "TARGET_DISTRIBUTION_SHAPE"
      ...
    }
    

Replace the following:

  * PROJECT_ID: the project ID.

  * REGION: the region to create the VMs in.

  * NAME_PATTERN: the name pattern for the VMs. Specify either this or `perInstanceProperties`. Use a sequence of hash (`#`) characters for Compute Engine to replace with a sequence of numbers. For example, using `vm-#` for the name pattern generates VMs with names such as `vm-1` and `vm-2`, up to the number of VMs specified by `--count`, which must be less than or equal to the number of VMs that the name pattern allows.

When using a name pattern, Compute Engine tries to avoid name conflicts by checking the names of existing VMs created from previous requests.

  * PREDEFINED_NAME_1, PREDEFINED_NAME_2, ...: a list of predefined names for the VMs to create. Specify either this or `namePattern`. If using this flag and specifying `COUNT`, `COUNT` must equal the number of names provided.

  * HOSTNAME_1, HOSTNAME_2, ...: fully qualified domain hostnames that you want to assign for the VMs. Custom hostnames must conform to [RFC 1035](https://tools.ietf.org/html/rfc1035) requirements for valid hostnames.

For example, to create two VMs `vm-1` and `vm-2` with custom hostnames `my-host1234.example.com` and `test.example.com` respectively, specify the `hostname` property in `perInstanceProperties` as follows:
        
        {
        ...
        "perInstanceProperties": {
        "vm-1": { "hostname": "my-host1234.example.com" },
        "vm-2": { "hostname": "test.example.com" },
        ...}
        },
        

  * COUNT: the number of VMs to create. This must be less than or equal to the number of VMs allowed by `NAME_PATTERN`. Or, if using `perInstanceProperties`, you don't have to specify `COUNT`, but if you do, it must be equal to the number of names provided.

  * MIN_COUNT: the minimum number of VMs to create. The following table describes the behavior of the request depending on how you set this flag:

Value | Description  
---|---  
Not set  | Default value is `COUNT`. If Compute Engine can't create the number of VMs specified by `COUNT`, the request fails and no VMs are created.  
`1` | Compute Engine creates as many VMs as possible, up to `COUNT`.  
Greater than `1` and less than `COUNT` | Compute Engine creates at least `MIN_COUNT` VMs up to a maximum of `COUNT` VMs. If `MIN_COUNT` VMs can't be created, the request fails and no VMs are created.  
  * LOCATION_POLICY: the zones to include or exclude within a region. Use a list of key-value pairs, with the zone as the key and the policy as the value. Valid values for the policy are `ALLOW`, which is the default, and `DENY`. The following is an example value for this field:
        
        "locations": {
          "zones/us-central1-a": { "preference": "ALLOW" },
          "zones/us-central1-c": { "preference": "DENY"  },
          ...
        },
        

  * TARGET_DISTRIBUTION_SHAPE: the distribution of VMs across the specified zones. Use the `locationPolicy` field to specify the zones. The following table shows the valid values for this field:

Value | Description  
---|---  
`ANY_SINGLE_ZONE` | Enforces VM placement in a single zone, and prioritizes utilization of unused reservations. Use this to avoid cross-zone network egress or to reduce network latency. This is the default value.  
`BALANCED` | Attempts to distribute VMs evenly across all zones in the region.  
`ANY` | Allows distribution of VMs across multiple zones in a region. Chooses zones that have available resources and that maximize unused zonal reservations.  



## Check the status of a request to create VMs in bulk

When you create a mutation request, Compute Engine returns an `operation` resource that you can poll to get the status of the operation. For more information, see [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

To get the status of a bulk insert request, [send an HTTP `GET` request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get) to the `operation` resource:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations/OPERATION_ID
    

To get the status of a regional bulk insert request, send the following request:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/operations/OPERATION_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you're creating VMs
  * `REGION`: the region in which you are creating VMs
  * `ZONE`: the zone in which you are creating VMs
  * `OPERATION_ID`: the bulk insert operation ID



The `instancesBulkInsertOperationMetadata` object in the response contains details about the operation on a per-zone basis in the `perLocationStatus` field. For each zone included in the bulk creation request, `perLocationStatus` contains the following fields:

  * `status`: The status is one of the following: 
    * `CREATING`: VM creation is in progress in the zone.
    * `ROLLING_BACK`: The request failed in the zone and it's being rolled back.
    * `DONE`: VM creation or rollback has completed successfully in the zone.
  * `targetVmCount`: The number of VMs that Compute Engine attempts to create in the zone. Compute Engine determines this count after initial checks, and it doesn't change during the operation. When you check the operation status, this field is always present for each zone.
  * `createdVmCount`: The number of VMs already created in the zone. This value does not exceed `targetVmCount` for a given zone. 
    * `failedToCreateVmCount`: The number of VMs that failed to create in the zone.
    * `deletedVmCount`: The number of VMs that were deleted in the zone as part of rolling back of a failed operation.



The `progress` field in the response represents the percentage of completion of the operation.

The status of the bulk insert operation is `RUNNING` until Compute Engine successfully creates at least the minimum number of VMs and no more VM creation or rollback of the request happens.

When the bulk insert operation is in progress, you should see a response similar to the following:
    
    
    {
      "kind" : "compute#operation",
      "id": "4653028658507445766",
      "name": "operation-1587661030638-5a3f823c143e3-e33bbfa3-bd72185c",
      "operationType": "bulkInsert",
      "targetLink":  "https://www.googleapis.com/compute/v1/projects/my-project"
      "targetId": 4653028658507445766,
      "status": "RUNNING",
      "progress": 2,
      "user": "example@google.com",
      "insertTime": "2023-04-23T09:57:13.474-07:00",
      "startTime": "2023-04-23T09:57:13.474-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/operations/operation-1587661030638-5a3f823c143e3-e33bbfa3-bd72185c",
      "operationGroupId": "4653028658507445766",
      "metadata":
        "instances_bulk_insert_operation_metadata": {
          "per_location_status": {
             "zones/us-central1-a": {
               "status": "CREATING",
               "targetVmCount": 50,
               "createdVmCount": 1
             }
          }
        }
    }
    

In this example, one instance has been successfully created and the operation is 2% completed.

The operation returns the status `DONE` when Compute Engine successfully creates at least the minimum number of VMs specified by `minCount`, or when Compute Engine completes the rollback of the request. After successful creation of the requested number of VMs, you get a response similar to the following:
    
    
    {
      "endTime": "2023-04-23T09:58:13.474-07:00",
      "id": "5053101474378293244",
      "insertTime": "2023-04-23T09:57:13.474-07:00",
      "instancesBulkInsertOperationMetadata": {
        "perLocationStatus": {
          "zones/us-central1-a": {
            "status": "DONE",
            "createdVmCount": 50,
            "targetVmCount": 50
          }
        }
      },
      "kind": "compute#operation",
      "name": "operation-1587661030638-5a3f823c143e3-e33bbfa3-bd72185c",
      "operationGroupId": "4653028658507445766",
      "operationType": "bulkInsert",
      "progress": 100,
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/operations/operation-1587661030638-5a3f823c143e3-e33bbfa3-bd72185c",
      "startTime": "2023-09-11T16:21:55.629-07:00",
      "status": "DONE",
      "targetId": "625521788110",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/my-project",
      "user": "example@google.com",
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a"
    }
    

For more information, see the documentation for the [`instancesBulkInsertOperationMetadata` object](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get).

## Check the status of a single VM

To check the status of a single VM created from a request to create VMs in bulk, use the gcloud CLI or the Compute Engine API.

###  gcloud 

  1. From the `Operation` returned by the request, get the value of the `operationGroupId` property.

  2. Use the `operationGroupId` property as a filter with the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) to search across all operations and all zones in the project for VMs associated with the regional or zonal request:
         
         gcloud compute operations list \
            --filter=(operationGroupId=OPERATION_GROUP_ID)
         

  3. Get the rest of the VM's properties by doing any of the following:

     * From the list of operations, the `targetLink` represents the path of the VM. Use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with this path as the name of the VM to get the VM's properties:
           
           gcloud compute instances describe VM_NAME
           

     * Use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) with a filter that includes the names of the VMs from the list of operations:
           
           gcloud compute instances list VM_NAME \
              --filter=(name=VM_NAME_1) OR (name=VM_NAME_2)
           

     * Use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) to get the properties of VMs from across all zones and regions, and filter by either a label that is unique to the instances or by their names:
           
           gcloud compute instances list \
              --filter=(name=VM_NAME_1) OR (name=VM_NAME_2)
           




###  REST 

  1. From the `Operation` returned by the request, get the value of the `operationGroupId` property.

  2. Use the `operationGroupId` property to get the list of VM operations associated with the regional or zonal request:

     * If you sent a regional request, then, to search across all operations and all zones in the project, use the [`globalOperations.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations/aggregatedList) and include `operationGroupId` property as a filter:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/aggregated/operations?filter=(operationGroupId=OPERATION_GROUP_ID)
           

     * If you sent a zonal request, then, to list the operations in that zone, use the [`zoneOperations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get) and include the `operationGroupId` property in the body of the request:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/bulkInsert
           
           {
           ...
           "operationGroupId":"OPERATION_GROUP_ID"
           ...
           }
           

  3. Get the rest of the VM's properties by doing any of the following:

     * From the list of operations, the `targetLink` represents the path of the VM. Use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) with this path as the name of the VM to get all of the VM's properties:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/VM_NAME
           

     * Use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) with a filter that includes the names of the VMs from the list of operations:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances?filter=(name=VM_NAME_1) OR (name=VM_NAME_2)
           

     * Use the [`instances.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList) to get the properties of VMs from across all zones and regions, and filter by either a label that is unique to the instances or by their names:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/aggregated/instances?filter=(name=VM_NAME_1) OR (name=VM_NAME_2)
           




## Pseudocode examples

The following pseudocode examples show how to customize requests for creating VMs in bulk.

### Create VMs in bulk in one region from a set of regions

The following pseudocode describes how to create 1,000 VMs in one region from a set of regions. When attempting to create VMs in bulk in one region from a set of regions, the request first checks for capacity. If there is not enough capacity, the request fails immediately and tries again with the next region in the set.

  1. Specify the number of VMs to create within a zone.
         
         nTarget = 1000
         

  2. Designate the regions to attempt to create the VMs in.
         
         acceptableRegions = ["us-central1", "us-east1", "us-west1"]
         

  3. Iterate through the regions, and attempt to create the VMs in each region until successful.
         
         for region in acceptableRegions:
           call bulk API: region=region, location-policy=location-policy, count=nTarget
           if request succeeds and the operation succeeds:
             break
         




### Create VMs of a specific machine type in bulk in a zone

The following pseudocode describes how to create multiple VMs of a specified machine type in a zone. When attempting to create VMs in bulk of the same machine type, the request first checks for availability of those machine types. If there is not enough of the machine type available, the request fails immediately and tries again with the next machine type.

  1. Specify the number of VMs to create and the region to create them in.
         
         nTarget = 1000
         region = "us-central1"
         

  2. Specify the machine families to attempt to create the VMs of.
         
         acceptableMachineFamilies = ["n2","c2","e2","n1"]
         

  3. Iterate through the set of machine types and attempt to create the VMs of the machine type until successful.
         
         for family in acceptableMachineFamilies:
           call bulk APIs: region=region, count=nTarget, machineFamily=family
           if request succeeds and the operation succeeds:
             break
         




### Create more than 5,000 VMs in a zone

When creating VMs in bulk, [you can only create 5,000 VMs with each request](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation#number_of_vms). The following pseudocode describes how to create more than 5,000 VMs in a zone by issuing multiple requests.

  1. Specify the number of VMs to create, a counter to keep track of the total number of created VMs, the region to create the VMs in, and a variable to store the zone that Compute Engine creates the VMs in.
         
         nTarget = 10000
         nCreated = 0
         region = "us-central1"
         targetZone = ""
         

  2. Issue an initial request to create 5,000 VMs, save the zone returned by the request, and update the counter of the number of VMs created.
         
         call bulk API: region=region, count=5000
         targetZone = zone chosen by bulk API
         nCreated += # of VMs created
         

  3. Continue issuing requests to create up to 5,000 VMs at a time in the zone until Compute Engine creates the specified number of VMs.
         
         while(nTarget - nCreated > 0):
           call bulk API: zone=targetZone, count=5000
           nCreated += # of VMs created
         




### Create VMs in bulk and view their status

The following procedure shows you how to create a group of VMs that have predefined names and then view their status:

  1. Specify the number of VMs to create, the zone to create them in, and a data structure to store the names in.
         
         nTarget = 1000
         targetZone = "us-central-1a"
         names = []
         

  2. Generate the patterned names for the VMs and add the names to the data structure.
         
         for n in range(0, 1000):
           names.push("instance-%d".format(n))
         

  3. Create the VMs, and use `perInstanceProperties` to specify the names.
         
         call bulk API(zone=targetZone, count=nTarget, names=perInstanceProperties)
         

  4. Get the details of the VMs by using the [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list) with a filter for the names of VMs to return the details about.
         
         instances.list(filter=(name = "instance-1") OR (name = "instance-2") ...)
         




## What's next

After creating VMs in bulk, do either or both of the following to simplify management of those VMs:

  * **Add the VMs to an unmanaged instance group.** [Adding VMs to an unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances) lets you use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Unmanaged instance groups don't provide load balancing or management of the [VM lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

  * **Use labels.** Labels let you [organize resources using key-value pairs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
