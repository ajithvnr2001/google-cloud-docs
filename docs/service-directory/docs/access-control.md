---
url: https://docs.cloud.google.com/service-directory/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:24.210096+00:00
---

# Roles and permissions  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers Identity and Access Management (IAM), which enables you to give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Service Directory API roles. For a detailed description of IAM, read the [IAM documentation](https://docs.cloud.google.com/iam/docs).

IAM enables you to adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM enables you to control _who_ has _what_ permissions to _which_ resources by setting IAM policies. IAM policies grant specific roles to a user, giving the user certain permissions.

## Permissions and Roles

Every Service Directory API method requires the caller to have the necessary IAM permissions. You can assign permissions by granting roles to a user, group, or service account. In addition to the basic Owner, Editor, and Viewer roles, you can grant Service Directory API roles to the users of your project.

### Permissions

You can find out which permissions are required for each method in the Service Directory [API reference documentation](https://docs.cloud.google.com/service-directory/docs/reference/rest).

### Roles

Role | Permissions  
---|---  
  
#### Service Directory Admin 

(`roles/servicedirectory.admin`) Full control of all Service Directory resources and permissions.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.*`

  * `servicedirectory.endpoints.create`
  * `servicedirectory.endpoints.delete`
  * `servicedirectory.endpoints.get`
  * `servicedirectory.endpoints.getIamPolicy`
  * `servicedirectory.endpoints.list`
  * `servicedirectory.endpoints.setIamPolicy`
  * `servicedirectory.endpoints.update`

`servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.*`

  * `servicedirectory.namespaces.associatePrivateZone`
  * `servicedirectory.namespaces.create`
  * `servicedirectory.namespaces.delete`
  * `servicedirectory.namespaces.get`
  * `servicedirectory.namespaces.getIamPolicy`
  * `servicedirectory.namespaces.list`
  * `servicedirectory.namespaces.setIamPolicy`
  * `servicedirectory.namespaces.update`

`servicedirectory.networks.attach` `servicedirectory.services.*`

  * `servicedirectory.services.bind`
  * `servicedirectory.services.create`
  * `servicedirectory.services.delete`
  * `servicedirectory.services.get`
  * `servicedirectory.services.getIamPolicy`
  * `servicedirectory.services.list`
  * `servicedirectory.services.resolve`
  * `servicedirectory.services.setIamPolicy`
  * `servicedirectory.services.update`

  
  
#### Service Directory Editor 

(`roles/servicedirectory.editor`) Edit Service Directory resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.create` `servicedirectory.endpoints.delete` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.endpoints.update` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.associatePrivateZone` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.namespaces.update` `servicedirectory.networks.attach` `servicedirectory.services.bind` `servicedirectory.services.create` `servicedirectory.services.delete` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve` `servicedirectory.services.update`  
  
#### Service Directory Viewer 

(`roles/servicedirectory.viewer`) View Service Directory resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve`  
  
#### Service Directory Network Attacher 

(`roles/servicedirectory.networkAttacher`) Gives access to attach VPC Networks to Service Directory Endpoints  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.networks.attach`  
  
#### Private Service Connect Authorized Service 

(`roles/servicedirectory.pscAuthorizedService`) Gives access to VPC Networks via Service Directory  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.networks.access`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Service Directory Service Agent 

(`roles/servicedirectory.serviceAgent`) Give the Service Directory service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `container.clusters.get` `gkehub.features.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.create` `servicedirectory.endpoints.delete` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.endpoints.update` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.associatePrivateZone` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.namespaces.update` `servicedirectory.networks.attach` `servicedirectory.services.bind` `servicedirectory.services.create` `servicedirectory.services.delete` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve` `servicedirectory.services.update`  
  
## Access Control using the Google Cloud console

You can use the Google Cloud console to manage access control for your registry.

To set access controls at the project level:

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select your project from the top pull-down menu.

  3. Click **Add**.

  4. In **New principals** , enter the email address of a new principal.

  5. Select the desired role from the drop-down menu: `servicedirectory.admin`, `servicedirectory.editor`, or `servicedirectory.viewer`

  6. Click **Save**.

  7. Verify that the principal is listed with the role that you granted.




## Service Directory zones override IAM restrictions

When assigning a namespace to a Service Directory zone, the service names become visible to all clients on any networks that are authorized to query the private zone. There is no IAM access control for DNS as the DNS protocol does not provide authentication capability.

## What's next

  * See the [IAM documentation](https://docs.cloud.google.com/iam/docs) for details on Identity and Access Management
  * See the [Overview](https://docs.cloud.google.com/service-directory/docs/overview) for an understanding of Service Directory.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
