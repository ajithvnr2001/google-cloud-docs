---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-upgrade-guide/
title: Prepare for a vCenter upgrade \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:34.663327+00:00
---

# Prepare for a vCenter upgrade  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-upgrade-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Prepare for a vCenter upgrade Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to prepare for a vCenter version upgrade and the downtime during upgrade.

## Disable auto-repair

Before the vCenter upgrade, [disable `autoRepair`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#disabling_node_repair_and_health_checking_for_a_user_cluster) on all user and admin clusters. This prevents machines from being recreated while vCenter is unavailable.

## Downtime during vCenter upgrade

There shouldn't be any downtime for the admin cluster and user clusters running in the vCenter during upgrade. The clusters remain up the entire time. However, there will be downtime for vCenter services like vMotion/DRS and VM creation.

If your workload directly interacts with vCenter, it might have downtime during the vCenter upgrade due to the vCenter service unavailabilities.

### Major version upgrade

To upgrade vCenter to the next major version, a new Virtual Center Appliance will be deployed. And then all vCenter services are shutdown while it copies all data to the new appliance. Once the data is copied, the new appliance reboots and takes over the identity (hostname/IP/etc) of the old vCenter.

Major version have been seen to have about 30 mins of downtime for the vCenter API.

### Minor version upgrade

The minor version upgrade will just update packages inside the OS and then reboot the appliance, which takes shorter time than major upgrade.

For minor updates, we have seen a downtime around 5 mins for the vCenter API.

## Known Issue

Machines might go to `Unavailable` state after a vCenter reboot for versions < 7.0U2. For more details, see the [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#restarting-or-upgrading-vcenter-for-versions-lower-than-7.0u2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
