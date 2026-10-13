---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfigOrBuilder
title: Interface EndUserAuthConfigOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:32.568482+00:00
---

# Interface EndUserAuthConfigOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EndUserAuthConfigOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface EndUserAuthConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthConfigCase()
    
    
    public abstract EndUserAuthConfig.AuthConfigCase getAuthConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[EndUserAuthConfig.AuthConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfig.AuthConfigCase)` |   
  
### getOauth2AuthCodeConfig()
    
    
    public abstract EndUserAuthConfig.Oauth2AuthCodeConfig getOauth2AuthCodeConfig()

Oauth 2.0 Authorization Code authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig oauth2_auth_code_config = 2; `

**Returns**  
---  
**Type** | **Description**  
`[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig)` | The oauth2AuthCodeConfig.  
  
### getOauth2AuthCodeConfigOrBuilder()
    
    
    public abstract EndUserAuthConfig.Oauth2AuthCodeConfigOrBuilder getOauth2AuthCodeConfigOrBuilder()

Oauth 2.0 Authorization Code authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig oauth2_auth_code_config = 2; `

**Returns**  
---  
**Type** | **Description**  
`[EndUserAuthConfig.Oauth2AuthCodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfigOrBuilder)` |   
  
### getOauth2JwtBearerConfig()
    
    
    public abstract EndUserAuthConfig.Oauth2JwtBearerConfig getOauth2JwtBearerConfig()

JWT Profile Oauth 2.0 Authorization Grant authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig oauth2_jwt_bearer_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig)` | The oauth2JwtBearerConfig.  
  
### getOauth2JwtBearerConfigOrBuilder()
    
    
    public abstract EndUserAuthConfig.Oauth2JwtBearerConfigOrBuilder getOauth2JwtBearerConfigOrBuilder()

JWT Profile Oauth 2.0 Authorization Grant authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig oauth2_jwt_bearer_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[EndUserAuthConfig.Oauth2JwtBearerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfigOrBuilder)` |   
  
### hasOauth2AuthCodeConfig()
    
    
    public abstract boolean hasOauth2AuthCodeConfig()

Oauth 2.0 Authorization Code authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig oauth2_auth_code_config = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oauth2AuthCodeConfig field is set.  
  
### hasOauth2JwtBearerConfig()
    
    
    public abstract boolean hasOauth2JwtBearerConfig()

JWT Profile Oauth 2.0 Authorization Grant authentication.

` .google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig oauth2_jwt_bearer_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oauth2JwtBearerConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
