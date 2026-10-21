---
url: https://docs.cloud.google.com/storage-transfer/docs/event-driven-google/
title: Event-driven transfers from Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:45.278128+00:00
---

# Event-driven transfers from Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/event-driven-google/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Event-driven transfers from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can listen to event notifications in Google Cloud to automatically transfer data that has been added or updated in a Cloud Storage bucket. [Learn more](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) about the benefits of event-driven transfers.

Event-driven transfers from Cloud Storage use Pub/Sub notifications to know when objects in the source bucket have been modified or added. Object deletions are not detected; deleting an object at the source does not delete the associated object in the destination bucket.

Event-driven transfers always use a Cloud Storage bucket as the destination.

## Configure permissions

In addition to the [permissions required for all transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#permissions), event-driven transfers require the `Pub/Sub Subscriber` role.

  1. Find the name of the Storage Transfer Service service agent for your project:

     1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

An interactive panel opens, titled **Try this method**.

     2. In the panel, under **Request parameters** , enter your project ID. The project you specify here must be the project you're using to manage Storage Transfer Service, which might be different from the source bucket's project.

     3. Click **Execute**.

Your service agent's email is returned as the value of `accountEmail`. Copy this value.

The service agent's email uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

  2. Grant the `Pub/Sub Subscriber` role to the Storage Transfer Service service agent.

###  Cloud console 

Follow the instructions in [Controlling access through the Google Cloud console](https://docs.cloud.google.com/pubsub/docs/access-control#console) to grant the `Pub/Sub Subscriber` role to the Storage Transfer Service service. The role can be granted at the topic, subscription, or project level.

###  `gcloud` CLI 

Follow the instructions in [Set a policy](https://docs.cloud.google.com/pubsub/docs/access-control#set-policy) to add the following binding:
         
         {
           "role": "roles/pubsub.subscriber",
           "members": [
             "serviceAccount:project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com"
         }




## Configure Pub/Sub

  1. Make sure that you've satisfied the [Prerequisites](https://docs.cloud.google.com/storage/docs/reporting-changes#prereqs) for using Pub/Sub with Cloud Storage.

  2. Create a Pub/Sub notification for the source Cloud Storage bucket.

You cannot manage Pub/Sub notifications with the Google Cloud console. Use the gcloud CLI or [one of the available client libraries](https://docs.cloud.google.com/storage/docs/reporting-changes#enabling) instead.
         
         gcloud storage buckets notifications create gs://SOURCE_BUCKET_NAME --topic=TOPIC_NAME

  3. Create a pull subscription for the topic. You must create a separate subscription for each transfer job.

The following example shows the Google Cloud CLI command to create a pull subscription. For console instructions and client library code, see [Create a pull subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription).
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID --topic=TOPIC_NAME --ack-deadline=300




## Create a transfer job

You can use the Google Cloud console, Google Cloud CLI, or REST API to create an event-based transfer job.

Don't include sensitive information such as personally identifiable information (PII) or security data in your transfer job name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

###  Cloud console 

  1. Go to the **Create transfer job** page in the Google Cloud console.

[Go to **Create transfer job**](https://console.cloud.google.com/transfer/create)

  2. Select **Cloud Storage** as both the source and the destination.

  3. As the **Scheduling mode** select **Event-driven** and click **Next step**.

  4. Select the source bucket for this transfer.

  5. In the **Event stream** section, enter the subscription name:

`projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID`

  6. Optionally, define any filters, then click **Next step**.

  7. Select the destination bucket for this transfer.

  8. Optionally, enter a start and end time for the transfer. If you don't specify a time, the transfer will start immediately and will run until [manually stopped](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#disable-transfer-job).

  9. Specify any transfer options. More information is available from the [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) page.

  10. Click **Create**.




Once created, the transfer job starts running and an event listener waits for notifications on the Pub/Sub subscription. The job details page shows one operation each hour, and includes details on data transferred for each job.

###  gcloud 

To create an event-driven transfer job using the Google Cloud CLI, use the `gcloud transfer jobs create` command with the `--event-stream-name` flag:
    
    
    gcloud transfer jobs create \
      gs://SOURCE_BUCKET \
      gs://DESTINATION_BUCKET \
      --event-stream-name=projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID \
      --event-stream-starts=EVENT_STREAM_STARTS \
      --event-stream-expires=EVENT_STREAM_EXPIRES
    

Replace the placeholders with your actual values:

  * SOURCE_BUCKET: The name of your source Cloud Storage bucket.
  * DESTINATION_BUCKET: Your destination Cloud Storage bucket.
  * PROJECT_NAME: The project that contains the Pub/Sub subscription.
  * SUBSCRIPTION_ID: The ID of the Pub/Sub subscription you created (e.g., `my-subscription`).
  * EVENT_STREAM_STARTS: When to start listening for events using the %Y-%m-%dT%H:%M:%S%z datetime format (e.g., `2020-04-12T06:42:12+04:00`). If not set, the job starts running and listening for events upon the successful submission of the create job command.
  * EVENT_STREAM_EXPIRES: When to stop listening for events. If not set, the job continues until manually stopped.



For a full list of supported fields, refer to the [`gcloud transfer jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create) reference.

###  REST 

To create an event-driven transfer using the REST API, send the following JSON object to the [transferJobs.create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create) endpoint:
    
    
    transfer_job {
      "description": "YOUR DESCRIPTION",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec" {
        "gcsDataSource" {
          "bucketName": "GCS_SOURCE_NAME"
        },
        "gcsDataSink": {
            "bucketName": "GCS_SINK_NAME"
        }
      }
      "eventStream" {
        "name": "projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID",
        "eventStreamStartTime": "2022-12-02T01:00:00+00:00",
        "eventStreamExpirationTime": "2023-01-31T01:00:00+00:00"
      }
    }

The `eventStreamStartTime` and `eventStreamExpirationTime` are optional. If the start time is omitted, the transfer starts immediately; if the end time is omitted, the transfer continues until manually stopped.

###  Client libraries 

### Go

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storagetransfer@v1.0.0/apiv1). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func createEventDrivenGCSTransfer(w io.Writer, projectID string, gcsSourceBucket string, gcsSinkBucket string, pubSubId string) (*storagetransferpb.TransferJob, error) {
    	// Your Google Cloud Project ID.
    	// projectID := "my-project-id"
    
    	// The name of the source GCS bucket.
    	// gcsSourceBucket := "my-source-bucket"
    
    	// The name of the GCS bucket to transfer objects to.
    	// gcsSinkBucket := "my-sink-bucket"
    
    	// The Pub/Sub topic to subscribe the event driven transfer to.
    	// pubSubID := "projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID"
    
    	ctx := context.Background()
    	client, err := storagetransfer.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storagetransfer.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &storagetransferpb.CreateTransferJobRequest{
    		TransferJob: &storagetransferpb.TransferJob{
    			ProjectId: projectID,
    			TransferSpec: &storagetransferpb.TransferSpec{
    				DataSource: &storagetransferpb.TransferSpec_GcsDataSource{
    					GcsDataSource: &storagetransferpb.GcsData{BucketName: gcsSourceBucket}},
    				DataSink: &storagetransferpb.TransferSpec_GcsDataSink{
    					GcsDataSink: &storagetransferpb.GcsData{BucketName: gcsSinkBucket}},
    			},
    			EventStream: &storagetransferpb.EventStream{Name: pubSubId},
    			Status:      storagetransferpb.TransferJob_ENABLED,
    		},
    	}
    	resp, err := client.CreateTransferJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("failed to create transfer job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created an event driven transfer job from %v to %v subscribed to %v with name %v", gcsSourceBucket, gcsSinkBucket, pubSubId, resp.Name)
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html);
    
    public class CreateEventDrivenGcsTransfer {
      public static void main(String[] args) throws Exception {
        // Your Google Cloud Project ID
        String projectId = "your-project-id";
    
        // The name of the GCS AWS bucket to transfer data from
        String gcsSourceBucket = "your-gcs-source-bucket";
    
        // The name of the GCS bucket to transfer data to
        String gcsSinkBucket = "your-gcs-sink-bucket";
    
        // The ARN of the PubSub queue to subscribe to
        String sqsQueueArn = "projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID";
    
        createEventDrivenGcsTransfer(projectId, gcsSourceBucket, gcsSinkBucket, sqsQueueArn);
      }
    
      public static void createEventDrivenGcsTransfer(
          String projectId, String gcsSourceBucket, String gcsSinkBucket, String pubSubId)
          throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources,
        // or use "try-with-close" statement to do this automatically.
        try ([StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html).create()) {
    
          [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferJob.newBuilder()
                  .setProjectId(projectId)
                  .setTransferSpec(
                      [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferSpec.newBuilder()
                          .setGcsDataSource(
                              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).GcsData.newBuilder().setBucketName(gcsSourceBucket))
                          .setGcsDataSink(
                              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).GcsData.newBuilder().setBucketName(gcsSinkBucket)))
                  .setStatus([TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferJob.Status.ENABLED)
                  .[setEventStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferJob_Builder_setEventStream_com_google_storagetransfer_v1_proto_TransferTypes_EventStream_)([TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).EventStream.newBuilder().setName(pubSubId).build())
                  .build();
    
          [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response =
              storageTransfer.createTransferJob(
                  [TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).CreateTransferJobRequest.newBuilder()
                      .setTransferJob(transferJob)
                      .build());
    
          System.out.println(
              "Created a transfer job between from "
                  + gcsSourceBucket
                  + " to "
                  + gcsSinkBucket
                  + " subscribed to "
                  + pubSubId
                  + " with name "
                  + response.getName());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Node.js API reference documentation](https://googleapis.dev/nodejs/storagetransfer/latest/index.html). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {
      StorageTransferServiceClient,
    } = require('[@google-cloud/storage-transfer](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of the Google Cloud Platform Project that owns the job
    // projectId = 'my-project-id'
    
    // Google Cloud Storage source bucket name
    // gcsSourceBucket = 'my-gcs-source-bucket'
    
    // Google Cloud Storage destination bucket name
    // gcsSinkBucket = 'my-gcs-destination-bucket'
    
    // The subscription ID to a Pubsub queue to track
    // pubsubId = 'projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID'
    
    // Creates a client
    const client = new [StorageTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)();
    
    /**
     * Creates an event driven transfer that tracks a Pubsub subscription.
     */
    async function createEventDrivenGcsTransfer() {
      const [transferJob] = await client.createTransferJob({
        transferJob: {
          projectId,
          status: '[ENABLED](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)',
          transferSpec: {
            gcsDataSource: {
              bucketName: gcsSourceBucket,
            },
            gcsDataSink: {
              bucketName: gcsSinkBucket,
            },
          },
          eventStream: {
            name: pubsubId,
          },
        },
      });
    
      console.log(
        `Created an event driven transfer from '${gcsSourceBucket}' to '${gcsSinkBucket}' with name ${transferJob.name}`
      );
    }
    
    createEventDrivenGcsTransfer();

### Python

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Python API reference documentation](https://cloud.google.com/python/docs/reference/storagetransfer/latest). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import storage_transfer
    
    
    def create_event_driven_gcs_transfer(
        project_id: str,
        description: str,
        source_bucket: str,
        sink_bucket: str,
        pubsub_id: str,
    ):
        """Create an event driven transfer between two GCS buckets that tracks a PubSub subscription"""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project-id'
    
        # A description of this job
        # description = 'Creates an event-driven transfer that tracks a pubsub subscription'
    
        # Google Cloud Storage source bucket name
        # source_bucket = 'my-gcs-source-bucket'
    
        # Google Cloud Storage destination bucket name
        # sink_bucket = 'my-gcs-destination-bucket'
    
        # The Pubsub Subscription ID to track
        # pubsub_id = 'projects/PROJECT_NAME/subscriptions/SUBSCRIPTION_ID'
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "gcs_data_source": {
                            "bucket_name": source_bucket,
                        },
                        "gcs_data_sink": {
                            "bucket_name": sink_bucket,
                        },
                    },
                    "event_stream": {
                        "name": pubsub_id,
                    },
                },
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

## Monitor an event-driven transfer

When you create an event-driven transfer, Storage Transfer Service creates a transfer job. Once the start time is reached, a transfer operation starts running and an event listener waits for notifications from the Pub/Sub queue.

The transfer operation runs, with a status of `in progress`, for approximately 24 hours. After 24 hours, the operation finishes and a new operation begins. A new operation is created every 24 hours until the end time of the transfer job is reached, or until the job is manually stopped.

If a file transfer is in progress when the operation is scheduled to finish, the current operation remains in progress until the file has been completely transferred. A new operation is started, and the two operations run simultaneously until the old operation finishes. Any events that are detected during this period are handled by the new operation.

To view the current operation and any completed operations:

###  Google Cloud console 

  1. Go to the **Storage Transfer Service** page in the Google Cloud console.

[Go to Storage Transfer Service](https://console.cloud.google.com/transfer/)

  2. In the job list, select either the **All** tab, or **Cloud-to-cloud**.

  3. Click the job ID for your transfer. The **Scheduling mode** column identifies all event-driven transfers versus batch transfers.

  4. Select the **Operations** tab. Details are shown for the current operation, and completed operations are listed in the **Run history** table. Click any completed operation for additional details.




###  gcloud 

To monitor the progress of a job in real time, use `gcloud transfer jobs monitor`. The response shows the current operation, the job start time, the amount of data transferred, skipped bytes, and error counts.
    
    
    gcloud transfer jobs monitor JOB_NAME
    

To retrieve the current operation name:
    
    
    gcloud transfer jobs describe JOB_NAME --format="value(latestOperationName)"
    

To list current and completed operations:
    
    
    gcloud transfer operations list --job-names=JOB_NAME
    

To see details about an operation:
    
    
    gcloud transfer operations describe OPERATION_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
