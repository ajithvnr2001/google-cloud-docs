---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ifilter
title: Interface protos.google.cloud.billing.budgets.v1beta1.IFilter (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:37:09.082742+00:00
---

# Interface protos.google.cloud.billing.budgets.v1beta1.IFilter (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ifilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.billing.budgets.v1beta1.IFilter (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  4.2.2  4.1.2  3.3.0  3.2.8 

Properties of a Filter.

## Package

[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)

## Properties 

### calendarPeriod
    
    
    calendarPeriod?: (google.cloud.billing.budgets.v1beta1.CalendarPeriod|keyof typeof google.cloud.billing.budgets.v1beta1.CalendarPeriod|null);

Filter calendarPeriod

### creditTypes
    
    
    creditTypes?: (string[]|null);

Filter creditTypes

### creditTypesTreatment
    
    
    creditTypesTreatment?: (google.cloud.billing.budgets.v1beta1.Filter.CreditTypesTreatment|keyof typeof google.cloud.billing.budgets.v1beta1.Filter.CreditTypesTreatment|null);

Filter creditTypesTreatment

### customPeriod
    
    
    customPeriod?: (google.cloud.billing.budgets.v1beta1.ICustomPeriod|null);

Filter customPeriod

### labels
    
    
    labels?: ({ [k: string]: google.protobuf.IListValue }|null);

Filter labels

### projects
    
    
    projects?: (string[]|null);

Filter projects

### resourceAncestors
    
    
    resourceAncestors?: (string[]|null);

Filter resourceAncestors

### services
    
    
    services?: (string[]|null);

Filter services

### subaccounts
    
    
    subaccounts?: (string[]|null);

Filter subaccounts

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
