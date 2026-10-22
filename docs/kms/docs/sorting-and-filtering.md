---
url: https://docs.cloud.google.com/kms/docs/sorting-and-filtering/
title: Sorting and filtering list results \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:47.657924+00:00
---

# Sorting and filtering list results  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/sorting-and-filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Sorting and filtering list results Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Key Management Service supports filtering and sorting results from the following `list` operations.

  * [keyRings.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list)
  * [cryptoKeys.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list)
  * [cryptoKeyVersions.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list)
  * [importJobs.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list)



Support for sorting and filtering in a `list` operation is indicated by the presence of `filter` and `orderBy` string fields in the list request body. Both fields use a simple language for referring to the fields in the object that is being sorted and/or filtered.

## Filter syntax

The filter syntax consists of an expression on one or more fields of the objects being filtered.

You can use the following expression operators.

Operator | Description  
---|---  
`=` | Equality.  
`>` | Greater than.  
`<` | Less than.  
`=>` | Greater than or equal to.  
`<=` | Less than or equal to.  
`!=`  
`-`  
`NOT` | Inequality.  
The following are equivalent:  
`name != "quickstart"`  
`-name="quickstart"`  
`NOT name = "quickstart"`  
`:` | Containment. This is a case-insensitive substring match.  
As an example, `name: "cloud"` filters on resources that contain `cloud` (case-insensitive) in the resource name.  
`AND` | Logical AND. A space is equivalent to `AND`, so the following are equivalent:  
`name: "cloud" AND name: "kms"`  
`name: "cloud" name: "kms"`  
`OR` | Logical OR.  
  
`AND` and `OR` operators are accepted at the same grouping level. `OR` takes precedence over `AND`. You can use parentheses to override default precedence.

When filtering on `time` values, encode the time as a string in the [RFC 3399](https://tools.ietf.org/html/rfc3339) format, such as `2019-06-20T01:30:15Z`.

When accessing a subfield, use dot syntax. For example, the [`CryptoKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) resource contains the `primary` field. You can filter `CryptoKey` results on the subfield `primary.algorithm` for a specific algorithm:
    
    
    primary.algorithm=RSA_SIGN_PSS_2048_SHA256
    

Use the dot syntax for a [label](https://docs.cloud.google.com/kms/docs/creating-managing-labels), and any other `map` type:
    
    
    labels.team=alpha
    

A quoted string is interpreted as a single value rather than a sequence of values.

## Filterable fields

You can filter on any field in the objects being returned.

List method | Link to filterable fields  
---|---  
[keyRings.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list) | [KeyRing fields](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing.FIELDS)  
[cryptoKeys.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list) | [CryptoKey fields](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS)  
[cryptoKeyVersions.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list) | [CryptoKeyVersion fields](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS)  
[importJobs.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list) | [ImportJob fields](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob.FIELDS)  
  
## Sort-order syntax

You can sort results by the resource's `name` field on the objects. The following shows the supported sort-order values for the `orderBy` field.

Value | Description  
---|---  
`''` (empty string) | Results are sorted in the default order.  
`'name'` | Results are sorted in ascending order by the resource's `name` field.  
`'name desc'` | Results are sorted in descending order by the resource's `name` field.  
**Note:** To find the primary key version, do not attempt to sort for the version with the newest creation date. There is no guarantee that the primary version is the newest version or that the newest version is the primary version. Instead, query using the [`primary` field](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS).**Note:** If you sort `CryptoKeyVersion` resources by `name`, they are sorted numerically by the version number.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
