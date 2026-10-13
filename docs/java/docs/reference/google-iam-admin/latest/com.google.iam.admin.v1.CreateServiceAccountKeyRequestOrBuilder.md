---
url: https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountKeyRequestOrBuilder
title: Interface CreateServiceAccountKeyRequestOrBuilder (3.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:24.981036+00:00
---

# Interface CreateServiceAccountKeyRequestOrBuilder (3.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountKeyRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateServiceAccountKeyRequestOrBuilder (3.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.94.0 (latest)  3.90.0  3.89.0  3.88.0  3.86.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.73.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.65.0  3.63.0  3.62.0  3.59.0  3.58.0  3.57.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.2.5  1.1.8  0.2.0 
    
    
    public interface CreateServiceAccountKeyRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getKeyAlgorithm()
    
    
    public abstract ServiceAccountKeyAlgorithm getKeyAlgorithm()

Which type of key and algorithm to use for the key. The default is currently a 2K RSA key. However this may change in the future.

`.google.iam.admin.v1.ServiceAccountKeyAlgorithm key_algorithm = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKeyAlgorithm)` | The keyAlgorithm.  
  
### getKeyAlgorithmValue()
    
    
    public abstract int getKeyAlgorithmValue()

Which type of key and algorithm to use for the key. The default is currently a 2K RSA key. However this may change in the future.

`.google.iam.admin.v1.ServiceAccountKeyAlgorithm key_algorithm = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for keyAlgorithm.  
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrivateKeyType()
    
    
    public abstract ServiceAccountPrivateKeyType getPrivateKeyType()

The output format of the private key. The default value is `TYPE_GOOGLE_CREDENTIALS_FILE`, which is the Google Credentials File format.

`.google.iam.admin.v1.ServiceAccountPrivateKeyType private_key_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ServiceAccountPrivateKeyType](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountPrivateKeyType)` | The privateKeyType.  
  
### getPrivateKeyTypeValue()
    
    
    public abstract int getPrivateKeyTypeValue()

The output format of the private key. The default value is `TYPE_GOOGLE_CREDENTIALS_FILE`, which is the Google Credentials File format.

`.google.iam.admin.v1.ServiceAccountPrivateKeyType private_key_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for privateKeyType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
