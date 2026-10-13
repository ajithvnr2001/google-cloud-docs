---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances
title: REST Resource: projects.locations.instances.integrations.connectors.connectorInstances \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:57.211916+00:00
---

# REST Resource: projects.locations.instances.integrations.connectors.connectorInstances  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.integrations.connectors.connectorInstances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConnectorInstance
    * JSON representation
  * ConnectorConnectivityStatus
  * ConnectorInstanceStatistics
    * JSON representation
  * ConnectorInstanceParameter
    * JSON representation
  * ParamType
  * Methods



## Resource: ConnectorInstance

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. This resource describes the connector instances found on the Connectors Management page..

JSON representation  
---  
      
    
    {
      "name": string,
      "agent": string,
      "environment": string,
      "displayName": string,
      "description": string,
      "intervalSeconds": integer,
      "documentationLink": string,
      "allowList": [
        string
      ],
      "productFieldName": string,
      "eventFieldName": string,
      "timeoutSeconds": string,
      "connectorDefinitionName": string,
      "integrationVersion": string,
      "version": string,
      "loggingEnabledUntilUnixMs": string,
      "statistics": {
        object ([ConnectorInstanceStatistics](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstanceStatistics))
      },
      "parameters": [
        {
          object ([ConnectorInstanceParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstanceParameter))
        }
      ],
      "connectorId": string,
      "identifier": string,
      "id": string,
      "updateAvailable": boolean,
      "custom": boolean,
      "enabled": boolean,
      "remote": boolean,
      "status": enum ([ConnectorConnectivityStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorConnectivityStatus)),
      "integration": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name of the connector instance. Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/connectors/{connector}/instances/{instance}  
`agent` |  `string` Optional. For a connector that runs on an agent, the agent identifier. This cannot be patched and must be defined when creating the instance  
`environment` |  `string` Required. Connector instance environment. In case of a remote connector this cannot be patched  
`displayName` |  `string` Required. Connector instance display name.  
`description` |  `string` Optional. Connector instance description.  
`intervalSeconds` |  `integer` Required. Connector instance execution interval in seconds.  
`documentationLink` |  `string` Output only. The documentation link to show in the UI.  
`allowList[]` |  `string` Optional. Connector instance allow list.  
`productFieldName` |  `string` Optional. Connector's device product.  
`eventFieldName` |  `string` Optional. Connector's event name.  
`timeoutSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Set the timeout of a single Python script run.  
`connectorDefinitionName` |  `string` Output only. Connector definition name.  
`integrationVersion` |  `string` Optional. The integration version. Required on patch.  
`version` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Determines the connector instance version.  
`loggingEnabledUntilUnixMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Determines the timeout when log collecting will be disabled.  
`statistics` |  `object (`[ConnectorInstanceStatistics](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstanceStatistics)`)` Output only. Connector's instance statistics.  
`parameters[]` |  `object (`[ConnectorInstanceParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstanceParameter)`)` Optional. Connector instance parameters.  
`connectorId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The connector definition's ID, or null if it doesn't exist.  
`identifier` |  `string` Output only. The connector instance identifier.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The connector instance id.  
`updateAvailable` |  `boolean` Output only. Indicates if the connector instance has an available update.  
`custom` |  `boolean` Output only. Determines whether this connector instance is based on a custom connector definition.  
`enabled` |  `boolean` Optional. Determines whether this connector is enabled or not.  
`remote` |  `boolean` Output only. Determines whether this connector instance is executed over a remote agent. This cannot be patched and must be defined when creating the instance. It is based on the agentIdentifier's value, if the identifier is null then the // connector is local.  
`status` |  `enum (`[ConnectorConnectivityStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorConnectivityStatus)`)` Output only. Connector's instance status.  
`integration` |  `string` Output only. Parent integration identifier.  
  
## ConnectorConnectivityStatus

Connector instance connectivity status.

Enums  
---  
`LIVE` | Connector instance is live.  
`NOT_LIVE` | Connector instance is not live.  
  
## ConnectorInstanceStatistics

Connector instance statistics.

JSON representation  
---  
      
    
    {
      "pastDayAlertsCount": integer,
      "avgAlertsPerDay": integer
    }  
  
Fields  
---  
`pastDayAlertsCount` |  `integer` Output only. The connector instance ingested alerts over the last 24 hours.  
`avgAlertsPerDay` |  `integer` Output only. The average number of the daily ingested alerts by the connector instance.  
  
## ConnectorInstanceParameter

Connector instance parameter.

JSON representation  
---  
      
    
    {
      "value": string,
      "displayName": string,
      "description": string,
      "mandatory": boolean,
      "advanced": boolean,
      "type": enum ([ParamType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ParamType))
    }  
  
Fields  
---  
`value` |  `string` Optional. The value of the parameter.  
`displayName` |  `string` Output only. The parameter's display name.  
`description` |  `string` Output only. The parameter's description.  
`mandatory` |  `boolean` Output only. Is parameter mandatory.  
`advanced` |  `boolean` Output only. Describes if the parameter is an advanced parameter.  
`type` |  `enum (`[ParamType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances#ParamType)`)` Output only. The parameter's type.  
  
## ParamType

Parameter type options.

Enums  
---  
`BOOLEAN` | Boolean parameter type.  
`INT` | Integer parameter type.  
`STRING` | String parameter type.  
`PASSWORD` | Password parameter type.  
`IP` | IP parameter type.  
`IP_OR_HOST` | IP or host parameter type.  
`URL` | URL parameter type.  
`DOMAIN` | Domain parameter type.  
`EMAIL` | Email parameter type.  
`VALUES_LIST` | Values parameter type.  
`VALUES_AS_SEMI_COLON_SEPARATED_STRING` | Values as semi-colon separated string parameter type.  
`MULTI_VALUES_SELECTION` | Multi values selection parameter type.  
`SCRIPT` | Script parameter type.  
`FILTER_LIST` | Filter list parameter type.  
`NUMERICAL_VALUES` | Numerical values parameter type.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/create)`

|  Creates a new ConnectorInstance based on a connector definition.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/delete)`

|  Deletes a ConnectorInstance.  
  
### `[fetchLatestDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/fetchLatestDefinition)`

|  Refreshes a connector instance with the latest definition from the integration.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/get)`

|  Gets a single ConnectorInstance by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/list)`

|  Lists ConnectorInstances for a specific connector definition.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/patch)`

|  Updates an existing ConnectorInstance.  
  
### `[runOnDemand](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/runOnDemand)`

|  Triggers an immediate, single execution of the connector.  
  
### `[setLogsCollection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances/setLogsCollection)`

|  Enables or disables debug log collection for a connector instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
