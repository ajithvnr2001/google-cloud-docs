---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models
title: REST Resource: publishers.models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:18:18.799127+00:00
---

# REST Resource: publishers.models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: publishers.models Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: PublisherModel

A Model Garden Publisher Model.

Fields  
  
`name` `string` Output only. Identifier. The resource name of the PublisherModel. | `versionId` `string` Output only. Immutable. The version id of the PublisherModel. A new version is committed when a new model version is uploaded under an existing model id. It is an auto-incrementing decimal number in string representation. | `openSourceCategory` `enum (`[OpenSourceCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenSourceCategory)`)` Required. Indicates the open source category of the publisher model. | `parent` `object (`[Parent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Parent)`)` Optional. The parent that this model was customized from. E.g., Vision API, Natural Language API, LaMDA, T5, etc. Foundation models don't have parents. | `supportedActions` `object (`[CallToAction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#CallToAction)`)` Optional. Supported call-to-action options. | `frameworks[]` `string` Optional. Additional information about the model's Frameworks. | `launchStage` `enum (`[LaunchStage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#LaunchStage)`)` Optional. Indicates the launch stage of the model. | `versionState` `enum (`[VersionState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#VersionState)`)` Optional. Indicates the state of the model version. | `publisherModelTemplate` `string` Optional. Output only. Immutable. Used to indicate this model has a publisher model and provide the template of the publisher model resource name. | `predictSchemata` `object (`[PredictSchemata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata)`)` Optional. The schemata that describes formats of the PublisherModel's predictions and explanations as given and returned via `[PredictionService.Predict](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/predict#google.cloud.aiplatform.v1beta1.PredictionService.Predict)`. | JSON representation  
---  
      
    
    {
      "name": string,
      "versionId": string,
      "openSourceCategory": enum ([OpenSourceCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenSourceCategory)),
      "parent": {
        object ([Parent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Parent))
      },
      "supportedActions": {
        object ([CallToAction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#CallToAction))
      },
      "frameworks": [
        string
      ],
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#LaunchStage)),
      "versionState": enum ([VersionState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#VersionState)),
      "publisherModelTemplate": string,
      "predictSchemata": {
        object ([PredictSchemata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata))
      }
    }  
  
## OpenSourceCategory

An enum representing the open source category of a PublisherModel.

Enums  
---  
`OPEN_SOURCE_CATEGORY_UNSPECIFIED` | The open source category is unspecified, which should not be used.  
`PROPRIETARY` | Used to indicate the PublisherModel is not open sourced.  
`GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT` | Used to indicate the PublisherModel is a Google-owned open source model w/ Google checkpoint.  
`THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT` | Used to indicate the PublisherModel is a 3p-owned open source model w/ Google checkpoint.  
`GOOGLE_OWNED_OSS` | Used to indicate the PublisherModel is a Google-owned pure open source model.  
`THIRD_PARTY_OWNED_OSS` | Used to indicate the PublisherModel is a 3p-owned pure open source model.  
  
## Parent

The information about the parent of a model.

Fields  
  
`displayName` `string` Required. The display name of the parent. E.g., LaMDA, T5, Vision API, Natural Language API. | `reference` `object (`[ResourceReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ResourceReference)`)` Optional. The Google Cloud resource name or the URI reference. | JSON representation  
---  
      
    
    {
      "displayName": string,
      "reference": {
        object ([ResourceReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ResourceReference))
      }
    }  
  
## ResourceReference

Reference to a resource.

Fields  
  
`reference` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`uri` `string` The URI of the resource. | `resourceName` `string` The resource name of the Google Cloud resource. | `useCase  
**(deprecated)**` `string` This item is deprecated!Use case (CUJ) of the resource. | `description  
**(deprecated)**` `string` This item is deprecated!description of the resource. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // reference
      "uri": string,
      "resourceName": string,
      "useCase": string,
      "description": string
      // Union type
    }  
  
## CallToAction

Actions could take on this Publisher Model.

Fields  
  
`viewRestApi` `object (`[ViewRestApi](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ViewRestApi)`)` Optional. To view Rest API docs. | `openNotebook` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open notebook of the PublisherModel. | `createApplication` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Create application using the PublisherModel. | `openFineTuningPipeline` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open fine-tuning pipeline of the PublisherModel. | `openPromptTuningPipeline` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open prompt-tuning pipeline of the PublisherModel. | `openGenie` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open Genie / Playground. | `deploy` `object (`[Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Deploy)`)` Optional. Deploy the PublisherModel to Vertex Endpoint. | `multiDeployVertex` `object (`[DeployVertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployVertex)`)` Optional. Multiple setups to deploy the PublisherModel to Vertex Endpoint. | `deployGke` `object (`[DeployGke](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployGke)`)` Optional. Deploy PublisherModel to Google Kubernetes Engine. | `openGenerationAiStudio` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open in Generation AI Studio. | `requestAccess` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Request for access. | `openEvaluationPipeline` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Optional. Open evaluation pipeline of the PublisherModel. | `openNotebooks` `object (`[OpenNotebooks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenNotebooks)`)` Optional. Open notebooks of the PublisherModel. | `openFineTuningPipelines` `object (`[OpenFineTuningPipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenFineTuningPipelines)`)` Optional. Open fine-tuning pipelines of the PublisherModel. | JSON representation  
---  
      
    
    {
      "viewRestApi": {
        object ([ViewRestApi](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ViewRestApi))
      },
      "openNotebook": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "createApplication": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "openFineTuningPipeline": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "openPromptTuningPipeline": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "openGenie": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "deploy": {
        object ([Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Deploy))
      },
      "multiDeployVertex": {
        object ([DeployVertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployVertex))
      },
      "deployGke": {
        object ([DeployGke](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployGke))
      },
      "openGenerationAiStudio": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "requestAccess": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "openEvaluationPipeline": {
        object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
      },
      "openNotebooks": {
        object ([OpenNotebooks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenNotebooks))
      },
      "openFineTuningPipelines": {
        object ([OpenFineTuningPipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#OpenFineTuningPipelines))
      }
    }  
  
## ViewRestApi

Rest API docs.

Fields  
  
`documentations[]` `object (`[Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Documentation)`)` Required. | `title` `string` Required. The title of the view rest API. | JSON representation  
---  
      
    
    {
      "documentations": [
        {
          object ([Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Documentation))
        }
      ],
      "title": string
    }  
  
## Documentation

A named piece of documentation.

Fields  
  
`title` `string` Required. E.g., OVERVIEW, USE CASES, DOCUMENTATION, SDK & SAMPLES, JAVA, NODE.JS, etc.. | `content` `string` Required. Content of this piece of document (in Markdown format). | JSON representation  
---  
      
    
    {
      "title": string,
      "content": string
    }  
  
## RegionalResourceReferences

The regional resource name or the URI. Key is region, e.g., us-central1, europe-west2, global, etc..

Fields  
  
`references` `map (key: string, value: object (`[ResourceReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ResourceReference)`))` Required. | `title` `string` Required.  | `resourceTitle` `string` Optional. title of the resource. | `resourceUseCase` `string` Optional. Use case (CUJ) of the resource. | `resourceDescription` `string` Optional. description of the resource. | JSON representation  
---  
      
    
    {
      "references": {
        string: {
          object ([ResourceReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#ResourceReference))
        },
        ...
      },
      "title": string,
      "resourceTitle": string,
      "resourceUseCase": string,
      "resourceDescription": string
    }  
  
## OpenNotebooks

Open notebooks.

Fields  
  
`notebooks[]` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Required. Regional resource references to notebooks. | JSON representation  
---  
      
    
    {
      "notebooks": [
        {
          object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
        }
      ]
    }  
  
## OpenFineTuningPipelines

Open fine tuning pipelines.

Fields  
  
`fineTuningPipelines[]` `object (`[RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences)`)` Required. Regional resource references to fine tuning pipelines. | JSON representation  
---  
      
    
    {
      "fineTuningPipelines": [
        {
          object ([RegionalResourceReferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#RegionalResourceReferences))
        }
      ]
    }  
  
## Deploy

Model metadata that is needed for UploadModel or DeployModel/CreateEndpoint requests.

Fields  
  
`modelDisplayName` `string` Optional. Default model display name. | `largeModelReference` `object (`[LargeModelReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#LargeModelReference)`)` Optional. Large model reference. When this is set, modelArtifactSpec is not needed. | `containerSpec` `object (`[ModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelContainerSpec)`)` Optional. The specification of the container that is to be used when deploying this Model in Agent Platform. Not present for Large Models. | `artifactUri` `string` Optional. The path to the directory containing the Model artifact and any of its supporting files. | `title` `string` Required. The title of the regional resource reference. | `publicArtifactUri` `string` Optional. The signed URI for ephemeral Cloud Storage access to model artifact. | `prediction_resources` `Union type`  
  
The prediction (for example, the machine) resources that the DeployedModel uses. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`dedicatedResources` `object (`[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DedicatedResources)`)` A description of resources that are dedicated to the DeployedModel, and that need a higher degree of manual configuration. | `automaticResources` `object (`[AutomaticResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/AutomaticResources)`)` A description of resources that to large degree are decided by Agent Platform, and require only a modest additional configuration. | `sharedResources` `string` The resource name of the shared DeploymentResourcePool to deploy on. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deploymentResourcePool}` End of mutually exclusive fields. | `deployTaskName` `string` Optional. The name of the deploy task (e.g., "text to image generation"). | `deployMetadata` `object (`[DeployMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployMetadata)`)` Optional. metadata information about this deployment config. | JSON representation  
---  
      
    
    {
      "modelDisplayName": string,
      "largeModelReference": {
        object ([LargeModelReference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#LargeModelReference))
      },
      "containerSpec": {
        object ([ModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelContainerSpec))
      },
      "artifactUri": string,
      "title": string,
      "publicArtifactUri": string,
    
      // prediction_resources
      "dedicatedResources": {
        object ([DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DedicatedResources))
      },
      "automaticResources": {
        object ([AutomaticResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/AutomaticResources))
      },
      "sharedResources": string
      // Union type
      "deployTaskName": string,
      "deployMetadata": {
        object ([DeployMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#DeployMetadata))
      }
    }  
  
## LargeModelReference

Contains information about the Large Model.

Fields  
  
`name` `string` Required. The unique name of the large Foundation or pre-built model. Like "chat-bison", "text-bison". Or model name with version id, like "chat-bison@001", "text-bison@005", etc. | JSON representation  
---  
      
    
    {
      "name": string
    }  
  
## DeployMetadata

metadata information about the deployment for managing deployment config.

Fields  
  
`labels` `map (key: string, value: string)` Optional. Labels for the deployment config. For managing deployment config like verifying, source of deployment config, etc. | `sampleRequest` `string` Optional. Sample request for deployed endpoint. | JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      },
      "sampleRequest": string
    }  
  
## DeployVertex

Multiple setups to deploy the PublisherModel.

Fields  
  
`multiDeployVertex[]` `object (`[Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Deploy)`)` Optional. One click deployment configurations. | JSON representation  
---  
      
    
    {
      "multiDeployVertex": [
        {
          object ([Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#Deploy))
        }
      ]
    }  
  
## DeployGke

Configurations for PublisherModel GKE deployment

Fields  
  
`gkeYamlConfigs[]` `string` Optional. GKE deployment configuration in yaml format. | JSON representation  
---  
      
    
    {
      "gkeYamlConfigs": [
        string
      ]
    }  
  
## LaunchStage

An enum representing the launch stage of a PublisherModel.

Enums  
---  
`LAUNCH_STAGE_UNSPECIFIED` | The model launch stage is unspecified.  
`EXPERIMENTAL` | Used to indicate the PublisherModel is at Experimental launch stage, available to a small set of customers.  
`PRIVATE_PREVIEW` | Used to indicate the PublisherModel is at Private Preview launch stage, only available to a small set of customers, although a larger set of customers than an Experimental launch. Previews are the first launch stage used to get feedback from customers.  
`PUBLIC_PREVIEW` | Used to indicate the PublisherModel is at Public Preview launch stage, available to all customers, although not supported for production workloads.  
`GA` | Used to indicate the PublisherModel is at GA launch stage, available to all customers and ready for production workload.  
  
## VersionState

An enum representing the state of the PublicModelVersion.

Enums  
---  
`VERSION_STATE_UNSPECIFIED` | The version state is unspecified.  
`VERSION_STATE_STABLE` | Used to indicate the version is stable.  
`VERSION_STATE_UNSTABLE` | Used to indicate the version is unstable.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/get)`

|  Gets a Model Garden publisher model.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list)`

|  Lists publisher models in Model Garden.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
