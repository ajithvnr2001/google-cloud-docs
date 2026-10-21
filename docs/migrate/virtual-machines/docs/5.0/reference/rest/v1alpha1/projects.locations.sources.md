---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources
title: REST Resource: projects.locations.sources \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:44.343308+00:00
---

# REST Resource: projects.locations.sources  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Source
    * JSON representation
  * VmwareSourceDetails
    * JSON representation
  * AwsSourceDetails
    * JSON representation
  * AccessKeyCredentials
    * JSON representation
  * State
  * Tag
    * JSON representation
  * AzureSourceDetails
    * JSON representation
  * ClientSecretCredentials
    * JSON representation
  * State
  * Methods



## Resource: Source

Source message describes a specific vm migration Source resource. It contains the source environment information.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status))
      },
    
      // Union field source_details can be only one of the following:
      "vmware": {
        object ([VmwareSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#VmwareSourceDetails))
      },
      "aws": {
        object ([AwsSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AwsSourceDetails))
      },
      "azure": {
        object ([AzureSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AzureSourceDetails))
      }
      // End of list of possible types for union field source_details.
    }  
  
Fields  
---  
`name` |  `string` Output only. The Source name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` The labels of the source.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` User-provided description of the source.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. Immutable. The encryption details of the source data stored by the service.  
`error  
**(deprecated)**` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status)`)` This item is deprecated!Output only. Provides details on the state of the Source in case of an error.  
Union field `source_details`.`source_details` can be only one of the following:  
`vmware` |  `object (`[VmwareSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#VmwareSourceDetails)`)` Vmware type source details.  
`aws` |  `object (`[AwsSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AwsSourceDetails)`)` AWS type source details.  
`azure` |  `object (`[AzureSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AzureSourceDetails)`)` Azure type source details.  
  
## VmwareSourceDetails

VmwareSourceDetails message describes a specific source details for the vmware source type.

JSON representation  
---  
      
    
    {
      "username": string,
      "password": string,
      "vcenterIp": string,
      "thumbprint": string,
      "resolvedVcenterHost": string
    }  
  
Fields  
---  
`username` |  `string` The credentials username.  
`password` |  `string` Input only. The credentials password. This is write only and can not be read in a GET operation.  
`vcenterIp` |  `string` The ip address of the vcenter this Source represents.  
`thumbprint` |  `string` The thumbprint representing the certificate for the vcenter.  
`resolvedVcenterHost` |  `string` The hostname of the vcenter.  
  
## AwsSourceDetails

AwsSourceDetails message describes a specific source details for the AWS source type.

JSON representation  
---  
      
    
    {
      "awsRegion": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#State)),
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status))
      },
      "inventoryTagList": [
        {
          object ([Tag](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#Tag))
        }
      ],
      "inventorySecurityGroupNames": [
        string
      ],
      "migrationResourcesUserTags": {
        string: string,
        ...
      },
      "publicIp": string,
    
      // Union field credentials_type can be only one of the following:
      "accessKeyCreds": {
        object ([AccessKeyCredentials](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AccessKeyCredentials))
      }
      // End of list of possible types for union field credentials_type.
    }  
  
Fields  
---  
`awsRegion` |  `string` Immutable. The AWS region that the source VMs will be migrated from.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#State)`)` Output only. State of the source as determined by the health check.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status)`)` Output only. Provides details on the state of the Source in case of an error.  
`inventoryTagList[]` |  `object (`[Tag](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#Tag)`)` AWS resource tags to limit the scope of the source inventory.  
`inventorySecurityGroupNames[]` |  `string` AWS security group names to limit the scope of the source inventory.  
`migrationResourcesUserTags` |  `map (key: string, value: string)` User specified tags to add to every M2VM generated resource in AWS. These tags will be set in addition to the default tags that are set as part of the migration process. The tags must not begin with the reserved prefix `m2vm`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`publicIp` |  `string` Output only. The source's public IP. All communication initiated by this source will originate from this IP.  
Union field `credentials_type`.`credentials_type` can be only one of the following:  
`accessKeyCreds` |  `object (`[AccessKeyCredentials](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#AccessKeyCredentials)`)` AWS Credentials using access key id and secret.  
  
## AccessKeyCredentials

Message describing AWS Credentials using access key id and secret.

JSON representation  
---  
      
    
    {
      "accessKeyId": string,
      "secretAccessKey": string,
      "sessionToken": string
    }  
  
Fields  
---  
`accessKeyId` |  `string` AWS access key ID.  
`secretAccessKey` |  `string` Input only. AWS secret access key.  
`sessionToken` |  `string` Input only. AWS session token. Used only when AWS security token service (STS) is responsible for creating the temporary credentials.  
  
## State

The possible values of the state.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`PENDING` | The state was not sampled by the health checks yet.  
`FAILED` | The source is available but might not be usable yet due to invalid credentials or another reason. The error message will contain further details.  
`ACTIVE` | The source exists and its credentials were verified.  
  
## Tag

Tag is an AWS tag representation.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. Key of tag.  
`value` |  `string` Required. Value of tag.  
  
## AzureSourceDetails

AzureSourceDetails message describes a specific source details for the Azure source type.

JSON representation  
---  
      
    
    {
      "subscriptionId": string,
      "azureLocation": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#State_1)),
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status))
      },
      "migrationResourcesUserTags": {
        string: string,
        ...
      },
      "resourceGroupId": string,
    
      // Union field credentials_type can be only one of the following:
      "clientSecretCreds": {
        object ([ClientSecretCredentials](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#ClientSecretCredentials))
      }
      // End of list of possible types for union field credentials_type.
    }  
  
Fields  
---  
`subscriptionId` |  `string` Immutable. Azure subscription ID.  
`azureLocation` |  `string` Immutable. The Azure location (region) that the source VMs will be migrated from.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#State_1)`)` Output only. State of the source as determined by the health check.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status)`)` Output only. Provides details on the state of the Source in case of an error.  
`migrationResourcesUserTags` |  `map (key: string, value: string)` User specified tags to add to every M2VM generated resource in Azure. These tags will be set in addition to the default tags that are set as part of the migration process. The tags must not begin with the reserved prefix `m4ce` or `m2vm`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`resourceGroupId` |  `string` Output only. The ID of the Azure resource group that contains all resources related to the migration process of this source.  
Union field `credentials_type`.`credentials_type` can be only one of the following:  
`clientSecretCreds` |  `object (`[ClientSecretCredentials](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources#ClientSecretCredentials)`)` Azure Credentials using tenant ID, client ID and secret.  
  
## ClientSecretCredentials

Message describing Azure Credentials using tenant ID, client ID and secret.

JSON representation  
---  
      
    
    {
      "tenantId": string,
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`tenantId` |  `string` Azure tenant ID.  
`clientId` |  `string` Azure client ID.  
`clientSecret` |  `string` Input only. Azure client secret.  
  
## State

The possible values of the state.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`PENDING` | The state was not sampled by the health checks yet.  
`FAILED` | The source is available but might not be usable yet due to invalid credentials or another reason. The error message will contain further details.  
`ACTIVE` | The source exists and its credentials were verified.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/create)`

|  Creates a new Source in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/delete)`

|  Deletes a single Source.  
  
### `[fetchInventory](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/fetchInventory)`

|  List remote source's inventory of VMs.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/get)`

|  Gets details of a single Source.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/list)`

|  Lists Sources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/patch)`

|  Updates the parameters of a single Source.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
