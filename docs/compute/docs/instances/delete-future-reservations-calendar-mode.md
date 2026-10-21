---
url: https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode/
title: Delete a future reservation request in calendar mode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:02:42.445090+00:00
---

# Delete a future reservation request in calendar mode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Delete a future reservation request in calendar mode Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to cancel or permanently delete a future reservation request in calendar mode.

If you no longer need a future reservation request in calendar mode, then you can do one or both of the following:

  * **Cancel the reservation request** : you can cancel a request to prevent Compute Engine from provisioning your requested resources and incurring charges for them. After you cancel a request, you can either retain your request for future reference or delete it.

  * **Delete the reservation request** : after you cancel a request or after the request reaches its end time, you can permanently delete the request to remove the record from your project.




Only the owner project, the project in which a request exists, can cancel or delete a shared request. To learn more about the requirements and limitations that you apply when you cancel or delete a request in calendar mode, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

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

To get the permissions that you need to cancel or delete future reservation requests in calendar mode, ask your administrator to grant you the [Compute Future Reservation Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationAdmin) (`roles/compute.futureReservationAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to cancel or delete future reservation requests in calendar mode. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to cancel or delete future reservation requests in calendar mode:

  * To cancel a future reservation request: `compute.futureReservations.cancel` on the project 
  * To delete a future reservation request: `compute.futureReservations.delete` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cancel a future reservation request in calendar mode

You can cancel a future reservation request in calendar mode if it meets one of the following conditions:

  * The start time is more than 30 days away.

  * You cancel the request within 24 hours after approval, and the start time is at least four days away.




After you cancel your request, Compute Engine deletes the empty reservation created for the request. You can [view the details of your request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations) or delete it.

To cancel multiple future reservation requests in calendar mode, use the Google Cloud console. Otherwise, to cancel a single request, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Select each future reservation request in calendar mode that you want to cancel.

  4. Click cancel **Cancel**.

  5. To confirm, click **Cancel**. Canceling a reservation request can take a few minutes to complete.




###  gcloud 

To cancel a future reservation request in calendar mode, use the [`gcloud compute future-reservations cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/cancel):
    
    
    gcloud compute future-reservations cancel FUTURE_RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of your future reservation request in calendar mode.

  * `ZONE`: the zone where your request exists.




###  REST 

To cancel a future reservation request in calendar mode, make a `POST` request to the [`futureReservations.cancel` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/cancel):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME/cancel
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your future reservation request in calendar mode exists.

  * `ZONE`: the zone where your request exists.

  * `FUTURE_RESERVATION_NAME`: the name of your request.




## Delete a future reservation request in calendar mode

You can only delete a future reservation request in calendar mode after one of the following happens:

  * The request is in the `CANCELLED` state.

  * The request has reached its end time.




To delete multiple future reservation requests in calendar mode simultaneously, use the Google Cloud console. Otherwise, to delete a single request, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Select each future reservation request in calendar mode that you want to delete.

  4. Click delete **Delete**.

  5. To confirm, click **Delete**. Deleting a request can take up to a minute to complete.




###  gcloud 

To delete a future reservation request in calendar mode, use the [`gcloud compute future-reservations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/delete):
    
    
    gcloud compute future-reservations delete FUTURE_RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of your future reservation request in calendar mode.

  * `ZONE`: the zone where your request exists.




###  REST 

To delete a future reservation request in calendar mode, make a `DELETE` request to the [`futureReservations.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your future reservation request in calendar mode exists.

  * `ZONE`: the zone where your request exists.

  * `FUTURE_RESERVATION_NAME`: the name of your request.




## What's next

  * [View reservations or future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view)

  * [Create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
