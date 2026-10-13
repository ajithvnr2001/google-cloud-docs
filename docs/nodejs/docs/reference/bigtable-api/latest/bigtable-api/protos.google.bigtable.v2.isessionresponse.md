---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.isessionresponse
title: Interface protos.google.bigtable.v2.ISessionResponse (0.9.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:31.806585+00:00
---

# Interface protos.google.bigtable.v2.ISessionResponse (0.9.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.isessionresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.bigtable.v2.ISessionResponse (0.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.0 (latest)  0.8.0  0.2.0 

Properties of a SessionResponse.

## Package

[@google-cloud/bigtable-api](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)

## Properties 

### error
    
    
    error?: (google.bigtable.v2.IErrorResponse|null);

SessionResponse error

### goAway
    
    
    goAway?: (google.bigtable.v2.IGoAwayResponse|null);

SessionResponse goAway

### heartbeat
    
    
    heartbeat?: (google.bigtable.v2.IHeartbeatResponse|null);

SessionResponse heartbeat

### openSession
    
    
    openSession?: (google.bigtable.v2.IOpenSessionResponse|null);

SessionResponse openSession

### sessionParameters
    
    
    sessionParameters?: (google.bigtable.v2.ISessionParametersResponse|null);

SessionResponse sessionParameters

### sessionRefreshConfig
    
    
    sessionRefreshConfig?: (google.bigtable.v2.ISessionRefreshConfig|null);

SessionResponse sessionRefreshConfig

### virtualRpc
    
    
    virtualRpc?: (google.bigtable.v2.IVirtualRpcResponse|null);

SessionResponse virtualRpc

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
