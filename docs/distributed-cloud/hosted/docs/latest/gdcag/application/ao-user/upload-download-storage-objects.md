---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects/
title: Upload and download storage objects in projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:27.476139+00:00
---

# Upload and download storage objects in projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Upload and download storage objects in projects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to upload and download objects to and from Google Distributed Cloud (GDC) air-gapped storage buckets.

## Before you begin

Storage buckets are resources scoped to a specific [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management). The project acts as a container, grouping your buckets and enabling their management through the Management API server. Before you can perform the operations on this page, you must either create a new project or select an existing one where you have sufficient permissions.

### Required IAM roles

Contact your IAM Project Admin to request the following roles in your project namespace:

  * **Project Bucket Admin** (`project-bucket-admin`): create, update, and delete storage buckets.
  * **Project Bucket Object Viewer** (`project-bucket-object-viewer`): view and check details of storage buckets and objects.



For more information, see [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/grant-obtain-storage-access#grant_bucket_access).

### Prepare your environment

To run commands against the management API server or the global API server, do the following:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the zonal management API server if you don't have one.
  2. For dual-zone buckets, do the following: 
     * Verify with your Infrastructure Operator (IO) that the `BucketLocationConfig` custom resource has been created for your paired zones.
     * [Generate the kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#global-resources-kubeconfig) for the global API server.



## Object naming guidelines

Use the following guidelines to name objects:

  * Use UTF-8 characters when naming objects.
  * Be between 1-55 characters long.
  * Refrain from including any personally identifiable information (PII).



## Upload objects to storage buckets

###  Console 

  1. In the navigation menu, click **Object Storage**.
  2. Click the name of the bucket you want to upload the object to.
  3. Optional: If you want to create a folder to store your object, click **Create folder** > enter a folder name > click **Create**.
  4. Click **Upload file** directly, or navigate into the folder you just created and then click **Upload file**.
  5. Select the desired file and click **Open**.
  6. Wait for the confirmation message that the upload was successful.



###  gdcloud 

To upload an object, run the following commands:
    
    
    gdcloud storage cp LOCAL_PATH s3://REMOTE_PATH
    gdcloud storage cp s3://FULLY_QUALIFIED_SOURCE_BUCKET_NAME s3://FULLY_QUALIFIED_DESTINATION_BUCKET_NAME
    gdcloud storage mv s3://FULLY_QUALIFIED_SOURCE_BUCKET_NAME s3://FULLY_QUALIFIED_DESTINATION_BUCKET_NAME
    

The following commands require the FULLY_QUALIFIED_BUCKET_NAME. Use the `GET` or `DESCRIBE` command from the [View bucket configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-view-storage-buckets#view_bucket_configurations) section to get the fully qualified bucket name.

The following command uploads all text files from the local directory to a bucket:
    
    
    gdcloud storage cp *.txt s3://FULLY_QUALIFIED_BUCKET_NAME
    

The following command uploads multiple files from the local directory to a bucket:
    
    
    gdcloud storage cp abc1.txt abc2.txt s3://FULLY_QUALIFIED_BUCKET_NAME
    

To upload a folder to a bucket, use the --recursive option to copy an entire directory tree. The following command uploads the directory tree dir:
    
    
    gdcloud storage cp DIRECTORY_NAME s3://FULLY_QUALIFIED_BUCKET_NAME --recursive
    

Perform multipart uploads for large objects, or use multipart uploads automatically when you have a file to upload that is larger than 15 MB. In that case, the file splits into multiple parts, with each part being 15 MB in size. The last part is smaller. Each part uploads separately and reconstructs at the destination when the transfer completes.

If an upload of one part fails, you can restart the upload without affecting any of the other parts already uploaded.

There are two options related to multipart uploads:

  * `--disable-multipart`: disables multipart uploads for all files.
  * `--multipart-chunk-size-mb=SIZE`: sets the size of each chunk of a multipart upload.



Files bigger than SIZE automatically upload as multithreaded-multipart. Smaller files upload using the traditional method. SIZE is in megabytes. The default chunk size is 15 MB. The minimum allowed chunk size is 5 MB, and the maximum is 5 GB.

## Download objects from storage buckets

###  Console 

  1. In the navigation menu, click **Object Storage**.
  2. Click the name of the bucket containing the objects.
  3. Select the checkbox next to the name of the object to download.
  4. Click **Download**.



###  gdcloud 

To get objects from the bucket:
    
    
    gdcloud storage cp s3://FULLY_QUALIFIED_BUCKET_NAME/OBJECT LOCAL_FILE_TO_SAVE
    

To download all text files from a bucket to your current directory:
    
    
    gdcloud storage cp s3://FULLY_QUALIFIED_BUCKET_NAME/*.txt .
    

To download the text file `abc.txt` from a bucket to your current directory:
    
    
    gdcloud storage cp s3://FULLY_QUALIFIED_BUCKET_NAME/abc.txt .
    

To download an older version of the file, list all versions of the file first:
    
    
    gdcloud storage ls s3://FULLY_QUALIFIED_BUCKET_NAME/abc.txt --all-versions
    

Example output:
    
    
    s3://my-bucket/abc.txt#OEQxNTk4MUEtMzEzRS0xMUVFLTk2N0UtQkM4MjAwQkJENjND
    s3://my-bucket/abc.txt#ODgzNEYzQ0MtMzEzRS0xMUVFLTk2NEItMjI1MTAwQkJENjND
    s3://my-bucket/abc.txt#ODNCNDEzNzgtMzEzRS0xMUVFLTlDOUMtQzRDOTAwQjg3RTg3
    

Then, download a specific version of the text file `abc.txt` from the bucket to your current directory:
    
    
    gdcloud storage cp s3://FULLY_QUALIFIED_BUCKET_NAME/abc.txt#OEQxNTk4MUEtMzEzRS0xMUVFLTk2N0UtQkM4MjAwQkJENjND .
    

## Use custom AEADKey

For greater customization, you can create your own AEADKey and use it directly when encrypting objects in your bucket. This gives you full control over the encryption key, bypassing the default. Follow [Create a key](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#create) to create a new AEADKey and make sure it's in the same `Namespace` as the bucket you intend to use. Then, whenever sending the request, make sure the `HEADER` is configured with `x-amz-server-side-encryption: SSE-KMS` and `x-amz-server-side-encryption-aws-kms-key-id: NAMESPACE_NAME/AEADKey_NAME`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
