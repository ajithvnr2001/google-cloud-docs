---
url: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/s3-compatible/
title: Transfer from S3-compatible storage to Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:59.961939+00:00
---

# Transfer from S3-compatible storage to Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/s3-compatible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from S3-compatible storage to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports transfers from cloud or on-premises object storage systems that are compatible with the Amazon S3 API.

Storage Transfer Service accesses your data in S3-compatible storage using transfer agents deployed on VMs close to the data source. These agents run in a Docker container and belong to an agent pool, which is a collection of agents using the same configuration and that collectively move your data in parallel.

This feature allows you to migrate from on-premise or cloud object storage to Cloud Storage, archive data to free up on-premises storage capacity, replicate data to Google Cloud for business continuity, or transfer data to Google Cloud for analysis and processing. For customers migrating from AWS S3 to Cloud Storage, this feature gives an option to control network routes to Google Cloud, resulting in considerably lower outbound data transfer charges.

## Before you begin

Before configuring your transfers, complete the following steps:

  * [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * Satisfy the [requirements for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up), including installing Docker on the transfer agent machine.



## Obtain source credentials

Transferring from S3-compatible storage requires an **access key ID** and a **secret access key**.

The steps to obtain these depend on your storage provider.

The account from which the ID and key are generated requires one of the following permissions:

  * Read-only permission on source objects, if you don't want to delete objects at source.
  * Full access to source objects, if you choose to delete objects at source as part of your transfer.



Once you've created the account, added permissions, and downloaded the **access key ID** and **secret access key** , store the ID and key in a safe place.

## Configure Google Cloud permissions

Before creating a transfer, you must configure permissions for the following entities:

![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/48px.svg) | The **user account** being used to create the transfer. This is the account that is signed in to the Google Cloud console, or the account that is specified when authenticating to the `gcloud` CLI. The user account can be a regular user account, or a user-managed service account.  
---|---  
![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/cloud_circle/wght600fill1/48px.svg) | The **[service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)** used by Storage Transfer Service. This account is generally identified by its email address, which uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.   
![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/images/forklift-circle.png) | The **transfer agent account** that provides Google Cloud permissions for transfer agents. Transfer agent accounts use the credentials of the user installing them, or the credentials of a user-managed service account, to authenticate.  
  
See [Agent-based transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions) for instructions.

## Transfer options

The following Storage Transfer Service features are available for transfers from S3-compatible storage to Cloud Storage:

Transfer specific files using a manifest
    You can pass a list of files for Storage Transfer Service to act on. See [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) for details.
Specify storage class
    You can specify the [ Cloud Storage storage class](https://docs.cloud.google.com/storage/docs/storage-classes) to use for your data in the destination bucket. See the [ `StorageClass`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#storageclass) options for REST details, or use the [ `--custom-storage-class`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--custom-storage-class) flag with Google Cloud CLI. 

Note that any storage class settings are ignored if the destination bucket has [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) enabled. If Autoclass is enabled, objects transferred into the bucket are initially set to Standard storage.

Metadata preservation
    

When transferring files from S3-compatible storage, Storage Transfer Service can optionally preserve certain attributes as custom metadata.

See the **Amazon S3 or S3-compatible storage to Cloud Storage** section of [ Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#s3-to-cloud) for details on which metadata can be preserved, and how to configure your transfer.

Logging and monitoring
    Transfers from S3-compatible storage can be viewed in Cloud Logging and Cloud Monitoring. See [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) and [Monitor transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs) for details. You can also configure [Pub/Sub notifications](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer).

## Create an agent pool

Don't include sensitive information such as personally identifiable information (PII) or security data in your agent pool name or agent ID prefix. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

To create an agent pool:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

The **Agent pools** page is displayed, listing your existing agent pools.

  2. Click **Create another pool**.

  3. Name your pool, and optionally describe it.

  4. You may choose to set a bandwidth limit that will apply to the pool as a whole. The specified bandwidth in MB/s will be split amongst all of the agents in the pool. See [Manage network bandwidth](https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem) for more information.

  5. Click **Create**.




### REST API

Use [projects.agentPools.create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/create):
    
    
    POST https://storagetransfer.googleapis.com/v1/projects/PROJECT_ID/agentPools?agent_pool_id=AGENT_POOL_ID
    

Replace the following:

  * `PROJECT_ID`: The project ID that you're creating the agent pool in.
  * `AGENT_POOL_ID`: The agent pool ID that you are creating.



If an agent pool is stuck in the `Creating` state for more than 30 minutes, we recommend deleting the agent pool and creating it again.

Revoking required Storage Transfer Service permissions from a project while an agent pool is in the `Creating` state leads to incorrect service behavior.

###  gcloud CLI 

To create an agent pool with the `gcloud` command line tool, run [`gcloud transfer agent-pools create`][agent-pools-create].
    
    
    gcloud transfer agent-pools create AGENT_POOL
    

Where the following options are available:

  * AGENT_POOL is a unique, permanent identifier for this pool.

  * `--no-async` blocks other tasks in your terminal until the pool has been created. If not included, pool creation runs asynchronously.

  * `--bandwidth-limit` defines how much of your bandwidth in MB/s to make available to this pool's agents. A bandwidth limit applies to all agents in a pool and can help prevent the pool's transfer workload from disrupting other operations that share your bandwidth. For example, enter '50' to set a bandwidth limit of 50 MB/s. By leaving this flag unspecified, this pool's agents will use all bandwidth available to them.

  * `--display-name` is a modifiable name to help you identify this pool. You can include details that might not fit in the pool's unique full resource name.




## Install transfer agents

Transfer agents are software agents that coordinate transfer activities from your source through Storage Transfer Service. They must be installed on a system with access to your source data.

###  gcloud CLI 

To install agents to use with an S3-compatible source using the `gcloud` CLI, use the `transfer agents install` command.

You must provide access credentials either as environment variables as the values of `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, or stored as default credentials in your system's configuration files.
    
    
    export AWS_ACCESS_KEY_ID=ID
    export AWS_SECRET_ACCESS_KEY=SECRET
    gcloud transfer agents install --pool=POOL_NAME
    

To run agents using a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys), use the `--creds-file` option:
    
    
    gcloud transfer agents install --pool=POOL_NAME \
      --creds-file=/relative/path/to/service-account-key.json
    

## Create a transfer job

###  Google Cloud console 

Follow these steps to create a transfer from an S3-compatible source to a Cloud Storage bucket.

  1. Go to the **Storage Transfer Service** page in the Google Cloud console.

[Go to Storage Transfer Service](https://console.cloud.google.com/transfer/)

  2. Click **Create transfer job**. The **Create a transfer job** page is displayed.

  3. Select **S3-compatible object storage** as the **Source type**. The destination must be **Google Cloud Storage**.

Click **Next step**.




### Configure your source

  1. Specify the required information for this transfer:

     1. Select the agent pool you configured for this transfer.

     2. Enter the **Bucket name** relative to the endpoint. For example, if your data resides at:

`https://example.com/bucket_a`

Enter: `bucket_a`

     3. Enter the **Endpoint**. Do not include the protocol (`http://` or `https://`) or the bucket name. For example:

`example.com`

  2. Specify any optional attributes for this transfer:

     1. Enter the **Signing region** to use for signing of requests.

     2. Choose the **Signing process** for this request.

     3. Select the **Addressing style**. This determines whether the bucket name is provided in path-style (e.g., `https://example.com/bucket-name/key-name`) or virtual hosted-style (e.g., `https://bucket-name.example.com/key-name`). Read [Virtual hosting of buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html) in the Amazon documentation for more information.

     4. Select the **Network protocol**.

     5. Select the listing API version to use. Refer to the [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) and [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) documentation for more information.

  3. Click **Next step**.




### Configure your sink

  1. In the **Bucket or folder** field, enter the destination bucket and (optionally) folder name, or click **Browse** to select a bucket from a list of existing buckets in your current project. To create a new bucket, click ![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/agent-based/images/bucket_icon.png)**Create new bucket**.

  2. Click **Next step**.




### Choose transfer settings

  1. In the **Description** field, enter a description of the transfer. As a best practice, enter a description that is meaningful and unique so that you can tell jobs apart.

  2. Under **Metadata options** , choose to use the default options, or click **View and select options** to specify values for all supported metadata. See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

  3. Under **When to overwrite** , select one of the following:

     * **If different** : Overwrites destination files if the source file with the same name has different Etags or checksum values.

     * **Always** : Always overwrites destination files when the source file has the same name, even if they're identical.

  4. Under **When to delete** , select one of the following:

     * **Never** : Never delete files from either the source or destination.

     * **Delete file from source after they're transferred** : Delete files from the source after they're transferred to the destination. If a source file isn't transferred, for example because it already exists in the destination, the source file is not deleted.

**Important:** If you don't have local backup, this option is a non-reversible action.
     * **Delete files from destination if they're not also at source** : If files in the destination Cloud Storage bucket aren't also in the source, then delete the files from the Cloud Storage bucket.

This option ensures that the destination Cloud Storage bucket exactly matches your source.

  5. Under **Notification options** , select your Pub/Sub topic and which events to notify for. See [Pub/Sub notifications](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer) for more details.

  6. Click **Next step**.




### Schedule the transfer

You can schedule your transfer to run one time only, or configure a recurring transfer.

Click **Create** to create the transfer job.

###  gcloud CLI 

Before using the `gcloud` CLI to create a transfer, follow the instructions in [Configure access to a Cloud Storage sink](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).

To use the `gcloud` CLI to create a transfer from an S3-compatible source to a Cloud Storage bucket, use the following command.
    
    
    gcloud transfer jobs create s3://SOURCE_BUCKET_NAME gs://SINK_BUCKET_NAME \
      --source-agent-pool=POOL_NAME \
      --source-endpoint=ENDPOINT \
      --source-signing-region=REGION \
      --source-auth-method=AWS_SIGNATURE_V2 | AWS_SIGNATURE_V4 \
      --source-request-model=PATH_STYLE | VIRTUAL_HOSTED_STYLE \
      --source-network-protocol=HTTP | HTTPS \
      --source-list-api=LIST_OBJECTS | LIST_OBJECTS_V2
    

The following flags are required:

  * `--source-agent-pool` is the name of the agent pool to use for this transfer.

  * `--source-endpoint` specifies your storage system's endpoint. For example, `s3.us-east.example.com`. Check with your provider for the correct formatting. Don't include the protocol (e.g., `https://`) or the bucket name.




The remaining flags are optional:

  * `--source-signing-region` specifies a region for signing requests. Omit this flag if your storage provider doesn't require a signing region.
  * `--source-auth-method` specifies the authentication method to use. Valid values are `AWS_SIGNATURE_V2` or `AWS_SIGNATURE_V4`. Refer to Amazon's [SigV4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) and [SigV2](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html) documentation for more information.
  * `--source-request-model` specifies the addressing style to use. Valid values are `PATH_STYLE` or `VIRTUAL_HOSTED_STYLE`. Path style uses the format `https://s3.REGION.example.com/BUCKET_NAME/KEY_NAME`. Virtual hosted style uses the format `https://BUCKET_NAME.s3.REGION.example.com/KEY_NAME.
  * `--source-network-protocol` specifies the network protocol that agents should use for this job. Valid values are `HTTP` or `HTTPS`.
  * `--source-list-api` specifies the version of the S3 listing API for returning objects from the bucket. Valid values are `LIST_OBJECTS` or `LIST_OBJECTS_V2`. Refer to Amazon's [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) and [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) documentation for more information.



For additional transfer job options, run `gcloud transfer jobs create --help` or refer to the [`gcloud` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create).

###  REST API 

Before using the REST API to create a transfer, follow the instructions in [Configure access to a Cloud Storage sink](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).

To create a transfer from an S3-compatible source using the REST API, create a JSON object similar to the following example.
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
      ...
      "transferSpec": {
        "source_agent_pool_name":"POOL_NAME",
        "awsS3CompatibleData": {
          "region":"us-east-1",
          "s3Metadata":{
            "protocol": "NETWORK_PROTOCOL_HTTPS",
            "requestModel": "REQUEST_MODEL_VIRTUAL_HOSTED_STYLE",
            "authMethod": "AUTH_METHOD_AWS_SIGNATURE_V4"
          },
          "endpoint": "example.com",
          "bucketName": "BUCKET_NAME",
          "path": "PATH",
        },
        "gcsDataSink": {
          "bucketName": "SINK_NAME",
          "path": "SINK_PATH"
        },
        "transferOptions": {
          "deleteObjectsFromSourceAfterTransfer": false
        }
      }
    }
    

See the [`AwsS3CompatibleData` API reference](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#awss3compatibledata) for field descriptions.

###  Client libraries 

Before using the client libraries to create a transfer, follow the instructions in [Configure access to a Cloud Storage sink](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).

### Go

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storagetransfer@v1.0.0/apiv1). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    	"cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func transferFromS3CompatibleSource(w io.Writer, projectID string, sourceAgentPoolName string, sourceBucketName string, sourcePath string, gcsSinkBucket string, gcsPath string) (*storagetransferpb.TransferJob, error) {
    	// Your project id.
    	// projectId := "my-project-id"
    
    	// The agent pool associated with the S3 compatible data source. If not provided, defaults to the default agent.
    	// sourceAgentPoolName := "projects/my-project/agentPools/transfer_service_default"
    
    	// The S3 compatible bucket name to transfer data from.
    	//sourceBucketName = "my-bucket-name"
    
    	// The S3 compatible path (object prefix) to transfer data from.
    	//sourcePath = "path/to/data"
    
    	// The ID of the GCS bucket to transfer data to.
    	//gcsSinkBucket = "my-sink-bucket"
    
    	// The GCS path (object prefix) to transfer data to.
    	//gcsPath = "path/to/data"
    
    	// The S3 region of the source bucket.
    	region := "us-east-1"
    
    	// The S3 compatible endpoint.
    	endpoint := "us-east-1.example.com"
    
    	// The S3 compatible network protocol.
    	protocol := storagetransferpb.[S3CompatibleMetadata_NETWORK_PROTOCOL_HTTPS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_S3CompatibleMetadata_NETWORK_PROTOCOL_UNSPECIFIED_S3CompatibleMetadata_NETWORK_PROTOCOL_HTTPS_S3CompatibleMetadata_NETWORK_PROTOCOL_HTTP)
    
    	// The S3 compatible request model.
    	requestModel := storagetransferpb.[S3CompatibleMetadata_REQUEST_MODEL_VIRTUAL_HOSTED_STYLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_S3CompatibleMetadata_REQUEST_MODEL_UNSPECIFIED_S3CompatibleMetadata_REQUEST_MODEL_VIRTUAL_HOSTED_STYLE_S3CompatibleMetadata_REQUEST_MODEL_PATH_STYLE)
    
    	// The S3 Compatible auth method.
    	authMethod := storagetransferpb.[S3CompatibleMetadata_AUTH_METHOD_AWS_SIGNATURE_V4](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_S3CompatibleMetadata_AUTH_METHOD_UNSPECIFIED_S3CompatibleMetadata_AUTH_METHOD_AWS_SIGNATURE_V4_S3CompatibleMetadata_AUTH_METHOD_AWS_SIGNATURE_V2)
    
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
    				DataSource: &storagetransferpb.TransferSpec_AwsS3CompatibleDataSource{
    					AwsS3CompatibleDataSource: &storagetransferpb.AwsS3CompatibleData{
    						BucketName: sourceBucketName,
    						Path:       sourcePath,
    						Endpoint:   endpoint,
    						Region:     region,
    						DataProvider: &storagetransferpb.AwsS3CompatibleData_S3Metadata{
    							S3Metadata: &storagetransferpb.S3CompatibleMetadata{
    								AuthMethod:   authMethod,
    								RequestModel: requestModel,
    								Protocol:     protocol,
    							},
    						},
    					}},
    				DataSink: &storagetransferpb.TransferSpec_GcsDataSink{
    					GcsDataSink: &storagetransferpb.GcsData{
    						BucketName: gcsSinkBucket,
    						Path:       gcsPath,
    					},
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
    	fmt.Fprintf(w, "Created and ran transfer job from %v to %v with name %v", sourceBucketName, gcsSinkBucket, resp.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name))
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[S3CompatibleMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.html).[AuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.AuthMethod.html);
    import static com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[S3CompatibleMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.html).[NetworkProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.NetworkProtocol.html);
    import static com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[S3CompatibleMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.html).[RequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.RequestModel.html);
    
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html);
    import java.io.IOException;
    
    public class TransferFromS3CompatibleSource {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your project id
        String projectId = "my-project-id";
    
        // The agent pool associated with the S3 compatible data source. If not provided, defaults to
        // the default agent
        String sourceAgentPoolName = "projects/my-project-id/agentPools/transfer_service_default";
    
        // The S3 compatible bucket name to transfer data from
        String sourceBucketName = "my-bucket-name";
    
        // The S3 compatible path (object prefix) to transfer data from
        String sourcePath = "path/to/data";
    
        // The ID of the GCS bucket to transfer data to
        String gcsSinkBucket = "my-sink-bucket";
    
        // The GCS path (object prefix) to transfer data to
        String gcsPath = "path/to/data";
    
        // The S3 region of the source bucket
        String region = "us-east-1";
    
        // The S3 compatible endpoint
        String endpoint = "us-east-1.example.com";
    
        // The S3 compatible network protocol
        [NetworkProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.NetworkProtocol.html) protocol = [NetworkProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.NetworkProtocol.html).NETWORK_PROTOCOL_HTTPS;
    
        // The S3 compatible request model
        [RequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.RequestModel.html) requestModel = [RequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.RequestModel.html).REQUEST_MODEL_VIRTUAL_HOSTED_STYLE;
    
        // The S3 Compatible auth method
        [AuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.AuthMethod.html) authMethod = [AuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.AuthMethod.html).AUTH_METHOD_AWS_SIGNATURE_V4;
    
        transferFromS3CompatibleSource(
            projectId,
            sourceAgentPoolName,
            sourceBucketName,
            sourcePath,
            region,
            endpoint,
            protocol,
            requestModel,
            authMethod,
            gcsSinkBucket,
            gcsPath);
      }
    
      public static void transferFromS3CompatibleSource(
          String projectId,
          String sourceAgentPoolName,
          String sourceBucketName,
          String sourcePath,
          String region,
          String endpoint,
          [NetworkProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.NetworkProtocol.html) protocol,
          [RequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.RequestModel.html) requestModel,
          [AuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.AuthMethod.html) authMethod,
          String gcsSinkBucket,
          String gcsPath)
          throws IOException {
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
            [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).newBuilder()
                .setProjectId(projectId)
                .setTransferSpec(
                    [TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html).newBuilder()
                        .[setSourceAgentPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setSourceAgentPoolName_java_lang_String_)(sourceAgentPoolName)
                        .[setAwsS3CompatibleDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setAwsS3CompatibleDataSource_com_google_storagetransfer_v1_proto_TransferTypes_AwsS3CompatibleData_)(
                            [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).AwsS3CompatibleData.newBuilder()
                                .[setRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsS3CompatibleData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsS3CompatibleData_Builder_setRegion_java_lang_String_)(region)
                                .[setEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsS3CompatibleData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsS3CompatibleData_Builder_setEndpoint_java_lang_String_)(endpoint)
                                .setBucketName(sourceBucketName)
                                .setPath(sourcePath)
                                .[setS3Metadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AwsS3CompatibleData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AwsS3CompatibleData_Builder_setS3Metadata_com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_)(
                                    [TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).S3CompatibleMetadata.newBuilder()
                                        .[setProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_Builder_setProtocol_com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_NetworkProtocol_)(protocol)
                                        .[setRequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_Builder_setRequestModel_com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_RequestModel_)(requestModel)
                                        .[setAuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_Builder_setAuthMethod_com_google_storagetransfer_v1_proto_TransferTypes_S3CompatibleMetadata_AuthMethod_)(authMethod)
                                        .build())
                                .build())
                        .setGcsDataSink(
                            [GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(gcsSinkBucket).setPath(gcsPath).build()))
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
                  + sourceBucketName
                  + " to "
                  + gcsSinkBucket
                  + " with "
                  + "name "
                  + response.getName());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Node.js API reference documentation](https://googleapis.dev/nodejs/storagetransfer/latest/index.html). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const storageTransfer = require('[@google-cloud/storage-transfer](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // Useful enums for AWS S3-Compatible Transfers
    // const {AuthMethod, NetworkProtocol, RequestModel} = storageTransfer.protos.google.storagetransfer.v1.S3CompatibleMetadata;
    
    // Your project id
    // const projectId = 'my-project';
    
    // The agent pool associated with the S3-compatible data source. Defaults to the default agent
    // const sourceAgentPoolName = 'projects/my-project/agentPools/transfer_service_default';
    
    // The S3-compatible bucket name to transfer data from
    // const sourceBucketName = "my-bucket-name";
    
    // The S3-compatible path (object prefix) to transfer data from
    // const sourcePath = "path/to/data/";
    
    // The ID of the GCS bucket to transfer data to
    // const gcsSinkBucket = "my-sink-bucket";
    
    // The GCS path (object prefix) to transfer data to
    // const gcsPath = "path/to/data/";
    
    // The S3 region of the source bucket
    // const region = 'us-east-1';
    
    // The S3-compatible endpoint
    // const endpoint = "us-east-1.example.com";
    
    // The S3-compatible network protocol
    // const protocol = NetworkProtocol.NETWORK_PROTOCOL_HTTPS;
    
    // The S3-compatible request model
    // const requestModel = RequestModel.REQUEST_MODEL_VIRTUAL_HOSTED_STYLE;
    
    // The S3-compatible auth method
    // const authMethod = AuthMethod.AUTH_METHOD_AWS_SIGNATURE_V4;
    
    // Creates a client
    const client = new storageTransfer.[StorageTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)();
    
    /**
     * Creates a transfer from an AWS S3-compatible source to GCS
     */
    async function transferFromS3CompatibleSource() {
      // Runs the request and creates the job
      const [transferJob] = await client.createTransferJob({
        transferJob: {
          projectId,
          transferSpec: {
            sourceAgentPoolName,
            awsS3CompatibleDataSource: {
              region,
              s3Metadata: {
                authMethod,
                protocol,
                requestModel,
              },
              endpoint,
              bucketName: sourceBucketName,
              path: sourcePath,
            },
            gcsDataSink: {
              bucketName: gcsSinkBucket,
              path: gcsPath,
            },
          },
          status: '[ENABLED](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)',
        },
      });
    
      await client.runTransferJob({
        jobName: transferJob.name,
        projectId,
      });
    
      console.log(
        `Created and ran a transfer job from '${sourceBucketName}' to '${gcsSinkBucket}' with name ${transferJob.name}`
      );
    }
    
    transferFromS3CompatibleSource();

### Python

To learn how to install and use the client library for Storage Transfer Service, see [Storage Transfer Service client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Storage Transfer Service Python API reference documentation](https://cloud.google.com/python/docs/reference/storagetransfer/latest). 

To authenticate to Storage Transfer Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import storage_transfer
    
    AuthMethod = storage_transfer.[S3CompatibleMetadata](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.html).[AuthMethod](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.AuthMethod.html)
    NetworkProtocol = storage_transfer.[S3CompatibleMetadata](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.html).[NetworkProtocol](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.NetworkProtocol.html)
    RequestModel = storage_transfer.[S3CompatibleMetadata](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.html).[RequestModel](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.RequestModel.html)
    
    
    def transfer_from_S3_compat_to_gcs(
        project_id: str,
        description: str,
        source_agent_pool_name: str,
        source_bucket_name: str,
        source_path: str,
        gcs_sink_bucket: str,
        gcs_path: str,
        region: str,
        endpoint: str,
        protocol: NetworkProtocol,
        request_model: RequestModel,
        auth_method: AuthMethod,
    ) -> None:
        """Creates a transfer from an AWS S3-compatible source to GCS"""
    
        client = storage_transfer.[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        # The ID of the Google Cloud Platform Project that owns the job
        # project_id = 'my-project'
    
        # A useful description for your transfer job
        # description = 'My transfer job'
    
        # The agent pool associated with the S3-compatible data source.
        # Defaults to 'projects/{project_id}/agentPools/transfer_service_default'
        # source_agent_pool_name = 'projects/my-project/agentPools/my-agent'
    
        # The S3 compatible bucket name to transfer data from
        # source_bucket_name = "my-bucket-name"
    
        # The S3 compatible path (object prefix) to transfer data from
        # source_path = "path/to/data/"
    
        # The ID of the GCS bucket to transfer data to
        # gcs_sink_bucket = "my-sink-bucket"
    
        # The GCS path (object prefix) to transfer data to
        # gcs_path = "path/to/data/"
    
        # The S3 region of the source bucket
        # region = 'us-east-1'
    
        # The S3-compatible endpoint
        # endpoint = "us-east-1.example.com"
    
        # The S3-compatible network protocol
        # protocol = NetworkProtocol.NETWORK_PROTOCOL_HTTPS
    
        # The S3-compatible request model
        # request_model = RequestModel.REQUEST_MODEL_VIRTUAL_HOSTED_STYLE
    
        # The S3-compatible auth method
        # auth_method = AuthMethod.AUTH_METHOD_AWS_SIGNATURE_V4
    
        transfer_job_request = storage_transfer.[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": storage_transfer.[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "source_agent_pool_name": source_agent_pool_name,
                        "aws_s3_compatible_data_source": {
                            "region": region,
                            "s3_metadata": {
                                "auth_method": auth_method,
                                "protocol": protocol,
                                "request_model": request_model,
                            },
                            "endpoint": endpoint,
                            "bucket_name": source_bucket_name,
                            "path": source_path,
                        },
                        "gcs_data_sink": {
                            "bucket_name": gcs_sink_bucket,
                            "path": gcs_path,
                        },
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

## Frequently asked questions

**What if my S3-compatible provider uses a custom SSL certificate?**

If your S3-compatible provider uses an SSL certificate that is not issued by a public certificate authority, your transfers may fail with a TLS error. To resolve this, mount the provider's root certificate to the transfer agent container at `/etc/ssl/certs/CERT_FILE` using the `-v` Docker flag.

For example:
    
    
    sudo docker run --ulimit memlock=64000000 -d --rm \
    -v HOST_DIRECTORY:CONTAINER_DIRECTORY \
    -v PATH/TO/KEY.JSON:/etc/gcloud/key.json:ro \
    **-v /path/to/your/CERT_FILE:/etc/ssl/certs/CERT_FILE** \
    -e AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY \
    gcr.io/cloud-ingest/tsop-agent:latest \
    --project-id=PROJECT_ID \
    --creds-file=/etc/gcloud/key.json \
    --hostname=$(hostname) \
    --agent-pool=POOL_NAME
    

**Is there a cost to transfer from S3-compatible storage?**

Transfers from S3-compatible storage do not incur the "Storage Transfer Service transfers requiring agents" fee. See [Pricing](https://cloud.google.com/storage-transfer/pricing) for any other fees that may be incurred. You may also incur outbound data transfer and operational charges from your source cloud provider.

**Is Cloud Logging supported for S3-compatible storage transfers?**

Yes, you can enable Cloud Logging for your transfers by following the instructions in [Cloud Logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs).

**Are transfers using a manifest supported?**

Yes, [manifest files](https://docs.cloud.google.com/storage-transfer/docs/manifest) are supported for S3-compatible transfers.

**If I add an object to the source bucket after the job has started, is that object transferred?**

Storage Transfer Service performs a list operation on the source bucket to compute the diff from the destination. If the list operation has already completed when the new object is added, that object is skipped until the next transfer.

**Does Storage Transfer Service perform checksum matching on S3-compatible sources?**

Storage Transfer Service relies on checksum data being returned by the source. For S3-compatible storage, Storage Transfer Service expects the object's Etag to be the MD5 hash of the object.

However, any objects that were transferred to S3-compatible storage using S3 multipart upload do not have MD5 ETags. In this case, Storage Transfer Service uses the file size to validate the transferred object.

**What throughput can be achieved for transfers from S3-compatible storage?**

Your transfer throughput can be scaled by adding more transfer agents. We recommend using 3 agents for fault tolerance and to fill a <10Gbps pipe. To scale more, add more agents. Agents can be added and removed while a transfer is in process.

**Where should transfer agents be deployed to transfer data from Amazon S3 to Cloud Storage?**

You can install agents in Amazon EC2 or EKS within the same region as your bucket. You can also run agents on Google Cloud in the nearest region.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
