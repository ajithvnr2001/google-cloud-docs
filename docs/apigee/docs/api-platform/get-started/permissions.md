---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions/
title: About Apigee provisioning permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:54.127889+00:00
---

# About Apigee provisioning permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  About Apigee provisioning permissions Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes the [ Google Cloud IAM permissions](https://docs.cloud.google.com/iam/docs/overview) that are required to successfully provision Apigee. 

You can specify permissions using the following: 

  * **Predefined roles:** Provide sufficient permission to do the provisioning steps. Predefined roles may give the Apigee administrator more permissions than they need to complete provisioning.
  * **Custom roles:** Provide the least-necessary privilege needed to do the provisioning steps.



##  Google Cloud project owner role 

The owner of the Google Cloud project that is used for Apigee provisioning already has permission to perform all of the basic Apigee provisioning steps. 

If the Apigee provisioner is not the project owner, then use this document to determine the permissions needed to perform each of the provisioning steps. 

If you use Shared Virtual Private Cloud (VPC) networking, additional permissions in the Shared VPC project are required, and these cases are also noted in this document. 

## Predefined roles

If you just want to make sure the Apigee administrator has sufficient permission to complete the provisioning, give the Apigee administrator the following [IAM predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles); however, predefined roles may give the Apigee administrator more permissions than they need to complete provisioning. See  Custom roles and permissions to provide least-necessary privileges. 

#### How to specify a predefined role

To add users and roles:

  1. In the Google Cloud console, go to **IAM & Admin > IAM** for your project.

[Go to the IAM/Iam page](https://console.cloud.google.com/iam-admin/iam)

  2. To add a new user: 
     1. Click **Grant access**.
     2. Type a new **Principal** name.
     3. Click the **Select a role** menu and then type the role name in the **Filter** field. For example, `Apigee Organization Admin`. Click the role listed in the results. 
     4. Click **Save**.
  3. To edit an existing user: 
     1. Click edit **Edit**.
     2. To change an existing role, click the **Role** menu and then select a different role.
     3. To add another role, click **Add another role.**
     4. Click the **Select a role** menu and then type the role name in the **Filter** field. For example, `Apigee Organization Admin`. Click the role listed in the results. 
     5. Click **Save**.

Role | Required for steps | Account type | Purpose  
---|---|---|---  
[ Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee)  
`apigee.admin` | 

  * Start Apigee provisioning
  * Create an organization
  * Create an environment
  * Create an Apigee instance

| Paid and eval | Grants full access to all Apigee resource features.  
[ Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage)  
`serviceusage.serviceUsageAdmin`  
| 

  * Enable APIs

| Paid and eval | Ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project.  
[ Cloud KMS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms)  
`cloudkms.admin`  
| 

  * Create an organization
  * Configure a runtime instance

| Paid only | Creating Cloud KMS keys and keyrings.  
[ Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute)  
`compute.admin`  
| 

  * Create an organization
  * Configure a runtime instance
  * Configure service networking
  * Configure access routing (to create the external HTTPS load balancer)

| Paid and eval | Listing Compute regions, setting up service networking, and creating the external HTTPS load balancer.  
  
## Custom roles and permissions

To provide least-necessary privileges, create an [IAM custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) and assign permissions from the following sections. 

#### How to specify a custom role

To add a custom role:

  1. In the Google Cloud console, go to **IAM & Admin > Roles** for your project.

[Go to the IAM & Admin/Roles page](https://console.cloud.google.com/iam-admin/roles)

  2. To add a new role: 
     1. Click **Create role**.
     2. Type a new **Title**.
     3. Type a **Description** (optional).
     4. Type an **ID**.
     5. Select a **Role launch stage**.
     6. Click **Add permissions**.
     7. Copy the desired permission text from the tables below and paste it into the **Filter** field. For example, `apigee.environments.create`.
     8. Press `Enter` or click an item from the results.
     9. Select the checkbox for the item just added.
     10. Click **Add**. **Note:** To add multiple permissions at a time: 
        * Select the `OR` operator between each permission as you add them, or
        * Search for a partial permission string, for example, `apigee.environments`, select multiple checkboxes, and then click **Save**.
     11. Once you have added all the permissions for this role, click **Create**. 


* To edit an existing custom role: 

  1. Locate the custom role.
  2. Click more_vert **More** > **Edit**.
  3. Make any desired changes.
  4. Click **Update**.



### UI-based Apigee management permissions

This permission is required for all users who will manage an organization through the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee). Include it in custom roles that involve management through that interface. 

Role | Account type | Purpose  
---|---|---  
`apigee.projectorganizations.get`  
| Paid and eval | 

  * Perform any actions through the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee).

  
  
### Provisioning permissions

These permissions are required to start provisioning Apigee: 

Role | Account type | Purpose  
---|---|---  
`apigee.entitlements.get`  
`apigee.environments.create`  
`apigee.environments.get`  
`apigee.environments.list`  
`apigee.envgroups.create`  
`apigee.envgroups.get`  
`apigee.envgroups.list`  
`apigee.envgroups.update`  
`apigee.envgroupattachments.create`  
`apigee.envgroupattachments.list`  
`apigee.instances.create`  
`apigee.instances.get`  
`apigee.instances.list`  
`apigee.instanceattachments.create`  
`apigee.instanceattachments.get`  
`apigee.instanceattachments.list`  
`apigee.operations.get`  
`apigee.operations.list`  
`apigee.organizations.create`  
`apigee.organizations.get`  
`apigee.organizations.update`  
`apigee.projectorganizations.get`  
`apigee.projects.update`  
`apigee.setupcontexts.get`  
`apigee.setupcontexts.update` | Paid and eval | 

  * Start Apigee provisioning
  * Create an organization
  * Create an environment
  * Create an Apigee instance

  
  
### API enablement permissions

These permissions are required to enable Google Cloud APIs:

Role | Account type | Purpose  
---|---|---  
`serviceusage.services.get`  
`serviceusage.services.list`  
`serviceusage.services.enable` | Paid and eval | Enabling Google Cloud APIs  
  
###  Organization creation permissions (paid org) 

These permissions are needed to create an Apigee organization for paid accounts (Subscription or Pay-as-you-go):

Permissions | Account type | Purpose  
---|---|---  
`compute.regions.list` | Paid only | Selecting an analytics hosting location  
`cloudkms.cryptoKeys.list`  
`cloudkms.locations.list`  
`cloudkms.keyRings.list` | Paid only | Selecting a runtime database encryption key  
`cloudkms.cryptoKeys.create`  
`cloudkms.keyRings.create` | Paid only | Creating a runtime database encryption key  
`cloudkms.cryptoKeys.getIamPolicy`  
`cloudkms.cryptoKeys.setIamPolicy` | Paid only | Granting Apigee service account permission to use an encryption key  
  
### Organization creation permissions (eval org)

This permission is required for selecting analytics and runtime hosting regions for an eval organization: 

Permissions | Account type | Purpose  
---|---|---  
`compute.regions.list` | Eval organizations only | Selecting analytics and runtime hosting regions  
  
### Service networking permissions

These permissions are needed in the service networking configuration steps. If you are using Shared VPC networking, see  Service networking permissions with Shared VPC. 

Permissions | Account type | Purpose  
---|---|---  
`compute.globalAddresses.createInternal`  
`compute.globalAddresses.get  
` `compute.globalAddresses.list  
` `compute.globalAddresses.use  
` `compute.networks.get  
` `compute.networks.list  
` `compute.networks.use  
` `compute.projects.get  
` `servicenetworking.operations.get  
` `servicenetworking.services.addPeering  
` `servicenetworking.services.get` | Paid and eval | These permissions are required to perform the tasks in the service networking configuration step. **Note:** If you are using [ Shared Virtual Private Cloud (VPC) networking](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs), see  Service networking permissions with Shared VPC.  
  
###  Service networking permissions with Shared VPC 

If you are using Shared Virtual Private Cloud (VPC) networking, a user with administrative privileges in the Shared VPC project must peer the Shared VPC project with Apigee, as described in [ Using shared VPC networks](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs). Peering must be completed before the Apigee admin can complete the service networking steps. See also [Administrators and IAM](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc). 

When Shared VPC is properly set up, the Apigee admin needs these permissions to complete the service networking configuration steps: 

Permissions | Account type | Purpose  
---|---|---  
`compute.projects.get` | Paid and eval | The Apigee admin must have this permission **in the project where Apigee is installed**. This permission allows the admin to view the Shared VPC host project ID.  
Compute Network User role  
(`compute.networkUser`) | Paid and eval |  The Apigee admin must be granted this role **in the Shared VPC host project**. This role allows the admin to view and select the Shared VPC network in the Apigee provisioning UI.   
  
### Runtime instance permissions

These permissions are needed to create a runtime instance (Subscription and Pay-as-you-go accounts only): 

Permissions | Account type | Purpose  
---|---|---  
`compute.regions.list` | Paid only | Selecting a runtime hosting location  
`cloudkms.cryptoKeys.list`  
`cloudkms.locations.list`  
`cloudkms.keyRings.list` | Paid only | Selecting a runtime disk encryption key  
`cloudkms.cryptoKeys.create`  
`cloudkms.keyRings.create` | Paid only | Creating a runtime disk encryption key  
`cloudkms.cryptoKeys.getIamPolicy`  
`cloudkms.cryptoKeys.setIamPolicy` | Paid only | Granting Apigee service account permission to use an encryption key  
  
### Access routing permissions

These permissions are needed for the access routing steps:

Permissions | Account type | Purpose  
---|---|---  
`compute.autoscalers.create`  
`compute.backendServices.create`  
`compute.backendServices.use`  
`compute.disks.create`  
`compute.globalAddresses.create`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalAddresses.use`  
`compute.globalForwardingRules.create`  
`compute.globalOperations.get`  
`compute.firewalls.create`  
`compute.firewalls.get`  
`compute.healthChecks.create`  
`compute.healthChecks.useReadOnly`  
`compute.images.get`  
`compute.images.useReadOnly`  
`compute.instances.create`  
`compute.instances.setMetadata`  
`compute.instanceGroups.use`  
`compute.instanceGroupManagers.create`  
`compute.instanceGroupManagers.use`  
`compute.instanceTemplates.get`  
`compute.instanceTemplates.create`  
`compute.instanceTemplates.useReadOnly`  
`compute.networks.get`  
`compute.networks.list`  
`compute.networks.updatePolicy`  
`compute.networks.use`  
`compute.regionOperations.get`  
`compute.regionNetworkEndpointGroups.create`  
`compute.regionNetworkEndpointGroups.delete`  
`compute.regionNetworkEndpointGroups.use`  
`compute.sslCertificates.create`  
`compute.sslCertificates.get`  
`compute.subnetworks.get`  
`compute.subnetworks.list`  
`compute.subnetworks.setPrivateIpGoogleAccess`  
`compute.subnetworks.use`  
`compute.targetHttpsProxies.create`  
`compute.targetHttpsProxies.use`  
`compute.urlMaps.create`  
`compute.urlMaps.use` | Paid and eval | Configuring basic access routing **Note:** If you are using [ Shared Virtual Private Cloud (VPC) networking](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs), see Access routing permissions with Shared VPC.  
  
###  Access routing permissions with Shared VPC 

If you are using [ Shared Virtual Private Cloud (VPC) networking](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs), be aware that the Shared VPC configuration and peering must be completed before you can perform the access routing step. 

After the Shared VPC is set up properly, the Apigee admin requires the [ `compute.networkUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) role **in the Shared VPC project** to complete the access routing steps. See also [ Required administrative roles](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_roles_required_for_shared_vpc) for Shared VPC. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
