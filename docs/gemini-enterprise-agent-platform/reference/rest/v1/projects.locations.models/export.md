---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export/
title: Method: models.export \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:09:30.269350+00:00
---

# Method: models.export  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.export Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.models.export

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one `[supported export format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model.FIELDS.supported_export_formats)`.

### Endpoint

post  `https://{service-endpoint}/v1/{name}:export`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported.

### Request body

The request body contains data with the following structure: | Fields  
  
`outputConfig` `object (`[OutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export#OutputConfig)`)` Required. The desired output location and configuration.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## OutputConfig

Output configuration for the Model export. | Fields  
  
`exportFormatId` `string` The id of the format in which the Model must be exported. Each Model lists the `[export formats it supports](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model.FIELDS.supported_export_formats)`. If no value is provided here, then the first from the list of the Model's supported formats is used by default. | `artifactDestination` `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination)`)` The Cloud Storage location where the Model artifact is to be written to. Under the directory given as the destination a new one with name "`model-export-<model-display-name>-<timestamp-of-export-call>`", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format, will be created. Inside, the Model and any of its supporting files will be written. This field should only be set when the `exportableContent` field of the [Model.supported_export_formats] object contains `ARTIFACT`. | `imageDestination` `object (`[ContainerRegistryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export#ContainerRegistryDestination)`)` The Google Artifact Registry uri where the Model container image will be copied to. This field should only be set when the `exportableContent` field of the [Model.supported_export_formats] object contains `IMAGE`. | JSON representation  
---  
      
    
    {
      "exportFormatId": string,
      "artifactDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination))
      },
      "imageDestination": {
        object ([ContainerRegistryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export#ContainerRegistryDestination))
      }
    }  
  
## ContainerRegistryDestination

The Artifact Registry location for the container image.

Fields  
  
`outputUri` `string` Required. Artifact Registry URI of a container image. Only Google Artifact Registry are supported now. Accepted forms:

  * Google Artifact Registry path. For example: `gcr.io/projectId/imageName:tag`.
  * Artifact Registry path. For example: `us-central1-docker.pkg.dev/projectId/repoName/imageName:tag`.

If a tag is not specified, "latest" will be used as the default tag. | JSON representation  
---  
      
    
    {
      "outputUri": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
