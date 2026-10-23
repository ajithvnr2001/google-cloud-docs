---
url: https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws/
title: Event-driven transfers from AWS S3 \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:42.835127+00:00
---

# Event-driven transfers from AWS S3  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Event-driven transfers from AWS S3 Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can listen to event notifications in AWS to automatically transfer data that has been added or updated in the source location, into a Cloud Storage bucket. [Learn more](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) about the benefits of event-driven transfers.

Event-driven transfers listen to [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) sent to Amazon SQS to know when objects in the source bucket have been modified or added. Object deletions are not detected; deleting an object at the source does not delete the associated object in the destination bucket.

Event-driven transfers always use a Cloud Storage bucket as the destination.

## Before you begin

Follow the instructions to grant the required permissions on your destination Cloud Storage bucket:

  * [Configure access to a destination: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)



## Create an SQS queue

  1. In the AWS console, go to the **Simple Queue Service** page.

  2. Click **Create queue**.

  3. Enter a **Name** for this queue.

  4. In the **Access policy** section, select **Advanced**. A JSON object is displayed.

###  Standard AWS regions 
         
         {
           "Version": "2008-10-17",
           "Id": "\_\_default\_policy\_ID",
           "Statement": [
             {
               "Sid": "\_\_owner\_statement",
               "Effect": "Allow",
               "Principal": {
                 **"AWS" : "01234567890"**
               },
               "Action": [
                 "SQS:*"
               ],
               **"Resource" : "arn:aws:sqs:us-west-2:01234567890:test"**
             }
           ]
         }

###  AWS GovCloud regions 
         
         {
           "Version": "2008-10-17",
           "Id": "\_\_default\_policy\_ID",
           "Statement": [
             {
               "Sid": "\_\_owner\_statement",
               "Effect": "Allow",
               "Principal": {
                 **"AWS" : "01234567890"**
               },
               "Action": [
                 "SQS:*"
               ],
               **"Resource" : "arn:aws-us-gov:sqs:us-gov-west-1:01234567890:test"**
             }
           ]
         }

Copy the values of `AWS` and `Resource`. These are unique for each project.

  5. Paste your specific values of `AWS` and `Resource` from the previous step into the following JSON snippet:

###  Standard AWS regions 
         
         {
         "Version": "2012-10-17",
         "Id": "example-ID",
         "Statement": [
           {
             "Sid": "example-statement-ID",
             "Effect": "Allow",
             "Principal": {
               "Service": "s3.amazonaws.com"
             },
             "Action": "SQS:SendMessage",
             "Resource": "RESOURCE",
             "Condition": {
               "StringEquals": {
                 "aws:SourceAccount": "AWS"
               },
               "ArnLike": {
                 "aws:SourceArn": "arn:aws:s3:::S3_BUCKET_NAME"
               }
             }
           }
         ]
         }

###  AWS GovCloud regions 
         
         {
         "Version": "2012-10-17",
         "Id": "example-ID",
         "Statement": [
           {
             "Sid": "example-statement-ID",
             "Effect": "Allow",
             "Principal": {
               "Service": "s3.amazonaws.com"
             },
             "Action": "SQS:SendMessage",
             "Resource": "RESOURCE",
             "Condition": {
               "StringEquals": {
                 "aws:SourceAccount": "AWS"
               },
               "ArnLike": {
                 "aws:SourceArn": "arn:aws-us-gov:s3:::S3_BUCKET_NAME"
               }
             }
           }
         ]
         }

Replace S3_BUCKET_NAME with the S3 source bucket's name.

  6. Copy this completed JSON snippet and use it to replace the JSON displayed in the **Access policy** section.

  7. Click **Create queue**.




Once complete, note the Amazon Resource Name (ARN) of the queue.

## Enable notifications on your S3 bucket

  1. In the AWS console, go to the **S3** page.

  2. In the **Buckets** list, select your source bucket.

  3. Select the **Properties** tab.

  4. In the **Event notifications** section, click **Create event notification**.

  5. Specify a name for this event.

  6. In the **Event types** section, select **All object create events**.

  7. As the **Destination** select **SQS queue** and select the queue you created for this transfer.

  8. Click **Save changes**.




## Configure permissions

Follow the instructions in [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) to create either an access key ID and secret key, or a Federated Identity role.

While following the instructions, use the following JSON when directed to specify a [custom role](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3#access_credentials) or a [custom trust policy](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3#federated_identity):

###  Standard AWS regions 
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sqs:DeleteMessage",
                  "sqs:ChangeMessageVisibility",
                  "sqs:ReceiveMessage",
                  "s3:GetObject",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::S3_BUCKET_NAME",
                  "arn:aws:s3:::S3_BUCKET_NAME/*",
                  "AWS_QUEUE_ARN"
              ]
          }
      ]
    }

Once created, note the following information:

  * For a user, note the access key ID and secret key.
  * For a Federated Identity role, note the Amazon Resource Name (ARN), which has the following format: `arn:aws:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME`



###  AWS GovCloud regions 
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sqs:DeleteMessage",
                  "sqs:ChangeMessageVisibility",
                  "sqs:ReceiveMessage",
                  "s3:GetObject",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws-us-gov:s3:::S3_BUCKET_NAME",
                  "arn:aws-us-gov:s3:::S3_BUCKET_NAME/*",
                  "AWS_QUEUE_ARN"
              ]
          }
      ]
    }

Once created, note the following information:

  * For a user, note the access key ID and secret key.
  * For a Federated Identity role, note the Amazon Resource Name (ARN), which has the following format: `arn:aws-us-gov:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME`



## Create a transfer job

You can use the Google Cloud console, Google Cloud CLI, or REST API to create an event-based transfer job.

###  Cloud console 

  1. Go to the **Create transfer job** page in the Google Cloud console.

[Go to **Create transfer job**](https://console.cloud.google.com/transfer/create)

  2. Select **Amazon S3** as the source type, and **Cloud Storage** as the destination.

  3. As the **Scheduling mode** select **Event-driven** and click **Next step**.

  4. Enter your S3 bucket name. The bucket name is the name as it appears in the [AWS Management Console](https://console.aws.amazon.com/). For example, `my-aws-bucket`.

  5. Select your authentication method and enter the requested information, which you created and noted in the previous section.

  6. Enter the Amazon SQS queue ARN that you created earlier. It uses one of the following formats:

     * For standard AWS regions: `arn:aws:sqs:AWS_REGION:AWS_ACCOUNT:AWS_QUEUE_NAME`
     * For AWS GovCloud regions: `arn:aws-us-gov:sqs:AWS_REGION:AWS_ACCOUNT:AWS_QUEUE_NAME`
  7. Optionally, define any filters, then click **Next step**.

  8. Select the destination Cloud Storage bucket and, optionally, path.

  9. Optionally, enter a start and end time for the transfer. If you don't specify a time, the transfer will start immediately and will run until manually stopped.

  10. Specify any transfer options. More information is available from the [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) page.

  11. Click **Create**.




Once created, the transfer job starts running and an event listener waits for notifications on the SQS queue. The job details page shows one operation each hour, and includes details on data transferred for each job.

###  gcloud 

To create an event-driven transfer job using the Google Cloud CLI, use the `gcloud transfer jobs create` command with the `--event-stream-name` flag:
    
    
    gcloud transfer jobs create \
      s3://S3_BUCKET_NAME \
      gs://GCS_BUCKET_NAME \
      --source-creds-file=SOURCE_CREDS_FILE \
      --event-stream-name=AWS_QUEUE_ARN \
      --event-stream-starts=EVENT_STREAM_STARTS \
      --event-stream-expires=EVENT_STREAM_EXPIRES
    

Replace the placeholders with your actual values:

  * S3_BUCKET_NAME: The name of your Amazon S3 source bucket.
  * GCS_BUCKET_NAME: Your destination Cloud Storage bucket.
  * SOURCE_CREDS_FILE: The relative path to a local file on your machine containing your AWS credentials. Depending on your authentication method, this file should contain either your access key ID and secret key, or your Federated Identity role ARN. For more information, see [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3#access_credentials).
  * AWS_QUEUE_ARN: The ARN of your Amazon SQS queue. For example, `arn:aws:sqs:us-east-1:123456789012:my-queue` for standard AWS regions or `arn:aws-us-gov:sqs:us-gov-west-1:123456789012:my-gov-queue` for AWS GovCloud regions.
  * EVENT_STREAM_STARTS: When to start listening for events using the %Y-%m-%dT%H:%M:%S%z datetime format (e.g., `2020-04-12T06:42:12+04:00`). If not set, the job starts running and listening for events upon the successful submission of the create job command.
  * EVENT_STREAM_EXPIRES: When to stop listening for events. If not set, the job continues until manually stopped.



For a full list of supported fields, refer to the [`gcloud transfer jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create) reference.

###  REST 

To create an event-driven transfer using the REST API, send the following JSON object to the [transferJobs.create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create) endpoint:
    
    
    {
    "description": "DESCRIPTION",
    "status": "ENABLED",
    "projectId": "PROJECT_ID",
    "transferSpec": {
      "awsS3DataSource": {
        "bucketName": "S3_BUCKET_NAME",
        "roleArn": "AWS_ROLE_ARN"
      },
      "gcsDataSink": {
        "bucketName": "GCS_BUCKET_NAME"
      }
    },
    "eventStream": {
      "name": "AWS_QUEUE_ARN",
      "eventStreamStartTime": "2022-12-02T01:00:00+00:00",
      "eventStreamExpirationTime": "2023-01-31T01:00:00+00:00"
    }
    }

The placeholders in the preceding JSON use the following values:

  * DESCRIPTION is a description of the transfer job.
  * PROJECT_ID is the ID of the Google Cloud project where the transfer job is created.
  * S3_BUCKET_NAME is the name of the Amazon S3 source bucket.
  * AWS_ROLE_ARN is the ARN of the Federated Identity role you created. For example, `arn:aws:iam::1234567891011:role/aws-role-name` for standard AWS regions or `arn:aws-us-gov:iam::1234567891011:role/aws-role-name` for AWS GovCloud regions.
  * GCS_BUCKET_NAME is the name of the Cloud Storage destination bucket.
  * AWS_QUEUE_ARN is the ARN of the SQS queue. For example, `arn:aws:sqs:us-east-1:1234567891011:s3-notification-queue` for standard AWS regions or `arn:aws-us-gov:sqs:us-gov-east-1:1234567890:event-queue` for AWS GovCloud regions.



The `eventStreamStartTime` and `eventStreamExpirationTime` are optional. If the start time is omitted, the transfer starts immediately; if the end time is omitted, the transfer continues until manually stopped.

###  Client libraries 

### Go

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storagetransfer@v1.0.0/apiv1). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func createEventDrivenAWSTransfer(w io.Writer, projectID string, s3SourceBucket string, gcsSinkBucket string, sqsQueueARN string) (*storagetransferpb.TransferJob, error) {
    	// Your Google Cloud Project ID.
    	// projectID := "my-project-id"
    
    	// The name of the source AWS S3 bucket.
    	// s3SourceBucket := "my-source-bucket"
    
    	// The name of the GCS bucket to transfer objects to.
    	// gcsSinkBucket := "my-sink-bucket"
    
    	// The Amazon Resource Name (ARN) of the AWS SNS queue to subscribe the event driven transfer to.
    	// sqsQueueARN := "arn:aws:sqs:us-east-1:1234567891011:s3-notification-queue"
    
    	// The AWS access key credential, should be accessed via environment variable for security
    	awsAccessKeyID := os.Getenv("AWS_ACCESS_KEY_ID")
    
    	// The AWS secret key credential, should be accessed via environment variable for security
    	awsSecretKey := os.Getenv("AWS_SECRET_ACCESS_KEY")
    
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
    				DataSource: &storagetransferpb.TransferSpec_AwsS3DataSource{
    					AwsS3DataSource: &storagetransferpb.AwsS3Data{
    						BucketName: s3SourceBucket,
    						AwsAccessKey: &storagetransferpb.AwsAccessKey{
    							AccessKeyId:     awsAccessKeyID,
    							SecretAccessKey: awsSecretKey,
    						}},
    				},
    				DataSink: &storagetransferpb.TransferSpec_GcsDataSink{
    					GcsDataSink: &storagetransferpb.GcsData{BucketName: gcsSinkBucket}},
    			},
    			EventStream: &storagetransferpb.EventStream{Name: sqsQueueARN},
    			Status:      storagetransferpb.TransferJob_ENABLED,
    		},
    	}
    	resp, err := client.CreateTransferJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("failed to create transfer job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created an event driven transfer job from %v to %v subscribed to %v with name %v", s3SourceBucket, gcsSinkBucket, sqsQueueARN, resp.Name)
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html);
    
    public class CreateEventDrivenAwsTransfer {
      public static void main(String[] args) throws Exception {
        // Your Google Cloud Project ID
        String projectId = "your-project-id";
    
        // The name of the source AWS bucket to transfer data from
        String s3SourceBucket = "yourS3SourceBucket";
    
        // The name of the GCS bucket to transfer data to
        String gcsSinkBucket = "your-gcs-bucket";
    
        // The ARN of the SQS queue to subscribe to
        String sqsQueueArn = "arn:aws:sqs:us-east-1:1234567891011:s3-notification-queue";
    
        createEventDrivenAwsTransfer(projectId, s3SourceBucket, gcsSinkBucket, sqsQueueArn);
      }
    
      public static void createEventDrivenAwsTransfer(
          String projectId, String s3SourceBucket, String gcsSinkBucket, String sqsQueueArn)
          throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources,
        // or use "try-with-close" statement to do this automatically.
        try ([StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html).create()) {
    
          // The ID used to access your AWS account. Should be accessed via environment variable.
          String awsAccessKeyId = System.getenv("AWS_ACCESS_KEY_ID");
    
          // The Secret Key used to access your AWS account. Should be accessed via environment
          // variable.
          String awsSecretAccessKey = System.getenv("AWS_SECRET_ACCESS_KEY");
    
          [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferJob.newBuilder()
                  .setProjectId(projectId)
                  .setTransferSpec(
                      [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferSpec.newBuilder()
                          .[setAwsS3DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setAwsS3DataSource_com_google_storagetransfer_v1_proto_TransferTypes_AwsS3Data_)(
                              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).AwsS3Data.newBuilder()
                                  .setBucketName(s3SourceBucket)
                                  .[setAwsAccessKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsS3Data.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsS3Data_Builder_setAwsAccessKey_com_google_storagetransfer_v1_proto_TransferTypes_AwsAccessKey_)(
                                      [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).AwsAccessKey.newBuilder()
                                          .[setAccessKeyId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsAccessKey.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsAccessKey_Builder_setAccessKeyId_java_lang_String_)(awsAccessKeyId)
                                          .[setSecretAccessKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsAccessKey.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsAccessKey_Builder_setSecretAccessKey_java_lang_String_)(awsSecretAccessKey))
                                  .build())
                          .setGcsDataSink(
                              [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).GcsData.newBuilder().setBucketName(gcsSinkBucket)))
                  .setStatus([TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).TransferJob.Status.ENABLED)
                  .[setEventStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferJob_Builder_setEventStream_com_google_storagetransfer_v1_proto_TransferTypes_EventStream_)([TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).EventStream.newBuilder().setName(sqsQueueArn).build())
                  .build();
    
          [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response =
              storageTransfer.createTransferJob(
                  [TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).CreateTransferJobRequest.newBuilder()
                      .setTransferJob(transferJob)
                      .build());
    
          System.out.println(
              "Created a transfer job from "
                  + s3SourceBucket
                  + " to "
                  + gcsSinkBucket
                  + " subscribed to "
                  + sqsQueueArn
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
    
    // AWS S3 source bucket name
    // s3SourceBucket = 'my-s3-source-bucket'
    
    // Google Cloud Storage destination bucket name
    // gcsSinkBucket = 'my-gcs-destination-bucket'
    
    // The ARN of the SQS queue to subscribe to
    // sqsQueueArn = 'arn:aws:sqs:us-east-1:1234567891011:s3-notification-queue'
    
    // AWS Access Key ID. Should be accessed via environment variable for security.
    // awsAccessKeyId = 'AKIA...'
    
    // AWS Secret Access Key. Should be accessed via environment variable for security.
    // awsSecretAccessKey = 'HEAoMK2.../...ku8'
    
    // Creates a client
    const client = new [StorageTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)();
    
    /**
     * Creates an event driven transfer that tracks an SQS queue.
     */
    async function createEventDrivenAwsTransfer() {
      const [transferJob] = await client.createTransferJob({
        transferJob: {
          projectId,
          status: '[ENABLED](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)',
          transferSpec: {
            awsS3DataSource: {
              bucketName: s3SourceBucket,
              awsAccessKey: {
                accessKeyId: awsAccessKeyId,
                secretAccessKey: awsSecretAccessKey,
              },
            },
            gcsDataSink: {
              bucketName: gcsSinkBucket,
            },
          },
          eventStream: {
            name: sqsQueueArn,
          },
        },
      });
    
      console.log(
        `Created an event driven transfer from '${s3SourceBucket}' to '${gcsSinkBucket}' with name ${transferJob.name}`
      );
    }
    
    createEventDrivenAwsTransfer();

### Python

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Python API reference documentation](https://cloud.google.com/python/docs/reference/storagetransfer/latest). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import storage_transfer
    
    
    def create_event_driven_aws_transfer(
        project_id: str,
        description: str,
        source_s3_bucket: str,
        sink_gcs_bucket: str,
        sqs_queue_arn: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
    ):
        """Create an event driven transfer between two GCS buckets that tracks an AWS SQS queue"""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project-id'
    
        # A description of this job
        # description = 'Creates an event-driven transfer that tracks an SQS queue'
    
        # AWS S3 source bucket name
        # source_s3_bucket = 'my-s3-source-bucket'
    
        # Google Cloud Storage destination bucket name
        # sink_gcs_bucket = 'my-gcs-destination-bucket'
    
        # The ARN of the SQS queue to subscribe to
        # pubsub_id = 'arn:aws:sqs:us-east-1:1234567891011:s3-notification-queue'
    
        # AWS Access Key ID. Should be accessed via environment variable for security purposes.
        # aws_access_key_id = 'AKIA...'
    
        # AWS Secret Access Key. Should be accessed via environment variable for security purposes.
        # aws_secret_access_key = 'HEAoMK2.../...ku8'
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "aws_s3_data_source": {
                            "bucket_name": source_s3_bucket,
                            "aws_access_key": {
                                "access_key_id": aws_access_key_id,
                                "secret_access_key": aws_secret_access_key,
                            },
                        },
                        "gcs_data_sink": {
                            "bucket_name": sink_gcs_bucket,
                        },
                    },
                    "event_stream": {
                        "name": sqs_queue_arn,
                    },
                },
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
