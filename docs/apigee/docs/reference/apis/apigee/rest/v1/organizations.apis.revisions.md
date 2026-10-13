---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions
title: REST Resource: organizations.apis.revisions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:24.673149+00:00
---

# REST Resource: organizations.apis.revisions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apis.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApiProxyRevision
    * JSON representation
  * Methods



## Resource: ApiProxyRevision

API proxy revision.

JSON representation  
---  
      
    
    {
      "basepaths": [
        string
      ],
      "configurationVersion": {
        object ([ConfigVersion](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ConfigVersion))
      },
      "contextInfo": string,
      "createdAt": string,
      "displayName": string,
      "description": string,
      "entityMetaDataAsProperties": {
        string: string,
        ...
      },
      "lastModifiedAt": string,
      "name": string,
      "revision": string,
      "policies": [
        string
      ],
      "proxies": [
        string
      ],
      "proxyEndpoints": [
        string
      ],
      "resourceFiles": {
        object ([ResourceFiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ResourceFiles))
      },
      "resources": [
        string
      ],
      "sharedFlows": [
        string
      ],
      "spec": string,
      "targetEndpoints": [
        string
      ],
      "targetServers": [
        string
      ],
      "targets": [
        string
      ],
      "integrationEndpoints": [
        string
      ],
      "type": string,
      "teams": [
        string
      ],
      "archive": string,
      "hasExtensiblePolicy": boolean
    }  
  
Fields  
---  
`basepaths[]` |  `string` Base URL of the API proxy.  
`configurationVersion` |  `object (`[ConfigVersion](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ConfigVersion)`)` Version of the API proxy configuration schema to which the API proxy conforms. Currently, the only supported value is 4.0 (`majorVersion.minorVersion`). This setting may be used in the future to track the evolution of the API proxy format.  
`contextInfo` |  `string` Revision number, app name, and organization for the API proxy.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time that the API proxy revision was created in milliseconds since epoch.  
`displayName` |  `string` Human-readable name of the API proxy.  
`description` |  `string` Description of the API proxy revision.  
`entityMetaDataAsProperties` |  `map (key: string, value: string)` Metadata describing the API proxy revision as a key-value map.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time that the API proxy revision was last modified in milliseconds since epoch.  
`name` |  `string` Name of the API proxy.  
`revision` |  `string` API proxy revision.  
`policies[]` |  `string` List of policy names included in the API proxy revision..  
`proxies[]` |  `string` List of proxy names included in the API proxy revision.  
`proxyEndpoints[]` |  `string` List of ProxyEndpoints in the `/proxies` directory of the API proxy. Typically, this element is included only when the API proxy was created using the Edge UI. This is a 'manifest' setting designed to provide visibility into the contents of the API proxy.  
`resourceFiles` |  `object (`[ResourceFiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ResourceFiles)`)` List of resource files included in the API proxy revision.  
`resources[]` |  `string` List of the resources included in the API proxy revision formatted as "{type}://{name}".  
`sharedFlows[]` |  `string` List of the shared flows included in the API proxy revision.  
`spec` |  `string` OpenAPI Specification that is associated with the API proxy. The value is set to a URL or to a path in the specification store.  
`targetEndpoints[]` |  `string` List of TargetEndpoints in the `/targets` directory of the API proxy. Typically, this element is included only when the API proxy was created using the Edge UI. This is a 'manifest' setting designed to provide visibility into the contents of the API proxy.  
`targetServers[]` |  `string` List of TargetServers referenced in any TargetEndpoint in the API proxy. Typically, you will see this element only when the API proxy was created using the Edge UI. This is a 'manifest' setting designed to provide visibility into the contents of the API proxy.  
`targets[]` |  `string` List of the targets included in the API proxy revision.  
`integrationEndpoints[]` |  `string` List of IntegrationEndpoints in the '/integration-endpoints' directory of the API proxy. This is a 'manifest' setting designed to provide visibility into the contents of the API proxy.  
`type` |  `string` Type. Set to `Application`. Maintained for compatibility with the Apigee Edge API.  
`teams[]` |  `string` List of the teams included in the API proxy revision.  
`archive` |  `string` Output only. The archive that generated this proxy revision. This field is only present on proxy revisions that were generated by an archive. Proxies generated by archives cannot be updated, deleted, or deployed to other environments. Format: `organizations/*/environments/*/archiveDeployments/*`  
`hasExtensiblePolicy` |  `boolean` Output only. This field will be marked as true if revision contains any policies marked as extensible.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/delete)`

|  Deletes an API proxy revision and all policies, resources, endpoints, and revisions associated with it.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get)`

|  Gets an API proxy revision.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/list)`

|  Lists all revisions for an API proxy.  
  
### `[updateApiProxyRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision)`

|  Updates an existing API proxy revision by uploading the API proxy configuration bundle as a zip file from your local machine.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
