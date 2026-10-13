---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequestOrBuilder
title: Interface FinishOAuthRequestOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:30.251785+00:00
---

# Interface FinishOAuthRequestOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FinishOAuthRequestOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface FinishOAuthRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccountConnector()
    
    
    public abstract String getAccountConnector()

Required. The resource name of the AccountConnector in the format `projects/*/locations/*/accountConnectors/*`.

` string account_connector = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The accountConnector.  
  
### getAccountConnectorBytes()
    
    
    public abstract ByteString getAccountConnectorBytes()

Required. The resource name of the AccountConnector in the format `projects/*/locations/*/accountConnectors/*`.

` string account_connector = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for accountConnector.  
  
### getGoogleOauthParams()
    
    
    public abstract FinishOAuthRequest.GoogleOAuthParams getGoogleOauthParams()

The params returned by Google OAuth flow redirects.

` .google.cloud.developerconnect.v1.FinishOAuthRequest.GoogleOAuthParams google_oauth_params = 3; `

**Returns**  
---  
**Type** | **Description**  
`[FinishOAuthRequest.GoogleOAuthParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequest.GoogleOAuthParams)` | The googleOauthParams.  
  
### getGoogleOauthParamsOrBuilder()
    
    
    public abstract FinishOAuthRequest.GoogleOAuthParamsOrBuilder getGoogleOauthParamsOrBuilder()

The params returned by Google OAuth flow redirects.

` .google.cloud.developerconnect.v1.FinishOAuthRequest.GoogleOAuthParams google_oauth_params = 3; `

**Returns**  
---  
**Type** | **Description**  
`[FinishOAuthRequest.GoogleOAuthParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequest.GoogleOAuthParamsOrBuilder)` |   
  
### getOauthParams()
    
    
    public abstract FinishOAuthRequest.OAuthParams getOauthParams()

The params returned by non-Google OAuth 2.0 flow redirect.

`.google.cloud.developerconnect.v1.FinishOAuthRequest.OAuthParams oauth_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FinishOAuthRequest.OAuthParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequest.OAuthParams)` | The oauthParams.  
  
### getOauthParamsOrBuilder()
    
    
    public abstract FinishOAuthRequest.OAuthParamsOrBuilder getOauthParamsOrBuilder()

The params returned by non-Google OAuth 2.0 flow redirect.

`.google.cloud.developerconnect.v1.FinishOAuthRequest.OAuthParams oauth_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FinishOAuthRequest.OAuthParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequest.OAuthParamsOrBuilder)` |   
  
### getParamsCase()
    
    
    public abstract FinishOAuthRequest.ParamsCase getParamsCase()

**Returns**  
---  
**Type** | **Description**  
`[FinishOAuthRequest.ParamsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-developerconnect/latest/com.google.cloud.developerconnect.v1.FinishOAuthRequest.ParamsCase)` |   
  
### hasGoogleOauthParams()
    
    
    public abstract boolean hasGoogleOauthParams()

The params returned by Google OAuth flow redirects.

` .google.cloud.developerconnect.v1.FinishOAuthRequest.GoogleOAuthParams google_oauth_params = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the googleOauthParams field is set.  
  
### hasOauthParams()
    
    
    public abstract boolean hasOauthParams()

The params returned by non-Google OAuth 2.0 flow redirect.

`.google.cloud.developerconnect.v1.FinishOAuthRequest.OAuthParams oauth_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oauthParams field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
