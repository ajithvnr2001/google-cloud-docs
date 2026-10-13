---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ServiceAccountAuthConfigOrBuilder
title: Interface ServiceAccountAuthConfigOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:24.732202+00:00
---

# Interface ServiceAccountAuthConfigOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ServiceAccountAuthConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServiceAccountAuthConfigOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ServiceAccountAuthConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getScopes(int index)
    
    
    public abstract String getScopes(int index)

Optional. The OAuth scopes to grant. If not specified, the default scope `<https://www.googleapis.com/auth/cloud-platform>` is used.

`repeated string scopes = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The scopes at the given index.  
  
### getScopesBytes(int index)
    
    
    public abstract ByteString getScopesBytes(int index)

Optional. The OAuth scopes to grant. If not specified, the default scope `<https://www.googleapis.com/auth/cloud-platform>` is used.

`repeated string scopes = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the scopes at the given index.  
  
### getScopesCount()
    
    
    public abstract int getScopesCount()

Optional. The OAuth scopes to grant. If not specified, the default scope `<https://www.googleapis.com/auth/cloud-platform>` is used.

`repeated string scopes = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of scopes.  
  
### getScopesList()
    
    
    public abstract List<String> getScopesList()

Optional. The OAuth scopes to grant. If not specified, the default scope `<https://www.googleapis.com/auth/cloud-platform>` is used.

`repeated string scopes = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the scopes.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.

The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.

`string service_account = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.

The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.

`string service_account = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
