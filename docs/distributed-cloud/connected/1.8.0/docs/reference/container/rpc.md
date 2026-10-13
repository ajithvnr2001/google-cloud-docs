---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/
title: Distributed Cloud Edge Container API \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:09.241997+00:00
---

# Distributed Cloud Edge Container API  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  Distributed Cloud Edge Container API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: edgecontainer.googleapis.com

The Service name `edgecontainer.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.edgecontainer.v1.EdgeContainer](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer)`

Methods  
---  
``[CreateCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.CreateCluster)`` |  Creates a new Cluster in a given project and location.  
``[CreateNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.CreateNodePool)`` |  Creates a new NodePool in a given project and location.  
``[CreateVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.CreateVpnConnection)`` |  Creates a new VPN connection in a given project and location.  
``[DeleteCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.DeleteCluster)`` |  Deletes a single Cluster.  
``[DeleteNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.DeleteNodePool)`` |  Deletes a single NodePool.  
``[DeleteVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.DeleteVpnConnection)`` |  Deletes a single VPN connection.  
``[GenerateAccessToken](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GenerateAccessToken)`` |  Generates an access token for a Cluster.  
``[GenerateOfflineCredential](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GenerateOfflineCredential)`` |  Generates an offline credential for a Cluster.  
``[GetCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GetCluster)`` |  Gets details of a single Cluster.  
``[GetMachine](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GetMachine)`` |  Gets details of a single Machine.  
``[GetNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GetNodePool)`` |  Gets details of a single NodePool.  
``[GetServerConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GetServerConfig)`` |  Gets the server config.  
``[GetVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.GetVpnConnection)`` |  Gets details of a single VPN connection.  
``[ListClusters](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.ListClusters)`` |  Lists Clusters in a given project and location.  
``[ListMachines](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.ListMachines)`` |  Lists Machines in a given project and location.  
``[ListNodePools](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.ListNodePools)`` |  Lists NodePools in a given project and location.  
``[ListVpnConnections](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.ListVpnConnections)`` |  Lists VPN connections in a given project and location.  
``[UpdateCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.UpdateCluster)`` |  Updates the parameters of a single Cluster.  
``[UpdateNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.UpdateNodePool)`` |  Updates the parameters of a single NodePool.  
``[UpgradeCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1#google.cloud.edgecontainer.v1.EdgeContainer.UpgradeCluster)`` |  Upgrades a single cluster.  
  
## `[google.cloud.edgecontainer.v1alpha.EdgeContainer](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer)`

Methods  
---  
``[CreateCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.CreateCluster)`` |  Creates a new Cluster in a given project and location.  
``[CreateNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.CreateNodePool)`` |  Creates a new NodePool in a given project and location.  
``[CreateVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.CreateVpnConnection)`` |  Creates a new VPN connection in a given project and location.  
``[DeleteCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.DeleteCluster)`` |  Deletes a single Cluster.  
``[DeleteNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.DeleteNodePool)`` |  Deletes a single NodePool.  
``[DeleteVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.DeleteVpnConnection)`` |  Deletes a single VPN connection.  
``[DisableZonalService](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.DisableZonalService)`` |  DisableZonalService removes service access from the zone.  
``[EnableZonalProject](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.EnableZonalProject)`` |  EnableZonalProject enables consumer project on the zone.  
``[EnableZonalService](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.EnableZonalService)`` |  EnableZonalService enables a service on a zone.  
``[GenerateAccessToken](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GenerateAccessToken)`` |  Generates an access token for a Cluster.  
``[GenerateOfflineCredential](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GenerateOfflineCredential)`` |  Generates an offline credential for a Cluster.  
``[GetCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetCluster)`` |  Gets details of a single Cluster.  
``[GetMachine](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetMachine)`` |  Gets details of a single Machine.  
``[GetNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetNodePool)`` |  Gets details of a single NodePool.  
``[GetServerConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetServerConfig)`` |  Gets the server config.  
``[GetVpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetVpnConnection)`` |  Gets details of a single VPN connection.  
``[GetZonalProject](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetZonalProject)`` |  GetZonalProject gets the ZonalProject.  
``[GetZonalService](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetZonalService)`` |  Get EnabledZonalService gets the enabled service details.  
``[GetZone](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.GetZone)`` |  Gets details of a single Zone on which the parent organization is enabled.  
``[ListClusters](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListClusters)`` |  Lists Clusters in a given project and location.  
``[ListMachines](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListMachines)`` |  Lists Machines in a given project and location.  
``[ListNodePools](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListNodePools)`` |  Lists NodePools in a given project and location.  
``[ListVpnConnections](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListVpnConnections)`` |  Lists VPN connections in a given project and location.  
``[ListZonalProjects](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListZonalProjects)`` |  Lists ZonalProjects on the zone.  
``[ListZonalServices](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListZonalServices)`` |  Lists ZonalServices in a given project and location.  
``[ListZones](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.ListZones)`` |  Lists Zones on which the parent organization is enabled.  
``[UpdateCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.UpdateCluster)`` |  Updates the parameters of a single Cluster.  
``[UpdateNodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.UpdateNodePool)`` |  Updates the parameters of a single NodePool.  
``[UpgradeCluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer.UpgradeCluster)`` |  Upgrades a single cluster.  
  
## `[google.cloud.location.Locations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
``[GetLocation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation)`` |  Gets information about a location.  
``[ListLocations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations)`` |  Lists information about the supported locations for this service.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[CancelOperation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)`` |  Starts asynchronous cancellation on a long-running operation.  
``[DeleteOperation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)`` |  Deletes a long-running operation.  
``[GetOperation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
