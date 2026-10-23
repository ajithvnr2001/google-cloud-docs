---
url: https://docs.cloud.google.com/tpu/docs/share-reservation/
title: Share a Cloud TPU reservation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.987178+00:00
---

# Share a Cloud TPU reservation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/share-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Share a Cloud TPU reservation

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to share a TPU reservation across multiple projects. Reservation sharing lets you create a Cloud TPU reservation in one project (the owner project) and use that reservation in another project (a consumer project) within the same organization as the owner project. Reservation sharing also lets you run custom training or prediction jobs in Vertex AI using a TPU reservation.

The _owner project_ is the project where you created the reservation. _Consumer projects_ are one or more projects that share the reservation. You can create TPU VMs in the owner project and consumer projects using the reservation in the owner project.

For more information about obtaining a TPU reservation, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

**Note:** Reservation sharing is supported on v4 and later [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

## Limitations

Before you modify a TPU reservation, consider the following:

  * You can modify a shared reservation only from its owner project.

  * You can modify a reservation only as follows:

    * Allow or disallow Vertex AI jobs to consume the reservation.

    * [Modify the share type](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type).




## Convert a single-project reservation into a shared reservation

You can convert a single-project reservation into a shared reservation. Modifying the share type of a TPU reservation helps you share reserved resources with up to 100 projects in your organization. All projects that share a TPU reservation must be part of the same [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#viewing_projects_in_an_organization_resource).

Before you convert a single-project reservation into a shared reservation, verify that you have sufficient quota. There are different quota requirements for shared and single-project reservations. For more information, see [Additional quota requirements for shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations).

To enable sharing of a TPU reservation, do the following:

  1. Grant permission to the owner project to create and modify shared reservations using the [`gcloud resource-manager org-policies allow` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow):
         
         gcloud resource-manager org-policies allow \
             compute.sharedReservationsOwnerProjects \
             projects/OWNER_PROJECT_NUMBER --organization=ORGANIZATION_ID

Replace the following:

     * OWNER_PROJECT_NUMBER: The [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) (not project ID) of a project in your organization that you want to allow to create and modify shared reservations.
     * ORGANIZATION_ID: The [organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) of your organization.
  2. Enable CUD sharing by updating the CUD scope for your Cloud Billing. For instructions, see [Enable CUD sharing for resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).

**Note:** The updated CUD scope takes effect at 12 AM US and Canadian Pacific Time the following day.
  3. To convert a single-project reservation into a shared reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--share-setting=projects` and `--add-share-with` flags:
         
         gcloud compute reservations update RESERVATION_NAME \
             --project=OWNER_PROJECT_ID \
             --share-setting=projects \
             --add-share-with=CONSUMER_PROJECT_IDS \
             --zone=ZONE

Replace the following:

     * RESERVATION_NAME: The name of the reservation.
     * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
     * CONSUMER_PROJECT_IDS: A comma-separated list of IDs of projects that can consume this reservation. For example, `project-1,project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the owner project. By default, the owner project is already allowed to consume the reservation.
     * ZONE: The zone where the reservation is located.



## Convert a shared reservation into a single-project reservation

To convert a [specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation) from a shared reservation into a single-project reservation, you must stop or delete any instances that are consuming the reservation in each project that the reservation is shared with. This requirement doesn't apply to the instances in the owner project.

To stop sharing a TPU reservation with all consumer projects, change the shared reservation to a single-project reservation using the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--share-setting=local` flag:
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --share-setting=local \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * ZONE: The zone where the reservation is located.



## Modify the consumer projects in a shared reservation

To avoid errors when you modify the consumer projects for a shared reservation, consider the following:

  * **Removal of projects** : you can remove consumer projects from a shared reservation only if those projects are not using the reserved resources. To stop instances from consuming a reservation, [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [delete the instances](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  * **Addition of projects** : you can allow consumer projects to consume a shared reservation only if these projects are in the same organization as the owner project. To migrate a project to the owner project's organization, see [Migrating projects between organization resources](https://docs.cloud.google.com/resource-manager/docs/project-migration) in the Resource Manager documentation.




### Add projects to a shared reservation

To add one or more projects to a shared reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--add-share-with` flag:
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --add-share-with=CONSUMER_PROJECT_IDS \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * CONSUMER_PROJECT_IDS: A comma-separated list of project IDs with which to share the reservation. For example, `project-1,project-2`.
  * ZONE: The zone where the reservation is located.



### Remove projects from a shared reservation

To remove one or more projects from a shared reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--remove-share-with` flag:
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --remove-share-with=CONSUMER_PROJECT_IDS \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * CONSUMER_PROJECT_IDS: A comma-separated list of project IDs that you want to stop sharing the reservation with. For example, `project-1,project-2`.
  * ZONE: The zone where the reservation is located.



### Replace the list of projects that can consume a shared reservation

To replace the list of projects that can consume a shared reservation, use the [`gcloud beta compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update) with the `--share-with` flag:
    
    
    gcloud beta compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --share-with=CONSUMER_PROJECT_IDS \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * CONSUMER_PROJECT_IDS: A comma-separated list of project IDs with which to share the reservation. For example, `project-1,project-2`.
  * ZONE: The zone where the reservation is located.



## Allow Vertex AI to use a TPU reservation

You can allow [training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI to consume a TPU reservation only after its start time.

To allow Vertex AI to consume a TPU reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--reservation-sharing-policy=ALLOW_ALL` flag:
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --zone=ZONE \
        --reservation-sharing-policy=ALLOW_ALL

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * ZONE: The zone of the reservation.



## Disallow Vertex AI from using a TPU reservation

Before you disallow Vertex AI from consuming a TPU reservation, stop any Vertex AI jobs that use it. Otherwise, you encounter errors.

To disallow Vertex AI from consuming a TPU reservation, use the [`gcloud compute reservations update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) command with the `--reservation-sharing-policy=DISALLOW_ALL` flag:
    
    
    gcloud compute reservations update RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --zone=ZONE \
        --reservation-sharing-policy=DISALLOW_ALL

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * ZONE: The zone of the reservation.



## Get information about a shared reservation

You can get information about a shared reservation only from its owner project.

To get information about a shared reservation, use the [`gcloud compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/describe):
    
    
    gcloud compute reservations describe RESERVATION_NAME \
        --project=OWNER_PROJECT_ID \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of the reservation.
  * OWNER_PROJECT_ID: The ID of the project that contains the reservation.
  * ZONE: The zone of the reservation.



The response is similar to the following:
    
    
    aggregateReservation:
    [...]
    name: RESERVATION_NAME
    reservationSharingPolicy:
      **serviceShareType: ALLOW_ALL**
    resourceStatus: {}
    selfLink: https://www.googleapis.com/compute/v1/projects/OWNER_PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME
    shareSettings:
      **projectMap:    'CONSUMER_PROJECT_1':
          projectId: 'CONSUMER_PROJECT_1'
        'CONSUMER_PROJECT_2':
          projectId: 'CONSUMER_PROJECT_2'
      shareType: SPECIFIC_PROJECTS**
    specificReservationRequired: true
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/OWNER_PROJECT_ID/zones/ZONE

## What's next

  * [Learn about Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations)
  * [Consume your reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute)
  * [Manage your TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
