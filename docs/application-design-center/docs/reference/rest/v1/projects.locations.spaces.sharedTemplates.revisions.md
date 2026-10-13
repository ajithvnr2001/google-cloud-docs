---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions
title: REST Resource: projects.locations.spaces.sharedTemplates.revisions \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.356266+00:00
---

# REST Resource: projects.locations.spaces.sharedTemplates.revisions  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.sharedTemplates.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SharedTemplateRevision
    * JSON representation
  * Methods



## Resource: SharedTemplateRevision

A read-only template revision that is shared with a space.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType)),
      "sharedTemplateMetadata": {
        object ([TFBlueprintMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata))
      },
      "originTemplateRevision": string,
      "createTime": string,
      "applicationTemplateRevision": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "helmChartMetadata": {
        object ([HelmChartMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata))
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
`name` |  `string` Identifier. The shared template revision name. $sharedTemplate is a server-generated UUID. `projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate/revisions/$revision`  
`description` |  `string` Optional. The shared template revision description.  
`type` |  `enum (`[TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType)`)` Optional. The Application Design Center assembly template type.  
`sharedTemplateMetadata` |  `object (`[TFBlueprintMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata)`)` Output only. The shared template metadata.  
`originTemplateRevision` |  `string` Output only. The shared template revision refers to the following catalog template revision.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The shared template revision creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`applicationTemplateRevision` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Output only. The serialized application template revision.  
`helmChartMetadata` |  `object (`[HelmChartMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata)`)` Output only. The helm chart metadata.  
`templateCategory` |  `enum (`[TemplateCategory](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateCategory)`)` Output only. The category of the template.  
`logicalProducts[]` |  `object (`[LogicalProduct](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/LogicalProduct)`)` Output only. The Product Main logical product type information.  
`annotations` |  `map (key: string, value: string)` Optional. The annotations of the shared template revision. Key is the annotation name. Value is the annotation value.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`inferredMetadata` |  `object (`[InferredMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/InferredMetadata)`)` Output only. Metadata that was automatically inferred from the template content.  
`resourceTypes[]` |  `object (`[ResourceType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ResourceType)`)` Output only. The resource types present in the template revision.  
Union field `artifact_location`. The artifact location of the Terraform in the template. `artifact_location` can be only one of the following:  
`gitSource` |  `object (`[GitSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource)`)` Optional. The git source.  
`gcsSourceUri` |  `string` Optional. The Cloud Storage URI, which must be in the format gs://[bucket] or gs://[bucket]/[object].  
`applicationTemplateRevisionSource` |  `string` Optional. The application template revision source.  
`developerConnectSourceConfig` |  `object (`[DeveloperConnectSourceConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig)`)` Optional. Configuration for fetching content from source code repository such as GitHub or Bitbucket through Developer Connect.  
`ociRepo` |  `object (`[OciRepo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/OciRepo)`)` Optional. The Open Container Initiative (OCI) repo source that contains helm charts.  
  
## Methods  
  
---  
  
### `[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/fetchAssessmentReport)`

|  Fetches the assessment report of a shared template revision if present.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/get)`

|  Gets details about a shared template revision.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/list)`

|  Lists shared template revisions in a given space.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
