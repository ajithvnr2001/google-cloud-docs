---
url: https://docs.cloud.google.com/dns/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:31.032972+00:00
---

# Roles and permissions  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Cloud DNS API roles. For a detailed description of IAM, see the [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs).

IAM lets you adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) so that you grant only the necessary access to your resources.

IAM lets you control _who_ has _what_ permissions to _which_ resources by setting IAM policies. IAM policies grant specific roles to a user, giving the user certain permissions. For example, a particular user might need to create and modify Domain Name System (DNS) record resources. You would then give that user (who) the `/roles/dns.admin` role, which has the `dns.changes.create` and `dns.resourceRecordSets.create` permissions (what) so that they can create and update resource record sets (which). In contrast, a support department might only need to view existing resource record sets, so they would get a `/roles/dns.reader` role.

Cloud DNS supports IAM permissions at the project level and individual DNS zone level. The default permission is at the project level. To configure permissions at the individual DNS zone (or resource) level, see [Create a zone with specific IAM permissions](https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones).

## Permissions and roles

Every Cloud DNS API method requires the caller to have the necessary IAM permissions. Permissions are assigned by granting roles to a user, group, or service account. In addition to the basic roles Owner, Editor, and Viewer, you can grant Cloud DNS API roles to the users of your project.

### Permissions

The following table lists the permissions that the caller must have to call each method.

Method | Required permission(s)  
---|---  
[`dns.changes.create`](https://docs.cloud.google.com/dns/docs/reference/v1/changes/create) | To create a resource record, set both `dns.changes.create` and `dns.resourceRecordSets.create` on the project containing the record set. To update a resource record, set both `dns.changes.create` and `dns.resourceRecordSets.update` on the project containing the record set.  To delete a resource record, set both `dns.changes.create` and `dns.resourceRecordSets.delete` on the project containing the record set.   
[`dns.changes.get`](https://docs.cloud.google.com/dns/docs/reference/v1/changes/get) | `dns.changes.get` on the project containing the managed zone.  
[`dns.changes.list`](https://docs.cloud.google.com/dns/docs/reference/v1/changes/list) | `dns.changes.list` on the project containing the managed zone.  
[`dns.dnsKeys.get`](https://docs.cloud.google.com/dns/docs/reference/v1/dnsKeys/get) | `dns.dnsKeys.get` on the project containing the managed zone.  
[`dns.dnsKeys.list`](https://docs.cloud.google.com/dns/docs/reference/v1/dnsKeys/list) | `dns.dnsKeys.list` on the project containing the managed zone.  
[`dns.managedZoneOperations.get`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZoneOperations/get) | `dns.managedZoneOperations.get` on the project containing the managed zone.  
[`dns.managedZoneOperations.list`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZoneOperations/list) | `dns.managedZoneOperations.list` on the project containing the managed zone.  
[`dns.managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) | `dns.managedZones.create` on the project containing the managed zone.If you are creating a private zone, you also need `dns.networks.bindPrivateDNSZone` and `dns.networks.targetWithPeeringZone` on each project with a VPC network authorized to access the zone. If you are creating a private zone with GKE integration, you also need `dns.gkeClusters.bindPrivateDNSZone` to configure a GKE cluster scope.  
[`dns.managedZones.delete`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/delete) | `dns.managedZones.delete` on the project containing the managed zone.  
[`dns.managedZones.get`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/get) | `dns.managedZones.get` on the project containing the managed zone.  
[`dns.managedZones.list`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/list) | `dns.managedZones.list` on the project containing the managed zone.  
[`dns.managedZones.update`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/update) | `dns.managedZones.update` on the project containing the managed zone.If you are creating a private zone, you also need `dns.networks.bindPrivateDNSZone` and `dns.networks.targetWithPeeringZone` on each project with a VPC network authorized to access the zone. If you are creating a private zone with GKE integration, you also need `dns.gkeClusters.bindPrivateDNSZone` to configure a GKE cluster scope.  
[`dns.policies.create`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/policies/create) | `dns.policies.create` on the project containing the policy. If the policy is created on a VPC network, you also need `dns.networks.bindPrivateDNSPolicy` for each project containing each VPC network.  
[`dns.policies.delete`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/policies/delete) | `dns.policies.delete` on the project containing the policy.  
[`dns.policies.get`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/policies/get) | `dns.policies.get` on the project containing the policy.  
[`dns.policies.list`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/policies/list) | `dns.policies.list` on the project containing the policy.  
[`dns.policies.update`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/policies/update) | `dns.policies.update` on the project containing the policy. If the policy is updated to be on a VPC network, you also need `dns.networks.bindPrivateDNSPolicy` for each project containing each VPC network.  
[`dns.projects.get`](https://docs.cloud.google.com/dns/docs/reference/v1/projects/get) | `dns.projects.get` on the project.  
[`dns.resourceRecordSets.create`](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/create) | `dns.resourceRecordSets.create` on the project containing the record set.  
[`dns.resourceRecordSets.delete`](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/delete) | `dns.resourceRecordSets.delete` on the project containing the record set.  
[`dns.resourceRecordSets.get`](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/get) | `dns.resourceRecordSets.get` on the project containing the record set.  
[`dns.resourceRecordSets.list`](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/list) | `dns.resourceRecordSets.list` on the project containing the managed zone.  
[`dns.resourceRecordSets.update`](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/patch) | `dns.resourceRecordSets.update` and `dns.changes.create` on the project containing the record set.  
[`dns.responsePolicies.create`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicies/create) | `dns.responsePolicies.create` on the project containing the response policy. You also need `dns.networks.bindDNSResponsePolicy` to validate the request. If you want to create a response policy attached to a GKE cluster, you need `dns.gkeClusters.bindDNSResponsePolicy`.   
[`dns.responsePolicies.delete`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicies/delete) | `dns.responsePolicies.delete` on the project containing the response policy.  
[`dns.responsePolicies.get`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicies/get) | `dns.responsePolicies.get` on the project containing the response policy.  
[`dns.responsePolicies.list`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicies/list) | `dns.responsePolicies.list` on the project.  
[`dns.responsePolicies.update`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicies/update) | `dns.responsePolicies.update` on the project containing the response policy. You also need `dns.networks.bindDNSResponsePolicy` to validate the request. If you want to create a response policy attached to a GKE cluster, you need `dns.gkeClusters.bindDNSResponsePolicy`.  
[`dns.responsePolicyRules.create`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicyRules/create) | `dns.responsePolicyRules.create` on the project containing the response policy rule.  
[`dns.responsePolicyRules.delete`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicyRules/delete) | `dns.responsePolicyRules.delete` on the project containing the response policy rule.  
[`dns.responsePolicyRules.get`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicyRules/get) | `dns.responsePolicyRules.get` on the project containing the response policy rule.  
[`dns.responsePolicyRules.list`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicyRules/list) | `dns.responsePolicyRules.list` on the project containing the response policy.  
[`dns.responsePolicyRules.update`](https://docs.cloud.google.com/dns/docs/reference/v1beta2/responsePolicyRules/update) | `dns.responsePolicyRules.update` on the project containing the response policy rule.  
[`networksecurity.dnsThreatDetectors.list`](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/list) | `networksecurity.dnsThreatDetectors.list` on the project where the VPC networks are monitored for threats.  
[`networksecurity.dnsThreatDetectors.get`](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/get) | `networksecurity.dnsThreatDetectors.get` on the project where the VPC networks are monitored for threats.  
[`networksecurity.dnsThreatDetectors.create`](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/create) | `networksecurity.dnsThreatDetectors.create` on the project containing the VPC networks you want to monitor for threats.  
[`networksecurity.dnsThreatDetectors.update`](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/patch) | `networksecurity.dnsThreatDetectors.update` on the project where the VPC networks are monitored for threats.  
[`networksecurity.dnsThreatDetectors.delete`](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/delete) | `networksecurity.dnsThreatDetectors.delete` on the project where the VPC networks are monitored for threats.  
  
### Roles

The following table lists the Cloud DNS API IAM roles with a corresponding list of all the permissions that each role includes. Every permission is applicable to a particular resource type.

You can also use [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) to make DNS changes.

Role | Permissions  
---|---  
  
#### DNS Administrator 

(`roles/dns.admin`) Provides read-write access to all Cloud DNS resources.  Lowest-level resources where you can grant this role:

  * Managed zone 

|  `compute.networks.get` `compute.networks.list` `dns.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`
  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`
  * `dns.gkeClusters.bindDNSResponsePolicy`
  * `dns.gkeClusters.bindPrivateDNSZone`
  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`
  * `dns.managedZones.create`
  * `dns.managedZones.delete`
  * `dns.managedZones.get`
  * `dns.managedZones.getIamPolicy`
  * `dns.managedZones.list`
  * `dns.managedZones.setIamPolicy`
  * `dns.managedZones.update`
  * `dns.networks.bindDNSResponsePolicy`
  * `dns.networks.bindPrivateDNSPolicy`
  * `dns.networks.bindPrivateDNSZone`
  * `dns.networks.targetWithPeeringZone`
  * `dns.networks.useHealthSignals`
  * `dns.policies.create`
  * `dns.policies.createTagBinding`
  * `dns.policies.delete`
  * `dns.policies.deleteTagBinding`
  * `dns.policies.get`
  * `dns.policies.list`
  * `dns.policies.listEffectiveTags`
  * `dns.policies.listTagBindings`
  * `dns.policies.update`
  * `dns.projects.get`
  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`
  * `dns.responsePolicies.create`
  * `dns.responsePolicies.delete`
  * `dns.responsePolicies.get`
  * `dns.responsePolicies.list`
  * `dns.responsePolicies.update`
  * `dns.responsePolicyRules.create`
  * `dns.responsePolicyRules.delete`
  * `dns.responsePolicyRules.get`
  * `dns.responsePolicyRules.list`
  * `dns.responsePolicyRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DNS Editor 

(`roles/dns.editor`) Editor role for DNS resources.  |  `compute.networks.get` `compute.networks.list` `dns.changes.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`

`dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

`dns.gkeClusters.*`

  * `dns.gkeClusters.bindDNSResponsePolicy`
  * `dns.gkeClusters.bindPrivateDNSZone`

`dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.getIamPolicy` `dns.managedZones.list` `dns.managedZones.update` `dns.networks.*`

  * `dns.networks.bindDNSResponsePolicy`
  * `dns.networks.bindPrivateDNSPolicy`
  * `dns.networks.bindPrivateDNSZone`
  * `dns.networks.targetWithPeeringZone`
  * `dns.networks.useHealthSignals`

`dns.policies.create` `dns.policies.delete` `dns.policies.get` `dns.policies.list` `dns.policies.listEffectiveTags` `dns.policies.listTagBindings` `dns.policies.update` `dns.projects.get` `dns.resourceRecordSets.*`

  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

`dns.responsePolicies.*`

  * `dns.responsePolicies.create`
  * `dns.responsePolicies.delete`
  * `dns.responsePolicies.get`
  * `dns.responsePolicies.list`
  * `dns.responsePolicies.update`

`dns.responsePolicyRules.*`

  * `dns.responsePolicyRules.create`
  * `dns.responsePolicyRules.delete`
  * `dns.responsePolicyRules.get`
  * `dns.responsePolicyRules.list`
  * `dns.responsePolicyRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DNS Viewer 

(`roles/dns.viewer`) Viewer role for DNS resources.  |  `compute.networks.get` `dns.changes.get` `dns.changes.list` `dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

`dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.get` `dns.managedZones.getIamPolicy` `dns.managedZones.list` `dns.policies.get` `dns.policies.list` `dns.policies.listEffectiveTags` `dns.policies.listTagBindings` `dns.projects.get` `dns.resourceRecordSets.get` `dns.resourceRecordSets.list` `dns.responsePolicies.get` `dns.responsePolicies.list` `dns.responsePolicyRules.get` `dns.responsePolicyRules.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DNS Peer 

(`roles/dns.peer`) Access to target networks with DNS peering zones  |  `dns.networks.targetWithPeeringZone`  
  
#### DNS Reader 

(`roles/dns.reader`) Provides read-only access to all Cloud DNS resources.  Lowest-level resources where you can grant this role:

  * Managed zone 

|  `compute.networks.get` `dns.changes.get` `dns.changes.list` `dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

`dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.get` `dns.managedZones.list` `dns.policies.get` `dns.policies.list` `dns.policies.listEffectiveTags` `dns.policies.listTagBindings` `dns.projects.get` `dns.resourceRecordSets.get` `dns.resourceRecordSets.list` `dns.responsePolicies.get` `dns.responsePolicies.list` `dns.responsePolicyRules.get` `dns.responsePolicyRules.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud DNS Service Agent 

(`roles/dns.serviceAgent`) Gives Cloud DNS Service Agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.globalNetworkEndpointGroups.attachNetworkEndpoints` `compute.globalNetworkEndpointGroups.create` `compute.globalNetworkEndpointGroups.delete` `compute.globalNetworkEndpointGroups.detachNetworkEndpoints` `compute.globalNetworkEndpointGroups.get` `compute.globalOperations.get` `compute.healthChecks.get` `compute.networks.get` `compute.networks.use` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use`  
  
The following table lists the DNS Armor IAM roles with a corresponding list of all the permissions that each role includes.

Role | Permissions  
---|---  
  
#### DNS Threat Detector Admin 

(`roles/networksecurity.dnsThreatDetectorAdmin`) Enables full access to DNS Threat Detector resources.  |  `networksecurity.dnsThreatDetectors.*`

  * `networksecurity.dnsThreatDetectors.create`
  * `networksecurity.dnsThreatDetectors.delete`
  * `networksecurity.dnsThreatDetectors.get`
  * `networksecurity.dnsThreatDetectors.list`
  * `networksecurity.dnsThreatDetectors.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DNS Threat Detector Viewer 

(`roles/networksecurity.dnsThreatDetectorViewer`) Enables view access to DNS Threat Detector resources.  |  `networksecurity.dnsThreatDetectors.get` `networksecurity.dnsThreatDetectors.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Manage access control

You can use the Google Cloud console to manage access control for your topics and projects.

To set access controls at the project level, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select your project from the top pull-down menu.

  3. Click **Add**.

  4. In **New principals** , enter the email address of a new principal.

  5. Select a role from the list.

  6. Click **Save**.

  7. Verify that the principal is listed with the role that you granted.




## What's next

  * To get started using Cloud DNS, see [Quickstart: Set up DNS records for a domain name with Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
