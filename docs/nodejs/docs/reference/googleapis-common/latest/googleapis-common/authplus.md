---
url: https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/latest/googleapis-common/authplus/
title: Class AuthPlus (7.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.994396+00:00
---

# Class AuthPlus (7.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/latest/googleapis-common/authplus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class AuthPlus (7.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 7.1.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/latest/googleapis-common/authplus/)
  * [ 7.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/7.0.1/googleapis-common/authplus/)
  * [ 6.0.3 ](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/6.0.3/googleapis-common/authplus/)
  * [ 5.1.0 ](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/5.1.0/googleapis-common/authplus/)
  * [ 5.0.5 ](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/5.0.5/googleapis-common/authplus/)



## Inheritance

[GoogleAuth](https://cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth) > AuthPlus

## Package

[googleapis-common](https://docs.cloud.google.com/nodejs/docs/reference/googleapis-common/latest/overview.html)

## Properties 

### AwsClient
    
    
    AwsClient: typeof AwsClient;

### Compute
    
    
    Compute: typeof Compute;

### ExternalAccountClient
    
    
    ExternalAccountClient: typeof ExternalAccountClient;

### GoogleAuth
    
    
    GoogleAuth: typeof GoogleAuth;

### IdentityPoolClient
    
    
    IdentityPoolClient: typeof IdentityPoolClient;

### JWT
    
    
    JWT: typeof JWT;

### OAuth2
    
    
    OAuth2: typeof OAuth2Client;

## Methods 

### getClient(options)
    
    
    getClient(options?: GoogleAuthOptions): Promise<Compute | JWT | UserRefreshClient | BaseExternalAccountClient | Impersonated>;

Override getClient(), memoizing an instance of auth for subsequent calls to getProjectId().

**Parameter**  
---  
**Name** | **Description**  
`options` |  `[GoogleAuthOptions](https://cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauthoptions)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<Compute | JWT | UserRefreshClient | BaseExternalAccountClient | Impersonated>` |   
  
### getProjectId()
    
    
    getProjectId(): Promise<string>;

Override getProjectId(), using the most recently configured auth instance when fetching projectId.

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### getProjectId(callback)
    
    
    getProjectId(callback: ProjectIdCallback): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `[ProjectIdCallback](https://cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/projectidcallback)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
