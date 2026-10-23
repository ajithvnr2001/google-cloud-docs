---
url: https://docs.cloud.google.com/tpu/docs/storage-buckets-compute/
title: Connect TPU VMs to Cloud Storage buckets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.632699+00:00
---

# Connect TPU VMs to Cloud Storage buckets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/storage-buckets-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect TPU VMs to Cloud Storage buckets

This page introduces [Cloud Storage](https://docs.cloud.google.com/storage/docs) as an option for storing your machine learning data and training output, and describes how to give your TPU VM access to the data objects on Cloud Storage.

## Before you begin

You need a service account attached to your TPU VM in order to access a Cloud Storage bucket. If you don't specify a service account when creating a TPU VM, it uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

**Note:** Once you set up a service account for your project, it stays set while the project is active; you don't have to set up the service account every time you run a training workload in the same project.

To setup a Google Cloud project for TPUs and create a TPU VM instance, follow the instructions in:

  1. [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).
  2. [Create a TPU VM instance using Compute Engine](https://docs.cloud.google.com/tpu/docs/create-instance-compute)



## Write data to Cloud Storage

**Note:** Set up the Cloud Storage bucket in the same location (region) that you set up the TPU VM. See [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) for all options available for managing storage buckets.

###  Console 

  1. Go to the Cloud Storage page on the Google Cloud console.

[Go to the Cloud Storage page](https://console.cloud.google.com/storage/browser)

  2. Create a new bucket, specifying the following options:

     * A unique name of your choosing.
     * Default storage class: `Standard`
     * Location: The region where you created the TPU VM. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).



###  CLI 

  1. Use the `gcloud storage buckets create` command to create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://BUCKET_NAME --location REGION
         

Replace the following placeholders:

     * BUCKET_NAME is the name of the bucket you want to create.
     * REGION is the region where you created the TPU VM. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
  2. Use the `gcloud storage cp` command to write files to the Cloud Storage bucket:
         
         gcloud storage cp -r LOCAL_DATA_DIR gs://BUCKET_NAME
         

Replace the following placeholders:

     * LOCAL_DATA_DIR is a local path to your data. For example: $HOME/your-data
     * BUCKET_NAME is the name of the bucket you want to write to.



## Give your TPU VM access to Cloud Storage

You need to give your TPU VM read and write access to your Cloud Storage objects. To do that, you must grant the required access to the service account attached to your TPU VM. The following sections show how to find the attached service account and grant the necessary access.

### Authorize the attached service account

The recommended way to authorize the attached service account is by using fine-grained access control lists (ACLs). You can also grant broader permissions using IAM permissions.

#### Using fine-grained ACLs for TPU VM (Recommended)

If you store training data on Cloud Storage, the attached service account needs read and write permission on the bucket.

###  Console 

  1. Go to the Cloud Storage browser page to view the buckets you own.

[Go to the Cloud Storage browser](https://console.cloud.google.com/storage/browser)

  2. Select the bucket whose ACL you want to modify.

  3. Select the **Permissions** tab.

  4. Select **Grant access** to add a new permission and type the complete service account name in the **New principals** edit box.

  5. If you are _reading_ from this bucket, you must authorize the attached service account to read from the resource. Do this by granting the service account the `Storage Legacy > Storage Legacy Bucket Reader` role.

  6. If you are _writing_ to this bucket, you must authorize the attached service account to write to the resource. Do this by granting the service account the `Storage Legacy > Storage Legacy Bucket Writer` role.




###  CLI 

  1. If you are _reading_ from this bucket, grant read permission for the attached service account:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=serviceAccount:SERVICE_ACCOUNT --role=roles/storage.objectViewer
         

Replace the following placeholders:

     * BUCKET_NAME is the name of the bucket you want to read from.
     * SERVICE_ACCOUNT is the name of the service account attached to your TPU VM.
  2. If you are _writing_ to this bucket, grant write permission for the attached service account:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=serviceAccount:SERVICE_ACCOUNT --role=roles/storage.objectCreator
         

Replace the following placeholders:

     * BUCKET_NAME is the name of the bucket you want to write to.
     * SERVICE_ACCOUNT is the name of the service account attached to your TPU VM.



#### Using IAM permissions for TPU VM (Alternative)

If you want to grant broader permissions instead of granting access to each bucket explicitly, you can grant the Identity Access Management (IAM) Storage Admin role to the service account attached to your TPU VM.

  1. [Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Grant access** button to add principals to the project.

  3. Enter the name of the attached service account in the **Principals** field.

  4. Click the **Roles** drop-down list.

  5. Enable the following roles:

     * **Project > Viewer**

     * **Storage > Storage Admin**




### Cloud Storage FUSE

Cloud Storage FUSE lets you mount and access Cloud Storage buckets as local file systems. This lets applications read and write objects in your bucket using standard file system semantics.

See the [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse) for details about how Cloud Storage FUSE works and a description of how Cloud Storage FUSE operations map to Cloud Storage operations. You can find additional information about how to use Cloud Storage FUSE, such as how to install the `gcsfuse` CLI and mounting buckets on [GitHub.](https://github.com/GoogleCloudPlatform/gcsfuse/tree/master/docs)

## Clean up

  1. Disconnect from the TPU VM, if you have not already done so:
         
         exit
         

  2. In your Cloud Shell or terminal, delete the TPU VM:
         
         gcloud compute instances delete TPU_NAME --zone=ZONE
         

Replace the following placeholders:

     * TPU_NAME: The name of the TPU VM you created.
     * ZONE: The zone where the TPU VM was created.
  3. Verify the VM has been deleted by running `gcloud compute instances list`. The deletion might take several minutes.
         
         gcloud compute instances list --zone=ZONE
         

Replace ZONE with the zone where the TPU VM was created.

If the response doesn't list your TPU instance, it has been successfully deleted.

  4. Run the following command to delete the Cloud Storage bucket and its contents, replacing BUCKET_NAME with the name of the bucket you created:
         
         gcloud storage rm --recursive gs://BUCKET_NAME
         

Replace the following placeholders:

     * BUCKET_NAME: The name of the bucket you want to delete.



## What's next

  * For more information about creating Cloud Storage buckets and writing data to those buckets, see the [Cloud Storage create buckets documentation](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * For more information about service accounts, see the [authentication overview](https://docs.cloud.google.com/docs/authentication).
  * For more information about storage best practices, see [Storage best practices for AI/ML on TPU VMs](https://docs.cloud.google.com/tpu/docs/storage-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
