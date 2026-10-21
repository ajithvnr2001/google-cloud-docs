---
url: https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies/
title: Create and apply spread placement policies to VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:46:27.035119+00:00
---

# Create and apply spread placement policies to VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and apply spread placement policies to VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to improve the reliability of your virtual machine (VM) instances by creating and applying spread placement policies to them. To learn more about placement policies, including their restrictions and pricing, see [Placement policies overview](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

A spread placement policy specifies that your instances should be distributed across different availability domains. This distribution helps mitigate location-specific disruptions, such as hardware errors, and is useful when running large-scale, distributed, and replicated workloads like Hadoop Distributed File System (HDFS), Cassandra, or Kafka.

## Before you begin

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

To get the permissions that you need to create and apply a spread placement policy to instances, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and apply a spread placement policy to instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and apply a spread placement policy to instances:

  * To create placement policies: `compute.resourcePolicies.create` on the project 
  * To apply a placement policy to existing instances: `compute.instances.addResourcePolicies` on the project 
  * To create instances: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To create a managed instance group (MIG): `compute.instanceGroupManagers.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a spread placement policy

Unless you want to test the application of the spread placement policy to your instances, Google Cloud recommends creating spread placement policies with two or more availability domains. This mitigates the risk of all instances being impacted by a single hardware error. For more information, see [About spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies).

To create a spread placement policy, select one of the following options:

###  gcloud 

To create a spread placement policy, use the [`gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement) with the `--availability-domain-count` flag.
    
    
    gcloud compute resource-policies create group-placement POLICY_NAME \
        --availability-domain-count=DOMAIN_COUNT \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of the spread placement policy.

  * `DOMAIN_COUNT`: the distinct number of availability domains to place your instances in. The value must be between `1` and `8`.

  * `REGION`: the region in which to create the placement policy.




###  REST 

To create a spread placement policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). In the request body, include the `availabilityDomainCount` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
    
    {
      "name": "POLICY_NAME",
      "groupPlacementPolicy": {
        "availabilityDomainCount": DOMAIN_COUNT
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the placement policy.

  * `REGION`: the region in which to create the placement policy.

  * `POLICY_NAME`: the name of the spread placement policy.

  * `DOMAIN_COUNT`: the distinct number of availability domains to place your instances in. The value must be between `1` and `8`.




## Apply a spread placement policy

You can apply a spread placement policy to an existing VM or MIG, or when creating instances, instance templates, or MIGs.

To apply a spread placement policy to a Compute Engine resource, select one of the following methods:

  * Apply the policy to an existing VM.
  * Apply the policy while creating a VM.
  * Apply the policy while creating instances in bulk.
  * Apply the policy while creating an instance template.



After you apply a spread placement policy to a VM, you can verify the availability domain in which the VM is located by [viewing the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) and checking the value of the `availabilityDomain` field.

### Apply the policy to an existing VM

Before applying a spread placement policy to an existing VM, consider the following:

  * If your spread placement policy specifies multiple availability domains, then you can apply the policy to a VM without stopping the VM. However, the VM might need to be relocated to a different availability domain. During this process, Compute Engine stops or live migrates the VM based on its [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

  * The VM and the spread placement policy must be located in the same region. For example, if the placement policy is located in region `us-central1`, then the VM must be located in a zone in `us-central1`. If you need to migrate a VM to another region, then see [Move a VM between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).




If you want to specify the availability domain in which to place your VM, then apply the placement policy to the VM by [updating its properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties). When updating the VM's properties, make sure to include the `resourcePolicies` and `scheduling.availabilityDomain` fields.

To apply a spread placement policy to an existing VM, select one of the following options:

###  gcloud 

To apply a spread placement policy to an existing VM, use the [`gcloud compute instances add-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-resource-policies).
    
    
    gcloud compute instances add-resource-policies VM_NAME \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of an existing VM.

  * `POLICY_NAME`: the name of an existing spread placement policy.

  * `ZONE`: the zone where the VM is located.




###  REST 

To apply a spread placement policy to an existing VM, make a `POST` request to the [`instances.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addResourcePolicies).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/addResourcePolicies
    
    {
      "resourcePolicies": [
        "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the spread placement policy and the VM are located.

  * `ZONE`: the zone where the VM is located.

  * `VM_NAME`: the name of an existing VM.

  * `REGION`: the region where the spread placement policy is located.

  * `POLICY_NAME`: the name of an existing spread placement policy.




### Apply the policy while creating a VM

You can only create a VM that specifies a spread placement policy in the same region as the placement policy.

To create a VM that specifies a spread placement policy, select one of the following options:

###  gcloud 

To create a VM that specifies a spread placement policy, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--resource-policies` flag.
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM to create.

  * `MACHINE_TYPE`: the machine type for the VM.

  * `POLICY_NAME`: the name of an existing spread placement policy.

  * `ZONE`: the zone in which to create the VM.




Optionally, to specify the availability domain in which to create the VM, include the `--availability-domain` flag.
    
    
    gcloud compute instances create VM_NAME \
        **--availability-domain= DOMAIN_NUMBER** \
        --machine-type=MACHINE_TYPE \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to place your VM in. The value must be between `1` and the number of domains specified in the spread placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

###  REST 

To create a VM that specifies a spread placement policy, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `resourcePolicies` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "resourcePolicies": [
        "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the spread placement policy is located.

  * `ZONE`: the zone where to create the VM in and where the machine type is located. You can only specify a zone within region of the spread placement policy.

  * `VM_NAME`: the name of the VM to create.

  * `MACHINE_TYPE`: the machine type for the VM.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `REGION`: the region where the spread placement policy is located.

  * `POLICY_NAME`: the name of an existing spread placement policy.




Optionally, to specify the availability domain in which to create the VM, include the `availabilityDomain` field in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "resourcePolicies": [
        "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ],
      **"scheduling": {
        "availabilityDomain": DOMAIN_NUMBER
      }**
    }
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to place your VM in. The value must be between `1` and the number of domains specified in the spread placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

For more information about the configuration options to create a VM, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Apply the policy while creating instances in bulk

Before creating instances in bulk that specify a spread placement policy, make sure of the following:

  * You can only create instances in bulk that specify a spread placement policy in the same region as the placement policy.

  * When creating instances in bulk with a spread placement policy, you can optionally specify the availability domain in which to create your instances. Avoid creating all your instances in a single domain. Otherwise, you don't mitigate the risk of a single hardware error impacting all your instances.




To create instances in bulk that specify a spread placement policy, select one of the following options:

###  gcloud 

To create instances in bulk that specify a spread placement policy, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--resource-policies` flag.

For example, to create instances in bulk in a single zone and specify a name pattern for the instances, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern=NAME_PATTERN \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of instances to create.

  * `MACHINE_TYPE`: the machine type for the instances.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in a VM name, use a sequence of hash (`#`) characters. For example, using `vm-#` for the name pattern generates instances with names starting with `vm-1`, `vm-2`, and continuing up to the number of instances specified by `COUNT`.

  * `POLICY_NAME`: the name of an existing spread placement policy.

  * `ZONE`: the zone in which to create the instances in bulk.




Optionally, to specify the availability domain in which to create the instances in bulk, include the `--availability-domain` flag.
    
    
    gcloud compute instances bulk create \
        **--availability-domain= DOMAIN_NUMBER** \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern=NAME_PATTERN \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to place your VM in. The value must be between `1` and the number of domains specified in the spread placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

###  REST 

To create instances in bulk that specify a spread placement policy, make a `POST` to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `resourcePolicies` field.

For example, to create instances in bulk in a single zone and specify a name pattern for the instances, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": "COUNT",
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "resourcePolicies": [
          "POLICY_NAME"
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the spread placement policy is located.

  * `ZONE`: the zone in which to create the instances in bulk.

  * `COUNT`: the number of instances to create.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in a VM name, use a sequence of hash (`#`) characters. For example, using `vm-#` for the name pattern generates instances with names starting with `vm-1`, `vm-2`, and continuing up to the number of instances specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type for the instances.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `POLICY_NAME`: the name of an existing spread placement policy.




Optionally, to specify the availability domain in which to create the instances in bulk, include the `availabilityDomain` field in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": "COUNT",
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "resourcePolicies": [
          "POLICY_NAME"
        ],
        **"scheduling": {
          "availabilityDomain": DOMAIN_NUMBER
        }**
      }
    }
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to place your VM in. The value must be between `1` and the number of domains specified in the spread placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

For more information about the configuration options to create instances in bulk, see [Create instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Apply the policy while creating an instance template

Before you create an instance template that specifies a spread placement policy, consider the following:

  * If you want to create a regional instance template, then the template and the spread placement policy must be in the same region. Otherwise, creating the instance template fails.

  * Avoid creating all instances within a single availability domain. Otherwise, you don't mitigate the risk of a single hardware error impacting all your instances.




After you create an instance template that specifies a spread placement policy, you can use the template to do the following:

  * [Apply a spread placement policy to the instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

**Caution:** Avoid using a spread placement policy (or its instance template) for multiple MIGs. A policy's maximum distance value affects the [maximum number of compute instances that the policy supports](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies). If you share a policy among multiple MIGs, then it restricts the number of instances that you can create in the MIGs. Instead, use a new instance template with a new spread placement policy for each MIG. 
  * [Create an instance from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).




To create a regional instance template and a new spread placement policy with eight availability domains, use the Google Cloud console. To create a global or regional instance template, and specify an existing spread placement policy, use the gcloud CLI or REST API:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page appears.

  3. In the **Region** field, specify the region where you want to create the spread placement policy and the instance template.

  4. In the **Machine configuration** section, specify a machine series and type.

  5. In the **Placement policy** section, in the **Placement policy** list, select **Spread**.

  6. Click **Create**.




###  gcloud 

To create an instance template that specifies a spread placement policy, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--resource-policies` flag.

For example, to create a global instance template that specifies a spread placement policy, run the following command:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --resource-policies=POLICY_NAME
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `MACHINE_TYPE`: the machine type for the instances created using the instance template.

  * `POLICY_NAME`: the name of an existing spread placement policy.




Optionally, to specify the availability domain in which to create the instances, include the `--availability-domain` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        **--availability-domain= DOMAIN_NUMBER**  \
        --machine-type=MACHINE_TYPE \
        --resource-policies=POLICY_NAME
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to create your instances in. The value must be between `1` and the number of domains specified in the placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

###  REST 

To create an instance template that specifies a spread placement policy, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




In the request body, specify the `resourcePolicies` field.

For example, to create a global instance template that specifies a spread placement policy, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "resourcePolicies": [
          "POLICY_NAME"
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the spread placement policy is located.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type for the instances created using the instance template.

  * `POLICY_NAME`: the name of an existing spread placement policy.




Optionally, to specify the availability domain in which to create the instances, include the `availabilityDomain` field in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "resourcePolicies": [
          "POLICY_NAME"
        ],
        **"scheduling": {
          "availabilityDomain": DOMAIN_NUMBER
        }**
      }
    }
    

Replace `DOMAIN_NUMBER` with the number of the availability domain to create your instances in. The value must be between `1` and the number of domains specified in the placement policy. To verify the number of domains in a spread placement policy, [view the details of the placement policy](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies#view-details-policy).

For more information about the configuration options to create an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## What's next?

  * Learn how to [view placement policies](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies).

  * Learn how to [replace, remove, or delete placement policies](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies).

  * Learn how to do the following with a VM that specifies a placement policy:

    * [View the status of the VM](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status).

    * [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  * Learn more about the [live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
