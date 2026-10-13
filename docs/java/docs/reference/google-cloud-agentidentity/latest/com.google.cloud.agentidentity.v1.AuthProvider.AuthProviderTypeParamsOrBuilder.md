---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParamsOrBuilder
title: Interface AuthProvider.AuthProviderTypeParamsOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:54.879147+00:00
---

# Interface AuthProvider.AuthProviderTypeParamsOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParamsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AuthProvider.AuthProviderTypeParamsOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface AuthProvider.AuthProviderTypeParamsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiKey()
    
    
    public abstract ApiKeyParams getApiKey()

ApiKey AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ApiKeyParams api_key = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ApiKeyParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ApiKeyParams)` | The apiKey.  
  
### getApiKeyOrBuilder()
    
    
    public abstract ApiKeyParamsOrBuilder getApiKeyOrBuilder()

ApiKey AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ApiKeyParams api_key = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ApiKeyParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ApiKeyParamsOrBuilder)` |   
  
### getGeAuthProvider()
    
    
    public abstract GeminiEnterpriseAuthProviderParams getGeAuthProvider()

GeminiEnterprise auth_provider type parameters.

`.google.cloud.agentidentity.v1.GeminiEnterpriseAuthProviderParams ge_auth_provider = 4; `

**Returns**  
---  
**Type** | **Description**  
`[GeminiEnterpriseAuthProviderParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GeminiEnterpriseAuthProviderParams)` | The geAuthProvider.  
  
### getGeAuthProviderOrBuilder()
    
    
    public abstract GeminiEnterpriseAuthProviderParamsOrBuilder getGeAuthProviderOrBuilder()

GeminiEnterprise auth_provider type parameters.

`.google.cloud.agentidentity.v1.GeminiEnterpriseAuthProviderParams ge_auth_provider = 4; `

**Returns**  
---  
**Type** | **Description**  
`[GeminiEnterpriseAuthProviderParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GeminiEnterpriseAuthProviderParamsOrBuilder)` |   
  
### getThreeLeggedOauth()
    
    
    public abstract ThreeLeggedOAuth getThreeLeggedOauth()

ThreeLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ThreeLeggedOAuth three_legged_oauth = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ThreeLeggedOAuth](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ThreeLeggedOAuth)` | The threeLeggedOauth.  
  
### getThreeLeggedOauthOrBuilder()
    
    
    public abstract ThreeLeggedOAuthOrBuilder getThreeLeggedOauthOrBuilder()

ThreeLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ThreeLeggedOAuth three_legged_oauth = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ThreeLeggedOAuthOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ThreeLeggedOAuthOrBuilder)` |   
  
### getTwoLeggedOauth()
    
    
    public abstract TwoLeggedOAuth getTwoLeggedOauth()

TwoLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.TwoLeggedOAuth two_legged_oauth = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TwoLeggedOAuth](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.TwoLeggedOAuth)` | The twoLeggedOauth.  
  
### getTwoLeggedOauthOrBuilder()
    
    
    public abstract TwoLeggedOAuthOrBuilder getTwoLeggedOauthOrBuilder()

TwoLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.TwoLeggedOAuth two_legged_oauth = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TwoLeggedOAuthOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.TwoLeggedOAuthOrBuilder)` |   
  
### getTypeCase()
    
    
    public abstract AuthProvider.AuthProviderTypeParams.TypeCase getTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[AuthProvider.AuthProviderTypeParams.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParams.TypeCase)` |   
  
### hasApiKey()
    
    
    public abstract boolean hasApiKey()

ApiKey AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ApiKeyParams api_key = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the apiKey field is set.  
  
### hasGeAuthProvider()
    
    
    public abstract boolean hasGeAuthProvider()

GeminiEnterprise auth_provider type parameters.

`.google.cloud.agentidentity.v1.GeminiEnterpriseAuthProviderParams ge_auth_provider = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the geAuthProvider field is set.  
  
### hasThreeLeggedOauth()
    
    
    public abstract boolean hasThreeLeggedOauth()

ThreeLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.ThreeLeggedOAuth three_legged_oauth = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the threeLeggedOauth field is set.  
  
### hasTwoLeggedOauth()
    
    
    public abstract boolean hasTwoLeggedOauth()

TwoLeggedOAuth AuthProvider type parameters.

`.google.cloud.agentidentity.v1.TwoLeggedOAuth two_legged_oauth = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the twoLeggedOauth field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
