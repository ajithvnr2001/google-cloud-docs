---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/
title: VMware Engine API \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:41:23.431192+00:00
---

# VMware Engine API  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  VMware Engine API Stay organized with collections  Save and categorize content based on your preferences. 

The Google VMware Engine API lets you programmatically manage VMware environments.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.announcements
  * REST Resource: v1.projects.locations.datastores
  * REST Resource: v1.projects.locations.dnsBindPermission
  * REST Resource: v1.projects.locations.networkPeerings
  * REST Resource: v1.projects.locations.networkPeerings.peeringRoutes
  * REST Resource: v1.projects.locations.networkPolicies
  * REST Resource: v1.projects.locations.networkPolicies.externalAccessRules
  * REST Resource: v1.projects.locations.nodeTypes
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.privateClouds
  * REST Resource: v1.projects.locations.privateClouds.clusters
  * REST Resource: v1.projects.locations.privateClouds.clusters.nodes
  * REST Resource: v1.projects.locations.privateClouds.externalAddresses
  * REST Resource: v1.projects.locations.privateClouds.hcxActivationKeys
  * REST Resource: v1.projects.locations.privateClouds.loggingServers
  * REST Resource: v1.projects.locations.privateClouds.managementDnsZoneBindings
  * REST Resource: v1.projects.locations.privateClouds.subnets
  * REST Resource: v1.projects.locations.privateClouds.upgrades
  * REST Resource: v1.projects.locations.privateConnections
  * REST Resource: v1.projects.locations.privateConnections.peeringRoutes
  * REST Resource: v1.projects.locations.vmwareEngineNetworks



## Service: vmwareengine.googleapis.com

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://vmwareengine.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getDnsBindPermission](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations/getDnsBindPermission)` |  `GET /v1/{name=projects/*/locations/*/dnsBindPermission}`   
Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.announcements](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements/get)` |  `GET /v1/{name=projects/*/locations/*/announcements/*}`   
Retrieves a `Announcement` by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements/list)` |  `GET /v1/{parent=projects/*/locations/*}/announcements`   
Lists `Announcements` for a given region and project  
  
## REST Resource: [v1.projects.locations.datastores](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/create)` |  `POST /v1/{parent=projects/*/locations/*}/datastores`   
Creates a new `Datastore` resource in a given project and location.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/delete)` |  `DELETE /v1/{name=projects/*/locations/*/datastores/*}`   
Deletes a `Datastore` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/get)` |  `GET /v1/{name=projects/*/locations/*/datastores/*}`   
Retrieves a `Datastore` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/list)` |  `GET /v1/{parent=projects/*/locations/*}/datastores`   
Lists `Datastore` resources in a given project and location.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/patch)` |  `PATCH /v1/{datastore.name=projects/*/locations/*/datastores/*}`   
Modifies a Datastore resource.  
  
## REST Resource: [v1.projects.locations.dnsBindPermission](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.dnsBindPermission)

Methods  
---  
`[grant](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.dnsBindPermission/grant)` |  `POST /v1/{name=projects/*/locations/*/dnsBindPermission}:grant`   
Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project.  
`[revoke](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.dnsBindPermission/revoke)` |  `POST /v1/{name=projects/*/locations/*/dnsBindPermission}:revoke`   
Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project.  
  
## REST Resource: [v1.projects.locations.networkPeerings](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/create)` |  `POST /v1/{parent=projects/*/locations/*}/networkPeerings`   
Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/networkPeerings/*}`   
Deletes a `NetworkPeering` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/get)` |  `GET /v1/{name=projects/*/locations/*/networkPeerings/*}`   
Retrieves a `NetworkPeering` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/list)` |  `GET /v1/{parent=projects/*/locations/*}/networkPeerings`   
Lists `NetworkPeering` resources in a given project.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/patch)` |  `PATCH /v1/{networkPeering.name=projects/*/locations/*/networkPeerings/*}`   
Modifies a `NetworkPeering` resource.  
  
## REST Resource: [v1.projects.locations.networkPeerings.peeringRoutes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings.peeringRoutes)

Methods  
---  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings.peeringRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*/networkPeerings/*}/peeringRoutes`   
Lists the network peering routes exchanged over a peering connection.  
  
## REST Resource: [v1.projects.locations.networkPolicies](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/networkPolicies`   
Creates a new network policy in a given VMware Engine network of a project and location (region).  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/networkPolicies/*}`   
Deletes a `NetworkPolicy` resource.  
`[fetchExternalAddresses](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/fetchExternalAddresses)` |  `GET /v1/{networkPolicy=projects/*/locations/*/networkPolicies/*}:fetchExternalAddresses`   
Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/networkPolicies/*}`   
Retrieves a `NetworkPolicy` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/networkPolicies`   
Lists `NetworkPolicy` resources in a specified project and location.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/patch)` |  `PATCH /v1/{networkPolicy.name=projects/*/locations/*/networkPolicies/*}`   
Modifies a `NetworkPolicy` resource.  
  
## REST Resource: [v1.projects.locations.networkPolicies.externalAccessRules](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/create)` |  `POST /v1/{parent=projects/*/locations/*/networkPolicies/*}/externalAccessRules`   
Creates a new external access rule in a given network policy.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/delete)` |  `DELETE /v1/{name=projects/*/locations/*/networkPolicies/*/externalAccessRules/*}`   
Deletes a single external access rule.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/get)` |  `GET /v1/{name=projects/*/locations/*/networkPolicies/*/externalAccessRules/*}`   
Gets details of a single external access rule.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/list)` |  `GET /v1/{parent=projects/*/locations/*/networkPolicies/*}/externalAccessRules`   
Lists `ExternalAccessRule` resources in the specified network policy.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/patch)` |  `PATCH /v1/{externalAccessRule.name=projects/*/locations/*/networkPolicies/*/externalAccessRules/*}`   
Updates the parameters of a single external access rule.  
  
## REST Resource: [v1.projects.locations.nodeTypes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/get)` |  `GET /v1/{name=projects/*/locations/*/nodeTypes/*}`   
Gets details of a single `NodeType`.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/list)` |  `GET /v1/{parent=projects/*/locations/*}/nodeTypes`   
Lists node types  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.privateClouds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/create)` |  `POST /v1/{parent=projects/*/locations/*}/privateClouds`   
Creates a new `PrivateCloud` resource in a given project and location.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateClouds/*}`   
Schedules a `PrivateCloud` resource for deletion.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*}`   
Retrieves a `PrivateCloud` resource by its resource name.  
`[getDnsForwarding](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/getDnsForwarding)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/dnsForwarding}`   
Gets details of the `DnsForwarding` config.  
`[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/privateClouds/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/list)` |  `GET /v1/{parent=projects/*/locations/*}/privateClouds`   
Lists `PrivateCloud` resources in a given project and location.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/patch)` |  `PATCH /v1/{privateCloud.name=projects/*/locations/*/privateClouds/*}`   
Modifies a `PrivateCloud` resource.  
`[privateCloudDeletionNow](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/privateCloudDeletionNow)` |  `POST /v1/{name=projects/*/locations/*/privateClouds/*}:privateCloudDeletionNow`   
Accelerates the deletion of a private cloud that is currently in soft deletion A `PrivateCloud` resource in soft deletion has `PrivateCloud.state` set to `SOFT_DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.  
`[resetNsxCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/resetNsxCredentials)` |  `POST /v1/{privateCloud=projects/*/locations/*/privateClouds/*}:resetNsxCredentials`   
Resets credentials of the NSX appliance.  
`[resetVcenterCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/resetVcenterCredentials)` |  `POST /v1/{privateCloud=projects/*/locations/*/privateClouds/*}:resetVcenterCredentials`   
Resets credentials of the Vcenter appliance.  
`[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[showNsxCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/showNsxCredentials)` |  `GET /v1/{privateCloud=projects/*/locations/*/privateClouds/*}:showNsxCredentials`   
Gets details of credentials for NSX appliance.  
`[showVcenterCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/showVcenterCredentials)` |  `GET /v1/{privateCloud=projects/*/locations/*/privateClouds/*}:showVcenterCredentials`   
Gets details of credentials for Vcenter appliance.  
`[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[undelete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/undelete)` |  `POST /v1/{name=projects/*/locations/*/privateClouds/*}:undelete`   
Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`.  
`[updateDnsForwarding](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/updateDnsForwarding)` |  `PATCH /v1/{dnsForwarding.name=projects/*/locations/*/privateClouds/*/dnsForwarding}`   
Updates the parameters of the `DnsForwarding` config, like associated domains.  
  
## REST Resource: [v1.projects.locations.privateClouds.clusters](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/create)` |  `POST /v1/{parent=projects/*/locations/*/privateClouds/*}/clusters`   
Creates a new cluster in a given private cloud.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateClouds/*/clusters/*}`   
Deletes a `Cluster` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/clusters/*}`   
Retrieves a `Cluster` resource by its resource name.  
`[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/privateClouds/*/clusters/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/clusters`   
Lists `Cluster` resources in a given private cloud.  
`[mountDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/mountDatastore)` |  `POST /v1/{name=projects/*/locations/*/privateClouds/*/clusters/*}:mountDatastore`   
Mounts a `Datastore` on a cluster resource  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/patch)` |  `PATCH /v1/{cluster.name=projects/*/locations/*/privateClouds/*/clusters/*}`   
Modifies a `Cluster` resource.  
`[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*/clusters/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*/clusters/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[unmountDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/unmountDatastore)` |  `POST /v1/{name=projects/*/locations/*/privateClouds/*/clusters/*}:unmountDatastore`   
Unmounts a `Datastore` on a cluster resource  
  
## REST Resource: [v1.projects.locations.privateClouds.clusters.nodes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/clusters/*/nodes/*}`   
Gets details of a single node.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*/clusters/*}/nodes`   
Lists nodes in a given cluster.  
  
## REST Resource: [v1.projects.locations.privateClouds.externalAddresses](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses/create)` |  `POST /v1/{parent=projects/*/locations/*/privateClouds/*}/externalAddresses`   
Creates a new `ExternalAddress` resource in a given private cloud.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateClouds/*/externalAddresses/*}`   
Deletes a single external IP address.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/externalAddresses/*}`   
Gets details of a single external IP address.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/externalAddresses`   
Lists external IP addresses assigned to VMware workload VMs in a given private cloud.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses/patch)` |  `PATCH /v1/{externalAddress.name=projects/*/locations/*/privateClouds/*/externalAddresses/*}`   
Updates the parameters of a single external IP address.  
  
## REST Resource: [v1.projects.locations.privateClouds.hcxActivationKeys](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/create)` |  `POST /v1/{parent=projects/*/locations/*/privateClouds/*}/hcxActivationKeys`   
Creates a new HCX activation key in a given private cloud.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/hcxActivationKeys/*}`   
Retrieves a `HcxActivationKey` resource by its resource name.  
`[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/privateClouds/*/hcxActivationKeys/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/hcxActivationKeys`   
Lists `HcxActivationKey` resources in a given private cloud.  
`[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*/hcxActivationKeys/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/privateClouds/*/hcxActivationKeys/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.privateClouds.loggingServers](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/create)` |  `POST /v1/{parent=projects/*/locations/*/privateClouds/*}/loggingServers`   
Create a new logging server for a given private cloud.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateClouds/*/loggingServers/*}`   
Deletes a single logging server.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/loggingServers/*}`   
Gets details of a logging server.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/loggingServers`   
Lists logging servers configured for a given private cloud.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/patch)` |  `PATCH /v1/{loggingServer.name=projects/*/locations/*/privateClouds/*/loggingServers/*}`   
Updates the parameters of a single logging server.  
  
## REST Resource: [v1.projects.locations.privateClouds.managementDnsZoneBindings](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/create)` |  `POST /v1/{parent=projects/*/locations/*/privateClouds/*}/managementDnsZoneBindings`   
Creates a new `ManagementDnsZoneBinding` resource in a private cloud.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateClouds/*/managementDnsZoneBindings/*}`   
Deletes a `ManagementDnsZoneBinding` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/managementDnsZoneBindings/*}`   
Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/managementDnsZoneBindings`   
Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/patch)` |  `PATCH /v1/{managementDnsZoneBinding.name=projects/*/locations/*/privateClouds/*/managementDnsZoneBindings/*}`   
Updates a `ManagementDnsZoneBinding` resource.  
`[repair](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/repair)` |  `POST /v1/{name=projects/*/locations/*/privateClouds/*/managementDnsZoneBindings/*}:repair`   
Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.  
  
## REST Resource: [v1.projects.locations.privateClouds.subnets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/subnets/*}`   
Gets details of a single subnet.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/subnets`   
Lists subnets in a given private cloud.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/patch)` |  `PATCH /v1/{subnet.name=projects/*/locations/*/privateClouds/*/subnets/*}`   
Updates the parameters of a single subnet.  
  
## REST Resource: [v1.projects.locations.privateClouds.upgrades](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades)

Methods  
---  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/get)` |  `GET /v1/{name=projects/*/locations/*/privateClouds/*/upgrades/*}`   
Retrieves a private cloud `Upgrade` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/list)` |  `GET /v1/{parent=projects/*/locations/*/privateClouds/*}/upgrades`   
Lists past, ongoing and upcoming `Upgrades` for the given private cloud.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/patch)` |  `PATCH /v1/{upgrade.name=projects/*/locations/*/privateClouds/*/upgrades/*}`   
Update the private cloud `Upgrade` resource.  
  
## REST Resource: [v1.projects.locations.privateConnections](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/create)` |  `POST /v1/{parent=projects/*/locations/*}/privateConnections`   
Creates a new private connection that can be used for accessing private Clouds.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/privateConnections/*}`   
Deletes a `PrivateConnection` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/get)` |  `GET /v1/{name=projects/*/locations/*/privateConnections/*}`   
Retrieves a `PrivateConnection` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/list)` |  `GET /v1/{parent=projects/*/locations/*}/privateConnections`   
Lists `PrivateConnection` resources in a given project and location.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/patch)` |  `PATCH /v1/{privateConnection.name=projects/*/locations/*/privateConnections/*}`   
Modifies a `PrivateConnection` resource.  
  
## REST Resource: [v1.projects.locations.privateConnections.peeringRoutes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections.peeringRoutes)

Methods  
---  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections.peeringRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*/privateConnections/*}/peeringRoutes`   
Lists the private connection routes exchanged over a peering connection.  
  
## REST Resource: [v1.projects.locations.vmwareEngineNetworks](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks)

Methods  
---  
`[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/create)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareEngineNetworks`   
Creates a new VMware Engine network that can be used by a private cloud.  
`[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/delete)` |  `DELETE /v1/{name=projects/*/locations/*/vmwareEngineNetworks/*}`   
Deletes a `VmwareEngineNetwork` resource.  
`[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/get)` |  `GET /v1/{name=projects/*/locations/*/vmwareEngineNetworks/*}`   
Retrieves a `VmwareEngineNetwork` resource by its resource name.  
`[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/list)` |  `GET /v1/{parent=projects/*/locations/*}/vmwareEngineNetworks`   
Lists `VmwareEngineNetwork` resources in a given project and location.  
`[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/patch)` |  `PATCH /v1/{vmwareEngineNetwork.name=projects/*/locations/*/vmwareEngineNetworks/*}`   
Modifies a VMware Engine network resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
