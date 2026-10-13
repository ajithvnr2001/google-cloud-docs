---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables/create/
title: Method: projects.instances.tables.create \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:33.602860+00:00
---

# Method: projects.instances.tables.create  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Method: projects.instances.tables.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request.

### HTTP request

`POST https://bigtableadmin.googleapis.com/v2/{parent=projects/*/instances/*}/tables`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The unique name of the instance in which to create the table. Values are of the form `projects/{project}/instances/{instance}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `bigtable.tables.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tableId": string,
      "table": {
        object ([Table](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#Table))
      },
      "initialSplits": [
        {
          object ([Split](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables/create#Split))
        }
      ]
    }  
  
Fields  
---  
`tableId` |  `string` Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.  
`table` |  `object (`[Table](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#Table)`)` Required. The Table to create.  
`initialSplits[]` |  `object (`[Split](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables/create#Split)`)` The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions). Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`.Example:

  * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]`
  * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]`
  * Key assignment: 
    * Tablet 1 `[, apple) => {"a"}.`
    * Tablet 2 `[apple, customer_1) => {"apple", "custom"}.`
    * Tablet 3 `[customer_1, customer_2) => {"customer_1"}.`
    * Tablet 4 `[customer_2, other) => {"customer_2"}.`
    * Tablet 5 `[other, ) => {"other", "zz"}.`

  
  
### Response body

If successful, the response body contains a newly created instance of `[Table](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables#Table)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigtable.admin`
  * `https://www.googleapis.com/auth/bigtable.admin.table`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin.table`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Split

An initial split point for a newly created table.

JSON representation  
---  
      
    
    {
      "key": string
    }  
  
Fields  
---  
`key` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Row key to use as an initial tablet boundary.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-03 UTC."],[],[]] 
