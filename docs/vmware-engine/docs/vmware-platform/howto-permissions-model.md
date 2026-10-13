---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model/
title: Managing vSphere permissions \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:15.891715+00:00
---

# Managing vSphere permissions  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing vSphere permissions

Some tasks in vSphere require users to have certain permissions in order to complete successfully. When you create a private cloud, VMware Engine performs an [initial setup of vSphere permissions](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model) for your ease of management. This document provides you with guidance on further managing permissions in vSphere.

## Before you begin

To manage vSphere permissions for your private cloud, you must first [elevate your privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege). Elevating your privileges through VMware Engine gives you the ability to perform administrative functions in vSphere.

## Managing vCenter user groups

Users in the `Cloud-Owner-Group` group can administer various parts of the vSphere environment in the private cloud. The `Cloud-Owner-Group` group is automatically given `Cloud-Owner-Role` privileges, and the `CloudOwner` user is added as a member of this group.

Google creates additional groups with limited privileges for ease of management. You can add any user to these pre-created groups, and this process assigns the corresponding privileges to the user.

For a full list of pre-created vCenter user groups and their associated vCenter privileges, see [Private cloud VMware vCenter permission model](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model).

### Granting management permission to individual users

To grant an individual user permissions to manage the private cloud, create a user account and add it to the appropriate groups:

  * `Cloud-Owner-Group`
  * `Cloud-Global-Cluster-Admin-Group`
  * `Cloud-Global-Storage-Admin-Group`
  * `Cloud-Global-Network-Admin-Group`
  * `Cloud-Global-VM-Admin-Group`

**Warning:** Users added to the **Administrators** group are automatically removed. The **Administrators** group must contain only service accounts created by Google.

### Creating new user groups

You can create additional user groups to enable access control for vCenter users. However, new user groups must have permissions that are lower than `Cloud-Owner-Role`. Groups with permissions higher than `Cloud-Owner-Role` are automatically reset to `Cloud-Owner-Role`.

## What's next

  * Learn how to [set up vCenter identity sources](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources).
  * Learn about the [private cloud vSphere permission model](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
