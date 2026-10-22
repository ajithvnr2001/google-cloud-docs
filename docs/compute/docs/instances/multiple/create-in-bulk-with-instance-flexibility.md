---
url: https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility/
title: Create VMs in bulk with instance flexibility \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:17.624376+00:00
---

# Create VMs in bulk with instance flexibility  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create VMs in bulk with instance flexibility Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure instance flexibility when you create virtual machines (VMs) in bulk. Instance flexibility lets you specify multiple machine types, rank them by preference, and override minimum CPU platform and disk settings for each selection so that Compute Engine can provision VMs based on capacity and quota availability in a region.

For more information about instance flexibility for VMs created in bulk, see [About instance flexibility for VMs created in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms).

## Before you begin

  * For VMs and any related resources that you plan to create, [make sure you have enough quota](https://docs.cloud.google.com/compute/resource-usage). 
  * If you want to create Spot VMs in bulk, then view the availability of resources before you create VMs. Checking the availability of resources helps reduce your chances of encountering resource availability errors when you create VMs. For instructions, see [View resource availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
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

## Create VMs with multiple machine types of equal preference

If your workload can operate on several different machine types, you can specify a list of all compatible machine types in a single instance selection. The following examples show how you can specify multiple machine types of equal preference.

###  gcloud 

To create VMs in bulk with a single instance selection, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--instance-selection-machine-types` flag.
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --region=REGION \
        --count=COUNT \
        --instance-selection-machine-types=MACHINE_TYPE_1,MACHINE_TYPE_2
    

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [name pattern](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create#--name-pattern) for the VMs
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types to use for the VMs
  * `REGION`: the region in which to create the VMs



**Example**
    
    
    gcloud compute instances bulk create \
        --name-pattern=test-bulk-# \
        --region=us-central1 \
        --count=10 \
        --instance-selection-machine-types=c3-standard-8,n2-standard-8,c2-standard-8
    

###  REST 

In the Compute Engine API, make a `POST` request to the [`regionInstances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstances/bulkInsert). In the request body, include `instanceFlexibilityPolicy` with one `instanceSelections` entry that lists the machine types.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "selection-1": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2"
            ]
          }
        }
      }
    }
    

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [name pattern](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create#--name-pattern) for the VMs
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types to use for the VMs
  * `IMAGE_PROJECT`: the project that contains the image
  * `IMAGE`: the name of the image or image family to use
  * `PROJECT_ID`: your project ID
  * `REGION`: the region in which to create the VMs



**Example**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/instances/bulkInsert
    {
      "count": 10,
      "namePattern": "test-bulk-#",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/debian-12"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "selection-1": {
            "machineTypes": [
              "c3-standard-8",
              "n2-standard-8",
              "c2-standard-8"
            ]
          }
        }
      }
    }
    

## Create VMs with multiple machine types ranked by preference

If you want Compute Engine to choose machine types in a specific order, you can configure multiple instance selections. Each instance selection includes a list of machine types and a rank, which is an integer that defines the preference for the machine types. A lower rank indicates a higher preference. Compute Engine attempts to create VMs using machine types with a higher preference (lower rank). If those machine types aren't available, Compute Engine uses machine types with a lower preference (higher rank).

The following examples show how to specify multiple instance selections with ranks.

###  gcloud 

To create VMs in bulk with multiple instance selections, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) and specify the `--instance-selection` flag multiple times.
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --region=REGION \
        --count=COUNT \
        --instance-selection "name=INSTANCE_SELECTION_1,rank=0,machine-type=MACHINE_TYPE_1,machine-type=MACHINE_TYPE_2" \
        --instance-selection "name=INSTANCE_SELECTION_2,rank=1,machine-type=MACHINE_TYPE_3,machine-type=MACHINE_TYPE_4"
    

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [name pattern](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create#--name-pattern) for the VMs
  * `INSTANCE_SELECTION_1`: the name for the first instance selection
  * `INSTANCE_SELECTION_2`: the name for the second instance selection
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types for the first instance selection
  * `MACHINE_TYPE_3`, `MACHINE_TYPE_4`: the machine types for the second instance selection
  * `REGION`: the region in which to create the VMs



**Example**
    
    
    gcloud compute instances bulk create \
        --name-pattern=test-bulk-# \
        --region=us-central1 \
        --count=10 \
        --instance-selection "name=most-preferred,rank=0,machine-type=c3-standard-16,machine-type=n2-standard-16,machine-type=c2-standard-16" \
        --instance-selection "name=least-preferred,rank=1,machine-type=c3-standard-8,machine-type=n2-standard-8,machine-type=c2-standard-8"
    

###  REST 

In the Compute Engine API, make a `POST` request to the [`regionInstances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstances/bulkInsert). In the request body, include `instanceFlexibilityPolicy` and specify multiple entries in `instanceSelections`, each with a list of machine types and a `rank`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "INSTANCE_SELECTION_1": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2"
            ],
            "rank": 1
          },
          "INSTANCE_SELECTION_2": {
            "machineTypes": [
              "MACHINE_TYPE_3",
              "MACHINE_TYPE_4"
            ],
            "rank": 2
          }
        }
      }
    }
    

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [naming pattern](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk#name-pattern) for the VMs
  * `INSTANCE_SELECTION_1`: the name for the first instance selection
  * `INSTANCE_SELECTION_2`: the name for the second instance selection
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types for the first instance selection
  * `MACHINE_TYPE_3`, `MACHINE_TYPE_4`: the machine types for the second instance selection
  * `IMAGE_PROJECT`: the project that contains the image
  * `IMAGE`: the name of the image or image family to use
  * `PROJECT_ID`: your project ID
  * `REGION`: the region in which to create the VMs



**Example**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/instances/bulkInsert
    {
      "count": 10,
      "namePattern": "test-bulk-#",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/debian-12"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "most-preferred": {
            "machineTypes": [
              "c3-standard-16",
              "c2-standard-16"
            ],
            "rank": 1
          },
          "least-preferred": {
            "machineTypes": [
              "n2-standard-16",
              "c3-standard-8",
              "n2-standard-8",
              "c2-standard-8"
            ],
            "rank": 2
          }
        }
      }
    }
    

## Create VMs with multiple machine types, minimum CPU platform, and disk overrides

In addition to specifying machine types and ranks, you can override the [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) and override or add to the disk definitions in `instanceProperties` for each instance selection. For example, if `instanceProperties` specifies a Persistent Disk and you select an N4 machine series, then you must override the boot disk with a supported Google Cloud Hyperdisk type.

For more information about supported disk types and how Compute Engine applies overrides, see the following resources:

  * [Machine series support for Persistent Disks](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series)
  * [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support)
  * [Instance property overrides in instance selections](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms#instance-property-overrides)



To create VMs in bulk with multiple machine types, minimum CPU platform, and disk overrides, select one of the following options:

###  gcloud 

To create VMs in bulk with multiple machine types, minimum CPU platform, and disk overrides, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--instance-flexibility-policy` flag. To override the default boot disk from `instanceProperties`, also include the `--boot-disk-device-name` flag and specify the same `deviceName` in the instance selection:
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --region=REGION \
        --count=COUNT \
        --boot-disk-device-name=BOOT_DISK_DEVICE_NAME \
        --instance-flexibility-policy='{"instanceSelections":
            {"INSTANCE_SELECTION_1":{"rank":RANK_1,"machineTypes":["MACHINE_TYPE_1","MACHINE_TYPE_2"],"minCpuPlatform":"MIN_CPU_PLATFORM_1","disks":[{"deviceName":"BOOT_DISK_DEVICE_NAME_1","boot":true,"initializeParams":{"diskType":"DISK_TYPE_1","diskSizeGb":DISK_SIZE_1,"sourceImage":"projects/IMAGE_PROJECT_1/global/images/IMAGE_1"}}]},
            "INSTANCE_SELECTION_2":{"rank":RANK_2,"machineTypes":["MACHINE_TYPE_3"],"minCpuPlatform":"MIN_CPU_PLATFORM_2","disks":[{"deviceName":"BOOT_DISK_DEVICE_NAME_2","boot":true,"initializeParams":{"diskType":"DISK_TYPE_2","diskSizeGb":DISK_SIZE_2,"sourceImage":"projects/IMAGE_PROJECT_2/global/images/IMAGE_2"}}]}}}'
    

Alternatively, to configure the instance flexibility policy by using a YAML or JSON file, use the [`--flags-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) instead of the `--instance-flexibility-policy` flag:
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --region=REGION \
        --count=COUNT \
        --boot-disk-device-name=BOOT_DISK_DEVICE_NAME \
        --flags-file=FILE_NAME.yaml
    

**Note:** If you only need to override the minimum CPU platform and don't require disk overrides, then you can include `min-cpu-platform=MIN_CPU_PLATFORM` in the `--instance-selection` flag instead of using the `--instance-flexibility-policy` flag.

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [name pattern](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create#--name-pattern) for the VMs
  * `REGION`: the region in which to create the VMs
  * `BOOT_DISK_DEVICE_NAME`: the device name for the default boot disk in `instanceProperties`
  * `INSTANCE_SELECTION_1`, `INSTANCE_SELECTION_2`: the names of the instance selections
  * `RANK_1`, `RANK_2`: optional numbers that represent your order of preference for each instance selection; a lower value indicates a higher preference
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types for the first instance selection
  * `MACHINE_TYPE_3`: the machine type for the second instance selection
  * `MIN_CPU_PLATFORM_1`, `MIN_CPU_PLATFORM_2`: optional [minimum CPU platforms](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) for the VMs in each instance selection
  * `BOOT_DISK_DEVICE_NAME_1`, `BOOT_DISK_DEVICE_NAME_2`: the device names for the boot disks in each instance selection; to override the default boot disk, specify the same name as `BOOT_DISK_DEVICE_NAME`
  * `DISK_TYPE_1`, `DISK_TYPE_2`: the disk types for the disk overrides, such as `pd-ssd` or `hyperdisk-balanced`
  * `DISK_SIZE_1`, `DISK_SIZE_2`: the disk sizes for the disk overrides
  * `IMAGE_PROJECT_1`, `IMAGE_PROJECT_2`: the projects that contain the images for the disk overrides
  * `IMAGE_1`, `IMAGE_2`: the names of the images or image families for the disk overrides
  * `FILE_NAME.yaml`: the name of the YAML or JSON file that contains the `--instance-flexibility-policy` configuration



**Example**

The following example creates 10 VMs using two instance selections that specify a minimum CPU platform, override the default boot disk, and attach additional disks:
    
    
    gcloud compute instances bulk create \
        --name-pattern=test-bulk-# \
        --region=us-central1 \
        --count=10 \
        --boot-disk-device-name=boot-disk \
        --instance-flexibility-policy='{"instanceSelections":
            {"selection-1":{"machineTypes":["n2-standard-8","c2-standard-8"],"minCpuPlatform":"Intel Cascade Lake","disks":[{"type":"PERSISTENT","deviceName":"boot-disk","boot":true,"initializeParams":{"diskType":"pd-ssd","diskSizeGb":50,"sourceImage":"projects/debian-cloud/global/images/family/debian-12"}},{"type":"SCRATCH","initializeParams":{"diskType":"local-ssd"}}]},
            "selection-2":{"machineTypes":["c4a-standard-8"],"disks":[{"type":"PERSISTENT","deviceName":"boot-disk","boot":true,"initializeParams":{"diskType":"hyperdisk-balanced","diskSizeGb":50,"sourceImage":"projects/debian-cloud/global/images/family/debian-12-arm64"}},{"type":"PERSISTENT","deviceName":"data-disk","initializeParams":{"diskType":"hyperdisk-balanced","diskSizeGb":128}}]}}}'
    

Alternatively, if you use the `--flags-file` flag, you can specify the same instance flexibility policy in a YAML file:
    
    
    --instance-flexibility-policy:
      instanceSelections:
        selection-1:
          machineTypes:
            - n2-standard-8
            - c2-standard-8
          minCpuPlatform: Intel Cascade Lake
          disks:
            - type: PERSISTENT
              deviceName: boot-disk
              boot: true
              initializeParams:
                diskType: pd-ssd
                diskSizeGb: 50
                sourceImage: projects/debian-cloud/global/images/family/debian-12
            - type: SCRATCH
              initializeParams:
                diskType: local-ssd
        selection-2:
          machineTypes:
            - c4a-standard-8
          disks:
            - type: PERSISTENT
              deviceName: boot-disk
              boot: true
              initializeParams:
                diskType: hyperdisk-balanced
                diskSizeGb: 50
                sourceImage: projects/debian-cloud/global/images/family/debian-12-arm64
            - type: PERSISTENT
              deviceName: data-disk
              initializeParams:
                diskType: hyperdisk-balanced
                diskSizeGb: 128
    

###  REST 

In the Compute Engine API, make a `POST` request to the [`regionInstances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstances/bulkInsert). In each `instanceSelections` entry of `instanceFlexibilityPolicy`, include the `minCpuPlatform` field to override `instanceProperties.minCpuPlatform`, and include the `disks` field to override or add to `instanceProperties.disks`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "deviceName": "boot-disk",
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "INSTANCE_SELECTION_1": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2"
            ],
            "minCpuPlatform": "MIN_CPU_PLATFORM_1",
            "disks": [
              {
                "type": "PERSISTENT",
                "deviceName": "boot-disk",
                "initializeParams": {
                  "diskType": "pd-ssd",
                  "diskSizeGb": 50,
                  "sourceImage": "projects/IMAGE_PROJECT_1/global/images/IMAGE_1"
                },
                "boot": true
              },
              {
                "type": "SCRATCH",
                "initializeParams": {
                  "diskType": "local-ssd"
                }
              }
            ]
          },
          "INSTANCE_SELECTION_2": {
            "machineTypes": [
              "MACHINE_TYPE_3"
            ],
            "minCpuPlatform": "MIN_CPU_PLATFORM_2",
            "disks": [
              {
                "type": "PERSISTENT",
                "deviceName": "boot-disk",
                "initializeParams": {
                  "diskType": "hyperdisk-balanced",
                  "diskSizeGb": 50,
                  "sourceImage": "projects/IMAGE_PROJECT_2/global/images/IMAGE_2"
                },
                "boot": true
              },
              {
                "type": "PERSISTENT",
                "deviceName": "data-disk",
                "initializeParams": {
                  "diskType": "hyperdisk-balanced",
                  "diskSizeGb": 128,
                  "sourceImage": "projects/IMAGE_PROJECT_3/global/images/IMAGE_3"
                }
              }
            ]
          }
        }
      }
    }
    

Replace the following:

  * `COUNT`: the number of VMs to create
  * `NAME_PATTERN`: the [naming pattern](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk#name-pattern) for the VMs
  * `INSTANCE_SELECTION_1`: the name for the first instance selection
  * `INSTANCE_SELECTION_2`: the name for the second instance selection
  * `MACHINE_TYPE_1`, `MACHINE_TYPE_2`: the machine types for the first instance selection
  * `MACHINE_TYPE_3`: the machine type for the second instance selection
  * `MIN_CPU_PLATFORM_1`, `MIN_CPU_PLATFORM_2`: optional [minimum CPU platforms](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) for the VMs in each instance selection
  * `IMAGE_PROJECT`: the project that contains the default boot image in `instanceProperties`
  * `IMAGE`: the name of the default boot image or image family in `instanceProperties`
  * `IMAGE_PROJECT_1`, `IMAGE_PROJECT_2`, `IMAGE_PROJECT_3`: the projects that contain the images for the disk overrides
  * `IMAGE_1`, `IMAGE_2`, `IMAGE_3`: the names of the images for the disk overrides
  * `PROJECT_ID`: your project ID
  * `REGION`: the region in which to create the VMs



**Example**

The following example creates 10 VMs using two instance selections that specify a minimum CPU platform, override the default boot disk, and attach additional disks:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/instances/bulkInsert
    {
      "count": 10,
      "namePattern": "test-bulk-#",
      "instanceProperties": {
        "disks": [
          {
            "boot": true,
            "deviceName": "boot-disk",
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/family/debian-12"
            }
          }
        ],
        "networkInterfaces": [{}]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "selection-1": {
            "machineTypes": [
              "n2-standard-8",
              "c2-standard-8"
            ],
            "minCpuPlatform": "Intel Cascade Lake",
            "disks": [
              {
                "type": "PERSISTENT",
                "deviceName": "boot-disk",
                "initializeParams": {
                  "diskType": "pd-ssd",
                  "diskSizeGb": 50,
                  "sourceImage": "projects/debian-cloud/global/images/family/debian-12"
                },
                "boot": true
              },
              {
                "type": "SCRATCH",
                "initializeParams": {
                  "diskType": "local-ssd"
                }
              }
            ]
          },
          "selection-2": {
            "machineTypes": [
              "c4a-standard-8"
            ],
            "disks": [
              {
                "type": "PERSISTENT",
                "deviceName": "boot-disk",
                "initializeParams": {
                  "diskType": "hyperdisk-balanced",
                  "diskSizeGb": 50,
                  "sourceImage": "projects/debian-cloud/global/images/family/debian-12-arm64"
                },
                "boot": true
              },
              {
                "type": "PERSISTENT",
                "deviceName": "data-disk",
                "initializeParams": {
                  "diskType": "hyperdisk-balanced",
                  "diskSizeGb": 128
                }
              }
            ]
          }
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
