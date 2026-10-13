---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions
title: REST Resource: projects.locations.goldengateDeploymentVersions \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:50.204994+00:00
---

# REST Resource: projects.locations.goldengateDeploymentVersions  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateDeploymentVersions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateDeploymentVersion
    * JSON representation
  * GoldengateDeploymentVersionProperties
    * JSON representation
  * DeploymentType
  * DeploymentReleaseType
  * Methods



## Resource: GoldengateDeploymentVersion

Details of the Goldengate Deployment Version resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "ocid": string,
      "properties": {
        object ([GoldengateDeploymentVersionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#GoldengateDeploymentVersionProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Goldengate Deployment Version resource with the format: projects/{project}/locations/{location}/goldengateDeploymentVersions/{goldengate_deployment_version}  
`ocid` |  `string` Output only. The deployment version ocid of the Goldengate Deployment Version resource.  
`properties` |  `object (`[GoldengateDeploymentVersionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#GoldengateDeploymentVersionProperties)`)` Output only. The technology type of the Goldengate Deployment Version resource.  
  
## GoldengateDeploymentVersionProperties

Properties of GoldengateDeploymentVersion.

JSON representation  
---  
      
    
    {
      "deploymentType": enum ([DeploymentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#DeploymentType)),
      "securityFix": boolean,
      "oggVersion": string,
      "releaseType": enum ([DeploymentReleaseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#DeploymentReleaseType)),
      "releaseTime": string,
      "supportEndTime": string
    }  
  
Fields  
---  
`deploymentType` |  `enum (`[DeploymentType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#DeploymentType)`)` Output only. The deployment type of the Goldengate Deployment Version resource.  
`securityFix` |  `boolean` Optional. Whether the Goldengate Deployment Version resource is a security fix.  
`oggVersion` |  `string` Output only. The OGG version of the Goldengate Deployment Version resource.  
`releaseType` |  `enum (`[DeploymentReleaseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions#DeploymentReleaseType)`)` Output only. The release type of the Goldengate Deployment Version resource.  
`releaseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The release time of the Goldengate Deployment Version resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`supportEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The support end time of the Goldengate Deployment Version resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## DeploymentType

The deployment type of the Goldengate Deployment Version resource.

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
  
## DeploymentReleaseType

The release type of the Goldengate Deployment Version resource.

Enums  
---  
`DEPLOYMENT_RELEASE_TYPE_UNSPECIFIED` | Default unspecified value.  
`MAJOR` | Goldengate Deployment Version release type is MAJOR.  
`BUNDLE` | Goldengate Deployment Version release type is BUNDLE.  
`MINOR` | Goldengate Deployment Version release type is MINOR.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions/list)`

|  Lists GoldengateDeploymentVersions in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
