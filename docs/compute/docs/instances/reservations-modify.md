---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-modify/
title: Modify reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:18:28.405218+00:00
---

# Modify reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-modify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Modify reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to modify reservations. To modify reservations that are attached to commitments, see instead [Replace reservations that are attached to commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#modifying_reservations_that_are_attached_to_commitments).

Modify a reservation when, for example, your capacity needs change or you want to change which workloads can consume a reservation.

## Limitations

Before you modify a reservation, consider the following:

  * You can modify a shared reservation only from the project in which you or Compute Engine created it.

  * You can modify an auto-created reservation for a future reservation only after the following occurs:

    * For a future reservation in calendar mode or for capacity blocks, you can modify the auto-created reservation at any time.

    * For a future reservation, you can modify the auto-created reservation only after its end time.

  * You can modify an auto-created reservation for a future reservation in calendar mode or for capacity blocks only as follows:

    * Allow or disallow Vertex AI jobs from consuming reserved resources

    * Modify the share type




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

To get the permissions that you need to modify reservations, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to modify reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to modify reservations:

  * To modify the auto-delete option in a reservation, the consumer projects in a shared reservation, or whether Vertex AI jobs can consume a reservation of instances with attached GPUs: `compute.reservations.update` on the project 
  * To modify the number of instances in a reservation: `compute.reservations.resize` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Modify reservations

Based on the properties that you want to modify in a reservation, use one of the following methods:

  * To enable or disable the automatic deletion of a reservation, or change the date and time when Compute Engine automatically deletes the reservation, modify the automatic deletion of a reservation.

  * To add or remove consumer projects that can consume a shared reservation, modify the consumer projects in a shared reservation.

  * To increase or decrease the number of reserved Compute Engine instances in a reservation, modify the number of reserved compute instances in a reservation.

  * To allow or disallow a reservation of GPU instances to be consumed by custom training jobs or prediction jobs in Vertex AI, modify the sharing policy of a reservation.

  * To switch between a single-project reservation and a shared reservation, modify the share type of a reservation.




To change any properties that aren't mentioned in this list, you must create a new reservation. For instructions, see Change other properties in a reservation in this document.

### Modify the automatic deletion of a reservation

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can modify when Compute Engine automatically deletes an existing reservation by doing one of the following:

  * Enable the [auto-delete option](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete) or change when the reservation is automatically deleted.

  * Disable the auto-delete option.




To modify the automatic deletion of a reservation, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), in the **Name** column, click the name of the reservation that you want to modify.

The details page of the reservation opens.

  3. In the **Auto-delete time** row, click edit **Edit auto-delete time**.

  4. In the **Update reservation** pane, do one of the following:

     * To delete the reservation at a specific date and time, do the following:

       1. If the auto-delete option isn't already enabled, click the **Enable auto-delete** toggle to the on position.

       2. In the **Auto-delete time** field, enter a date and time when Compute Engine automatically deletes the reservation.

     * Otherwise, click the **Enable auto-delete** toggle to the off position.

  5. Click **Submit**.

Modifying your reservation might take a few seconds to complete.




###  gcloud 

When you enable the auto-delete option in a reservation, you can specify a date and time when the reservation should be deleted or specify a duration after which the reservation should be deleted.

To enable the auto-delete option or change when the reservation should be deleted, do one of the following:

  * To delete the reservation at a specific date and time, use the [`gcloud beta compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update) with the `--delete-at-time` flag.
        
        gcloud beta compute reservations update RESERVATION_NAME \
            --delete-at-time=DELETE_AT_TIME \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing reservation.

    * `DELETE_AT_TIME`: a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339).

    * `ZONE`: the zone where the reservation is located.

  * To delete the reservation after a specific duration, use the [`gcloud beta compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update) with the `--delete-after-duration` flag.
        
        gcloud beta compute reservations update RESERVATION_NAME \
            --delete-after-duration=DELETE_AFTER_DURATION \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing reservation.

    * `DELETE_AFTER_DURATION`: a duration in days, hours, minutes, or seconds before the reservation is automatically deleted. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.

    * `ZONE`: the zone where the reservation is located.




To disable the auto-delete option, use the [`gcloud beta compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update) with the `--disable-auto-delete` flag.
    
    
    gcloud beta compute reservations update RESERVATION_NAME \
        --disable-auto-delete \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of an existing reservation.

  * `ZONE`: the zone where the reservation is located.




###  REST 

When you enable the auto-delete option in a reservation, you can specify a date and time when the reservation should be deleted or specify a duration after which the reservation should be deleted.

To enable the auto-delete option or change when the reservation should be deleted, do one of the following:

  * To delete the reservation at a specific date and time, make a `PATCH` request to the [`beta.reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/update). In the request URL, include the `paths` query parameter set to `deleteAtTime`.
        
        PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=deleteAtTime
        
        {
          "name": "RESERVATION_NAME",
          "deleteAtTime": "DELETE_AT_TIME"
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where the reservation is located.

    * `ZONE`: the zone where the reservation is located.

    * `RESERVATION_NAME`: the name of an existing reservation.

    * `DELETE_AT_TIME`: a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339).

  * To delete the reservation after a specific duration, make a `PATCH` request to the [`beta.reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/update). In the request URL, include the `paths` query parameter set to `deleteAfterDuration.seconds`.
        
        PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=deleteAfterDuration.seconds
        
        {
          "name": "RESERVATION_NAME",
          "deleteAfterDuration": {
            "seconds": "DELETE_AFTER_DURATION"
          }
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where the reservation is located.

    * `ZONE`: the zone where the reservation is located.

    * `RESERVATION_NAME`: the name of an existing reservation.

    * `DELETE_AFTER_DURATION`: a duration in seconds before the reservation is automatically deleted. For example, specify `86400` for 86,400 seconds (1 day).




To disable the auto-delete option, make a `PATCH` request to the [`beta.reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/update). In the request, specify the `paths=deleteAtTime&paths=deleteAfterDuration` query parameter and omit the request body.
    
    
    PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=deleteAtTime&paths=deleteAfterDuration
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation is located.

  * `ZONE`: the zone where the reservation is located.

  * `RESERVATION_NAME`: the name of an existing reservation.




### Modify the consumer projects in a shared reservation

To avoid errors when you modify the consumer projects for a shared reservation, consider the following:

  * **Removal of projects** : you can disallow consumer projects from consuming a shared reservation only if no compute instances in those projects consume the reservation. To stop instances from consuming a reservation, [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [delete the instances](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  * **Addition of projects** : you can allow consumer projects to consume a shared reservation only if these projects are in the same organization as the owner project. To migrate a project to the owner project's organization, see [Migrating projects between organization resources](https://docs.cloud.google.com/resource-manager/docs/project-migration) in the Resource Manager documentation.




After you modify the consumer projects for a shared reservation, the consumption of the reservation might change. For example, if you configured the reservation to let any matching instances consume it (the default configuration), then any newly added consumer projects might immediately start consuming the reservation. To learn more about which matching reservations projects consume first, see the [reservations consumption order](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type).

To modify the consumer projects that can consume a shared reservation, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), in the **Name** column, click the name of the reservation you want to describe.

The details page for the reservation opens.

  3. Click edit **Edit**.

  4. In the **Selected projects** section, do one of the following:

     * To stop sharing the reservation with a specific consumer project, click delete **Delete**.

     * To start sharing the reservation with one or more specific projects, do the following:

       1. Click add **Add projects**.

       2. Select the checkbox for each project from the owner project's organization that you want to share the reservation with. You can share a shared reservation with up to 100 consumer projects.

       3. Click **Select**.

  5. To confirm your changes, click **Save**.

Modifying your reservation might take a few seconds to complete.




###  gcloud 

When you modify the consumer projects for a shared reservation, you must specify a comma-separated list of IDs of projects that you want to allow, or stop allowing, to consume the shared reservation. All consumer projects must belong to the same organization as the owner project. Don't specify the owner project; by default, the owner project of a shared reservation can always consume it.

To modify the consumer projects for a shared reservation, do one of the following:

  * To allow one or more projects to consume a shared reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--add-share-with` flag.
        
        gcloud compute reservations update RESERVATION_NAME \
            --add-share-with=CONSUMER_PROJECT_IDS \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing shared reservation.

    * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects to share the reservation with—for example, `project-1,project-2`. You can share a shared reservation with up to 100 consumer projects.

    * `ZONE`: the zone where the shared reservation is located.

  * To stop allowing one or more projects to consume a shared reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--remove-share-with` flag.
        
        gcloud compute reservations update RESERVATION_NAME \
            --remove-share-with=CONSUMER_PROJECT_IDS \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing shared reservation.

    * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects that you want to stop sharing the reservation with—for example, `project-1,project-2`.

    * `ZONE`: the zone where the shared reservation is located.

  * To replace the list of projects that can consume a shared reservation, use the [`gcloud beta compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update) with the `--share-with` flag.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        gcloud beta compute reservations update RESERVATION_NAME \
            --share-with=CONSUMER_PROJECT_IDS \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing shared reservation.

    * `ZONE`: the zone where the shared reservation is located.

    * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects to share the reservation with—for example, `project-1,project-2`. You can share a shared reservation with up to 100 consumer projects.




###  REST 

When you modify the consumer projects for a shared reservation, you must specify the projects that you want to add or remove. To allow a project to consume the reservation, specify either the project ID or the project number. To disallow a project from consuming the reservation, you must specify the project number. All consumer projects must belong to the same organization as the owner project. Don't specify the owner project; by default, the owner project of a shared reservation can always consume it.

To modify the consumer projects for a shared reservation, do one of the following:

  * To allow one or more projects to consume a shared reservation, make a `PATCH` request to the [`reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/update). In the request URL, include the `paths=shareSettings.projectMap.PROJECT_ID_OR_NUMBER` query parameter for each project that you want to share the reservation with.

For example, to allow two projects to consume a shared reservation, make a `PATCH` request as follows. You can share a shared reservation with up to 100 consumer projects.
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_1&paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_2
        
        {
          "name": "RESERVATION_NAME",
          "shareSetting": {
            "projectMap": {
              "CONSUMER_PROJECT_ID_OR_NUMBER_1": {
                "projectId": "CONSUMER_PROJECT_ID_OR_NUMBER_1"
              },
              "CONSUMER_PROJECT_ID_OR_NUMBER_2": {
                "projectId": "CONSUMER_PROJECT_ID_OR_NUMBER_2"
              }
            }
          }
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project in which the shared reservation exists (the owner project).

    * `ZONE`: the zone where the shared reservation exists.

    * `RESERVATION_NAME`: the name of an existing shared reservation.

    * `CONSUMER_PROJECT_ID_OR_NUMBER_1` and `CONSUMER_PROJECT_ID_OR_NUMBER_2`: the ID or number of the two projects that you want to share the reservation with.

  * To stop allowing one or more projects to consume a shared reservation, make a `PATCH` request to the [`reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/update). In the request URL, include the `paths=shareSettings.projectMap.PROJECT_NUMBER` query parameter for each project that you want to stop sharing the reservation with. Additionally, you must omit the `shareSetting` field from the request body.

For example, to stop allowing two projects to consume a shared reservation, make a `PATCH` request as follows:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_1&paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_2
        
        {
          "name": "RESERVATION_NAME"
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project in which the shared reservation exists (the owner project).

    * `ZONE`: the zone where the shared reservation exists.

    * `RESERVATION_NAME`: the name of an existing shared reservation.

    * `CONSUMER_PROJECT_NUMBER_1` and `CONSUMER_PROJECT_NUMBER_2`: the numbers of the two projects that you want to stop sharing the reservation with.




### Modify the number of reserved instances in a reservation

You can increase or decrease the number of reserved compute instances in a reservation. However, before you modify the number of instances, consider the following to avoid errors:

  * To increase the number of instances in any reservation, ensure the following:

    * You can't exceed the [maximum instance count for a reservation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation#max-vm-count-exceeded).

    * You must have enough unused quota for the additional resources to reserve. To increase quota, see [View and manage quotas](https://docs.cloud.google.com/compute/resource-usage#vm_instance_quota) in the Cloud Quotas documentation.

    * There must be enough resources available in the zone of the reservation. If not, then your request fails with a resource availability error. To troubleshoot this error, see [Troubleshooting resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability).

  * To decrease the number of instances in a [specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), ensure that the number of instances that consume the reservation doesn't exceed the new, smaller number. If it does, then do one of the following with the instances in excess of the new number:

    * [Delete instances](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

    * [Stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [suspend the instances](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)

**Caution:** If you stop or suspend instances in excess instead of deleting them, then those instances no longer count against the reservation, and you can proceed to modify the reservation. However, after you modify the reservation, you can't restart or resume the instances unless you increase the number of instances in the reservation or delete other instances that are consuming it. 



To modify the number of reserved instances in a reservation, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), in the **Name** column, click the name of the reservation that you want to modify.

The details page for the reservation opens.

  3. Click edit **Edit**.

  4. In the **Number of VM instances** field, enter the updated number of instances to reserve.

  5. To confirm, click **Save**.

Modifying your reservation might take a few seconds to complete.




###  gcloud 

To modify the number of reserved instances in a reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update).
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --vm-count=NUMBER_OF_VMS \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of an existing reservation.

  * `NUMBER_OF_VMS`: the new number of instances to reserve.

  * `ZONE`: the zone where the reservation is located.




###  REST 

To modify the number of reserved instances in a reservation, make a `POST` request to the [`reservations.resize` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/resize).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/resize
    
    {
      "specificSkuCount": "NUMBER_OF_VMS"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation is located.

  * `ZONE`: the zone where the reservation is located.

  * `RESERVATION_NAME`: the name of an existing reservation.

  * `NUMBER_OF_VMS`: the new number of instances to reserve.




### Modify the sharing policy of a reservation

When you modify the [sharing policy](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#sharing-policy) of a reservation of GPU compute instances, you control whether Vertex AI training or prediction jobs consume the reservation.

Before you disallow Vertex AI jobs from consuming a reservation, stop any Vertex AI jobs that use it. Otherwise, you encounter errors.

To modify the sharing policy of a reservation of GPU instances, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), in the **Name** column, click the name of the reservation of GPU instances that you want to modify. A page that gives the details of the reservation appears.

  3. In the **Share with other Google Cloud services** row, click edit **Edit service sharing settings**.

  4. In the **Reservation sharing** pane, do one of the following:

     * To allow Vertex AI jobs to consume the reservation, select **Share reservation**.

     * To disallow Vertex AI jobs to consume the reservation, select **Don't share reservation**.

  5. Click **Save**.

Modifying your reservation might take a few seconds to complete.




###  gcloud 

To modify the sharing policy of a reservation of GPU instances, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--reservation-sharing-policy` flag.
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --reservation-sharing-policy=SHARING_POLICY \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of an existing reservation.

  * `SHARING_POLICY`: the sharing policy of the reservation. Specify one of the following values:

    * To allow Vertex AI jobs to consume the reservation: `ALLOW_ALL`

    * To disallow Vertex AI jobs to consume the reservation: `DISALLOW_ALL`

  * `ZONE`: the zone where the reservation exists




###  REST 

To modify the sharing policy of a reservation of GPU instances, make a `PATCH` request to the [`reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/update). In the request URL, include the `paths` query parameter set to `reservationSharingPolicy.serviceShareType`.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=reservationSharingPolicy.serviceShareType
    
    {
      "name": "RESERVATION_NAME",
      "reservationSharingPolicy": {
        "serviceShareType": "SHARING_POLICY"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation exists.

  * `ZONE`: the zone where the reservation exists.

  * `RESERVATION_NAME`: the name of an existing reservation.

  * `SHARING_POLICY`: the sharing policy of the reservation. Specify one of the following values:

    * To allow Vertex AI jobs to consume the reservation: `ALLOW_ALL`

    * To disallow Vertex AI jobs to consume the reservation: `DISALLOW_ALL`




### Modify the share type for a reservation

You can convert a single-project reservation into a shared reservation, or a shared reservation into a single-project reservation. When you modify the share type for a reservation, you can share reserved resources with up to 100 projects in your organization or restrict access to only the owner project.

Before you modify the share type for a reservation, consider the following to avoid errors:

  * To convert a single-project reservation into a shared reservation, check the following:

    * **Project permissions** : verify that your project can create shared reservations. For instructions, see [Allow or restrict projects from creating shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation#allow-restrict-projects).

    * **Quota limits** : if the reservation type requires quota, then you might need additional quota for your reserved resources. Shared reservations and single-project reservations have different quota requirements. For more information, see [Additional quota requirements for shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations).

  * To convert a shared reservation into a single-project reservation, check the following:

    * **Consumer compute instances** : to modify a [specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation), you must stop, suspend, or delete any compute instances that are consuming the reservation in each project that the reservation is shared with (the consumer projects). This requirement doesn't apply to the compute instances in the owner project.

**Caution:** If you stop or suspend compute instances in a consumer project that target a shared reservation, then you can't restart or resume those compute instances until you create a replacement reservation. To restart or resume the compute instances, you must create a new reservation in the same owner project and zone, and with the same name and matching properties, as the original reservation.



To modify the share type for a reservation, select one of the following options:

###  gcloud 

To modify the share type for a reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update).

Based on how you want to modify your reservation, include one of the following flags:

  * To convert a single-project reservation into a shared reservation, include the `--add-share-with` and `--share-setting=projects` flags:
        
        gcloud compute reservations update RESERVATION_NAME \
            **--add-share-with= CONSUMER_PROJECT_IDS** \
            **--share-setting=projects** \
            --zone=ZONE
        

  * To convert a shared reservation into a single-project reservation, include the `--share-setting=local` flag:
        
        gcloud compute reservations update RESERVATION_NAME \
            **--share-setting=local** \
            --zone=ZONE
        




Replace the following:

  * `RESERVATION_NAME`: the name of the reservation that you want to modify.

  * `CONSUMER_PROJECT_IDS`: a comma-separated list of IDs of projects to share the reservation with—for example, `project-1,project-2`. You can share a reservation with up to 100 projects that are in the same organization as the owner project.

  * `ZONE`: the zone where the reservation exists.




###  REST 

To modify the share type for a reservation, make a `PATCH` request to the [`reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/update).

Based on how you want to modify your reservation, make one of the following requests:

  * To convert a single-project reservation into a shared reservation, make a request as follows. In the request URL, include the `paths=shareSettings.projectMap.PROJECT_ID_OR_NUMBER` query parameter for each project that you want to share the reservation with.

For example, to share a reservation with two projects, make a request as follows. You can share a reservation with up to 100 projects that are in the same organization as the owner project.
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=shareSettings.shareType&paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_1&paths=shareSettings.projectMap.CONSUMER_PROJECT_NUMBER_2
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_OR_NUMBER_1": {
                "projectId": "CONSUMER_PROJECT_ID_OR_NUMBER_1"
              },
              "CONSUMER_PROJECT_ID_OR_NUMBER_2": {
                "projectId": "CONSUMER_PROJECT_ID_OR_NUMBER_2"
              }
            }
          }
        }
        

  * To convert a shared reservation into a single-project reservation, make a request as follows:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=shareSettings.shareType
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "LOCAL"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project in which the reservation exists (the owner project).

  * `ZONE`: the zone where the reservation exists.

  * `RESERVATION_NAME`: the name of the reservation that you want to modify.

  * `CONSUMER_PROJECT_ID_OR_NUMBER_1` and `CONSUMER_PROJECT_ID_OR_NUMBER_2`: the ID or number of the two projects that you want to share the reservation with.




### Change other properties in a reservation

If you want to modify a property that isn't mentioned in the [Modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modifying_reservations) section, then you must create a replacement reservation instead.

To replace a reservation without risking an unintended reduction in your reserved capacity, do the following:

  1. Create a new [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#creating_a_reservation) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#creating_a_reservation) with updated properties.

  2. If you don't need the original reservation anymore, then [delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation).




## Troubleshoot

Learn how to [troubleshoot issues with reservation updates](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-updates).

## What's next

  * Learn how to [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view).

  * Learn how to [consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).

  * Learn how to [delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
