---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control/
title: Roles and permissions \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:41.127619+00:00
---

# Roles and permissions  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions needed for running Connectivity Tests.

You can grant users or service accounts permissions or predefined roles, or you can create a custom role that uses permissions that you specify.

The IAM permissions use a prefix of `networkmanagement`.

To get or set IAM policies, or to test IAM permissions with the Network Management API, see [Manage access policies](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-access-control).

## Roles

This section describes how to use predefined and custom roles when granting permissions for Connectivity Tests.

For an explanation of each permission, see the permissions table.

For more information about project roles and Google Cloud resources, see the following documentation:

  * [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_basic_roles)
  * [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs/roles-overview#role-types)
  * [Compute Engine documentation describing access control](https://docs.cloud.google.com/compute/docs/access/iam-permissions)



### Predefined roles

Connectivity Tests has the following predefined roles:

  * `networkmanagement.admin` has permission to perform all operations on a test resource.
  * `networkmanagement.viewer` has permission to list or get a specific test resource.



The following table lists the predefined roles and the permissions that apply to each role.

Role | Permissions  
---|---  
  
#### Network Management Admin 

(`roles/networkmanagement.admin`) Full access to Network Management resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkmanagement.*`

  * `networkmanagement.connectivitytests.create`
  * `networkmanagement.connectivitytests.createTagBinding`
  * `networkmanagement.connectivitytests.delete`
  * `networkmanagement.connectivitytests.deleteTagBinding`
  * `networkmanagement.connectivitytests.get`
  * `networkmanagement.connectivitytests.getIamPolicy`
  * `networkmanagement.connectivitytests.list`
  * `networkmanagement.connectivitytests.listEffectiveTags`
  * `networkmanagement.connectivitytests.listTagBindings`
  * `networkmanagement.connectivitytests.rerun`
  * `networkmanagement.connectivitytests.setIamPolicy`
  * `networkmanagement.connectivitytests.update`
  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`
  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`
  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`
  * `networkmanagement.operations.cancel`
  * `networkmanagement.operations.delete`
  * `networkmanagement.operations.get`
  * `networkmanagement.operations.list`
  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`
  * `networkmanagement.topologygraphs.read`
  * `networkmanagement.vpcflowlogsconfigs.create`
  * `networkmanagement.vpcflowlogsconfigs.delete`
  * `networkmanagement.vpcflowlogsconfigs.get`
  * `networkmanagement.vpcflowlogsconfigs.list`
  * `networkmanagement.vpcflowlogsconfigs.update`
  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Network Management Editor 

(`roles/networkmanagement.editor`) Editor role for Network Management resources.  |  `networkmanagement.connectivitytests.create` `networkmanagement.connectivitytests.delete` `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.getIamPolicy` `networkmanagement.connectivitytests.list` `networkmanagement.connectivitytests.listEffectiveTags` `networkmanagement.connectivitytests.listTagBindings` `networkmanagement.connectivitytests.rerun` `networkmanagement.connectivitytests.update` `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.*`

  * `networkmanagement.operations.cancel`
  * `networkmanagement.operations.delete`
  * `networkmanagement.operations.get`
  * `networkmanagement.operations.list`

`networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.topologygraphs.read` `networkmanagement.vpcflowlogsconfigs.*`

  * `networkmanagement.vpcflowlogsconfigs.create`
  * `networkmanagement.vpcflowlogsconfigs.delete`
  * `networkmanagement.vpcflowlogsconfigs.get`
  * `networkmanagement.vpcflowlogsconfigs.list`
  * `networkmanagement.vpcflowlogsconfigs.update`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Network Management Viewer 

(`roles/networkmanagement.viewer`) Read-only access to Network Management resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.getIamPolicy` `networkmanagement.connectivitytests.list` `networkmanagement.connectivitytests.listEffectiveTags` `networkmanagement.connectivitytests.listTagBindings` `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.topologygraphs.read` `networkmanagement.vpcflowlogsconfigs.get` `networkmanagement.vpcflowlogsconfigs.list` `networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Admin 

(`roles/networkmanagement.CloudNetworkInsightsAdmin`) Full access to Cloud Network Insights resources.  |  `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.*`

  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`

`networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.*`

  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Editor 

(`roles/networkmanagement.CloudNetworkInsightsEditor`) Editor access to Cloud Network Insights resources.  |  `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.*`

  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`

`networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.*`

  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Viewer 

(`roles/networkmanagement.CloudNetworkInsightsViewer`) Read-only access to Cloud Network Insights resources.  |  `networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### GCP Network Management Service Agent 

(`roles/networkmanagement.serviceAgent`) Grants the GCP Network Management API the authority to complete analysis based on network configurations from Compute Engine and Container Engine.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudsql.instances.get` `cloudsql.instances.list` `compute.addresses.get` `compute.addresses.list` `compute.backendServices.get` `compute.backendServices.list` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.firewalls.get` `compute.firewalls.list` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instances.get` `compute.instances.list` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.routers.get` `compute.routers.list` `compute.routes.get` `compute.routes.list` `compute.subnetworks.get` `compute.subnetworks.list` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetPools.get` `compute.targetPools.list` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.urlMaps.get` `compute.urlMaps.list` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `container.clusters.get` `container.clusters.list` `container.nodes.get` `container.nodes.list`  
  
### Custom roles

You can create custom roles by selecting a list of permissions from the permissions table for Connectivity Tests.

For example, you can create a role called `reachabilityUsers`, and grant the `list`, `get`, and `rerun` permissions to this role. A user with this role can rerun existing Connectivity Tests and view updated test results based on the latest network configuration.

### Project roles

You can use project roles to set permissions to Google Cloud resources. Because Connectivity Tests must have read access to the Google Cloud resource configurations in your Virtual Private Cloud (VPC) network to run a test, you must grant at least the [Compute Network Viewer role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) (`roles/compute.networkViewer`) to users or service accounts running a test against those resources. You can also create a custom role or temporarily authorize permissions associated with the preceding role for a specific user.

Alternatively, you can grant a user or service account one of the following predefined roles for Google Cloud projects:

  * [`project.viewer`](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_basic_roles) has all the permissions of a `networkmanagement.viewer` role.
  * [`project.editor` or `project.owner`](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_basic_roles) has all the permissions of the `networkmanagement.admin` role.



## Permissions

This section describes permissions for Connectivity Tests and how to use them when testing different types of network configurations.

### Connectivity Tests permissions

Connectivity Tests has the following IAM permissions.

Permission | Description  
---|---  
`networkmanagement.connectivitytests.list` | Lists all tests configured in the specified project.  
`networkmanagement.connectivitytests.get` | Gets the details of a specific test.  
`networkmanagement.connectivitytests.create` | Creates a new test object in the specified project with the data that you specify for the test. This permission includes permission to update, rerun, or delete tests.  
`networkmanagement.connectivitytests.update` | Updates one or more fields in an existing test.  
`networkmanagement.connectivitytests.delete` | Deletes the specified test.  
`networkmanagement.connectivitytests.rerun` | Reruns a one-time reachability verification for a specified test.  
  
If you don't have permission to create or update a test, the corresponding buttons are inactive. These include the **Create connectivity test** button and, on the **Connectivity test details** page, the **Edit** button. In each case, when you hold the pointer over the inactive button, Connectivity Tests displays a message describing the permission that you need.

### Permissions for running a test

You need the following roles and permissions to run a test:

  * `networkmanagement.connectivitytests.create` permission (or `networkmanagement.connectivitytests.rerun`) in a project with a Connectivity Tests resource.
  * [Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) or the legacy [Viewer role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) to all the projects included in the trace path.



Note the following additional considerations with different types of connectivity options.

#### VPC Network Peering, NCC, or Cloud VPN connectivity

If the trace path includes VPC Network Peering, Network Connectivity Center, or Cloud VPN connectivity to a network in a different project, a packet path in that network is simulated only if you have permissions to that project. Otherwise, an incomplete test result is returned (for example, a trace ending with the [**Forward** final state](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#forward-state)).

#### Shared VPC projects

If a source or destination endpoint (such as a virtual machine (VM) instance) uses Shared VPC, you must have permission to access both the host and service projects.

  * If you have permission to access both the host and service projects, the trace information includes details about all the relevant resources.
  * If you don't have permission to access one of the projects, information about resources defined in this project is hidden in the trace. A permission error is displayed.



##### Examples

  * You have access to the VM instance project (service project) but don't have access to its network project (host project). If you run a test with this VM instance as a source (specified by the name), any steps associated with the host project (for example, applying firewalls or routes) are hidden.

  * You have access to the network project (host project) but don't have access to the VM project (service project). If you run a test with this VM instance as a source (specified by its IP address), any steps associated with the service project—for example, a step with the VM instance details—are hidden.




#### Private Service Connect published services

If the packet goes to the Private Service Connect published service (through a Private Service Connect endpoint or Private Service Connect backend), the part of the trace in the producer project is shown only if you have access to it. Otherwise, the trace ends with a general final state such as **Packet delivered to the PSC producer project** or **Packet dropped inside the PSC producer project**.

#### Google-managed services

If the packet goes to or from the Google-managed network associated with a Google-managed service (like Cloud SQL), the steps inside the Google-managed project aren't shown. A general starting step or a final step is displayed.

#### Google-managed resources

Some resources, such as nodes in a Google Kubernetes Engine Autopilot cluster, are created and managed automatically by Google Cloud. When a step is hidden because it references these resources, the step shows the resource type (such as VM instance), but not its details.

#### Public IP addresses of Google Cloud resources

If you specify a public IP address that is assigned to a resource in one of your projects as a test source or destination but don't have permissions to the project where the resource with this address is defined, this IP address is considered to be an internet IP address. Any details about the underlying resource or packet path after this resource is reached are not displayed.

### Permissions for viewing test results

To view the test results, note the following:

  * To view the results of tests created or updated after October 2024, you only need the permission to view the test resource (`networkmanagement.connectivitytests.get`); you don't need permissions to the resources and projects included in the trace path.
  * To view the results of tests executed before October 2024, you must have the [Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) or the legacy [Viewer role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) for all projects included in the trace path.

**Note:** In the Google Cloud console, the color of the card for each tested resource reflects the test condition of the resource, not the permissions that you have to view the resource.

#### Hierarchical firewall policies

Your trace might include a hierarchical firewall policy that you don't have permission to view. However, even if you don't have permission to view the policy details, you can still see the policy rules that apply to your VPC network. For details, see [IAM roles](https://docs.cloud.google.com/firewall/docs/firewall-policies#iam) in the "Hierarchical firewall policies" overview.

## What's next

  * [Manage access policies](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-access-control)
  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
