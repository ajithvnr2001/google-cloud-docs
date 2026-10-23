---
url: https://docs.cloud.google.com/tpu/docs/storage-buckets/
title: Connecting to Cloud Storage Buckets \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.416444+00:00
---

# Connecting to Cloud Storage Buckets  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting to Cloud Storage Buckets

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This page introduces [Cloud Storage](https://docs.cloud.google.com/storage/docs) as an option for storing your machine learning data and training output, and describes how to give your Cloud TPU access to the data objects on Cloud Storage.

## Before you begin

You need a Cloud TPU [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in order to access a Cloud Storage bucket.

**Note:** Once you set up a service account for your project, it stays set while the project is active; you don't have to set up the service account every time you run a training workload in the same project.

  1. Create a Cloud TPU service account for your project.
         
         gcloud beta services identity create --service tpu.googleapis.com --project project-id

The command returns a Cloud TPU service account with following format:
         
         service-project-number@cloud-tpu.iam.gserviceaccount.com
         

**Important:** This command creates a [service agent](https://docs.cloud.google.com/iam/docs/service-agents), a special type of Google-managed service account which is not listed in your Service accounts page in the Google Cloud console.
  2. Follow the instructions found in either the [Cloud TPU quickstart guides](https://docs.cloud.google.com/tpu/docs/quickstart) or [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm) to configure your Google Cloud project and create your Cloud TPU VM and TPU resources.




## Write data to Cloud Storage

**Note:** Set up the Cloud Storage bucket in the same location (region) that you set up the Cloud TPU. See [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) for all options available for managing storage buckets.

###  Console 

  1. Go to the Cloud Storage page on the Google Cloud console.

[Go to the Cloud Storage page](https://console.cloud.google.com/storage/browser)

  2. Create a new bucket, specifying the following options:

     * A unique name of your choosing.
     * Default storage class: `Standard`
     * Location: The region where you created the Cloud TPU. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).



###  CLI 

  1. Use the `gcloud storage buckets create` command to create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://bucket-name --location region

where:

     * region is the region where you created the Cloud TPU. For more information about regions and TPU availability, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).

     * bucket-name is the name of the bucket you want to create.

  2. Use the `gcloud storage cp` command to write files to the Cloud Storage bucket:
         
         gcloud storage cp -r local-data-dir gs://bucket-name

where local-data-dir is a local path to your data. For example:`$HOME/your-data`




## Give your Cloud TPU access to Cloud Storage

You need to give your Cloud TPU read and write access to your Cloud Storage objects. To do that, you must grant the required access to the Cloud TPU service account used by the Cloud TPU. The following sections show how to find the Cloud TPU service account and grant the necessary access.

### Authorize the Cloud TPU service account

The recommended way to authorize the Cloud TPU service account is by using fine-grained access control lists (ACLs). You can also grant broader permissions using IAM permissions.

#### Using fine-grained ACLs for Cloud TPU (Recommended)

If you store training data on Cloud Storage, the Cloud TPU service account needs read and write permission on the bucket.

###  Console 

  1. Go to the Cloud Storage browser page to view the buckets you own. 

[Go to the Cloud Storage browser](https://console.cloud.google.com/storage/browser)

  2. Select the bucket whose ACL you want to modify.

  3. Select the **Permissions** tab.

  4. Select **Grant access** to add a new permission and type the complete service account name in the **New principals** edit box.

  5. If you are _reading_ from this bucket, you must authorize the TPU Service Account to read from the resource. Do this by granting the Service Account the `Storage Legacy > Storage Legacy Bucket Reader` role.

  6. If you are _writing_ to this bucket, you must authorize the TPU Service Account to write to the resource. Do this by granting the Service Account the `Storage Legacy > Storage Legacy Bucket Writer` role.




###  CLI 

  1. If you are _reading_ from this bucket, grant read permission for the Cloud TPU service account:
         
         gcloud storage buckets add-iam-policy-binding gs://bucket-name --member=serviceAccount:service-account --role=roles/storage.objectViewer
          

  2. If you are _writing_ to this bucket, grant write permission for the Cloud TPU service account:
         
         gcloud storage buckets add-iam-policy-binding gs://bucket-name --member=serviceAccount:service-account --role=roles/storage.objectCreator




#### Using IAM permissions for Cloud TPU (Alternative)

If you want to grant broader permissions instead of granting access to each bucket explicitly, you can grant the Identity Access Management (IAM) Storage Admin role to the Cloud TPU service account.

  1. [Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Grant access** button to add principals to the project.

  3. Enter the names of the Cloud TPU service account in the **Principals** text box.

  4. Click the **Roles** dropdown list.

  5. Enable the following roles:

     * **Project > Viewer**

     * **Storage > Storage Admin**




### Cloud Storage FUSE

Cloud Storage FUSE allows you to mount and access Cloud Storage buckets as local file systems. This allows applications to read and write objects in your bucket using standard file system semantics.

See the [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse) for details about how Cloud Storage FUSE works and a description of how Cloud Storage FUSE operations map to Cloud Storage operations. You can find additional information about how to use Cloud Storage FUSE, such as how to install the gcsfuse CLI and mounting buckets on [GitHub.](https://github.com/GoogleCloudPlatform/gcsfuse/tree/master/docs)

## Clean up

  1. Disconnect from the Cloud TPU, if you have not already done so:
         
         (vm)$ exit

  2. In your Cloud Shell, delete the Cloud TPU: 
         
         gcloud compute tpus tpu-vm delete tpu-name --zone=zone

  3. Verify the VM has been deleted by running `gcloud compute tpus tpu-vm list`. The deletion might take several minutes. 
         
         gcloud compute tpus tpu-vm list --zone=zone

A response like the following indicates your instances have been successfully deleted.
         
         Listed 0 items
         

  4. Run the following command to delete the Cloud Storage bucket and its contents, replacing bucket-name with the name of the bucket you created:
         
         gcloud storage rm --recursive gs://bucket-name




## What's next

  * For more information about creating Cloud Storage buckets and writing data to those buckets, see the [Cloud Storage create buckets documentation](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * For more information about service accounts, see the [authentication overview](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
