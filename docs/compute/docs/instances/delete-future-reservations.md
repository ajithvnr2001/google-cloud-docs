---
url: https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations/
title: Cancel or delete future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:43:17.788441+00:00
---

# Cancel or delete future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Cancel or delete future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to cancel or delete future reservation requests.

Before a future reservation request reaches its [lock time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#lock-time), you can prevent Compute Engine from provisioning the requested resources by doing one of the following:

  * **Cancel the future reservation request**. This is useful to keep the canceled request for reference when creating new requests. However, a canceled future reservation request prevents you from creating new requests with properties that match the canceled request in your project, or in the projects that the request is shared with, until you delete it. For more information, see [Restrictions on creation](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions-create).

  * **Delete the future reservation request**. This is useful when you no longer need the request. Deleting a future reservation request permanently deletes it and removes any restrictions on creating new requests.




After a fulfilled future reservation reaches the end of its reservation period, you can delete it to remove any restrictions on creating new requests. However, deleting a fulfilled future reservation doesn't delete its auto-created reservations. To delete an auto-created reservation after its reservation period ends, see [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).

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

To get the permissions that you need to cancel or delete future reservation requests, ask your administrator to grant you the [Compute Future Reservation Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationAdmin) (`roles/compute.futureReservationAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to cancel or delete future reservation requests. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to cancel or delete future reservation requests:

  * To cancel a future reservation: `compute.futureReservations.cancel` on the project 
  * To delete a future reservation: `compute.futureReservations.delete` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cancel future reservation requests

You can only cancel a future reservation request in the following cases:

  * The request is pending approval or has been declined.

  * The request was approved, but its state hasn't changed to `PROCURING` yet.




After you cancel a future reservation request, you can only [view its details](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations) or delete it.

**Important:** As long as a canceled request exists, it prevents you from creating new requests with properties that match the canceled requests in your project, or in any of the projects that the canceled request is shared with. To create new requests with properties that match the canceled request, delete the canceled request before creating new ones.

To cancel a future reservation request, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Select each future reservation request that you want to cancel.

  4. Click cancel **Cancel**.

  5. To confirm, click **Cancel**. Canceling a reservation request can take a few minutes to complete.




###  gcloud 

To cancel a future reservation request, use the [`gcloud compute future-reservations cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/cancel).
    
    
    gcloud compute future-reservations cancel FUTURE_RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.

  * `ZONE`: the zone where the future reservation request is located.




###  REST 

To cancel a future reservation request, make a `POST` request to the [`futureReservations.cancel` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/cancel).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME/cancel
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the future reservation request is located.

  * `ZONE`: the zone where the future reservation request is located.

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.




## Delete future reservation requests

You can only delete a future reservation request in the following cases:

  * The request hasn't reached its lock time yet (`PROCURING`) and isn't pending approval.

  * The request was fulfilled and its reservation period has ended.




To delete a future reservation request that is pending approval, you must cancel the request before deleting it.

Deleting a fulfilled future reservation doesn't delete its auto-created reservations. To delete an auto-created reservation after its reservation period ends, see [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation).

To delete multiple future reservation requests simultaneously, use the Google Cloud console. Otherwise, to delete a single future reservation request, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Select each future reservation request that you want to delete.

  4. Click delete **Delete reservation**.

  5. To confirm, click **Delete**.

Deleting a future reservation request can take up to a minute to complete.




###  gcloud 

To delete a future reservation request, use the [`gcloud compute future-reservations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/delete).
    
    
    gcloud compute future-reservations delete FUTURE_RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.

  * `ZONE`: the zone where the future reservation request is located.




###  REST 

To delete a future reservation request, make a `DELETE` request to the [`futureReservations.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the future reservation request is located.

  * `ZONE`: the zone where the future reservation request is located.

  * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.




## What's next

  * Learn how to [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
