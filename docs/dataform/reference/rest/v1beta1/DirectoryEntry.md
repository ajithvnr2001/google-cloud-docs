---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DirectoryEntry/
title: DirectoryEntry \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:11:06.800993+00:00
---

# DirectoryEntry  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DirectoryEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  DirectoryEntry Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FilesystemEntryMetadata
    * JSON representation



Represents a single entry in a directory.

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([FilesystemEntryMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DirectoryEntry#FilesystemEntryMetadata))
      },
    
      // Union field entry can be only one of the following:
      "file": string,
      "directory": string
      // End of list of possible types for union field entry.
    }  
  
Fields  
---  
`metadata` |  `object (`[FilesystemEntryMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DirectoryEntry#FilesystemEntryMetadata)`)` Entry with metadata.  
Union field `entry`. The entry's contents. `entry` can be only one of the following:  
`file` |  `string` A file in the directory. The path is returned including the full folder structure from the root.  
`directory` |  `string` A child directory in the directory. The path is returned including the full folder structure from the root.  
  
## FilesystemEntryMetadata

Represents metadata for a single entry in a filesystem.

JSON representation  
---  
      
    
    {
      "sizeBytes": string,
      "updateTime": string
    }  
  
Fields  
---  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Provides the size of the entry in bytes. For directories, this will be 0.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Represents the time of the last modification of the entry.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
