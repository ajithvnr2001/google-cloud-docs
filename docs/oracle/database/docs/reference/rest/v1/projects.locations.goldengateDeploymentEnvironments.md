---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments
title: REST Resource: projects.locations.goldengateDeploymentEnvironments \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:49.994094+00:00
---

# REST Resource: projects.locations.goldengateDeploymentEnvironments  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateDeploymentEnvironments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateDeploymentEnvironment
    * JSON representation
  * DeploymentCategory
  * DeploymentEnvironmentType
  * Methods



## Resource: GoldengateDeploymentEnvironment

Details of the Goldengate Deployment Environment resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "category": enum ([DeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#DeploymentCategory)),
      "displayName": string,
      "defaultCpuCoreCount": integer,
      "environmentType": enum ([DeploymentEnvironmentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#DeploymentEnvironmentType)),
      "autoScalingEnabled": boolean,
      "maxCpuCoreCount": integer,
      "memoryGbPerCpuCore": integer,
      "minCpuCoreCount": integer,
      "networkBandwidthGbpsPerCpuCore": integer,
      "storageUsageLimitGbPerCpuCore": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Goldengate Deployment Environment resource with the format: projects/{project}/locations/{location}/goldengateDeploymentEnvironments/{goldengate_deployment_environment}  
`category` |  `enum (`[DeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#DeploymentCategory)`)` Output only. The category of the Goldengate Deployment Environment resource.  
`displayName` |  `string` The display name of the Goldengate Deployment Environment resource.  
`defaultCpuCoreCount` |  `integer` Output only. The default CPU core count of the Goldengate Deployment Environment resource.  
`environmentType` |  `enum (`[DeploymentEnvironmentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#DeploymentEnvironmentType)`)` Output only. The environment type of the Goldengate Deployment Environment resource.  
`autoScalingEnabled` |  `boolean` Output only. Whether auto scaling is enabled by default for the Goldengate Deployment Environment resource.  
`maxCpuCoreCount` |  `integer` Output only. The max CPU core count of the Goldengate Deployment Environment resource.  
`memoryGbPerCpuCore` |  `integer` Output only. The memory per CPU core in GBs of the Goldengate Deployment Environment resource.  
`minCpuCoreCount` |  `integer` Output only. The min CPU core count of the Goldengate Deployment Environment resource.  
`networkBandwidthGbpsPerCpuCore` |  `integer` Output only. The network bandwidth per CPU core in Gbps of the Goldengate Deployment Environment resource.  
`storageUsageLimitGbPerCpuCore` |  `integer` Output only. The storage usage limit per CPU core in GBs of the Goldengate Deployment Environment resource.  
  
## DeploymentCategory

Deployment category of the Goldengate Deployment resource.

Enums  
---  
`DEPLOYMENT_CATEGORY_UNSPECIFIED` | Default unspecified value.  
`DATA_REPLICATION_CATEGORY` | Goldengate Deployment Environment category is DATA_REPLICATION_CATEGORY.  
`DATA_TRANSFORMS_CATEGORY` | Goldengate Deployment Environment category is DATA_TRANSFORMS_CATEGORY.  
  
## DeploymentEnvironmentType

The environment type of the Goldengate Deployment Environment resource.

Enums  
---  
`DEPLOYMENT_ENVIRONMENT_TYPE_UNSPECIFIED` | Default unspecified value.  
`PRODUCTION` | Goldengate Deployment Environment type is PRODUCTION.  
`DEVELOPMENT_OR_TESTING` | Goldengate Deployment Environment type is DEVELOPMENT_OR_TESTING.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments/list)`

|  Lists GoldengateDeploymentEnvironments in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
