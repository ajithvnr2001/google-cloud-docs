---
url: https://docs.cloud.google.com/filestore/docs/getting-operation-information/
title: Getting operation information \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:39.047255+00:00
---

# Getting operation information  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/getting-operation-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Getting operation information Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to get status information and other metadata about Filestore operations.

## Before you begin

You can only get operation information using the gcloud CLI. To use the gcloud CLI, you must either [install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads) or use the Cloud Shell that's built into the Google Cloud console:

[Go to the Google Cloud console](https://console.cloud.google.com/)

## Getting information about all operations

You can get a list of Filestore operations by running the [`operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/operations/list) command:
    
    
    gcloud filestore operations list
        --[project=project-id] \
        --[zone=zone]
    

where:

  * project-id is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running:
        
        gcloud config set project project-id
        

  * zone is the zone where the Filestore instance resides. Run the [`gcloud filestore zones list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/zones/list) command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running:
        
        gcloud config set filestore/zone zone
        




The command returns a response similar to the following:
    
    
    OPERATION_NAME                                           LOCATION        TYPE    TARGET   STATUS  CREATE_TIME          DURATION
    operation-1505929956434-559a2a41c217c-231e6a94-a4b6a803  us-central1-c   create  nfs1     DONE    2017-09-20T17:52:36  <1S
    operation-1505931180862-559a2ed176d0d-a0d70ae0-35ef2e71  europe-west1-b  create  nfs2     DONE    2017-09-20T18:13:00  <1S
    

## Getting information about a specific operation

You can get details of a specific Filestore operation by running the [`operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/operations/describe) command:
    
    
    gcloud filestore operations describe operation-name \
        --[project=project-id] \
        --[zone=zone]
    

where:

  * operation-name is the name of the Filestore operation. Use the [`operations list`](https://docs.cloud.google.com/filestore/docs/getting-operation-information#get-all-operations) command to get a list of operation names.
  * project-id is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running:
        
        gcloud config set project project-id
        

  * zone is the zone where the Filestore instance resides. Run the `gcloud filestore zones list` command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running the [`config set filestore/zone`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command:
        
        gcloud config set filestore/zone zone
        




The command returns a response similar to the following:
    
    
    done: true
    metadata:
      '@type': type.googleapis.com/google.cloud.common.OperationMetadata
      apiVersion: v1beta1
      createTime: '2017-10-09T22:18:09.347400Z'
      endTime: '2017-10-09T22:20:04.392199183Z'
      target: projects/filestore-test/locations/us-central1-c/instances/filer3
      verb: delete
    name: projects/filestore-test/locations/us-central1-c/operations/operation-1507587489330-55b2490c4f394-faece090-1c0e16db
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
