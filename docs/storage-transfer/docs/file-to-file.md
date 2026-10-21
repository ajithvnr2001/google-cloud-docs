---
url: https://docs.cloud.google.com/storage-transfer/docs/file-to-file/
title: Transfer data between file systems \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:45.786763+00:00
---

# Transfer data between file systems  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/file-to-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer data between file systems Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to transfer data between two POSIX file systems. Common use cases include:

  * **Burst to cloud and Hybrid HPC:** Quickly transfer large data sets from on-premises to the cloud for processing.
  * **Migration and sync to Filestore:** Migrate or sync data from an on-premises file system to [Filestore](https://docs.cloud.google.com/filestore).
  * **Managed file transfer:** Securely and reliably transfer data between data centers or between two in-cloud file systems.



## Transfer performance guidelines

The following guidelines can help to maximize performance during file system to file system transfers.

### Agent deployment

In general, we recommend using three agents in each of the source and destination agent pools. Monitor the transfer and add more agents if required. Each agent needs 4 vCPU and 8 GiB RAM.

If you are migrating to a Filestore instance, Filestore recommends using the `n2-standard-8` instance type for each agent. Specify `nconnect=2` when you mount the instance to a Compute Engine VM. Refer to [Filestore's performance guidelines](https://docs.cloud.google.com/filestore/docs/performance) for more information on how to optimize and test instance performance.

### Transferring large numbers of small files

For better performance when transferring a large number of small files, we recommend splitting the files into multiple directories and avoiding a single directory with millions of files.

## Before you begin

Before you can perform the tasks described on this page, complete the [prerequisite steps](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up).

## Create agent pools and install agents

For file system to file system transfers, you need to create [agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) and [agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) for both the source and destination file systems. Agents for the source agent pool need to be installed on machines or VMs that have access to the source file system. Agents for the destination agent pool need to be installed on machines or VMs that have access to the destination file system.

Don't include sensitive information such as personally identifiable information (PII) or security data in your agent ID prefix or agent pool name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

### Create a source agent pool

Create a source agent pool using one of the following methods:

###  gcloud CLI 

Create a source agent pool by running:
    
    
    gcloud transfer agent-pools create SOURCE_AGENT_POOL
    

Replace SOURCE_AGENT_POOL with the name that you want to give to the source agent pool.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

The **Agent pools** page is displayed, listing your existing agent pools.

  2. Click **Create another pool**.

  3. Enter a name for the pool.

  4. Click **Create**.




### Install agents for the source agent pool

Install agents for the source agent pool on a machine or VM that has access to the source file system:

###  gcloud CLI 

Install agents for the source agent pool by running:
    
    
    gcloud transfer agents install --pool=SOURCE_AGENT_POOL --count=NUMBER_OF_AGENTS \
      --mount-directories=MOUNT_DIRECTORIES
    

Replace the following:

  * SOURCE_AGENT_POOL with the name of the source agent pool.
  * NUMBER_OF_AGENTS with the number of agents that you want to install for the source agent pool. To determine the optimal number of agents for your environment, see [Agent requirements and best practices](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices).
  * MOUNT_DIRECTORIES with a comma-separated list of directories on the source file system from which to copy. Omitting this flag mounts the entire file system, which could [present a security risk](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access).



###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

The **Agent pools** page is displayed, listing your existing agent pools.

  2. Click the name of the source agent pool that you just created.

  3. Under the **Agents** tab, click **Install agent**.

  4. Follow the instructions in Google Cloud console to install Docker and start the agent.




### Create a destination agent pool and install agents

Repeat the preceding steps to create a destination agent pool and install agents.

## Create a Cloud Storage bucket as an intermediary

File system to file system transfers require a Cloud Storage bucket as an intermediary for the data transfer.

  1. [Create](https://docs.cloud.google.com/storage/docs/creating-buckets) a Cloud Storage [Standard](https://docs.cloud.google.com/storage/docs/storage-classes#standard) class bucket with the following settings:

     * **Encryption** : You can specify a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) (CMEK). Otherwise, a Google-owned and Google-managed encryption key is used.
     * **Object Versioning** , **Bucket Lock** , and **default object holds** : Keep these features disabled.
  2. Grant permissions and roles using one of the following methods:

     * [Grant](https://docs.cloud.google.com/storage-transfer/docs/configure-access#cloud-storage) the Storage Transfer Service service account the Storage Admin role (`roles/storage.admin`) for the bucket.
     * Use `gcloud transfer authorize` to authorize your account for all Storage Transfer Service features. This command grants project-wide Storage Admin permissions:
           
           gcloud transfer authorize --add-missing
           




## Create a transfer job

###  gcloud CLI 

To create a transfer from the source file system to the destination file system, run
    
    
    gcloud transfer jobs create SOURCE_DIRECTORY DESTINATION_DIRECTORY \
        --source-agent-pool=SOURCE_AGENT_POOL \
        --destination-agent-pool=DESTINATION_AGENT_POOL \
        --intermediate-storage-path= gs://STORAGE_BUCKET/FOLDER/
    

Replace the following variables:

  * SOURCE_DIRECTORY with the path of the source directory.
  * DESTINATION_DIRECTORY with the path of the destination directory.
  * SOURCE_AGENT_POOL with the name of the source agent pool.
  * DESTINATION_AGENT_POOL with the name of the destination agent pool.
  * STORAGE_BUCKET with the name of the Cloud Storage bucket.
  * FOLDER with the name of the folder you would like the data to be transferred into.



When you start a transfer job, the system first computes the data in the source and destination to determine the source data that's new or updated since the previous transfer. Only the new data is transferred.

###  Client Libraries 

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
    
    public class TransferBetweenPosix {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your project id
        String projectId = "my-project-id";
    
        // The agent pool associated with the POSIX data source. If not provided, defaults to the
        // default agent
        String sourceAgentPoolName = "projects/my-project-id/agentPools/transfer_service_default";
    
        // The agent pool associated with the POSIX data sink. If not provided, defaults to the default
        // agent
        String sinkAgentPoolName = "projects/my-project-id/agentPools/transfer_service_default";
    
        // The root directory path on the source filesystem
        String rootDirectory = "/directory/to/transfer/source";
    
        // The root directory path on the sink filesystem
        String destinationDirectory = "/directory/to/transfer/sink";
    
        // The ID of the GCS bucket for intermediate storage
        String bucketName = "my-intermediate-bucket";
    
        transferBetweenPosix(
            projectId,
            sourceAgentPoolName,
            sinkAgentPoolName,
            rootDirectory,
            destinationDirectory,
            bucketName);
      }
    
      public static void transferBetweenPosix(
          String projectId,
          String sourceAgentPoolName,
          String sinkAgentPoolName,
          String rootDirectory,
          String destinationDirectory,
          String bucketName)
          throws IOException {
    
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
            [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).newBuilder()
                .setProjectId(projectId)
                .setTransferSpec(
                    [TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html).newBuilder()
                        .[setSinkAgentPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setSinkAgentPoolName_java_lang_String_)(sinkAgentPoolName)
                        .[setSourceAgentPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setSourceAgentPoolName_java_lang_String_)(sourceAgentPoolName)
                        .[setPosixDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setPosixDataSource_com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_)(
                            [PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html).newBuilder().[setRootDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_Builder_setRootDirectory_java_lang_String_)(rootDirectory).build())
                        .[setPosixDataSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setPosixDataSink_com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_)(
                            [PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html).newBuilder().[setRootDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_Builder_setRootDirectory_java_lang_String_)(destinationDirectory).build())
                        .[setGcsIntermediateDataLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setGcsIntermediateDataLocation_com_google_storagetransfer_v1_proto_TransferTypes_GcsData_)(
                            [GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(bucketName).build())
                        .build())
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
              "Created and ran a transfer job from "
                  + rootDirectory
                  + " to "
                  + destinationDirectory
                  + " with name "
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
    
    // The agent pool associated with the POSIX data sink. Defaults to the default agent
    // const sinkAgentPoolName = 'projects/my-project/agentPools/transfer_service_default'
    
    // The root directory path on the source filesystem
    // const rootDirectory = '/directory/to/transfer/source'
    
    // The root directory path on the sink filesystem
    // const destinationDirectory = '/directory/to/transfer/sink'
    
    // The ID of the GCS bucket for intermediate storage
    // const bucketName = 'my-intermediate-bucket'
    
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
            sinkAgentPoolName,
            posixDataSource: {
              rootDirectory,
            },
            posixDataSink: {
              rootDirectory: destinationDirectory,
            },
            gcsIntermediateDataLocation: {
              bucketName,
            },
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
        `Created and ran a transfer job from '${rootDirectory}' to '${destinationDirectory}' with name ${transferJob.name}`
      );
    }
    
    transferDirectory();

### Python
    
    
    from google.cloud import storage_transfer
    
    
    def transfer_between_posix(
        project_id: str,
        description: str,
        source_agent_pool_name: str,
        sink_agent_pool_name: str,
        root_directory: str,
        destination_directory: str,
        intermediate_bucket: str,
    ):
        """Creates a transfer between POSIX file systems."""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project-id'
    
        # A useful description for your transfer job
        # description = 'My transfer job'
    
        # The agent pool associated with the POSIX data source.
        # Defaults to 'projects/{project_id}/agentPools/transfer_service_default'
        # source_agent_pool_name = 'projects/my-project/agentPools/my-agent'
    
        # The agent pool associated with the POSIX data sink.
        # Defaults to 'projects/{project_id}/agentPools/transfer_service_default'
        # sink_agent_pool_name = 'projects/my-project/agentPools/my-agent'
    
        # The root directory path on the source filesystem
        # root_directory = '/directory/to/transfer/source'
    
        # The root directory path on the destination filesystem
        # destination_directory = '/directory/to/transfer/sink'
    
        # The Google Cloud Storage bucket for intermediate storage
        # intermediate_bucket = 'my-intermediate-bucket'
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "source_agent_pool_name": source_agent_pool_name,
                        "sink_agent_pool_name": sink_agent_pool_name,
                        "posix_data_source": {
                            "root_directory": root_directory,
                        },
                        "posix_data_sink": {
                            "root_directory": destination_directory,
                        },
                        "gcs_intermediate_data_location": {
                            "bucket_name": intermediate_bucket
                        },
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

## Manage intermediary buckets

After a transfer job completes, Storage Transfer Service saves [transfer logs](https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format#viewing-logs) listing transferred and failed-to-transfer data in the bucket. After the transfer, clean-up tasks initiate automatically to delete the intermediate data. In some instances, clean-up tasks fail to delete all of the data in the bucket. To delete data that isn't erased during clean-up, use the instructions below to either delete the data manually, or to set a lifecycle rule to delete the data automatically.

###  Manual clean-up 

Delete data from the intermediary bucket by running the following commands based on the type of data you want to delete.

  * To erase data in the intermediary bucket that wasn't deleted during clean-up, run the following command:
        
        gcloud storage rm gs://STORAGE_BUCKET/PREFIX**
        

  * To delete all data, including transfer logs, specify the root of the bucket using the matches-all (*) wildcard.
        
        gcloud storage rm gs://STORAGE_BUCKET/*
        

  * To delete the bucket, run the following command:
        
        gcloud storage rm gs://STORAGE_BUCKET
        




Replace the following variables:

  * STORAGE_BUCKET with the name of the intermediary bucket.

  * PREFIX with the name of the folder the data was transferred into within the intermediary bucket.




###  Set a lifecycle rule 

To delete data that isn't erased by the automatic clean-up cycle, set a lifecycle rule for the Cloud Storage bucket. Use the [`age` condition](https://docs.cloud.google.com/storage/docs/lifecycle#age) to erase intermediate data in the bucket by specifying a period longer than the longest transfer job that uses the bucket as an intermediary. If the specified age condition is shorter than the time required to download the file from the intermediary bucket to the destination, the file transfer fails.

Optionally, use the [`matchesPrefix` condition](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix) to erase data in the folder you specified for the intermediate bucket. To delete transfer logs along with data in the bucket, the `matchesPrefix` condition is not required.

## Preserving file metadata

To preserve file metadata, including numeric UID, GID, MODE, and symbolic links:

###  gcloud CLI 

Use the `--preserve-metadata` field to specify the preservation behavior for this transfer. Options that apply to file system transfers are: `gid`, `mode`, `symlink`, `uid`.

###  REST API 

Specify the appropriate options in a [`metadataOptions`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#MetadataOptions) object.

See [Preserving optional POSIX attributes](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#posix-metadata) for more information.

## Example transfer using the gcloud CLI

In this example, we transfer data from the `/tmp/datasource` directory on VM1 to `/tmp/destination` on VM2.

  1. Set up the source of the transfer.

     1. Create the source agent pool:
            
            gcloud transfer agent-pools create source_agent_pool
            

     2. On VM1, install agents for `source_agent_pool` by running:
            
            gcloud transfer agents install --pool=source_agent_pool \
                --count=1 \
                --mount-directories="/tmp/datasource"
            

  2. Set up the destination of the transfer.

     1. Create the destination agent pool:
            
            gcloud transfer agent-pools create destination_agent_pool
            

     2. On VM2, install agents for `destination_agent_pool` by running:
            
            gcloud transfer agents install --pool=destination_agent_pool \
                --count=3 \
                --mount-directories="/tmp/destination"
            

  3. Create an intermediary Cloud Storage bucket.

     1. Create a bucket named `my-intermediary-bucket`:
            
            gcloud storage buckets create gs://my-intermediary-bucket
            

     2. Authorize your account for all Storage Transfer Service features by running:
            
            gcloud transfer authorize --add-missing
            

  4. Create a transfer job by running:
         
         gcloud transfer jobs create posix:///tmp/datasource posix:///tmp/destination \
             --source-agent-pool=source_agent_pool \
             --destination-agent-pool=destination_agent_pool \
             --intermediate-storage-path=gs://my-intermediary-bucket
         




## What's next

  * Learn more about [managing jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
