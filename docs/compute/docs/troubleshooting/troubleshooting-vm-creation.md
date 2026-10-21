---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation/
title: Troubleshoot creating, updating and deleting VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:05:24.464709+00:00
---

# Troubleshoot creating, updating and deleting VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot creating, updating and deleting VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document lists errors that you might encounter when creating or updating VMs. 

## Errors when creating VMs

If you can't create a VM instance, it might be due to one of the issues that's described in this section.

### Insufficient quota

A quota error occurs when a resource request exceeds your quota.

**Error messages:**
    
    
    RESOURCE_NAME creation failed:
    Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in region REGION
    
    
    
    RESOURCE_NAME creation failed:
    Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in zone ZONE
    
    
    
    Resource exhausted (HTTP 429): QUOTA_EXCEEDED
    

**Resolution:** Request a higher quota limit. For more information, see [Edit your quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota).

### Simultaneous resource mutation or creation operations

If you update more than one resource at a time, for example, modifying secondary ranges in a subnetwork and creating a VM at the same time, you might see a `not ready` error.

**Error message** : 
    
    
    The resource 'projects/PROJECT/regions/REGION/subnetworks/default' is not ready
    

**Resolution** : To resolve this issue, try the following:

  * [Wait for operations to be done](https://docs.cloud.google.com/compute/docs/api/best-practices#wait-for-operations) before creating new requests.
  * [Retry operations with exponential backoff](https://docs.cloud.google.com/compute/docs/api/best-practices#retry-with-exponential-backoff).
  * [Poll operations](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#polling_operations) to check their completion status.



### Resource availability

The following are examples of common resource errors that you might encounter when you request new Compute Engine resources or create new reservations:
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    
    
    
    The zone 'projects/PROJECT_ID/zones/ZONE' does not have enough resources available to fulfill the request.
    Try a different zone, or try again later.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone.
    
    Capacity changes frequently, so try your request in a different zone, with a different VM hardware
    configuration, or at a later time. For more options, see troubleshooting documentation.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone, because of  REASON.
    
    Consider trying your request in the ZONE zone(s), which currently has capacity to accommodate your request.
    
    If you cannot move your VM to ZONE, review the REASON failure resolution instructions available in troubleshooting documentation, then try your request again.
    If your workload can't accommodate the suggested resolution, try your request with a different VM hardware configuration or at a later time.
    

To learn how to resolve resource errors, see [Troubleshooting resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability).

### Zone availability

If you receive a `notFound` or `does not exist in zone` error when requesting new resources, it means that the zone you are requesting the resource in does not offer the resource or machine type that you have requested.

**Error messages** : 
    
    
    notFound
    
    
    
    does not exist in zone
    

**Resolution** : See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) to find out which features are available in each zone.

### Rate exceeded for resource type

The following error occurs when you create more than one disk or VM from a snapshot in a ten minute period.

**Error message** :
    
    
    "code": "RESOURCE_OPERATION_RATE_EXCEEDED",
    "message": "Operation rate exceeded for resource 'projects/project-id/zones/zone-id/disks/disk-name'.
    Too frequent operations from the source resource."
    

**Resolution** :

To resolve this issue, do one of the following:

  * **Create VMs in bulk**.

For instructions, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk) and use the following flag or parameter to create VMs from a snapshot:

    * If using gcloud CLI, use the [`--source-snapshot` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create#--source-snapshot).

    * If using REST, use the [`instanceProperties.disks[].initializeParams.sourceSnapshot` parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert#body.request_body.FIELDS.inlinedField_69).

  * **Use images to create disks**. 

To create multiple disks from a snapshot, use the snapshot to create an image then create your disks from the image:

    1. [Create an image from the snapshot](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image).
    2. [Create disks from the image](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks).

For non-boot disks, follow the instructions to [create persistent disks from the image](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) and use the following steps:

    * In the Google Cloud console, select **Image** as the disk **Source type**.
    * With the gcloud CLI, use the [`image` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create#--image).
    * If using REST, use the [`sourceImage` parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert#body.request_body.FIELDS.source_image).

For more information about backing up and replicating your persistent disk data, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).




### Insufficient permissions

If you receive a `permission` error when you try to create a VM, you don't have the necessary IAM permissions to create a VM.

**Error message** : 
    
    
    Error: googleapi: Error 403: Google Compute Engine: Required 'compute.regions.get' permission for 'projects/PROJECT_ID/regions/REGION'., forbidden
    

**Resolution** : Ask your organization administrator to grant you access to create VMs. For more information, see [Granting access to Compute Engine resources](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources#bind-member).

### Resource names

If you receive a `resource already exists` error when you try to create a resource, your creation request failed because you specified a non-unique name for the resource for the specified location and project.

**Error messages** : 
    
    
    The resource 'projects/PROJECT_NAME/zones/ZONE/RESOURCE_TYPE/RESOURCE_NAME' already exists"
    
    
    
    The resource 'projects/PROJECT_NAME/regions/REGION/RESOURCE_TYPE/RESOURCE_NAME' already exists"
    

**Resolution** : Retry your creation request with a [unique resource name](https://docs.cloud.google.com/compute/docs/naming-resources#name_uniqueness).

### Network interfaces

The following are examples of network interface errors that you might encounter while creating an instance.

#### Too many network interfaces

If you receive a `Too many network interfaces` error when creating a VM, your request exceeded the network interface limit for the VM's machine type.

**Error messages** :
    
    
    Invalid value for field 'resource': ".
    
    Too many network interfaces. The maximum number of network interfaces allowed for this machine type is NUMBER.
    
    
    
    Invalid value for field 'resource.networkInterfaces': ".
    
    Too many network interfaces. The maximum number of network interfaces allowed for this machine type is NUMBER.
    

**Resolution** : To learn about how the maximum number of network interfaces is calculated for different machine types, see [Maximum number of network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces).

#### Invalid network interface card (NIC) configuration

If you receive an error about network interface cards (NICs) when creating an A3 Ultra or A4 instance, which have unique [NIC arrangements](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#review_network_bandwidth_and_nic_arrangement), then your request had an invalid networking configuration.

**Error message** : 
    
    
    On MACHINE_SERIES, the first NIC and the second NIC (if present) must be of type GVNIC. These must be followed by 0 or 8 MRDMA NICs.
    

**Resolution** : To learn how to configure the VPC networks and network interfaces for A3 Ultra or A4 instances, see [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4).

### Constraint violated

If you receive a `Constraint violated` error when creating a VM, your request violated one or more [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

**Error message** :

For example, if your organization restricts Shared VPC subnetworks, you might get the following error:
    
    
    Constraint constraints/compute.CONSTRAINT violated for projects/PROJECT_ID.
    Using the PARAMETER projects/PROJECT_ID/regions/REGION/CONSTRAINTPROJECT_ID is not allowed.
    

**Resolution** : Contact your organization administrator.

### Required CPU platform

If you receive a `required CPU platform` error, the CPU platform you specified in the creation request isn't supported by the specified machine type.

**Error message** :
    
    
    Could not fetch resource:
    - The selected machine type (MACHINE_TYPE) has a required CPU
      platform of REQUIRED_CPU_PLATFORM. The minimum CPU platform must
      match this, but was SPECIFIED_CPU_PLATFORM.
    

**Resolution** :

  1. To learn about which CPU platform your machine type supports, review [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  2. Retry your request with a supported CPU platform.



### Mismatched reservation properties

If you receive a `No available resources in specified reservations` error when creating a VM, the properties of the VM and the [specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) that the VM is targeting for consumption aren't matching.

**Error message** :
    
    
    Invalid value for field 'resource.reservationAffinity':
    - No available resources in specified reservations [RESERVATION_NAME].
    

**Resolution** : Try one of the following:

  * If the VM doesn't match the reservation's properties, modify the VM until its properties match the reservation's properties. Then, try creating the VM again.

  * If the VM has the right properties, but doesn't match the reservation's properties, you can't change the reservation. Instead, do one of the following:

    * When creating the VM, target a different specific reservation.

You can create a new specific reservation with matching properties if you don't already have one with the correct properties. If you no longer need the previous specific reservation, then you can [delete it](https://docs.cloud.google.com/compute/docs/instances/reservations-delete) so you are no longer paying for those reserved resources.

    * When creating the VM, target any matching reservation.

If there is a reservation configured for automatic consumption that has properties that match the VM, then the new VM consumes that reservation. Otherwise, the VM is still created, but without consuming any of your reserved resources.

For more information, see [Test that VM properties match a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#test-properties-match).




### Service account access denied

The following error might appear in Cloud Audit Logs when you create VMs using a service account:

**Error message** :
    
    
    SERVICE_ACCOUNT_ACCESS_DENIED
    

**Resolution** : This error appears when the service account that is used to create a VM doesn't have the Identity and Access Management role to access the new VM's service account.

Grant the [`roles/iam.serviceAccountUser` role](https://docs.cloud.google.com/compute/docs/access/iam#the_serviceaccountuser_role) to the service account that is creating the VM. You can either grant this role at the [project-level](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#impersonate-parent-level), which would give the service account that is creating VMs access to all service accounts created in the project, or you can grant this role [only on the service account for the new VM](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#iam-service-accounts-grant-role-sa-console).

### Missing required permissions

The following error might occur when you try to create a VM from existing VM
    
    
    Required 'compute.images.useReadOnly' permission for 'projects/PROJECT_ID/global/images/IMAGE_NAME
    

This error can occur for several reasons. The following is a common cause of this error:

  * You tried to [create a new VM from an existing VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) but you don't have read-access to the existing VM's boot disk image.

To resolve this issue, contact the owner of the boot disk, and ask them to [share the existing VM's image with you](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#share-images-between-organization).




### Free Trial

If you try to create a Windows VM during a [Free Trial of Google Cloud](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial), then you receive an error.

**Error message** :
    
    
    Windows VM instances are not included with free trial. To use them,
    first enable billing on your account.
    

**Resolution** : Windows Server images aren't included in the Free Trial. [Upgrade to a paid Cloud Billing account](https://docs.cloud.google.com/free/docs/gcp-free-tier#how-to-upgrade).

### VM doesn't start

If a Linux VM that uses a startup script doesn't start after it was created, it might be related to an issue connecting to the metadata server.

This issue can last for up to seven minutes due to a transient network issue that resolves on its own. If the issue does not resolve itself after seven minutes, recreate the VM.

## Errors when updating VMs

If you can't update a VM instance, it might be due to the following issue.

### Error when changing the machine type

The following error might occur when you try to change the machine type of a VM:
    
    
    Invalid value for field 'resource.sourceMachineImage': Updating 'sourceMachineImage' is not supported
    

**Resolution:**

  * Make sure that your VM supports the processor of the new machine type. For more information about the processors supported by different machine types, see [Machine family comparison](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison).

  * Try to [change the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) by using the Google Cloud CLI.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
