---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/map-s3-commands/
title: S3cmd and gdcloud CLI storage commands \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:49.391598+00:00
---

# S3cmd and gdcloud CLI storage commands  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/map-s3-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  S3cmd and gdcloud CLI storage commands Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you the mapping of s3cmd commands to their gdcloud CLI equivalent. See the following table:

**s3cmd command** | **gdcloud command**  
---|---  
s3cmd put LOCAL_PATH s3://REMOTE_PATH  | gdcloud storage cp LOCAL_PATH s3://REMOTE_PATH   
s3cmd cp s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH  | gdcloud storage cp s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH   
s3cmd mv s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH  | gdcloud storage mv s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH   
s3cmd put FILE [FILE...] s3://BUCKET[/PREFIX]  | gdcloud storage cp FILE [FILE...] s3://BUCKET[/PREFIX]   
s3cmd get s3://BUCKET/OBJECT LOCAL_FILE_TO_SAVE  | gdcloud storage cp s3://BUCKET/OBJECT LOCAL_FILE_TO_SAVE   
s3cmd ls s3://FULLY_QUALIFIED_BUCKET_NAME  | gdcloud storage ls s3://FULLY_QUALIFIED_BUCKET_NAME   
s3cmd ls s3://FULLY_QUALIFIED_BUCKET_NAME/<Prefix>/  | s3cmd ls s3://FULLY_QUALIFIED_BUCKET_NAME/<Prefix>/   
s3cmd put FILE [FILE...] s3://BUCKET[/PREFIX]  | s3cmd cp FILE [FILE...] s3://BUCKET[/PREFIX]   
s3cmd modify s3://BUCKET1/OBJECT  | Note that the following command is not supported at this time: gdcloud storage objects update s3://BUCKET1/OBJECT --custom-metadata=Key1=Value1   
s3cmd mv s3://BUCKET1/OBJECT1 s3://BUCKET2[/OBJECT2]  |  gdcloud storage mv s3://BUCKET1/OBJECT1 s3://BUCKET2[/OBJECT2].  Note that the following flags are not supported at this time:  \--disable-multipart  \--multipart-chunk-size-mb=SIZE   
s3cmd del s3://BUCKET/OBJECT  | gdcloud storage rm s3://BUCKET/OBJECT   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
