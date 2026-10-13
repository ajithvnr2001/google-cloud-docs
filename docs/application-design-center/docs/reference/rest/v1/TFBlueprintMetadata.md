---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata/
title: TFBlueprintMetadata \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:20.969780+00:00
---

# TFBlueprintMetadata  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  TFBlueprintMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TerraformInput
    * JSON representation
  * TerraformInputConnections
    * JSON representation
  * TerraformOutput
    * JSON representation
  * TerraformBlueprintUiMetadata
    * JSON representation
  * TerraformUiInput
    * JSON representation
  * TerraformUiOutput
    * JSON representation



Terraform input and output metadata.

JSON representation  
---  
      
    
    {
      "terraformInput": [
        {
          object ([TerraformInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInput))
        }
      ],
      "terraformOutput": [
        {
          object ([TerraformOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformOutput))
        }
      ],
      "apis": [
        string
      ],
      "roles": [
        string
      ],
      "deploymentDuration": string,
      "iconUri": string,
      "connections": [
        {
          object ([TerraformInputConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInputConnections))
        }
      ],
      "uiMetadata": {
        object ([TerraformBlueprintUiMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformBlueprintUiMetadata))
      },
      "providerVersions": [
        {
          object ([ProviderVersion](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ProviderVersion))
        }
      ]
    }  
  
Fields  
---  
`terraformInput[]` |  `object (`[TerraformInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInput)`)` Output only. Terraform inputs.  
`terraformOutput[]` |  `object (`[TerraformOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformOutput)`)` Output only. Terraform outputs.  
`apis[]` |  `string` Output only. APIs that must be enabled to deploy the template, in the form of "compute.googleapis.com".  
`roles[]` |  `string` Output only. IAM roles required by the service account deploying the template, in the form of "roles/compute.admin".  
`deploymentDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The time estimate for deploying the blueprint.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`iconUri` |  `string` Output only. The icon URI for the blueprint.  
`connections[]` |  `object (`[TerraformInputConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInputConnections)`)` Output only. Union of all the Terraform input connections.  
`uiMetadata` |  `object (`[TerraformBlueprintUiMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformBlueprintUiMetadata)`)` Output only. UI metadata for the blueprint.  
`providerVersions[]` |  `object (`[ProviderVersion](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ProviderVersion)`)` Output only. Provider versions required to deploy the blueprint.  
  
## TerraformInput

Terraform inputs.

JSON representation  
---  
      
    
    {
      "terraformInputVariable": string,
      "description": string,
      "type": string,
      "defaultValue": value,
      "connections": [
        {
          object ([TerraformInputConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInputConnections))
        }
      ],
      "isRequired": boolean
    }  
  
Fields  
---  
`terraformInputVariable` |  `string` Output only. Input variable name present in Terraform.  
`description` |  `string` Output only. Terraform variable description.  
`type` |  `string` Output only. The Terraform input data type.  
`defaultValue` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. The default value of the Terraform input variable.  
`connections[]` |  `object (`[TerraformInputConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformInputConnections)`)` Output only. Terraform input connections.  
`isRequired` |  `boolean` Output only. Indicates if input is required.  
  
## TerraformInputConnections

TerraformInputConnections

JSON representation  
---  
      
    
    {
      "cftTemplateUri": string,
      "cftTemplateVersion": string,
      "outputVar": string,
      "inputPath": string
    }  
  
Fields  
---  
`cftTemplateUri` |  `string` Output only. List of other templates that can be connected to.  
`cftTemplateVersion` |  `string` Output only. Version of the other template that can be connected to.  
`outputVar` |  `string` Output only. Output variable name present in Terraform.  
`inputPath` |  `string` Output only. Input path of the other template that can be connected to.  
  
## TerraformOutput

Terraform outputs.

JSON representation  
---  
      
    
    {
      "type": value,
      "terraformOutputVariable": string,
      "description": string
    }  
  
Fields  
---  
`type` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. Type of Terraform output.  
`terraformOutputVariable` |  `string` Output only. Output variable name present in Terraform.  
`description` |  `string` Output only. Description of the Terraform varaiable.  
  
## TerraformBlueprintUiMetadata

Terraform blueprint UI metadata.

JSON representation  
---  
      
    
    {
      "terraformUiInput": {
        object ([TerraformUiInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformUiInput))
      },
      "terraformUiOutput": {
        object ([TerraformUiOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformUiOutput))
      }
    }  
  
Fields  
---  
`terraformUiInput` |  `object (`[TerraformUiInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformUiInput)`)` Output only. Terraform UI inputs.  
`terraformUiOutput` |  `object (`[TerraformUiOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TFBlueprintMetadata#TerraformUiOutput)`)` Output only. Terraform UI outputs.  
  
## TerraformUiInput

Terraform blueprint UI input.

JSON representation  
---  
      
    
    {
      "terraformUiInputs": {
        string: {
          object ([TerraformUiInputDisplayVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformUiInputDisplayVariable))
        },
        ...
      }
    }  
  
Fields  
---  
`terraformUiInputs` |  `map (key: string, value: object (`[TerraformUiInputDisplayVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformUiInputDisplayVariable)`))` Output only. Terraform UI inputs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## TerraformUiOutput

Terraform blueprint UI output.

JSON representation  
---  
      
    
    {
      "outputMessage": string,
      "terraformUiOutputs": {
        string: {
          object ([TerraformUiOutputDisplay](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformUiOutputDisplay))
        },
        ...
      }
    }  
  
Fields  
---  
`outputMessage` |  `string` Output only. Message to be displayed in the UI.  
`terraformUiOutputs` |  `map (key: string, value: object (`[TerraformUiOutputDisplay](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformUiOutputDisplay)`))` Output only. Visibility of the output.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
