---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/create/
title: Method: projects.instanceConfigs.create \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:59.670365+00:00
---

# Method: projects.instanceConfigs.create  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instanceConfigs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates an instance configuration and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance configuration. The instance configuration name is assigned by the caller. If the named instance configuration already exists, `instanceConfigs.create` returns `ALREADY_EXISTS`.

Immediately after the request returns:

  * The instance configuration is readable via the API, with all requested attributes. The instance configuration's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig.FIELDS.reconciling)` field is set to true. Its state is `CREATING`.



While the operation is pending:

  * Cancelling the operation renders the instance configuration immediately unreadable via the API.
  * Except for deleting the creating resource, all other attempts to modify the instance configuration are rejected.



Upon completion of the returned operation:

  * Instances can be created using the instance configuration.
  * The instance configuration's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig.FIELDS.reconciling)` field becomes false. Its state becomes `READY`.



The returned long-running operation will have a name of the format `<instance_config_name>/operations/<operationId>` and can be used to track creation of the instance configuration. The metadata field type is `[CreateInstanceConfigMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstanceConfigMetadata)`. The response field type is `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)`, if successful.

Authorization requires `spanner.instanceConfigs.create` permission on the resource `[parent](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/create#body.PATH_PARAMETERS.parent)`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{parent=projects/*}/instanceConfigs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project in which to create the instance configuration. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instanceConfigs.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instanceConfigId": string,
      "instanceConfig": {
        object ([InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig))
      },
      "validateOnly": boolean
    }  
  
Fields  
---  
`instanceConfigId` |  `string` Required. The ID of the instance configuration to create. Valid identifiers are of the form `custom-[-a-z0-9]*[a-z0-9]` and must be between 2 and 64 characters in length. The `custom-` prefix is required to avoid name conflicts with Google-managed configurations.  
`instanceConfig` |  `object (`[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)`)` Required. The `InstanceConfig` proto of the configuration to create. `instanceConfig.name` must be `<parent>/instanceConfigs/<instanceConfigId>`. `instanceConfig.base_config` must be a Google-managed configuration name, e.g. /instanceConfigs/us-east1, /instanceConfigs/nam3.  
`validateOnly` |  `boolean` An option to validate, but not actually execute, a request, and provide the same response.  
  
### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
