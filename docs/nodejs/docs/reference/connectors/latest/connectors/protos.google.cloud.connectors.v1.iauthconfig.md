---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iauthconfig
title: Interface protos.google.cloud.connectors.v1.IAuthConfig (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:43.828061+00:00
---

# Interface protos.google.cloud.connectors.v1.IAuthConfig (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iauthconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.connectors.v1.IAuthConfig (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Properties of an AuthConfig.

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Properties 

### additionalVariables
    
    
    additionalVariables?: (google.cloud.connectors.v1.IConfigVariable[]|null);

AuthConfig additionalVariables

### authType
    
    
    authType?: (google.cloud.connectors.v1.AuthType|keyof typeof google.cloud.connectors.v1.AuthType|null);

AuthConfig authType

### oauth2ClientCredentials
    
    
    oauth2ClientCredentials?: (google.cloud.connectors.v1.AuthConfig.IOauth2ClientCredentials|null);

AuthConfig oauth2ClientCredentials

### oauth2JwtBearer
    
    
    oauth2JwtBearer?: (google.cloud.connectors.v1.AuthConfig.IOauth2JwtBearer|null);

AuthConfig oauth2JwtBearer

### sshPublicKey
    
    
    sshPublicKey?: (google.cloud.connectors.v1.AuthConfig.ISshPublicKey|null);

AuthConfig sshPublicKey

### userPassword
    
    
    userPassword?: (google.cloud.connectors.v1.AuthConfig.IUserPassword|null);

AuthConfig userPassword

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
