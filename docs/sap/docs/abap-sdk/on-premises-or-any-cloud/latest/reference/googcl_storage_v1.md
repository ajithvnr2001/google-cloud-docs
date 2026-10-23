---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_storage_v1/
title: Class /GOOG/CL_STORAGE_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:05.076213+00:00
---

# Class /GOOG/CL_STORAGE_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_storage_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_STORAGE_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_storage_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_storage_v1)



## Class
    
    
    /GOOG/CL_STORAGE_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Storage JSON API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Bucket` | PUBLIC  
`TY_002` | `BucketAccessControl` | PUBLIC  
`TY_003` | `BucketAccessControls` | PUBLIC  
`TY_004` | `Buckets` | PUBLIC  
`TY_005` | `Channel` | PUBLIC  
`TY_006` | `ComposeRequest` | PUBLIC  
`TY_007` | `Expr` | PUBLIC  
`TY_008` | `HmacKey` | PUBLIC  
`TY_009` | `HmacKeyMetadata` | PUBLIC  
`TY_010` | `HmacKeysMetadata` | PUBLIC  
`TY_011` | `Notification` | PUBLIC  
`TY_012` | `Notifications` | PUBLIC  
`TY_013` | `Object` | PUBLIC  
`TY_014` | `ObjectAccessControl` | PUBLIC  
`TY_015` | `ObjectAccessControls` | PUBLIC  
`TY_016` | `Objects` | PUBLIC  
`TY_017` | `Policy` | PUBLIC  
`TY_018` | `RewriteResponse` | PUBLIC  
`TY_019` | `ServiceAccount` | PUBLIC  
`TY_020` | `TestIamPermissionsResponse` | PUBLIC  
`TY_042` | `Bindings` | PUBLIC  
`TY_043` | `ProjectTeam` | PUBLIC  
`TY_044` | `Autoclass` | PUBLIC  
`TY_045` | `Billing` | PUBLIC  
`TY_046` | `Cors` | PUBLIC  
`TY_047` | `CustomPlacementConfig` | PUBLIC  
`TY_049` | `Encryption` | PUBLIC  
`TY_050` | `BucketPolicyOnly` | PUBLIC  
`TY_051` | `UniformBucketLevelAccess` | PUBLIC  
`TY_052` | `IamConfiguration` | PUBLIC  
`TY_053` | `Action` | PUBLIC  
`TY_054` | `Condition` | PUBLIC  
`TY_055` | `Rule` | PUBLIC  
`TY_056` | `Lifecycle` | PUBLIC  
`TY_057` | `Logging` | PUBLIC  
`TY_058` | `Owner` | PUBLIC  
`TY_059` | `RetentionPolicy` | PUBLIC  
`TY_060` | `Versioning` | PUBLIC  
`TY_061` | `Website` | PUBLIC  
`TY_066` | `ObjectPreconditions` | PUBLIC  
`TY_067` | `SourceObjects` | PUBLIC  
`TY_071` | `ProjectTeam` | PUBLIC  
`TY_072` | `CustomerEncryption` | PUBLIC  
`TY_073` | `Owner` | PUBLIC  
`TY_074` | `AnywhereCache` | PUBLIC  
`TY_075` | `AnywhereCaches` | PUBLIC  
`TY_076` | `BulkRestoreObjectsRequest` | PUBLIC  
`TY_077` | `Folder` | PUBLIC  
`TY_078` | `Folders` | PUBLIC  
`TY_079` | `GoogleLongrunningListOperationsResponse` | PUBLIC  
`TY_080` | `GoogleLongrunningOperation` | PUBLIC  
`TY_081` | `GoogleRpcStatus` | PUBLIC  
`TY_082` | `ManagedFolder` | PUBLIC  
`TY_083` | `ManagedFolders` | PUBLIC  
`TY_087` | `HierarchicalNamespace` | PUBLIC  
`TY_088` | `ObjectRetention` | PUBLIC  
`TY_089` | `SoftDeletePolicy` | PUBLIC  
`TY_091` | `PendingRenameInfo` | PUBLIC  
`TY_094` | `Retention` | PUBLIC  
`TY_095` | `BucketStorageLayout` | PUBLIC  
`TY_099` | `CustomPlacementConfig` | PUBLIC  
`TY_100` | `HierarchicalNamespace` | PUBLIC  
`TY_101` | `PublicNetworkSource` | PUBLIC  
`TY_102` | `VpcNetworkSources` | PUBLIC  
`TY_103` | `IpFilter` | PUBLIC  
`TY_104` | `AdvanceRelocateBucketOperationRequest` | PUBLIC  
`TY_105` | `RelocateBucketRequest` | PUBLIC  
`TY_106` | `DestinationCustomPlacementC` | PUBLIC  
`TY_T_001` | `Bucket` | PUBLIC  
`TY_T_002` | `BucketAccessControl` | PUBLIC  
`TY_T_009` | `HmacKeyMetadata` | PUBLIC  
`TY_T_011` | `Notification` | PUBLIC  
`TY_T_013` | `Object` | PUBLIC  
`TY_T_014` | `ObjectAccessControl` | PUBLIC  
`TY_T_042` | `Bindings` | PUBLIC  
`TY_T_046` | `Cors` | PUBLIC  
`TY_T_055` | `Rule` | PUBLIC  
`TY_T_067` | `SourceObjects` | PUBLIC  
`TY_T_074` | `AnywhereCache` | PUBLIC  
`TY_T_077` | `Folder` | PUBLIC  
`TY_T_080` | `GoogleLongrunningOperation` | PUBLIC  
`TY_T_082` | `ManagedFolder` | PUBLIC  
`TY_T_102` | `VpcNetworkSources` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_MULTIPART` | `STRING` | Multipart Upload | multipart | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.0 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /storage/v1/ | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250304 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://storage.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | storage:v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_MULTIPART

  * Description: Add Multipart 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_XBODY` | IMPORTING | `XSTRING` | Body  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_BODY` | IMPORTING | `STRING` | Body  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADVANCE_RELOCATE_BUCKET_OPE

  * Description: storage.buckets.operations.advanceRelocateBucket 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OPERATION_ID` | IMPORTING | `STRING` | operationId  
`IS_INPUT` | IMPORTING | `TY_104` | AdvanceRelocateBucketOperationRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BULK_RESTORE_OBJECTS

  * Description: storage.objects.bulkRestore 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_076` | BulkRestoreObjectsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CANCEL_OPERATIONS

  * Description: storage.buckets.operations.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OPERATION_ID` | IMPORTING | `STRING` | operationId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COMPOSE_OBJECTS

  * Description: storage.objects.compose 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DESTINATIONPREDEFINEDACL` | IMPORTING | `STRING` | destinationPredefinedAcl  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_KMSKEYNAME` | IMPORTING | `STRING` | kmsKeyName  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_DESTINATION_BUCKET` | IMPORTING | `STRING` | destinationBucket  
`IV_P_DESTINATION_OBJECT` | IMPORTING | `STRING` | destinationObject  
`IS_INPUT` | IMPORTING | `TY_006` | ComposeRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COPY_OBJECTS

  * Description: storage.objects.copy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DESTINATIONKMSKEYNAME` | IMPORTING | `STRING` | destinationKmsKeyName  
`IV_Q_DESTINATIONPREDEFINEDACL` | IMPORTING | `STRING` | destinationPredefinedAcl  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_IFSOURCEGENERATIONMATCH` | IMPORTING | `STRING` | ifSourceGenerationMatch  
`IV_Q_IFSOURCEGENERATIONNOTMATC` | IMPORTING | `STRING` | ifSourceGenerationNotMatch  
`IV_Q_IFSOURCEMETAGENERATIONMAT` | IMPORTING | `STRING` | ifSourceMetagenerationMatch  
`IV_Q_IFSOURCEMETAGENERATIONNOT` | IMPORTING | `STRING` | ifSourceMetagenerationNotMatch  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_SOURCEGENERATION` | IMPORTING | `STRING` | sourceGeneration  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_DESTINATION_BUCKET` | IMPORTING | `STRING` | destinationBucket  
`IV_P_DESTINATION_OBJECT` | IMPORTING | `STRING` | destinationObject  
`IV_P_SOURCE_BUCKET` | IMPORTING | `STRING` | sourceBucket  
`IV_P_SOURCE_OBJECT` | IMPORTING | `STRING` | sourceObject  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_HMAC_KEYS

  * Description: storage.projects.hmacKeys.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SERVICEACCOUNTEMAIL` | IMPORTING | `STRING` | serviceAccountEmail  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | HmacKey  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_BUCKETS

  * Description: storage.buckets.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_BUCKET_ACCESS_CONTRO

  * Description: storage.bucketAccessControls.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DEFAULT_OBJECT_ACCES

  * Description: storage.defaultObjectAccessControls.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_FOLDERS

  * Description: storage.folders.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_FOLDER` | IMPORTING | `STRING` | folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_HMAC_KEYS

  * Description: storage.projects.hmacKeys.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_ACCESS_ID` | IMPORTING | `STRING` | accessId  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_MANAGED_FOLDERS

  * Description: storage.managedFolders.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWNONEMPTY` | IMPORTING | `STRING` | allowNonEmpty  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_MANAGED_FOLDER` | IMPORTING | `STRING` | managedFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_NOTIFICATIONS

  * Description: storage.notifications.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_NOTIFICATION` | IMPORTING | `STRING` | notification  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OBJECTS

  * Description: storage.objects.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OBJECT_ACCESS_CONTRO

  * Description: storage.objectAccessControls.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DISABLE_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.disable 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ANYWHERE_CACHE_ID` | IMPORTING | `STRING` | anywhereCacheId  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | AnywhereCache  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ANYWHERE_CACHE_ID` | IMPORTING | `STRING` | anywhereCacheId  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | AnywhereCache  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BUCKETS

  * Description: storage.buckets.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_SOFTDELETED` | IMPORTING | `STRING` | softDeleted  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BUCKET_ACCESS_CONTROLS

  * Description: storage.bucketAccessControls.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | BucketAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEFAULT_OBJECT_ACCESS_C

  * Description: storage.defaultObjectAccessControls.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FOLDERS

  * Description: storage.folders.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_FOLDER` | IMPORTING | `STRING` | folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_HMAC_KEYS

  * Description: storage.projects.hmacKeys.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_ACCESS_ID` | IMPORTING | `STRING` | accessId  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | HmacKeyMetadata  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_BUCKETS

  * Description: storage.buckets.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | optionsRequestedPolicyVersion  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_MANAGED_FOLD

  * Description: storage.managedFolders.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | optionsRequestedPolicyVersion  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_MANAGED_FOLDER` | IMPORTING | `STRING` | managedFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_OBJECTS

  * Description: storage.objects.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_MANAGED_FOLDERS

  * Description: storage.managedFolders.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_MANAGED_FOLDER` | IMPORTING | `STRING` | managedFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_082` | ManagedFolder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_NOTIFICATIONS

  * Description: storage.notifications.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_NOTIFICATION` | IMPORTING | `STRING` | notification  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Notification  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OBJECTS

  * Description: storage.objects.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_RESTORETOKEN` | IMPORTING | `STRING` | restoreToken  
`IV_Q_SOFTDELETED` | IMPORTING | `STRING` | softDeleted  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OBJECT_ACCESS_CONTROLS

  * Description: storage.objectAccessControls.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: storage.buckets.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OPERATION_ID` | IMPORTING | `STRING` | operationId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SERVICE_ACCOUNT

  * Description: storage.projects.serviceAccount.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | ServiceAccount  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_STORAGE_LAYOUT_BUCKETS

  * Description: storage.buckets.getStorageLayout 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_095` | BucketStorageLayout  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_074` | AnywhereCache  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_BUCKETS

  * Description: storage.buckets.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENABLEOBJECTRETENTION` | IMPORTING | `STRING` | enableObjectRetention  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PREDEFINEDDEFAULTOBJECTAC` | IMPORTING | `STRING` | predefinedDefaultObjectAcl  
`IV_Q_PROJECT` | IMPORTING | `STRING` | project  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IS_INPUT` | IMPORTING | `TY_001` | Bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_BUCKET_ACCESS_CONTRO

  * Description: storage.bucketAccessControls.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_002` | BucketAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | BucketAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_DEFAULT_OBJECT_ACCES

  * Description: storage.defaultObjectAccessControls.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_FOLDERS

  * Description: storage.folders.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_RECURSIVE` | IMPORTING | `STRING` | recursive  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_077` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_MANAGED_FOLDERS

  * Description: storage.managedFolders.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_082` | ManagedFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_082` | ManagedFolder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_NOTIFICATIONS

  * Description: storage.notifications.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_011` | Notification  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Notification  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_OBJECTS

  * Description: storage.objects.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONTENTENCODING` | IMPORTING | `STRING` | contentEncoding  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_KMSKEYNAME` | IMPORTING | `STRING` | kmsKeyName  
`IV_Q_NAME` | IMPORTING | `STRING` | name  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CHUNK_SIZE` | IMPORTING | `I` | Chunk Size  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_OBJECTS_MULTIPART

  * Description: Multipart Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_URI` | IMPORTING | `STRING` | URI  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_OBJECTS_RESUMABLE

  * Description: Resumable Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_URI` | IMPORTING | `STRING` | URI  
`IV_CHUNK_SIZE` | IMPORTING | `I` | Chunk Size  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_OBJECTS_SIMPLE

  * Description: Simple Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_URI` | IMPORTING | `STRING` | URI  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_OBJECT_ACCESS_CONTRO

  * Description: storage.objectAccessControls.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_075` | AnywhereCaches  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BUCKETS

  * Description: storage.buckets.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_Q_PROJECT` | IMPORTING | `STRING` | project  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_SOFTDELETED` | IMPORTING | `STRING` | softDeleted  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Buckets  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BUCKET_ACCESS_CONTROLS

  * Description: storage.bucketAccessControls.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | BucketAccessControls  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEFAULT_OBJECT_ACCESS

  * Description: storage.defaultObjectAccessControls.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | ObjectAccessControls  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FOLDERS

  * Description: storage.folders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DELIMITER` | IMPORTING | `STRING` | delimiter  
`IV_Q_ENDOFFSET` | IMPORTING | `STRING` | endOffset  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_Q_STARTOFFSET` | IMPORTING | `STRING` | startOffset  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_078` | Folders  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_HMAC_KEYS

  * Description: storage.projects.hmacKeys.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SERVICEACCOUNTEMAIL` | IMPORTING | `STRING` | serviceAccountEmail  
`IV_Q_SHOWDELETEDKEYS` | IMPORTING | `STRING` | showDeletedKeys  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | HmacKeysMetadata  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MANAGED_FOLDERS

  * Description: storage.managedFolders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_083` | ManagedFolders  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_NOTIFICATIONS

  * Description: storage.notifications.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Notifications  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OBJECTS

  * Description: storage.objects.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DELIMITER` | IMPORTING | `STRING` | delimiter  
`IV_Q_ENDOFFSET` | IMPORTING | `STRING` | endOffset  
`IV_Q_INCLUDEFOLDERSASPREFIXES` | IMPORTING | `STRING` | includeFoldersAsPrefixes  
`IV_Q_INCLUDETRAILINGDELIMITER` | IMPORTING | `STRING` | includeTrailingDelimiter  
`IV_Q_MATCHGLOB` | IMPORTING | `STRING` | matchGlob  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_SOFTDELETED` | IMPORTING | `STRING` | softDeleted  
`IV_Q_STARTOFFSET` | IMPORTING | `STRING` | startOffset  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_Q_VERSIONS` | IMPORTING | `STRING` | versions  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | Objects  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OBJECT_ACCESS_CONTROLS

  * Description: storage.objectAccessControls.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | ObjectAccessControls  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: storage.buckets.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_079` | GoogleLongrunningListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LOCK_RETENTION_POLICY_BUCKE

  * Description: storage.buckets.lockRetentionPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MOVE_OBJECTS

  * Description: storage.objects.move 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_IFSOURCEGENERATIONMATCH` | IMPORTING | `STRING` | ifSourceGenerationMatch  
`IV_Q_IFSOURCEGENERATIONNOTMATC` | IMPORTING | `STRING` | ifSourceGenerationNotMatch  
`IV_Q_IFSOURCEMETAGENERATIONMAT` | IMPORTING | `STRING` | ifSourceMetagenerationMatch  
`IV_Q_IFSOURCEMETAGENERATIONNOT` | IMPORTING | `STRING` | ifSourceMetagenerationNotMatch  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_DESTINATION_OBJECT` | IMPORTING | `STRING` | destinationObject  
`IV_P_SOURCE_OBJECT` | IMPORTING | `STRING` | sourceObject  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_BUCKETS

  * Description: storage.buckets.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PREDEFINEDDEFAULTOBJECTAC` | IMPORTING | `STRING` | predefinedDefaultObjectAcl  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_001` | Bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_BUCKET_ACCESS_CONTROL

  * Description: storage.bucketAccessControls.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IS_INPUT` | IMPORTING | `TY_002` | BucketAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | BucketAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEFAULT_OBJECT_ACCESS

  * Description: storage.defaultObjectAccessControls.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_OBJECTS

  * Description: storage.objects.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_OVERRIDEUNLOCKEDRETENTION` | IMPORTING | `STRING` | overrideUnlockedRetention  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_OBJECT_ACCESS_CONTROL

  * Description: storage.objectAccessControls.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PAUSE_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.pause 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ANYWHERE_CACHE_ID` | IMPORTING | `STRING` | anywhereCacheId  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | AnywhereCache  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RELOCATE_BUCKETS

  * Description: storage.buckets.relocate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_105` | RelocateBucketRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RENAME_FOLDERS

  * Description: storage.folders.rename 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFSOURCEMETAGENERATIONMAT` | IMPORTING | `STRING` | ifSourceMetagenerationMatch  
`IV_Q_IFSOURCEMETAGENERATIONNOT` | IMPORTING | `STRING` | ifSourceMetagenerationNotMatch  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_DESTINATION_FOLDER` | IMPORTING | `STRING` | destinationFolder  
`IV_P_SOURCE_FOLDER` | IMPORTING | `STRING` | sourceFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESTORE_BUCKETS

  * Description: storage.buckets.restore 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESTORE_OBJECTS

  * Description: storage.objects.restore 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_COPYSOURCEACL` | IMPORTING | `STRING` | copySourceAcl  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_RESTORETOKEN` | IMPORTING | `STRING` | restoreToken  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.resume 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ANYWHERE_CACHE_ID` | IMPORTING | `STRING` | anywhereCacheId  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | AnywhereCache  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD

  * Description: Resume Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_LAST_BYTE` | IMPORTING | `I` | Last Byte to upload  
`IV_SESSION_ID` | IMPORTING | `STRING` | Resumable Session Id  
`IV_START_BYTE` | IMPORTING | `I` | Start Byte to upload  
`IV_TOT_BYTES` | IMPORTING | `I` | Total Bytes to upload  
`EV_LAST_BYTE` | EXPORTING | `I` | Last Byte uploaded  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_CREATE_REQ

  * Description: Resume Upload Create Request 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_SESSION_ID` | IMPORTING | `STRING` | Resumable Session Id  
`EO_HTTP_CLIENT` | EXPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_HANDLE_RES

  * Description: Resume Upload Handle Request 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
`EV_LAST_BYTE` | EXPORTING | `I` | Last Byte uploaded  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_RECEIVE_RES

  * Description: Resume Upload Receive Response 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_SEND_REQ

  * Description: Resume Upload Send Request 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REWRITE_OBJECTS

  * Description: storage.objects.rewrite 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DESTINATIONKMSKEYNAME` | IMPORTING | `STRING` | destinationKmsKeyName  
`IV_Q_DESTINATIONPREDEFINEDACL` | IMPORTING | `STRING` | destinationPredefinedAcl  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_IFSOURCEGENERATIONMATCH` | IMPORTING | `STRING` | ifSourceGenerationMatch  
`IV_Q_IFSOURCEGENERATIONNOTMATC` | IMPORTING | `STRING` | ifSourceGenerationNotMatch  
`IV_Q_IFSOURCEMETAGENERATIONMAT` | IMPORTING | `STRING` | ifSourceMetagenerationMatch  
`IV_Q_IFSOURCEMETAGENERATIONNOT` | IMPORTING | `STRING` | ifSourceMetagenerationNotMatch  
`IV_Q_MAXBYTESREWRITTENPERCALL` | IMPORTING | `STRING` | maxBytesRewrittenPerCall  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_REWRITETOKEN` | IMPORTING | `STRING` | rewriteToken  
`IV_Q_SOURCEGENERATION` | IMPORTING | `STRING` | sourceGeneration  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_DESTINATION_BUCKET` | IMPORTING | `STRING` | destinationBucket  
`IV_P_DESTINATION_OBJECT` | IMPORTING | `STRING` | destinationObject  
`IV_P_SOURCE_BUCKET` | IMPORTING | `STRING` | sourceBucket  
`IV_P_SOURCE_OBJECT` | IMPORTING | `STRING` | sourceObject  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | RewriteResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_BUCKETS

  * Description: storage.buckets.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_017` | Policy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_MANAGED_FOLD

  * Description: storage.managedFolders.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_MANAGED_FOLDER` | IMPORTING | `STRING` | managedFolder  
`IS_INPUT` | IMPORTING | `TY_017` | Policy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_OBJECTS

  * Description: storage.objects.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_017` | Policy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_CHANNELS

  * Description: storage.channels.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_005` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_BUCKET

  * Description: storage.buckets.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PERMISSIONS` | IMPORTING | `STRING` | permissions  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | TestIamPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_MANAGE

  * Description: storage.managedFolders.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PERMISSIONS` | IMPORTING | `STRING` | permissions  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_MANAGED_FOLDER` | IMPORTING | `STRING` | managedFolder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | TestIamPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_OBJECT

  * Description: storage.objects.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_PERMISSIONS` | IMPORTING | `STRING` | permissions  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | TestIamPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_ANYWHERE_CACHES

  * Description: storage.anywhereCaches.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ANYWHERE_CACHE_ID` | IMPORTING | `STRING` | anywhereCacheId  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_074` | AnywhereCache  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_BUCKETS

  * Description: storage.buckets.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PREDEFINEDDEFAULTOBJECTAC` | IMPORTING | `STRING` | predefinedDefaultObjectAcl  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_001` | Bucket  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Bucket  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_BUCKET_ACCESS_CONTRO

  * Description: storage.bucketAccessControls.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IS_INPUT` | IMPORTING | `TY_002` | BucketAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | BucketAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_DEFAULT_OBJECT_ACCES

  * Description: storage.defaultObjectAccessControls.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_HMAC_KEYS

  * Description: storage.projects.hmacKeys.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_ACCESS_ID` | IMPORTING | `STRING` | accessId  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_009` | HmacKeyMetadata  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | HmacKeyMetadata  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_OBJECTS

  * Description: storage.objects.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_IFGENERATIONMATCH` | IMPORTING | `STRING` | ifGenerationMatch  
`IV_Q_IFGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifGenerationNotMatch  
`IV_Q_IFMETAGENERATIONMATCH` | IMPORTING | `STRING` | ifMetagenerationMatch  
`IV_Q_IFMETAGENERATIONNOTMATCH` | IMPORTING | `STRING` | ifMetagenerationNotMatch  
`IV_Q_OVERRIDEUNLOCKEDRETENTION` | IMPORTING | `STRING` | overrideUnlockedRetention  
`IV_Q_PREDEFINEDACL` | IMPORTING | `STRING` | predefinedAcl  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_013` | Object  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Object  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_OBJECT_ACCESS_CONTRO

  * Description: storage.objectAccessControls.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GENERATION` | IMPORTING | `STRING` | generation  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IV_P_ENTITY` | IMPORTING | `STRING` | entity  
`IV_P_OBJECT` | IMPORTING | `STRING` | object  
`IS_INPUT` | IMPORTING | `TY_014` | ObjectAccessControl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ObjectAccessControl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_ALL_OBJECTS

  * Description: storage.objects.watchAll 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DELIMITER` | IMPORTING | `STRING` | delimiter  
`IV_Q_ENDOFFSET` | IMPORTING | `STRING` | endOffset  
`IV_Q_INCLUDETRAILINGDELIMITER` | IMPORTING | `STRING` | includeTrailingDelimiter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PREFIX` | IMPORTING | `STRING` | prefix  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_STARTOFFSET` | IMPORTING | `STRING` | startOffset  
`IV_Q_USERPROJECT` | IMPORTING | `STRING` | userProject  
`IV_Q_VERSIONS` | IMPORTING | `STRING` | versions  
`IV_P_BUCKET` | IMPORTING | `STRING` | bucket  
`IS_INPUT` | IMPORTING | `TY_005` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Channel  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
