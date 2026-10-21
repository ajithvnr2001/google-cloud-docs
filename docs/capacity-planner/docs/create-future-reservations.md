---
url: https://docs.cloud.google.com/capacity-planner/docs/create-future-reservations/
title: Create future reservation requests \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:36:45.435419+00:00
---

# Create future reservation requests  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/create-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Create future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to create [future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) based on the usage and forecast of your Compute Engine resources.

You can use future reservation requests to gain high-level assurance that you have capacity available for creating Compute Engine instances or GPUs at future date and time. Specifically, future reservation requests help ensure that your Google Cloud project, folder, or organization has sufficient capacity during expected growth in a specific zone, such as in the following scenarios:

  * Peak scale events

  * Large-scale migrations

  * Compliance requirements




When you create a future reservation request, and Google Cloud approves it, you commit to pay for the requested resources for the entire reservation period and regardless of usage.

### Limitations

Creating future reservation requests in Capacity Planner has the following limitations:

  * You can only create requests by [specifying properties directly](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#vm-properties).

  * You can only create requests based on the usage and forecast of your compute instances or GPUs.

  * You can't set an end time more than six months from the current date. To set an end time further in the future, choose one of the following:

    * Create a draft request using the Google Cloud console, and then modify it.

    * Generate gcloud CLI commands, and manually edit them before running them.




## Before you begin

  * If you haven't used Capacity Planner before, review [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview) and enable Capacity Planner by completing the [prerequisites for projects and users](https://docs.cloud.google.com/capacity-planner/docs/overview#prerequisites).

  * If you want to create shared future reservation requests, then ensure that the project in which to create a shared request (the owner project) is allowed to create and modify shared reservations. For details, see [Allow and restrict projects from creating and modifying shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).

  * Verify that you have sufficient quota for the resources that you want to reserve. To learn how to check your quota, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).




### Required roles

To get the permissions that you need to create future reservation requests, ask your administrator to grant you the following IAM roles: 

  * To access and view Capacity Planner: [Capacity Planner Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`) on the project, folder, or organization 
  * To create future reservation requests: [Compute Future Reservation User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationUser) (`roles/compute.futureReservationUser`) on the owner project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create future reservation requests. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create future reservation requests:

  * To create future reservation requests: `compute.futureReservations.create` on the owner project 
  * To let Compute Engine auto-create reservations: `compute.reservations.create` on the owner project 
  * To view the forecasted usage of your instances or GPUs: `capacityplanner.forecasts.list` on the project, folder, or organization 
  * To view the actual usage of your instances or GPUs: `capacityplanner.usageHistories.list` on the project, folder, or organization 
  * To summarize the actual usage of your instances or GPUs: `capacityplanner.usageHistories.summarize` on the project, folder, or organization 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

To reserve capacity by creating future reservation requests in Capacity Planner, complete the following steps:

  1. **Choose the creation method**. Choose one of the following methods based on how many machine types you want to reserve capacity for at once, and whether you want to edit a future reservation request before creating it:

     * Recommended: **Generate gcloud CLI commands**

This method is useful for creating one or more future reservation requests at once for various machine types. After configuring the requests in the Google Cloud console, the Google Cloud console generates the gcloud CLI commands to create the requests. Before running the commands, you can optionally edit their fields according to your needs—for example, to specify a recommended [start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time) or [minimum duration](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period) for the reservation period.

     * **Use the Google Cloud console**

This method is useful for creating a single future reservation request for one machine type. Use the Google Cloud console to configure and create the request. You can only modify the request after creating a draft of it.

  2. **Select Compute Engine resources**. Select the compute instances or GPUs, along with their actual and forecasted usage data, that you want to use to create your future reservation requests.

For instructions, see Select the Compute Engine resources in this document.

  3. **Create future reservation requests**. After you select the Compute Engine resources, create a future reservation request using the Google Cloud console for a single machine type, or generate gcloud CLI commands to create future reservation requests for multiple machine types at once.

For instructions, see Create future reservation requests in this document.




## Select the Compute Engine resources

To select the Compute Engine resources to create future reservation requests for, do the following:

  1. In the Google Cloud console, open Capacity Planner.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/overview)

The **Overview** page appears.

  2. Optional: To change the scope (project, folder, or organization) that you want to view data for, do the following:

     1. On the Google Cloud console toolbar, click the resource selector.
     2. In the **Select a resource** dialog that appears, select a project, folder, or organization.
  3. Select one of the following Compute Engine resources:

###  Compute instances 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **Virtual machine** page.

     2. For **Machine family** , select one of the following options:

        * To select a single machine family, select one of the available machine families.

        * To select all machine families, select **All**.

###  GPUs 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **GPU** page.

     2. For **GPU type** , select one of the following options:

        * To select a single GPU type, select one of the available GPU types.

        * To select all GPU types, select **All**.

  4. For **Location** , select a region or zone.

  5. For **Usage percentile** , select a usage percentile.

  6. In the **Usage and forecast by machine types** table, do the following:

     1. In the **View data for** list, select one of the following options:

        * To view usage and forecast by instances, select **VM**.

        * To view usage and forecast by CPU cores, select **Cores**.

        * To view usage and forecast by GPUs, select **GPU**.

     2. For **History start date** , select the start date of the usage period.

     3. For **History end date** , select the end date of the usage period.




## Create future reservation requests

After you select a Compute Engine resource and its usage data in the previous section using the Google Cloud console, you can create future reservation requests for one or more machine types by completing the following steps:

  1. Specify the request name, name prefix, and auto-delete option

  2. Specify the number of instances to reserve

  3. Specify the share type

  4. Create draft requests and submit them




### Specify the request name, name prefix, and auto-delete option

If you're creating multiple future reservation requests at once by generating gcloud CLI commands, then the following properties will have matching values across all requests:

  * Auto-delete option

  * Name prefix

  * Reservation period




You can optionally customize these values for individual requests by editing the generated gcloud CLI commands.

To create future reservation requests for multiple machine types at once, select the gcloud CLI. For individual machine types, select one of the following options:

###  Console 

  1. In the **Usage and forecast by machine types** table, select the machine type that you want to create a future reservation request for, and then click add **Create future reservation**.

The **Create future reservations** page appears.

  2. For **Name** , enter a name for the future reservation request.

  3. For **Prefix** , enter a name prefix. The names of the auto-created reservations for this request will start with this prefix.

  4. For **Start date and time** , enter the start time for the reservation period.

  5. For **End date and time** , enter the end time for the reservation period.

**Important:** Ensure that your reservation period doesn't overlap with existing future reservation requests with matching compute instance properties and zone, and that were created in or are shared with the project in which you want to create your future reservation request. Otherwise, creating the request fails. For more information, see [Overlapping reservation periods](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations#overlapping-reservation-periods).
  6. In the **Auto-generated reservations auto-delete** section, do one of the following:

     * To automatically delete the auto-created reservations after the reservation period ends, regardless if they're fully consumed or not, do the following:

       1. Click the **Enable auto-delete** to the on position, if it isn't already.

       2. For **Auto-delete time** , specify a date and time time with no UTC offset when Compute Engine can automatically delete the auto-created reservations.

     * To prevent the auto-created reservations from being deleted after the reservation period ends, click the **Enable auto-delete** to the off position.

  7. Click **Continue**.




###  gcloud 

  1. In the **Usage and forecast by machine types** table, select the machine types that you want to create a future reservation request for, and then click add **Generate future reservation gcloud commands**.

The **Create future reservations** pane appears.

  2. For **Name** , enter a name for the future reservation requests. If you create more than one request, then Capacity Planner names the requests as NAME-1, NAME-2, continuing up to the number of requests that you're creating.

  3. For **Prefix** , enter a name prefix. The names of the auto-created reservations for your requests will start with this prefix.

  4. For **Start date and time** , enter the start time for the reservation period.

  5. For **End date and time** , enter the end time for the reservation period.

**Important:** Ensure that your reservation period doesn't overlap with existing future reservation requests with matching compute instances properties and zone, and that were created in or are shared with the project in which you want to create your future reservation request. Otherwise, creating the request fails. For more information, see [Overlapping reservation periods](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations#overlapping-reservation-periods).
  6. In the **Auto-generated reservations auto-delete** section, do one of the following:

     * To automatically delete the auto-created reservations after the reservation period ends, regardless if they're fully consumed or not, do the following:

       1. Click the **Enable auto-delete** to the on position, if it isn't already.

       2. For **Auto-delete time** , specify a date and time time with no UTC offset when Compute Engine can automatically delete the auto-created reservations.

     * To prevent the auto-created reservations from being deleted after the reservation period ends, click the **Enable auto-delete** to the off position.

  7. Click **Continue**.




### Specify the number of instances to reserve

To specify the number of compute instances to reserve, do the following:

  1. For **VM count based on** , select the option to base the number of VMs to request.

  2. For **Operator** , select whether to increase or decrease the calculated usage value:

     * To increase the selected usage value, select **(+) Increase**.

     * To decrease the selected usage value, select **(-) Decrease**.

  3. For **Value percentage** , enter the percentage to increase or decrease the calculated usage. This affects the total number of instances to reserve.

  4. Optional: For **Total VM count** , adjust the number of instances to reserve.

  5. Optional: For **Min CPU Platform and Local SSD interface based on historical usage percentage** , specify a minimum CPU platform and Local SSD disk interface. The default is based on the highest percentage of usage in the past 30 days.

**Note:** If the selected machine types have used only one type of minimum CPU platform or Local SSD disk interface interface in the past 30 days, then that type is automatically selected.
  6. Click **Continue**.




### Specify the share type

To specify the share type for your future reservation requests, select the same option that you used in the previous sections:

###  Console 

  1. For **Owner project** , specify the owner project for your request.

  2. To specify the share type for the request, do one of the following:

     * To share a request across multiple projects, do the following:

       1. For **Share type** , select **Project**.

       2. For **Share with** , enter or select the projects to share the request with.

     * To create a single-project request, for **Share type** , select **Local**.




###  gcloud 

  1. Specify the **Owner project** for each request.

  2. To specify the share type for each request, do one of the following:

     * To share a request across multiple projects, do the following:

       1. For **Share type** , select **Project**.

       2. For **Share with** , enter or select the projects to share the request with.

     * To create a single-project request, for **Share type** , select **Local**.




### Create draft requests and submit them

After completing the steps in the previous sections, you can either create draft future reservation requests and submit them later, or immediately submit the requests for review. Google recommends creating a draft request first. This lets you [determine the number of instances](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation) that Compute Engine will provision for your request, and optionally modify the request before submitting it.

To create draft future reservation requests and submit them for review, select the same option that you used in the previous sections:

###  Console 

  1. Click **Save a draft**.

The creation of the draft request can take up to one minute.

  2. To submit the draft request for review, do one of the following:

     * To change one or more properties before submitting, [modify the draft request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations).

     * Otherwise, [submit the request for review](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#submit-review).




###  gcloud 

  1. Click **Generate gcloud commands**.

  2. In the **Generate gcloud commands for future reservations** pane, do the following:

     1. Optional: Edit the generated gcloud CLI commands.

     2. Copy and store the generated gcloud CLI commands. You need them later to create the future reservation requests.

  3. In the Cloud Shell or a command line of your choice, run the commands that you stored in the previous step.

For example, the output for creating two future reservation requests is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/futureReservations/example-fr-1].
         Created [https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-f/futureReservations/example-fr-2].
         

  4. To submit the draft request for review, do one of the following:

     * To change one or more properties before submitting, [modify the draft request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations).

     * Otherwise, [submit the request for review](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#submit-review).




## What's next

  * Learn how to [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

  * Learn how to [consume the automatically created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation) that Compute Engine provisions for a future reservation.

  * Learn how to [cancel or delete future reservation requests](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
