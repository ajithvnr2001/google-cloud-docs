---
url: https://docs.cloud.google.com/storage/docs/working-with-big-data/
title: Use Cloud Storage with big data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:24.865521+00:00
---

# Use Cloud Storage with big data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/working-with-big-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use Cloud Storage with big data Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage is a key part of storing and working with Big Data on Google Cloud. For example, you can use Cloud Storage to [load data](https://docs.cloud.google.com/bigquery/loading-data-into-bigquery) into BigQuery, hold staging files and temporary data for [Dataflow](https://docs.cloud.google.com/dataflow/docs/quickstarts) pipelines, and integrate with [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage), so you can run Apache Hadoop or Apache Spark jobs directly on your data in Cloud Storage.

This page describes how to use the [gcloud command-line tool](https://docs.cloud.google.com/sdk/gcloud/reference/storage) to accomplish big data tasks, such as copying large files or copying many files in parallel. For an introduction to gcloud, see the [gcloud quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud).

## Before you begin

To get the most out of the examples shown on this page, you'll need to complete the following (if you haven't yet):

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the gcloud CLI.
  * [Initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI.



## Copying many files to a bucket

The `cp` command efficiently uploads large numbers of files by automatically performing parallel (multi-threaded/multi-processing) copies as needed. To recursively copy subdirectories, use the `--recursive` flag in the command. For example, to copy files including subdirectories from a local directory named `top-level-dir` to a bucket, you can use:
    
    
    gcloud storage cp top-level-dir gs://example-bucket --recursive
    

You can use [wildcards](https://docs.cloud.google.com/storage/docs/wildcards) to match a specific set of names for an operation. For example, to copy only files that start with `image`:
    
    
    gcloud storage cp top-level-dir/subdir/image* gs://example-bucket --recursive
    

You can remove files using the same wildcard:
    
    
    gcloud storage rm gs://example-bucket/top-level-dir/subdir/image*
    

In addition to copying local files to the cloud and vice versa, you can also copy in the cloud, for example:
    
    
    gcloud storage cp gs://example-bucket/top-level-dir/subdir/** gs://example-bucket/top-level-dir/subdir/subdir2
    

`gcloud storage` automatically detects that you're moving multiple files and creates them in a new directory named `subdir2`.

## Synchronizing a local directory

If you want to synchronize a local directory with a bucket or vice versa, you can do that with the [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command. For example, to make `gs://example-bucket` match the contents of the local directory `local-dir` you can use:
    
    
    gcloud storage rsync local-dir gs://example-bucket --recursive
    

If you use the `--delete-unmatched-destination-objects` flag, it signals the command to delete files at the destination (`gs://example-bucket` in the command above) that aren't present at the source (`local-dir`). You can also synchronize between two buckets.

## Copying large files to a bucket

In general, when working with big data, once your data is in the cloud it should stay there. Once your data is in Google Cloud, it's very fast to transfer it to other services in the same location, such as Compute Engine.

To copy a large local file to a bucket, use:
    
    
    gcloud storage cp local-file gs://example-bucket
    

To copy a large file from an existing bucket, use:
    
    
    gcloud storage cp gs://example-source-bucket/file  gs://example-destination-bucket
    

`gcloud storage` takes full advantage of Cloud Storage resumable upload and download features. For large files this is particularly important because the likelihood of a network failure at your ISP increases with the size of the data being transferred. By resuming an upload based on how many bytes the server [actually received](https://docs.cloud.google.com/storage/docs/resumable-uploads), `gcloud storage` avoids unnecessarily resending bytes and ensures that the upload can eventually be completed. The same logic is applied for downloads based on the size of the local file.

## Configuring a bucket

Typical big data tasks where you will want to configure a bucket include when you move data to a different [storage class](https://docs.cloud.google.com/storage/docs/storage-classes), configure [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning), or set up a [lifecycle rule](https://docs.cloud.google.com/storage/docs/lifecycle).

You can list a bucket's configuration details with [`buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe):
    
    
    gcloud storage buckets describe gs://example-bucket
    

In the output, notice the bucket configuration information, most of which is also configurable via `gcloud storage`:

  * [CORS](https://docs.cloud.google.com/storage/docs/cross-origin): controls Cross-Origin-Resource-Sharing settings for a bucket.
  * [Website](https://docs.cloud.google.com/storage/docs/website-configuration): allows objects in the bucket to act as web pages or be used as static assets in a website.
  * [Versioning](https://docs.cloud.google.com/storage/docs/object-versioning): causes deletes on objects in the bucket to create noncurrent versions.
  * [Storage Class](https://docs.cloud.google.com/storage/docs/storage-classes): allows you to set the set storage class during bucket creation.
  * [Lifecycle](https://docs.cloud.google.com/storage/docs/lifecycle): allows periodic operations to run on the bucket - the most common is stale object deletion.



For example, suppose you only want to keep files in a particular bucket around for just one day, then you can set up the lifecycle rule for the bucket with:
    
    
    echo '{ "rule": [{ "action": {"type": "Delete"}, "condition": {"age": 1}}]}' > lifecycle_config.json
    gcloud storage buckets update gs://example-bucket --lifecycle-file=lifecycle_config.json
    

Now, any objects in your bucket older than a day will automatically get deleted from this bucket. You can verify the configuration you just set with the [`buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command (other configuration commands work in a similar fashion):
    
    
    gcloud storage buckets describe gs://example-bucket
    

## Sharing data in a bucket

When working with big data, you will likely work on files collaboratively and you'll need to be able to give access to specific people or groups. Identity and Access Management policies define who can access your files and what they're allowed to do. You can view a bucket's IAM policy using the [`buckets get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy) command:
    
    
    gcloud storage buckets get-iam-policy gs://example-bucket
    

The response to the command shows _principals_ , which are accounts that are granted access to your bucket, and [_roles_](https://docs.cloud.google.com/storage/docs/access-control/iam-roles), which are groups of permissions granted to the principals.

Three common scenarios for sharing data are sharing publicly, sharing with a group, and sharing with a person:

  * **Sharing publicly** : For a bucket whose contents are meant to be listed and read by anyone on the Internet, you can configure the IAM policy using the 'AllUsers' designation:

gcloud storage buckets add-iam-policy-binding gs://example-bucket --member=allUsers --role=roles/storage.objectViewer

  * **Sharing with a group** : For collaborators who do not have access to your other Google Cloud resources, we recommend that you [create a Google group](https://support.google.com/groups/answer/2464926?hl=en) and then add the Google group to the bucket. For example, to give access to the `my-group` Google Group, you can configure the following IAM policy:

gcloud storage buckets add-iam-policy-binding gs://example-bucket --member=group:my-group@googlegroups.com --role=roles/storage.objectViewer

For more information, see [Using a Group to Control Access to Objects](https://docs.cloud.google.com/storage/docs/collaboration#group).

  * **Sharing with one person** : For many collaborators, use a group to give access in bulk. For one person, you can grant read access as follows:

gcloud storage buckets add-iam-policy-binding gs://example-bucket --member=user:jeffersonloveshiking@gmail.com --role=roles/storage.objectViewer




## Cleaning up a bucket

You can clean a bucket quickly with the following command:
    
    
    gcloud storage rm gs://example-bucket/ --recursive
    

## Working with checksums

When performing copies, the `gcloud storage cp` and `gcloud storage rsync` commands validate that the checksum of the source file matches the checksum of the destination file. In the rare event that checksums don't match, `gcloud storage` deletes the invalid copy and prints a warning message. For more information, see [checksum validation](https://docs.cloud.google.com/storage/docs/data-validation).

You can use `gcloud storage` to get the checksum of an object in a bucket. For example, suppose you copy a [Landsat public data](https://docs.cloud.google.com/storage/docs/public-datasets) object to your working bucket with:
    
    
    gcloud storage cp gs://gcp-public-data-landsat/LC08/01/001/003/LC08_L1GT_001003_20140812_20170420_01_T2/LC08_L1GT_001003_20140812_20170420_01_T2_B3.TIF gs://example-bucket
    

Now, you can get the checksums of both the public bucket version of the file and your version of the file in your bucket to ensure they match:
    
    
    gcloud storage objects describe gs://example-bucket/LC08_L1GT_001003_20140812_20170420_01_T2_B3.TIF
    gcloud storage objects describe gs://gcp-public-data-landsat/LC08/01/001/003/LC08_L1GT_001003_20140812_20170420_01_T2/LC08_L1GT_001003_20140812_20170420_01_T2_B3.TIF
    

You can also use `gcloud storage` to calculate the checksum of a local file. For example, suppose your data is in a file at a local data center and you copied it into Cloud Storage. You can use [`gcloud storage hash`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hash) to get the checksum of your local file and then compare that with the checksum of the file you copied to a bucket. To get the checksum of a local file use:
    
    
    gcloud storage hash local-file
    

### MD5 values

For non-composite objects, running `gcloud storage objects describe` on an object in a bucket returns output like the following:
    
    
    bucket: example-bucket
    contentType: text/plain
    crc32c: FTiauw==
    customTime: '1970-01-01T00:00:00+00:00'
    etag: CPjo7ILqxsQCEAE=
    generation: '1629833823159214'
    id: example-bucket/100MBfile.txt/1629833823159214
    kind: storage#object
    md5Hash: daHmCObxxQdY9P7lp9jj0A==
    ...
    

Running `gcloud storage hash` on a local file returns output like the following:
    
    
    ---
    crc32c_hash: IJfuvg==
    digest_format: base64
    md5_hash: +bqpwgYMTRn0kWmp5HXRMw==
    url: file.txt
    

Both outputs have a CRC32c and MD5 value. There is no MD5 value for composite objects, such as those created from [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

## What's next

  * [Find out the total size and number of objects in a bucket](https://docs.cloud.google.com/storage/docs/getting-bucket-size).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
