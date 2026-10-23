---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-rebalance-manually/
title: Manually rebalance a regional MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:28.492869+00:00
---

# Manually rebalance a regional MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-rebalance-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually rebalance a regional MIG Stay organized with collections  Save and categorize content based on your preferences. 

A [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) is not balanced if the difference in the number of VMs between two zones is 2 or more VMs. A regional MIG can fall out of balance if you disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution) and then delete or abandon instances to cause an uneven distribution across zones.

If your group is not balanced and you want to re-enable proactive instance distribution, you must first manually rebalance your group to achieve an even distribution of instances across zones.

## Manually rebalance by deleting VMs or resizing the group

You can manually rebalance your group to achieve an even distribution of instances across zones by [deleting](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) VMs from zones with more instances or by [resizing](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) to add instances to zones with fewer VMs until the distribution is even.

When you resize a MIG that has proactive instance redistribution turned off, the group still _opportunistically_ converges toward balance, treating each resize operation as an opportunity to balance the group:

  * When the group grows, the group always tries to add VMs to the zones with the smallest number of VMs.
  * When the group shrinks, the group always removes VMs from the zones with the largest number of VMs.

[ ![](https://docs.cloud.google.com/static/compute/images/rmig-manual-redistribution.svg)](https://docs.cloud.google.com/static/compute/images/rmig-manual-redistribution.svg) _Example of manually resizing a group to achieve even redistribution_

## What's next

  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution) to verify that your instances are evenly distributed across zones.
  * Learn how to re-enable or disable [proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).
  * Learn how to set a regional MIG's [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
