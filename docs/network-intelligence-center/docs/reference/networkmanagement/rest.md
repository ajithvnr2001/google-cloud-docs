---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/
title: Network Management API \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:22.498145+00:00
---

# Network Management API  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Network Management API Stay organized with collections  Save and categorize content based on your preferences. 

The Network Management API provides a collection of network performance monitoring and diagnostic capabilities.

  * REST Resource: v1beta1.organizations.locations
  * REST Resource: v1beta1.organizations.locations.global.operations
  * REST Resource: v1beta1.organizations.locations.vpcFlowLogsConfigs
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.global.connectivityTests
  * REST Resource: v1beta1.projects.locations.global.operations
  * REST Resource: v1beta1.projects.locations.vpcFlowLogsConfigs
  * REST Resource: v1alpha1.projects.locations
  * REST Resource: v1alpha1.projects.locations.networkMonitoringProviders
  * REST Resource: v1alpha1.projects.locations.networkMonitoringProviders.monitoringPoints
  * REST Resource: v1alpha1.projects.locations.networkMonitoringProviders.networkPaths
  * REST Resource: v1alpha1.projects.locations.networkMonitoringProviders.webPaths
  * REST Resource: v1alpha1.projects.locations.operations
  * REST Resource: v1.organizations.locations
  * REST Resource: v1.organizations.locations.global.operations
  * REST Resource: v1.organizations.locations.vpcFlowLogsConfigs
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.global.connectivityTests
  * REST Resource: v1.projects.locations.global.operations
  * REST Resource: v1.projects.locations.networkMonitoringProviders
  * REST Resource: v1.projects.locations.networkMonitoringProviders.monitoringPoints
  * REST Resource: v1.projects.locations.networkMonitoringProviders.networkPaths
  * REST Resource: v1.projects.locations.networkMonitoringProviders.webPaths
  * REST Resource: v1.projects.locations.vpcFlowLogsConfigs



## Service: networkmanagement.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networkmanagement.googleapis.com/$discovery/rest?version=v1>
  * <https://networkmanagement.googleapis.com/$discovery/rest?version=v1beta1>
  * <https://networkmanagement.googleapis.com/$discovery/rest?version=v1alpha1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networkmanagement.googleapis.com`



## REST Resource: [v1beta1.organizations.locations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations/list)` |  `GET /v1beta1/{name=organizations/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.organizations.locations.global.operations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.global.operations/cancel)` |  `POST /v1beta1/{name=organizations/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.global.operations/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.global.operations/get)` |  `GET /v1beta1/{name=organizations/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.global.operations/list)` |  `GET /v1beta1/{name=organizations/*/locations/global}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.organizations.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/vpcFlowLogsConfigs`   
Creates a new `VpcFlowLogsConfig`.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Deletes a specific `VpcFlowLogsConfig`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Gets the details of a specific `VpcFlowLogsConfig`.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/vpcFlowLogsConfigs`   
Lists all `VpcFlowLogsConfigs` in a given organization.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/patch)` |  `PATCH /v1beta1/{vpcFlowLogsConfig.name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Updates an existing `VpcFlowLogsConfig`.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.global.connectivityTests](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/create)` |  `POST /v1beta1/{parent=projects/*/locations/global}/connectivityTests`   
Creates a new Connectivity Test.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/connectivityTests/*}`   
Deletes a specific `ConnectivityTest`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/get)` |  `GET /v1beta1/{name=projects/*/locations/global/connectivityTests/*}`   
Gets the details of a specific Connectivity Test.  
`[getIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/global/connectivityTests/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/list)` |  `GET /v1beta1/{parent=projects/*/locations/global}/connectivityTests`   
Lists all Connectivity Tests owned by a project.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/patch)` |  `PATCH /v1beta1/{resource.name=projects/*/locations/global/connectivityTests/*}`   
Updates the configuration of an existing `ConnectivityTest`.  
`[rerun](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/rerun)` |  `POST /v1beta1/{name=projects/*/locations/global/connectivityTests/*}:rerun`   
Rerun an existing `ConnectivityTest`.  
`[setIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/global/connectivityTests/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/global/connectivityTests/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.global.operations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/global}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs`   
Creates a new `VpcFlowLogsConfig`.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Deletes a specific `VpcFlowLogsConfig`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/get)` |  `GET /v1beta1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Gets the details of a specific `VpcFlowLogsConfig`.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs`   
Lists all `VpcFlowLogsConfigs` in a given project.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/patch)` |  `PATCH /v1beta1/{vpcFlowLogsConfig.name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Updates an existing `VpcFlowLogsConfig`.  
`[queryOrgVpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/queryOrgVpcFlowLogsConfigs)` |  `GET /v1beta1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:queryOrgVpcFlowLogsConfigs`   
QueryOrgVpcFlowLogsConfigs returns a list of all organization-level VPC Flow Logs configurations applicable to the specified project.  
`[showEffectiveFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs)` |  `GET /v1beta1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:showEffectiveFlowLogsConfigs`   
ShowEffectiveFlowLogsConfigs returns a list of all VPC Flow Logs configurations applicable to a specified resource.  
  
## REST Resource: [v1alpha1.projects.locations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations/list)` |  `GET /v1alpha1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha1.projects.locations.networkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/networkMonitoringProviders`   
Creates a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*}`   
Deletes a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource and all of its child resources.  
`[generateMonitoringPointConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/generateMonitoringPointConfig)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*}:generateMonitoringPointConfig`   
Generates Monitoring Point configuration of a NetworkMonitoringProvider resource.  
`[generateProviderAccessToken](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/generateProviderAccessToken)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*}:generateProviderAccessToken`   
Generates a provider access token for a given Google access token.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*}`   
Gets the `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/networkMonitoringProviders`   
Lists `[NetworkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` for a given project and location.  
  
## REST Resource: [v1alpha1.projects.locations.networkMonitoringProviders.monitoringPoints](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints)

Methods  
---  
`[downloadInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript)` |  `GET /v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints:downloadInstallScript`   
Downloads an install script for MonitoringPoints for a given network monitoring provider.  
`[downloadRecreateInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadRecreateInstallScript)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*/monitoringPoints/*}:downloadRecreateInstallScript`   
Downloads an install script for a specific Container MonitoringPoint.  
`[downloadServerConnectConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadServerConnectConfig)` |  `GET /v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints:downloadServerConnectConfig`   
Downloads the server connect configuration for a given network monitoring provider.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*/monitoringPoints/*}`   
Gets the `[MonitoringPoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints`   
Lists `[MonitoringPoints](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` for a given network monitoring provider.  
  
## REST Resource: [v1alpha1.projects.locations.networkMonitoringProviders.networkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*/networkPaths/*}`   
Gets the `[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/networkPaths`   
Lists `[NetworkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` for a given network monitoring provider.  
  
## REST Resource: [v1alpha1.projects.locations.networkMonitoringProviders.webPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*/webPaths/*}`   
Gets the `[WebPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/webPaths`   
Lists `[WebPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` for a given network monitoring provider.  
  
## REST Resource: [v1alpha1.projects.locations.operations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.operations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.organizations.locations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations/get)` |  `GET /v1/{name=organizations/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations/list)` |  `GET /v1/{name=organizations/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.organizations.locations.global.operations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.global.operations/cancel)` |  `POST /v1/{name=organizations/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.global.operations/delete)` |  `DELETE /v1/{name=organizations/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.global.operations/get)` |  `GET /v1/{name=organizations/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.global.operations/list)` |  `GET /v1/{name=organizations/*/locations/global}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.organizations.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/create)` |  `POST /v1/{parent=organizations/*/locations/*}/vpcFlowLogsConfigs`   
Creates a new `VpcFlowLogsConfig`.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/delete)` |  `DELETE /v1/{name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Deletes a specific `VpcFlowLogsConfig`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/get)` |  `GET /v1/{name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Gets the details of a specific `VpcFlowLogsConfig`.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/list)` |  `GET /v1/{parent=organizations/*/locations/*}/vpcFlowLogsConfigs`   
Lists all `VpcFlowLogsConfigs` in a given organization.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/patch)` |  `PATCH /v1/{vpcFlowLogsConfig.name=organizations/*/locations/*/vpcFlowLogsConfigs/*}`   
Updates an existing `VpcFlowLogsConfig`.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.global.connectivityTests](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create)` |  `POST /v1/{parent=projects/*/locations/global}/connectivityTests`   
Creates a new Connectivity Test.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/delete)` |  `DELETE /v1/{name=projects/*/locations/global/connectivityTests/*}`   
Deletes a specific `ConnectivityTest`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/get)` |  `GET /v1/{name=projects/*/locations/global/connectivityTests/*}`   
Gets the details of a specific Connectivity Test.  
`[getIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/global/connectivityTests/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/list)` |  `GET /v1/{parent=projects/*/locations/global}/connectivityTests`   
Lists all Connectivity Tests owned by a project.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/patch)` |  `PATCH /v1/{resource.name=projects/*/locations/global/connectivityTests/*}`   
Updates the configuration of an existing `ConnectivityTest`.  
`[rerun](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/rerun)` |  `POST /v1/{name=projects/*/locations/global/connectivityTests/*}:rerun`   
Rerun an existing `ConnectivityTest`.  
`[setIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/global/connectivityTests/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/global/connectivityTests/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.global.operations](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.operations/cancel)` |  `POST /v1/{name=projects/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.operations/get)` |  `GET /v1/{name=projects/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.operations/list)` |  `GET /v1/{name=projects/*/locations/global}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.networkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/create)` |  `POST /v1/{parent=projects/*/locations/*}/networkMonitoringProviders`   
Creates a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/delete)` |  `DELETE /v1/{name=projects/*/locations/*/networkMonitoringProviders/*}`   
Deletes a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource and all of its child resources.  
`[generateMonitoringPointConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateMonitoringPointConfig)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*}:generateMonitoringPointConfig`   
Generates Monitoring Point configuration of a NetworkMonitoringProvider resource.  
`[generateProviderAccessToken](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateProviderAccessToken)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*}:generateProviderAccessToken`   
Generates a provider access token for a given Google access token.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/get)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*}`   
Gets the `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/list)` |  `GET /v1/{parent=projects/*/locations/*}/networkMonitoringProviders`   
Lists `[NetworkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` for a given project and location.  
  
## REST Resource: [v1.projects.locations.networkMonitoringProviders.monitoringPoints](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints)

Methods  
---  
`[downloadInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript)` |  `GET /v1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints:downloadInstallScript`   
Downloads an install script for MonitoringPoints for a given network monitoring provider.  
`[downloadRecreateInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadRecreateInstallScript)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*/monitoringPoints/*}:downloadRecreateInstallScript`   
Downloads an install script for a specific Container MonitoringPoint.  
`[downloadServerConnectConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadServerConnectConfig)` |  `GET /v1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints:downloadServerConnectConfig`   
Downloads the server connect configuration for a given network monitoring provider.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/get)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*/monitoringPoints/*}`   
Gets the `[MonitoringPoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/list)` |  `GET /v1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints`   
Lists `[MonitoringPoints](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` for a given network monitoring provider.  
  
## REST Resource: [v1.projects.locations.networkMonitoringProviders.networkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.networkPaths)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.networkPaths/get)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*/networkPaths/*}`   
Gets the `[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.networkPaths/list)` |  `GET /v1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/networkPaths`   
Lists `[NetworkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` for a given network monitoring provider.  
  
## REST Resource: [v1.projects.locations.networkMonitoringProviders.webPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.webPaths)

Methods  
---  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.webPaths/get)` |  `GET /v1/{name=projects/*/locations/*/networkMonitoringProviders/*/webPaths/*}`   
Gets the `[WebPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` resource.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.webPaths/list)` |  `GET /v1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/webPaths`   
Lists `[WebPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` for a given network monitoring provider.  
  
## REST Resource: [v1.projects.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs`   
Creates a new `VpcFlowLogsConfig`.  
`[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Deletes a specific `VpcFlowLogsConfig`.  
`[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Gets the details of a specific `VpcFlowLogsConfig`.  
`[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs`   
Lists all `VpcFlowLogsConfigs` in a given project.  
`[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/patch)` |  `PATCH /v1/{vpcFlowLogsConfig.name=projects/*/locations/*/vpcFlowLogsConfigs/*}`   
Updates an existing `VpcFlowLogsConfig`.  
`[queryOrgVpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/queryOrgVpcFlowLogsConfigs)` |  `GET /v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:queryOrgVpcFlowLogsConfigs`   
QueryOrgVpcFlowLogsConfigs returns a list of all organization-level VPC Flow Logs configurations applicable to the specified project.  
`[showEffectiveFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs)` |  `GET /v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:showEffectiveFlowLogsConfigs`   
ShowEffectiveFlowLogsConfigs returns a list of all VPC Flow Logs configurations applicable to a specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
