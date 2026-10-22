---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations/
title: Troubleshoot future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:38.450605+00:00
---

# Troubleshoot future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve issues when creating or modifying [future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) for Compute Engine zonal resources.

## General future reservation requests errors

This section describes the errors that might prevent you from creating or modifying a future reservation request.

### Can't access and see future reservations

If you can't access and use future reservations in the gcloud CLI or Compute Engine API, then you might not be eligible to access and use future reservations at this time. In that case, contact your [Technical Account Manager](https://cloud.google.com/tam) or the [Sales Team](https://cloud.google.com/contact).

### Exceeded maximum number of consumer projects

The following error occurs when you specify more than 100 consumer projects for a shared future reservation request.

**Error message** :
    
    
    Can only share with at most 100 projects.
    

**Resolution** : You can specify up to 100 consumer projects for a shared future reservation request. If you want to specify more, then create multiple shared future reservation requests. For more information, see the [best practices for shared reservations](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations).

### Invalid deletion time for the auto-created reservations

The following error occurs when you specify an invalid deletion time for the auto-created reservations for a future reservation request.

**Error message** :
    
    
    Auto-created reservations cannot be deleted before future reservation end time.
    

**Resolution** : You can only delete an auto-created reservation for a future reservation after the end time of the reservation period. To view the date and time when you can delete an auto-created reservation, [view the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations) and look for the value of the `deleteAtTime` field.

### Invalid end time

The following error occurs when you specify an invalid duration for the reservation period of a future reservation request.

**Error message** :
    
    
    Future reservation end time must be at least 24 hours later than start time.
    

**Resolution** : The end time of a reservation period must be at least 24 hours later than the start time. However, to increase your chances that Google Cloud approves your future reservation request, specify a [recommended minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period).

### Invalid start time

The following error occurs when you specify an invalid start time for the reservation period of a future reservation request.

**Error messages** :
    
    
    Future reservation start time is either in the past or too early.
    

**Resolution** : When creating or modifying a future reservation request, specify a start time that is at least one hour later when you submit a future reservation request for review. However, to increase your chances that Google Cloud approves your future reservation request, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

### Overlapping consumer projects

The following error occurs when your current project, or a project you want to share a future reservation request with, contains one or both of the following:

  * A shared reservation with matching VM properties and zone that specifies a consumer project that isn't specified in the future reservation request that you want to create.

  * A future reservation request with matching VM properties and zone that specifies an owner or consumer project that is not specified in the future reservation request that you want to create.




**Error message** :
    
    
    Future reservation with conflicting projects and matching instance properties with existing and overlapping shared projects is not allowed.
    

**Resolution** : When you're creating a future reservation request, make sure to follow the [restrictions for creating future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions-create).

If you need to delete or modify auto-created reservations, on-demand reservations, or future reservation requests to stop them from restricting the type of future reservation requests that you can create, then do one or more of the following:

  * Modify existing [draft](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-draft-future-reservation) or [approved shared future reservation requests](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-submitted-future-reservation) to change their consumer projects or share type.

  * [Modify existing on-demand or auto-created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modifying-consumer-projects-shared-reservation) to modify their consumer projects.

  * [Delete any existing future reservation requests](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#delete-future-reservation) before the start time of its reservation period or after the end time of its reservation period.

  * [Delete any existing on-demand or auto-created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete). You can only delete an auto-created reservation after the end of its reservation period.




### Overlapping reservation periods

The following error occurs when the reservation period of your future reservation request overlaps with the reservation period of an existing future reservation request with matching VM properties and zone.

The existing future reservation request can be either located in the same project of your reservation request or in a project you want to share your future reservation request with.

**Error message** :
    
    
    Future reservation with overlapping time window for same instance properties and overlapping shared projects is not allowed.
    

**Resolution** : Try one of the following:

  * Modify the reservation period of the future reservation request that you're creating.

  * Modify the reservation period of an existing [draft](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-draft-future-reservation) or [approved future reservation request](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-submitted-future-reservation)

  * [Delete an existing future reservation request](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#delete-future-reservation) and stop it from restricting the reservation period of the future reservation request that you're creating.




### Project without an organization

The following error occurs when you specify a project that doesn't belong to an organization.

**Error message** :
    
    
    Cannot create Shared Future Reservations in a project that does not belong to an organization.
    

**Resolution** : Try one of the following:

  * [Migrate your current project to an organization](https://docs.cloud.google.com/resource-manager/docs/project-migration#migrating_projects_no_org) and then create the shared future reservation request.

**Caution:** Any existing reservations and future reservations in a project you want to share the future reservation request with restrict the project from the types of future reservation requests you can create. For more information, see [Restrictions](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions).
  * Create a shared future reservation request in a project that belongs to the [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) where you want to create the future reservation request.




## Future reservation requests errors from instance templates

This section describes the errors that might prevent you from creating a future reservation request by [specifying an instance template](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-instance-template).

### Cross project referencing is not allowed

The following error occurs when you try to create a future reservation request by specifying an instance template from another project.

**Error message** :
    
    
    Cross project referencing is not allowed for this resource.
    

**Resolution** : Do the following:

  1. Make sure that the project ID and instance template's name you specify in your future reservation request are correct. To check that an instance template exists, [get information about the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template).

  2. An instance template contains project-specific settings, so you can only access and use an instance template within the same project. Instead, do one of the following:

     * To create a future reservation request by specifying an instance template:

       1. [Create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template) within your project.

       2. Specify the newly created instance template when creating a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-instance-template) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-instance-template).

**Caution:** Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in `us-central1-a` zone, then you must create your reservation in the same zone. Otherwise, creating the reservation or the VMs that can consume the reservation fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ get information about the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

     * To create a future reservation request without specifying an instance template, create instead a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-vm-properties) or [shared reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-vm-properties) by specifying VM properties directly.




### Invalid Local SSD disk size

The following error occurs when you try to create a future reservation request by specifying an instance template that includes a Local SSD disk, but the template doesn't specify the Local SSD disk's size.

**Error message** :
    
    
    Disk LOCAL_SSD_NAME provided in the instance template has invalid size: 0 GB.
    

**Resolution** : You can't update instance templates. Instead, do the following:

  1. Create a new instance template and make sure to specify the [disk size](https://docs.cloud.google.com/compute/docs/disks#localssds) of any Local SSD disks that you include in the template.

  2. Use the newly created instance template to create a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-instance-template) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-instance-template).

**Caution:** Create your future reservation request in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in the `us-central1-a` zone, then you must create your future reservation request in the same zone. Otherwise, creating the future reservation request fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ view details about the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).




### Invalid zone for an instance template

The following error occurs when you try to create a future reservation request by specifying an instance template with an invalid location for your template.

**Error message** :
    
    
    Future reservation cannot be created outside the zone/region of source resource.
    

**Resolution** : Do one of the following:

  * Make sure to create your future reservation request in the same region and zone as the resources within the instance template. Any [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in the `us-central1-a` zone, then you must create your future reservation request in the same zone. Otherwise, creating the future reservation request fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [get information about the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  * Use an instance template that doesn't restrict to a specific region or zone. Because you can't update instance templates, do the following:

    1. [Create a new instance template based on an existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template) with the updated properties.

    2. Create a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-instance-template) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-instance-template). by specifying the newly created instance template.

    3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).




### Override instance template properties

The following error occurs when you try to create a future reservation request by specifying both an instance template and VM properties.

**Error message** :
    
    
    InstanceProperties cannot be specified while an instance template is being provided.
    

**Resolution** : Do one of the following:

  * To create a future reservation request by specifying an instance template, make sure to remove _any_ field that specifies VM properties.

  * To create a future reservation request by specifying an instance template with different VM properties, do the following:

    1. You can't update an existing instance template. Instead, [create a new instance template based on an existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template).

    2. Specify the newly created instance template when creating a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-instance-template) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-instance-template).

**Caution:** Create your future reservation request in the same region and zone as the resources within the instance template. Any [ regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [ zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk in the `us-central1-a` zone, then you must create your future reservation request in the same zone. Otherwise, creating the future reservation request fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [ view details about the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

    3. Optional: [Delete the older instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

  * To create a future reservation request without specifying an instance template, create instead a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-vm-properties) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-vm-properties) by specifying VM properties directly.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
