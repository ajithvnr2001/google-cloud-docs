---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ThreeLeggedOAuthOrBuilder
title: Interface ThreeLeggedOAuthOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:57.734544+00:00
---

# Interface ThreeLeggedOAuthOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ThreeLeggedOAuthOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ThreeLeggedOAuthOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface ThreeLeggedOAuthOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthorizationUrl()
    
    
    public abstract String getAuthorizationUrl()

Optional. The authorization endpoint to send users to for consenting to delegate to the agent. eg. "<https://auth.example.com/authorize>"

`string authorization_url = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The authorizationUrl.  
  
### getAuthorizationUrlBytes()
    
    
    public abstract ByteString getAuthorizationUrlBytes()

Optional. The authorization endpoint to send users to for consenting to delegate to the agent. eg. "<https://auth.example.com/authorize>"

`string authorization_url = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for authorizationUrl.  
  
### getClientId()
    
    
    public abstract String getClientId()

Optional. The client ID of the OAuth client.

`string client_id = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientId.  
  
### getClientIdBytes()
    
    
    public abstract ByteString getClientIdBytes()

Optional. The client ID of the OAuth client.

`string client_id = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientId.  
  
### getClientSecret()
    
    
    public abstract String getClientSecret()

Optional. Input only. The client secret of the OAuth client.

` string client_secret = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientSecret.  
  
### getClientSecretBytes()
    
    
    public abstract ByteString getClientSecretBytes()

Optional. Input only. The client secret of the OAuth client.

` string client_secret = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientSecret.  
  
### getDefaultContinueUri()
    
    
    public abstract String getDefaultContinueUri()

Optional. The default continue URI for 3LO flow and it will be used when no continue URI is provided in the RetrieveCredentials request.

`string default_continue_uri = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The defaultContinueUri.  
  
### getDefaultContinueUriBytes()
    
    
    public abstract ByteString getDefaultContinueUriBytes()

Optional. The default continue URI for 3LO flow and it will be used when no continue URI is provided in the RetrieveCredentials request.

`string default_continue_uri = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for defaultContinueUri.  
  
### getEnablePkce()
    
    
    public abstract boolean getEnablePkce()

Optional. Enables Proof Key for Code Exchange (PKCE) for the OAuth flow to prevent authorization code interception attacks.

`bool enable_pkce = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePkce.  
  
### getRedirectUrl()
    
    
    public abstract String getRedirectUrl()

Output only. The redirect URL this auth_provider uses for the OAuth exchange. This is deterministic based on the name of the auth_provider.

`string redirect_url = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The redirectUrl.  
  
### getRedirectUrlBytes()
    
    
    public abstract ByteString getRedirectUrlBytes()

Output only. The redirect URL this auth_provider uses for the OAuth exchange. This is deterministic based on the name of the auth_provider.

`string redirect_url = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for redirectUrl.  
  
### getTokenUrl()
    
    
    public abstract String getTokenUrl()

Optional. The token endpoint for requesting tokens on behalf of an end user. eg. "<https://auth.example.com/oauth/token>"

`string token_url = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tokenUrl.  
  
### getTokenUrlBytes()
    
    
    public abstract ByteString getTokenUrlBytes()

Optional. The token endpoint for requesting tokens on behalf of an end user. eg. "<https://auth.example.com/oauth/token>"

`string token_url = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tokenUrl.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
