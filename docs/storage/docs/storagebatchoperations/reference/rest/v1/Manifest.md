---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest/
title: Manifest \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:52:59.862478+00:00
---

# Manifest  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Manifest Stay organized with collections  Save and categorize content based on your preferences. 

Describes list of objects to be transformed.

JSON representation  
---  
      
    
    {
      "manifestLocation": string
    }  
  
Fields  
---  
`manifestLocation` |  `string` Required. Specify the manifest file location. The format of manifest location can be an absolute path to the object in the format of `gs://bucketName/path/object_name`. For example, `gs://bucketName/path/object_name.csv`. Alternatively, you can specify an absolute path with a single wildcard character in the file name, for example `gs://bucketName/path/fileName*.csv`. If the manifest location is specified with a wildcard, objects in all manifest files matching the pattern will be acted upon. The manifest is a CSV file, uploaded to Cloud Storage, that contains one object or a list of objects that you want to process. Each row in the manifest must include the `bucket` and `name` of the object. You can optionally specify the `generation` of the object. If you don't specify the `generation`, the current version of the object is used.You can optionally include a header row with the following format: `bucket,name,generation`. For example,
    
    
    bucket,name,generation
    bucket_1,object_1,generation_1
    bucket_1,object_2,generation_2
    bucket_1,object_3,generation_3
    

Note: The manifest file must specify only objects within the bucket provided to the job. Rows referencing objects in other buckets are ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
