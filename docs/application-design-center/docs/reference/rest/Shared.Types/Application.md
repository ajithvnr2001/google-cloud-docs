---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application/
title: Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:38.296250+00:00
---

# Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Application Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DeploymentSource
    * JSON representation
  * DeploymentMetadata
    * JSON representation
  * ComponentOutputParameters
    * JSON representation
  * DeploymentError
    * JSON representation
  * DeploymentFailureResolutionInfo
    * JSON representation
  * ApplicationOutputParameters
    * JSON representation
  * HelmApplicationOutputParameters
    * JSON representation
  * ProjectParameters
    * JSON representation
  * UpdatedTemplateRevision
    * JSON representation
  * ConnectionConfig
    * JSON representation
  * DeploymentTarget
    * JSON representation
  * GKEDeploymentTarget
    * JSON representation
  * CompositeApplicationParameters
    * JSON representation
  * ProjectParametersList
    * JSON representation
  * DeploymentGroupMetadata
    * JSON representation



Represents the application resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "source": {
        object ([DeploymentSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentSource))
      },
      "appParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ],
      "componentParameters": [
        {
          object ([ComponentParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameters))
        }
      ],
      "serviceAccount": string,
      "displayName": string,
      "description": string,
      "attributes": {
        object ([Attributes](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes))
      },
      "scope": {
        object ([Scope](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Scope))
      },
      "importExistingResources": boolean,
      "previewReference": string,
      "deploymentRevision": string,
      "apphubApplication": string,
      "serializedApplicationTemplate": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "state": enum (State),
      "deploymentMetadata": {
        object ([DeploymentMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentMetadata))
      },
      "projectParameters": [
        {
          object ([ProjectParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParameters))
        }
      ],
      "deploymentRegion": string,
      "updatedTemplateRevision": {
        object ([UpdatedTemplateRevision](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#UpdatedTemplateRevision))
      },
      "deploymentProject": string,
      "connectionConfigs": [
        {
          object ([ConnectionConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ConnectionConfig))
        }
      ],
      "artifactLocation": {
        object ([ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation))
      },
      "type": enum ([ApplicationType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationType)),
      "deploymentTarget": {
        object ([DeploymentTarget](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentTarget))
      },
      "compositionType": enum ([ApplicationCompositionType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationCompositionType)),
      "compositeApplicationParameters": {
        object ([CompositeApplicationParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#CompositeApplicationParameters))
      },
      "deploymentGroupMetadata": {
        object ([DeploymentGroupMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentGroupMetadata))
      },
      "paramsUpdateStrategy": enum ([UpdateStrategy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/UpdateStrategy))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the application. Format: projects/{project}/locations/{location}/spaces/{space}/applications/{application}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`source` |  `object (`[DeploymentSource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentSource)`)` Required. The application deployment source.  
`appParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. A list of parameters to attach to the deployment source object, which is a catalog entry or application template snapshot.  
`componentParameters[]` |  `object (`[ComponentParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameters)`)` Optional. A list of component parameters to associate with the application.  
`serviceAccount` |  `string` Optional. Your own service account that you use to deploy an application.  
`displayName` |  `string` Optional. Display name of the application.  
`description` |  `string` Optional. Description of the application.  
`attributes` |  `object (`[Attributes](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes)`)` Optional. Attributes of the application.  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Scope)`)` Required. Scope of the application.  
`importExistingResources` |  `boolean` Optional. Import existing resources into the application.  
`previewReference` |  `string` Output only. Preview reference for the application.  
`deploymentRevision` |  `string` Output only. [Output only] Optional Infra Manager deployment Id with revision  
`apphubApplication` |  `string` Output only. The App Hub App associated with the application.  
`serializedApplicationTemplate` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Output only. [Output only] Serialized application template.  
`state` |  `enum (`State`)` Output only. Deployment state of the application.  
`deploymentMetadata` |  `object (`[DeploymentMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentMetadata)`)` Output only. Deployment metadata of the application.  
`projectParameters[]` |  `object (`[ProjectParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParameters)`)` Output only. List of project parameters for the application.  
`deploymentRegion` |  `string` Optional. The region where the application is deployed.  
`updatedTemplateRevision` |  `object (`[UpdatedTemplateRevision](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#UpdatedTemplateRevision)`)` Output only. The updated template revision because of which the application is outdated.  
`deploymentProject` |  `string` Optional. Deployment project of the application.  
`connectionConfigs[]` |  `object (`[ConnectionConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ConnectionConfig)`)` Optional. Connection configuration for the application.  
`artifactLocation` |  `object (`[ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation)`)` Output only. Details of the location where the IaC for this application was last successfully exported.  
`type` |  `enum (`[ApplicationType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationType)`)` Optional. The type of the application.  
`deploymentTarget` |  `object (`[DeploymentTarget](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentTarget)`)` Optional. The deployment target of the application.  
`compositionType` |  `enum (`[ApplicationCompositionType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationCompositionType)`)` Output only. The composition type of the application: STANDARD OR COMPOSITE.  
`compositeApplicationParameters` |  `object (`[CompositeApplicationParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#CompositeApplicationParameters)`)` Optional. Parameters that are required for composite applications.  
`deploymentGroupMetadata` |  `object (`[DeploymentGroupMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentGroupMetadata)`)` Output only. The deployment group metadata of the application. This is applicable only for composite applications.  
`paramsUpdateStrategy` |  `enum (`[UpdateStrategy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/UpdateStrategy)`)` Optional. Specifies the strategy to use when updating the application parameters while updating the application template revision.  
  
## DeploymentSource

Source template information for the deployment.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "applicationTemplateRevision": string,
      "sharedTemplateRevisionUri": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. The source for the IaC deployment. `source` can be only one of the following:  
`applicationTemplateRevision` |  `string` Application template revision URI.  
`sharedTemplateRevisionUri` |  `string` Shared template revision URI.  
  
## DeploymentMetadata

Deployment information for the application.

JSON representation  
---  
      
    
    {
      "revision": string,
      "componentOutputParameters": [
        {
          object ([ComponentOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ComponentOutputParameters))
        }
      ],
      "error": {
        object ([DeploymentError](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentError))
      },
      "build": string,
      "workerPool": string,
      "retryAttempts": integer,
      "applicationOutputParameters": {
        object ([ApplicationOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ApplicationOutputParameters))
      }
    }  
  
Fields  
---  
`revision` |  `string` Output only. The revision of the deployment associated with the Application.  
`componentOutputParameters[]` |  `object (`[ComponentOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ComponentOutputParameters)`)` Output only. The component output parameters of the deployment.  
`error` |  `object (`[DeploymentError](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentError)`)` Output only. The error associated with the deployment.  
`build` |  `string` Output only. Cloud Build instance UUID associated with this deployment.  
`workerPool` |  `string` Output only. The user-specified Cloud Build worker pool resource used, which the system uses to deploy the application. Format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`.  
`retryAttempts` |  `integer` Output only. The attempted number of deployment retries.  
`applicationOutputParameters` |  `object (`[ApplicationOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ApplicationOutputParameters)`)` Output only. The application output parameters of the deployment.  
  
## ComponentOutputParameters

The component output parameters of the deployment.

JSON representation  
---  
      
    
    {
      "component": string,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ]
    }  
  
Fields  
---  
`component` |  `string` Output only. The component name of the output parameters.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Output only. The output parameters of the component.  
  
## DeploymentError

The error associated with the deployment.

JSON representation  
---  
      
    
    {
      "type": enum ([ErrorType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ErrorType)),
      "code": enum ([ErrorCode](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ErrorCode)),
      "tfErrors": [
        {
          object ([TerraformError](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformError))
        }
      ],
      "detail": string,
      "deploymentFailureResolutionInfo": [
        {
          object ([DeploymentFailureResolutionInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentFailureResolutionInfo))
        }
      ],
      "errorMessage": string
    }  
  
Fields  
---  
`type` |  `enum (`[ErrorType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ErrorType)`)` Output only. The error type based on the deployment error code.  
`code` |  `enum (`[ErrorCode](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ErrorCode)`)` Output only. The deployment error code. Based on Infrastructure Manager error codes.  
`tfErrors[]` |  `object (`[TerraformError](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformError)`)` Output only. The error message associated with the deployment.  
`detail` |  `string` Output only. Human readable string that summarizes the deployment error issue.  
`deploymentFailureResolutionInfo[]` |  `object (`[DeploymentFailureResolutionInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentFailureResolutionInfo)`)` Output only. The call to actions associated with the deployment issue.  
`errorMessage` |  `string` Output only. Stores errors generated by Infra Manager, as well as all non-internal errors (such as INVALID_ARGUMENT) that occur before initiating the deployment.  
  
## DeploymentFailureResolutionInfo

The call to action associated with the deployment issue.

JSON representation  
---  
      
    
    {
      "resolutionLink": string,
      "resolutionMessage": string,
      "resolutionLinkText": string
    }  
  
Fields  
---  
`resolutionLink` |  `string` Output only. Link for the call to action.  
`resolutionMessage` |  `string` Output only. Elaborative error resolution message.  
`resolutionLinkText` |  `string` Output only. Call to action link text.  
  
## ApplicationOutputParameters

The application output parameters of the deployment.

JSON representation  
---  
      
    
    {
    
      // Union field parameters can be only one of the following:
      "helmApplicationOutputParameters": {
        object ([HelmApplicationOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#HelmApplicationOutputParameters))
      }
      // End of list of possible types for union field parameters.
    }  
  
Fields  
---  
Union field `parameters`. The output parameters of the application. `parameters` can be only one of the following:  
`helmApplicationOutputParameters` |  `object (`[HelmApplicationOutputParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#HelmApplicationOutputParameters)`)` Output only. Helm application output parameters.  
  
## HelmApplicationOutputParameters

The helm application output parameters of the deployment.

JSON representation  
---  
      
    
    {
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ]
    }  
  
Fields  
---  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Output only. The output parameters of the helm application.  
  
## ProjectParameters

The ProjectParameters provides the parameters needed to deploy the application in the given project.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "roles": [
        string
      ],
      "apis": [
        string
      ]
    }  
  
Fields  
---  
`projectId` |  `string` Output only. The project ID of the project.  
`roles[]` |  `string` Output only. IAM roles required by the service account to deploy the application in given project.  
`apis[]` |  `string` Output only. APIs required to be enabled to deploy the application, in the form of "*.googleapis.com".  
  
## UpdatedTemplateRevision

The updated template revision, which results in an outdated application.

JSON representation  
---  
      
    
    {
      "templateRevision": string,
      "createTime": string,
      "templateDisplayName": string
    }  
  
Fields  
---  
`templateRevision` |  `string` Output only. The details of the updated template revision.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the template was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`templateDisplayName` |  `string` Output only. The display name of the template. If the display name is not available, the template resource name is used.  
  
## ConnectionConfig

Connection configuration for the application.

JSON representation  
---  
      
    
    {
      "connectionUri": string,
      "sourceComponentParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ],
      "destinationComponentParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ]
    }  
  
Fields  
---  
`connectionUri` |  `string` Required. The connection URI.  
`sourceComponentParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. The parameters of the connection associated with the source component.  
`destinationComponentParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. The parameters of the connection associated with the destination component.  
  
## DeploymentTarget

The deployment target of the application.

JSON representation  
---  
      
    
    {
    
      // Union field target can be only one of the following:
      "gkeDeploymentTarget": {
        object ([GKEDeploymentTarget](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#GKEDeploymentTarget))
      }
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
Union field `target`. Different deployment targets for the application. `target` can be only one of the following:  
`gkeDeploymentTarget` |  `object (`[GKEDeploymentTarget](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#GKEDeploymentTarget)`)` Optional. The GKE deployment target.  
  
## GKEDeploymentTarget

The GKE deployment target.

JSON representation  
---  
      
    
    {
      "clusterSelfLink": string,
      "namespace": string,
      "kubernetesServiceAccount": string,
      "kubernetesServiceAccountCreation": boolean
    }  
  
Fields  
---  
`clusterSelfLink` |  `string` Required. The self link of the cluster where GKE based application is deployed.  
`namespace` |  `string` Required. The namespace where the application is deployed.  
`kubernetesServiceAccount` |  `string` Required. The kubernetes service account that is created within the namespace provided above. Example: default or node-sa  
`kubernetesServiceAccountCreation` |  `boolean` Optional. Whether to create the provided KSA. If true, the KSA will be created in the namespace provided above. If false, the KSA is expected to already exist in the namespace provided above.  
  
## CompositeApplicationParameters

Holds parameters that are specific to composite applications.

JSON representation  
---  
      
    
    {
      "serviceAccountMap": {
        string: string,
        ...
      },
      "projectParametersMap": {
        string: {
          object ([ProjectParametersList](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParametersList))
        },
        ...
      }
    }  
  
Fields  
---  
`serviceAccountMap` |  `map (key: string, value: string)` Optional. A map from a component's URI to the deployment service account for composite application. key format: projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{applicationTemplate}/components/{component} value format: projects/{project}/serviceAccounts/{email_address}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`projectParametersMap` |  `map (key: string, value: object (`[ProjectParametersList](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParametersList)`))` Output only. A map from a component's URI to its project parameters. The key format is: projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{applicationTemplate}/components/{component}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ProjectParametersList

Provides the list of project parameters needed to deploy an application.

JSON representation  
---  
      
    
    {
      "projectParameters": [
        {
          object ([ProjectParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParameters))
        }
      ]
    }  
  
Fields  
---  
`projectParameters[]` |  `object (`[ProjectParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#ProjectParameters)`)` Output only. List of project parameters for the application.  
  
## DeploymentGroupMetadata

Metadata for the infra manager deployment group. A deployment group in Infrastructure Manager is a logical grouping of one or more deployments.

JSON representation  
---  
      
    
    {
      "deploymentGroup": string,
      "deploymentMetadataMap": {
        string: {
          object ([DeploymentMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentMetadata))
        },
        ...
      }
    }  
  
Fields  
---  
`deploymentGroup` |  `string` Output only. The deployment group name. Format: projects/{project}/locations/{location}/deploymentGroup/{deploymentGroup}  
`deploymentMetadataMap` |  `map (key: string, value: object (`[DeploymentMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Application#DeploymentMetadata)`))` Output only. Map of component name to deployment metadata for the component. Key format: projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{applicationTemplate}/components/{component}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
