---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dns/
title: Cloud DNS roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:23.806166+00:00
---

# Cloud DNS roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud DNS roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud DNS. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud DNS roles

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
  
## Cloud DNS permissions

Permission | Included in roles  
---|---  
  
#### `dns.changes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.changes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.changes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.dnsKeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.dnsKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.gkeClusters.bindDNSResponsePolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.gkeClusters.bindPrivateDNSZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZoneOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZoneOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Composer Shared VPC Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.sharedVpcAgent) (`roles/composer.sharedVpcAgent`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Composer Shared VPC Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.sharedVpcAgent) (`roles/composer.sharedVpcAgent`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Attack Surface Management Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackSurfaceManagementScannerServiceAgent) (`roles/securitycenter.attackSurfaceManagementScannerServiceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.managedZones.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `dns.managedZones.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.networks.bindDNSResponsePolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.networks.bindPrivateDNSPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.networks.bindPrivateDNSZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `dns.networks.targetWithPeeringZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Composer Shared VPC Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.sharedVpcAgent) (`roles/composer.sharedVpcAgent`)  [DNS Peer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.peer) (`roles/dns.peer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Agent Gateway Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/agentgateway#agentgateway.serviceAgent) (`roles/agentgateway.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 
  * [Managed Flink Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent) (`roles/managedflink.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `dns.networks.useHealthSignals`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `dns.policies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `dns.policies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.policies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.projects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.resourceRecordSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.resourceRecordSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.resourceRecordSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.resourceRecordSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Attack Surface Management Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackSurfaceManagementScannerServiceAgent) (`roles/securitycenter.attackSurfaceManagementScannerServiceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.resourceRecordSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicyRules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicyRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicyRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicyRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [DNS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.viewer) (`roles/dns.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [DNS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.reader) (`roles/dns.reader`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `dns.responsePolicyRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [DNS Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)  [DNS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.editor) (`roles/dns.editor`)  [Kubernetes Engine Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Managed Identities Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent) (`roles/managedidentities.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 
  * [Service Networking Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent) (`roles/servicenetworking.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
