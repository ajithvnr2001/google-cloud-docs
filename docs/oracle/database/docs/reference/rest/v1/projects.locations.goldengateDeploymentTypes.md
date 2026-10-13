---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes
title: REST Resource: projects.locations.goldengateDeploymentTypes \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:50.053469+00:00
---

# REST Resource: projects.locations.goldengateDeploymentTypes  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateDeploymentTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateDeploymentType
    * JSON representation
  * DeploymentType
  * DeploymentCategory
  * Methods



## Resource: GoldengateDeploymentType

Details of the Goldengate Deployment Type resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "deploymentType": enum ([DeploymentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes#DeploymentType)),
      "category": enum ([DeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes#DeploymentCategory)),
      "connectionTypes": [
        string
      ],
      "displayName": string,
      "oggVersion": string,
      "sourceTechnologies": [
        string
      ],
      "supportedCapabilities": [
        string
      ],
      "supportedTechnologiesUrl": string,
      "targetTechnologies": [
        string
      ],
      "defaultUsername": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Goldengate Deployment Type resource with the format: projects/{project}/locations/{region}/goldengateDeploymentTypes/{goldengate_deployment_type}  
`deploymentType` |  `enum (`[DeploymentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes#DeploymentType)`)` Output only. The deployment type of the Goldengate Deployment Type resource.  
`category` |  `enum (`[DeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes#DeploymentCategory)`)` Output only. The category of the Goldengate Deployment Type resource.  
`connectionTypes[]` |  `string` Output only. The connection types of the Goldengate Deployment Type resource.  
`displayName` |  `string` Output only. The display name of the Goldengate Deployment Type resource.  
`oggVersion` |  `string` Output only. The Ogg version of the Goldengate Deployment Type resource.  
`sourceTechnologies[]` |  `string` Output only. The source technologies of the Goldengate Deployment Type resource.  
`supportedCapabilities[]` |  `string` Output only. The supported capabilities of the Goldengate Deployment Type resource.  
`supportedTechnologiesUrl` |  `string` Output only. The supported technologies URL of the Goldengate Deployment Type resource.  
`targetTechnologies[]` |  `string` Output only. The target technologies of the Goldengate Deployment Type resource.  
`defaultUsername` |  `string` Output only. The default username of the Goldengate Deployment Type resource.  
  
## DeploymentType

The deployment type of the Goldengate Deployment Type resource.

Enums  
---  
`DEPLOYMENT_TYPE_UNSPECIFIED` | Default unspecified value.  
`OGG` | Goldengate Deployment Type category is OGG.  
`DATABASE_ORACLE` | Goldengate Deployment Type category is DATABASE_ORACLE.  
`BIGDATA` | Goldengate Deployment Type category is BIGDATA.  
`DATABASE_MICROSOFT_SQLSERVER` | Goldengate Deployment Type category is DATABASE_MICROSOFT_SQLSERVER.  
`DATABASE_MYSQL` | Goldengate Deployment Type category is DATABASE_MYSQL.  
`DATABASE_POSTGRESQL` | Goldengate Deployment Type category is DATABASE_POSTGRESQL.  
`DATABASE_DB2ZOS` | Goldengate Deployment Type category is DATABASE_DB2ZOS.  
`DATABASE_DB2I` | Goldengate Deployment Type category is DATABASE_DB2I.  
`GGSA` | Goldengate Deployment Type category is GGSA.  
`DATA_TRANSFORMS` | Goldengate Deployment Type category is DATA_TRANSFORMS.  
  
## DeploymentCategory

The category of the Goldengate Deployment Type resource.

Enums  
---  
`DEPLOYMENT_CATEGORY_UNSPECIFIED` | Default unspecified value.  
`DATA_REPLICATION_CATEGORY` | Goldengate Deployment Type category is DATA_REPLICATION_CATEGORY.  
`DATA_TRANSFORMS_CATEGORY` | Goldengate Deployment Type category is DATA_TRANSFORMS_CATEGORY.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes/list)`

|  Lists GoldenGateDeploymentTypes in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
