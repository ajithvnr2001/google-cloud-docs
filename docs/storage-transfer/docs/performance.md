---
url: https://docs.cloud.google.com/storage-transfer/docs/performance/
title: Improve transfer speeds \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:10.335776+00:00
---

# Improve transfer speeds  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Improve transfer speeds Stay organized with collections  Save and categorize content based on your preferences. 

Transfer speeds are affected by factors including source location and provider, file sizes, and number of files.

If your transfer is progressing more slowly than expected, refer to the information on this page for possible reasons and resolutions.

## Agentless transfers

For transfers to Cloud Storage from Amazon S3, Microsoft Azure, URL lists, or Cloud Storage, Storage Transfer Service manages the transfer without the need for hosted transfer agents.

### Create multiple parallel transfers

Storage Transfer Service has a maximum number of allowed queries per second (QPS) per transfer job. If your job involves a large number of relatively small files, its transfer speed is limited by this QPS cap. Transferring an object can trigger list, read, and write operations, each of which count against the maximum QPS.

To work around the QPS limit, split your large transfer into multiple transfer jobs. Use [include and exclude prefixes](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) to create transfer jobs containing fewer files. You can create:

  * up to [5000 jobs per day](https://docs.cloud.google.com/storage-transfer/quotas#rate-quotas)
  * with [200 jobs running](https://docs.cloud.google.com/storage-transfer/quotas#transferOperations) at any point in time



For example, to transfer only files whose filename or path begin with the letters `a` through `e`:

###  gcloud CLI 
    
    
    gcloud transfer jobs create SOURCE DESTINATION \
      --include-prefixes="a,b,c,d,e"
    

###  REST 
    
    
    {
        "description": "YOUR DESCRIPTION",
        "status": "ENABLED",
        "projectId": "PROJECT_ID",
        "schedule": {
            "scheduleStartDate": {
                "day": 1,
                "month": 1,
                "year": 2015
            },
            "startTimeOfDay": {
                "hours": 1,
                "minutes": 1
            }
        },
        "transferSpec": {
            "gcsDataSource": {
                "bucketName": "GCS_SOURCE_NAME"
            },
            "gcsDataSink": {
                "bucketName": "GCS_SINK_NAME"
            },
            "transferOptions": {
                "deleteObjectsFromSourceAfterTransfer": true
            },
            "objectConditions": {
                "includePrefixes": [
                    "a","b","c","d","e"
                ],
                "excludePrefixes": [
                    "path_1/subpath_2/object_5"
                ]
            }
        }
    }
    

## Agent-based transfers

For tips on speeding up agent-based transfers, refer to [Best practices for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
