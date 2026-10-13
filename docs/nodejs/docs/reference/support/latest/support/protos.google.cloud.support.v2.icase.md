---
url: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2.icase
title: Interface protos.google.cloud.support.v2.ICase (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:59.522803+00:00
---

# Interface protos.google.cloud.support.v2.ICase (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2.icase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.support.v2.ICase (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.5.0  2.4.0  1.0.2 

Properties of a Case.

## Package

[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)

## Properties 

### classification
    
    
    classification?: (google.cloud.support.v2.ICaseClassification|null);

Case classification

### contactEmail
    
    
    contactEmail?: (string|null);

Case contactEmail

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Case createTime

### creator
    
    
    creator?: (google.cloud.support.v2.IActor|null);

Case creator

### description
    
    
    description?: (string|null);

Case description

### displayName
    
    
    displayName?: (string|null);

Case displayName

### escalated
    
    
    escalated?: (boolean|null);

Case escalated

### languageCode
    
    
    languageCode?: (string|null);

Case languageCode

### name
    
    
    name?: (string|null);

Case name

### priority
    
    
    priority?: (google.cloud.support.v2.Case.Priority|keyof typeof google.cloud.support.v2.Case.Priority|null);

Case priority

### state
    
    
    state?: (google.cloud.support.v2.Case.State|keyof typeof google.cloud.support.v2.Case.State|null);

Case state

### subscriberEmailAddresses
    
    
    subscriberEmailAddresses?: (string[]|null);

Case subscriberEmailAddresses

### testCase
    
    
    testCase?: (boolean|null);

Case testCase

### timeZone
    
    
    timeZone?: (string|null);

Case timeZone

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Case updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
