---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/Partition/
title: Partition \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:10.324102+00:00
---

# Partition  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/Partition/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  Partition Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Information about a Hive partition.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ],
      "createTime": string,
      "storageDescriptor": {
        object ([StorageDescriptor](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#StorageDescriptor))
      },
      "parameters": {
        string: string,
        ...
      },
      "fields": [
        {
          object ([FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Required. Represents the values of the partition keys, where each value corresponds to a specific partition key in the order in which the keys are defined. Each value is limited to 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the partition.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storageDescriptor` |  `object (`[StorageDescriptor](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#StorageDescriptor)`)` Optional. Contains information about the physical storage of the data in the partition.  
`parameters` |  `map (key: string, value: string)` Optional. Additional parameters or metadata associated with the partition. Maximum size 10 KiB.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fields[]` |  `object (`[FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema)`)` Optional. List of columns.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
