---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig/
title: Method: projects.locations.instances.getConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:53:15.941348+00:00
---

# Method: projects.locations.instances.getConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.instances.getConfig Stay organized with collections  Save and categorize content based on your preferences. 

Returns various configuration parameters.

### HTTP request

`GET https://notebooks.googleapis.com/v2/{name}/instances:getConfig`

### Path parameters

Parameters  
---  
`name` |  `string` Required. Format: `projects/{projectId}/locations/{location}`  
  
### Request body

The request body must be empty.

### Response body

Response for getting WbI configurations in a location

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "defaultValues": {
        object ([DefaultValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#DefaultValues))
      },
      "supportedValues": {
        object ([SupportedValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#SupportedValues))
      },
      "availableImages": [
        {
          object ([ImageRelease](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#ImageRelease))
        }
      ],
      "disableWorkbenchLegacyCreation": boolean
    }  
  
Fields  
---  
`defaultValues` |  `object (`[DefaultValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#DefaultValues)`)` Output only. The default values for configuration.  
`supportedValues` |  `object (`[SupportedValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#SupportedValues)`)` Output only. The supported values for configuration.  
`availableImages[]` |  `object (`[ImageRelease](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/getConfig#ImageRelease)`)` Output only. The list of available images to create a WbI.  
`disableWorkbenchLegacyCreation` |  `boolean` Output only. Flag to disable the creation of legacy Workbench notebooks (User-managed notebooks and Google-managed notebooks).  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DefaultValues

DefaultValues represents the default configuration values.

JSON representation  
---  
      
    
    {
      "machineType": string
    }  
  
Fields  
---  
`machineType` |  `string` Output only. The default machine type used by the backend if not provided by the user.  
  
## SupportedValues

SupportedValues represents the values supported by the configuration.

JSON representation  
---  
      
    
    {
      "machineTypes": [
        string
      ],
      "acceleratorTypes": [
        string
      ]
    }  
  
Fields  
---  
`machineTypes[]` |  `string` Output only. The machine types supported by WbI.  
`acceleratorTypes[]` |  `string` Output only. The accelerator types supported by WbI.  
  
## ImageRelease

ConfigImage represents an image release available to create a WbI

JSON representation  
---  
      
    
    {
      "imageName": string,
      "releaseName": string,
      "imageFamily": string,
      "description": string
    }  
  
Fields  
---  
`imageName` |  `string` Output only. The name of the image of the form workbench-instances-vYYYYmmdd--  
`releaseName` |  `string` Output only. The release of the image of the form m123  
`imageFamily` |  `string` Output only. The image family of the image. (ex: workbench-instances or workbench-2603)  
`description` |  `string` Output only. The description of the image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
