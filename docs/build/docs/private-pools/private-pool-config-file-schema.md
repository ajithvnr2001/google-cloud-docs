---
url: https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema/
title: Private pool configuration file schema \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:26.929483+00:00
---

# Private pool configuration file schema  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Private pool configuration file schema Stay organized with collections  Save and categorize content based on your preferences. 

A private pool configuration file (private pool config file) contains instructions for Cloud Build to create a private pool based on your specifications. A private pool config file contains information such as the disk size and machine type you want to use for your private pool. The private pool config file is required when you create and manage private pools using the `gcloud` tool or the Cloud Build API.

**Note:** The private pool config file is different from the [Cloud Build configuration file](https://docs.cloud.google.com/build/docs/build-config): the Cloud Build config file lets you configure your build whereas the private pool config file lets you configure your private pool.

## Structure of a private pool config file

You can write the private pool config file using the YAML or the JSON syntax. To create and manage private pools using `curl`, write the private pool config file in the JSON format. To create and manage private pools using the `gcloud` tool, write the private pool config file in the YAML or the JSON format.

A private pool config file has the following structure:

###  YAML 
    
    
    privatePoolV1Config:
      networkConfig:
        egressOption: NO_PUBLIC_EGRESS
        peeredNetwork: PEERED_NETWORK,
        peeredNetworkIpRange: PEERED_NETWORK_IP_RANGE
      workerConfig:
        diskSizeGb: PRIVATE_POOL_DISK_SIZE,
        machineType: PRIVATE_POOL_MACHINE_TYPE,
        workerRelease: CHANNEL_OR_VERSION
    

###  JSON 
    
    
    {
      "privatePoolV1Config": {
        "networkConfig": {
          "egressOption": "NO_PUBLIC_EGRESS",
          "peeredNetwork": "PEERED_NETWORK",
          "peeredNetworkIpRange": "PEERED_NETWORK_IP_RANGE"
        },
        "workerConfig": {
          "diskSizeGb": "PRIVATE_POOL_DISK_SIZE",
          "machineType": "PRIVATE_POOL_MACHINE_TYPE",
          "workerRelease": "CHANNEL_OR_VERSION"
        }
      }
    }
    

The fields in the private pool config file are explained as follows:

## `networkConfig`

This is an optional field. Specify `networkConfig` only if you're peering your VPC network with the service producer network.

### `egressOption`

This is an optional field. Set the value of this field to `NO_PUBLIC_EGRESS` if you're creating your private pool within a VPC Service Controls perimeter. If you don't include this field in the private pool config file, public egress is enabled. For information on setting up VPC Service Controls for private pools, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

### `peeredNetwork`

This is a required field if your private pool config file contains the `networkConfig` field. Set the value of this field to the network resource URL of the VPC network that is peered to the service producer network. The network resource URL must be of the format `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`, where NETWORK_PROJECT_ID is the project ID of the Google Cloud project that holds your VPC network and NETWORK_NAME is the name of your VPC network. If you don't specify a value, Cloud Build uses the [service producer network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment) by default.

### `peeredNetworkIpRange`

This is an optional field. Set the value of this field to specify the internal IP range that VMs can be assigned to within the peered network's allocated range. If the specified IP range can't be allocated within the range of the private connection, for example due to size limitations or an invalid starting IP, then the private pool can't be created.

`peeredNetworkIpRange` is specified using Classless Inter-Domain Routing (CIDR) notation in the format `'STARTING_IP/SUBNET_PREFIX_SIZE'`. If this field is used, then `SUBNET_PREFIX_SIZE` must be specified. `SUBNET_PREFIX_SIZE` determines the size of the IP range. It must begin with a slash (`/`) and have a value less than or equal to 29.The `STARTING_IP` portion is optional, and specifies the starting address of the range. If the `STARTING_IP` is not specified, then a starting address is automatically assigned from within the private connection range. If no value is specified for `peeredNetworkIpRange`, a default value of `/24` will be used which automatically assigns a starting IP with a range of 256 IPs. 

The value of `SUBNET_PREFIX_SIZE` must not exceed 29. A larger number specifies a larger subnet prefix, which would leave fewer possible IPs and result in a smaller IP range. Since an IP address is 32 bits, a prefix size of `/24` allows 256 possible IPs in the range (eight bits) whereas a prefix size of `/29` leaves eight possible IPs (three bits). The maximum number of builder VMs is limited to the number of usable IPs in the range (the total possible number of IPs in the range minus two).

See the following for examples of the `peeredNetworkIpRange` field:

  * `192.168.0.0/24` specifies an IP range starting at 192.168.0.0 with a subnet prefix size of 24 (256 IPs, with 254 usable IPs). 
  * `/29` specifies a range with an automatically determined starting IP and a subnet prefix size of 29 (eight IPs, with six usable IPs).



## `workerConfig`

This is a required field. It contains configuration options for your private pool.

### `diskSizeGb`

This is an optional field. Use this field to specify a disk size for your private pool instance in GB. Specify a value greater than or equal to 100 and less than or equal to 4000. If you don't include this field in your private pool config file, or if you specify `0` as the value of this field, Cloud Build uses the default value of 100.

### `machineType`

This is an optional field. Use this field to specify the [Compute Engine machine type](https://docs.cloud.google.com/compute/docs/machine-resource#predefined_machine_types) for your private pool instance. If you don't specify a value, then Cloud Build uses the default value of `e2-medium`. Otherwise, specify one of the following machine types:

#### Machine types

`e2` | `n2d` | `c3`  
---|---|---  
e2-medium | n2d-standard-2 | c3-standard-4  
e2-standard-2 | n2d-standard-4 | c3-standard-8  
e2-standard-4 | n2d-standard-8 | c3-standard-22  
e2-standard-8 | n2d-standard-16 | c3-standard-44  
e2-standard-16 | n2d-standard-32 | c3-standard-88  
e2-standard-32 | n2d-standard-48 | c3-standard-176 |   
e2-highmem-2 | n2d-standard-64 | c3-highcpu-4 |   
e2-highmem-4 | n2d-standard-80 | c3-highcpu-8 |   
e2-highmem-8 | n2d-standard-96 | c3-highcpu-22 |   
e2-highmem-16 | n2d-standard-128 | c3-highcpu-44 |   
e2-highcpu-2 | n2d-standard-224 | c3-highcpu-88 |   
e2-highcpu-4 | n2d-highmem-2 | c3-highcpu-176 |   
e2-highcpu-8 | n2d-highmem-4 | c3-highmem-4 |   
e2-highcpu-16 | n2d-highmem-8 | c3-highmem-8 |   
e2-highcpu-32 | n2d-highmem-16 | c3-highmem-22 |   
| n2d-highmem-32 | c3-highmem-44 |   
| n2d-highmem-48 | c3-highmem-88 |   
| n2d-highmem-64 | c3-highmem-176 |   
| n2d-highmem-80 |  |   
| n2d-highmem-96 |  |   
| n2d-highcpu-2 |  |   
| n2d-highcpu-4 |  |   
| n2d-highcpu-8 |  |   
| n2d-highcpu-16 |  |   
| n2d-highcpu-32 |  |   
| n2d-highcpu-48 |  |   
| n2d-highcpu-64 |  |   
| n2d-highcpu-80 |  |   
| n2d-highcpu-96 |  |   
| n2d-highcpu-128 |  |   
| n2d-highcpu-224 |  |   
  
The following table shows the availability of machine types by region:

#### Machine type availability by region

`c3-standard-*` | `c3-highcpu-*` | `c3-highmem-*` | `e2-*` | `n2d-*`  
---|---|---|---|---  
asia-northeast1 | asia-southeast1 | asia-southeast1 | africa-south1 | africa-south1  
asia-southeast1 | europe-west1 | europe-west1 | asia-east1 | asia-east1  
australia-southeast1 | europe-west3 | europe-west2 | asia-east2 | asia-east2  
europe-west1 | europe-west4 | europe-west3 | asia-northeast1 | asia-northeast1  
europe-west2 | me-central2 | europe-west4 | asia-northeast2 | asia-northeast2  
europe-west3 | us-central1 | us-central1 | asia-northeast3 | asia-northeast3  
europe-west4 | us-east1 | us-east1 | asia-south1 | asia-south1  
europe-west9 | us-east4 | us-east4 | asia-south2 | asia-south2  
me-central2 | us-east5 | us-east5 | asia-southeast1 | asia-southeast1  
me-west1 | us-west2 | us-west1 | asia-southeast2 | asia-southeast2  
northamerica-northeast1 | us-west3 | us-west2 | australia-southeast1 | australia-southeast1  
southamerica-east1 |  | us-west4 | australia-southeast2 | australia-southeast2  
us-central1 |  |  | europe-central2 | europe-central2  
us-east1 |  |  | europe-north1 | europe-north1  
us-east4 |  |  | europe-north2 | europe-southwest1  
us-east5 |  |  | europe-southwest1 | europe-west1  
us-west1 |  |  | europe-west1 | europe-west10  
us-west2 |  |  | europe-west2 | europe-west12  
us-west3 |  |  | europe-west3 | europe-west2  
us-west4 |  |  | europe-west4 | europe-west3  
|  |  | europe-west6 | europe-west4  
|  |  | europe-west8 | europe-west6  
|  |  | europe-west9 | europe-west8  
|  |  | europe-west10 | europe-west9  
|  |  | europe-west12 | me-central1  
|  |  | me-central1 | me-central2  
|  |  | me-central2 | me-west1  
|  |  | me-west1 | northamerica-northeast1  
|  |  | northamerica-northeast1 | northamerica-northeast2  
|  |  | northamerica-northeast2 | southamerica-east1  
|  |  | northamerica-south1 | southamerica-west1  
|  |  | southamerica-east1 | us-central1  
|  |  | southamerica-west1 | us-east1  
|  |  | us-central1 | us-east4  
|  |  | us-east1 | us-east5  
|  |  | us-east4 | us-south1  
|  |  | us-east5 | us-west1  
|  |  | us-south1 | us-west2  
|  |  | us-west1 | us-west3  
|  |  | us-west2 | us-west4  
|  |  | us-west3 |   
|  |  | us-west4 |   
  
### `enableNestedVirtualization`

This is an optional field. If your private pool uses a VM with a `C3` machine type, then you can enable nested virtualization to run other VM instances inside your private pool's VM. For more information, see [About nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview).

### `workerRelease`

This is an optional field, containing either the [channel](https://docs.cloud.google.com/build/docs/release-channels) name or a specific [release version](https://docs.cloud.google.com/build/docs/release-channels#available_releases) to use for all builds using this worker pool.

## What's next

  * Learn how to [run builds in private pools](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool).
  * Learn how to [create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
