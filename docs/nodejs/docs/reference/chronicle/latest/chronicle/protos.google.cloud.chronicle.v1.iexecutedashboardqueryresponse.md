---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse
title: Interface protos.google.cloud.chronicle.v1.IExecuteDashboardQueryResponse (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:57.891819+00:00
---

# Interface protos.google.cloud.chronicle.v1.IExecuteDashboardQueryResponse (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.chronicle.v1.IExecuteDashboardQueryResponse (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Properties of an ExecuteDashboardQueryResponse.

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Properties 

### dataSources
    
    
    dataSources?: (google.cloud.chronicle.v1.DataSource[]|null);

ExecuteDashboardQueryResponse dataSources

### languageFeatures
    
    
    languageFeatures?: (google.cloud.chronicle.v1.LanguageFeature[]|null);

ExecuteDashboardQueryResponse languageFeatures

### lastBackendCacheRefreshedTime
    
    
    lastBackendCacheRefreshedTime?: (google.protobuf.ITimestamp|null);

ExecuteDashboardQueryResponse lastBackendCacheRefreshedTime

### queryRuntimeErrors
    
    
    queryRuntimeErrors?: (google.cloud.chronicle.v1.IQueryRuntimeError[]|null);

ExecuteDashboardQueryResponse queryRuntimeErrors

### results
    
    
    results?: (google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.IColumnData[]|null);

ExecuteDashboardQueryResponse results

### timeWindow
    
    
    timeWindow?: (google.type.IInterval|null);

ExecuteDashboardQueryResponse timeWindow

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
