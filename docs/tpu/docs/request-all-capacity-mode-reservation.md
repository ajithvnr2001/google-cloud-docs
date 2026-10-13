---
url: https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation/
title: Request TPU capacity in All Capacity mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:07.040459+00:00
---

# Request TPU capacity in All Capacity mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request TPU capacity in All Capacity mode

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

Contact your Google Cloud account team to request an All Capacity mode reservation.

## Request TPU capacity in All Capacity mode with optional project sharing

Contact your account team with the required intake information. Your account team will create a future reservation in draft state for you to review through the Google Cloud console.

You can request a reservation that can be shared across other Google Cloud projects in your organization. You can also request a reservation that can be shared with another Google Cloud service like Vertex AI. Indicate your reservation share preference as part of the intake information you give your account team:

Property | Description  
---|---  
Project number | The [number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) (not ID) of the project where your account team creates the request and Compute Engine provisions the capacity.  
TPU generation | Trillium or Ironwood  
Zone | The zone where you want to reserve capacity.  
Number of chips | The total number of TPU chips to reserve.  
Start time | The start time of the reservation period  
End time | The end time of the reservation period  
Reservation name | The name of the reservation that Compute Engine creates to deliver your reserved capacity  
Reservation automatic deletion | Whether you want Compute Engine to automatically delete the auto-created reservation at the end of the reservation period. If you want to manually delete the reservation, then you must contact your account team to delete the reservation.  
Share type | Whether only your project can use the auto-created reservation (`LOCAL`), or other projects can use the reservation (`SPECIFIC_PROJECTS`). You can't change this setting after you submit the request. To share reserved capacity with other projects in your organization, do the following: 

  1. If you haven't already, verify the project where Google creates the request is [ allowed to create shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).
  2. Provide the IDs of the projects to share the reserved capacity with. You can specify up to 100 projects in your organization.

  
Commitment name | If your reservation period is one year or longer, then Google Cloud creates a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for those resources and attaches the commitment to your reservation. If your reservation period is less than 3 years, then you receive committed use discounts (CUDs) that apply to the 1-year plan for that commitment. If your reservation period is 3 years or more, then you receive CUDs that apply to the 3-year plan. If you share the reserved capacity with other projects, then usage from those projects receive resource-based CUDs only if they use the same [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts) as the project where you reserve capacity. For details, see [Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing). You can't renew, extend, merge, split, or upgrade commitments that you purchased through future reservations for Cloud TPUs.  
  
The following properties are preset for your All Capacity mode reservation:

Property | Description  
---|---  
Maintenance scheduling type | How Compute Engine schedules host maintenance for the VMs in your cluster. All Capacity mode only supports the `GROUPED` option, which means maintenance is synchronized across all TPU VMs in a sub-block of your reservation.  
Reservation operational mode | How Google Cloud manages the VM recovery process after a host error or faulty host report. The reservation operational mode is preset to `ALL_CAPACITY`, which means you must self-manage the maintenance and recovery process for a VM. However, you have full access to all machines in your reservation, as well as more granular control over your VM topology and maintenance.  
Deployment type | Capacity deployment type. All Capacity mode only supports `DENSE`.  
  
## Confirm your capacity reservation draft

You must confirm the draft reservation your account team creates for you in order to receive the All Capacity mode capacity in your Google Cloud project. Follow the instructions from [Review and submit a draft reservation request](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity#review_and_submit_a_draft_reservation_request) to confirm the reservation.

## Check the status of a capacity request

You can determine the status of your All Capacity mode capacity request. If the request is approved, the capacity is allocated at the requested start time for the requested duration. Billing starts at the reservation start time.

For more details, see [View future reservations](https://docs.cloud.google.com/compute/docs/instances/view-future-reservations).

To view the details of a future reservation request, run the following command using the Google Cloud CLI:
    
    
    gcloud compute future-reservations describe RESERVATION_NAME \
        --zone=ZONE

Replace the following:

  * RESERVATION_NAME: the name of your reservation request.
  * ZONE: the zone where Google created the request.



The output is similar to the following:
    
    
    creationTimestamp: '2025-04-01'
    kind: compute#FutureReservation
    name: 'RESERVATION_NAME'
       aggregateReservations:
         vmFamily:VM_FAMILY_CLOUD_TPU_LITE_DEVICE_CT6L
    status:
      lockTime: 2024-03-01T17:00:00Z
      procurementStatus: APPROVED
    timeWindow:
      endTime: 2025-06-01T17:00:00Z
      startTime: 2024-05-01T17:00:00Z
    ...

## Expand an existing capacity request

You can receive additional capacity through an existing reservation. When additional capacity is added, it inherits all of the reservation properties such as reservation sharing policies. You can request a CUD with the additional capacity. The new CUD will point to the same reservation. Your account team will complete the reservation expansion process for you.

## View reservation details from the Google Cloud console

Once your future reservation is fulfilled, you can find it on the Google Cloud console [Reservation page](https://console.cloud.google.com/compute/reservations) and view its details. A TPU reservation with a deployment type `Dense` indicates that it's an All Capacity mode reservation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
