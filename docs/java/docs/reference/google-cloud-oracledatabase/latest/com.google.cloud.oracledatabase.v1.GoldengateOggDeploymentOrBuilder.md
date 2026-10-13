---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateOggDeploymentOrBuilder
title: Interface GoldengateOggDeploymentOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:06.227032+00:00
---

# Interface GoldengateOggDeploymentOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateOggDeploymentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GoldengateOggDeploymentOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GoldengateOggDeploymentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdminPassword()
    
    
    public abstract String getAdminPassword()

Optional. The Goldengate deployment console password in plain text.

`string admin_password = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adminPassword.  
  
### getAdminPasswordBytes()
    
    
    public abstract ByteString getAdminPasswordBytes()

Optional. The Goldengate deployment console password in plain text.

`string admin_password = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adminPassword.  
  
### getAdminPasswordSecretVersion()
    
    
    public abstract String getAdminPasswordSecretVersion()

Optional. Input only. The Goldengate deployment console password secret version.

` string admin_password_secret_version = 10 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adminPasswordSecretVersion.  
  
### getAdminPasswordSecretVersionBytes()
    
    
    public abstract ByteString getAdminPasswordSecretVersionBytes()

Optional. Input only. The Goldengate deployment console password secret version.

` string admin_password_secret_version = 10 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adminPasswordSecretVersion.  
  
### getAdminUsername()
    
    
    public abstract String getAdminUsername()

Required. The Goldengate deployment console username.

`string admin_username = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adminUsername.  
  
### getAdminUsernameBytes()
    
    
    public abstract ByteString getAdminUsernameBytes()

Required. The Goldengate deployment console username.

`string admin_username = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adminUsername.  
  
### getCertificate()
    
    
    public abstract String getCertificate()

Output only. The certificate of the GoldengateDeployment.

`string certificate = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The certificate.  
  
### getCertificateBytes()
    
    
    public abstract ByteString getCertificateBytes()

Output only. The certificate of the GoldengateDeployment.

`string certificate = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for certificate.  
  
### getCredentialStore()
    
    
    public abstract GoldengateOggDeployment.CredentialStore getCredentialStore()

Output only. The credential store of the GoldengateDeployment.

` .google.cloud.oracledatabase.v1.GoldengateOggDeployment.CredentialStore credential_store = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateOggDeployment.CredentialStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateOggDeployment.CredentialStore)` | The credentialStore.  
  
### getCredentialStoreValue()
    
    
    public abstract int getCredentialStoreValue()

Output only. The credential store of the GoldengateDeployment.

` .google.cloud.oracledatabase.v1.GoldengateOggDeployment.CredentialStore credential_store = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for credentialStore.  
  
### getDeployment()
    
    
    public abstract String getDeployment()

Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`string deployment = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deployment.  
  
### getDeploymentBytes()
    
    
    public abstract ByteString getDeploymentBytes()

Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`string deployment = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deployment.  
  
### getDeploymentPasswordOptionsCase()
    
    
    public abstract GoldengateOggDeployment.DeploymentPasswordOptionsCase getDeploymentPasswordOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[GoldengateOggDeployment.DeploymentPasswordOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateOggDeployment.DeploymentPasswordOptionsCase)` |   
  
### getGroupRolesMapping()
    
    
    public abstract GoldengateGroupToRolesMapping getGroupRolesMapping()

Output only. The group to roles mapping of the GoldengateDeployment.

` .google.cloud.oracledatabase.v1.GoldengateGroupToRolesMapping group_roles_mapping = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateGroupToRolesMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateGroupToRolesMapping)` | The groupRolesMapping.  
  
### getGroupRolesMappingOrBuilder()
    
    
    public abstract GoldengateGroupToRolesMappingOrBuilder getGroupRolesMappingOrBuilder()

Output only. The group to roles mapping of the GoldengateDeployment.

` .google.cloud.oracledatabase.v1.GoldengateGroupToRolesMapping group_roles_mapping = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateGroupToRolesMappingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateGroupToRolesMappingOrBuilder)` |   
  
### getIdentityDomainId()
    
    
    public abstract String getIdentityDomainId()

Output only. The identity domain id of the GoldengateDeployment.

`string identity_domain_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The identityDomainId.  
  
### getIdentityDomainIdBytes()
    
    
    public abstract ByteString getIdentityDomainIdBytes()

Output only. The identity domain id of the GoldengateDeployment.

`string identity_domain_id = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for identityDomainId.  
  
### getOggVersion()
    
    
    public abstract String getOggVersion()

Optional. Version of OGG

`string ogg_version = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The oggVersion.  
  
### getOggVersionBytes()
    
    
    public abstract ByteString getOggVersionBytes()

Optional. Version of OGG

`string ogg_version = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for oggVersion.  
  
### getPasswordSecretId()
    
    
    public abstract String getPasswordSecretId()

Output only. The password secret id of the GoldengateDeployment.

`string password_secret_id = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The passwordSecretId.  
  
### getPasswordSecretIdBytes()
    
    
    public abstract ByteString getPasswordSecretIdBytes()

Output only. The password secret id of the GoldengateDeployment.

`string password_secret_id = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for passwordSecretId.  
  
### hasAdminPassword()
    
    
    public abstract boolean hasAdminPassword()

Optional. The Goldengate deployment console password in plain text.

`string admin_password = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adminPassword field is set.  
  
### hasAdminPasswordSecretVersion()
    
    
    public abstract boolean hasAdminPasswordSecretVersion()

Optional. Input only. The Goldengate deployment console password secret version.

` string admin_password_secret_version = 10 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adminPasswordSecretVersion field is set.  
  
### hasGroupRolesMapping()
    
    
    public abstract boolean hasGroupRolesMapping()

Output only. The group to roles mapping of the GoldengateDeployment.

` .google.cloud.oracledatabase.v1.GoldengateGroupToRolesMapping group_roles_mapping = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the groupRolesMapping field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
