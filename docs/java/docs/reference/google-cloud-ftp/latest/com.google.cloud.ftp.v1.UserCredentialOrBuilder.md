---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredentialOrBuilder
title: Interface UserCredentialOrBuilder (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:00.359080+00:00
---

# Interface UserCredentialOrBuilder (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredentialOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UserCredentialOrBuilder (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface UserCredentialOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCredentialName()
    
    
    public abstract String getCredentialName()

Required. Name of the user credential.

`string credential_name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The credentialName.  
  
### getCredentialNameBytes()
    
    
    public abstract ByteString getCredentialNameBytes()

Required. Name of the user credential.

`string credential_name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for credentialName.  
  
### getCredentialType()
    
    
    public abstract UserCredential.Type getCredentialType()

Required. Type of credential.

` .google.cloud.ftp.v1.UserCredential.Type credential_type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCredential.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredential.Type)` | The credentialType.  
  
### getCredentialTypeValue()
    
    
    public abstract int getCredentialTypeValue()

Required. Type of credential.

` .google.cloud.ftp.v1.UserCredential.Type credential_type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for credentialType.  
  
### getSshPublicKeyBody()
    
    
    public abstract String getSshPublicKeyBody()

Optional. SSH public key body in OpenSSH format. Example: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ..."

`string ssh_public_key_body = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sshPublicKeyBody.  
  
### getSshPublicKeyBodyBytes()
    
    
    public abstract ByteString getSshPublicKeyBodyBytes()

Optional. SSH public key body in OpenSSH format. Example: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ..."

`string ssh_public_key_body = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sshPublicKeyBody.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
