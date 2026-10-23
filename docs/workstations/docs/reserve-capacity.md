---
url: https://docs.cloud.google.com/workstations/docs/reserve-capacity/
title: Reserve capacity for your workstation \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:45.391220+00:00
---

# Reserve capacity for your workstation  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/reserve-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Reserve capacity for your workstation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Reserve capacity for your workstation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Compute Engine reservations provide a high level of assurance in obtaining capacity for Compute Engine virtual machine (VM) instances. Reservations help ensure that capacity for VMs with specific properties, such as machine type, is held for your project.

When you create a reservation, you help protect your workloads from errors caused by insufficient capacity. For more information, see the Compute Engine [Reservations overview](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

This document describes how to configure your workstation configurations to consume reserved capacity by setting a reservation affinity. In the API, these affinity parameters are collectively referred to as [`ReservationAffinity`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#reservationaffinity).

## Before you begin

  * [Create a Compute Engine reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project). The reservation must be in the same project and region, and target the same zone, as your workstation cluster.
  * The reservation's machine properties (for example, machine type) **must match** the properties you intend to use in the workstation configuration.



## How reservation affinity works

You can control how a workstation configuration consumes reserved capacity by specifying its reservation affinity. There are three modes:

  * **Specific reservation:** The configuration uses capacity _only_ from a specific matching reservation. You target this reservation using the `--reservation-affinity` flag with `consume-reservation-type=specific-reservation`.
  * **No reservation:** The configuration is prevented from using capacity from _any_ reservation. You set this using the `--reservation-affinity` flag with `consume-reservation-type=no-reservation`.
  * **Any matching reservation (default):** By default, if you don't specify a reservation affinity, Cloud Workstations uses capacity from _any_ matching reservations available in the project. This behavior occurs because the underlying Compute Engine instances default to using any matching reservation.



## Configure reservation affinity

To control reservation usage, you specify the `--reservation-affinity` flag when creating or updating a workstation configuration.

### Consume a specific reservation

To create a workstation configuration that consumes capacity only from a specific named reservation, run the following `gcloud` CLI command:
    
    
    gcloud beta workstations configs create WORKSTATION_CONFIG_ID \
        --cluster=WORKSTATION_CLUSTER_ID \
        --region=REGION \
        --project=PROJECT_ID \
        --machine-type=MACHINE_TYPE \
        --reservation-affinity=consume-reservation-type=specific-reservation,key=compute.googleapis.com/reservation-name,values=RESERVATION_NAME
    

Replace the following:

  * `WORKSTATION_CONFIG_ID`: the ID of the workstation configuration.
  * `WORKSTATION_CLUSTER_ID`: the ID of the workstation cluster.
  * `REGION`: the region of the workstation cluster.
  * `PROJECT_ID`: the ID of the project.
  * `MACHINE_TYPE`: the machine type for the VMs in the workstation configuration—for example, `e2-standard-4`. This machine type **must match** the machine type of the reservation.
  * `RESERVATION_NAME`: the name of the specific Compute Engine reservation to use capacity from.



If you configure workstations to consume a specific reservation, workstations started using this configuration draw capacity only from that reservation. If the reservation runs out of capacity, the configuration will be degraded until capacity becomes available in the reservation.

### Prevent using any reservation

To create a workstation configuration that does not use capacity from any reservation, use `--reservation-affinity=consume-reservation-type=no-reservation`:
    
    
    gcloud beta workstations configs create WORKSTATION_CONFIG_ID \
        --cluster=WORKSTATION_CLUSTER_ID \
        --region=REGION \
        --project=PROJECT_ID \
        --machine-type=MACHINE_TYPE \
        --reservation-affinity=consume-reservation-type=no-reservation
    

You can use the same variable replacements as listed in the previous section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
