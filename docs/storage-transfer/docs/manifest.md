---
url: https://docs.cloud.google.com/storage-transfer/docs/manifest/
title: Transfer specific files or objects using a manifest \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:42.080537+00:00
---

# Transfer specific files or objects using a manifest  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/manifest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer specific files or objects using a manifest Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports the transfer of specific files or objects, which are specified using a _manifest_. A manifest is a CSV file, uploaded to Cloud Storage, that contains a list of files or objects for Storage Transfer Service to act upon.

A manifest can be used for the following transfers:

  * From AWS S3, S3-compatible storage, Azure Blobstore, or Cloud Storage to a Cloud Storage bucket.

  * From a file system to a Cloud Storage bucket.

  * From a Cloud Storage bucket to a file system.

  * Between two file systems.

  * From a publicly-accessible HTTP/HTTPS source to a Cloud Storage bucket. Follow the instructions in [Create a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list) as the manifest format is unique for URL lists.




## Create a manifest

Manifest files have the following requirements:

  * Manifests must be formatted as CSV.
  * They can contain any UTF-8 characters.
  * The first column must be a filename or object name. The name is relative to the root path or the bucket and folder specified in the transfer job; see File system transfers and Object storage transfers for details.
  * Manifest files do not support wildcards. Folder names without a file or object name are not supported.
  * If a file or object name contains a comma, the name must be enclosed in double-quotes. For example, `"doe,john.txt"`.
  * There is no limit to the size of the manifest file.



We recommend testing your transfer with a small subset of files or objects to avoid unnecessary API calls due to configuration errors.

You can monitor the status of file transfers from the [Transfer Jobs page](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#monitoring-jobs). Files or objects that fail to transfer are listed in the [transfer logs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#viewing-logs).

### File system transfers

To create a manifest of files on a file system, create a CSV file with a single column containing the file paths relative to the root directory specified in the transfer job creation.

For example, to transfer the following file system files:

File path  
---  
`rootdir/dir1/subdir1/file1.txt`  
`rootdir/file2.txt`  
`rootdir/dir2/subdir1/file3.txt`  
  
Your manifest should look like the following example:
    
    
    dir1/subdir1/file1.txt
    file2.txt
    dir2/subdir1/file3.txt
    

Save the manifest file with any filename, and a `.csv` extension.

### Object storage transfers

To create a manifest of objects, create a CSV file whose first column contains the object names relative to the bucket name and path specified in the transfer job creation. All objects must be in the same bucket.

You can also specify an optional second column with the Cloud Storage generation number of the specific version to transfer.

For example, you may wish to transfer the following objects:

Object path | Cloud Storage generation number  
---|---  
`SOURCE_PATH/object1.pdf` | 1664826685911832  
`SOURCE_PATH/object2.pdf` |   
`SOURCE_PATH/object3.pdf` | 1664826610699837  
  
Your manifest should look like the following example:
    
    
    object1.pdf,1664826685911832
    object2.pdf
    object3.pdf,1664826610699837
    

Save the manifest file with any filename, and a `.csv` extension.

### HTTP/HTTPS transfers

To transfer specific files from an HTTP or HTTPS source, refer to the instructions in [Create a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list).

## Publish the manifest

Once you've created the manifest, you must make it available to Storage Transfer Service. Storage Transfer Service can access the file in a Cloud Storage bucket, or on your file system.

### Upload the manifest to Cloud Storage

You can store the manifest file in any Cloud Storage bucket.

The service agent running the transfer must have `storage.objects.get` permission for the bucket containing the manifest. See [Grant the required permissions](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions) for instructions on finding the service agent ID, and granting permissions to that service agent on a bucket.

For instructions on uploading the manifest to a bucket, see [Upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects) in the Cloud Storage documentation.

For example, to use the `gcloud` CLI to upload a file to Cloud Storage, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp MANIFEST.CSV gs://DESTINATION_BUCKET_NAME/

Replace the following:

  * `MANIFEST.CSV` is the local path to your manifest file. For example, `Desktop/manifest01.csv`.

  * `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.




If successful, the response looks like the following example:
    
    
    Completed files 1/1 | 164.3kiB/164.3kiB

You can encrypt a manifest using customer-managed [Cloud KMS encryption keys](https://docs.cloud.google.com/kms/docs/cmek). In this case, ensure that any service accounts accessing the manifest are [assigned the applicable encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access). Customer-supplied keys are not supported.

### Store the manifest on a file system

You can store the manifest file on your source or destination file system.

The location of the file must be accessible to the transfer agents. If you [restrict directory access](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access) for your agents, make sure the manifest file is located within a mounted directory.

## Start a transfer

Do not modify the manifest file until a transfer operation completes. We recommend that you lock the manifest file when a transfer is taking place.

###  Cloud console 

To start a transfer with a manifest from the Cloud console:

  1. Follow the instructions in [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) to select your source, destination, and options.

  2. In the final step, **Choose settings** , select the checkbox named **Provide list of files to transfer via manifest file**.

  3. Enter the manifest file location.




###  gcloud 

To transfer the files or objects that are listed in the manifest, include the `--manifest-file=MANIFEST_FILE` flag with your `gcloud transfer jobs create` command.
    
    
    gcloud transfer jobs create SOURCE DESTINATION \
      --manifest-file=MANIFEST_FILE
    

MANIFEST_FILE can be any of the following values:

  * The path to the CSV file in a Cloud Storage bucket:
        
        --manifest-file=gs://my_bucket/sample_manifest.csv
        

See Upload the manifest to Cloud Storage for details on required permissions, if the bucket or file is not public.

  * The relative path from the file system SOURCE, including any path that was specified:
        
        --manifest-file=source://relative_path/sample_manifest.csv
        

  * The relative path from the file system DESTINATION, including any path that was specified:
        
        --manifest-file=destination://relative_path/sample_manifest.csv
        




###  REST + Client libraries 

### REST

To transfer the files or objects that are listed in the manifest, make a `createTransferJob` API call that specifies a `transferSpec` with the `transferManifest` field added. For example:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    ...
      "transferSpec": {
          "posixDataSource": {
              "rootDirectory": "/home/",
          },
          "gcsDataSink": {
              "bucketName": "GCS_NEARLINE_SINK_NAME",
              "path": "GCS_SINK_PATH",
          },
          **"transferManifest": {
              "location": "gs://my_bucket/sample_manifest.csv"**
          }
      }
    

The manifest file can be stored in a Cloud Storage bucket, or on the source or destination file system. Cloud Storage buckets must use the `gs://` prefix and include the full path, including the bucket name. File system locations must use a `source://` or `destination://` prefix and are relative to the file system source or destination, and optional root directory.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    	"cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func transferUsingManifest(w io.Writer, projectID string, sourceAgentPoolName string, rootDirectory string, gcsSinkBucket string, manifestBucket string, manifestObjectName string) (*storagetransferpb.TransferJob, error) {
    	// Your project id
    	// projectId := "myproject-id"
    
    	// The agent pool associated with the POSIX data source. If not provided, defaults to the default agent
    	// sourceAgentPoolName := "projects/my-project/agentPools/transfer_service_default"
    
    	// The root directory path on the source filesystem
    	// rootDirectory := "/directory/to/transfer/source"
    
    	// The ID of the GCS bucket to transfer data to
    	// gcsSinkBucket := "my-sink-bucket"
    
    	// The ID of the GCS bucket that contains the manifest file
    	// manifestBucket := "my-manifest-bucket"
    
    	// The name of the manifest file in manifestBucket that specifies which objects to transfer
    	// manifestObjectName := "path/to/manifest.csv"
    
    	ctx := context.Background()
    	client, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storagetransfer.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	manifestLocation := "gs://" + manifestBucket + "/" + manifestObjectName
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
    				TransferManifest: &storagetransferpb.TransferManifest{Location: manifestLocation},
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
    	fmt.Fprintf(w, "Created and ran transfer job from %v to %v using manifest file %v with name %v", rootDirectory, gcsSinkBucket, manifestLocation, resp.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name))
    	return resp, nil
    }
    

### Java
    
    
    import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html);
    import com.google.storagetransfer.v1.proto.[TransferProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferManifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferManifest.html);
    import com.google.storagetransfer.v1.proto.[TransferTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html);
    import java.io.IOException;
    
    public class TransferUsingManifest {
    
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
    
        // The ID of the GCS bucket which has your manifest file
        String manifestBucket = "my-bucket";
    
        // The ID of the object in manifestBucket that specifies which files to transfer
        String manifestObjectName = "path/to/manifest.csv";
    
        transferUsingManifest(
            projectId,
            sourceAgentPoolName,
            rootDirectory,
            gcsSinkBucket,
            manifestBucket,
            manifestObjectName);
      }
    
      public static void transferUsingManifest(
          String projectId,
          String sourceAgentPoolName,
          String rootDirectory,
          String gcsSinkBucket,
          String manifestBucket,
          String manifestObjectName)
          throws IOException {
        String manifestLocation = "gs://" + manifestBucket + "/" + manifestObjectName;
        [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob =
            [TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).newBuilder()
                .setProjectId(projectId)
                .setTransferSpec(
                    [TransferSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html).newBuilder()
                        .[setSourceAgentPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setSourceAgentPoolName_java_lang_String_)(sourceAgentPoolName)
                        .[setPosixDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setPosixDataSource_com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_)(
                            [PosixFilesystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.html).newBuilder().[setRootDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.PosixFilesystem.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_PosixFilesystem_Builder_setRootDirectory_java_lang_String_)(rootDirectory).build())
                        .setGcsDataSink(([GcsData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html).newBuilder().setBucketName(gcsSinkBucket)).build())
                        .[setTransferManifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setTransferManifest_com_google_storagetransfer_v1_proto_TransferTypes_TransferManifest_)(
                            [TransferManifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferManifest.html).newBuilder().[setLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferManifest.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferManifest_Builder_setLocation_java_lang_String_)(manifestLocation).build()))
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
                  + gcsSinkBucket
                  + " using "
                  + "manifest file "
                  + manifestLocation
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
    
    // The root directory path on the source filesystem
    // const rootDirectory = '/directory/to/transfer/source'
    
    // The ID of the GCS bucket to transfer data to
    // const gcsSinkBucket = 'my-sink-bucket'
    
    // Transfer manifest location. Must be a `gs:` URL
    // const manifestLocation = 'gs://my-bucket/sample_manifest.csv'
    
    // Creates a client
    const client = new [StorageTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)();
    
    /**
     * Creates a request to transfer from the local file system to the sink bucket
     */
    async function transferViaManifest() {
      const createRequest = {
        transferJob: {
          projectId,
          transferSpec: {
            sourceAgentPoolName,
            posixDataSource: {
              rootDirectory,
            },
            gcsDataSink: {bucketName: gcsSinkBucket},
            transferManifest: {
              location: manifestLocation,
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
        `Created and ran a transfer job from '${rootDirectory}' to '${gcsSinkBucket}' using manifest \`${manifestLocation}\` with name ${transferJob.name}`
      );
    }
    
    transferViaManifest();

### Python
    
    
    from google.cloud import storage_transfer
    
    
    def create_transfer_with_manifest(
        project_id: str,
        description: str,
        source_agent_pool_name: str,
        root_directory: str,
        sink_bucket: str,
        manifest_location: str,
    ):
        """Create a transfer from a POSIX file system to a GCS bucket using
        a manifest file."""
    
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
    
        # Google Cloud Storage destination bucket name
        # sink_bucket = 'my-gcs-destination-bucket'
    
        # Transfer manifest location. Must be a `gs:` URL
        # manifest_location = 'gs://my-bucket/sample_manifest.csv'
    
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
                        "gcs_data_sink": {
                            "bucket_name": sink_bucket,
                        },
                        "transfer_manifest": {"location": manifest_location},
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transferJob: {result.name}")
    
    

The objects or files in the manifest aren't necessarily transferred in the listed order.

If the manifest includes files that already exist in the destination, those files are skipped unless the **overwrite objects already existing in sink** option is specified.

If the manifest includes objects that exist in a different version in the destination, the object in the destination is overwritten with the source version of the object. If the destination is a versioned bucket, a new version of the object is created.

## What's next

  * Learn how to filter objects from transfers:

    * [By prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers)
    * [By storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class)
    * [By last modified time](https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified)
  * Learn how to [schedule transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/schedule-transfer-jobs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
