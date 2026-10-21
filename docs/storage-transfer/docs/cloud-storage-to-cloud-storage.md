---
url: https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage/
title: Transfer between Cloud Storage buckets \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:48.662070+00:00
---

# Transfer between Cloud Storage buckets  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer between Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can be used to transfer large amounts of data between Cloud Storage buckets, either within the same Google Cloud project, or between different projects.

Bucket migrations are useful in a number of scenarios. They can be used to consolidate data from separate projects, to move data into a backup location, or to change the location of your data.

## When to use Storage Transfer Service

Google Cloud offers multiple options to transfer data between Cloud Storage buckets. We recommend the following guidelines:

  * Transferring less than 1 TB: Use `gcloud`. For instructions, refer to [Move and rename buckets](https://docs.cloud.google.com/storage/docs/moving-buckets#move-buckets-gcloud).

  * Transferring more than 1 TB: Use Storage Transfer Service. Storage Transfer Service is a managed transfer option that provides out of the box security, reliability, and performance. It eliminates the need to optimize and maintain scripts, and handle retries.




This guide discusses best practices when transferring data between Cloud Storage buckets using Storage Transfer Service.

## Define a transfer strategy

What your transfer strategy looks like depends on the complexity of your situation. Make sure to include the following considerations in your plan.

### Choose a bucket name

To move your data to a storage bucket with a different location, choose one of the following approaches:

  * **New bucket name.** Update your applications to point to a storage bucket with a different name.
  * **Keep bucket name.** Replace your storage bucket to keep the current name, meaning you don't need to update your applications.



In both cases you should plan for downtime, and give your users suitable notice that downtime is coming. Review the following explanations to understand which choice is best for you.

#### New bucket name

With a new bucket name, you need to update all code and services that use your current bucket. How you do this depends on how your applications are built and deployed.

For certain setups this approach might have less downtime, but requires more work to ensure a smooth transition. It involves the following steps:

  1. Copying your data to a new storage bucket.
  2. Starting your downtime.
  3. Updating your applications to point to the new bucket.
  4. Verifying that everything works as expected, and that all relevant systems and accounts have access to the bucket.
  5. Deleting the original bucket.
  6. Ending your downtime.



#### Keep bucket name

Use this approach if you prefer not to change your code to point to a new bucket name. It involves the following steps:

  1. Copying your data to a temporary storage bucket.
  2. Starting your downtime.
  3. Deleting your original bucket.
  4. Creating a new bucket with the same name as your original bucket.
  5. Copying the data to your new bucket from the temporary bucket.
  6. Deleting the temporary bucket.
  7. Verifying that everything works as expected, and that all relevant systems and accounts have access to the bucket.
  8. Ending your downtime.

**Caution:** Bucket names must be [globally unique](https://cloud.google.com/storage/docs/buckets#naming). There's a risk that someone else could take the bucket name that you need after you delete your old bucket, but before you create your new one. Make sure to create the new bucket immediately after deleting the old one.

### Minimize downtime

Storage Transfer Service does not lock reads or writes on the source or destination buckets during a transfer.

If you choose to manually lock reads/writes on your bucket, you can minimize downtime by transferring your data in two steps: seed, and sync.

  1. **Seed transfer** : Perform a bulk transfer without locking read/write on the source.

  2. **Sync transfer** : After the first run is complete, lock the read/write on the source bucket and perform another transfer. Storage Transfer Service transfers are incremental by default, so this second transfer only transfers data that changed during the seed transfer.




### Optimize the transfer speed

When estimating how long a transfer job takes, consider the possible bottlenecks. For example, if the source has billions of small files, then your transfer speed is going to be QPS-bound. If object sizes are large, bandwidth might be the bottleneck.

Bandwidth limits are set at the region level and are fairly allocated across all projects. If sufficient bandwidth is available, Storage Transfer Service can complete around 1000 tasks per transfer job per second. You can accelerate a transfer in this case by splitting your job into multiple small transfer jobs, for example by using [include and exclude prefixes](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) to transfer certain files.

In cases where the location, storage class, and encryption key are the same, Storage Transfer Service does not create a new copy of the bytes; it instead creates a new metadata entry that points to the source blob. As a result, same location and class copies of a large corpus are completed very quickly and are only QPS-bound.

Deletes are also metadata-only operations. For these transfers, parallelizing the transfer by splitting it into multiple small jobs can increase the speed.

### Preserve metadata

The following object metadata is preserved when transferring data between Cloud Storage buckets with Storage Transfer Service:

  * User-created [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata).
  * Cloud Storage fixed-key metadata fields, such as Cache-Control, Content-Disposition, Content-Type, and Custom-Time.
  * Object size.
  * [Generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) is preserved as a custom metadata field with the key `x-goog-reserved-source-generation`, which you can edit later or remove.



The following metadata fields can optionally be preserved when transferring using the API:

  * ACLs (`acl`)
  * Storage class (`storageClass`)
  * CMEK (`kmsKey`)
  * Temporary hold (`temporaryHold`)
  * Object creation time (`customTime`)



Refer to the [`TransferSpec` API reference](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#metadataoptions) for more details.

The following metadata fields aren't preserved:

  * Last updated time (`updated`)
  * `etag`
  * `componentCount`



If preserved, object creation time is stored as a custom field, `customTime`. The object's `updated` time is reset upon transfer, so the object's time spent in its storage class is also reset. This means an object in Coldline Storage, post-transfer, has to exist again for 90 days at the destination to avoid early deletion charges.

You can apply your `createTime`-based lifecycle policies using `customTime`. Existing `customTime` values are overwritten.

For more details on what is and isn't preserved, refer to [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation).

### Handle versioned objects

If you want to transfer all versions of your storage objects and not just the latest, you can use Storage Transfer Service's [manifest feature](https://docs.cloud.google.com/storage-transfer/docs/manifest#manifest_of_objects).

To transfer all object versions:

  1. List the bucket objects and copy them into a JSON file:
         
         gcloud storage ls --all-versions --recursive --json [SOURCE_BUCKET] > object-listing.json
         

This command typically lists around 1k objects per second.

  2. Copy the non-current objects into a CSV file:
         
         jq -r '.[] | select( .type=="cloud_object" and (.metadata | has("timeDeleted"))) | [.metadata.name, .metadata.generation] | @csv' object-listing.json > non-current-object-manifest.csv
         

  3. [Enable object versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning#set) on the destination bucket.

  4. Transfer the non-current versions with the following transfer options:

     * [Specify the manifest file](https://docs.cloud.google.com/storage-transfer/docs/manifest#start_a_transfer_with_the_manifest_specified).
     * Choose to always overwrite objects in the sink (`OVERWRITE_WHEN=always`). Note that this can in rare cases create duplicate versions of a file.
     * Preserve the `timeCreated` metadata (`MetdataOptions.timeCreated=TIME_CREATED_PRESERVE_AS_CUSTOM_TIME`).
  5. Transfer the live versions using a regular transfer job.




### Configure transfer options

Some of the options available to you when setting up your transfer are as follows:

  * [Logging](https://docs.cloud.google.com/storage-transfer/docs/configure-transfer-logs): Cloud Logging provides detailed logs of individual objects, allowing you to verify transfer status and to perform additional data integrity checks.

  * [Filtering](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers): You can use include and exclude prefixes to limit which objects Storage Transfer Service operates on. This option can be used to split a transfer into multiple transfer jobs so that they can run in parallel. See Optimize the transfer speed for more information.

  * [Transfer options](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions): You can configure your transfer to overwrite existing items in the destination bucket; to delete objects in the destination that don't exist in the transfer set; or to delete transferred objects from the source.




## Transfer your data

After you've defined your transfer strategy, you can perform the transfer itself.

### Create a new bucket

Before beginning the transfer, [create a storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-cli). See [location_considerations](https://docs.cloud.google.com/storage/docs/locations#considerations) for help choosing an appropriate bucket location.

You might wish to copy over some of the [bucket metadata](https://docs.cloud.google.com/storage/docs/bucket-metadata) when you create the new bucket. See [Get bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata) to learn how to display the source bucket's metadata, so that you can apply the same settings to your new bucket.

### Copy objects to the new bucket

You can copy objects from the source bucket to a new bucket using the Google Cloud console, the `gcloud` CLI, REST API, or client libraries. Which approach you choose depends on your transfer strategy.

The following instructions are for the basic use case of transferring objects from one bucket to another, and should be modified to fit your needs.

Don't include sensitive information such as personally identifiable information (PII) or security data in your transfer job name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

###  Google Cloud console 

Use the [Cloud Storage Transfer Service](https://docs.cloud.google.com/storage-transfer) from within Google Cloud console:

  1. Open the Transfer page in the Google Cloud console.

[Open the **Transfer** page](https://console.cloud.google.com/transfer/jobs)

  2. Click **Create transfer job**.
  3. Follow the step-by-step walkthrough, clicking **Next step** as you complete each step:

     * Get started: Use **Google Cloud Storage** as both your **Source Type** and **Destination Type**.

     * Choose a source: Either enter the name of the wanted bucket directly, or click **Browse** to find and select the bucket you want.

     * Choose a destination: Either enter the name of the wanted bucket directly, or click **Browse** to find and select the bucket you want.

     * Choose settings: Select the option **Delete files from source after they're transferred**.

     * Scheduling options: You can ignore this section.

  4. After you complete the step-by-step walkthrough, click **Create**.

This begins the process of copying objects from your old bucket into your new one. This process may take some time; however, after you click **Create** , you can navigate away from the Google Cloud console.

To view the transfer's progress: 

Open the Transfer page in the Google Cloud console.

[Open the **Transfer** page](https://console.cloud.google.com/transfer/jobs)

To learn how to get detailed error information about failed Storage Transfer Service operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

  5. After the transfer completes, you don't need to do anything to delete the objects from your old bucket if you selected the **Delete source objects after the transfer completes** checkbox during setup. You may, however, want to also [delete your old bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets), which you must do separately.




###  gcloud CLI 

### Install the gcloud CLI

If you haven't already, [install the gcloud command-line tool](https://docs.cloud.google.com/sdk/docs/install).

Then, call `gcloud init` to initialize the tool and to specify your project ID and user account. See [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize) for more details.
    
    
    gcloud init
    

### Add the service account to your destination folder

You must add the Storage Transfer Service service account to your destination bucket before creating a transfer. To do so, use `gcloud storage buckets add-iam-policy-binding`:
    
    
    gcloud storage buckets add-iam-policy-binding gs://bucket_name \
    --member=serviceAccount:project-12345678@storage-transfer-service.iam.gserviceaccount.com \
    --role=roles/storage.admin
    

For instructions using the Google Cloud console or API, refer to [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) in the Cloud Storage documentation.

### Create the transfer job

To create a new transfer job, use the `gcloud transfer jobs create` command. Creating a new job initiates the specified transfer, unless a schedule or `--do-not-run` is specified.
    
    
    gcloud transfer jobs create SOURCE DESTINATION
    

Replace the following:

  * SOURCE is the data source for this transfer, in the format `gs://BUCKET_NAME`.

  * DESTINATION is your new bucket, in the form `gs://BUCKET_NAME`.




Additional options include:

  * **Job information** : You can specify `--name` and `--description`.

  * **Schedule** : Specify `--schedule-starts`, `--schedule-repeats-every`, and `--schedule-repeats-until`, or `--do-not-run`.

  * **Object conditions** : Use conditions to determine which objects are transferred. These include `--include-prefixes` and `--exclude-prefixes`, and the time-based conditions in `--include-modified-[before | after]-[absolute | relative]`.

  * **Transfer options** : Specify whether to overwrite destination files (`--overwrite-when=different` or `always`) and whether to delete certain files during or after the transfer (`--delete-from=destination-if-unique` or `source-after-transfer`); specify which [metadata values to preserve](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--preserve-metadata) (`--preserve-metadata`); and optionally set a storage class on transferred objects (`--custom-storage-class`).

  * **Notifications** : Configure [Pub/Sub notifications for transfers](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer) with `--notification-pubsub-topic`, `--notification-event-types`, and `--notification-payload-format`.




To view all options, run `gcloud transfer jobs create --help`.

For example, to transfer all objects with the prefix `folder1`:
    
    
    gcloud transfer jobs create gs://old-bucket gs://new-bucket \
      --include-prefixes="folder1/"
    

###  REST 

In this example, you'll learn how to move files from one Cloud Storage bucket to another. For example, you can move data to a bucket in another [location](https://docs.cloud.google.com/storage/docs/bucket-locations).

**Note:** The process is the same if the bucket is located in a different project.

Request using [transferJobs create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create):
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
      "description": "YOUR DESCRIPTION",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "schedule": {
          "scheduleStartDate": {
              "day": 1,
              "month": 1,
              "year": 2025
          },
          "startTimeOfDay": {
              "hours": 1,
              "minutes": 1
          },
          "scheduleEndDate": {
              "day": 1,
              "month": 1,
              "year": 2025
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
          }
      }
    }

Response:
    
    
    200 OK
    {
      "transferJob": [
          {
              "creationTime": "2015-01-01T01:01:00.000000000Z",
              "description": "YOUR DESCRIPTION",
              "name": "transferJobs/JOB_ID",
              "status": "ENABLED",
              "lastModificationTime": "2015-01-01T01:01:00.000000000Z",
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
                      "bucketName": "GCS_SOURCE_NAME",
                  },
                  "gcsDataSink": {
                      "bucketName": "GCS_NEARLINE_SINK_NAME"
                  },
                  "objectConditions": {
                      "minTimeElapsedSinceLastModification": "2592000.000s"
                  },
                  "transferOptions": {
                      "deleteObjectsFromSourceAfterTransfer": true
                  }
              }
          }
      ]
    }

###  Client libraries 

In this example, you'll learn how to move files from one Cloud Storage bucket to another. For example, you can replicate data to a bucket in another [location](https://docs.cloud.google.com/storage/docs/bucket-locations).

**Note:** The process is the same if the bucket is located in a different project.

For more information about the Storage Transfer Service client libraries, see [Getting started with Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/libraries).

### Java

Looking for older samples? See the [Storage Transfer Service Migration Guide](https://docs.cloud.google.com/storage-transfer/docs/reference/migration-guide). 
    
    
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).[CreateTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.CreateTransferJobRequest.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[ObjectConditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[Schedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).Status;
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html);
    import com.google.type.[Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html);
    import com.google.type.[TimeOfDay](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html);
    import java.io.IOException;
    import java.util.Calendar;
    
    public class TransferToNearline {
      /**
       * Creates a one-off transfer job that transfers objects in a standard GCS bucket that are more
       * than 30 days old to a Nearline GCS bucket.
       */
      public static void transferToNearline(
          String projectId,
          String jobDescription,
          String gcsSourceBucket,
          String gcsNearlineSinkBucket,
          long startDateTime)
          throws IOException {
    
        // Your Google Cloud Project ID
        // String projectId = "your-project-id";
    
        // A short description of this job
        // String jobDescription = "Sample transfer job of old objects to a Nearline GCS bucket.";
    
        // The name of the source GCS bucket to transfer data from
        // String gcsSourceBucket = "your-gcs-source-bucket";
    
        // The name of the Nearline GCS bucket to transfer old objects to
        // String gcsSinkBucket = "your-nearline-gcs-bucket";
    
        // What day and time in UTC to start the transfer, expressed as an epoch date timestamp.
        // If this is in the past relative to when the job is created, it will run the next day.
        // long startDateTime =
        //     new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2000-01-01 00:00:00").getTime();
    
        // Parse epoch timestamp into the model classes
        Calendar startCalendar = Calendar.getInstance();
        startCalendar.setTimeInMillis(startDateTime);
        // Note that this is a Date from the model class package, not a java.util.Date
        [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) date =
            [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html).newBuilder()
                .setYear(startCalendar.get(Calendar.YEAR))
                .setMonth(startCalendar.get(Calendar.MONTH) + 1)
                .setDay(startCalendar.get(Calendar.DAY_OF_MONTH))
                .build();
        [TimeOfDay](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html) time =
            [TimeOfDay](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html).newBuilder()
                .setHours(startCalendar.get(Calendar.HOUR_OF_DAY))
                .setMinutes(startCalendar.get(Calendar.MINUTE))
                .setSeconds(startCalendar.get(Calendar.SECOND))
                .build();
    
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
            [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).newBuilder()
                .setDescription(jobDescription)
                .setProjectId(projectId)
                .setTransferSpec(
                    [TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html).newBuilder()
                        .setGcsDataSource([GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(gcsSourceBucket))
                        .setGcsDataSink([GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(gcsNearlineSinkBucket))
                        .setObjectConditions(
                            [ObjectConditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.html).newBuilder()
                                .[setMinTimeElapsedSinceLastModification](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_ObjectConditions_Builder_setMinTimeElapsedSinceLastModification_com_google_protobuf_Duration_)(
                                    [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(2592000 /* 30 days */)))
                        .setTransferOptions(
                            [TransferOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.html).newBuilder().[setDeleteObjectsFromSourceAfterTransfer](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferOptions_Builder_setDeleteObjectsFromSourceAfterTransfer_boolean_)(true)))
                .[setSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferJob_Builder_setSchedule_com_google_storagetransfer_v1_proto_TransferTypes_Schedule_)([Schedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.html).newBuilder().[setScheduleStartDate](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_Schedule_Builder_setScheduleStartDate_com_google_type_Date_)(date).[setStartTimeOfDay](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_Schedule_Builder_setStartTimeOfDay_com_google_type_TimeOfDay_)(time))
                .setStatus(Status.ENABLED)
                .build();
    
        // Create a Transfer Service client
        [StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html).create();
    
        // Create the transfer job
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response =
            storageTransfer.[createTransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html#com_google_storagetransfer_v1_proto_StorageTransferServiceClient_createTransferJob_com_google_storagetransfer_v1_proto_TransferProto_CreateTransferJobRequest_)(
                CreateTransferJobRequest.newBuilder().setTransferJob(transferJob).build());
    
        System.out.println("Created transfer job from standard bucket to Nearline bucket:");
        System.out.println(response.toString());
      }
    }

### Python

Looking for older samples? See the [Storage Transfer Service Migration Guide](https://docs.cloud.google.com/storage-transfer/docs/reference/migration-guide). 
    
    
    from datetime import datetime
    
    from google.cloud import storage_transfer
    from google.protobuf.duration_pb2 import Duration
    
    
    def create_daily_nearline_30_day_migration(
        project_id: str,
        description: str,
        source_bucket: str,
        sink_bucket: str,
        start_date: datetime,
    ):
        """Create a daily migration from a GCS bucket to a Nearline GCS bucket
        for objects untouched for 30 days."""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project-id'
    
        # A useful description for your transfer job
        # description = 'My transfer job'
    
        # Google Cloud Storage source bucket name
        # source_bucket = 'my-gcs-source-bucket'
    
        # Google Cloud Storage destination bucket name
        # sink_bucket = 'my-gcs-destination-bucket'
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "schedule": {
                        "schedule_start_date": {
                            "day": start_date.day,
                            "month": start_date.month,
                            "year": start_date.year,
                        }
                    },
                    "transfer_spec": {
                        "gcs_data_source": {
                            "bucket_name": source_bucket,
                        },
                        "gcs_data_sink": {
                            "bucket_name": sink_bucket,
                        },
                        "object_conditions": {
                            "min_time_elapsed_since_last_modification": Duration(
                                seconds=2592000  # 30 days
                            )
                        },
                        "transfer_options": {
                            "delete_objects_from_source_after_transfer": True
                        },
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

### Verify copied objects

After your transfer is complete, we recommend performing additional data integrity checks.

  * Validate that the objects were copied correctly, by verifying the metadata on the objects, such as checksums and size.

  * Verify that the correct version of the objects were copied. Storage Transfer Service offers an out-of-the-box option to verify that objects are copies. If you've enabled [logging](https://docs.cloud.google.com/storage-transfer/docs/configure-transfer-logs), [view logs](https://docs.cloud.google.com/storage-transfer/docs/read-transfer-logs#view-logs) to verify whether all the objects were successfully copied, including their corresponding metadata fields.




### Start using the destination bucket

After the migration is complete and verified, update any existing applications or workloads so that they use the target bucket name. Check [data access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) in [Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/audit-logging) to ensure that your operations are correctly modifying and reading objects.

### Delete the original bucket

After everything is working well, [delete the original bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

Storage Transfer Service offers the option of deleting objects after they have been transferred by specifying `deleteObjectsFromSourceAfterTransfer: true` in the job configuration, or selecting the option in the Google Cloud console.

#### Schedule object deletion

To schedule the deletion of your objects at a later date, use a combination of a [scheduled transfer job](https://docs.cloud.google.com/storage-transfer/docs/schedule-transfer-jobs), and the [`deleteObjectsUniqueInSink = true`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#TransferOptions) option.

The transfer job should be set up to transfer an empty bucket into the bucket containing your objects. This causes Storage Transfer Service to list the objects and begin deleting them. As deletions are a metadata-only operation, the transfer job is only QPS-bound. To speed up the process, split the transfer into multiple jobs, each acting on a distinct set of prefixes.

Alternatively, Google Cloud offers a [managed cron job scheduler](https://docs.cloud.google.com/scheduler). For more information, see [Schedule Google Cloud STS Transfer Job with Cloud Scheduler](https://medium.com/@bambang20/schedule-google-cloud-sts-transfer-job-with-cloud-scheduler-7e25e9943e4e).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
