---
url: https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies/
title: Reduce latency by using compact placement policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:20.374453+00:00
---

# Reduce latency by using compact placement policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Reduce latency by using compact placement policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can reduce network latency among your Compute Engine instances by creating and applying compact placement policies. To learn more about placement policies, including their supported machine series, restrictions, and pricing, see [Placement policies overview](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

A compact placement policy specifies that Compute Engine physically places your instances closer to each other. This can help improve performance and reduce network latency among your instances when you run high performance computing (HPC), machine learning (ML), or database server workloads.

**Important:** To reduce network latency in MIGs with A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High, or H4D instances, use workload policies instead. Workload policies give you more control over the placement of your compute instances by letting you communicate the specific intent of your workload to the underlying infrastructure. For more information, see [About workload policies in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).

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

To get the permissions that you need to create and apply a compact placement policy to compute instances, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To create a reservation: [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and apply a compact placement policy to compute instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and apply a compact placement policy to compute instances:

  * To create placement policies: `compute.resourcePolicies.create` on the project 
  * To apply a placement policy to existing compute instances: `compute.instances.addResourcePolicies` on the project 
  * To create compute instances: 
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
  * To create a reservation: `compute.reservations.create` on the project 
  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To create a MIG: `compute.instanceGroupManagers.create` on the project 
  * To view the details of a compute instance: `compute.instances.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a compact placement policy

Before you create a compact placement policy, consider the following:

  * If you want to apply a compact placement policy to a compute instance other than M3, M2, M1, N2D, or N2, then do one of the following based on the machine type:

    * For standalone [A4X Max or A4X instances](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms), you must specify to create compute instances in the same [_sub-block_](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#overview) to use an NVLink domain, as described in this section.

    * For other compute instances that support compact placement policies, specify a [maximum distance value](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

  * If you want to apply a compact placement policy to an A3 Mega, A3 High, or A3 Edge instance that was created before October 1, 2025, then contact your account team.




To create a compact placement policy, select one of the following options:

###  gcloud 

  * To apply the compact placement policy to M3, M2, M1, N2D, or N2 instances, create the policy by using the [`gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement) with the `--collocation=collocated` flag.
        
        gcloud compute resource-policies create group-placement POLICY_NAME \
            --collocation=collocated \
            --region=REGION
        

Replace the following:

    * `POLICY_NAME`: the name of the compact placement policy.

    * `REGION`: the region in which to create the placement policy.

  * To apply the compact placement policy to standalone A4X Max or A4X instances, create the policy by using the [`gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement) with the `--collocation=collocated` and `--gpu-topology=1x72` flags.
        
        gcloud compute resource-policies create group-placement POLICY_NAME \
            --collocation=collocated \
            --gpu-topology=1x72 \
            --region=REGION
        

  * To apply the compact placement policy to any other supported compute instances, create the policy by using the [`gcloud beta compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/create/group-placement) with the `--collocation=collocated` and `--max-distance` flags.

**Preview — The`--max-distance` flag **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        gcloud beta compute resource-policies create group-placement POLICY_NAME \
            --collocation=collocated \
            --max-distance=MAX_DISTANCE \
            --region=REGION
        




Replace the following:

  * `POLICY_NAME`: the name of the compact placement policy.

  * `MAX_DISTANCE`: the maximum distance configuration for your compute instances. The value must be between `1`, which specifies to place your compute instances in the same sub-block for the lowest network latency possible, and `3`, which specifies to place your compute instances in the same cluster. If you want to apply the compact placement policy to a reservation, then you can only specify a value of `3` or `2`.

  * `REGION`: the region in which to create the placement policy.




###  REST 

  * To apply the compact placement policy to M3, M2, M1, N2D, or N2 instances, create the policy by making a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). In the request body, include the `collocation` field and set it to `COLLOCATED`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
        {
          "name": "POLICY_NAME",
          "groupPlacementPolicy": {
            "collocation": "COLLOCATED"
          }
        }
        

  * To apply the compact placement policy to standalone A4X Max or A4X instances, create the policy by making a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). In the request body, include the `collocation` field set to `COLLOCATED`, and the `gpuTopology` field set to `1x72`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
        {
          "name": "POLICY_NAME",
          "groupPlacementPolicy": {
            "collocation": "COLLOCATED",
            "gpuTopology": "1x72"
          }
        }
        

  * To apply the compact placement policy to any other supported compute instances, create the policy by making a `POST` request to the [`beta.resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/resourcePolicies/insert). In the request body, include the following:

    * The `collocation` field set to `COLLOCATED`.

    * The `maxDistance` field.

**Preview — The`maxDistance` field **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/resourcePolicies
    
    {
      "name": "POLICY_NAME",
      "groupPlacementPolicy": {
        "collocation": "COLLOCATED",
        "maxDistance": MAX_DISTANCE
      }
    }
    




Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the placement policy.

  * `REGION`: the region in which to create the placement policy.

  * `MAX_DISTANCE`: the maximum distance configuration for your compute instances. The value must be between `1`, which specifies to place your compute instances in the same sub-block for the lowest network latency possible, and `3`, which specifies to place your compute instances in the same cluster. If you want to apply the compact placement policy to a reservation, then you can only specify a value of `3` or `2`.




## Apply a compact placement policy

You can apply a compact placement policy to an existing compute instance or managed instance group (MIG), or when creating compute instances, instance templates, MIGs, or reservations of compute instances.

To apply a compact placement policy to a Compute Engine resource, select one of the following methods:

  * Apply the policy to an existing instance.
  * Apply the policy while creating an instance.
  * Apply the policy while creating instances in bulk.
  * Apply the policy while creating a reservation.
  * Apply the policy while creating an instance template.



After you apply a compact placement policy to an instance, you can [verify the physical location of the instance](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology) in relation to other instances that specify the same placement policy.

### Apply the policy to an existing instance

Before applying a compact placement policy to an existing compute instance, make sure of the following:

  * The compute instance and the compact placement policy must be located in the same region. For example, if the placement policy is located in region `us-central1`, then the compute instance must be located in a zone in `us-central1`. If you need to migrate a compute instance to another region, then see [Move a compute instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).

  * The compute instance must use a supported [machine series](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) and [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies). If you need to make changes to the compute instance, then do one or both of the following:

    * [Change the machine type of the compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).

    * [Update the host maintenance policy of the compute instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#updatingoption).




Otherwise, applying the compact placement policy to the compute instance fails. If the compute instance already specifies a placement policy and you want to replace it, then see instead [Replace a placement policy in a compute instance](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#replace-policy).

To apply a compact placement policy to an existing compute instance, select one of the following options:

###  gcloud 

  1. [Stop the compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To apply a compact placement policy to an existing compute instance, use the [`gcloud compute instances add-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-resource-policies).
         
         gcloud compute instances add-resource-policies INSTANCE_NAME \
             --resource-policies=POLICY_NAME \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of an existing compute instance.

     * `POLICY_NAME`: the name of an existing compact placement policy.

     * `ZONE`: the zone where the compute instance exists.

  3. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).




###  REST 

  1. [Stop the compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To apply a compact placement policy to an existing compute instance, make a `POST` request to the [`instances.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addResourcePolicies).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/addResourcePolicies
         
         {
           "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compact placement policy and the compute instance exist.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of an existing compute instance.

     * `REGION`: the region where the compact placement policy is located.

     * `POLICY_NAME`: the name of an existing compact placement policy.

  3. [Restart the compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).




### Apply the policy while creating an instance

You can only create a compute instance that specifies a compact placement policy in the same region as the placement policy.

To create a compute instance that specifies a compact placement policy, select one of the following options:

###  gcloud 

To create a compute instance that specifies a compact placement policy, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--maintenance-policy` and `--resource-policies` flags.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance to create.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the compute instance. If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `ZONE`: the zone in which to create the compute instance.




###  REST 

To create a compute instance that specifies a compact placement policy, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `onHostMaintenance` and `resourcePolicies` fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
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
      "scheduling": {
        "onHostMaintenance": "MAINTENANCE_POLICY"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compact placement policy is located.

  * `ZONE`: the zone where to create the compute instance in and where the machine type is located. You can only specify a zone in the region of the compact placement policy.

  * `INSTANCE_NAME`: the name of the compute instance to create.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `REGION`: the region where the compact placement policy is located.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the compute instance. If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.




For more information about the configuration options to create a compute instance, see [Create and start a compute instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Apply the policy while creating instances in bulk

You can only create compute instances in bulk with a compact placement policy in the same region as the placement policy.

To create compute instances in bulk that specify a compact placement policy, select one of the following options:

###  gcloud 

To create compute instances in bulk that specify a compact placement policy, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--maintenance-policy` and `--resource-policies` flags.

For example, to create compute instances in bulk in a single zone and specify a name pattern for the compute instances, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --name-pattern=NAME_PATTERN \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of compute instances to create, which can't be higher than the [supported maximum number of compute instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) of the specified compact placement policy.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the compute instance. If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in a compute instance name, use a sequence of hash (`#`) characters. For example, using `vm-#` for the name pattern generates instances with names starting with `vm-1`, `vm-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `ZONE`: the zone in which to create the compute instances in bulk.




###  REST 

To create compute instances in bulk that specify a compact placement policy, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `onHostMaintenance` and `resourcePolicies` fields.

For example, to create compute instances in bulk in a single zone and specify a name pattern for the compute instances, make a `POST` request as follows:
    
    
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
          "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
        ],
        "scheduling": {
          "onHostMaintenance": "MAINTENANCE_POLICY"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compact placement policy is located.

  * `ZONE`: the zone in which to create the compute instances in bulk.

  * `COUNT`: the number of compute instances to create, which can't be higher than the [supported maximum number of instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) of the specified compact placement policy.

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `vm-#` for the name pattern generates compute instances with names starting with `vm-1`, `vm-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `REGION`: the region where the compact placement policy is located.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the instance. If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.




For more information about the configuration options to create compute instances in bulk, see [Create compute instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Apply the policy while creating a reservation

If you want to create an on-demand, single-project reservation that specifies a compact placement policy, then you must create a [specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type). When you create compute instances to consume the reservation, make sure of the following:

  * The compute instances must specify the same compact placement policy applied to the reservation.

  * The compute instances must specifically target the reservation to consume it. For more information, see [Consume compute instances from a specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).




To create a single-project reservation with a compact placement policy, select one of the following methods:

  * Create the reservation by specifying properties directly as described in this section.

  * Apply the policy while creating an instance template as described in this document, and then create a single-project reservation by [specifying the newly created instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).


**Note:** You can apply compact placement policies only to single-project, standalone reservations. Shared reservations or reservations attached to commitments aren't supported. For the full list of requirements, see the [requirements for reservations with compact placement policies](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-reservations-placement-policies).

To create a single-project reservation with a compact placement policy by specifying properties directly, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select the region and zone where you want to reserve resources.

  5. In the **Use with VM instance** section, select **Select specific reservation**.

  6. In the **VM instances and GPUs** section, do the following:

     1. In the **Number of VM instances** field, enter the number of VMs to reserve.

     2. Specify a machine series and type that supports compact placement policies.

  7. In the **Group placement policy** section, click the **Select or create a group placement policy** list, and then do one of the following:

     * To create a compact placement policy, complete the following steps:

**Important:** This method creates a compact placement policy without specifying a maximum distance value. If you need to specify a maximum distance value of `3` or `2`, then first create a compact placement policy separately, and then select the newly created policy.
       1. Click **Create group placement policy**. The **Create a group placement policy** pane appears.

       2. In the **Policy name** field, enter a name for your policy.

       3. Click **Create**.

     * To select an existing compact placement policy, select a policy that exists in the same region where you want to reserve instances.

  8. To create the reservation, click **Create**.




###  gcloud 

To create a single-project reservation with a compact placement policy by specifying properties directly, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--require-specific-reservation` and `--resource-policies=policy` flags.
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --machine-type=MACHINE_TYPE \
        --require-specific-reservation \
        --resource-policies=policy=POLICY_NAME \
        --vm-count=NUMBER_OF_INSTANCES \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `NUMBER_OF_INSTANCES`: the number of compute instances to reserve, which can't be higher than the [supported maximum number of instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) of the specified compact placement policy.

  * `ZONE`: the zone in which to reserve compute instances. You can only reserve compute instances in a zone in the region of the specified compact placement policy.




###  REST 

To create a single-project reservation with a compact placement policy by specifying properties directly, make a `POST` request to the [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert). In the request body, include the `resourcePolicies` field, and the `specificReservationRequired` field set to `true`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
    
    {
      "name": "RESERVATION_NAME",
      "resourcePolicies": {
        "policy" : "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      },
      "specificReservation": {
        "count": "NUMBER_OF_INSTANCES",
        "instanceProperties": {
          "machineType": "MACHINE_TYPE",
        }
      },
      "specificReservationRequired": true
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compact placement policy is located.

  * `ZONE`: the zone in which to reserve compute instances. You can only reserve compute instances in a zone in the region of the specified compact placement policy.

  * `RESERVATION_NAME`: the name of the reservation.

  * `REGION`: the region where the compact placement policy is located.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `NUMBER_OF_INSTANCES`: the number of compute instances to reserve, which can't be higher than the [supported maximum number of compute instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) of the specified compact placement policy.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.




For more information about the configuration options to create single-project reservations, see [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project).

### Apply the policy while creating an instance template

If you want to create a regional instance template, then the template and the compact placement policy must be in the same region. Otherwise, creating the instance template fails.

After you create an instance template that specifies a compact placement policy, you can use the template to do the following:

  * [Apply the policy to compute instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

**Caution:** Avoid using a compact placement policy (or its instance template) for multiple MIGs. A policy's maximum distance value affects the [maximum number of compute instances that the policy supports](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies). If you share a policy among multiple MIGs, then it restricts the number of instances that you can create in the MIGs. Instead, use a new instance template with a new compact placement policy for each MIG. 
  * [Create a compute instance from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).

  * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).




To create an instance template that specifies a compact placement policy, use one of the following methods:

  * To create a regional instance template with a new compact placement policy, use the Google Cloud console. The new policy doesn't specify a maximum distance value, and you can apply it to a maximum of 22 instances.

  * To create a global or regional instance template that specifies an existing compact placement policy, use the gcloud CLI or REST API.




To create the instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page appears.

  3. In the **Region** field, specify the region where you want to create the compact placement policy and the instance template.

  4. In the **Machine configuration** section, specify a supported machine series and type for compact placement policies.

  5. In the **Placement policy** section, in the **Placement policy** list, select **Compact**. When you select this option, the Google Cloud console automatically generates a compact placement policy without a maximum distance value and that supports up to 22 instances.

  6. Click **Create**.




###  gcloud 

To create an instance template that specifies a compact placement policy, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--maintenance-policy` and `--resource-policies` flags.

For example, to create a global instance template that specifies a compact placement policy, run the following command:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --resource-policies=POLICY_NAME
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties). If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.

  * `POLICY_NAME`: the name of an existing compact placement policy.




###  REST 

To create an instance template that specifies a compact placement policy, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




In the request body, include the `onHostMaintenance` and `resourcePolicies` fields.

For example, to create a global instance template that specifies a compact placement policy, make a `POST` request as follows:
    
    
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
        "scheduling": {
          "onHostMaintenance": "MAINTENANCE_POLICY"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compact placement policy is located.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

  * `POLICY_NAME`: the name of an existing compact placement policy.

  * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties). If the compact placement policy you specify uses a maximum distance value of `1` or `2`, or your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`.




For more information about the configuration options to create an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

### Apply the policy to instances in a MIG

After you create an instance template that specifies a compact placement policy, you can use the template to do the following:

  * Apply the policy while creating a MIG.

  * Apply the policy to an existing MIG.


**Caution:** Avoid using a compact placement policy (or its instance template) for multiple MIGs. A policy's maximum distance value affects the [maximum number of compute instances that the policy supports](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies). If you share a placement policy among multiple MIGs, then it restricts the number of compute instances that you can create in the MIGs.

#### Apply the policy while creating a MIG

You can only create compute instances that specify a compact placement policy if the compute instances are located in the same region as the placement policy.

To create a MIG by using an instance template that specifies a compact placement policy, select one of the following options:

###  gcloud 

To create a MIG by using an instance template that specifies a compact placement policy, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

For example, to create a zonal MIG by using a global instance template that specifies a compact placement policy, run the following command:
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --size=SIZE \
        --template=INSTANCE_TEMPLATE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG to create.

  * `SIZE`: the size of the MIG.

  * `INSTANCE_TEMPLATE_NAME`: the name of an existing global instance template that specifies a compact placement policy.

  * `ZONE`: the zone in which to create the MIG, which must be in the region where the compact placement policy is located.




###  REST 

To create a MIG by using an instance template that specifies a compact placement policy, make a `POST` request to one of the following methods:

  * To create a zonal MIG: [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).

  * To create a regional MIG: [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).




For example, to create a zonal MIG by using a global instance template that specifies a compact placement policy, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
    
    {
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": SIZE,
      "versions": [
        {
          "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE_NAME"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compact placement policy and the instance template that specifies the placement policy are located.

  * `ZONE`: the zone in which to create the MIG, which must be in the region where the compact placement policy is located.

  * `INSTANCE_GROUP_NAME`: the name of the MIG to create.

  * `INSTANCE_TEMPLATE_NAME`: the name of an existing global instance template that specifies a compact placement policy.

  * `SIZE`: the size of the MIG.




For more information about the configuration options to create MIGs, see [Basic scenarios for creating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

#### Apply the policy to an existing MIG

You can only apply a compact placement policy to an existing MIG if the MIG is located in the same region as the placement policy or, for zonal MIGs, in a zone in the same region as the placement policy.

To update a MIG to use an instance template that specifies a compact placement policy, select one of the following options:

###  gcloud 

To update a MIG to use an instance template that specifies a compact placement policy, use the [`gcloud compute instance-groups managed rolling-action start-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update).

For example, to update a zonal MIG to use an instance template that specifies a compact placement policy, and replace the existing compute instances from the MIG with new compute instances that specify the template's properties, run the following command:
    
    
    gcloud compute instance-groups managed rolling-action start-update MIG_NAME \
        --version=template=INSTANCE_TEMPLATE_NAME \
        --zone=ZONE
    

Replace the following:

  * `MIG_NAME`: the name of an existing MIG.

  * `INSTANCE_TEMPLATE_NAME`: the name of an existing global instance template that specifies a compact placement policy.

  * `ZONE`: the zone where the MIG is located. You can only apply the compact placement policy to a MIG located in the same region as the placement policy.




###  REST 

To update a MIG to use an instance template that specifies a compact placement policy, and automatically apply the properties of the template and the placement policy to existing compute instances in the MIG, make a `PATCH` request to one of the following methods:

  * To update a zonal MIG: [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).

  * To update a regional MIG: [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).




For example, to update a zonal MIG to use a global instance template that specifies a compact placement policy, and replace the existing compute instances from the MIG with new compute instances that specify the template's properties, make the following `PATCH` request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
      "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE_NAME"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the MIG, the compact placement policy, and the instance template that specifies the placement policy are located.

  * `ZONE`: the zone where the MIG is located. You can only apply the compact placement policy to a MIG located in the same region as the placement policy.

  * `MIG_NAME`: the name of an existing MIG.

  * `INSTANCE_TEMPLATE_NAME`: the name of an existing global instance template that specifies a compact placement policy.




For more information about the configuration options to update the compute instances in a MIG, see [Update and apply new configurations to instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

## What's next?

  * Learn how to [view compute instance topology](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).

  * Learn how to [view placement policies](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies).

  * Learn how to [replace, remove, or delete placement policies](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies).

  * Learn how to do the following with a compute instance that specifies a placement policy:

    * [View the status of the compute instance](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status).

    * [Connect to the compute instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
