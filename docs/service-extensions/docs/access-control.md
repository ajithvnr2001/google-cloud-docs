---
url: https://docs.cloud.google.com/service-extensions/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:32.200310+00:00
---

# Roles and permissions  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to let you provide more granular access to specific Google Cloud resources and prevent access to other resources. This page describes the roles and permissions for Service Extensions.

IAM lets you adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) so that you need to grant only the necessary access to your resources.

Roles are collections of IAM permissions. To make permissions available to principals, including users, groups, and service accounts, you grant roles to the principals. You can control _who_ has _what_ permissions to _which_ resources by setting IAM policies. IAM policies grant specific roles to principals, thereby giving them certain permissions.

For detailed information about IAM roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

## Predefined roles and permissions for Service Extensions

Service Extensions supports IAM permissions at the project level.

The following table lists Service Extensions IAM roles and the permissions that each role includes.

Roles | Permissions  
---|---  
**Service Extensions Admin** (`roles/networkservices.serviceExtensionsAdmin`) Permissions to create, updated, list, view, and delete extensions. |  `networkservices.authzExtensions.create`  
`networkservices.authzExtensions.delete`  
`networkservices.authzExtensions.get`  
`networkservices.authzExtensions.list`  
`networkservices.authzExtensions.update`  
`networkservices.authzExtensions.use`  
`networkservices.lbEdgeExtensions.create`  
`networkservices.lbEdgeExtensions.delete`  
`networkservices.lbEdgeExtensions.get`  
`networkservices.lbEdgeExtensions.list`  
`networkservices.lbEdgeExtensions.update`  
`networkservices.lbRouteExtensions.create`  
`networkservices.lbRouteExtensions.delete`  
`networkservices.lbRouteExtensions.get`  
`networkservices.lbRouteExtensions.list`  
`networkservices.lbRouteExtensions.update`  
`networkservices.lbTrafficExtensions.create`  
`networkservices.lbTrafficExtensions.delete`  
`networkservices.lbTrafficExtensions.get`  
`networkservices.lbTrafficExtensions.list`  
`networkservices.lbTrafficExtensions.update`  
`networkservices.wasmActions.get`  
`networkservices.wasmActions.list`  
`networkservices.wasmActions.create`  
`networkservices.wasmActions.delete`  
`networkservices.wasmPlugins.get`  
`networkservices.wasmPlugins.list`  
`networkservices.wasmPlugins.create`  
`networkservices.wasmPlugins.update`  
`networkservices.wasmPlugins.delete`  
`networkservices.wasmPlugins.use` |  **Service Extensions Viewer** (`roles/networkservices.serviceExtensionsViewer`) Permissions to list and view extensions. |  `networkservices.authzExtensions.get`  
`networkservices.authzExtensions.list`  
`networkservices.lbEdgeExtensions.get`  
`networkservices.lbEdgeExtensions.list`  
`networkservices.lbRouteExtensions.get`  
`networkservices.lbRouteExtensions.list`  
`networkservices.lbTrafficExtensions.get`  
`networkservices.lbTrafficExtensions.list`  
`networkservices.wasmActions.get`  
`networkservices.wasmActions.list`  
`networkservices.wasmPlugins.get`  
`networkservices.wasmPlugins.list`  
  
The following table lists IAM roles that you need for other services and the permissions that each role includes.

Roles | Permissions  
---|---  
**[Compute Load Balancer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin)** (`roles/compute.loadBalancerAdmin`) Permissions to update forwarding rules. Required while creating and updating extensions that attach to forwarding rules.  |  `compute.forwardingRules.update`  
`compute.globalForwardingRules.update`  
**[Compute Load Balancer Services User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerServiceUser)** (`roles/compute.loadBalancerServiceUser`) Permissions to use backend services. Required while creating and updating extensions that use backend services as extension services.  |  `compute.backendServices.use`  
`compute.regionBackendBuckets.use`  
  
Role | Permissions  
---|---  
  
#### Service Extensions Admin Beta

(`roles/serviceextensions.admin`) Grants full access to Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.*`

  * `serviceextensions.callouts.invoke`
  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
#### Service Extensions Editor Beta

(`roles/serviceextensions.editor`) Grants access to edit Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.*`

  * `serviceextensions.callouts.invoke`
  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
#### Service Extensions Viewer Beta

(`roles/serviceextensions.viewer`) Grants read access to Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.locations.*`

  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Network Actions Service Agent 

(`roles/networkactions.serviceAgent`) Gives Network Actions service account access to read required resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.files.download` `artifactregistry.repositories.downloadArtifacts`  
  
## Manage access control

To set access controls at the project level, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select your project.

  3. Click **Add**.

  4. In **New principals** , enter the email address of a new principal.

  5. Select the required role.

  6. Click **Save**.

  7. Verify that the principal is listed with the role that you granted.




## Identify the permissions in a role

To determine whether one or more permissions are included in a role, you can use one of the following methods:

  * The [IAM permissions search reference](https://docs.cloud.google.com/iam/docs/permissions-reference)
  * The [`gcloud iam roles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe)
  * The [`roles.get()` method](https://docs.cloud.google.com/iam/reference/rest/v1/roles/get) in the IAM API



## What's next

  * See the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).
  * Learn how to [prepare the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code) to create plugins.
  * Learn how to [create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin).
  * Learn how to [manage plugins](https://docs.cloud.google.com/service-extensions/docs/manage-plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
