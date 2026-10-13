---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder
title: Interface GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:52.371225+00:00
---

# Interface GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GoldengateAzureDataLakeStorageConnectionPropertiesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccount()
    
    
    public abstract String getAccount()

Optional. Sets the Azure storage account name.

`string account = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The account.  
  
### getAccountBytes()
    
    
    public abstract ByteString getAccountBytes()

Optional. Sets the Azure storage account name.

`string account = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for account.  
  
### getAccountKeySecret()
    
    
    public abstract String getAccountKeySecret()

Optional. Azure storage account key. This property is required when 'authentication_type' is set to 'SHARED_KEY'.

`string account_key_secret = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The accountKeySecret.  
  
### getAccountKeySecretBytes()
    
    
    public abstract ByteString getAccountKeySecretBytes()

Optional. Azure storage account key. This property is required when 'authentication_type' is set to 'SHARED_KEY'.

`string account_key_secret = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for accountKeySecret.  
  
### getAuthenticationType()
    
    
    public abstract GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType getAuthenticationType()

Optional. Authentication mechanism to access Azure Data Lake Storage.

` .google.cloud.oracledatabase.v1.GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType authentication_type = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType)` | The authenticationType.  
  
### getAuthenticationTypeValue()
    
    
    public abstract int getAuthenticationTypeValue()

Optional. Authentication mechanism to access Azure Data Lake Storage.

` .google.cloud.oracledatabase.v1.GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType authentication_type = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authenticationType.  
  
### getAzureAuthorityHost()
    
    
    public abstract String getAzureAuthorityHost()

Optional. The endpoint used for authentication with Microsoft Entra ID (formerly Azure Active Directory). Default value: <https://login.microsoftonline.com>

`string azure_authority_host = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The azureAuthorityHost.  
  
### getAzureAuthorityHostBytes()
    
    
    public abstract ByteString getAzureAuthorityHostBytes()

Optional. The endpoint used for authentication with Microsoft Entra ID (formerly Azure Active Directory). Default value: <https://login.microsoftonline.com>

`string azure_authority_host = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for azureAuthorityHost.  
  
### getAzureTenantId()
    
    
    public abstract String getAzureTenantId()

Optional. Azure tenant ID of the application. This property is required when 'authentication_type' is set to 'AZURE_ACTIVE_DIRECTORY'.

`string azure_tenant_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The azureTenantId.  
  
### getAzureTenantIdBytes()
    
    
    public abstract ByteString getAzureTenantIdBytes()

Optional. Azure tenant ID of the application. This property is required when 'authentication_type' is set to 'AZURE_ACTIVE_DIRECTORY'.

`string azure_tenant_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for azureTenantId.  
  
### getClientId()
    
    
    public abstract String getClientId()

Optional. Azure client ID of the application. This property is required when 'authentication_type' is set to 'AZURE_ACTIVE_DIRECTORY'.

`string client_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientId.  
  
### getClientIdBytes()
    
    
    public abstract ByteString getClientIdBytes()

Optional. Azure client ID of the application. This property is required when 'authentication_type' is set to 'AZURE_ACTIVE_DIRECTORY'.

`string client_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientId.  
  
### getClientSecret()
    
    
    public abstract String getClientSecret()

Optional. Azure client secret (aka application password) for authentication.

`string client_secret = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientSecret.  
  
### getClientSecretBytes()
    
    
    public abstract ByteString getClientSecretBytes()

Optional. Azure client secret (aka application password) for authentication.

`string client_secret = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientSecret.  
  
### getEndpoint()
    
    
    public abstract String getEndpoint()

Optional. Azure Storage service endpoint. e.g: <https://test.blob.core.windows.net>

`string endpoint = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpoint.  
  
### getEndpointBytes()
    
    
    public abstract ByteString getEndpointBytes()

Optional. Azure Storage service endpoint. e.g: <https://test.blob.core.windows.net>

`string endpoint = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpoint.  
  
### getSasTokenSecret()
    
    
    public abstract String getSasTokenSecret()

Optional. Credential that uses a shared access signature (SAS) to authenticate to an Azure Service.

`string sas_token_secret = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sasTokenSecret.  
  
### getSasTokenSecretBytes()
    
    
    public abstract ByteString getSasTokenSecretBytes()

Optional. Credential that uses a shared access signature (SAS) to authenticate to an Azure Service.

`string sas_token_secret = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sasTokenSecret.  
  
### getTechnologyType()
    
    
    public abstract String getTechnologyType()

Optional. The technology type of AzureDataLakeStorageConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The technologyType.  
  
### getTechnologyTypeBytes()
    
    
    public abstract ByteString getTechnologyTypeBytes()

Optional. The technology type of AzureDataLakeStorageConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for technologyType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
