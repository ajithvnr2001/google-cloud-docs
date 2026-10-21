---
url: https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations/
title: Create shared future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:19.558364+00:00
---

# Create shared future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create shared future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a shared future reservation request. This request lets you share reserved resources with up to 100 projects in your Google Cloud organization. To reserve resources for only one project, see [Create future reservation requests for a single project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations).

When you create a future reservation request, you request Google Cloud to reserve vCPUs, memory, GPUs, and Local SSD disks to create virtual machine (VM) instances for a future date and time. If Google Cloud approves your request, then Compute Engine creates reservations with your requested resources at your specified date and time. An approved future reservation request gives you the following benefits:

  * **Exclusive resource access**. Your project, and any project that you share the future reservation request with, maintain exclusive access to the reserved resources for the entire reservation period. After the reservation period ends, any VMs that you created by using the reserved resources continue to run unless you stop or delete them.

  * **High assurance of VM creation**. You can use the reserved resources to create VMs that exactly match the properties of your reservations. This action gives you high assurance of VM capacity and minimizes the risk of encountering resource availability errors.




To learn more about the requirements and limitations that apply when you create a future reservation request, see [About future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview).

## Before you begin

  * Before you submit a future reservation request for GPU or H4D VMs, you must contact your account team or the sales team. Otherwise, Google Cloud is likely to decline it.
  * Verify that you have sufficient quota for the resources that you want to reserve. If your quota is insufficient, then Google Cloud is likely to decline your future reservation request. Or, if the request is approved but you lack quota at the start time of your request, Compute Engine only delivers part, or none, of the reserved resources. For more information about the different types of quota in Compute Engine, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).
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

To get the permissions that you need to create shared future reservation requests, ask your administrator to grant you the [Compute Future Reservation User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationUser) (`roles/compute.futureReservationUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create shared future reservation requests. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create shared future reservation requests:

  * To create a future reservation request: `compute.futureReservations.create` on the project 
  * To let Compute Engine auto-create reservations: `compute.reservations.create` on the project 
  * To specify an instance template: `compute.instanceTemplates.useReadOnly` on the instance template 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restrictions

In addition to the general [restrictions](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions) for future reservations, creating shared future reservation requests has the following restrictions:

  * The project you use to create shared future reservation requests (the owner project) must be added to the allowlist for the **Shared Reservations Owner Projects** (`compute.sharedReservationsOwnerProjects`) organization policy constraint by an organization policy administrator. For more information, see [Allow and restrict projects to create and modify shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#allow-shared-reservations) in the Compute Engine reservations documentation.

  * If you move a project that created a shared future reservation request to a different organization, the shared future reservation is deleted. The project is not automatically removed from the **Shared Reservations Owner Projects** (`compute.sharedReservationsOwnerProjects`) organizational policy constraint, but you can remove the project from this constraint if needed.

  * Each shared future reservation request can be shared with up to 100 consumer projects.

  * For each organization, you can create up to 100 shared future reservation requests for each unique combination of [VM properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).




## Create a draft request

When creating a future reservation request, you can either save the request as a draft and later submit it to Google Cloud for review, or directly submit the request for review. Google recommends creating a draft request first as this lets you [determine the number of VMs](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation) that Compute Engine will provision for your request instead of manually estimating this number, and optionally [modify the number of reserved VMs in the request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations) before submitting it for review.

To consume an auto-created reservation for a future reservation, a VM must have [properties that _exactly_ match](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) that reservation. To specify the properties of the VMs that you want to request to reserve by creating a draft future reservation request, use one of the following methods:

  * Recommended: Specify an instance template

You can use an existing [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to define the properties of a draft future reservation request. By using an instance template, you can define the properties of a future reservation request and the VMs that can consume the auto-created reservations in the same place. However, because templates are project-specific, you can't use the same template to create VMs that can consume the auto-created reservations outside of the project that created the future reservation request. For the projects the future reservation is shared with, you must create similar templates in those projects or create VMs by specifying properties directly.

  * Specify an existing VM

You can use an existing VM to define the properties of a future reservation request. By using the properties of an existing VM, you can consume the auto-created reservations provisioned for the future reservation by creating VMs with properties that match the reference VM.

  * Specify properties directly

You can directly define the properties of a draft future reservation request. This method requires you to manually ensure that the properties of your VMs and the auto-created reservations _exactly_ match—any mismatched properties prevent consumption.




An auto-created reservation for a future reservation can be automatically consumed by any VM with matching properties. If you want to avoid a VM to consume any of these auto-created reservations, see how to [create VMs without consuming reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption).

### Specify an instance template

When creating a shared future reservation request by specifying an instance template, consider the following:

  * An instance template contains project-specific settings, so you can only access and use an instance template within the same project. If you create a shared future reservation request by specifying an instance template, you must create similar templates to create VMs, or create VMs by specifying matching properties directly, to consume the auto-created reservations in each consumer project.

  * You must create your future reservation request in the same region and zone as the resources within the instance template. Any [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresources) that are specified in an instance template—such as a machine type or a Persistent Disk—restrict the use of the template to the locations where those resources are located. For example, if your instance template specifies an existing Persistent Disk in the `us-central1-a` zone, then you must create your future reservation request in the same zone. Otherwise, creating the future reservation request fails.

To check if an existing template specifies any resources that bind the template to a specific region or zone, [view the details of the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  * If you want to attach the auto-created reservations provisioned for a future reservation to a commitment, then you must disable the auto-delete option. For more information, see [Restrictions after creation](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions-after-create).




After creating a future reservation request, you can't modify the future reservation request to override the template's VM properties or specify another template. Instead, if you need to change the VM properties specified in the request, you must [create a new future reservation request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations#change-other-properties).

To create a shared future reservation by specifying an existing instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

  4. In the **Machine configuration** section, do the following: 

     1. Select **Use instance template**.

     2. In **Instance template** list, select the instance template. If you select a regional instance template, then you can only reserve resources within the same region as the template's region.

  5. In the **Location** section, in the **Region** and **Zone** lists, select the region and zone in which to reserve resources.

  6. In the **Capacity details** section, in the **Total capacity needed** , enter the [total count of VMs](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) that you want to reserve.

**Important:** Verify that you have sufficient quota for the resources that you want to reserve, both when you submit your request and at the request's start time. Otherwise, Google Cloud might decline your future reservation request or deliver only part of the requested resources.
  7. In the **Reservation period** section, do the following:

     1. In the **Start time** field, specify a start time for the reservation period. The start time can't be later than one year from when you submit your future reservation request for review. To have sufficient time to optionally modify, cancel, or delete the future reservation before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

     2. In the **End time** field, specify an end time for the reservation period. In the **Duration summary** section, you can see the length of the reservation period. To increase the likelihood that Google Cloud approves your future reservation request after you submit it, we recommend that you specify a reservation period of at least 365 days.

  8. Click **Next**.

  9. In the **Auto-delete** section, do one of the following:

     * To enable Compute Engine to automatically delete the auto-created reservations for your future reservation request, do the following:

**Caution:** If you enable the auto-delete option, then Compute Engine deletes all the auto-created reservations at the specified deletion time, whether the reservations are fully consumed or not.
       1. Select the **Enable auto-delete** checkbox.

       2. Optional: In the **Auto-delete time** field, enter a date and time when to delete the auto-created reservations. The date and time must be after the end time of the reservation period. If you leave this field empty, then Compute Engine deletes the auto-created reservations within two hours after the reservation period's end time.

     * To disable automatic deletion, clear the **Enable auto-delete** checkbox.

  10. In the **Share type** section, do the following:

     1. To shared the reserved resources with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the future reservation request with. You can select up to 100 projects.

  11. Click **Next**.

  12. In the **Future reservation name** field, enter a name for your future reservation request.

  13. In the **Prefix** field, enter a name prefix. All auto-created reservations for this future reservation request use this prefix.

  14. To finish creating the draft future reservation request, click **Save a draft**. The **Reservations** page appears. Creating the future reservation request can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).




###  gcloud 

To create a shared future reservation request by specifying an instance template, use the [`gcloud compute future-reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create) with the `--share-setting=projects` and `--share-with` flags. 

To create a draft future reservation request by specifying an instance template without including any optional flags, and auto-delete the auto-created reservation at the end of the reservation period, run the following command:
    
    
    gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
        --auto-delete-auto-created-reservations \
        --share-setting=projects \
        --share-with=CONSUMER_PROJECT_IDS \
        --source-instance-template=INSTANCE_TEMPLATE_URL \
        --start-time=START_TIME \
        --end-time=END_TIME \
        --total-count=TOTAL_COUNT \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.


  * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects that you want to allow to consume the auto-created reservations for this future reservation request—for example, `project-1,project-2`. You can specify up to 100 projects. These projects must be in the same organization as the project where the future reservation request is created (the owner project). Don't specify the owner project. By default, it's already allowed to consume the auto-created reservations for this future reservation request.


  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`



  * `START_TIME`: the start time of the reservation period as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be formatted as follows:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a data formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

The start time can't be later than one year from the date and time at which you submit a future reservation request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation request after it's approved and before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: the end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, we recommend that you specify a reservation period of at least 365 days. To specify a duration instead of an end time, replace the `--end-time` flag with the `--duration=END_DURATION` flag. Replace `END_DURATION` with a duration in seconds. For example, specify `31536000` for 31,536,000 seconds (365 days).

**Important:** To prevent errors when creating the future reservation request, verify that the reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. To get an overview of the reservation periods of your future reservation requests, [view a list of future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).
  * `TOTAL_COUNT`: the [total count](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) of VMs that you want reserved.

  * `ZONE`: the zone in which to reserve resources.




For example, suppose that you want to create a draft future reservation request named `fr-02` in zone `us-central1-a` with the following properties:

  * A reservation period that starts at midnight on November 10, 2024 UTC, and ends at midnight on December 10, 2024 UTC.

  * A total count of 80 VMs.



  * A regional instance template from region `us-central1`.


  * The auto-delete option enabled. The auto-created reservations are deleted at the end of the reservation period.


  * The future reservation request is shared with `project-1` and `project-2`.



To create `fr-02`, run the following command:
    
    
    gcloud compute future-reservations create fr-02 \
        --auto-delete-auto-created-reservations \
        --share-setting=projects \
        --share-with=project-1,project-2 \
        --source-instance-template=projects/example-project/regions/us-central1/instanceTemplates/example-template \
        --start-time=2024-11-10T00:00:00Z \
        --end-time=2024-12-10T00:00:00Z \
        --total-count=80 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To delete the auto-created reservations after the end time of the reservation period, select one of the following methods:

    * To delete the auto-created reservations at a specific date and time after the end time of the reservation period, include the `--auto-created-reservations-delete-time` flag.
          
          gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-delete-time= AUTO_CREATED_RESERVATIONS_DELETE_TIME** \
              --auto-delete-auto-created-reservations \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --start-time=START_TIME \
              --end-time=END_TIME \
              --total-count=TOTAL_COUNT \
              --zone=ZONE
          

Replace AUTO_CREATED_RESERVATIONS_DELETE_TIME with a date and time formatted as an RFC 3339 timestamp.

    * To delete the auto-created reservations after a specific duration after the end time of the reservation period, include the `--auto-created-reservations-duration` flag.
          
          gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-duration= DURATION_BEFORE_DELETE** \
              --auto-delete-auto-created-reservations \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --start-time=START_TIME \
              --end-time=END_TIME \
              --total-count=TOTAL_COUNT \
              --zone=ZONE
          

Replace DURATION_BEFORE_DELETE with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for one day, two hours, three minutes, and four seconds.

  * To disable the auto-delete option for the auto-created reservations, replace the `--auto-delete-auto-created-reservations` flag with the `--no-auto-delete-auto-created-reservations` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            **--no-auto-delete-auto-created-reservations** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        



  * To specify a name prefix for the auto-created reservations, include the `--name-prefix` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            **--name-prefix= NAME_PREFIX** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        

Replace `NAME_PREFIX` with the name prefix for each auto-created reservation. To help you identify the auto-created reservations for this future reservation request, Google Cloud recommends to specify a unique name prefix.




###  REST 

To create a shared future reservation request by specifying an instance template, make a `POST` request to the [`futureReservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/insert).

To create a draft future reservation request by specifying an instance template without including any optional fields, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
    
    {
      "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
      "name": "FUTURE_RESERVATION_NAME",
      "shareSettings": {
        "projects": [
          "CONSUMER_PROJECT_ID_1",
          "CONSUMER_PROJECT_ID_2"
        ],
        "shareType": "SPECIFIC_PROJECTS"
      },
      "specificSkuProperties": { 
        "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL",
        "totalCount": TOTAL_COUNT
      },
      "timeWindow": {
        "startTime": "START_TIME",
        "endTime": "END_TIME"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you want to reserve resources and where the instance template is located. 

  * `ZONE`: the zone in which to reserve resources.

  * `AUTO_DELETE_AUTO_CREATED_RESERVATIONS`: if you set this field to `true`, then Compute Engine automatically deletes the auto-created reservations for this future reservation within two hours from the end time of reservation period. If you want to attach your auto-created reservations to a commitment, then set this field to `false`.



  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the IDs of projects that this future reservation request can be shared with. You can specify up to 100 projects. These projects must be in the same organization as the project where the future reservation request is created (the owner project). Don't specify the owner project. By default, it's already allowed to consume the auto-created reservations for this future reservation request.


  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`



  * `TOTAL_COUNT`: the [total count](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) of VMs that you want reserved.

  * `START_TIME`: the start time of the reservation period as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be formatted as follows:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a data formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

The start time can't be later than one year from the date and time at which you submit a future reservation request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation request after it's approved and before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: the end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, specify a reservation period of at least 365 days. To specify a duration instead of an end time, you can replace the `endTime` field with the `duration` field:
        
        "duration": {
          "seconds": END_DURATION
        }
        

Replace `END_DURATION` with a duration in seconds. For example, specify `31536000` for 31,536,000 seconds (365 days).

**Important:** To prevent errors when you create the future reservation request, verify that the reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. To get an overview of the reservation periods of your future reservation requests, [view a list of future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).



For example, suppose that you want to create a draft future reservation request named `fr-02` in zone `us-central1-a` with the following properties:

  * A reservation period that starts at midnight on November 10, 2024 UTC, and ends at midnight on December 10, 2024 UTC.

  * A total count of 80 VMs.



  * A regional instance template from region `us-central1`.


  * The auto-delete option enabled. The auto-created reservations are deleted at the end of the reservation period.


  * The future reservation request is shared with `project-1` and `project-2`.



To create `fr-02`, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations
    
    {
      "autoDeleteAutoCreatedReservations": true,
      "name": "fr-02",
      "specificSkuProperties": { 
        "sourceInstanceTemplate": "projects/example-project/regions/us-central1/instanceTemplates/example-template",
        "totalCount": 80
      },
      "shareSettings": {
        "projects": [
          "project-1",
          "project-2"
        ],
        "shareType": "SPECIFIC_PROJECTS"
      },
      "timeWindow": {
        "startTime": "2024-11-10T00:00:00Z",
        "endTime": "2024-12-10T00:00:00Z"
      }
    }
    

Optionally, you can do one or more of the following:

  * To specify a name prefix for the auto-created reservations, include the `namePrefix` field.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
          "name": "FUTURE_RESERVATION_NAME",
          **"namePrefix": " NAME_PREFIX"**,
          "shareSettings": {
            "projects": [
              "CONSUMER_PROJECT_ID_1",
              "CONSUMER_PROJECT_ID_2"
            ],
            "shareType": "SPECIFIC_PROJECTS"
          },
          "specificSkuProperties": { 
            "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL",
            "totalCount": TOTAL_COUNT
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

Replace `NAME_PREFIX` with the name prefix for each auto-created reservation. To help you identify the auto-created reservations for this future reservation request, Google Cloud recommends to specify a unique name prefix.



  * To delete the auto-created reservations after the end time of the reservation period, select one of the following methods:

    * To delete the auto-created reservations after a specific time after the end of your reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and include the `autoCreatedReservationsDeleteTime` field.
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
          
          {
            **"autoCreatedReservationsDeleteTime": " DELETE_TIME",
            "autoDeleteAutoCreatedReservations": true**,
            "name": "FUTURE_RESERVATION_NAME",
            "shareSettings": {
              "projects": [
                "CONSUMER_PROJECT_ID_1",
                "CONSUMER_PROJECT_ID_2"
              ],
              "shareType": "SPECIFIC_PROJECTS"
            },
            "specificSkuProperties": { 
              "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL",
              "totalCount": TOTAL_COUNT
            },
            "timeWindow": {
              "startTime": "START_TIME",
              "endTime": "END_TIME"
            }
          }
          

Replace `DELETE_TIME` with a date and time when Compute Engine deletes the auto-created reservations. The date and time must be formatted as an RFC 3339 timestamp.

    * To delete the auto-created reservations after a specific duration from the start time of the reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and include the `autoCreatedReservationsDuration` field.
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
          
          {
            **"autoCreatedReservationsDuration": {
              "seconds": " DURATION_BEFORE_DELETE"
            },
            "autoDeleteAutoCreatedReservations": true**,
            "name": "FUTURE_RESERVATION_NAME",
            "shareSettings": {
              "projects": [
                "CONSUMER_PROJECT_ID_1",
                "CONSUMER_PROJECT_ID_2"
              ],
              "shareType": "SPECIFIC_PROJECTS"
            },
            "specificSkuProperties": { 
              "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL",
              "totalCount": TOTAL_COUNT
            },
            "timeWindow": {
              "startTime": "START_TIME",
              "endTime": "END_TIME"
            }
          }
          

Replace `DURATION_BEFORE_DELETE` with a duration in seconds. For example, specify `604800` for 604,800 seconds (7 days).




After creating a draft future reservation request, you can determine the [number of VMs that Compute Engine will provision for the request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation).

### Specify an existing VM

You can only create a draft future reservation request based on an existing VM in the same project and zone as the VM.

After the future reservation request is approved by Google Cloud and it enters its reservation period, you can consume its auto-created reservations by creating VMs with properties that match the reference VM. You can do this by doing one of the following:

  * Create and use an instance template as follows:

    1. [Create an instance template based on the reference VM](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) without overriding the reference VM's properties.

**Note:** You can't create an instance template based on the reference VM outside of the VM's project. For the projects that the reservation is shared with, you must create similar instance templates in those projects.
    2. Create VMs using the newly-created template by doing one or both of the following:

       * [Create a single VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

       * [Create a zonal managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig)

  * Create a VM with properties that _exactly_ match the reference VM as follows:

    * In the owner project, [create a VM based on the reference VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) without changing the properties of the VM that you're creating.

    * In the consumer projects, create a VM while manually ensuring that its properties and the reference VM's properties match.




To create a shared future reservation request that uses the properties of an existing VM, do the following:

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

  4. In the **Machine configuration** section, do the following: 

     1. Select **Use existing VM**.

     2. In the **Existing VM** list, select the VM whose properties you want to use to create the reservation.

  5. In the **Location** section, in the **Region** and **Zone** lists, select the region and zone in which to reserve resources.

  6. In the **Capacity details** section, in the **Total capacity needed** , enter the [total count of VMs](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) that you want to reserve.

**Important:** Verify that you have sufficient quota for the resources that you want to reserve, both when you submit your request and at the request's start time. Otherwise, Google Cloud might decline your future reservation request or deliver only part of the requested resources.
  7. In the **Reservation period** section, do the following:

     1. In the **Start time** field, specify a start time for the reservation period. The start time can't be later than one year from when you submit your future reservation request for review. To have sufficient time to optionally modify, cancel, or delete the future reservation before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

     2. In the **End time** field, specify an end time for the reservation period. In the **Duration summary** section, you can see the length of the reservation period. To increase the likelihood that Google Cloud approves your future reservation request after you submit it, we recommend that you specify a reservation period of at least 365 days.

  8. Click **Next**.

  9. In the **Auto-delete** section, do one of the following:

     * To enable Compute Engine to automatically delete the auto-created reservations for your future reservation request, do the following:

**Caution:** If you enable the auto-delete option, then Compute Engine deletes all the auto-created reservations at the specified deletion time, whether the reservations are fully consumed or not.
       1. Select the **Enable auto-delete** checkbox.

       2. Optional: In the **Auto-delete time** field, enter a date and time when to delete the auto-created reservations. The date and time must be after the end time of the reservation period. If you leave this field empty, then Compute Engine deletes the auto-created reservations within two hours after the reservation period's end time.

     * To disable automatic deletion, clear the **Enable auto-delete** checkbox.

  10. In the **Share type** section, do the following:

     1. To shared the reserved resources with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the future reservation request with. You can select up to 100 projects.

  11. Click **Next**.

  12. In the **Future reservation name** field, enter a name for your future reservation request.

  13. In the **Prefix** field, enter a name prefix. All auto-created reservations for this future reservation request use this prefix.

  14. To finish creating the draft future reservation request, click **Save a draft**. The **Reservations** page appears. Creating the future reservation request can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).




After creating a draft future reservation request, you can determine the [number of VMs that Compute Engine will provision for the request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation).

### Specify properties directly

If you want to attach the auto-created reservations provisioned for a future reservation to a commitment, then you must disable the auto-delete option. For more information, see [Restrictions after creation](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions-after-create).

To create a shared future reservation request by specifying properties directly, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

  4. In the **Machine configuration** section, do the following: 

     1. Select **Specify machine type** if it isn't already selected.

     2. Specify the machine type to use for the reserved VMs.

  5. In the **Location** section, in the **Region** and **Zone** lists, select the region and zone in which to reserve resources.

  6. In the **Capacity details** section, in the **Total capacity needed** , enter the [total count of VMs](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) that you want to reserve.

**Important:** Verify that you have sufficient quota for the resources that you want to reserve, both when you submit your request and at the request's start time. Otherwise, Google Cloud might decline your future reservation request or deliver only part of the requested resources.
  7. In the **Reservation period** section, do the following:

     1. In the **Start time** field, specify a start time for the reservation period. The start time can't be later than one year from when you submit your future reservation request for review. To have sufficient time to optionally modify, cancel, or delete the future reservation before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

     2. In the **End time** field, specify an end time for the reservation period. In the **Duration summary** section, you can see the length of the reservation period. To increase the likelihood that Google Cloud approves your future reservation request after you submit it, we recommend that you specify a reservation period of at least 365 days.

  8. Click **Next**.

  9. In the **Auto-delete** section, do one of the following:

     * To enable Compute Engine to automatically delete the auto-created reservations for your future reservation request, do the following:

**Caution:** If you enable the auto-delete option, then Compute Engine deletes all the auto-created reservations at the specified deletion time, whether the reservations are fully consumed or not.
       1. Select the **Enable auto-delete** checkbox.

       2. Optional: In the **Auto-delete time** field, enter a date and time when to delete the auto-created reservations. The date and time must be after the end time of the reservation period. If you leave this field empty, then Compute Engine deletes the auto-created reservations within two hours after the reservation period's end time.

     * To disable automatic deletion, clear the **Enable auto-delete** checkbox.

  10. In the **Share type** section, do the following:

     1. To shared the reserved resources with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the future reservation request with. You can select up to 100 projects.

  11. Click **Next**.

  12. In the **Future reservation name** field, enter a name for your future reservation request.

  13. In the **Prefix** field, enter a name prefix. All auto-created reservations for this future reservation request use this prefix.

  14. To finish creating the draft future reservation request, click **Save a draft**. The **Reservations** page appears. Creating the future reservation request can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).




###  gcloud 

To create a shared future reservation request by specifying properties directly, use the [`gcloud compute future-reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create) with the `--share-setting=projects` and `--share-with` flags. 

To create a draft future reservation request by specifying properties directly without including any optional flags, and auto-delete the auto-created reservation at the end of the reservation period, run the following command:
    
    
    gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
        --auto-delete-auto-created-reservations \
        --machine-type=MACHINE_TYPE \
        --share-setting=projects \
        --share-with=CONSUMER_PROJECT_IDS \
        --start-time=START_TIME \
        --end-time=END_TIME \
        --total-count=TOTAL_COUNT \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.


  * `MACHINE_TYPE`: the machine type to use for each reserved VM.


  * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects that you want to allow to consume the auto-created reservations for this future reservation request—for example, `project-1,project-2`. You can specify up to 100 projects. These projects must be in the same organization as the project where the future reservation request is created (the owner project). Don't specify the owner project. By default, it's already allowed to consume the auto-created reservations for this future reservation request.


  * `START_TIME`: the start time of the reservation period as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be formatted as follows:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a data formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

The start time can't be later than one year from the date and time at which you submit a future reservation request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation request after it's approved and before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: the end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, we recommend that you specify a reservation period of at least 365 days. To specify a duration instead of an end time, replace the `--end-time` flag with the `--duration=END_DURATION` flag. Replace `END_DURATION` with a duration in seconds. For example, specify `31536000` for 31,536,000 seconds (365 days).

**Important:** To prevent errors when creating the future reservation request, verify that the reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. To get an overview of the reservation periods of your future reservation requests, [view a list of future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).
  * `TOTAL_COUNT`: the [total count](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) of VMs that you want reserved.

  * `ZONE`: the zone in which to reserve resources.




For example, suppose that you want to create a draft future reservation request named `fr-02` in zone `us-central1-a` with the following properties:

  * A reservation period that starts at midnight on November 10, 2024 UTC, and ends at midnight on December 10, 2024 UTC.

  * A total count of 80 VMs.



  * An N2 predefined machine type with 4 vCPUs.


  * The auto-delete option enabled. The auto-created reservations are deleted at the end of the reservation period.


  * The future reservation request is shared with `project-1` and `project-2`.



To create `fr-02`, run the following command:
    
    
    gcloud compute future-reservations create fr-02 \
        --auto-delete-auto-created-reservations \
        --machine-type=n2-standard-4 \
        --share-setting=projects \
        --share-with=project-1,project-2 \
        --start-time=2024-11-10T00:00:00Z \
        --end-time=2024-12-10T00:00:00Z \
        --total-count=80 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To attach GPUs to your reserved N1 VMs, include the `--accelerator` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            **--accelerator= NUMBER_OF_ACCELERATORS,type=ACCELERATOR_TYPE** \
            --auto-delete-auto-created-reservations \
            --machine-type=MACHINE_TYPE \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        

Replace the following:

    * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

    * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). To prevent errors, verify that your chosen GPU model is available in the zone where you're creating the future reservation request.



  * To delete the auto-created reservations after the end time of the reservation period, select one of the following methods:

    * To delete the auto-created reservations at a specific date and time after the end time of the reservation period, include the `--auto-created-reservations-delete-time` flag.
          
          gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-delete-time= AUTO_CREATED_RESERVATIONS_DELETE_TIME** \
              --auto-delete-auto-created-reservations \
              --machine-type=MACHINE_TYPE \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --start-time=START_TIME \
              --end-time=END_TIME \
              --total-count=TOTAL_COUNT \
              --zone=ZONE
          

Replace AUTO_CREATED_RESERVATIONS_DELETE_TIME with a date and time formatted as an RFC 3339 timestamp.

    * To delete the auto-created reservations after a specific duration after the end time of the reservation period, include the `--auto-created-reservations-duration` flag.
          
          gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-duration= DURATION_BEFORE_DELETE** \
              --auto-delete-auto-created-reservations \
              --machine-type=MACHINE_TYPE \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --start-time=START_TIME \
              --end-time=END_TIME \
              --total-count=TOTAL_COUNT \
              --zone=ZONE
          

Replace DURATION_BEFORE_DELETE with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for one day, two hours, three minutes, and four seconds.

  * To disable the auto-delete option for the auto-created reservations, replace the `--auto-delete-auto-created-reservations` flag with the `--no-auto-delete-auto-created-reservations` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            **--no-auto-delete-auto-created-reservations** \
            --machine-type=MACHINE_TYPE \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        



  * To attach Local SSD disks to a [machine type that doesn't include Local SSD disks by default](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options), include the `--local-ssd` flag. You can only attach Local SSD disk of 375 GB.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            **--local-ssd=count= NUMBER_OF_LOCAL_SSD_DISKS,size=375,interface=INTERFACE_TYPE** \
            --machine-type=MACHINE_TYPE \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        

Replace the following:

    * `NUMBER_OF_LOCAL_SSD_DISKS`: the number of Local SSD disks to attach.

    * `INTERFACE_TYPE`: the type of disk interface that you want the Local SSD disks to use and that [your specified machine type supports](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface). Specify one of the following values:

      * For the NVME disk interface: `nvme`

      * For the SCSI disk interface: `scsi`

  * To have the reserved VMs use a specific minimum CPU platform instead of the zone's default CPU platform, include the `--min-cpu-platform` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            --machine-type=MACHINE_TYPE \
            **--min-cpu-platform=" MIN_CPU_PLATFORM"** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        

Replace MIN_CPU_PLATFORM with a minimum CPU platform. To make sure that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).



  * To specify a name prefix for the auto-created reservations, include the `--name-prefix` flag.
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            --machine-type=MACHINE_TYPE \
            **--name-prefix= NAME_PREFIX** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --total-count=TOTAL_COUNT \
            --zone=ZONE
        

Replace `NAME_PREFIX` with the name prefix for each auto-created reservation. To help you identify the auto-created reservations for this future reservation request, Google Cloud recommends to specify a unique name prefix.




###  REST 

To create a shared future reservation request by specifying properties directly, make a `POST` request to the [`futureReservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/insert).

To create a draft future reservation request by specifying properties directly without including any optional fields, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
    
    {
      "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
      "name": "FUTURE_RESERVATION_NAME",
      "shareSettings": {
        "projects": [
          "CONSUMER_PROJECT_ID_1",
          "CONSUMER_PROJECT_ID_2"
        ],
        "shareType": "SPECIFIC_PROJECTS"
      },
      "specificSkuProperties": { 
        "instanceProperties": {
          "machineType": "MACHINE_TYPE"
        },
        "totalCount": TOTAL_COUNT
      },
      "timeWindow": {
        "startTime": "START_TIME",
        "endTime": "END_TIME"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you want to reserve resources. 

  * `ZONE`: the zone in which to reserve resources.

  * `AUTO_DELETE_AUTO_CREATED_RESERVATIONS`: if you set this field to `true`, then Compute Engine automatically deletes the auto-created reservations for this future reservation within two hours from the end time of reservation period. If you want to attach your auto-created reservations to a commitment, then set this field to `false`.



  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the IDs of projects that this future reservation request can be shared with. You can specify up to 100 projects. These projects must be in the same organization as the project where the future reservation request is created (the owner project). Don't specify the owner project. By default, it's already allowed to consume the auto-created reservations for this future reservation request.


  * `TOTAL_COUNT`: the [total count](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) of VMs that you want reserved.

  * `START_TIME`: the start time of the reservation period as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be formatted as follows:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a data formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

The start time can't be later than one year from the date and time at which you submit a future reservation request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation request after it's approved and before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: the end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, specify a reservation period of at least 365 days. To specify a duration instead of an end time, you can replace the `endTime` field with the `duration` field:
        
        "duration": {
          "seconds": END_DURATION
        }
        

Replace `END_DURATION` with a duration in seconds. For example, specify `31536000` for 31,536,000 seconds (365 days).

**Important:** To prevent errors when you create the future reservation request, verify that the reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. To get an overview of the reservation periods of your future reservation requests, [view a list of future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).



For example, suppose that you want to create a draft future reservation request named `fr-02` in zone `us-central1-a` with the following properties:

  * A reservation period that starts at midnight on November 10, 2024 UTC, and ends at midnight on December 10, 2024 UTC.

  * A total count of 80 VMs.



  * An N2 predefined machine type with 4 vCPUs.


  * The auto-delete option enabled. The auto-created reservations are deleted at the end of the reservation period.


  * The future reservation request is shared with `project-1` and `project-2`.



To create `fr-02`, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations
    
    {
      "autoDeleteAutoCreatedReservations": true,
      "name": "fr-02",
      "specificSkuProperties": { 
        "instanceProperties": {
          "machineType": "n2-standard-4"
        },
        "totalCount": 80
      },
      "shareSettings": {
        "projects": [
          "project-1",
          "project-2"
        ],
        "shareType": "SPECIFIC_PROJECTS"
      },
      "timeWindow": {
        "startTime": "2024-11-10T00:00:00Z",
        "endTime": "2024-12-10T00:00:00Z"
      }
    }
    

Optionally, you can do one or more of the following:

  * To specify a name prefix for the auto-created reservations, include the `namePrefix` field.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
          "name": "FUTURE_RESERVATION_NAME",
          **"namePrefix": " NAME_PREFIX"**,
          "shareSettings": {
            "projects": [
              "CONSUMER_PROJECT_ID_1",
              "CONSUMER_PROJECT_ID_2"
            ],
            "shareType": "SPECIFIC_PROJECTS"
          },
          "specificSkuProperties": { 
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            },
            "totalCount": TOTAL_COUNT
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

Replace `NAME_PREFIX` with the name prefix for each auto-created reservation. To help you identify the auto-created reservations for this future reservation request, Google Cloud recommends to specify a unique name prefix.



  * To attach GPUs to your reserved N1 VMs, include the `guestAccelerators` field.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
          "name": "FUTURE_RESERVATION_NAME",
          "shareSettings": {
            "projects": [
              "CONSUMER_PROJECT_ID_1",
              "CONSUMER_PROJECT_ID_2"
            ],
            "shareType": "SPECIFIC_PROJECTS"
          },
          "specificSkuProperties": {
            "instanceProperties": {
              **"guestAccelerators": [
                {
                  "acceleratorCount": NUMBER_OF_ACCELERATORS,
                  "acceleratorType": "ACCELERATOR_TYPE"
                }
              ]**,
              "machineType": "MACHINE_TYPE"
            },
            "totalCount": TOTAL_COUNT
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

Replace the following:

    * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

    * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). To prevent errors, verify that your chosen GPU model is available in the zone where you're creating the future reservation request.

  * To attach Local SSD disks to a [machine type that doesn't include Local SSD disks by default](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options), include the `localSsds` field in the request body. You can only attach Local SSD disks of 375 GB.

For example, to specify two Local SSD disks when creating a draft future reservation request, make a `POST` request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
          "name": "FUTURE_RESERVATION_NAME",
          "shareSettings": {
            "projects": [
              "CONSUMER_PROJECT_ID_1",
              "CONSUMER_PROJECT_ID_2"
            ],
            "shareType": "SPECIFIC_PROJECTS"
          },
          "specificSkuProperties": {
            "instanceProperties": {
              **"localSsds": [
                {
                  "diskSizeGb": "375",
                  "interface": " INTERFACE_TYPE"
                },
                {
                  "diskSizeGb": "375",
                  "interface": "INTERFACE_TYPE"
                }
              ]**,
              "machineType": "MACHINE_TYPE"
            },
            "totalCount": TOTAL_COUNT
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

Replace `INTERFACE_TYPE` with the type of disk interface that you want the Local SSD disks to use and that [your specified machine type supports](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface). Specify one of the following values:

    * For the NVME disk interface: `NVME`

    * For the SCSI disk interface: `SCSI`

  * To have the reserved VMs use a specific minimum CPU platform instead of the zone's default CPU platform, include the `minCpuPlatform`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "autoDeleteAutoCreatedReservations": AUTO_DELETE_AUTO_CREATED_RESERVATIONS,
          "name": "FUTURE_RESERVATION_NAME",
          "shareSettings": {
            "projects": [
              "CONSUMER_PROJECT_ID_1",
              "CONSUMER_PROJECT_ID_2"
            ],
            "shareType": "SPECIFIC_PROJECTS"
          },
          "specificSkuProperties": {
            "instanceProperties": {
              "machineType": "MACHINE_TYPE",
              **"minCpuPlatform": " MINIMUM_CPU_PLATFORM"**
            },
            "totalCount": TOTAL_COUNT
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

Replace MIN_CPU_PLATFORM with a minimum CPU platform. To verify that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).



  * To delete the auto-created reservations after the end time of the reservation period, select one of the following methods:

    * To delete the auto-created reservations after a specific time after the end of your reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and include the `autoCreatedReservationsDeleteTime` field.
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
          
          {
            **"autoCreatedReservationsDeleteTime": " DELETE_TIME",
            "autoDeleteAutoCreatedReservations": true**,
            "name": "FUTURE_RESERVATION_NAME",
            "shareSettings": {
              "projects": [
                "CONSUMER_PROJECT_ID_1",
                "CONSUMER_PROJECT_ID_2"
              ],
              "shareType": "SPECIFIC_PROJECTS"
            },
            "specificSkuProperties": { 
              "instanceProperties": {
                "machineType": "MACHINE_TYPE"
              },
              "totalCount": TOTAL_COUNT
            },
            "timeWindow": {
              "startTime": "START_TIME",
              "endTime": "END_TIME"
            }
          }
          

Replace `DELETE_TIME` with a date and time when Compute Engine deletes the auto-created reservations. The date and time must be formatted as an RFC 3339 timestamp.

    * To delete the auto-created reservations after a specific duration from the start time of the reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and include the `autoCreatedReservationsDuration` field.
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
          
          {
            **"autoCreatedReservationsDuration": {
              "seconds": " DURATION_BEFORE_DELETE"
            },
            "autoDeleteAutoCreatedReservations": true**,
            "name": "FUTURE_RESERVATION_NAME",
            "shareSettings": {
              "projects": [
                "CONSUMER_PROJECT_ID_1",
                "CONSUMER_PROJECT_ID_2"
              ],
              "shareType": "SPECIFIC_PROJECTS"
            },
            "specificSkuProperties": { 
              "instanceProperties": {
                "machineType": "MACHINE_TYPE"
              },
              "totalCount": TOTAL_COUNT
            },
            "timeWindow": {
              "startTime": "START_TIME",
              "endTime": "END_TIME"
            }
          }
          

Replace `DURATION_BEFORE_DELETE` with a duration in seconds. For example, specify `604800` for 604,800 seconds (7 days).




After creating a draft future reservation request, you can determine the [number of VMs that Compute Engine will provision for the request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation).

## Submit a draft request

After a future reservation request is submitted, approved by Google Cloud, and past its lock time, you can delete the future reservation and its auto-created reservations only after the end of the future reservation's reservation period. Deleting an existing future reservation is useful if you need to create another future reservation with the same properties. Thus, before creating a future reservation request, make sure of the following:

  * Any existing reservations or future reservations in a project restrict the share settings of the future reservation requests that you can create. To ensure that you can successfully create a future reservation request, and your request doesn't cause issues in other projects you share future reservation requests or reservations with, see [Restrictions](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions).

  * You must commit to pay for the reserved resources that Compute Engine provisions for the entire reservation period, regardless if the auto-created reservations are consumed or not. For more information, see [Billing](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#billing).




If you want to modify one or more properties when submitting the draft future reservation request for review, then see [Modify future reservation requests](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations) instead.

To submit a draft future reservation request to Google Cloud for review, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. In the **Name** column, click the name of the future reservation request with a procurement status of **Drafting**. The **Future reservations** page with the details of the future reservation request appears.

  4. Click edit **Edit draft**. A page to update the draft future reservation request appears.

  5. To submit the draft future reservation request for review, click **Create**. The **Reservation** page appears.




###  gcloud 

To submit a draft future reservation request for review, use the [`gcloud compute future-reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/update) with the `--planning-status` flag set to `SUBMITTED`.
    
    
    gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
        --planning-status=SUBMITTED \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of an existing draft future reservation request.

  * `ZONE`: the zone where the future reservation request is located.




###  REST 

To submit a draft future reservation request for review, make a `PATCH` request to the [`futureReservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/update). In the request URL, include the `updateMask` query parameter set to `planningStatus`.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus
    
    {
      "name": "FUTURE_RESERVATION_NAME",
      "planningStatus": "SUBMITTED"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the future reservation request is located.

  * `ZONE`: the zone where the future reservation request is located.

  * `FUTURE_RESERVATION_NAME`: the name of an existing draft future reservation request.




After you submit a draft future reservation request for review, you can do the following:

  * To monitor the request's procurement status and see whether Google Cloud has approved or declined your request, [view the details of your future reservation request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

  * To stop Google Cloud from reviewing your request and prevent Compute Engine from provisioning the requested capacity, [cancel or delete your future reservation request](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).




## Troubleshoot

If you run into errors when creating a future reservation request, then see how to [troubleshoot future reservation requests](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations).

If you still encounter issues after troubleshooting, then contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

## What's next

  * Learn how to [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

  * Learn how to [modify future reservation requests](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations).

  * Learn how to [cancel or delete future reservation requests](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).

  * After you reach the start time of your reservation period, learn how to [consume the auto-created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
