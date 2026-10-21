---
url: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/file-system-to-cloud-storage/
title: Transfer from a file system to Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:53.662140+00:00
---

# Transfer from a file system to Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/file-system-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from a file system to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create transfer jobs between a file system (either on-premises or in-cloud) and Cloud Storage.

Transfers from file systems to Cloud Storage are agent-based transfers, meaning you will install software agents on a machine with access to your file system to orchestrate the transfer.

## Configure permissions

Before creating a transfer, you must configure permissions for the following entities:

![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/48px.svg) | The **user account** being used to create the transfer. This is the account that is signed in to the Google Cloud console, or the account that is specified when authenticating to the `gcloud` CLI. The user account can be a regular user account, or a user-managed service account.  
---|---  
![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/cloud_circle/wght600fill1/48px.svg) | The **[service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)** used by Storage Transfer Service. This account is generally identified by its email address, which uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.   
![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/images/forklift-circle.png) | The **transfer agent account** that provides Google Cloud permissions for transfer agents. Transfer agent accounts use the credentials of the user installing them, or the credentials of a user-managed service account, to authenticate.  
  
See [Agent-based transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions) for instructions.

## Install agents into an agent pool

Agent-based transfers use software agents to orchestrate transfers. These agents must be installed on a machine with access to the file system involved in the transfer.

Don't include sensitive information such as personally identifiable information (PII) or security data in your agent pool name or agent ID prefix. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

  1. Create an [agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools). Use your **user account** ![User account symbol](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/24px.svg) for this action.
  2. [Install agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent) into the agent pool. Use your **transfer agent account** ![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/images/forklift-circle.png) for this action.



We recommend starting with 3 agents in your source agent pool. Once the transfer is in progress, [monitor the transfer speed](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#monitor-agents); you can add more agents into the pool while the transfer is in progress.

We recommend one VM per agent, each with a minimum of 4 CPU and 8 GiB RAM.

## Transfer options

The following Storage Transfer Service features are available for transfers from file systems to Cloud Storage.

Transfer specific files using a manifest
    You can pass a list of files for Storage Transfer Service to act on. See [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) for details.
Specify storage class
    You can specify the [ Cloud Storage storage class](https://docs.cloud.google.com/storage/docs/storage-classes) to use for your data in the destination bucket. See the [ `StorageClass`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#storageclass) options for REST details, or use the [ `--custom-storage-class`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--custom-storage-class) flag with Google Cloud CLI. 

Note that any storage class settings are ignored if the destination bucket has [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) enabled. If Autoclass is enabled, objects transferred into the bucket are initially set to Standard storage.

Metadata preservation
    

When transferring files from file systems, Storage Transfer Service can optionally preserve certain attributes as custom metadata. If these files are later written back to a file system, Storage Transfer Service can convert the preserved metadata back to POSIX attributes.

See the **POSIX file system transfers** section of [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details on which metadata can be preserved, and how to configure your transfer.

Manage network bandwidth
    Storage Transfer Service by default uses as much bandwidth as is available to it to transfer files from your file system. You can set a bandwidth limit to prevent a transfer from affecting other network traffic. Bandwidth limits are applied at an agent pool level. 

See [Manage network bandwidth](https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem) to learn more.

![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/24px.svg) Your user account requires the **Storage Transfer Admin** (`roles/storagetransfer.admin`) role to set or change bandwidth limits.

Logging
    Storage Transfer Service supports [ Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) (recommended) as well as [agent-based transfer logs](https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format). 

## Create a transfer

Don't include sensitive information such as personally identifiable information (PII) or security data in your transfer job name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

Storage Transfer Service provides multiple interfaces through which to create a transfer.

###  Google Cloud console 

  1. Go to the **Storage Transfer Service** page in the Google Cloud console.

[Go to Storage Transfer Service](https://console.cloud.google.com/transfer/)

  2. Click **Create transfer job**. The **Create a transfer job** page is displayed.

  3. Choose **POSIX file system** as the source.

  4. Select **Cloud Storage** as the destination type and click **Next step**.

  5. Select an existing agent pool, or select **Create agent pool** and follow the instructions to create a new pool.

  6. Specify the fully qualified path of the file system directory.

  7. Click **Next step**.

  8. In the **Bucket or folder** field, enter the destination bucket and (optionally) folder name, or click **Browse** to select a bucket from a list of existing buckets in your current project. To create a new bucket, click ![Bucket icon](https://docs.cloud.google.com/static/storage-transfer/docs/images/bucket_icon.png)**Create new bucket**.

  9. Click **Next step**.

  10. Choose your scheduling options.

**Note:** Storage Transfer Service displays transfer job schedules in your local timezone, but it stores those times in Universal Time Coordinated (UTC). If you are affected by Daylight Savings Time (DST), you might experience a transfer job schedule change when DST starts or ends.
  11. Click **Next step**.

  12. Choose settings for the transfer job.

     * In the **Description** field, enter a description of the transfer. As a best practice, enter a description that is meaningful and unique so that you can tell jobs apart.

     * Under **Metadata options** , use the default options, or update one or more values. See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

     * Under **When to overwrite** , select one of the following:

       * **Never** : Storage Transfer Service skips transferring any files from the source that have the same name as a file present in the destination.

       * **If different** : Overwrites destination files if the source file with the same name has different Etags or checksum values.

       * **Always** : Always overwrites destination files when the source file has the same name, even if they're identical.

     * Under **When to delete** , select one of the following:

       * **Never** : Never delete files from either the source or destination.

       * **Delete file from source after they're transferred** : Delete files from the source after they're transferred to the destination. If a source file isn't transferred, for example because it already exists in the destination, the source file is not deleted.

**Important:** If you don't have local backup, this option is a non-reversible action.
       * **Delete files from destination if they're not also at source** : If files in the destination Cloud Storage bucket aren't also in the source, then delete the files from the Cloud Storage bucket.

This option ensures that the destination Cloud Storage bucket exactly matches your source.

     * Select whether to **Enable logging in Cloud Storage** and/or **Enable logging in Cloud Logging**. See [File system transfer logs](https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format) and [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for more information.

  13. To create your transfer job, click **Create**.




###  `gcloud`

Before using `gcloud` commands, [install Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

To create a new transfer job, use the `gcloud transfer jobs create` command. Creating a new job initiates the specified transfer, unless a schedule or `--do-not-run` is specified.
    
    
    gcloud transfer jobs create \
      posix:///SOURCE \
      gs://DESTINATION/ \
      --source-agent-pool=SOURCE_POOL_NAME

Replace the following:

  * SOURCE is an absolute path from the root of the file system. It's prefixed with `posix://` so the final value will include 3 forward slashes. For example, `posix:///tmp/data/`.

  * DESTINATION is one the name of a Cloud Storage bucket and, optionally, a folder path followed by a trailing slash. For example, `gs://example-bucket/data/`.

  * `--source-agent-pool` specifies the source agent pool to use for this transfer.




Additional options include:

  * `--do-not-run` prevents Storage Transfer Service from running the job upon submission of the command. To run the job, update it to add a schedule, or use `jobs run` to start it manually.

  * `--manifest-file` specifies the path to a CSV file in Cloud Storage containing a list of files to transfer from your source. For manifest file formatting, see [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).

  * **Job information** : You can specify `--name` and `--description`.

  * **Schedule** : Specify `--schedule-starts`, `--schedule-repeats-every`, and `--schedule-repeats-until`, or `--do-not-run`.

  * **Transfer options** : Specify whether to overwrite destination files (`--overwrite-when=different` or `always`) and whether to delete certain files during or after the transfer (`--delete-from=destination-if-unique` or `source-after-transfer`); specify which [metadata values to preserve](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) (`--preserve-metadata`); and optionally set a storage class on transferred objects (`--custom-storage-class`).




To view all options, run `gcloud transfer jobs create --help` or refer to the [`gcloud` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create). Note that not all options are supported for agent-based transfers; unsupported options contain a note to this effect in their help text.

###  REST 

The following example shows you how to use Storage Transfer Service through the REST API.

When you configure or edit transfer jobs using the Storage Transfer Service API, the time must be in UTC. For more information on specifying the schedule of a transfer job, see [Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#Schedule).

To move files from a POSIX file system to a Cloud Storage bucket, use [transferJobs.create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create) with a [`posixDataSource`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#FIELDS.posix_data_source):
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
     "name":"transferJobs/sample_transfer",
     "description": "My First Transfer",
     "status": "ENABLED",
     "projectId": "my_transfer_project_id",
     "schedule": {
         "scheduleStartDate": {
             "year": 2022,
             "month": 5,
             "day": 2
         },
         "startTimeOfDay": {
             "hours": 22,
             "minutes": 30,
             "seconds": 0,
             "nanos": 0
         }
         "scheduleEndDate": {
             "year": 2022,
             "month": 12,
             "day": 31
         },
         "repeatInterval": {
             "259200s"
         },
     },
     "transferSpec": {
         "posixDataSource": {
              "rootDirectory": "/bar/",
         },
         "sourceAgentPoolName": "my_example_pool",
         "gcsDataSink": {
              "bucketName": "destination_bucket"
              "path": "foo/bar/"
         },
      }
    }

The [`schedule`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#schedule) field is optional; if it's not included, the transfer job must be started with a [`transferJobs.run`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/run) request.

To check your transfer's status after creating a job, use [`transferJobs.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/get):
    
    
    GET https://storagetransfer.googleapis.com/v1/transferJobs/sample_transfer?project_id=my_transfer_project_id

###  Client libraries 

The following samples show you how to use Storage Transfer Service programmatically with Go, Java, Node.js, and Python.

When you configure or edit transfer jobs programmatically, the time must be in UTC. For more information on specifying the schedule of a transfer job, see [Schedule](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#Schedule).

For more information about the Storage Transfer Service client libraries, see [Getting started with Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries).

To move files from a POSIX file system to a Cloud Storage bucket:

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    	"cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func transferFromPosix(w io.Writer, projectID string, sourceAgentPoolName string, rootDirectory string, gcsSinkBucket string) (*storagetransferpb.TransferJob, error) {
    	// Your project id
    	// projectId := "myproject-id"
    
    	// The agent pool associated with the POSIX data source. If not provided, defaults to the default agent
    	// sourceAgentPoolName := "projects/my-project/agentPools/transfer_service_default"
    
    	// The root directory path on the source filesystem
    	// rootDirectory := "/directory/to/transfer/source"
    
    	// The ID of the GCS bucket to transfer data to
    	// gcsSinkBucket := "my-sink-bucket"
    
    	ctx := context.Background()
    	client, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storagetransfer.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.CreateTransferJobRequest{
    		TransferJob: &storagetransferpb.TransferJob{
    			ProjectId: projectID,
    			TransferSpec: &storagetransferpb.TransferSpec{
    				SourceAgentPoolName: sourceAgentPoolName,
    				DataSource: &storagetransferpb.TransferSpec_PosixDataSource{
    					PosixDataSource: &storagetransferpb.PosixFilesystem{RootDirectory: rootDirectory},
    				},
    				DataSink: &storagetransferpb.TransferSpec_GcsDataSink{
    					GcsDataSink: &storagetransferpb.GcsData{BucketName: gcsSinkBucket},
    				},
    			},
    			Status: storagetransferpb.[TransferJob_ENABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob_STATUS_UNSPECIFIED_TransferJob_ENABLED_TransferJob_DISABLED_TransferJob_DELETED),
    		},
    	}
    
    	resp, err := client.CreateTransferJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("failed to create transfer job: %w", err)
    	}
    	if _, err = client.RunTransferJob(ctx, &storagetransferpb.RunTransferJobRequest{
    		ProjectId: projectID,
    		JobName:   resp.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name),
    	}); err != nil {
    		return nil, fmt.Errorf("failed to run transfer job: %w", err)
    	}
    	fmt.Fprintf(w, "Created and ran transfer job from %v to %v with name %v", rootDirectory, gcsSinkBucket, resp.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name))
    	return resp, nil
    }
    

### Java
    
    
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html);
    import java.io.IOException;
    
    public class TransferFromPosix {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your project id
        String projectId = "my-project-id";
    
        // The agent pool associated with the POSIX data source. If not provided, defaults to the
        // default agent
        String sourceAgentPoolName = "projects/my-project-id/agentPools/transfer_service_default";
    
        // The root directory path on the source filesystem
        String rootDirectory = "/directory/to/transfer/source";
    
        // The ID of the GCS bucket to transfer data to
        String gcsSinkBucket = "my-sink-bucket";
    
        transferFromPosix(projectId, sourceAgentPoolName, rootDirectory, gcsSinkBucket);
      }
    
      public static void transferFromPosix(
          String projectId, String sourceAgentPoolName, String rootDirectory, String gcsSinkBucket)
          throws IOException {
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
            [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).newBuilder()
                .setProjectId(projectId)
                .setTransferSpec(
                    [TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html).newBuilder()
                        .[setSourceAgentPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setSourceAgentPoolName_java_lang_String_)(sourceAgentPoolName)
                        .[setPosixDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setPosixDataSource_com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_)(
                            [PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html).newBuilder().[setRootDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_Builder_setRootDirectory_java_lang_String_)(rootDirectory).build())
                        .setGcsDataSink([GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(gcsSinkBucket).build()))
                .setStatus([TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).Status.ENABLED)
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources,
        // or use "try-with-close" statement to do this automatically.
        try ([StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html).create()) {
    
          // Create the transfer job
          [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response =
              storageTransfer.createTransferJob(
                  [TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).CreateTransferJobRequest.newBuilder()
                      .setTransferJob(transferJob)
                      .build());
    
          System.out.println(
              "Created a transfer job from "
                  + rootDirectory
                  + " to "
                  + gcsSinkBucket
                  + " with "
                  + "name "
                  + response.getName());
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library
    const {
      StorageTransferServiceClient,
    } = require('[@google-cloud/storage-transfer](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // Your project id
    // const projectId = 'my-project'
    
    // The agent pool associated with the POSIX data source. Defaults to the default agent
    // const sourceAgentPoolName = 'projects/my-project/agentPools/transfer_service_default'
    
    // The root directory path on the source filesystem
    // const rootDirectory = '/directory/to/transfer/source'
    
    // The ID of the GCS bucket to transfer data to
    // const gcsSinkBucket = 'my-sink-bucket'
    
    // Creates a client
    const client = new [StorageTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)();
    
    /**
     * Creates a request to transfer from the local file system to the sink bucket
     */
    async function transferDirectory() {
      const createRequest = {
        transferJob: {
          projectId,
          transferSpec: {
            sourceAgentPoolName,
            posixDataSource: {
              rootDirectory,
            },
            gcsDataSink: {bucketName: gcsSinkBucket},
          },
          status: '[ENABLED](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)',
        },
      };
    
      // Runs the request and creates the job
      const [transferJob] = await client.createTransferJob(createRequest);
    
      const runRequest = {
        jobName: transferJob.name,
        projectId: projectId,
      };
    
      await client.runTransferJob(runRequest);
    
      console.log(
        `Created and ran a transfer job from '${rootDirectory}' to '${gcsSinkBucket}' with name ${transferJob.name}`
      );
    }
    
    transferDirectory();

### Python
    
    
    from google.cloud import storage_transfer
    
    
    def transfer_from_posix_to_gcs(
        project_id: str,
        description: str,
        source_agent_pool_name: str,
        root_directory: str,
        sink_bucket: str,
    ):
        """Create a transfer from a POSIX file system to a GCS bucket."""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project-id'
    
        # A useful description for your transfer job
        # description = 'My transfer job'
    
        # The agent pool associated with the POSIX data source.
        # Defaults to 'projects/{project_id}/agentPools/transfer_service_default'
        # source_agent_pool_name = 'projects/my-project/agentPools/my-agent'
    
        # The root directory path on the source filesystem
        # root_directory = '/directory/to/transfer/source'
    
        # Google Cloud Storage sink bucket name
        # sink_bucket = 'my-gcs-sink-bucket'
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "source_agent_pool_name": source_agent_pool_name,
                        "posix_data_source": {
                            "root_directory": root_directory,
                        },
                        "gcs_data_sink": {"bucket_name": sink_bucket},
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
