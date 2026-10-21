---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit/
title: Method: services.configs.submit \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:28.389604+00:00
---

# Method: services.configs.submit  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.configs.submit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * ConfigSource
    * JSON representation
  * ConfigFile
    * JSON representation
  * FileType



Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification). This method stores the source configurations as well as the generated service configuration. To rollout the service configuration to other services, please call `[rollouts.create](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/create#google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout)`.

Only the 100 most recent configuration sources and ones referenced by existing service configurtions are kept for each service. The rest will be deleted eventually.

Operation<response: SubmitConfigSourceResponse>

### HTTP request

`POST https://servicemanagement.googleapis.com/v1/services/{serviceName}/configs:submit`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "configSource": {
        object ([ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigSource))
      },
      "validateOnly": boolean
    }  
  
Fields  
---  
`configSource` |  `object (`[ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigSource)`)` Required. The source configuration for the service.  
`validateOnly` |  `boolean` Optional. If set, this will result in the generation of a `google.api.Service` configuration based on the `ConfigSource` provided, but the generated config and the sources will NOT be persisted.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations#Operation)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ConfigSource

Represents a source file which is used to generate the service configuration defined by `google.api.Service`.

JSON representation  
---  
      
    
    {
      "id": string,
      "files": [
        {
          object ([ConfigFile](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigFile))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. If empty, the server may choose to generate one instead.  
`files[]` |  `object (`[ConfigFile](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigFile)`)` Set of source configuration files that are used to generate a service configuration (`google.api.Service`).  
  
## ConfigFile

Generic specification of a source configuration file

JSON representation  
---  
      
    
    {
      "filePath": string,
      "fileContents": string,
      "fileType": enum ([FileType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#FileType))
    }  
  
Fields  
---  
`filePath` |  `string` The file name of the configuration file (full or relative path).  
`fileContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The bytes that constitute the file.A base64-encoded string.  
`fileType` |  `enum (`[FileType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#FileType)`)` The type of configuration file this represents.  
  
## FileType

Enums  
---  
`FILE_TYPE_UNSPECIFIED` | Unknown file type.  
`SERVICE_CONFIG_YAML` | YAML-specification of service.  
`OPEN_API_JSON` | OpenAPI specification, serialized in JSON.  
`OPEN_API_YAML` | OpenAPI specification, serialized in YAML.  
`FILE_DESCRIPTOR_SET_PROTO` | FileDescriptorSet, generated by protoc.To generate, use protoc with imports and source info included. For an example test.proto file, the following command would put the value in a new file named out.pb.$protoc --include_imports --include_source_info test.proto -o out.pb  
`PROTO_FILE` | Uncompiled Proto file. Used for storage and display purposes only, currently server-side compilation is not supported. Should match the inputs to 'protoc' command used to generated FILE_DESCRIPTOR_SET_PROTO. A file of this type can only be included if at least one file of type FILE_DESCRIPTOR_SET_PROTO is included.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
