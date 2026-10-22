---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/upload-download-storage-objects/
title: Upload and download storage objects \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:10.806503+00:00
---

# Upload and download storage objects  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/upload-download-storage-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Upload and download storage objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to upload and download objects to and from Google Distributed Cloud (GDC) air-gapped appliance storage buckets.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

## Object naming guidelines

Use the following guidelines to name objects:

  * Use UTF-8 characters when naming objects.
  * Refrain from including any personally identifiable information (PII).



## Upload objects to storage buckets

To upload an object, run the following commands:
    
    
    gdcloud storage cp LOCAL_PATH s3://REMOTE_PATH
    gdcloud storage cp s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH
    gdcloud storage mv s3://REMOTE_SOURCE_PATH s3://REMOTE_MOVE_DESTINATION_PATH
    

The following command uploads all text files from the local directory to a bucket:
    
    
    gdcloud storage cp *.txt s3://BUCKET
    

The following command uploads multiple files from the local directory to a bucket:
    
    
    gdcloud storage cp abc1.txt abc2.txt s3://BUCKET
    

To upload a folder to a bucket, use the --recursive option to copy an entire directory tree. The following command uploads the directory tree dir:
    
    
    gdcloud storage cp dir s3://BUCKET --recursive
    

Perform multipart uploads for large objects, or use multipart uploads automatically when you have a file to upload that is larger than 15 MB. In that case, the file splits into multiple parts, with each part being 15 MB in size. The last part is smaller. Each part uploads separately and reconstructs at the destination when the transfer completes.

If an upload of one part fails, you can restart the upload without affecting any of the other parts already uploaded.

There are two options related to multipart uploads:

  * `--disable-multipart`: disables multipart uploads for all files.
  * `--multipart-chunk-size-mb=SIZE`: sets the size of each chunk of a multipart upload.



Files bigger than SIZE automatically upload as multithreaded-multipart. Smaller files upload using the traditional method. SIZE is in megabytes. The default chunk size is 15 MB. The minimum allowed chunk size is 5 MB, and the maximum is 5 GB.

## Download objects from storage buckets

To get objects from the bucket:
    
    
    gdcloud storage cp s3://BUCKET/OBJECT LOCAL_FILE_TO_SAVE
    

To download all text files from a bucket to your current directory:
    
    
    gdcloud storage cp s3://BUCKET/*.txt .
    

To download the text file `abc.txt` from a bucket to your current directory:
    
    
    gdcloud storage cp s3://BUCKET/abc.txt .
    

To download an older version of the file, list all versions of the file first:
    
    
    gdcloud storage ls s3://BUCKET/abc.txt --all-versions
    

Example output:
    
    
    s3://my-bucket/abc.txt#OEQxNTk4MUEtMzEzRS0xMUVFLTk2N0UtQkM4MjAwQkJENjND
    s3://my-bucket/abc.txt#ODgzNEYzQ0MtMzEzRS0xMUVFLTk2NEItMjI1MTAwQkJENjND
    s3://my-bucket/abc.txt#ODNCNDEzNzgtMzEzRS0xMUVFLTlDOUMtQzRDOTAwQjg3RTg3
    

Then, download a specific version of the text file `abc.txt` from the bucket to your current directory:
    
    
    gdcloud storage cp s3://BUCKET/abc.txt#OEQxNTk4MUEtMzEzRS0xMUVFLTk2N0UtQkM4MjAwQkJENjND .
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
