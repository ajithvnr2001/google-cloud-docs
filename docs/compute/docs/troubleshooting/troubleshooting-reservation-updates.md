---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-updates/
title: Troubleshooting reservation updates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:29:08.760993+00:00
---

# Troubleshooting reservation updates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting reservation updates Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with modifying reservations. To learn more about reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview). 

## Attempt to delete a reservation's compact placement policy

The following error occurs when you try to delete a reservation's [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) before deleting the reservation.

**Error message** :
    
    
    The resource_policy resource 'projects/PROJECT_ID/regions/REGION/resourcePolicies/COMPACT_PLACEMENT_POLICY_NAME' is already being used by 'projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME'
    

**Resolution** : To delete a compact placement policy specified in a reservation, select one of the following methods:

  * If you created the reservation by specifying an instance template, follow these steps:

    1. [View the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations) and make note of the reservation's instance template.

    2. [Delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation).

    3. [Delete the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).

**Note:** You can't [update instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#how_to_update_instance_templates). If you delete a compact placement policy specified in an instance template, attempting to use the template to create reservations or virtual machine (VM) instances causes errors.
    4. [Delete the compact placement policy](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#delete-policy).

  * If you created the reservation by specifying properties directly, follow these steps:

    1. [Delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation).

    2. [Delete the compact placement policy](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies#delete-policy).




## Attempt to downsize a specific reservation to less VMs than the targeted number

The following error occurs when you try to decrease the number of reserved VMs in a [specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) to a number that is lower than the number of VMs that consume the reservation.

**Error message** :
    
    
    The resize instance count cannot be lower than the in use count for a specific reservation.
    

**Resolution** : To ensure that the number of VMs in the specific reservation is equal to or lower than the number of VMs that consume the reservation, do one of the following with the VMs in excess:

  * [Delete VMs](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

  * [Stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [suspend the VMs](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)

**Caution:** If you stop or suspend instances in excess instead of deleting them, then those instances no longer count against the reservation, and you can proceed to modify the reservation. However, after you modify the reservation, you can't restart or resume the instances unless you increase the number of instances in the reservation or delete other instances that are consuming it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
