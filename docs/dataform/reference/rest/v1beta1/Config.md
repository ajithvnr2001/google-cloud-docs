---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Config/
title: Config \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:58:00.324610+00:00
---

# Config  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Config Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * CreatorRoleConfig
    * JSON representation



Config for all repositories in a given project and location.

JSON representation  
---  
      
    
    {
      "name": string,
      "defaultKmsKeyName": string,
      "creatorRoleConfig": {
        object ([CreatorRoleConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Config#CreatorRoleConfig))
      },
      "enablePrivateWorkspace": boolean,
      "enableProjectChecksForScheduling": boolean,
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The config name.  
`defaultKmsKeyName` |  `string` Optional. The default KMS key that is used if no encryption key is provided when a repository is created.  
`creatorRoleConfig` |  `object (`[CreatorRoleConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Config#CreatorRoleConfig)`)` Optional. Configures the IAM role grant for the resource creator at the time of creation.  
`enablePrivateWorkspace` |  `boolean` Optional. Controls the enablement of the private workspace for the repositorires.When set to True, repositories will use the private workspace model.  
`enableProjectChecksForScheduling` |  `boolean` Optional. Controls the enablement of the project level checks for creating workflow configs and release configs.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## CreatorRoleConfig

Configures the IAM role grant for the resource creator at the time of creation. This message allows customization of the default behavior of granting a role to the creator, which is enabled by the flag `setAuthenticatedUserAdmin` on the resource.

JSON representation  
---  
      
    
    {
    
      // Union field grant_configuration can be only one of the following:
      "disableGrant": boolean,
      "creatorRole": string
      // End of list of possible types for union field grant_configuration.
    }  
  
Fields  
---  
Union field `grant_configuration`. The configuration for the creator role grant. `grant_configuration` can be only one of the following:  
`disableGrant` |  `boolean` Optional. If set to true, disables any automatic IAM role grant to the creator upon resource creation. This setting supersedes the `setAuthenticatedUserAdmin` flag on the resource.  
`creatorRole` |  `string` Optional. Specifies the custom IAM role (e.g., "roles/dataform.editor") to grant to the resource's creator on the resource at the time of creation. This custom role is only granted if the `setAuthenticatedUserAdmin` field on the created resource (e.g., Repository, Workspace) is `true`. When provided, this role replaces the default role of "roles/dataform.admin".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-08 UTC."],[],[]] 
