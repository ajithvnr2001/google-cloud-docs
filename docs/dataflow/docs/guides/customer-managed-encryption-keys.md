---
url: https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys/
title: Use customer-managed encryption keys \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:20.354500+00:00
---

# Use customer-managed encryption keys  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Dataflow encrypts customer content at rest. Dataflow handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Dataflow. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Dataflow resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

You can create a batch or streaming pipeline that is protected with a CMEK or access CMEK-protected data in sources and sinks.

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Dataflow resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation or update in Dataflow. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

To learn how to use manually-created CMEKs to protect your Dataflow resources, see Create a pipeline protected by Cloud KMS.

To use CMEKs created by Cloud KMS Autokey to protect your Dataflow resources, use the steps provided for Dataflow at [Using Autokey with Dataflow resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#dataflow-autokey) to generate a key, then follow Create a pipeline protected by Cloud KMS.

## Cloud KMS quotas and Dataflow

When you use CMEK in Dataflow, your projects can consume Cloud KMS cryptographic requests quotas. For example, Dataflow pipelines can consume these quotas when your pipeline accesses CMEK-protected data in sources and sinks or when the state of a CMEK-encrypted pipeline is retrieved. For more information, see the Encryption of pipeline state locations section in this page.

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Support and limitations

  * Cloud KMS is supported in the following Apache Beam SDK versions:

    * Java SDK versions 2.13.0 and later
    * Python SDK versions 2.13.0 and later
    * Go SDK versions 2.40.0 and later
  * Cloud KMS with Dataflow supports [regional keys](https://docs.cloud.google.com/kms/docs/locations#location_types). If you [override the worker region or zone of the pipeline](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#workeroverride) to use a region other than the one associated with your keys, regional keys don't work.

  * The region for your CMEK and the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) for your Dataflow job must be the same.

  * Multi-region and global locations are not supported. You can't use global and multi-regional keys with Dataflow pipelines.




## Encryption of pipeline state artifacts

Data that a Dataflow pipeline reads from user-specified data sources is encrypted, except for the data keys that you specify for key-based transforms in streaming jobs.

For batch jobs, all data, including data keys that you specify for key-based transforms, is always protected by CMEK encryption.

For streaming jobs created after March 7, 2024, all user data is encrypted with CMEK.

For streaming jobs created before March 7, 2024, data keys used in key-based operations, such as windowing, grouping, and joining, are not protected by CMEK encryption. To enable this encryption for your jobs, [drain or cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline), and then restart it.

Job metadata is not encrypted with Cloud KMS keys. Job metadata includes the following:

  * User-supplied data, such as Job Names, Job Parameter values, and Pipeline Graph
  * System-generated data, such as Job IDs and IP addresses of workers



## Encryption of pipeline state locations

The following storage locations are protected with Cloud KMS keys:

  * Persistent Disks attached to Dataflow workers and used for Persistent Disk-based shuffle and streaming state storage.
  * Dataflow [Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) state for batch pipelines.
  * Cloud Storage buckets that store temporary export or import data. Dataflow only supports default keys set by the user on the bucket level.
  * Cloud Storage buckets used to store binary files containing pipeline code. Dataflow only supports default keys set by the user on the bucket level.
  * Cloud Storage buckets used to store sampled pipeline data, when [data sampling](https://docs.cloud.google.com/dataflow/docs/guides/data-sampling) is enabled.
  * Dataflow Streaming Engine state for streaming pipelines.



## External keys

You can use [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) to encrypt data within Google Cloud using external keys that you manage.

When you use a Cloud EKM key, Google has no control over the availability of your externally managed key. If the key becomes unavailable during the job or pipeline creation period, your job or pipeline is canceled.

For more considerations when using external keys, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm#considerations).

## Before you begin

  1. Verify that you have the Apache Beam SDK for Java 2.13.0 or later, the Apache Beam SDK for Python 2.13.0 or later, or the Apache Beam SDK for Go 2.40.0 or later.

For more information, see [Installing the Apache Beam SDK](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk).

  2. Decide whether you're going to run Dataflow and Cloud KMS in the same Google Cloud project or in different projects. This page uses the following convention:

     * `PROJECT_ID` is the project ID of the project that is running Dataflow.
     * `PROJECT_NUMBER` is the project number of the project that is running Dataflow.
     * `KMS_PROJECT_ID` is the project ID of the project that is running Cloud KMS.

For information about Google Cloud project IDs and project numbers, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. On the Google Cloud project that you want to run Cloud KMS:

     1. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).
     2. Create a key ring and a key as described in [Creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys). Cloud KMS and Dataflow are both regionalized services. The region for your CMEK and the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) of your Dataflow job must be the same. Don't use global or multi-regional keys with your Dataflow pipelines. Instead, use regional keys.



## Grant Encrypter/Decrypter permissions

**Note:** If you use the Google Cloud console and the **Create job from template** page, a prompt appears to grant the encrypt and decrypt permissions to your Compute Engine service account and Dataflow service account. If you follow that prompt to grant the permissions, you can skip this section, which describes how to manually set these permissions.

  1. Assign the `Cloud KMS CryptoKey Encrypter/Decrypter` [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to the **Dataflow service account**. This permission grants your Dataflow service account the permission to encrypt and decrypt with the CMEK you specify. If you use the Google Cloud console and the **Create job from template** page, this permission is granted automatically and you can skip this step.

Use the Google Cloud CLI to assign the role:
         
         gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
         --member serviceAccount:service-PROJECT_NUMBER@dataflow-service-producer-prod.iam.gserviceaccount.com \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace `KMS_PROJECT_ID` with the ID of your Google Cloud project that is running Cloud KMS, and replace `PROJECT_NUMBER` with the project number (not project ID) of your Google Cloud project that is running the Dataflow resources.

  2. Assign the `Cloud KMS CryptoKey Encrypter/Decrypter` [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to the **Compute Engine service account**. This permission grants your Compute Engine service account the permission to encrypt and decrypt with the CMEK you specify.

Use the Google Cloud CLI to assign the role:
         
         gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
         --member serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace `KMS_PROJECT_ID` with the ID of your Google Cloud project that is running Cloud KMS, and replace `PROJECT_NUMBER` with the project number (not project ID) of your Google Cloud project that is running the Compute Engine resources.




## Create a pipeline protected by Cloud KMS

When you create a batch or streaming pipeline, you can select a Cloud KMS key to encrypt the pipeline state. The pipeline state is the data that is stored by Dataflow in temporary storage.

### Command-line interface

To create a new pipeline with pipeline state that is protected by a Cloud KMS key, add the relevant flag to the pipeline parameters. The following example demonstrates [running a word count pipeline](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python#run-wordcount-on-the-cloud-dataflow-service) with Cloud KMS.

#### Use Autokey

If you haven't already done so, [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

To use Autokey with pipelines created from the command line, follow [Using Autokey with Dataflow resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#dataflow-autokey) to provision a key, then use it in place of `KMS_KEY`.

### Java

Dataflow does not support creating default Cloud Storage paths for temporary files when using a Cloud KMS key. Specifying `gcpTempLocation` is required.
    
    
    mvn compile exec:java -Dexec.mainClass=org.apache.beam.examples.WordCount \
      -Dexec.args="--inputFile=gs://dataflow-samples/shakespeare/kinglear.txt \
                   --output=gs://STORAGE_BUCKET/counts \
                   --runner=DataflowRunner --project=PROJECT_ID \
                   --gcpTempLocation=gs://STORAGE_BUCKET/tmp \
                   --dataflowKmsKey=KMS_KEY"
      -Pdataflow-runner

### Python

Dataflow does not support creating default Cloud Storage paths for temporary files when using a Cloud KMS key. Specifying `gcpTempLocation` is required.
    
    
    python -m apache_beam.examples.wordcount \
      --input gs://dataflow-samples/shakespeare/kinglear.txt \
      --output gs://STORAGE_BUCKET/counts \
      --runner DataflowRunner \
      --region HOST_GCP_REGION \
      --project PROJECT_ID \
      --temp_location gs://STORAGE_BUCKET/tmp/ \
      --dataflow_kms_key=KMS_KEY

### Go

Dataflow does not support creating default Cloud Storage paths for temporary files when using a Cloud KMS key. Specifying `gcpTempLocation` is required.
    
    
    wordcount
      --project HOST_PROJECT_ID \
      --region HOST_GCP_REGION \
      --runner dataflow \
      --staging_location gs://STORAGE_BUCKET/staging \
      --temp_location gs://STORAGE_BUCKET/temp \
      --input gs://dataflow-samples/shakespeare/kinglear.txt \
      --output gs://STORAGE_BUCKET/output \
      --dataflow_kms_key=KMS_KEY

### Google Cloud console

  1. Open the Dataflow monitoring interface.  
[Go to the Dataflow Web Interface](https://console.cloud.google.com/dataflow)
  2. Select **Create job from template**.
  3. In the **Encryption** section, select **Customer-managed key**.

![The encryption options on the Create job from template page to use
              a Google-owned and Google-managed encryption key or customer-managed keys.](https://docs.cloud.google.com/static/dataflow/images/CMEK-warning1.png)**Note:** The drop-down menu **Select a customer-managed key** only shows keys with the regional scope global or the region you selected in the **Regional endpoint** drop-down menu. In order to minimize Cloud KMS operation latency and improve system availability, we recommend choosing regional keys.

The first time you attempt to run a job with a particular Cloud KMS key, your **Compute Engine service account** or **Dataflow service account** might not have been granted the permissions to encrypt and decrypt using that key. In this case, a warning message appears to prompt you to grant the permission to your service account.

![Prompts to grant permissions to encrypt and decrypt on your
              Compute Engine and Dataflow service accounts using a
              particular CMEK.](https://docs.cloud.google.com/static/dataflow/images/CMEK-warning2.png)

## Verify Cloud KMS key usage

You can verify whether your pipeline uses a Cloud KMS key using the Google Cloud console or the Google Cloud CLI.

### Console

  1. Open the Dataflow monitoring interface.  
[Go to the Dataflow Web Interface](https://console.cloud.google.com/dataflow)
  2. To view job details, select your Dataflow job.
  3. In the **Job info** side panel, to see the key type, check the **Encryption type** field. 
     * For Encryption type: "Google-Managed key" ![Job info side panel listing the details of a Dataflow job.
      The type of key your job uses is listed in the Encryption type field.](https://docs.cloud.google.com/static/dataflow/images/job-summary-cmek-details.png)
     * For Encryption type: "Customer-Managed key" ![Job info side panel listing the details of a Dataflow job.
      The type of key your job uses is listed in the Encryption type field.](https://docs.cloud.google.com/static/dataflow/images/job-summary-gmek-details.png)




### CLI

Run the [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command using the gcloud CLI:

`gcloud dataflow jobs describe JOB_ID`

Search for the line that contains `serviceKmsKeyName`. This information shows that a Cloud KMS key was used for Dataflow pipeline state encryption.

You can verify Cloud KMS key usage for encrypting sources and sinks by using the Google Cloud console pages and tools of those sources and sinks, including Pub/Sub, Cloud Storage, and BigQuery. You can also verify Cloud KMS key usage through viewing your [Cloud KMS audit logs](https://docs.cloud.google.com/kms/docs/audit-logging#viewing_logs).

## Disable or destroy the key

If for any reason you may need to disable or destroy the key, you can use the Google Cloud console. Both disable and destroy operations cancel the jobs using that key. This operation is permanent.

If you're using Cloud EKM, disable or destroy the key in your external key manager.

If you're using the Streaming Engine option, taking a [snapshot](https://cloud.google.com/dataflow/docs/guides/using-snapshots) of the job before disabling the key is recommended.

## Remove Dataflow access to the Cloud KMS key

You can remove Dataflow access to the Cloud KMS key by using the following steps:

  1. Revoke `Cloud KMS CryptoKey Encrypter/Decrypter` [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to the **Dataflow service account** using the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#updating-gcloud).
  2. Revoke `Cloud KMS CryptoKey Encrypter/Decrypter` [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to the **Compute Engine service account** using the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#updating-gcloud).
  3. Optionally, you can also [destroy the key version material](https://docs.cloud.google.com/kms/docs/destroy-restore) to further prevent Dataflow and other services from accessing the pipeline state. You can also [delete the key or key version](https://docs.cloud.google.com/kms/docs/delete-kms-resources) to remove them from lists of your Cloud KMS resources.



You can't delete keys rings, but they don't have billable costs or quota limitations, so their continued existence doesn't affect costs or production limits.

Dataflow jobs periodically validate whether the **Dataflow service account** can successfully use the given Cloud KMS key. If an encrypt or decrypt request fails, the Dataflow service halts all data ingestion and processing as soon as possible. Dataflow immediately begins cleaning up the Google Cloud resources attached to your job.

## Use sources and sinks that are protected with Cloud KMS keys

Dataflow can access Google Cloud sources and sinks that are protected by Cloud KMS keys. If you're not creating new objects, you don't need to specify the Cloud KMS key of those sources and sinks. If your Dataflow pipeline might create new objects in a sink, you must define pipeline parameters. These parameters specify the Cloud KMS keys for that sink and pass this Cloud KMS key to appropriate I/O connector methods.

For Dataflow pipeline sources and sinks that don't support CMEK managed by Cloud KMS, the Dataflow CMEK settings are irrelevant.

### Cloud KMS key permissions

When accessing services that are protected with Cloud KMS keys, verify that you have assigned the `Cloud KMS CryptoKey Encrypter/Decrypter` [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to that service. The accounts are of the following form:

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#prereqs): `service-{project_number}@gs-project-accounts.iam.gserviceaccount.com`
  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#grant_permission): `bq-{project_number}@bigquery-encryption.iam.gserviceaccount.com`
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/cmek): `service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com`



### Cloud Storage

If you want to protect the temporary and staging buckets that you specified with the `TempLocation`/`temp_location` and `stagingLocation`/`staging_location` pipeline parameters, see [setting up CMEK-protected Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

### BigQuery

### Java

Use the `with_kms_key()` method on return values from `BigQueryIO.readTableRows()`, `BigQueryIO.read()`, `BigQueryIO.writeTableRows()`, and `BigQueryIO.write()`.

You can find an example in the [Apache Beam GitHub repository](https://github.com/apache/beam/blob/49403c00499f7f87c2bf9a4c63dec8ebd68d640d/sdks/java/io/google-cloud-platform/src/test/java/org/apache/beam/sdk/io/gcp/bigquery/BigQueryKmsKeyIT.java#L91-L100).

### Python

Use the `kms_key` argument in [BigQuerySource](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.bigquery.html?highlight=bigquery#apache_beam.io.gcp.bigquery.BigQuerySource) and [BigQuerySink](https://beam.apache.org/releases/pydoc/current/_modules/apache_beam/io/gcp/bigquery.html#BigQuerySink).

You can find an example in the [Apache Beam GitHub repository](https://github.com/apache/beam/blob/006b7419de5c707912da315f3f66450a72c95a36/sdks/python/apache_beam/io/gcp/big_query_query_to_table_pipeline.py#L64-L73).

### Go

BigQuery IOs don't support using the kms key in Go.

### Pub/Sub

Dataflow handles access to CMEK-protected topics by using your topic CMEK configuration.

To read from and write to CMEK-protected Pub/Sub topics, see [Pub/Sub instructions for using CMEK](https://docs.cloud.google.com/pubsub/docs/cmek).

## Audit logging for Cloud KMS key usage

Dataflow enables Cloud KMS to use Cloud Audit Logs for logging [key operations](https://docs.cloud.google.com/kms/docs/audit-logging#audited_operations), such as encrypt and decrypt. Dataflow provides the job ID as context to a Cloud KMS caller. This ID lets you track each instance a specific Cloud KMS key is used for a Dataflow job.

Cloud Audit Logs maintains [audit logs](https://docs.cloud.google.com/logging/docs/audit) for each Google Cloud project, folder, and organization. You have several options for [viewing your Cloud KMS audit logs](https://docs.cloud.google.com/kms/docs/audit-logging#viewing_logs).

Cloud KMS writes **Admin Activity** audit logs for your Dataflow jobs with CMEK encryption. These logs record operations that modify the configuration or metadata of a resource. You can't disable Admin Activity audit logs.

If explicitly enabled, Cloud KMS writes **Data Access** audit logs for your Dataflow jobs with CMEK encryption. Data Access audit logs contain API calls that read the configuration or metadata of resources. These logs also contain user-driven API calls that create, modify, or read user-provided resource data. For instructions on enabling some or all of your Data Access audit logs, go to [Configuring data access Logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Pricing

You can use Cloud KMS encryption keys with Dataflow in all [Dataflow regions](https://docs.cloud.google.com/dataflow/docs/resources/locations) where Cloud KMS is available.

This integration does not incur additional costs beyond the key operations, which are billed to your Google Cloud project. Each time the Dataflow service account uses your Cloud KMS key, the operation is billed at the rate of Cloud KMS key operations.

For more information, see [Cloud KMS pricing details](https://cloud.google.com/kms/pricing).

## Troubleshooting

Use the suggestions in this section to troubleshoot errors.

### Cloud KMS cannot be validated

Your workflow might fail with the following error:
    
    
    Workflow failed. Causes: Cloud KMS key <key-name> cannot be validated.
    

To fix this issue, verify that you have passed the full key path. It looks like `projects/<project-id>/locations/<gcp-region>/keyRings/<key-ring-name>/cryptoKeys/<key-name>`. Look for possible typos in the key path.

### Cloud KMS key permission denied

Your workflow might fail with the following error:
    
    
    Workflow failed. Causes: Cloud KMS key Permission 'cloudkms.cryptoKeyVersions.useToEncrypt' denied on resource
    'projects/<project-id>/locations/<gcp-region>/keyRings/<key-ring-name>/cryptoKeys/<key-name>' (or it may not exist). cannot be validated.
    

To fix this issue, verify that the [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) mentioned in the key path is correct. Also, check that you have the [permission](https://cloud.google.com/kms/docs/reference/permissions-and-roles#resource_hierarchy) to use the key.

### Cloud KMS key location doesn't match Dataflow job location

Your workflow might fail with the following error:
    
    
    Workflow failed. Causes: Cloud KMS key projects/<project-id>/locations/<gcp-region>/keyRings/<key-ring-name>/cryptoKeys/<key-name>
    can't protect resources for this job. Make sure the region of the KMS key matches the Dataflow region.
    

To fix this issue, if you're using a regional key, verify that the Cloud KMS key is in the same region as the Dataflow job.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
