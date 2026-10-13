---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest
title: Interface protos.google.analytics.admin.v1beta.IRunAccessReportRequest (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:48.453766+00:00
---

# Interface protos.google.analytics.admin.v1beta.IRunAccessReportRequest (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.analytics.admin.v1beta.IRunAccessReportRequest (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Properties of a RunAccessReportRequest.

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Properties 

### dateRanges
    
    
    dateRanges?: (google.analytics.admin.v1beta.IAccessDateRange[]|null);

RunAccessReportRequest dateRanges

### dimensionFilter
    
    
    dimensionFilter?: (google.analytics.admin.v1beta.IAccessFilterExpression|null);

RunAccessReportRequest dimensionFilter

### dimensions
    
    
    dimensions?: (google.analytics.admin.v1beta.IAccessDimension[]|null);

RunAccessReportRequest dimensions

### entity
    
    
    entity?: (string|null);

RunAccessReportRequest entity

### expandGroups
    
    
    expandGroups?: (boolean|null);

RunAccessReportRequest expandGroups

### includeAllUsers
    
    
    includeAllUsers?: (boolean|null);

RunAccessReportRequest includeAllUsers

### limit
    
    
    limit?: (number|Long|string|null);

RunAccessReportRequest limit

### metricFilter
    
    
    metricFilter?: (google.analytics.admin.v1beta.IAccessFilterExpression|null);

RunAccessReportRequest metricFilter

### metrics
    
    
    metrics?: (google.analytics.admin.v1beta.IAccessMetric[]|null);

RunAccessReportRequest metrics

### offset
    
    
    offset?: (number|Long|string|null);

RunAccessReportRequest offset

### orderBys
    
    
    orderBys?: (google.analytics.admin.v1beta.IAccessOrderBy[]|null);

RunAccessReportRequest orderBys

### returnEntityQuota
    
    
    returnEntityQuota?: (boolean|null);

RunAccessReportRequest returnEntityQuota

### timeZone
    
    
    timeZone?: (string|null);

RunAccessReportRequest timeZone

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
