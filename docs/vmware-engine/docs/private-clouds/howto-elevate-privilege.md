---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege/
title: Elevate VMware Engine privileges \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:20.874232+00:00
---

# Elevate VMware Engine privileges  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Elevate VMware Engine privileges

Google Cloud VMware Engine privileges give vCenter users the privileges they need to perform normal operations. Some administrative functions require additional privileges in the private cloud vCenter.

Google Cloud VMware Engine is now integrated with the Google Cloud console but the integration does not provide the **Elevate privilege** feature. To perform these tasks, you can use a solution user account to:

  * Configure identity sources
  * Perform user management
  * Delete a distributed port group
  * Create service accounts



## Solution user accounts

Some tools and products used with your private cloud might require a user to have administrative privileges in vSphere. When you create a private cloud, VMware Engine also creates user accounts with administrative privileges that you can use for the third-party tools and products. Multiple solution user accounts are created for managing different applications. Using a specific solution user account, you can audit the actions performed by each application. This document provides you with guidance on managing these solution user accounts in vSphere.

Here are some examples of tools and products that require administrative privileges during setup:

  * VMware Site Recovery Manager (SRM)
  * VMware Cloud Director
  * Zerto

**Note:** If you want to disable or re-enable all solution user accounts, contact [Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/support).

## Before you begin

Before signing in to a third-party tool or product with a solution user account, confirm that the tool or product requires administrative privileges. If the tool or product requires [privileges](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model) that are already provided by `Cloud-Owner-Role`, then [create a new user](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model) and add the user to `Cloud-Owner-Group` instead.

**Caution:** Solution user accounts have administrator privileges in vSphere. Only use solution user accounts for their intended purpose. VMware Engine reverts [forbidden actions](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#forbidden-actions) taken by these accounts automatically because of their potential for adverse impact on your private cloud.

You can use any of the following built-in solution user IDs:

  * `solution-user-01@gve.local`
  * `solution-user-02@gve.local`
  * `solution-user-03@gve.local`
  * `solution-user-04@gve.local`
  * `solution-user-05@gve.local`



## Get a solution user password

To get a solution user password, take the following steps.

###  gcloud 
    
    
    gcloud vmware private-clouds vcenter credentials describe \
      --private-cloud=PRIVATE_CLOUD_NAME \
      --project=PROJECT_ID \
      --username=USERNAME_ID \
      --location=ZONE
    

Replace the following:

  * `PRIVATE_CLOUD_NAME`: the private cloud for this request
  * `PROJECT_ID`: the project for this request
  * `USERNAME_ID`: one of the solution user IDs
  * `ZONE`: the zone of the private cloud



###  API 

In the REST API, make a `GET` request to the `showVcenterCredentials` method and provide the provide the solution user ID:
    
    
    https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_NAME:showVcenterCredentials?username=USERNAME_ID
    

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone of the private cloud
  * `PRIVATE_CLOUD_NAME`: the private cloud for this request
  * `USERNAME_ID`: one of the solution user IDs



## Reset solution user password

To reset a solution user password, take the following steps.

###  gcloud 
    
    
    gcloud vmware private-clouds vcenter credentials reset \
      --private-cloud=PRIVATE_CLOUD_NAME \
      --project=PROJECT_ID \
      --username=USERNAME_ID \
      --location=ZONE
    

Replace the following:

  * `PRIVATE_CLOUD_NAME`: the private cloud for this request
  * `PROJECT_ID`: the project for this request
  * `USERNAME_ID`: one of the solution user IDs
  * `ZONE`: the zone of the private cloud



###  API 

In the REST API, make a `POST` request to the `resetVcenterCredentials` method and provide the solution user ID in the request body:
    
    
    https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_NAME:resetVcenterCredentials
    
    {
      "username": :"USERNAME_ID"
    }
    

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone of the private cloud
  * `USERNAME_ID`: one of the solution user IDs



## Forbidden actions

When VMware Engine detects any of the following forbidden actions, VMware Engine reverts the changes to ensure that service remains uninterrupted whenever possible. Performing a forbidden action can result in the private cloud becoming inaccessible. Certain actions, like deleting management VMs, are irreversible. In such scenarios, VMware Engine support may recommend disaster recovery, or creating a new private cloud to recover your workload VMs from backup.

**Caution:** VMware Engine support team may not be able to help you recover access to your private cloud if a forbidden action causes an issue.

### Cluster actions

The following cluster actions are forbidden:

  * Removing a cluster from vCenter
  * Changing vSphere high availability (HA) on a cluster
  * Adding a host to the cluster from vCenter
  * Removing a host from the cluster from vCenter
  * Changing vSphere Distributed Resource Scheduler (DRS) on a cluster
  * Creating new Data Centers in VMware Engine
  * Sharing vSAN datastores across two or more clusters



### Host actions

The following host actions are forbidden:

  * Adding or removing datastores on an ESXi host; you can mount a temporary disaster recovery datastore, but SLAs won't apply
  * Uninstalling vCenter agent from host
  * Modifying the host configuration
  * Making any changes to the host profiles
  * Placing a host in maintenance mode



### Network actions

The following network actions are forbidden in vCenter Server:

  * Deleting the default distributed virtual switch (DVS) in a private cloud
  * Removing a host from the default DVS
  * Importing any DVS setting
  * Reconfiguring any DVS setting
  * Upgrading any DVS
  * Deleting the management portgroup
  * Editing the management portgroup



The following network actions are forbidden in NSX Manager:

  * Adding a new NSX Edge node
  * Changing an existing NSX Edge node



### Roles and permissions actions

The following roles and permissions actions are forbidden:

  * Modifying or deleting permission to any management objects
  * Modifying or removing any default roles
  * Increase the privileges of a role to higher than of Cloud-Owner-Role
  * Adding users and groups to the Administrator group on vCenter
  * Adding any Active Directory users and groups to the Administrator group on vCenter



### Other actions

The following actions are additionally forbidden:

  * Removing any default licenses: 
    * vCenter Server
    * ESXi nodes
    * NSX
    * HCX
  * Modifying or deleting the management resource pool.
  * Cloning management VMs.
  * Deleting any management VMs.
  * Deleting any NSX-T Edge VMs.
  * Assigning a management network to a workload VM.
  * Using an IP address in the management internal IP address range for a workload VM.
  * Renaming the data center.
  * Renaming the cluster.
  * Configuring Syslog forwarding using TLS protocol is not supported and is a forbidden action.
  * Configuring syslog forwarding using the vCenter Server Appliance Management Interface (VAMI).
  * Configuring syslog forwarding on ESXi Hosts directly using the vCenter user interface. Instead, use the VMware Engine portal or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/create) to configure syslog forwarding for vCenter Server or ESXi Hosts.
  * Joining your private cloud vCenter to an Active Directory domain.
  * Resetting vCenter or NSX sign-in credentials using VMware tools, API calls, or management appliances (vCenter/NSX manager). As a reminder, you can [retrieve or reset generated credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/classic-console/howto-access-vsphere-client#sign-in), including password updates, from the private cloud details page in the VMware Engine portal.
  * Changing statistics collection intervals or statistics levels in the vSphere Client.



## What's next

  * Learn how to [set up vCenter identity sources](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/classic-console/howto-identity-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
