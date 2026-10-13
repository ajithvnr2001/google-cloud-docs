---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments
title: REST Resource: organizations.environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:43.952665+00:00
---

# REST Resource: organizations.environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Environment
    * JSON representation
  * DeploymentType
  * NodeConfig
    * JSON representation
  * EnvironmentType
  * ClientIPResolutionConfig
    * JSON representation
  * HeaderIndexAlgorithm
    * JSON representation
  * Methods



## Resource: Environment

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createdAt": string,
      "lastModifiedAt": string,
      "properties": {
        object ([Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties))
      },
      "displayName": string,
      "state": enum (State),
      "deploymentType": enum ([DeploymentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#DeploymentType)),
      "apiProxyType": enum ([ApiProxyType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxyType)),
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#NodeConfig))
      },
      "forwardProxyUri": string,
      "type": enum ([EnvironmentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#EnvironmentType)),
      "hasAttachedFlowHooks": boolean,
      "clientIpResolutionConfig": {
        object ([ClientIPResolutionConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#ClientIPResolutionConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the environment. Values must match the regular expression `^[.\\p{Alnum}-_]{1,255}$`  
`description` |  `string` Optional. Description of the environment.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Creation time of this environment as milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Last modification time of this environment as milliseconds since epoch.  
`properties` |  `object (`[Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties)`)` Optional. Key-value pairs that may be used for customizing the environment.  
`displayName` |  `string` Optional. Display name for this environment.  
`state` |  `enum (`State`)` Output only. State of the environment. Values other than ACTIVE means the resource is not ready to use.  
`deploymentType` |  `enum (`[DeploymentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#DeploymentType)`)` Optional. Deployment type supported by the environment. The deployment type can be set when creating the environment and cannot be changed. When you enable archive deployment, you will be **prevented from performing** a [subset of actions](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview#prevented-actions) within the environment, including:

  * Managing the deployment of API proxy or shared flow revisions
  * Creating, updating, or deleting resource files
  * Creating, updating, or deleting target servers

  
`apiProxyType` |  `enum (`[ApiProxyType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxyType)`)` Optional. API Proxy type supported by the environment. The type can be set when creating the Environment and cannot be changed.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#NodeConfig)`)` Optional. NodeConfig of the environment.  
`forwardProxyUri` |  `string` Optional. URI of the forward proxy to be applied to the runtime instances in this environment. Must be in the format of {scheme}://{hostname}:{port}. Note that the only supported scheme is "http". The port must be supplied.To remove a forward proxy setting, update the field to an empty value.Note: At this time, PUT operations to add forwardProxyUri to an existing environment fail if the environment has nodeConfig set up. To successfully add the forwardProxyUri setting in this case, include the NodeConfig details with the request.  
`type` |  `enum (`[EnvironmentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#EnvironmentType)`)` Optional. EnvironmentType selected for the environment.  
`hasAttachedFlowHooks` |  `boolean`  
`clientIpResolutionConfig` |  `object (`[ClientIPResolutionConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#ClientIPResolutionConfig)`)` Optional. The algorithm to resolve IP. This will affect Analytics, API Security, and other features that use the client ip. To remove a client ip resolution config, update the field to an empty value. Example: '{ "clientIpResolutionConfig" = {} }' For more information, see: <https://cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution>.  
  
## DeploymentType

Deployment type, proxy or archive, supported by the environment.

Enums  
---  
`DEPLOYMENT_TYPE_UNSPECIFIED` | Deployment type not specified.  
`PROXY` | Proxy deployment enables you to develop and deploy API proxies using Apigee on Google Cloud. This cannot currently be combined with the CONFIGURABLE API proxy type.  
`ARCHIVE` | Archive deployment enables you to develop API proxies locally then deploy an archive of your API proxy configuration to an environment in Apigee on Google Cloud. You will be prevented from performing a [subset of actions](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview#prevented-actions) within the environment.  
  
## NodeConfig

NodeConfig for setting the min/max number of nodes associated with the environment.

JSON representation  
---  
      
    
    {
      "minNodeCount": string,
      "maxNodeCount": string,
      "currentAggregateNodeCount": string
    }  
  
Fields  
---  
`minNodeCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The minimum total number of gateway nodes that the is reserved for all instances that has the specified environment. If not specified, the default is determined by the recommended minimum number of nodes for that gateway.  
`maxNodeCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The maximum total number of gateway nodes that the is reserved for all instances that has the specified environment. If not specified, the default is determined by the recommended maximum number of nodes for that gateway.  
`currentAggregateNodeCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The current total number of gateway nodes that each environment currently has across all instances.  
  
## EnvironmentType

Types that can be selected for an Environment. Each of the types are limited by capability and capacity. Refer to Apigee's public documentation to understand about each of these types in details. An Apigee org can support heterogeneous Environments.

Enums  
---  
`ENVIRONMENT_TYPE_UNSPECIFIED` | Environment type not specified.  
`BASE` | This is the default type. Base environment has limited capacity and capabilities and are usually used when you are getting started with Apigee or while experimenting. Refer to Apigee's public documentation for more details.  
`INTERMEDIATE` | Intermediate environment supports API management features and higher capacity than Base environment. Refer to Apigee's public documentation for more details.  
`COMPREHENSIVE` | Comprehensive environment supports advanced capabilites and even higher capacity than Intermediate environment. Refer to Apigee's public documentation for more details.  
  
## ClientIPResolutionConfig

Configuration for resolving the client ip.

JSON representation  
---  
      
    
    {
    
      // Union field IPResolutionAlgorithm can be only one of the following:
      "headerIndexAlgorithm": {
        object ([HeaderIndexAlgorithm](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#HeaderIndexAlgorithm))
      }
      // End of list of possible types for union field IPResolutionAlgorithm.
    }  
  
Fields  
---  
Union field `IPResolutionAlgorithm`. The algorithm to resolve IP. `IPResolutionAlgorithm` can be only one of the following:  
`headerIndexAlgorithm` |  `object (`[HeaderIndexAlgorithm](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#HeaderIndexAlgorithm)`)` Resolves the client ip based on a custom header.  
  
## HeaderIndexAlgorithm

Resolves the client ip based on a custom header.

JSON representation  
---  
      
    
    {
      "ipHeaderName": string,
      "ipHeaderIndex": integer
    }  
  
Fields  
---  
`ipHeaderName` |  `string` Required. The name of the header to extract the client ip from.  
`ipHeaderIndex` |  `integer` Required. The index of the ip in the header. Positive indices 0, 1, 2, 3 chooses indices from the left (first ips) Negative indices -1, -2, -3 chooses indices from the right (last ips)  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create)`

|  Creates an environment in an organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete)`

|  Deletes an environment from an organization.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/get)`

|  Gets environment details.  
  
### `[getAddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getAddonsConfig)`

|  Gets the add-ons config of an environment.  
  
### `[getApiSecurityRuntimeConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getApiSecurityRuntimeConfig)`

|  Gets the API Security runtime configuration for an environment.  
  
### `[getDebugmask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getDebugmask)`

|  Gets the debug mask singleton resource for an environment.  
  
### `[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getIamPolicy)`

|  Gets the IAM policy on an environment.  
  
### `[getSecurityActionsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getSecurityActionsConfig)`

|  GetSecurityActionConfig returns the current SecurityActions configuration.  
  
### `[getTraceConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getTraceConfig)`

|  Get distributed trace configuration in an environment.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/list)`

|  Lists all environments in an organization.  
  
### `[modifyEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/modifyEnvironment)`

|  Updates properties for an Apigee environment with patch semantics using a field mask.  
  
### `[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/setIamPolicy)`

|  Sets the IAM policy on an environment, if the policy already exists it will be replaced.  
  
### `[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/testIamPermissions)`

|  Tests the permissions of a user on an environment, and returns a subset of permissions that the user has on the environment.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/update)`

|  Updates an existing environment.  
  
### `[updateDebugmask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateDebugmask)`

|  Updates the debug mask singleton resource for an environment.  
  
### `[updateEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateEnvironment)`

|  Updates an existing environment.  
  
### `[updateSecurityActionsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateSecurityActionsConfig)`

|  UpdateSecurityActionConfig updates the current SecurityActions configuration.  
  
### `[updateTraceConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateTraceConfig)`

|  Updates the trace configurations in an environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
