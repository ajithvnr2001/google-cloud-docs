---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha
title: Package google.cloud.edgecontainer.v1alpha \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:09.444135+00:00
---

# Package google.cloud.edgecontainer.v1alpha  |  Google Distributed Cloud connected, version 1.6.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha

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
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/apis)



Send feedback 

#  Package google.cloud.edgecontainer.v1alpha Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[EdgeContainer](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.EdgeContainer)` (interface)
  * `[Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Authorization)` (message)
  * `[ChannelConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ChannelConfig)` (message)
  * `[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster)` (message)
  * `[Cluster.ControlPlane](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane)` (message)
  * `[Cluster.ControlPlane.Local](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.Local)` (message)
  * `[Cluster.ControlPlane.Remote](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.Remote)` (message)
  * `[Cluster.ControlPlane.SharedDeploymentPolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.SharedDeploymentPolicy)` (enum)
  * `[Cluster.ControlPlaneEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlaneEncryption)` (message)
  * `[Cluster.MaintenanceEvent](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent)` (message)
  * `[Cluster.MaintenanceEvent.Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.Schedule)` (enum)
  * `[Cluster.MaintenanceEvent.State](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.State)` (enum)
  * `[Cluster.MaintenanceEvent.Type](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.Type)` (enum)
  * `[Cluster.ReleaseChannel](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ReleaseChannel)` (enum)
  * `[Cluster.Status](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.Status)` (enum)
  * `[Cluster.SurvivabilityConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SurvivabilityConfig)` (message)
  * `[Cluster.SystemAddonsConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SystemAddonsConfig)` (message)
  * `[Cluster.SystemAddonsConfig.Ingress](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SystemAddonsConfig.Ingress)` (message)
  * `[ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ClusterNetworking)` (message)
  * `[ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ClusterUser)` (message)
  * `[CreateClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateClusterRequest)` (message)
  * `[CreateNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateNodePoolRequest)` (message)
  * `[CreateVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateVpnConnectionRequest)` (message)
  * `[DeleteClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteClusterRequest)` (message)
  * `[DeleteNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteNodePoolRequest)` (message)
  * `[DeleteVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteVpnConnectionRequest)` (message)
  * `[Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Fleet)` (message)
  * `[GenerateAccessTokenRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateAccessTokenRequest)` (message)
  * `[GenerateAccessTokenResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateAccessTokenResponse)` (message)
  * `[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateOfflineCredentialRequest)` (message)
  * `[GenerateOfflineCredentialResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateOfflineCredentialResponse)` (message)
  * `[GetClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetClusterRequest)` (message)
  * `[GetMachineRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetMachineRequest)` (message)
  * `[GetNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetNodePoolRequest)` (message)
  * `[GetServerConfigRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetServerConfigRequest)` (message)
  * `[GetVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetVpnConnectionRequest)` (message)
  * `[KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.KmsKeyState)` (enum)
  * `[ListClustersRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListClustersRequest)` (message)
  * `[ListClustersResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListClustersResponse)` (message)
  * `[ListMachinesRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListMachinesRequest)` (message)
  * `[ListMachinesResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListMachinesResponse)` (message)
  * `[ListNodePoolsRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListNodePoolsRequest)` (message)
  * `[ListNodePoolsResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListNodePoolsResponse)` (message)
  * `[ListVpnConnectionsRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListVpnConnectionsRequest)` (message)
  * `[ListVpnConnectionsResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListVpnConnectionsResponse)` (message)
  * `[LocationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.LocationMetadata)` (message)
  * `[Machine](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Machine)` (message)
  * `[MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.MaintenancePolicy)` (message)
  * `[MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.MaintenanceWindow)` (message)
  * `[NodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool)` (message)
  * `[NodePool.LocalDiskEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool.LocalDiskEncryption)` (message)
  * `[NodePool.NodeConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool.NodeConfig)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.OperationMetadata)` (message)
  * `[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Quota)` (message)
  * `[RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.RecurringTimeWindow)` (message)
  * `[ServerConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ServerConfig)` (message)
  * `[TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.TimeWindow)` (message)
  * `[UpdateClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpdateClusterRequest)` (message)
  * `[UpdateNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpdateNodePoolRequest)` (message)
  * `[UpgradeClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpgradeClusterRequest)` (message)
  * `[UpgradeClusterRequest.Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpgradeClusterRequest.Schedule)` (enum)
  * `[Version](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Version)` (message)
  * `[VpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection)` (message)
  * `[VpnConnection.BgpRoutingMode](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.BgpRoutingMode)` (enum)
  * `[VpnConnection.Details](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details)` (message)
  * `[VpnConnection.Details.CloudRouter](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.CloudRouter)` (message)
  * `[VpnConnection.Details.CloudVpn](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.CloudVpn)` (message)
  * `[VpnConnection.Details.State](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.State)` (enum)
  * `[VpnConnection.VpcProject](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.VpcProject)` (message)
  * `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ZoneMetadata)` (message)
  * `[ZoneMetadata.RackType](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ZoneMetadata.RackType)` (enum)



## EdgeContainer

EdgeContainer API provides management of Kubernetes Clusters on Google Edge Cloud deployments.

CreateCluster  
---  
` rpc CreateCluster(`[CreateClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateClusterRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Cluster in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateNodePool  
---  
` rpc CreateNodePool(`[CreateNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateNodePoolRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new NodePool in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateVpnConnection  
---  
` rpc CreateVpnConnection(`[CreateVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.CreateVpnConnectionRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new VPN connection in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteCluster  
---  
` rpc DeleteCluster(`[DeleteClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteClusterRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single Cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteNodePool  
---  
` rpc DeleteNodePool(`[DeleteNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteNodePoolRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single NodePool.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteVpnConnection  
---  
` rpc DeleteVpnConnection(`[DeleteVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.DeleteVpnConnectionRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single VPN connection.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GenerateAccessToken  
---  
` rpc GenerateAccessToken(`[GenerateAccessTokenRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateAccessTokenRequest)`) returns (`[GenerateAccessTokenResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateAccessTokenResponse)`) ` Generates an access token for a Cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GenerateOfflineCredential  
---  
` rpc GenerateOfflineCredential(`[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateOfflineCredentialRequest)`) returns (`[GenerateOfflineCredentialResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GenerateOfflineCredentialResponse)`) ` Generates an offline credential for a Cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetCluster  
---  
` rpc GetCluster(`[GetClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetClusterRequest)`) returns (`[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster)`) ` Gets details of a single Cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetMachine  
---  
` rpc GetMachine(`[GetMachineRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetMachineRequest)`) returns (`[Machine](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Machine)`) ` Gets details of a single Machine.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetNodePool  
---  
` rpc GetNodePool(`[GetNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetNodePoolRequest)`) returns (`[NodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool)`) ` Gets details of a single NodePool.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetServerConfig  
---  
` rpc GetServerConfig(`[GetServerConfigRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetServerConfigRequest)`) returns (`[ServerConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ServerConfig)`) ` Gets the server config.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetVpnConnection  
---  
` rpc GetVpnConnection(`[GetVpnConnectionRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.GetVpnConnectionRequest)`) returns (`[VpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection)`) ` Gets details of a single VPN connection.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListClusters  
---  
` rpc ListClusters(`[ListClustersRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListClustersRequest)`) returns (`[ListClustersResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListClustersResponse)`) ` Lists Clusters in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListMachines  
---  
` rpc ListMachines(`[ListMachinesRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListMachinesRequest)`) returns (`[ListMachinesResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListMachinesResponse)`) ` Lists Machines in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListNodePools  
---  
` rpc ListNodePools(`[ListNodePoolsRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListNodePoolsRequest)`) returns (`[ListNodePoolsResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListNodePoolsResponse)`) ` Lists NodePools in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListVpnConnections  
---  
` rpc ListVpnConnections(`[ListVpnConnectionsRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListVpnConnectionsRequest)`) returns (`[ListVpnConnectionsResponse](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ListVpnConnectionsResponse)`) ` Lists VPN connections in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateCluster  
---  
` rpc UpdateCluster(`[UpdateClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpdateClusterRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single Cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateNodePool  
---  
` rpc UpdateNodePool(`[UpdateNodePoolRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpdateNodePoolRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single NodePool.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpgradeCluster  
---  
` rpc UpgradeCluster(`[UpgradeClusterRequest](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpgradeClusterRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.longrunning#google.longrunning.Operation)`) ` Upgrades a single cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## Authorization

RBAC policy that will be applied and managed by GEC.

Fields  
---  
`admin_users` |  ``[ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ClusterUser)`` Required. User that will be granted the cluster-admin role on the cluster, providing full access to the cluster. Currently, this is a singular field, but will be expanded to allow multiple admins in the future.  
  
## ChannelConfig

Configuration for a release channel.

Fields  
---  
`default_version` |  `string` Output only. Default version for this release channel, e.g.: "1.4.0".  
  
## Cluster

A Google Distributed Cloud Edge Kubernetes cluster.

Fields  
---  
`name` |  `string` Required. The resource name of the cluster.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the cluster was created.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the cluster was last updated.  
`labels` |  `map<string, string>` Labels associated with this resource.  
`fleet` |  ``[Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Fleet)`` Required. Fleet configuration.  
`networking` |  ``[ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ClusterNetworking)`` Required. Cluster-wide networking configuration.  
`authorization` |  ``[Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Authorization)`` Required. Immutable. RBAC policy that will be applied and managed by GEC.  
`default_max_pods_per_node` |  `int32` Optional. The default maximum number of pods per node used if a maximum value is not specified explicitly for a node pool in this cluster. If unspecified, the Kubernetes default value will be used.  
`endpoint` |  `string` Output only. The IP address of the Kubernetes API server.  
`port` |  `int32` Output only. The port number of the Kubernetes API server.  
`cluster_ca_certificate` |  `string` Output only. The PEM-encoded public certificate of the cluster's CA.  
`maintenance_policy` |  ``[MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.MaintenancePolicy)`` Optional. Cluster-wide maintenance policy configuration.  
`control_plane_version` |  `string` Output only. The control plane release version  
`node_version` |  `string` Output only. The lowest release version among all worker nodes. This field can be empty if the cluster does not have any worker nodes.  
`control_plane` |  ``[ControlPlane](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane)`` Optional. The configuration of the cluster control plane.  
`system_addons_config` |  ``[SystemAddonsConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SystemAddonsConfig)`` Optional. The configuration of the system add-ons.  
`external_load_balancer_ipv4_address_pools[]` |  `string` Optional. IPv4 address pools for cluster data plane external load balancing.  
`control_plane_encryption` |  ``[ControlPlaneEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlaneEncryption)`` Optional. Remote control plane disk encryption options. This field is only used when enabling CMEK support.  
`status` |  ``[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.Status)`` Output only. The current status of the cluster.  
`maintenance_events[]` |  ``[MaintenanceEvent](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent)`` Output only. All the maintenance events scheduled for the cluster, including the ones ongoing, planned for the future and done in the past (up to 90 days).  
`target_version` |  `string` Optional. The target cluster version. For example: "1.5.0".  
`release_channel` |  ``[ReleaseChannel](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ReleaseChannel)`` Optional. The release channel a cluster is subscribed to.  
`survivability_config` |  ``[SurvivabilityConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SurvivabilityConfig)`` Optional. Configuration of the cluster survivability, e.g., for the case when network connectivity is lost. Note: This only applies to local control plane clusters.  
`external_load_balancer_ipv6_address_pools[]` |  `string` Optional. IPv6 address pools for cluster data plane external load balancing.  
  
## ControlPlane

Configuration of the cluster control plane.

Fields  
---  
Union field `config`.`config` can be only one of the following:  
`remote` |  ``[Remote](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.Remote)`` Remote control plane configuration.  
`local` |  ``[Local](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.Local)`` Local control plane configuration.Warning: Local control plane clusters must be created in their own project. Local control plane clusters cannot coexist in the same project with any other type of clusters, including non-GDCE clusters. Mixing local control plane GDCE clusters with any other type of clusters in the same project can result in data loss.  
  
## Local

Configuration specific to clusters with a control plane hosted locally.

Warning: Local control plane clusters must be created in their own project. Local control plane clusters cannot coexist in the same project with any other type of clusters, including non-GDCE clusters. Mixing local control plane GDCE clusters with any other type of clusters in the same project can result in data loss.

Fields  
---  
`node_location` |  `string` Name of the Google Distributed Cloud Edge zones where this node pool will be created. For example: `us-central1-edge-customer-a`.  
`node_count` |  `int32` The number of nodes to serve as replicas of the Control Plane.  
`machine_filter` |  `string` Only machines matching this filter will be allowed to host control plane nodes. The filtering language accepts strings like "name=", and is documented here: [AIP-160](https://google.aip.dev/160).  
`shared_deployment_policy` |  ``[SharedDeploymentPolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.ControlPlane.SharedDeploymentPolicy)`` Policy configuration about how user applications are deployed.  
  
## Remote

This type has no fields.

Configuration specific to clusters with a control plane hosted remotely.

## SharedDeploymentPolicy

Represents the policy configuration about how user applications are deployed.

Enums  
---  
`SHARED_DEPLOYMENT_POLICY_UNSPECIFIED` | Unspecified.  
`ALLOWED` | User applications can be deployed both on control plane and worker nodes.  
`DISALLOWED` | User applications can not be deployed on control plane nodes and can only be deployed on worker nodes.  
  
## ControlPlaneEncryption

Configuration for Customer-managed KMS key support for remote control plane cluster disk encryption.

Fields  
---  
`kms_key` |  `string` Immutable. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting control plane disks. If not specified, a Google-managed key will be used instead.  
`kms_key_active_version` |  `string` Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting control plane disks. Only applicable if kms_key is set.  
`kms_key_state` |  ``[KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.KmsKeyState)`` Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.  
`kms_status` |  ``[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.rpc#google.rpc.Status)`` Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kms_key_state` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.  
  
## MaintenanceEvent

A Maintenance Event is an operation that could cause temporary disruptions to the cluster workloads, including Google-driven or user-initiated cluster upgrades, user-initiated cluster configuration changes that require restarting nodes, etc.

Fields  
---  
`uuid` |  `string` Output only. UUID of the maintenance event.  
`target_version` |  `string` Output only. The target version of the cluster.  
`operation` |  `string` Output only. The operation for running the maintenance event. Specified in the format projects/*/locations/*/operations/*. If the maintenance event is split into multiple operations (e.g. due to maintenance windows), the latest one is recorded.  
`type` |  ``[Type](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.Type)`` Output only. The type of the maintenance event.  
`schedule` |  ``[Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.Schedule)`` Output only. The schedule of the maintenance event.  
`state` |  ``[State](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.MaintenanceEvent.State)`` Output only. The state of the maintenance event.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the maintenance event request was created.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the maintenance event started.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the maintenance event ended, either successfully or not. If the maintenance event is split into multiple maintenance windows, end_time is only updated when the whole flow ends.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the maintenance event message was updated.  
  
## Schedule

Indicates when the maintenance event should be performed.

Enums  
---  
`SCHEDULE_UNSPECIFIED` | Unspecified.  
`IMMEDIATELY` | Immediately after receiving the request.  
  
## State

Indicates the maintenance event state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`RECONCILING` | The maintenance event is ongoing. The cluster might be unusable.  
`SUCCEEDED` | The maintenance event succeeded.  
`FAILED` | The maintenance event failed.  
  
## Type

Indicates the maintenance event type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`USER_INITIATED_UPGRADE` | Upgrade initiated by users.  
`GOOGLE_DRIVEN_UPGRADE` | Upgrade driven by Google.  
  
## ReleaseChannel

The release channel a cluster is subscribed to.

Enums  
---  
`RELEASE_CHANNEL_UNSPECIFIED` | Unspecified release channel. This will default to the REGULAR channel.  
`NONE` | No release channel.  
`REGULAR` | Regular release channel.  
  
## Status

Indicates the status of the cluster.

Enums  
---  
`STATUS_UNSPECIFIED` | Status unknown.  
`PROVISIONING` | The cluster is being created.  
`RUNNING` | The cluster is created and fully usable.  
`DELETING` | The cluster is being deleted.  
`ERROR` | The status indicates that some errors occurred while reconciling/deleting the cluster.  
`RECONCILING` | The cluster is undergoing some work such as version upgrades, etc.  
  
## SurvivabilityConfig

Configuration of the cluster survivability, e.g., for the case when network connectivity is lost.

Fields  
---  
`offline_reboot_ttl` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Optional. Time period that allows the cluster nodes to be rebooted and become functional without network connectivity to Google. The default 0 means not allowed. The maximum is 7 days.  
  
## SystemAddonsConfig

Config that customers are allowed to define for GDCE system add-ons.

Fields  
---  
`ingress` |  ``[Ingress](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster.SystemAddonsConfig.Ingress)`` Optional. Config for Ingress.  
  
## Ingress

Config for the Ingress add-on which allows customers to create an Ingress object to manage external access to the servers in a cluster. The add-on consists of istiod and istio-ingress.

Fields  
---  
`disabled` |  `bool` Optional. Whether Ingress is disabled.  
`ipv4_vip` |  `string` Optional. Ingress VIP.  
  
## ClusterNetworking

Cluster-wide networking configuration.

Fields  
---  
`cluster_ipv4_cidr_blocks[]` |  `string` Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these blocks. Only a single block is supported. This field cannot be changed after creation.  
`services_ipv4_cidr_blocks[]` |  `string` Required. All services in the cluster are assigned an RFC1918 IPv4 address from these blocks. Only a single block is supported. This field cannot be changed after creation.  
  
## ClusterUser

A user principal for an RBAC policy.

Fields  
---  
`username` |  `string` Required. An active Google username.  
  
## CreateClusterRequest

Creates a cluster.

Fields  
---  
`parent` |  `string` Required. The parent location where this cluster will be created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.clusters.create`

  
`cluster_id` |  `string` Required. A client-specified unique identifier for the cluster.  
`cluster` |  ``[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster)`` Required. The cluster to create.  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## CreateNodePoolRequest

Creates a node pool.

Fields  
---  
`parent` |  `string` Required. The parent cluster where this node pool will be created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.nodePools.create`

  
`node_pool_id` |  `string` Required. A client-specified unique identifier for the node pool.  
`node_pool` |  ``[NodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool)`` Required. The node pool to create.  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## CreateVpnConnectionRequest

Creates a VPN connection.

Fields  
---  
`parent` |  `string` Required. The parent location where this vpn connection will be created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.vpnConnections.create`

  
`vpn_connection_id` |  `string` Required. The VPN connection identifier.  
`vpn_connection` |  ``[VpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection)`` Required. The VPN connection to create.  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## DeleteClusterRequest

Deletes a cluster.

Fields  
---  
`name` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.clusters.delete`

  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## DeleteNodePoolRequest

Deletes a node pool.

Fields  
---  
`name` |  `string` Required. The resource name of the node pool. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.nodePools.delete`

  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## DeleteVpnConnectionRequest

Deletes a vpn connection.

Fields  
---  
`name` |  `string` Required. The resource name of the vpn connection. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.vpnConnections.delete`

  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## Fleet

Fleet related configuration.

Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems.

Fields  
---  
`project` |  `string` Required. The name of the Fleet host project where this cluster will be registered.Project names are formatted as `projects/<project-number>`.  
`membership` |  `string` Output only. The name of the managed Hub Membership resource associated to this cluster.Membership names are formatted as `projects/<project-number>/locations/global/membership/<cluster-id>`.  
  
## GenerateAccessTokenRequest

Generates an access token for a cluster.

Fields  
---  
`cluster` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `cluster`:

  * `edgecontainer.clusters.get`

  
  
## GenerateAccessTokenResponse

An access token for a cluster.

Fields  
---  
`access_token` |  `string` Output only. Access token to authenticate to k8s api-server.  
`expire_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. Timestamp at which the token will expire.  
  
## GenerateOfflineCredentialRequest

Generates an offline credential(offline) for a cluster.

Fields  
---  
`cluster` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `cluster`:

  * `edgecontainer.clusters.get`

  
  
## GenerateOfflineCredentialResponse

An offline credential for a cluster.

Fields  
---  
`client_certificate` |  `string` Output only. Client certificate to authenticate to k8s api-server.  
`client_key` |  `string` Output only. Client private key to authenticate to k8s api-server.  
`user_id` |  `string` Output only. Client's identity.  
`expire_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. Timestamp at which this credential will expire.  
  
## GetClusterRequest

Gets a cluster.

Fields  
---  
`name` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.clusters.get`

  
  
## GetMachineRequest

Gets a machine.

Fields  
---  
`name` |  `string` Required. The resource name of the machine. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.machines.get`

  
  
## GetNodePoolRequest

Gets a node pool.

Fields  
---  
`name` |  `string` Required. The resource name of the node pool. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.nodePools.get`

  
  
## GetServerConfigRequest

Gets the server config.

Fields  
---  
`name` |  `string` Required. The name (project and location) of the server config to get, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.serverConfig.get`

  
  
## GetVpnConnectionRequest

Gets a VPN connection.

Fields  
---  
`name` |  `string` Required. The resource name of the vpn connection. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.vpnConnections.get`

  
  
## KmsKeyState

Represents the accessibility state of a customer-managed KMS key used for CMEK integration.

Enums  
---  
`KMS_KEY_STATE_UNSPECIFIED` | Unspecified.  
`KMS_KEY_STATE_KEY_AVAILABLE` | The key is available for use, and dependent resources should be accessible.  
`KMS_KEY_STATE_KEY_UNAVAILABLE` | The key is unavailable for an unspecified reason. Dependent resources may be inaccessible.  
  
## ListClustersRequest

Lists clusters in a location.

Fields  
---  
`parent` |  `string` Required. The parent location, which owns this collection of clusters. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.clusters.list`

  
`page_size` |  `int32` The maximum number of resources to list.  
`page_token` |  `string` A page token received from previous list request. A page token received from previous list request.  
`filter` |  `string` Only resources matching this filter will be listed.  
`order_by` |  `string` Specifies the order in which resources will be listed.  
  
## ListClustersResponse

List of clusters in a location.

Fields  
---  
`clusters[]` |  ``[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster)`` Clusters in the location.  
`next_page_token` |  `string` A token to retrieve next page of results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListMachinesRequest

Lists machines in a site.

Fields  
---  
`parent` |  `string` Required. The parent site, which owns this collection of machines. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.machines.list`

  
`page_size` |  `int32` The maximum number of resources to list.  
`page_token` |  `string` A page token received from previous list request.  
`filter` |  `string` Only resources matching this filter will be listed.  
`order_by` |  `string` Specifies the order in which resources will be listed.  
  
## ListMachinesResponse

List of machines in a site.

Fields  
---  
`machines[]` |  ``[Machine](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Machine)`` Machines in the site.  
`next_page_token` |  `string` A token to retrieve next page of results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListNodePoolsRequest

Lists node pools in a cluster.

Fields  
---  
`parent` |  `string` Required. The parent cluster, which owns this collection of node pools. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.nodePools.list`

  
`page_size` |  `int32` The maximum number of resources to list.  
`page_token` |  `string` A page token received from previous list request.  
`filter` |  `string` Only resources matching this filter will be listed.  
`order_by` |  `string` Specifies the order in which resources will be listed.  
  
## ListNodePoolsResponse

List of node pools in a cluster.

Fields  
---  
`node_pools[]` |  ``[NodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool)`` Node pools in the cluster.  
`next_page_token` |  `string` A token to retrieve next page of results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListVpnConnectionsRequest

Lists VPN connections.

Fields  
---  
`parent` |  `string` Required. The parent location, which owns this collection of VPN connections. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.vpnConnections.list`

  
`page_size` |  `int32` The maximum number of resources to list.  
`page_token` |  `string` A page token received from previous list request.  
`filter` |  `string` Only resources matching this filter will be listed.  
`order_by` |  `string` Specifies the order in which resources will be listed.  
  
## ListVpnConnectionsResponse

List of VPN connections in a location.

Fields  
---  
`vpn_connections[]` |  ``[VpnConnection](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection)`` VpnConnections in the location.  
`next_page_token` |  `string` A token to retrieve next page of results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## LocationMetadata

Metadata for a given `[google.cloud.location.Location](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Location)`.

Fields  
---  
`available_zones` |  `map<string, `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ZoneMetadata)`>` The set of available Google Distributed Cloud Edge zones in the location. The map is keyed by the lowercase ID of each zone.  
  
## Machine

A Google Distributed Cloud Edge machine capable of acting as a Kubernetes node.

Fields  
---  
`name` |  `string` Required. The resource name of the machine.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the node pool was created.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the node pool was last updated.  
`labels` |  `map<string, string>` Labels associated with this resource.  
`hosted_node` |  `string` Canonical resource name of the node that this machine is responsible for hosting e.g. projects/{project}/locations/{location}/clusters/{cluster_id}/nodePools/{pool_id}/{node}, Or empty if the machine is not assigned to assume the role of a node.For control plane nodes hosted on edge machines, this will return the following format: "projects/{project}/locations/{location}/clusters/{cluster_id}/controlPlaneNodes/{node}".  
`zone` |  `string` The Google Distributed Cloud Edge zone of this machine.  
`version` |  `string` Output only. The software version of the machine.  
`disabled` |  `bool` Output only. Whether the machine is disabled. If disabled, the machine is unable to enter service.  
  
## MaintenancePolicy

Maintenance policy configuration.

Fields  
---  
`window` |  ``[MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.MaintenanceWindow)`` Specifies the maintenance window in which maintenance may be performed.  
  
## MaintenanceWindow

Maintenance window configuration

Fields  
---  
`recurring_window` |  ``[RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.RecurringTimeWindow)`` Configuration of a recurring maintenance window.  
  
## NodePool

A set of Kubernetes nodes in a cluster with common configuration and specification.

Fields  
---  
`name` |  `string` Required. The resource name of the node pool.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the node pool was created.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the node pool was last updated.  
`labels` |  `map<string, string>` Labels associated with this resource.  
`node_location` |  `string` Name of the Google Distributed Cloud Edge zone where this node pool will be created. For example: `us-central1-edge-customer-a`.  
`node_count` |  `int32` Required. The number of nodes in the pool.  
`machine_filter` |  `string` Only machines matching this filter will be allowed to join the node pool. The filtering language accepts strings like "name=", and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`local_disk_encryption` |  ``[LocalDiskEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool.LocalDiskEncryption)`` Optional. Local disk encryption options. This field is only used when enabling CMEK support.  
`node_version` |  `string` Output only. The lowest release version among all worker nodes.  
`node_config` |  ``[NodeConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool.NodeConfig)`` Optional. Configuration for each node in the NodePool  
  
## LocalDiskEncryption

Configuration for CMEK support for edge machine local disk encryption.

Fields  
---  
`kms_key` |  `string` Immutable. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting node local disks. If not specified, a Google-managed key will be used instead.  
`kms_key_active_version` |  `string` Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting node local disks. Only applicable if kms_key is set.  
`kms_key_state` |  ``[KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.KmsKeyState)`` Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.  
`kms_status` |  ``[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.rpc#google.rpc.Status)`` Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kms_key_state` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.  
  
## NodeConfig

Configuration for each node in the NodePool

Fields  
---  
`labels` |  `map<string, string>` Optional. The Kubernetes node labels  
  
## OperationMetadata

Long-running operation metadata for Edge Container API methods.

Fields  
---  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation was created.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation finished running.  
`target` |  `string` Server-defined resource path for the target of the operation.  
`verb` |  `string` The verb executed by the operation.  
`status_message` |  `string` Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have [Operation.error][] value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` API version used to start the operation.  
`warnings[]` |  `string` Warnings that do not block the operation, but still hold relevant information for the end user to receive.  
  
## Quota

Represents quota for Edge Container resources.

Fields  
---  
`metric` |  `string` Name of the quota metric.  
`limit` |  `double` Quota limit for this metric.  
`usage` |  `double` Current usage of this metric.  
  
## RecurringTimeWindow

Represents an arbitrary window of time that recurs.

Fields  
---  
`window` |  ``[TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.TimeWindow)`` The window of the first recurrence.  
`recurrence` |  `string` An RRULE (<https://tools.ietf.org/html/rfc5545#section-3.8.5.3>) for how this window recurs. They go on for the span of time between the start and end time.  
  
## ServerConfig

Server configuration for supported versions and release channels.

Fields  
---  
`channels` |  `map<string, `[ChannelConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ChannelConfig)`>` Output only. Mapping from release channel to channel config.  
`versions[]` |  ``[Version](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Version)`` Output only. Supported versions, e.g.: ["1.4.0", "1.5.0"].  
`default_version` |  `string` Output only. Default version, e.g.: "1.4.0".  
  
## TimeWindow

Represents an arbitrary window of time.

Fields  
---  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time that the window first starts.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time that the window ends. The end time must take place after the start time.  
  
## UpdateClusterRequest

Updates a cluster.

Fields  
---  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cluster` |  ``[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Cluster)`` The updated cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `cluster`:

  * `edgecontainer.clusters.update`

  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## UpdateNodePoolRequest

Updates a node pool.

Fields  
---  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Field mask is used to specify the fields to be overwritten in the NodePool resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`node_pool` |  ``[NodePool](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.NodePool)`` The updated node pool. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `nodePool`:

  * `edgecontainer.nodePools.update`

  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## UpgradeClusterRequest

Upgrades a cluster.

Fields  
---  
`name` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.clusters.upgrade`

  
`target_version` |  `string` Required. The version the cluster is going to be upgraded to.  
`schedule` |  ``[Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.UpgradeClusterRequest.Schedule)`` The schedule for the upgrade.  
`request_id` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.  
  
## Schedule

Represents the schedule about when the cluster is going to be upgraded.

Enums  
---  
`SCHEDULE_UNSPECIFIED` | Unspecified. The default is to upgrade the cluster immediately which is the only option today.  
`IMMEDIATELY` | The cluster is going to be upgraded immediately after receiving the request.  
  
## Version

Version of a cluster.

Fields  
---  
`name` |  `string` Output only. Name of the version, e.g.: "1.4.0".  
  
## VpnConnection

A VPN connection .

Fields  
---  
`name` |  `string` Required. The resource name of VPN connection  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the VPN connection was created.  
`update_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time when the VPN connection was last updated.  
`labels` |  `map<string, string>` Labels associated with this resource.  
`nat_gateway_ip` |  `string` NAT gateway IP, or WAN IP address. If a customer has multiple NAT IPs, the customer needs to configure NAT such that only one external IP maps to the GMEC Anthos cluster. This is empty if NAT is not used.  
`bgp_routing_mode  
**(deprecated)**` |  ``[BgpRoutingMode](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.BgpRoutingMode)`` This item is deprecated!Dynamic routing mode of the VPC network, `regional` or `global`.  
`cluster` |  `string` The canonical Cluster name to connect to. It is in the form of projects/{project}/locations/{location}/clusters/{cluster}.  
`vpc` |  `string` The network ID of VPC to connect to.  
`vpc_project` |  ``[VpcProject](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.VpcProject)`` Optional. Project detail of the VPC network. Required if VPC is in a different project than the cluster project.  
`enable_high_availability` |  `bool` Whether this VPN connection has HA enabled on cluster side. If enabled, when creating VPN connection we will attempt to use 2 ANG floating IPs.  
`router` |  `string` Optional. The VPN connection Cloud Router name.  
`details` |  ``[Details](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details)`` Output only. The created connection details.  
  
## BgpRoutingMode

Routing mode.

Enums  
---  
`BGP_ROUTING_MODE_UNSPECIFIED` | Unknown.  
`REGIONAL` | Regional mode.  
`GLOBAL` | Global mode.  
  
## Details

The created connection details.

Fields  
---  
`state` |  ``[State](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.State)`` The state of this connection.  
`error` |  `string` The error message. This is only populated when state=ERROR.  
`cloud_router` |  ``[CloudRouter](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.CloudRouter)`` The Cloud Router info.  
`cloud_vpns[]` |  ``[CloudVpn](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.VpnConnection.Details.CloudVpn)`` Each connection has multiple Cloud VPN gateways.  
  
## CloudRouter

The Cloud Router info.

Fields  
---  
`name` |  `string` The associated Cloud Router name.  
  
## CloudVpn

The Cloud VPN info.

Fields  
---  
`gateway` |  `string` The created Cloud VPN gateway name.  
  
## State

The current connection state.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown.  
`STATE_CONNECTED` | Connected.  
`STATE_CONNECTING` | Still connecting.  
`STATE_ERROR` | Error occurred.  
  
## VpcProject

Project detail of the VPC network.

Fields  
---  
`project_id` |  `string` The project of the VPC to connect to. If not specified, it is the same as the cluster project.  
`service_account  
**(deprecated)**` |  `string` This item is deprecated!Optional. The service account in the VPC project configured by user. It is used to create/delete Cloud Router and Cloud HA VPNs for VPN connection. If this SA is changed during/after a VPN connection is created, you need to remove the Cloud Router and Cloud VPN resources in |project_id|. It is in the form of service-{project_number}@gcp-sa-edgecontainer.iam.gserviceaccount.com.  
  
## ZoneMetadata

A Google Distributed Cloud Edge zone where edge machines are located.

Fields  
---  
`quota[]` |  ``[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.Quota)`` Quota for resources in this zone.  
`rack_types` |  `map<string, `[RackType](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.edgecontainer.v1alpha#google.cloud.edgecontainer.v1alpha.ZoneMetadata.RackType)`>` The map keyed by rack name and has value of RackType.  
  
## RackType

Type of the rack.

Enums  
---  
`RACK_TYPE_UNSPECIFIED` | Unspecified rack type, single rack also belongs to this type.  
`BASE` | Base rack type, a pair of two modified Config-1 racks containing Aggregation switches.  
`EXPANSION` | Expansion rack type, also known as standalone racks, added by customers on demand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
