---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking/
title: Service Networking roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:11.768715+00:00
---

# Service Networking roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Networking roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Networking. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Networking roles

Role | Permissions  
---|---  
  
#### Service Networking Admin Beta

(`roles/servicenetworking.admin`) Admin role for Service Networking  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicenetworking.*`

  * `servicenetworking.operations.cancel`
  * `servicenetworking.operations.delete`
  * `servicenetworking.operations.get`
  * `servicenetworking.operations.list`
  * `servicenetworking.services.addDnsRecordSet`
  * `servicenetworking.services.addDnsZone`
  * `servicenetworking.services.addPeering`
  * `servicenetworking.services.addSubnetwork`
  * `servicenetworking.services.createPeeredDnsDomain`
  * `servicenetworking.services.deleteConnection`
  * `servicenetworking.services.deletePeeredDnsDomain`
  * `servicenetworking.services.disableVpcServiceControls`
  * `servicenetworking.services.enableVpcServiceControls`
  * `servicenetworking.services.get`
  * `servicenetworking.services.getConsumerConfig`
  * `servicenetworking.services.getVpcServiceControls`
  * `servicenetworking.services.listPeeredDnsDomains`
  * `servicenetworking.services.removeDnsRecordSet`
  * `servicenetworking.services.removeDnsZone`
  * `servicenetworking.services.updateConsumerConfig`
  * `servicenetworking.services.updateDnsRecordSet`
  * `servicenetworking.services.use`

  
  
#### Service Networking Editor Beta

(`roles/servicenetworking.editor`) Editor role for Service Networking  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicenetworking.operations.*`

  * `servicenetworking.operations.cancel`
  * `servicenetworking.operations.delete`
  * `servicenetworking.operations.get`
  * `servicenetworking.operations.list`

`servicenetworking.services.addDnsRecordSet` `servicenetworking.services.addDnsZone` `servicenetworking.services.addSubnetwork` `servicenetworking.services.createPeeredDnsDomain` `servicenetworking.services.deleteConnection` `servicenetworking.services.deletePeeredDnsDomain` `servicenetworking.services.disableVpcServiceControls` `servicenetworking.services.enableVpcServiceControls` `servicenetworking.services.get` `servicenetworking.services.getConsumerConfig` `servicenetworking.services.getVpcServiceControls` `servicenetworking.services.listPeeredDnsDomains` `servicenetworking.services.removeDnsRecordSet` `servicenetworking.services.removeDnsZone` `servicenetworking.services.updateConsumerConfig` `servicenetworking.services.updateDnsRecordSet` `servicenetworking.services.use`  
  
#### Service Networking Viewer Beta

(`roles/servicenetworking.viewer`) Viewer role for Service Networking  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicenetworking.operations.get` `servicenetworking.operations.list` `servicenetworking.services.get` `servicenetworking.services.getConsumerConfig` `servicenetworking.services.getVpcServiceControls` `servicenetworking.services.listPeeredDnsDomains` `servicenetworking.services.use`  
  
#### Service Networking Admin Beta

(`roles/servicenetworking.networksAdmin`) Full control of service networking with projects.  |  `servicenetworking.*`

  * `servicenetworking.operations.cancel`
  * `servicenetworking.operations.delete`
  * `servicenetworking.operations.get`
  * `servicenetworking.operations.list`
  * `servicenetworking.services.addDnsRecordSet`
  * `servicenetworking.services.addDnsZone`
  * `servicenetworking.services.addPeering`
  * `servicenetworking.services.addSubnetwork`
  * `servicenetworking.services.createPeeredDnsDomain`
  * `servicenetworking.services.deleteConnection`
  * `servicenetworking.services.deletePeeredDnsDomain`
  * `servicenetworking.services.disableVpcServiceControls`
  * `servicenetworking.services.enableVpcServiceControls`
  * `servicenetworking.services.get`
  * `servicenetworking.services.getConsumerConfig`
  * `servicenetworking.services.getVpcServiceControls`
  * `servicenetworking.services.listPeeredDnsDomains`
  * `servicenetworking.services.removeDnsRecordSet`
  * `servicenetworking.services.removeDnsZone`
  * `servicenetworking.services.updateConsumerConfig`
  * `servicenetworking.services.updateDnsRecordSet`
  * `servicenetworking.services.use`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Service Networking Service Agent 

(`roles/servicenetworking.serviceAgent`) Gives permission to manage network configuration, such as establishing network peering, necessary for service producers  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalOperations.get` `compute.networks.addPeering` `compute.networks.create` `compute.networks.delete` `compute.networks.get` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.networks.removePeering` `compute.networks.update` `compute.networks.updatePeering` `compute.networks.updatePolicy` `compute.projects.get` `compute.regionOperations.get` `compute.routers.get` `compute.routers.list` `compute.routes.list` `compute.subnetworks.create` `compute.subnetworks.delete` `compute.subnetworks.get` `compute.subnetworks.list` `dns.changes.*`

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

`networkconnectivity.internalRanges.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Service Networking permissions

Permission | Included in roles  
---|---  
  
#### `servicenetworking.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicenetworking.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.addDnsRecordSet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.addDnsZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.addPeering`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicenetworking.services.addSubnetwork`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.createPeeredDnsDomain`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 

  
  
#### `servicenetworking.services.deleteConnection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicenetworking.services.deletePeeredDnsDomain`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicenetworking.services.disableVpcServiceControls`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 

  
  
#### `servicenetworking.services.enableVpcServiceControls`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 

  
  
#### `servicenetworking.services.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 

  
  
#### `servicenetworking.services.getConsumerConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.getVpcServiceControls`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 

  
  
#### `servicenetworking.services.listPeeredDnsDomains`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `servicenetworking.services.removeDnsRecordSet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.removeDnsZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.updateConsumerConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.updateDnsRecordSet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
#### `servicenetworking.services.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.admin) (`roles/servicenetworking.admin`)  [Service Networking Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.editor) (`roles/servicenetworking.editor`)  [Service Networking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.viewer) (`roles/servicenetworking.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Service Networking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin) (`roles/servicenetworking.networksAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
