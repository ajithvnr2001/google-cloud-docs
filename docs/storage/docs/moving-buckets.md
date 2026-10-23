---
url: https://docs.cloud.google.com/storage/docs/moving-buckets/
title: Move data between buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:09.129897+00:00
---

# Move data between buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/moving-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Move data between buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can copy objects between Cloud Storage buckets when you want to reorganize your storage layout or work around immutable bucket properties. For example, you can copy objects to a new bucket to change a bucket's name or transfer workloads across projects. To complete a move, you copy objects from a source bucket to a destination bucket and then delete the original objects.

If your primary goal is to store data in a different geographic location, consider using [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) instead.

## Overview

When you create a bucket, some of the properties you set are permanent and cannot be changed, including the bucket's name and its parent project.

If you want to use a new name for your bucket, you can _effectively_ do so by [creating a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) with the name you want to use, and then copying your objects from the old bucket to the new bucket. You can then [delete](https://docs.cloud.google.com/storage/docs/deleting-buckets) the old bucket. Note the following:

  * When you delete a bucket, the [bucket's name can be reused](https://docs.cloud.google.com/storage/docs/buckets#considerations).

**Important:** If you create a new bucket with the same name as the original bucket but in a different location, requests made to the new bucket might fail with a `404-Bucket Not Found` error for up to 10 minutes after the deletion of the original bucket. For the [XML API](https://docs.cloud.google.com/storage/docs/xml-api), this behavior includes attempts to create the new bucket.
  * If your primary goal of moving objects from one bucket to another is to store your data in a different [bucket location](https://docs.cloud.google.com/storage/docs/locations), we recommend [directly relocating your bucket](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).

  * Moving data between locations incurs [network usage costs](https://docs.cloud.google.com/storage/pricing#network-buckets). In addition, moving data might incur additional charges, depending on the storage classes of the source data and on the location of the destination bucket. For more information, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).




## Required permissions

### Console

In order to complete this guide using the [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console), you must have the proper IAM permissions. If the buckets you want to access exist in a project that you did not create, you might need the project owner to give you a role that contains the necessary permissions.

For a list of permissions required for specific actions, see [IAM permissions for the Google Cloud console](https://docs.cloud.google.com/storage/docs/access-control/iam-console).

For a list of relevant roles, see [Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). Alternatively, you can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that has specific, limited permissions.

### Command line

In order to complete this guide using a command-line utility, you must have the proper IAM permissions. If the buckets you want to access exist in a project that you did not create, you might need the project owner to give you a role that contains the necessary permissions.

For a list of permissions required for specific actions, see [IAM permissions for `gcloud storage` commands](https://docs.cloud.google.com/storage/docs/access-control/iam-gcloud).

For a list of relevant roles, see [Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). Alternatively, you can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that has specific, limited permissions.

### REST APIs

### JSON API

In order to complete this guide using the [JSON API](https://docs.cloud.google.com/storage/docs/json_api), you must have the proper IAM permissions. If the buckets you want to access exist in a project that you did not create, you might need the project owner to give you a role that contains the necessary permissions.

For a list of permissions required for specific actions, see [IAM permissions for JSON methods](https://docs.cloud.google.com/storage/docs/access-control/iam-json).

For a list of relevant roles, see [Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). Alternatively, you can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that has specific, limited permissions.

## Move data from one bucket to another

### Console

Use the [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer) from within Google Cloud console:

  1. If you don't have a destination bucket yet, [create the bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Open the Transfer page in the Google Cloud console.

[Open the **Transfer** page](https://console.cloud.google.com/transfer/jobs)

  3. Click **Create transfer job**.
  4. Follow the step-by-step walkthrough, clicking **Next step** as you complete each step:

     * Choose a source: Use **Google Cloud Storage bucket** as your source type, and either enter the name of the wanted bucket directly, or click **Browse** to find and select the bucket you want.

     * Choose a destination: Either enter the name of the wanted bucket directly, or click **Browse** to find and select the bucket you want.

     * Choose settings: Select the option **Delete files from source after they're transferred**.

     * Scheduling options: You can ignore this section.

  5. After you complete the step-by-step walkthrough, click **Create**.

This begins the process of copying objects from your old bucket into your new one. This process may take some time; however, after you click **Create** , you can navigate away from the Google Cloud console.

To view the transfer's progress: 

Open the Transfer page in the Google Cloud console.

[Open the **Transfer** page](https://console.cloud.google.com/transfer/jobs)

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

  6. Once the transfer completes, you don't need to do anything to delete the objects from your old bucket if you selected the **Delete source objects after the transfer completes** checkbox during setup. You may, however, want to also [delete your old bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets), which you must do separately.




### Command line

  1. If you don't have one yet, [create a destination bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. To recursively copy the contents of your source bucket to your destination bucket, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with the `--recursive` option:
         
         gcloud storage cp --recursive gs://SOURCE_BUCKET/* gs://DESTINATION_BUCKET

Where:

     * `SOURCE_BUCKET` is the name of your original bucket. For example, `old-bucket`.

     * `DESTINATION_BUCKET` is the name of the bucket you are moving your data to. For example, `my-bucket`.

If your bucket uses [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) and a [flat namespace](https://docs.cloud.google.com/storage/docs/objects#namespace), you must include the flag `--include-managed-folders` in the command for the managed folders to be copied.

  3. To recursively delete the contents from the source bucket, along with the source bucket itself, use the [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) command with the `--recursive` option:
         
         gcloud storage rm --recursive gs://SOURCE_BUCKET

Where `SOURCE_BUCKET` is the name of your original bucket. For example, `old-bucket`.

Alternatively, to delete the contents from the source bucket without deleting the source bucket itself, use the `gcloud storage rm` command with the `--all-versions` flag and `**` wildcard:
         
         gcloud storage rm --all-versions gs://SOURCE_BUCKET/**

Where `SOURCE_BUCKET` is the name of your original bucket. For example, `old-bucket`.




### REST APIs

### JSON API

  1. If you don't have a destination bucket yet, [create the bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. [Copy each object](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects#copy) from your source bucket to the destination bucket.

  3. [Delete each object](https://docs.cloud.google.com/storage/docs/deleting-objects) in your source bucket.

  4. [Delete your source bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).




### XML API

  1. If you don't have a destination bucket yet, [create the bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. [Copy each object](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects#copy) from your source bucket to the destination bucket.

  3. [Delete each object](https://docs.cloud.google.com/storage/docs/deleting-objects) in your source bucket.

  4. [Delete your source bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).




## What's next

  * [Copy, rename, or move individual objects](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects).

  * Learn about [available bucket locations](https://docs.cloud.google.com/storage/docs/locations) and [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#considerations).

  * Learn more about [creating and managing data transfers with the Google Cloud console](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-console#configure).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
