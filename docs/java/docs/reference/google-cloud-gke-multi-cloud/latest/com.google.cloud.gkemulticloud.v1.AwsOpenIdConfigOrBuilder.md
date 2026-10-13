---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AwsOpenIdConfigOrBuilder
title: Interface AwsOpenIdConfigOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:29.713358+00:00
---

# Interface AwsOpenIdConfigOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AwsOpenIdConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AwsOpenIdConfigOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.0 
    
    
    public interface AwsOpenIdConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClaimsSupported(int index) (deprecated)
    
    
    public abstract String getClaimsSupported(int index)

Supported claims.

`repeated string claims_supported = 6 [json_name = "claims_supported"];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The claimsSupported at the given index.  
  
### getClaimsSupportedBytes(int index) (deprecated)
    
    
    public abstract ByteString getClaimsSupportedBytes(int index)

Supported claims.

`repeated string claims_supported = 6 [json_name = "claims_supported"];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the claimsSupported at the given index.  
  
### getClaimsSupportedCount() (deprecated)
    
    
    public abstract int getClaimsSupportedCount()

Supported claims.

`repeated string claims_supported = 6 [json_name = "claims_supported"];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of claimsSupported.  
  
### getClaimsSupportedList() (deprecated)
    
    
    public abstract List<String> getClaimsSupportedList()

Supported claims.

`repeated string claims_supported = 6 [json_name = "claims_supported"];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the claimsSupported.  
  
### getGrantTypes(int index) (deprecated)
    
    
    public abstract String getGrantTypes(int index)

Supported grant types.

`repeated string grant_types = 7 [json_name = "grant_types"];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The grantTypes at the given index.  
  
### getGrantTypesBytes(int index) (deprecated)
    
    
    public abstract ByteString getGrantTypesBytes(int index)

Supported grant types.

`repeated string grant_types = 7 [json_name = "grant_types"];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the grantTypes at the given index.  
  
### getGrantTypesCount() (deprecated)
    
    
    public abstract int getGrantTypesCount()

Supported grant types.

`repeated string grant_types = 7 [json_name = "grant_types"];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of grantTypes.  
  
### getGrantTypesList() (deprecated)
    
    
    public abstract List<String> getGrantTypesList()

Supported grant types.

`repeated string grant_types = 7 [json_name = "grant_types"];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the grantTypes.  
  
### getIdTokenSigningAlgValuesSupported(int index) (deprecated)
    
    
    public abstract String getIdTokenSigningAlgValuesSupported(int index)

supported ID Token signing Algorithms.

` repeated string id_token_signing_alg_values_supported = 5 [json_name = "id_token_signing_alg_values_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The idTokenSigningAlgValuesSupported at the given index.  
  
### getIdTokenSigningAlgValuesSupportedBytes(int index) (deprecated)
    
    
    public abstract ByteString getIdTokenSigningAlgValuesSupportedBytes(int index)

supported ID Token signing Algorithms.

` repeated string id_token_signing_alg_values_supported = 5 [json_name = "id_token_signing_alg_values_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the idTokenSigningAlgValuesSupported at the given index.  
  
### getIdTokenSigningAlgValuesSupportedCount() (deprecated)
    
    
    public abstract int getIdTokenSigningAlgValuesSupportedCount()

supported ID Token signing Algorithms.

` repeated string id_token_signing_alg_values_supported = 5 [json_name = "id_token_signing_alg_values_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of idTokenSigningAlgValuesSupported.  
  
### getIdTokenSigningAlgValuesSupportedList() (deprecated)
    
    
    public abstract List<String> getIdTokenSigningAlgValuesSupportedList()

supported ID Token signing Algorithms.

` repeated string id_token_signing_alg_values_supported = 5 [json_name = "id_token_signing_alg_values_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the idTokenSigningAlgValuesSupported.  
  
### getIssuer() (deprecated)
    
    
    public abstract String getIssuer()

OIDC Issuer.

`string issuer = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The issuer.  
  
### getIssuerBytes() (deprecated)
    
    
    public abstract ByteString getIssuerBytes()

OIDC Issuer.

`string issuer = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for issuer.  
  
### getJwksUri() (deprecated)
    
    
    public abstract String getJwksUri()

JSON Web Key uri.

`string jwks_uri = 2 [json_name = "jwks_uri"];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The jwksUri.  
  
### getJwksUriBytes() (deprecated)
    
    
    public abstract ByteString getJwksUriBytes()

JSON Web Key uri.

`string jwks_uri = 2 [json_name = "jwks_uri"];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for jwksUri.  
  
### getResponseTypesSupported(int index) (deprecated)
    
    
    public abstract String getResponseTypesSupported(int index)

Supported response types.

`repeated string response_types_supported = 3 [json_name = "response_types_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The responseTypesSupported at the given index.  
  
### getResponseTypesSupportedBytes(int index) (deprecated)
    
    
    public abstract ByteString getResponseTypesSupportedBytes(int index)

Supported response types.

`repeated string response_types_supported = 3 [json_name = "response_types_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the responseTypesSupported at the given index.  
  
### getResponseTypesSupportedCount() (deprecated)
    
    
    public abstract int getResponseTypesSupportedCount()

Supported response types.

`repeated string response_types_supported = 3 [json_name = "response_types_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of responseTypesSupported.  
  
### getResponseTypesSupportedList() (deprecated)
    
    
    public abstract List<String> getResponseTypesSupportedList()

Supported response types.

`repeated string response_types_supported = 3 [json_name = "response_types_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the responseTypesSupported.  
  
### getSubjectTypesSupported(int index) (deprecated)
    
    
    public abstract String getSubjectTypesSupported(int index)

Supported subject types.

`repeated string subject_types_supported = 4 [json_name = "subject_types_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subjectTypesSupported at the given index.  
  
### getSubjectTypesSupportedBytes(int index) (deprecated)
    
    
    public abstract ByteString getSubjectTypesSupportedBytes(int index)

Supported subject types.

`repeated string subject_types_supported = 4 [json_name = "subject_types_supported"]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subjectTypesSupported at the given index.  
  
### getSubjectTypesSupportedCount() (deprecated)
    
    
    public abstract int getSubjectTypesSupportedCount()

Supported subject types.

`repeated string subject_types_supported = 4 [json_name = "subject_types_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subjectTypesSupported.  
  
### getSubjectTypesSupportedList() (deprecated)
    
    
    public abstract List<String> getSubjectTypesSupportedList()

Supported subject types.

`repeated string subject_types_supported = 4 [json_name = "subject_types_supported"]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subjectTypesSupported.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
