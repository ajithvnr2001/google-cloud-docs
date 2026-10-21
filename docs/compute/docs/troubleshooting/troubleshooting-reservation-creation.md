---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation/
title: Troubleshooting reservation creation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:24.241121+00:00
---

# Troubleshooting reservation creation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting reservation creation Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve issues with creating reservations. To learn more about reservations, see [About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

In addition to the errors on this page, reservation creation can also fail due to issues that happen when creating Compute Engine resources. If your issue is not listed on this page, then do the following:

  1. [Create virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) with the resources that you want to reserve.

  2. If you still encounter errors, then see [Troubleshooting VM creation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation).




## Reservation creation errors

If you can't create a reservation, then it might be due to one of the errors in this section. If you can't create a shared reservation, then also review Shared reservation creation errors in this document.

### Insufficient quota

A quota error occurs when a resource request exceeds your quota.

**Error messages:**
    
    
    RESOURCE_NAME creation failed:
    Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in region REGION
    
    
    
    RESOURCE_NAME creation failed:
    Quota QUOTA_NAME exceeded. Limit: QUOTA_LIMIT in zone ZONE
    
    
    
    Resource exhausted (HTTP 429): QUOTA_EXCEEDED
    

**Resolution:** Request a higher quota limit. For more information, see [Edit your quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota).

### Resource availability

To create a reservation, all the resources you specify in the reservation must be available in the specified in order for them to be reserved for you.

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

### Resource name

If you receive a `resource already exists` error when you try to create a resource, your creation request failed because you specified a non-unique name for the resource for the specified location and project.

**Error messages** : 
    
    
    The resource 'projects/PROJECT_NAME/zones/ZONE/RESOURCE_TYPE/RESOURCE_NAME' already exists"
    
    
    
    The resource 'projects/PROJECT_NAME/regions/REGION/RESOURCE_TYPE/RESOURCE_NAME' already exists"
    

**Resolution** : Retry your creation request with a [unique resource name](https://docs.cloud.google.com/compute/docs/naming-resources#name_uniqueness).

### Maximum VM count exceeded

The following error occurs when you try to reserve more VMs than are allowed in a reservation.

**Error message** : 
    
    
    Invalid value for field 'resource.specificReservation.count': VM_COUNT. Must be less than or equal to 1000
    

Where VM_COUNT is the number of VMs in a reservation. 

**Resolution** : Create multiple reservations that specify the same zone, project, and VM properties. However, ensure that each reservation doesn't reserve more than the following number of VMs:

  * If you specify a compact placement policy with a maximum distance value of `2` in the reservation, then you can reserve up to the [supported number of VMs](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

  * Otherwise, up to 1,000 VMs.




### Reservation capacity limit exceeded

The following error occurs when you try to create an on-demand reservation, but the zone lacks available reservation capacity for your requested machine family.

**Error messages** :
    
    
    RESERVATION_CAPACITY_LIMIT_EXCEEDED
    
    
    
    Failed to reserve additional capacity for 'MACHINE_FAMILY' because reservation capacity limit exceeded in 'ZONE'. Select a different machine family or zone.
    

**Resolution** : If you try to create an automatically consumed reservation and consume existing, running VMs, then Compute Engine rejects the request when the zone lacks reservation capacity. This rejection prevents Compute Engine from charging you twice for the running VMs and an unused reservation. To resolve this error, try one or more of the following options:

  * **Use a different zone**. Create a reservation in a zone that has available capacity for your requested machine family.

  * **Use a different machine family**. Create a reservation that specifies a machine type from a different machine family.

  * **Reduce the VM count**. Request fewer VMs in the reservation.

  * **Retry later**. Submit the creation request again at a later time.


**Note:** If you have running VMs in the zone, then this error doesn't affect them. The VMs continue to run.

## Shared reservation creation errors

If you can't create a shared reservation, then it might be due to one of the errors in this section or in Reservation creation errors.

### Project without an organization

The following error occurs when you try to create a shared reservation in a project that does not belong to an organization.

**Error message** : 
    
    
    Cannot create Shared Reservations in a project that does not belong to an organization.
    

**Resolution** : Do one of the following:

  * [Migrate this project to an organization](https://docs.cloud.google.com/resource-manager/docs/project-migration#migrating_projects_no_org) before using it to create a shared reservation.
  * Create a shared reservation using a project that belongs to an [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).



### Constraint violation

The following error occurs when the [**Shared Reservations Owner Projects** (`compute.sharedReservationsOwnerProjects`) organization policy constraint](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation) doesn't allow a project to create and modify shared reservations.

**Error message** : 
    
    
    Constraint constraints/compute.sharedReservationsOwnerProjects violated for project projects/PROJECT_NUMBER
    Shared reservation can not be created in this project for your organization.
    

**Resolution** : Do one of the following:

  * Use a project that is allowed to create and modify shared reservations. To see which projects in your organization have this permission, [view the shared reservations organization policy constraint](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation#view-policy).
  * Grant the project permission to create and modify shared reservations by [editing the shared reservations organization policy constraint](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation#edit-policy). If you continue to see this error after editing, then you might just need to wait a few minutes for the edit to take effect.



### Invalid consumer projects

This section describes errors that occur when you specify invalid consumer projects for a shared reservation.

#### Project not found in this organization

The following error occurs when the consumer project you specified can't be found in the same organization as the project you're using.

**Error message** : 
    
    
    Project PROJECT_ID doesn't exist or doesn't belong to the same organization of the current project.
    

Where PROJECT_ID is a project ID that you specified as a consumer project.

**Resolution** : Do the following:

  1. [View all the projects in the organization](https://docs.cloud.google.com/resource-manager/docs/organization-resource-management#viewing_all_projects_in_an_organization) to verify that the specified consumer project exists in this organization.
  2. [View the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) to verify that you specified its project ID, PROJECT_ID, correctly.



#### Owner project specified as a consumer project

The following error occurs when you try to specify a shared reservation's owner project (the project used to create the shared reservation) as a consumer project.

**Error message** : 
    
    
    Project PROJECT_ID which is the owner project of this reservation is always included in the share projects, please do not add it.
    

**Resolution** : Remove the owner project from the list of consumer projects. A shared reservation can always be consumed by VMs in the owner project, so you cannot include it in the list of consumer projects.

#### Zero consumer projects

The following error occurs when a shared reservation has zero consumer projects:

**Error message** : 
    
    
    Have to share with at least 1 project.
    

**Resolution** : Do one of the following:

  * Specify at least one consumer project to share this reservation with. For more information, see [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation).
  * Use a [single-project reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) instead of a shared reservation.



#### Maximum consumer projects exceeded

The following error occurs when a shared reservation has more than 100 consumer projects:

**Error message** : 
    
    
    Can only share with at most 100 projects.
    

**Resolution** : Do the following:

  1. Reduce the number of consumer projects to, at most, 100 consumer projects for the shared reservation.
  2. If you still need to reserve capacity for any omitted projects, then [create another shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation) that is shared with those projects.



### Maximum shared reservation count exceeded

The following error occurs when your organization already has 100 shared reservations with the same VM properties.

**Error message** : 
    
    
    Cannot support more than 100 shared reservations of the same shape under an organization.
    

**Resolution** : Follow the [best practice](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations) of minimizing the number of separate shared reservations with the same [VM properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) in your organization by doing the following:

  * [Resize existing reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#resizing_a_reservation) to have larger VM counts. If you have multiple identical shared reservations that don't exceed the maximum VM count, then consider if you can combine them into fewer shared reservations with the same combined VM count.

  * [Modify the consumer projects for a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modifying-consumer-projects-shared-reservation) to include more projects. For example, if you have multiple shared reservations with the same VM properties and zone but similar owner and consumer projects, consider if you can combine them into one shared reservation that can be consumed by all of these projects.

  * [Delete shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation) that you no longer need.




## Reservations from instance templates creation errors

If you fail to create a reservation by [specifying an instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template), then it might be due to one of the errors in this section.

### Cross project referencing is not allowed

The following error occurs when you try to create a reservation by specifying an instance template from another project.

**Error message** :
    
    
    Cross project referencing is not allowed for this resource.
    

**Resolution** : Do the following:

  1. Make sure that the project ID and instance template's name you specify in your reservation are correct. To check that an instance template exists, [get information about the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or [list the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#list_instance_templates).

  2. An instance template contains project-specific settings, so you can only access and use an instance template within the same project. Instead, do one of the following:

     * To create a reservation by specifying an instance template:

       1. [Create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template) within your project.

       2. Specify the newly created instance template when creating a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-instance-template).

**Caution:** Create your reservation in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ get information about the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

     * To create a reservation without specifying an instance template, create a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-vm-properties) by specifying VM properties directly.




### Instance template not found

The following error occurs when you try to create a reservation by specifying an instance template that doesn't exist.

**Error message** :
    
    
    Source resource reference provided invalid.
    

**Resolution** : Check if the name of the instance template you specified is correct. Then— _after_ you [list instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#list_instance_templates) to check that your template doesn't exist and _only if_ your project doesn't have another template that you want to use—you can [create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

### Invalid Local SSD disk size

The following error occurs when you try to create a reservation by specifying an instance template that includes one or more Local SSD disks, but the template doesn't specify the Local SSD disks' size.

**Error message** :
    
    
    Disk LOCAL_SSD_NAME provided in the instance template has invalid size: 0 GB.
    

**Resolution** : You can't update instance templates. Instead, do the following:

  1. Create a new instance template and make sure to specify the [disk size](https://docs.cloud.google.com/compute/docs/disks#localssds) of any Local SSD disks that you include in the template.

  2. Use the newly created instance template to create a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-instance-template).

**Caution:** Create your reservation in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing disk in the `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ describe the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).




### Invalid zone for an instance template

The following error occurs when you try to create a reservation by specifying an instance template, and you specify an invalid location for your instance template.

**Error message** :
    
    
    Reservation cannot be created outside the zone/region of source resource.
    

**Resolution** : Do one of the following:

  * Make sure to create your reservation in the same region and zone as the resources within the instance template. Any [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in the `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [get information about the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  * Use an instance template that doesn't restrict to a specific region or zone. Because you can't update instance templates, do the following:

    1. [Create a new instance template based on an existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template) with the updated properties.

    2. Create a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-instance-template) by specifying the newly created instance template.

**Caution:** Create your reservation in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing disk in the `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ describe the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

    3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).




### Override instance template properties

The following error occurs when you try to create a reservation by specifying an instance template, and you specify both an instance template and VM properties when creating the reservation.

**Error message** :
    
    
    Reservation cannot override properties populated by source resource.
    

**Resolution** : Do one of the following:

  * To create a reservation by specifying an instance template, make sure to remove _any_ field that specifies VM properties.

  * To create a reservation by specifying an instance template with different VM properties, do the following:

    1. You can't update an existing instance template. Instead, [create a new instance template based on an existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template).

    2. Specify the newly created instance template when creating a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-instance-template).

**Caution:** Create your reservation in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing disk in the `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ describe the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

    3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

  * To create a reservation without specifying an instance template, create instead a [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-vm-properties) by specifying VM properties directly.




## Reservations with compact placement policies creation errors

If you fail to create a reservation by specifying a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies), it might be due to one of the errors in this section.

### Attempt to create an automatically consumed reservation

The following error occurs when you try to create an automatically consumed reservation and specify a compact placement policy.
    
    
    Placement policy only supports specific reservations.
    

**Resolution** : You can only specify compact placement policies when creating [specifically targeted reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

### Attempt to create a shared reservation

The following error occurs when you try to create a shared reservation by specifying a compact placement policy.

**Error message** :
    
    
    Creating shared reservations with placement policy is not supported.
    

**Resolution** : You can specify a compact placement policy only for [single-project reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project). Thus, create a new reservation _and_ a new compact placement policy for each project you wanted to initially share your shared reservation with.

### Attempt to specify a policy with a `max-distance` value of `1`

The following error occurs when you try to specify a compact placement policy with a `max-distance` value of `1` in a single-project reservation.

**Error message** :
    
    
    Resource policies with max-distance less than 2 are not supported.
    

**Resolution** : You can't specify compact placement policies with a `max-distance` value of `1` when creating a single-project reservation. Instead, do the following:

  1. [Create a new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) that doesn't specify a `max-distance` value of `1`.

  2. Do one of the following:

     * Create a single-project reservation by specifying an instance template by doing the following:

       1. You can't modify the properties of an existing instance template. Instead, [create a new instance template](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-instance-template) that specifies the newly created compact placement policy.

       2. [Create a reservation by specifying the newly created instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).

       3. Optional: [Delete the old instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

     * [Create a single-project reservation by specifying properties directly](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties) and specify the newly created compact placement policy.




Additionally, if you no longer need the old compact placement policy, see how to [delete the placement policy](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#delete-policy).

### Attempt to specify a spread placement policy

The following error occurs when you try to specify a spread placement policy in a reservation.

**Error message** :
    
    
    Failed to create reservation with policy
    SPREAD_PLACEMENT_POLICY_NAME. Reservations do not support
    spread placement policies.
    

**Resolution** : When creating a reservation, you can only specify a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies). Spread placement policies aren't supported.

### Invalid type of resource policy

The following error occurs when you try to create a reservation by specifying another type of resource policy.

**Error message** :
    
    
    Reservation can only be supported by placement policy.
    

**Resolution** : When creating a reservation, you can only specify a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies). Other types of resource policies, such as instance schedules or snapshots schedules, aren't supported.

### Invalid zone for the policy

The following error occurs when you try to specify a compact placement policy in a reservation, and you specify a zone which isn't within the region of the specified compact placement policy.

**Error message** :
    
    
    ZONE does not match placement policy region.
    

Where `ZONE` is the zone where you tried to reserve VMs.

**Resolution** : Try one of the following:

  * Make sure that your zone is within the same region of the compact placement policy you specify in a reservation or a reservation's instance template.

  * You can't update compact placement policies. Instead, do the following:

    1. [Create a new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) with the updated properties.

    2. Select one of the following methods:

       * Create a new reservation by specifying properties directly, and specify the newly created compact placement policy.

       * Do the following:

         1. You can't update instance templates. Instead, create a new instance template by [specifying the newly created compact placement policy](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

**Important:** Placement policies are [regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources). If you specify a placement policy when creating an instance template, then the policy restricts the use of the template to the region where it exists. For example, if you create a compact placement policy in `us-central1`, you can only use the template to create VMs or reservations within the same region.
         2. Create a new reservation by specifying the newly created instance template.

         3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

    3. Optional: [Delete the older compact placement policy](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#delete-policy).




### Maximum VM count exceeded

The following error occurs when you try to reserve more VMs than the supported limit for a compact placement policy with a maximum distance value of `2`.

**Error message** :
    
    
    No more than SUPPORTED_NUMBER_OF_VMS instances of machine type can be created with this policy.
    

**Resolution** : To reserve more than the [maximum number of supported VMs](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for a compact placement policy with a maximum distance value of `2`, do one of the following:

  * Create multiple reservations with matching zone, project, and properties. Since you can't share compact placement policies across reservations, you must specify a separate policy with a maximum distance value of `2` for each reservation.

  * Specify a compact placement policy with a maximum distance value of `3` (recommended) or without a maximum distance value.




### Override compact placement policy

The following error occurs when you try to create a reservation by specifying an instance template that includes a compact placement policy, and you also specify a compact placement policy directly.

**Error message** :
    
    
    Setting resource policy in both reservation and instance template is not allowed.
    

**Resolution** : When you create a reservation, you can specify a compact placement policy either directly or by using an instance template.

To create a reservation by specifying an instance template and a different policy from the one specified in the template, do the following:

  1. If you haven't already, then [create a new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy).

  2. Because you can't update instance templates, [create a new template that specifies the new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-instance-template).

  3. [Create a reservation by specifying the new instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).

  4. Optional: [Delete the old instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

  5. Optional: [Delete the old compact placement policy](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#delete-policy).




### The policy is already specified in another reservation

The following error occurs when you try to create a reservation by specifying a compact placement policy, and the compact placement policy is already specified in another reservation.

**Error message** :
    
    
    Placement policy has been used by another reservation.
    

**Resolution** : You can use _one_ compact placement policy only per reservation. You can't share compact placement policies across reservations. If you want to use a similar compact placement policy for another reservation, select one of the following methods:

  * To create a reservation by specifying an instance template that includes a compact placement policy, follow these steps:

    1. [Create a new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy).

    2. Create a new instance template by [specifying the newly created compact placement policy](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

**Important:** Placement policies are [regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources). If you specify a placement policy when creating an instance template, then the policy restricts the use of the template to the region where the policy exists. For example, if you create a compact placement policy in `us-central1`, you can only use the template to create VMs or reservations within the same region.
    3. Create a reservation by [specifying the newly created instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).

    4. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

  * To create a reservation by specifying VM properties and a compact placement policy directly, follow these steps:

    1. [Create a new compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy).

    2. Create a reservation by [specifying the new compact placement policy directly](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties).




### Unsupported machine type

The following error occurs when you try to create a reservation by specifying an invalid machine type for compact placement policies.

**Error message** :
    
    
    Placement policy with reservation is not applicable to machine type MACHINE_TYPE.
    

Where `MACHINE_TYPE` is the machine type you tried to specify when creating a reservation.

**Resolution** : When creating a reservation that specifies a compact placement policy, make sure to specify a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
