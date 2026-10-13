---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions
title: REST Resource: projects.locations.spaces.catalogs.templates.revisions \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:17.902593+00:00
---

# REST Resource: projects.locations.spaces.catalogs.templates.revisions  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.catalogs.templates.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CatalogTemplateRevision
    * JSON representation
  * State
  * MetadataInput
    * JSON representation
  * MetadataInputSpec
    * JSON representation
  * TemplateInfo
    * JSON representation
  * IacFormatInfo
    * JSON representation
  * TemplateSchema
    * JSON representation
  * TemplateVariable
    * JSON representation
  * TemplateConnections
    * JSON representation
  * ConnectionSource
    * JSON representation
  * ConnectionSpec
    * JSON representation
  * TemplateRequirements
    * JSON representation
  * TemplateRoles
    * JSON representation
  * TemplateUi
    * JSON representation
  * TemplateUiInput
    * JSON representation
  * Methods



## Resource: CatalogTemplateRevision

Template revisions inside a catalog.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType)),
      "createTime": string,
      "updateTime": string,
      "templateMetadata": {
        object ([TFBlueprintMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata))
      },
      "state": enum ([State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#State)),
      "applicationTemplateRevision": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "helmChartMetadata": {
        object ([HelmChartMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata))
      },
      "uuid": string,
      "metadataInput": {
        object ([MetadataInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#MetadataInput))
      },
      "templateCategory": enum ([TemplateCategory](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateCategory)),
      "logicalProducts": [
        {
          object ([LogicalProduct](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/LogicalProduct))
        }
      ],
      "annotations": {
        string: string,
        ...
      },
      "inferredMetadata": {
        object ([InferredMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/InferredMetadata))
      },
      "resourceTypes": [
        {
          object ([ResourceType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ResourceType))
        }
      ],
    
      // Union field artifact_location can be only one of the following:
      "gitSource": {
        object ([GitSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource))
      },
      "gcsSourceUri": string,
      "applicationTemplateRevisionSource": string,
      "developerConnectSourceConfig": {
        object ([DeveloperConnectSourceConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig))
      },
      "ociRepo": {
        object ([OciRepo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/OciRepo))
      }
      // End of list of possible types for union field artifact_location.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The catalog template revision name. `projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template/revisions/$revision`  
`description` |  `string` Optional. The catalog template revision description.  
`type` |  `enum (`[TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType)`)` Optional. The Application Design Center application template type.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The catalog template creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The catalog template update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`templateMetadata` |  `object (`[TFBlueprintMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata)`)` Output only. Template metadata related to Terraform input and output.  
`state` |  `enum (`[State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#State)`)` Output only. The template state (validating/ready/invalid).  
`applicationTemplateRevision` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Output only. The application template revision.  
`helmChartMetadata` |  `object (`[HelmChartMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata)`)` Output only. The helm chart metadata.  
`uuid` |  `string` Output only. UUID of the template revision.  
`metadataInput` |  `object (`[MetadataInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#MetadataInput)`)` Optional. Metadata input.  
`templateCategory` |  `enum (`[TemplateCategory](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateCategory)`)` Output only. The category of the template.  
`logicalProducts[]` |  `object (`[LogicalProduct](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/LogicalProduct)`)` Output only. The Product Main logical product type information.  
`annotations` |  `map (key: string, value: string)` Optional. The annotations of the template revision. Key is the annotation name. Value is the annotation value.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`inferredMetadata` |  `object (`[InferredMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/InferredMetadata)`)` Output only. Metadata that was automatically inferred from the template content. This field can be updated by the system as it gets new information.  
`resourceTypes[]` |  `object (`[ResourceType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ResourceType)`)` Output only. The resource types present in the template revision.  
Union field `artifact_location`. The artifact location of the Terraform in the template. `artifact_location` can be only one of the following:  
`gitSource` |  `object (`[GitSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource)`)` Optional. The git source.  
`gcsSourceUri` |  `string` Optional. The Cloud Storage URI, which must be in the format gs://[bucket] or gs://[bucket]/[object].  
`applicationTemplateRevisionSource` |  `string` Optional. The application template revision source.  
`developerConnectSourceConfig` |  `object (`[DeveloperConnectSourceConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig)`)` Optional. Configuration for fetching content from source code repository such as GitHub or Bitbucket through Developer Connect.  
`ociRepo` |  `object (`[OciRepo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/OciRepo)`)` Optional. The Open Container Initiative (OCI) repo source that contains helm charts.  
  
## State

The template state.

Enums  
---  
`STATE_UNSPECIFIED` | Default.  
`VALIDATING` | The template is being validated.  
`ACTIVE` | The template is ready to be used.  
`INVALID` | The template is invalid.  
  
## MetadataInput

Metadata for the input

JSON representation  
---  
      
    
    {
      "spec": {
        object ([MetadataInputSpec](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#MetadataInputSpec))
      }
    }  
  
Fields  
---  
`spec` |  `object (`[MetadataInputSpec](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#MetadataInputSpec)`)` Required. spec containing the metadata  
  
## MetadataInputSpec

Specifications for the input

JSON representation  
---  
      
    
    {
      "info": {
        object ([TemplateInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateInfo))
      },
      "interfaces": {
        object ([TemplateSchema](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateSchema))
      },
      "requirements": {
        object ([TemplateRequirements](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateRequirements))
      },
      "ui": {
        object ([TemplateUi](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateUi))
      }
    }  
  
Fields  
---  
`info` |  `object (`[TemplateInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateInfo)`)` Optional. TemplateInfo provides the actuation tool information.  
`interfaces` |  `object (`[TemplateSchema](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateSchema)`)` Optional. TemplateSchemas provides the input variables lists and connection information.  
`requirements` |  `object (`[TemplateRequirements](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateRequirements)`)` Required. TemplateRequirements defines the roles required and the provider versions.  
`ui` |  `object (`[TemplateUi](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateUi)`)` Optional. TemplateUi defines the UI related information for the Template.  
  
## TemplateInfo

TemplateInfo provides the actuation tool information.

JSON representation  
---  
      
    
    {
      "actuationTool": {
        object ([IacFormatInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#IacFormatInfo))
      }
    }  
  
Fields  
---  
`actuationTool` |  `object (`[IacFormatInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#IacFormatInfo)`)` Required. IaCFormatInfo defines the actuation tool used to provision the Template.  
  
## IacFormatInfo

IacFormatInfo defines the actuation tool used to provision the Template.

JSON representation  
---  
      
    
    {
      "flavor": string,
      "version": string
    }  
  
Fields  
---  
`flavor` |  `string` Required. Flavor is the type of the actuation tool.  
`version` |  `string` Required. Required version for the actuation tool. required_version = ">= 0.13"  
  
## TemplateSchema

TemplateSchema provides the input variables lists and connection information.

JSON representation  
---  
      
    
    {
      "variables": [
        {
          object ([TemplateVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateVariable))
        }
      ]
    }  
  
Fields  
---  
`variables[]` |  `object (`[TemplateVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateVariable)`)` Required. All defined variables for the Template  
  
## TemplateVariable

TemplateTerraform inputs.

JSON representation  
---  
      
    
    {
      "name": string,
      "connections": [
        {
          object ([TemplateConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateConnections))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Input variable name present in Terraform.  
`connections[]` |  `object (`[TemplateConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateConnections)`)` Required. Terraform input connections.  
  
## TemplateConnections

TemplateConnections

JSON representation  
---  
      
    
    {
      "source": {
        object ([ConnectionSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#ConnectionSource))
      },
      "spec": {
        object ([ConnectionSpec](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#ConnectionSpec))
      }
    }  
  
Fields  
---  
`source` |  `object (`[ConnectionSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#ConnectionSource)`)` Required. Source of the connection.  
`spec` |  `object (`[ConnectionSpec](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#ConnectionSpec)`)` Required. Connection specifications.  
  
## ConnectionSource

Defines the source of a connection.

JSON representation  
---  
      
    
    {
      "source": string,
      "version": string
    }  
  
Fields  
---  
`source` |  `string` Required. Source of the connection. Defined using the same format as module source of form [hostname]/namespace/name/provider for registry references and unprefixed github.com URLs for github references.  
`version` |  `string` Required. Version constraint syntax using the same format as module version constraints.  
  
## ConnectionSpec

Defines the specifications of a connection.

JSON representation  
---  
      
    
    {
      "outputExpr": string,
      "inputPath": string
    }  
  
Fields  
---  
`outputExpr` |  `string` Required. Output expression identifying output being connected to variable.  
`inputPath` |  `string` Optional. Optional dot separated attribuite notation to connect to a specific object field of the input variable.  
  
## TemplateRequirements

TemplateRequirements defines the roles required and the associated services that need to be enabled to provision Template resources.

JSON representation  
---  
      
    
    {
      "roles": [
        {
          object ([TemplateRoles](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateRoles))
        }
      ],
      "providerVersions": [
        {
          object ([ProviderVersion](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ProviderVersion))
        }
      ]
    }  
  
Fields  
---  
`roles[]` |  `object (`[TemplateRoles](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateRoles)`)` Required. All roles required for the component  
`providerVersions[]` |  `object (`[ProviderVersion](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ProviderVersion)`)` Required. Required provider versions.  
  
## TemplateRoles

Template Roles provide the level and roles

JSON representation  
---  
      
    
    {
      "level": string,
      "roles": [
        string
      ]
    }  
  
Fields  
---  
`level` |  `string` Required. Level of the role.  
`roles[]` |  `string` Required. List of roles.  
  
## TemplateUi

TemplateUi defines the UI related information for the Template.

JSON representation  
---  
      
    
    {
      "input": {
        object ([TemplateUiInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateUiInput))
      }
    }  
  
Fields  
---  
`input` |  `object (`[TemplateUiInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions#TemplateUiInput)`)` Required. The top-level input section that defines the list of variables and their sections on the deployment page.  
  
## TemplateUiInput

TemplateUiInput defines the list of variables and their sections on the deployment page.

JSON representation  
---  
      
    
    {
      "variables": {
        string: {
          object ([DisplayVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DisplayVariable))
        },
        ...
      }
    }  
  
Fields  
---  
`variables` |  `map (key: string, value: object (`[DisplayVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DisplayVariable)`))` Required. variables is a map defining all inputs on the UI.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/create)`

|  Creates a template revision.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/delete)`

|  Deletes a template revision.  
  
### `[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/fetchAssessmentReport)`

|  Fetches the assessment report of a catalog template revision if present.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/get)`

|  Gets details about a template revision.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/list)`

|  Lists template revisions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
