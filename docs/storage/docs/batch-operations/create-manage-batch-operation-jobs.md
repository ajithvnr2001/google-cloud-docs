---
url: https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs/
title: Create and manage batch operation jobs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:57.282914+00:00
---

# Create and manage batch operation jobs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create and manage batch operation jobs Stay organized with collections  Save and categorize content based on your preferences. 

[Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) lets you automate large-scale tasks across Cloud Storage objects by running batch jobs. You can create, view, list, cancel, and delete these jobs, and track administrative activity by using Cloud Audit Logs.

## Before you begin

To create and manage storage batch operations jobs, complete the steps in the following sections.

### Configure Storage Intelligence

To create and manage storage batch operations jobs, [configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#configure-storage-intelligence) on the bucket where you want to run the job.

### Enable the storage batch operations API

Enable the storage batch operations API.
    
    
    gcloud services enable storagebatchoperations.googleapis.com

### Create a manifest

If you want to use a manifest for [object selection](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-selection), create a manifest file. Using a manifest is one of the ways you can select objects to process in a storage batch operations job.

## Create a storage batch operations job

This section describes how to create a storage batch operations job.

To get the permissions that you need to create a storage batch operations job, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the objects on which you want to perform batch operations.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Click **Create batch operations**.
  4. In the **Select operation** pane, choose the operation type: 
     * **Manage object holds** : Select **Temporary hold** or **Event-based hold**. For more information, see [object holds](https://docs.cloud.google.com/storage/docs/object-holds).
     * **Update object metadata** : To add [object metadata](https://docs.cloud.google.com/storage/docs/metadata), do the following: 
       * To add custom metadata, complete the following steps: 
         1. In the **Key** field, enter a key name.
         2. In the **Value** field, enter a value for that key.
         3. Optional: Click **\+ Add item** to add more key-value pairs.
       * To update fixed-key metadata, complete the following steps: 
         1. To expand the **Update fixed-key metadata** section, click the expand_moreexpander arrow.
         2. In the **Select one or more metadata to update** list, select metadata items to edit.
     * **Update/Rotate encryption key** : To use or update [the encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for objects, do the following: 
       1. In the **Select a Cloud KMS key** list, select a customer-managed encryption key (CMEK).
       2. Optional: Select **Switch project** to pick a key from another project or select **Enter key manually** to fill details.
     * **Delete objects** : To [delete objects](https://docs.cloud.google.com/storage/docs/object-deletion-overview), do the following: 
       1. [Check whether Object Versioning is enabled](https://docs.cloud.google.com/storage/docs/using-object-versioning#check).
       2. If Object Versioning is enabled, choose one of the following deletion options:

          * Select **Delete all versions of the objects** to remove both live and noncurrent versions.
          * Select **Permanently delete live versions** to remove only the live version.

If Object Versioning is not enabled, any objects selected for deletion are permanently deleted.

**Warning:** Accidental object deletion carries a risk of data loss. Enable soft delete to recover accidental object deletions. 
  5. Click **Next**.
  6. In the **Name operation & specify objects** pane, do the following: 
     1. In the **Name** field, enter a name.
     2. Optional: In the **Description** field, enter a description.
     3. In the **Specify objects** section, define a criterion to process objects from the bucket. Choose one of the following options: 
        * **Select all objects** : Includes all objects in the bucket.
        * **Select objects by using prefix filters** : To define the list of objects by using prefix filters, do the following: 
          1. In the **Enter Prefixes of the objects to be included** field, enter a prefix.
          2. Optional: Click **\+ Add prefix** to specify additional prefixes.
        * **Upload lists of objects using manifest CSV files** : To use a manifest file for selecting objects, do the following: 

          1. Upload your manifest CSV file to a bucket. This file must contain headers for **Bucket name** , **Object key** , and **Generation number**.
          2. In the **Select manifest file mode** list, choose one of the following options: 
             * If you select **Select a manifest file from Cloud Storage** , click **Browse** in the **Select a manifest file from Cloud Storage** field. In the **Select object** dialog that appears, navigate to your manifest CSV file, then click **Select**.
             * If you select **Select multiple manifest files using wildcard** , enter the file path in the **Enter manifest file location using wildcard** field. For example, `bucket-name/folder/manifest_*`.
  7. Click **Create**.



### Command line

To define the list of objects for your batch operation job, you can choose one of the following source configurations:

  * **Project as the source** : Targets objects for a project using a Storage Insights dataset configuration. Instead of specifying individual buckets or prefixes, you can specify advanced filter parameters, such as `--insights-dataset-config`, `--target-project`, `--bucket-filters`, and `--object-filters`. For details see, Create a job using advanced filters.
  * **Buckets as the source** : Targets objects within specific buckets. You must specify one of the following flags: 
    * `--bucket` or `--bucket-list` to define the target buckets.
    * A manifest CSV file (`--manifest-location`) or object prefixes (`--included-object-prefixes`) to define the target objects.


  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use [Google Cloud CLI version 516.0.0 or later](https://docs.cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version).

  3. To set the default project, run the `gcloud config set project` command:
         
         gcloud config set project PROJECT_ID

Where PROJECT_ID is the ID of your project.

  4. Optional: Run a [dry run](https://docs.cloud.google.com/storage/docs/batch-operations/overview#dry-run) job. Before executing any job, we recommend that you run the job in dry run mode to verify the object selection criteria and check for any errors. The dry run doesn't modify any objects.

In your development environment, run the [`gcloud storage batch-operations jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create) command with the `--dry-run` flag:
         
         gcloud storage batch-operations jobs create DRY_RUN_JOB_NAME \
         {--bucket=BUCKET | --bucket-list=BUCKET_LIST} OBJECT_SELECTION_FLAG JOB_TYPE_FLAG \
         --dry-run

Where:

     * `DRY_RUN_JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations dry run job.

The other parameters are the same as for the actual job. For more information, see parameter descriptions.

To view the results of the dry run, see Get storage batch operations job details.

  5. After a successful dry run, run the [`gcloud storage batch-operations jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create) command.
         
         gcloud storage batch-operations jobs create JOB_NAME \
         {--bucket=BUCKET | --bucket-list=BUCKET_LIST} OBJECT_SELECTION_FLAG JOB_TYPE_FLAG

Where the parameters are as follows:

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

**Note:** When you create the actual job, specify a unique job name or delete the dry run job first. Reusing the dry run's job name causes the creation to fail with an `already exists` error.
     * `--bucket`: `BUCKET` is the name of the bucket containing the objects you want to process.

     * `--bucket-list`: `BUCKET_LIST` is a comma-separated list of one or more bucket names containing the objects you want to process. You can specify up to 1,000 buckets from any project, as long as each bucket is enrolled in a storage intelligence plan.

     * `OBJECT_SELECTION_FLAG` is one of the following flags that you need to specify:

       * `--included-object-prefixes`: Specify one or more [object prefixes](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-prefixes). For example:

         * To match a single prefix, use: `--included-object-prefixes='prefix1'`.
         * To match multiple prefixes, use a comma-separated prefix list: `--included-object-prefixes='prefix1,prefix2'`.
         * To include all objects, use an empty prefix: `--included-object-prefixes=''`.
       * `--manifest-location`: Specify the manifest location. For example, `gs://bucket_name/path/object_name.csv`.

     * `JOB_TYPE_FLAG` is one of the following flags that you need to specify, depending on the [job type](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type).

       * `--delete-object`: Delete one or more objects.

         * If [Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-lock#enable-retentions) is enabled for the bucket, current objects transition to a noncurrent state, and noncurrent objects are skipped.

         * If Object Versioning is disabled for the bucket, the delete operation permanently deletes objects and skips noncurrent objects.

       * `--enable-permanent-object-deletion`: Permanently delete objects. Use this flag along with the `--delete-object` flag to permanently delete both live and noncurrent objects in a bucket, regardless of the bucket's object versioning configuration.

       * `--rewrite-object`: Update the [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for one or more objects. You can also use this flag to change the object's storage class by specifying the `storage-class` key. Supported storage classes include `STANDARD`, `NEARLINE`, `COLDLINE`, and `ARCHIVE`. For example, `--rewrite-object=storage-class=NEARLINE`.

**Caution:** If you change the storage class of an object in an Autoclass-enabled bucket, the operation has no effect. The operation reports success, but Cloud Storage resets the object's storage class to the default class defined by Autoclass.**Note:** Changing the storage class of an object involves rewriting its data. A rewrite is a Class A operation. These operations might incur additional charges depending on the age, location, and storage class of the data. For more information, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing). If you enable [Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) for your bucket, Cloud Storage retains the original object as a noncurrent version. This version remains in the bucket until you explicitly delete it.
       * `--set-object-acls-from-file`: Patch object access control lists (ACLs). Provide a JSON or YAML file with grants to add or update for entities such as `allUsers` or `allAuthenticatedUsers`. For example: `--set-object-acls-from-file=acl-updates.yaml` or `--set-object-acls-from-file=acl-updates.json`.

The structure of the YAML file for updates is as follows:
             
             grants:
               - entity: allAuthenticatedUsers
                 role: READER
               remove_entities:
               - allUsers
             

The structure of the JSON file for updates is as follows:
             
             {
             "grants": [
               {
                 "entity": "allAuthenticatedUsers",
                 "role": "READER"
               }
             ],
             "remove_entities": [
               "allUsers"
             ]
             }

       * `--put-object-event-based-hold`: Enable event-based [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--no-put-object-event-based-hold`: Disable event-based [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--put-object-temporary-hold`: Enable temporary [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--no-put-object-temporary-hold`: Disable temporary [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

The following example shows how to create a job to update the `Content-Language` metadata to `en` for all objects listed in `manifest.csv`.
             
             gcloud storage batch-operations jobs create my-job \
             --bucket=my-bucket \
             --manifest-location=gs://my-bucket/manifest.csv \
             --put-metadata=Content-Language=en

The following example shows how to create a job targeting multiple buckets to update `Content-Language` to `en-us`:
             
             gcloud storage batch-operations jobs create my-job \
             --bucket-list=bucket1,bucket2 \
             --included-object-prefixes='' \
             --put-metadata=Content-Language=en-us

       * `--put-metadata`: Update [object metadata](https://docs.cloud.google.com/storage/docs/batch-operations/overview#metadata-updates). Specify the key-value pair for the object metadata you want to modify. You can specify one or more key-value pairs as a list. You can also set [object retention configurations](https://docs.cloud.google.com/storage/docs/object-lock) using the `--put-metadata` flag. To do so, specify the retention parameters using the `Retain-Until` and `Retention-Mode` fields. For example,
             
             gcloud storage batch-operations jobs create my-job \
             --bucket=my-bucket \
             --manifest-location=gs://my-bucket/manifest.csv \
             --put-metadata=Retain-Until=RETAIN_UNTIL_TIME,Retention-Mode=RETENTION_MODE

Where:

         * `RETAIN_UNTIL_TIME` is the date and time, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format, until which the object is retained. For example, `2025-10-09T10:30:00Z`. To set the retention configuration on an object, you'll need to [enable retention on the bucket](https://docs.cloud.google.com/storage/docs/using-object-lock#enable-retentions) which contains the object. 

         * `RETENTION_MODE` is the retention mode, either `Unlocked` or `Locked`.

When you send a request to update the `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields, consider the following:

           * To update the object retention configuration, you must provide non-empty values for both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields; setting only one results in an `INVALID_ARGUMENT` error.
           * You can extend the `RETAIN_UNTIL_TIME` value for objects in both `Unlocked` or `Locked` modes.
           * The object retention must be in `Unlocked` mode if you want to do the following: 
             * Reduce the `RETAIN_UNTIL_TIME` value.
             * Remove the retention configuration. To remove the configuration, you'll need to provide empty values for both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields.
           * If you omit both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields, the retention configuration remains unchanged. 

       * `--clear-all-object-custom-contexts`: Delete all existing [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

The following example shows how to create a job to clear all object contexts for objects listed in `manifest.csv`:
             
             gcloud storage batch-operations jobs create my-job \
             --bucket=my-bucket \
             --manifest-location=gs://my-bucket/manifest.csv \
             --clear-all-object-custom-contexts

**Caution:** Clearing all object contexts deletes all the existing contexts on the object. To preserve the previous object contexts, enable [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). The logs contain contexts from before the update, which you can use to restore previous values.
       * `--clear-object-custom-contexts`: Remove contexts with specific keys. You can also update specific contexts along with removing keys by using both the `--clear-object-custom-contexts` flag and one of the following flags:

         * `--update-object-custom-contexts`: Provide a map of key-value pairs.

The following example shows how to create a job to remove the context with key `temp-id` and update or insert context with key `project-id` and `cost-center` for all objects listed in `manifest.csv`:
               
               gcloud storage batch-operations jobs create my-job \
               --bucket=my-bucket \
               --manifest-location=gs://my-bucket/manifest.csv \
               --clear-object-custom-contexts=temp-id \
               --update-object-custom-contexts=project-id=project-A,cost-center=engineering

**Note:** You can't specify the same key in both the `--clear-object-custom-contexts` flag and the `--update-object-custom-contexts` flag. Doing so results in an `INVALID_ARGUMENT` error.
         * `--update-object-custom-contexts-file`: Provide the path to a JSON or YAML file with key-value pairs.

The following example shows how to create a job to process objects defined in `manifest.csv`. The job does the following:

           * Removes all contexts with the `temp-id` key.

           * Updates existing contexts with the `project-id` and `cost-center` keys defined in the `/tmp/context_updates.json` file.
    
    gcloud storage batch-operations jobs create my-job \
    --bucket=my-bucket \
    --manifest-location=gs://my-bucket/manifest.csv \
    --clear-object-custom-contexts=temp-id \
    --update-object-custom-contexts-file=/tmp/context_updates.json

Where `/tmp/context_updates.json` contains the following object contexts:
    
    {
    "project-id": {"value": "project-A"},
    "cost-center": {"value": "engineering"}
    }




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id,
       std::string const& target_bucket_name, std::string const& object_prefix) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      namespace sbo = google::cloud::storagebatchoperations::v1;
      sbo::Job job;
      sbo::BucketList* bucket_list = job.mutable_bucket_list();
      sbo::BucketList::Bucket* bucket_config = bucket_list->add_buckets();
      bucket_config->set_bucket(target_bucket_name);
      sbo::PrefixList* prefix_list_config = bucket_config->mutable_prefix_list();
      prefix_list_config->add_included_object_prefixes(object_prefix);
      sbo::DeleteObject* delete_object_config = job.mutable_delete_object();
      delete_object_config->set_permanent_object_deletion_enabled(false);
      auto result = client.CreateJob(parent, job, job_id).get();
      if (!result) throw result.status();
      std::cout << "Created job: " << result->name() << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\CreateJobRequest;
    use Google\Cloud\StorageBatchOperations\V1\Job;
    use Google\Cloud\StorageBatchOperations\V1\BucketList;
    use Google\Cloud\StorageBatchOperations\V1\BucketList\Bucket;
    use Google\Cloud\StorageBatchOperations\V1\PrefixList;
    use Google\Cloud\StorageBatchOperations\V1\DeleteObject;
    
    /**
     * Create a new batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     * @param string $bucketName The name of your Cloud Storage bucket to operate on.
     *        (e.g. 'my-bucket')
     * @param string $objectPrefix The prefix of objects to include in the operation.
     *        (e.g. 'prefix1')
     */
    function create_job(string $projectId, string $jobId, string $bucketName, string $objectPrefix): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
    
        $prefixListConfig = new PrefixList(['included_object_prefixes' => [$objectPrefix]]);
        $bucket = new Bucket(['bucket' => $bucketName, 'prefix_list' => $prefixListConfig]);
        $bucketList = new BucketList(['buckets' => [$bucket]]);
    
        $deleteObject = new DeleteObject(['permanent_object_deletion_enabled' => false]);
    
        $job = new Job(['bucket_list' => $bucketList, 'delete_object' => $deleteObject]);
    
        $request = new CreateJobRequest([
            'parent' => $parent,
            'job_id' => $jobId,
            'job' => $job,
        ]);
        $response = $storageBatchOperationsClient->createJob($request);
    
        printf('Created job: %s', $response->getName());
    }

### JSON API

To define the list of objects for your batch operation job, you can choose one of the following source configurations:

  * **Project as the source** : Targets objects project-wide using a `projectSource` configuration. Instead of listing individual buckets or prefixes, you specify advanced filter parameters to query storage insights metadata dynamically. For more information, see the JSON API tab in Create a job using advanced filters.
  * **Buckets as the source** : Targets objects within specific buckets using a `bucketList` configuration. You must specify the target buckets and either a manifest CSV file (`manifest_location`) or object prefixes (`include_object_prefixes`).


  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the [storage batch operations job](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs). The following are common settings to include:
         
         {
                 "Description": "JOB_DESCRIPTION",
                 "BucketList":
                 {
                 "Buckets":
                 [
                  {
                    "Bucket": "BUCKET_NAME",
                    "Manifest": {
                       "manifest_location": "MANIFEST_LOCATION"
                        }
                    "PrefixList": {
                       "include_object_prefixes": "OBJECT_PREFIXES"
                        }
                  }
                 ]
                 },
                 "DeleteObject":
                 {
                 "permanent_object_deletion_enabled": OBJECT_DELETION_VALUE
                  }
                 "RewriteObject": {
                   "kms_key":"KMS_KEY_VALUE",
                   "storage_class":"STORAGE_CLASS_VALUE"
                   }
                 "PutMetadata":{
                   "METADATA_KEY": "METADATA_VALUE",
                   ...,
                   "objectRetention": {
                       "retainUntilTime": "RETAIN_UNTIL_TIME",
                       "mode": "RETENTION_MODE"
                      }
                    }
                 "PutObjectHold": {
                   "temporary_hold": TEMPORARY_HOLD_VALUE,
                   "event_based_hold": EVENT_BASED_HOLD_VALUE
                 },
                 "updateObjectCustomContext": {
                    "customContextUpdates": {
                       "updates": {
                          "CONTEXT_KEY": { "value": "CONTEXT_VALUE" }
                       },
                       "keysToClear": ["CONTEXT_KEY_TO_CLEAR"]
                    },
                    "clearAll": CLEAR_ALL_VALUE
                 },
                 "SetObjectAcls": {
                    "accessControlsUpdates": {
                       "grants": [
                          { "entity": "allUsers", "role": "READER" }
                       ],
                       "removeEntities": ["allAuthenticatedUsers"]
                    }
                 },
                 "dryRun": DRY_RUN_VALUE
                 }
                  
         
         Where:
         

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

     * `JOB_DESCRIPTION` is the [description](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-description) of the storage batch operations job.

     * `BUCKET_NAME` is the [name of the bucket](https://docs.cloud.google.com/storage/docs/batch-operations/overview#bucket-list) that contains one or more objects you want to process.

     * To specify the objects you want to process, use any one of the following attributes in the JSON file:

       * `MANIFEST_LOCATION` is the manifest location. For example, `gs://bucket_name/path/object_name.csv`.

       * `OBJECT_PREFIXES` is the comma-separated list containing one or more [object prefixes](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-prefixes). To match all objects, use an empty list.

     * Depending on the job you want to process, specify any one of the following options:

       * Delete objects:
             
             "DeleteObject":
               {
               "permanent_object_deletion_enabled": OBJECT_DELETION_VALUE
               }

Where `OBJECT_DELETION_VALUE` is `TRUE` to delete objects.

       * Update the [Customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for objects:
             
             "RewriteObject":
               {
               "kms_key": KMS_KEY_VALUE
               }

Where `KMS_KEY_VALUE` is the value of the object's KMS key you want to update.

       * Update the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for objects:
             
             "RewriteObject":
               {
               "storage_class": STORAGE_CLASS_VALUE
               }

Where `STORAGE_CLASS_VALUE` is the new storage class you want to transition the objects to. Supported storage classes include `STANDARD`, `NEARLINE`, `COLDLINE`, and `ARCHIVE`.

       * Update [object metadata](https://docs.cloud.google.com/storage/docs/metadata#editable):
             
             "PutMetadata": {
                  "METADATA_KEY": "METADATA_VALUE",
                  ...,
                 "objectRetention": {
                    "retainUntilTime": "RETAIN_UNTIL_TIME",
                    "mode": "RETENTION_MODE"
                  }
                }

Where:

         * `METADATA_KEY/VALUE` is the [object's metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) key-value pair. You can specify one or more pairs.
         * `RETAIN_UNTIL_TIME` is the date and time, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format, until which the object is retained. For example, `2025-10-09T10:30:00Z`. To set the retention configuration on an object, you'll need to [enable retention on the bucket](https://docs.cloud.google.com/storage/docs/using-object-lock#enable-retentions) which contains the object. 
         * `RETENTION_MODE` is the retention mode, either `Unlocked` or `Locked`. 

When you send a request to update the `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields, consider the following:

           * To update the object retention configuration, you must provide non-empty values for both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields; setting only one results in an `INVALID_ARGUMENT` error.
           * You can extend the `RETAIN_UNTIL_TIME` value for objects in both `Unlocked` or `Locked` modes.
           * The object retention must be in `Unlocked` mode if you want to do the following: 
             * Reduce the `RETAIN_UNTIL_TIME` value.
             * Remove the retention configuration. To remove the configuration, you'll need to provide empty values for both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields.
           * If you omit both `RETENTION_MODE` and `RETAIN_UNTIL_TIME` fields, the retention configuration remains unchanged. 
       * Update [object holds](https://docs.cloud.google.com/storage/docs/object-holds):
             
             "PutObjectHold": {
                 "temporary_hold": TEMPORARY_HOLD_VALUE,
                 "event_based_hold": EVENT_BASED_HOLD_VALUE
               }

Where:

         * `TEMPORARY_HOLD_VALUE` is used to enable or disable the temporary object hold. A value of `1` enables the hold, and a value of `2` disables the hold.

         * `EVENT_BASED_HOLD_VALUE` is used to enable or disable the event-based object hold. A value of `1` enables the hold, and a value of `2` disables the hold.

       * Update [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts):
             
             "updateObjectCustomContext": {
                 "customContextUpdates": {
                   "updates": {
                     "CONTEXT_KEY": { "value": "CONTEXT_VALUE" }
                   },
                   "keysToClear": ["CONTEXT_KEY_TO_CLEAR"]
                 },
                 "clearAll": CLEAR_ALL_VALUE
               }

Where:

         * `CONTEXT_KEY` is the object context key to insert or update.
         * `CONTEXT_VALUE` is the object context value for the key.
         * `CONTEXT_KEY_TO_CLEAR` is the key to remove.
         * `CLEAR_ALL_VALUE` is set to `true` to delete all existing object contexts.
       * Update [object access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists):
             
             "SetObjectAcls": {
                 "accessControlsUpdates": {
                    "grants": [
                       { "entity": "ENTITY_NAME", "role": "ROLE_NAME" }
                    ],
                    "removeEntities": ["ENTITY_TO_REMOVE"]
                 }
               }

Where:

         * `ENTITY_NAME` is the entity to add or update access, For example, `allUsers`, `allAuthenticatedUsers`, or a specific user/group.
         * `ROLE_NAME` is the role to grant. For example, `READER`, `OWNER`.
         * `ENTITY_TO_REMOVE` is the entity whose credentials you want to remove.
     * `DRY_RUN_VALUE` is an optional boolean value. Set to `true` to run the job in dry run mode. The default value is `false`.

**Important:** We recommend running the job in dry run mode before running the actual job. The dry run verifies object selection criteria and checks for errors without modifying any objects.
     1. Use [`curl`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` storage batch operations job](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/create) request:
            
            curl -X POST --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs?job_id=JOB_NAME"

Where:

        * `JSON_FILE_NAME` is the name of the JSON file.
        * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.
        * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

**Note:** When creating the actual job after a dry run, you must specify a unique job name, unless you explicitly delete the dry run job first. Reusing the dry run's job name causes the job creation to fail with an `already exists` error.



## Get storage batch operations job details

This section describes how to get the storage batch operations job details.

To get the permissions that you need to view a storage batch operations job, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the operation.
  3. On the **Bucket details** page, click the **Operations** tab.
  4. In the list of operations, click the **Operation ID** of the job you want to view.
  5. The details page shows metrics for your job in the **Overview** tab, such as objects discovered, processed, and any errors that occurred.
  6. In the **Error summary** table, review execution failure details or click **View in Cloud Logging** to view records.
  7. To view the configuration settings for the job, click the **Configuration** tab.



### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage batch-operations jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/describe) command.
         
         gcloud storage batch-operations jobs describe JOB_NAME

Where:

`JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

When you dry run a job, the output includes the following fields:

     * `totalObjectCount`: Displays the number of objects that match your selection criteria.
     * `errorSummaries`: Lists any errors found during the dry run, such as permission issues or invalid configurations.
     * `totalBytesFound`: Displays the total size of the affected objects. This field only appears when you use [object prefixes](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-prefixes) for object selection.

If successful, the response for the dry run job looks similar to the following example:
    
    bucketList:
        buckets:
        - bucket: my-bucket
          manifest:
            manifestLocation: gs://my-bucket/manifest.csv
      completeTime: '2025-10-27T23:56:32Z'
      counters:
        totalObjectCount: '4'
      createTime: '2025-10-27T23:56:22.243528568Z'
      dryRun: true
      name: projects/my-project/locations/global/jobs/my-job
      putMetadata:
        contentLanguage: en
      state: SUCCEEDED
    

A successful job response omits the `dryRun` field and returns the following metrics in the `counters` field:

     * Total objects found.
     * Total bytes found when using object prefixes.
     * Successful object transformations.
     * Failed object transformations, if applicable.
     * Object contexts created, if applicable.
     * Object contexts deleted, if applicable.
     * Object contexts updated, if applicable. This counter tracks updates made to existing context keys.

The response for an actual job run looks similar to the following example:
    
    bucketList:
        buckets:
        - bucket: my-bucket
          manifest:
            manifestLocation: gs://my-bucket/manifest.csv
      completeTime: '2025-10-31T20:19:42.357826655Z'
      counters:
        succeededObjectCount: '4'
        totalObjectCount: '4'
      createTime: '2025-10-31T20:19:22.016517077Z'
      name: projects/my-project/locations/global/jobs/my-job
      putMetadata:
        contentLanguage: en
      state: SUCCEEDED
      

**Note:** If the objects in the bucket are modified after a dry run, the `totalObjectCount` value of the actual job might differ from the dry run's results.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      auto const name = parent + "/jobs/" + job_id;
      auto job = client.GetJob(name);
      if (!job) throw job.status();
      std::cout << "Got job: " << job->name() << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\GetJobRequest;
    
    /**
     * Gets a batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     */
    function get_job(string $projectId, string $jobId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
        $formattedName = $parent . '/jobs/' . $jobId;
    
        $request = new GetJobRequest([
            'name' => $formattedName,
        ]);
    
        $response = $storageBatchOperationsClient->getJob($request);
    
        printf('Got job: %s', $response->getName());
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/json_api) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` storage batch operations job](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs/JOB_NAME"

Where:

     * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.
     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

When you dry run a job, the output includes the following fields:

     * `totalObjectCount`: Displays the number of objects that match your selection criteria.
     * `errorSummaries`: Lists any errors found during the dry run, such as permission issues or invalid configurations.
     * `totalBytesFound`: Displays the total size of the affected objects. This field only appears when you use [object prefixes](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-prefixes) for object selection.

If successful, the response for the dry run looks similar to the following example:
    
    {
      "name": "projects/my-project/locations/global/jobs/my-job",
      "description": "dry-run-job",
      "deleteObject": {
        "permanent_object_deletion_enabled": true
         },
      "createTime": "2025-10-28T00:26:53.900882459Z",
      "completeTime": "2025-10-28T00:27:04.101663275Z",
      "counters": {
          "totalObjectCount": "5",
          "totalBytesFound": "203"
        },
      "state": "SUCCEEDED",
      "bucketList": {
        "buckets": [
          {
            "bucket": "my-bucket",
            "prefixList": {
              "includedObjectPrefixes": [
                ""
              ]
            }
          }
        ]
      },
      "dryRun": true
    }
    

A successful job response omits the `dryRun` field and returns the following metrics in the `counters` field:

     * Total objects found.
     * Total bytes found when using object prefixes.
     * Successful object transformations.
     * Failed object transformations, if applicable.
     * Object contexts created, if applicable.
     * Object contexts deleted, if applicable.
     * Object contexts updated, if applicable. This counter tracks updates made to existing context keys.

The response for an actual job run looks similar to the following example:
           
           {
           "name": "my-job",
           "description": "my-delete-objects-job",
           "deleteObject": {
             "permanent_object_deletion_enabled": true
           },
           "createTime": "2025-10-28T00:26:53.900882459Z",
           "completeTime": "2025-10-28T00:27:04.101663275Z",
           "counters": {
             "succeededObjectCount: "5"
             "totalObjectCount": "5",
             "totalBytesFound": "203"
           },
           "state": "SUCCEEDED",
           "bucketList": {
             "buckets": [
               {
                 "bucket": "my-bucket",
                 "prefixList": {
                   "includedObjectPrefixes": [
                     ""
                   ]
                 }
               }
             ]
           }
           }
           

**Note:** If the objects in the bucket are modified after a dry run, the `totalObjectCount` value of the actual job might differ from the dry run's results.



### List bucket operations

For jobs that include multiple buckets, you can view the progress and status of operations on individual buckets. To list the operations performed on buckets for a specific job, run the `gcloud storage batch-operations bucket-operations list` command:
    
    
    gcloud storage batch-operations bucket-operations list --job=JOB_NAME

You can also filter the list to specific buckets using the `--buckets` flag:
    
    
    gcloud storage batch-operations bucket-operations list --job=JOB_NAME --buckets=BUCKET_NAME_LIST

The following example shows how to list operations for `bucket1` and `bucket2` for the job `my-job`:
    
    
    gcloud storage batch-operations bucket-operations list --job=my-job --buckets=bucket1,bucket2

Where:

  * `JOB_NAME` is the unique name of the storage batch operations job that you created. For example, `my-job`.
  * `BUCKET_NAME_LIST` is a comma-separated list of bucket names, without spaces between names. For example, `bucket1,bucket2`.

**Note:** If bucket operations are not immediately visible, wait a few moments and try running the command again.

### Describe a bucket operation

To view details for a specific bucket operation, you can use either of the following methods:

  * Use the `gcloud storage batch-operations bucket-operations describe` command with the operation resource name flag:
        
        gcloud alpha storage batch-operations bucket-operations describe BUCKET_OPERATION_RESOURCE_NAME

Where:

    * `BUCKET_OPERATION_RESOURCE_NAME` is the full resource path of the bucket operation. For example, `projects/my-project/locations/global/jobs/my-job/bucketOperations/bo-1`.
  * Use the `gcloud storage batch-operations bucket-operations describe` command with the operation bucket operation ID and job ID flags:
        
        gcloud alpha storage batch-operations bucket-operations describe BUCKET_OPERATION_ID --job=JOB_NAME

Where:

    * `BUCKET_OPERATION_ID` is the ID of the bucket operation.
    * `JOB_NAME` is the unique name of the storage batch operations job that you created. For example, `my-job`.



## List storage batch operations jobs

This section describes how to list the storage batch operations jobs within a project.

To get the permissions that you need to list storage batch operations jobs, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the operation.
  3. On the **Bucket details** page, click the **Operations** tab. The **Operations** page shows a list of active running operations.



### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage batch-operations jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/list) command.
         
         gcloud storage batch-operations jobs list




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      for (auto const& job : client.ListJobs(parent)) {
        if (!job) throw job.status();
        std::cout << job->name() << "\n";
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\ListJobsRequest;
    
    /**
     * List Jobs in a given project.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     */
    function list_jobs(string $projectId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
    
        $request = new ListJobsRequest([
            'parent' => $parent,
        ]);
    
        $jobs = $storageBatchOperationsClient->listJobs($request);
    
        foreach ($jobs as $job) {
            printf('Job name: %s' . PHP_EOL, $job->getName());
        }
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/json_api) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`LIST` storage batch operations jobs](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/list) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs"

Where:

`PROJECT_ID` is the ID or number of the project. For example, `my-project`.




## Cancel a storage batch operations job

This section describes how to cancel a storage batch operations job within a project.

**Note:** Canceling a job might not stop all in-progress operations immediately. Objects that have already been processed don't revert.

To get the permissions that you need to cancel a storage batch operations job, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket associated with the storage batch operation that you want to cancel.

  3. Click the **Operations** tab. This tab displays a list of batch operation jobs. You can only cancel jobs that are in progress.

  4. In the list of operations, select one or multiple jobs that you want to cancel, and then click **Cancel**.




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage batch-operations jobs cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/cancel) command.
         
         gcloud storage batch-operations jobs cancel JOB_NAME

Where:

`JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      auto const name = parent + "/jobs/" + job_id;
      auto response = client.CancelJob(name);
      if (!response) throw response.status();
      std::cout << "Cancelled job: " << name << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\CancelJobRequest;
    
    /**
     * Cancel a batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     */
    function cancel_job(string $projectId, string $jobId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
        $formattedName = $parent . '/jobs/' . $jobId;
    
        $request = new CancelJobRequest([
            'name' => $formattedName,
        ]);
    
        $storageBatchOperationsClient->cancelJob($request);
    
        printf('Cancelled job: %s', $formattedName);
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/json_api) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`CANCEL` a storage batch operations job](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/cancel) request:
         
         curl -X CANCEL \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs/JOB_NAME"

Where:

     * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.




## Delete a storage batch operations job

This section describes how to delete a storage batch operations job.

To get the permissions that you need to delete a storage batch operations job, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket associated with the storage batch operation that you want to delete.

  3. Click the **Operations** tab. This tab displays a list of batch operation jobs. You can delete only jobs that aren't running, such as jobs that succeeded, failed, or were canceled.

  4. In the list of operations, select one or multiple jobs that you want to delete, and then click **Delete**.




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage batch-operations jobs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/delete) command.
         
         gcloud storage batch-operations jobs delete JOB_NAME

Where:

`JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    [](google::cloud::storagebatchoperations_v1::StorageBatchOperationsClient
           client,
       std::string const& project_id, std::string const& job_id) {
      auto const parent =
          std::string{"projects/"} + project_id + "/locations/global";
      auto const name = parent + "/jobs/" + job_id;
      auto status = client.DeleteJob(name);
      if (!status.ok()) throw status;
      std::cout << "Deleted job: " << name << "\n";
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\StorageBatchOperations\V1\Client\StorageBatchOperationsClient;
    use Google\Cloud\StorageBatchOperations\V1\DeleteJobRequest;
    
    /**
     * Delete a batch job.
     *
     * @param string $projectId Your Google Cloud project ID.
     *        (e.g. 'my-project-id')
     * @param string $jobId A unique identifier for this job.
     *        (e.g. '94d60cc1-2d95-41c5-b6e3-ff66cd3532d5')
     */
    function delete_job(string $projectId, string $jobId): void
    {
        // Create a client.
        $storageBatchOperationsClient = new StorageBatchOperationsClient();
    
        $parent = $storageBatchOperationsClient->locationName($projectId, 'global');
        $formattedName = $parent . '/jobs/' . $jobId;
    
        $request = new DeleteJobRequest([
            'name' => $formattedName,
        ]);
    
        $storageBatchOperationsClient->deleteJob($request);
    
        printf('Deleted job: %s', $formattedName);
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/json_api) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE` a storage batch operations job](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/delete) request:
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs/JOB_NAME"

Where:

     * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.




## Create a storage batch operations job using Storage Insights datasets

To run a batch operations job on objects listed in a dataset, select one of the following options:

  * **Use advanced filters** : Filter objects dynamically at the project level directly in the Google Cloud CLI command.

Storage Insights datasets are created from periodic, point-in-time snapshots of your storage metadata. Each snapshot has a snapshot time that shows when the metadata was captured. When you run a batch job using advanced filters, this snapshot time determines which objects and versions are processed. By default, Storage batch operations automatically selects the latest snapshot time. To prevent operations on outdated data, job creation fails if the selected snapshot is more than two days old. For information about how to resolve this failure, see [Troubleshooting Storage batch operations issues](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#batchops-stale-snapshot).

  * **Use a manifest file** : Generate a CSV manifest file by running a BigQuery query, and then provide it to the job.




The methods are described in the following sections.

### Use advanced filters

Instead of creating a manifest file, you can use [Common Expression Language (CEL) filters](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference) to select objects directly based on fields in your Storage Insights dataset. You can run jobs across multiple buckets in a project. When you use dataset filters for object selection, storage batch operations targets objects that are live and current as of the selected dataset snapshot. Consequently, the job only includes objects that have a `NULL` value for both `softDeleteTime` and `timeDeleted` at the time of the snapshot.

### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the `gcloud storage batch-operations jobs create` command:
         
         gcloud storage batch-operations jobs create JOB_NAME \
         {--insights-dataset-config=INSIGHTS_DATASET_CONFIG_RESOURCE_NAME --target-project=TARGET_PROJECT [--bucket-filters=BUCKET_FILTER_CEL] [--object-filters=OBJECT_FILTER_CEL] [--target-locations=TARGET_LOCATIONS] [--target-snapshot-time=TARGET_SNAPSHOT_TIME] | --dry-run-job-id=DRY_RUN_JOB_ID} \
         --JOB_TYPE_FLAG

Where:

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.
     * `INSIGHTS_DATASET_CONFIG_RESOURCE_NAME`: The resource name of the dataset configuration. For example: `projects/{project-id}/locations/{location-id}/datasetConfigs/{dataset_config_id}`. You must specify this parameter before you use the `--bucket-filters` and `--object-filters` flags.
     * `TARGET_PROJECT`: The project ID or project number associated with the target resources.
     * `BUCKET_FILTER_CEL` and `OBJECT_FILTER_CEL` (Optional): The CEL filter expressions used to select objects. The following are examples: 
       * `--bucket-filters="name in ['bucket-1', 'bucket-2']"`
       * `--object-filters="size >= 5000 && name.endsWith('.pdf')"` For information about supported fields, operators, and functions, see the [CEL filters reference](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).
     * `TARGET_LOCATIONS` (Optional): A list of Cloud Storage locations used to narrow the job scope. For example: `us,us-central1,us-east4`. Use this parameter to exclude locations experiencing a service outage. If only `TARGET_LOCATIONS` is specified and `TARGET_SNAPSHOT_TIME` is omitted, the job automatically chooses the most recent snapshot timestamp that is successfully populated in both the object and bucket attribute views across all the specified locations.
     * `TARGET_SNAPSHOT_TIME` (Optional): The UTC timestamp of the dataset snapshot to use, in RFC 3339 format. For example, `2026-05-03T16:00:00Z`. This snapshot must exist across your bucket and object attribute views. If you specify this parameter, you must also specify the `TARGET_LOCATIONS` parameter.
     * `DRY_RUN_JOB_ID`: The identifier of a previously executed dry-run job. If you specify this parameter, you cannot specify any other object selection parameters, including `--insights-dataset-config`, `--target-project`, `--bucket-filters`, `--object-filters`, `--target-locations`, and `--target-snapshot-time`. The active job polls all selection criteria directly from the dry-run job.
     * `JOB_TYPE_FLAG`: The flag corresponding to the bulk operation you want to perform, such as `--put-metadata` or `--delete-object`.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON configuration file that specifies the dataset filters and bulk operations settings. For example:
         
         {
             "description": "JOB_DESCRIPTION",
             "projectSource": {
                 "project": "projects/TARGET_PROJECT",
                 "insightsDatasetConfig": "INSIGHTS_DATASET_CONFIG_RESOURCE_NAME",
                 "bucketFilters": {
                     "expression": "BUCKET_FILTER_CEL"
                 },
                 "objectFilters": {
                     "expression": "OBJECT_FILTER_CEL"
                 },
                 "snapshotTime": "SNAPSHOT_TIME",
                 "targetLocations": {
                     "locations": ["LOCATION_1", "LOCATION_2"]
                 }
             },
             "deleteObject": {
                 "permanentObjectDeletionEnabled": OBJECT_DELETION_VALUE
             }
          }

Where:

     * `JOB_DESCRIPTION` is the [description](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-description) of the job. 
       * `TARGET_PROJECT` is the project ID or project number associated with the target objects.
     * `INSIGHTS_DATASET_CONFIG_RESOURCE_NAME` is the fully qualified resource name of the dataset configuration (for example, `projects/{project-id}/locations/{location-id}/datasetConfigs/{dataset_config_id}`).
     * `BUCKET_FILTER_CEL` is the CEL filter expression for buckets. For example, `name in ['bucket-1', 'bucket-2']`. For details about supported keywords, fields, and operators, see the [CEL filters reference](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).
     * `OBJECT_FILTER_CEL` is the CEL filter expression for objects. For example, `size >= 5000 && name.endsWith('.pdf')`.
     * `snapshotTime` (Optional): A specific UTC timestamp in RFC 3339 format (for example, `"2026-05-03T16:00:00Z"`) specifying which dataset snapshot to use. This snapshot must exist in both your bucket and object dataset views across all target locations. If you specify this field, you must also specify the `targetLocations` field.
     * `targetLocations` (Optional): A JSON object specifying a list of Cloud Storage locations (for example, `["us", "us-central1", "us-east4"]`) to filter the scope of the job. If dependencies are experiencing an outage in specific locations, you can narrow the job to specific locations. If only `targetLocations` is specified and `snapshotTime` is omitted, the job automatically chooses the most recent snapshot timestamp that is successfully populated in both the object and bucket attribute views across all the specified locations.
     * `OBJECT_DELETION_VALUE` is the Boolean that toggles permanent deletion. For example, `true` or `false`.
  3. Send a `POST` request using `cURL` to execute the job:
         
         curl -X POST \
              -H "Authorization: Bearer OAUTH2_TOKEN" \
              -H "Content-Type: application/json" \
              -d @JSON_FILE_NAME \
              "https://storagebatchoperations.googleapis.com/v1/projects/PROJECT_ID/locations/global/jobs?job_id=JOB_NAME"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file.
     * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.
     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.



### Use a manifest file

To get the permissions that you need to create a storage batch operations job, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Create a manifest using Storage Insights datasets

You can create the [manifest](https://docs.cloud.google.com/storage/docs/batch-operations/overview#manifest) for your storage batch operations job by extracting data from BigQuery. To do so, you'll need to [query the linked dataset](https://docs.cloud.google.com/storage/docs/insights/manage-datasets#query-linked-datasets), export the resulting data as a CSV file, and save it to a Cloud Storage bucket. The storage batch operations job can then use this CSV file as its manifest.

Running the following SQL query in BigQuery on a Storage Insights dataset view retrieves objects larger than 1 KiB that are named `Temp_Training`:
    
    
      EXPORT DATA OPTIONS(
       uri=`URI`,
       format=`CSV`,
       overwrite=OVERWRITE_VALUE,
       field_delimiter=',') AS
      SELECT bucket, name, generation
      FROM DATASET_VIEW_NAME
      WHERE bucket = BUCKET_NAME
      AND name LIKE (`Temp_Training%`)
      AND size > 1024 * 1024
      AND snapshotTime = SNAPSHOT_TIME
      

Where:

  * `URI` is the URI to the bucket that contains the manifest. For example, `gs://bucket_name/path_to_csv_file/*.csv`. When you use the `*.csv` wildcard, BigQuery exports the result to multiple CSV files.
  * `OVERWRITE_VALUE` is a boolean value. If set to `true`, the export operation overwrites existing files at the specified location.
  * `DATASET_VIEW_NAME` is the fully qualified name of the Storage Insights dataset view in `PROJECT_ID.DATASET_ID.VIEW_NAME` format. To find the name of your dataset, [view the linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings#view-linked-datasets).

Where:

    * `PROJECT_ID` is the ID or number of the project. For example, `my-project`.
    * `DATASET_ID` is the name of the dataset. For example, `objects-deletion-dataset`.
    * `VIEW_NAME` is the name of the dataset view. For example, `bucket_attributes_view`.
  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.

  * `SNAPSHOT_TIME` is the snapshot time of the Storage Insights dataset view. For example, `2024-09-10T00:00:00Z`.




### Create a storage batch operations job using a manifest file

To create a storage batch operations job to process objects contained in the manifest, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the objects on which you want to perform batch operations.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Click **Create batch operations**.
  4. In the **Select operation** pane, choose the operation type: 
     * **Manage object holds** : Select **Temporary hold** or **Event-based hold**. For more information, see [object holds](https://docs.cloud.google.com/storage/docs/object-holds).
     * **Update object metadata** : To add [object metadata](https://docs.cloud.google.com/storage/docs/metadata), do the following: 
       * To add custom metadata, complete the following steps: 
         1. In the **Key** field, enter a key name.
         2. In the **Value** field, enter a value for that key.
         3. Optional: Click **\+ Add item** to add more key-value pairs.
       * To update fixed-key metadata, complete the following steps: 
         1. To expand the **Update fixed-key metadata** section, click the expand_moreexpander arrow.
         2. In the **Select one or more metadata to update** list, select metadata items to edit.
     * **Update/Rotate encryption key** : To use or update [the encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for objects, do the following: 
       1. In the **Select a Cloud KMS key** list, select a customer-managed encryption key (CMEK).
       2. Optional: Select **Switch project** to pick a key from another project or select **Enter key manually** to fill details.
     * **Delete objects** : To [delete objects](https://docs.cloud.google.com/storage/docs/object-deletion-overview), do the following: 
       1. [Check whether Object Versioning is enabled](https://docs.cloud.google.com/storage/docs/using-object-versioning#check).
       2. If Object Versioning is enabled, choose one of the following deletion options:

          * Select **Delete all versions of the objects** to remove both live and noncurrent versions.
          * Select **Permanently delete live versions** to remove only the live version.

If Object Versioning is not enabled, any objects selected for deletion are permanently deleted.

**Warning:** Accidental object deletion carries a risk of data loss. Enable soft delete to recover accidental object deletions. 
  5. Click **Next**.
  6. In the **Name operation & specify objects** pane, do the following: 
     1. In the **Name** field, enter a name.
     2. Optional: In the **Description** field, enter a description.
     3. In the **Specify objects** section, select **Upload lists of objects using manifest CSV files** , and then do the following: 

        1. Upload your manifest CSV file to a bucket. This file must contain headers for **Bucket name** , **Object key** , and **Generation number**.
        2. In the **Select manifest file mode** list, choose one of the following options: 
           * If you select **Select a manifest file from Cloud Storage** , click **Browse** in the **Select a manifest file from Cloud Storage** field. In the **Select object** dialog that appears, navigate to your manifest CSV file, then click **Select**.
           * If you select **Select multiple manifest files using wildcard** , enter the file path in the **Enter manifest file location using wildcard** field. For example, `bucket-name/folder/manifest_*`.
  7. Click **Create**.



### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage batch-operations jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create) command:
         
         gcloud storage batch-operations jobs create \
         JOB_NAME \
         {--bucket=SOURCE_BUCKET | --bucket-list=SOURCE_BUCKET_LIST} \
         --manifest-location=URI \
         JOB_TYPE_FLAG

Where:

     * `JOB_NAME` is the [name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name) of the storage batch operations job.

     * `SOURCE_BUCKET` is the name of the bucket that contains the objects you want to process. For example, `my-bucket`.

     * `SOURCE_BUCKET_LIST` is a comma-separated list of one or more bucket names that contain the objects you want to process. For example, `bucket1,bucket2`.

     * `URI` is the URI to the bucket that contains the manifest. For example, `gs://bucket_name/path_to_csv_file/*.csv`. When you use the `*.csv` wildcard, BigQuery exports the result to multiple CSV files.

     * `JOB_TYPE_FLAG` is one of the following flags, depending on the [job type](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type).

       * `--delete-object`: Delete one or more objects.

       * `--put-metadata`: Update [object metadata](https://docs.cloud.google.com/storage/docs/batch-operations/overview#metadata-updates). Object metadata is stored as key-value pairs. Specify the key-value pair for the metadata you want to modify. You can specify one or more key-value pairs as a list. You can also provide [object retention configurations](https://docs.cloud.google.com/storage/docs/object-lock) using the `--put-metadata` flag.

       * `--rewrite-object`: Update the [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for one or more objects. You can also use this flag to change the object's storage class by specifying the `storage-class` key. Supported storage classes include `STANDARD`, `NEARLINE`, `COLDLINE`, and `ARCHIVE`. For example: `--rewrite-object=storage-class=NEARLINE`.

       * `--set-object-acls-from-file`: Patch object access control lists (ACLs). Provide the path to a JSON or YAML file with grants to add or update for entities such as `allUsers` or `allAuthenticatedUsers`. For example: `--set-object-acls-from-file=acl-updates.yaml`.

       * `--put-object-event-based-hold`: Enable event-based [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--no-put-object-event-based-hold`: Disable event-based [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--put-object-temporary-hold`: Enable temporary [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--no-put-object-temporary-hold`: Disable temporary [object holds](https://docs.cloud.google.com/storage/docs/object-holds).

       * `--clear-all-object-custom-contexts`: Delete all existing [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

The following example shows how to create a job to clear all object contexts for objects listed in `manifest.csv`:
             
             gcloud storage batch-operations jobs create my-job \
             --bucket=my-bucket \
             --manifest-location=gs://my-bucket/manifest.csv \
             --clear-all-object-custom-contexts

**Caution:** Clearing all object contexts deletes all the existing contexts on the object. To preserve the previous object contexts, enable [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). The logs contain contexts from before the update, which you can use to restore previous values.
       * `--clear-object-custom-contexts`: Remove contexts with specific keys. You can also update specific contexts along with removing keys by using both the `--clear-object-custom-contexts` flag and one of the following flags:

         * `--update-object-custom-contexts`: Provide a map of key-value pairs.

The following example shows how to create a job to remove the context with key `temp-id` and update or insert context with key `project-id` and `cost-center` for all objects listed in `manifest.csv`:
               
               gcloud storage batch-operations jobs create my-job \
               --bucket=my-bucket \
               --manifest-location=gs://my-bucket/manifest.csv \
               --clear-object-custom-contexts=temp-id \
               --update-object-custom-contexts=project-id=project-A,cost-center=engineering

**Note:** You can't specify the same key in both the `--clear-object-custom-contexts` flag and the `--update-object-custom-contexts` flag. Doing so results in an `INVALID_ARGUMENT` error.
         * `--update-object-custom-contexts-file`: Provide the path to a JSON or YAML file with key-value pairs.

The following example shows how to create a job to process objects defined in `manifest.csv`. The job does the following:

           * Removes all contexts with the `temp-id` key.

           * Updates existing contexts with the `project-id` and `cost-center` keys defined in the `/tmp/context_updates.json` file.
    
    gcloud storage batch-operations jobs create my-job \
    --bucket=my-bucket \
    --manifest-location=gs://my-bucket/manifest.csv \
    --clear-object-custom-contexts=temp-id \
    --update-object-custom-contexts-file=/tmp/context_updates.json

Where `/tmp/context_updates.json` contains the following object contexts:
    
    {
    "project-id": {"value": "project-A"},
    "cost-center": {"value": "engineering"}
    }




## Integration with VPC Service Controls

VPC Service Controls provides an additional layer of security for storage batch operations resources. By placing projects within a service perimeter, you help protect resources and services from requests that originate from outside the perimeter. To learn more about VPC Service Controls service perimeter details for storage batch operations, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage_batch_operations).

## Use Cloud Audit Logs for storage batch operations jobs

Storage batch operations jobs record transformations on Cloud Storage objects in Cloud Audit Logs for Cloud Storage. Use [Cloud Audit Logs with Cloud Storage](https://docs.cloud.google.com/storage/docs/audit-logging) to track these transformations. For details on how to enable audit logs, see [Enabling audit logs](https://docs.cloud.google.com/storage/docs/audit-logging#settings). In the audit log entry, a `callUserAgent` metadata field with the value `StorageBatchOperations` indicates that the transformation was performed by storage batch operations.

## Next steps

  * Learn about [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
