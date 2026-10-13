---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.Index.Types.Density
title: Firestore Admin v1 API - Enum Index.Types.Density (3.19.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:15.937202+00:00
---

# Firestore Admin v1 API - Enum Index.Types.Density (3.19.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.Index.Types.Density

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore Admin v1 API - Enum Index.Types.Density (3.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.19.0 (latest)  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum Index.Types.Density

Reference documentation and code samples for the Firestore Admin v1 API enum Index.Types.Density.

The density configuration for the index.

## Namespace

[Google.Cloud.Firestore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1)

## Assembly

Google.Cloud.Firestore.Admin.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`Dense` | An index entry will exist regardless of if the fields are present or not. This is the default density for an Enterprise Edition database. The index will store `unset` values for fields that are not present in the document.  
`SparseAll` | An index entry will only exist if ALL fields are present in the document. This is both the default and only allowed value for Standard Edition databases (for both Cloud Firestore `ANY_API` and Cloud Datastore `DATASTORE_MODE_API`). Take for example the following document:
    
    
    {
      "__name__": "...",
      "a": 1,
      "b": 2,
      "c": 3
    }
    

an index on `(a ASC, b ASC, c ASC, __name__ ASC)` will generate an index entry for this document since `a`, 'b', `c`, and `__name__` are all present but an index of `(a ASC, d ASC, __name__ ASC)` will not generate an index entry for this document since `d` is missing. This means that such indexes can only be used to serve a query when the query has either implicit or explicit requirements that all fields from the index are present.  
`SparseAny` | An index entry will exist if ANY field are present in the document. This is used as the definition of a sparse index for Enterprise Edition databases. Take for example the following document:
    
    
    {
      "__name__": "...",
      "a": 1,
      "b": 2,
      "c": 3
    }
    

an index on `(a ASC, d ASC)` will generate an index entry for this document since `a` is present, and will fill in an `unset` value for `d`. An index on `(d ASC, e ASC)` will not generate any index entry as neither `d` nor `e` are present. An index that contains `__name__` will generate an index entry for all documents since Firestore guarantees that all documents have a `__name__` field.  
`Unspecified` | Unspecified. It will use database default setting. This value is input only.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
