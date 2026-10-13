---
url: https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/googletoken/
title: Class GoogleToken (8.0.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:12.234616+00:00
---

# Class GoogleToken (8.0.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/googletoken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class GoogleToken (8.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 8.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/googletoken/)
  * [ 7.1.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/7.1.0/gtoken/googletoken/)
  * [ 7.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/7.0.1/gtoken/googletoken/)
  * [ 6.1.2 ](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/6.1.2/gtoken/googletoken/)
  * [ 5.3.2 ](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/5.3.2/gtoken/googletoken/)



## Package

[gtoken](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/overview.html)

## Constructors 

### (constructor)(options)
    
    
    constructor(options?: TokenOptions);

Create a GoogleToken.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `[TokenOptions](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/tokenoptions)`   
Configuration object.  
  
## Properties 

### accessToken
    
    
    get accessToken(): string | undefined;

### additionalClaims
    
    
    additionalClaims?: {};

### eagerRefreshThresholdMillis
    
    
    eagerRefreshThresholdMillis?: number;

### email
    
    
    email?: string;

### expiresAt
    
    
    expiresAt?: number;

### idToken
    
    
    get idToken(): string | undefined;

### iss
    
    
    iss?: string;

### key
    
    
    key?: string;

### keyFile
    
    
    keyFile?: string;

### rawToken
    
    
    rawToken?: TokenData;

### refreshToken
    
    
    get refreshToken(): string | undefined;

### scope
    
    
    scope?: string;

### sub
    
    
    sub?: string;

### tokenExpires
    
    
    tokenExpires?: number;

### tokenType
    
    
    get tokenType(): string | undefined;

### transporter
    
    
    transporter: Transporter;

## Methods 

### getCredentials(keyFile)
    
    
    getCredentials(keyFile: string): Promise<Credentials>;

Given a keyFile, extract the key and client email if available

**Parameter**  
---  
**Name** | **Description**  
`keyFile` |  `string`   
Path to a json, pem, or p12 file that contains the key.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[Credentials](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/credentials)>` | an object with privateKey and clientEmail properties  
  
### getToken(opts)
    
    
    getToken(opts?: GetTokenOptions): Promise<TokenData>;

Returns a cached token or retrieves a new one from Google.

**Parameter**  
---  
**Name** | **Description**  
`opts` |  `[GetTokenOptions](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/gettokenoptions)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[TokenData](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/tokendata)>` |   
  
### getToken(callback, opts)
    
    
    getToken(callback: GetTokenCallback, opts?: GetTokenOptions): void;

**Parameters**  
---  
**Name** | **Description**  
`callback` |  `[GetTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/overview.html)`   
  
`opts` |  `[GetTokenOptions](https://docs.cloud.google.com/nodejs/docs/reference/gtoken/latest/gtoken/gettokenoptions)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### hasExpired()
    
    
    hasExpired(): boolean;

Returns whether the token has expired.

true if the token has expired, false otherwise.

**Returns**  
---  
**Type** | **Description**  
`boolean` |   
  
### isTokenExpiring()
    
    
    isTokenExpiring(): boolean;

Returns whether the token will expire within eagerRefreshThresholdMillis

true if the token will be expired within eagerRefreshThresholdMillis, false otherwise.

**Returns**  
---  
**Type** | **Description**  
`boolean` |   
  
### revokeToken()
    
    
    revokeToken(): Promise<void>;

Revoke the token if one is set.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` |   
  
### revokeToken(callback)
    
    
    revokeToken(callback: (err?: Error) => void): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `(err?: Error) => void`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
