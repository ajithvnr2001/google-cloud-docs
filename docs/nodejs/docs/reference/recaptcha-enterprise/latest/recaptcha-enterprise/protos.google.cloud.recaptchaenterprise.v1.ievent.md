---
url: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.ievent
title: Interface protos.google.cloud.recaptchaenterprise.v1.IEvent (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:40.567454+00:00
---

# Interface protos.google.cloud.recaptchaenterprise.v1.IEvent (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.ievent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.recaptchaenterprise.v1.IEvent (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  6.2.0  6.0.1  5.13.0  5.11.0  5.10.0  5.8.0  5.5.0  5.4.0  5.2.0  5.1.1  5.0.0  4.1.0  3.4.1  3.3.1  3.1.1  3.0.4  2.5.0  2.4.0  2.3.0  2.2.1  2.1.7 

Properties of an Event.

## Package

[@google-cloud/recaptcha-enterprise](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/overview.html)

## Properties 

### expectedAction
    
    
    expectedAction?: (string|null);

Event expectedAction

### express
    
    
    express?: (boolean|null);

Event express

### firewallPolicyEvaluation
    
    
    firewallPolicyEvaluation?: (boolean|null);

Event firewallPolicyEvaluation

### fraudPrevention
    
    
    fraudPrevention?: (google.cloud.recaptchaenterprise.v1.Event.FraudPrevention|keyof typeof google.cloud.recaptchaenterprise.v1.Event.FraudPrevention|null);

Event fraudPrevention

### hashedAccountId
    
    
    hashedAccountId?: (Uint8Array|Buffer|string|null);

Event hashedAccountId

### headers
    
    
    headers?: (string[]|null);

Event headers

### ja3
    
    
    ja3?: (string|null);

Event ja3

### ja4
    
    
    ja4?: (string|null);

Event ja4

### requestedUri
    
    
    requestedUri?: (string|null);

Event requestedUri

### siteKey
    
    
    siteKey?: (string|null);

Event siteKey

### token
    
    
    token?: (string|null);

Event token

### transactionData
    
    
    transactionData?: (google.cloud.recaptchaenterprise.v1.ITransactionData|null);

Event transactionData

### userAgent
    
    
    userAgent?: (string|null);

Event userAgent

### userInfo
    
    
    userInfo?: (google.cloud.recaptchaenterprise.v1.IUserInfo|null);

Event userInfo

### userIpAddress
    
    
    userIpAddress?: (string|null);

Event userIpAddress

### wafTokenAssessment
    
    
    wafTokenAssessment?: (boolean|null);

Event wafTokenAssessment

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
