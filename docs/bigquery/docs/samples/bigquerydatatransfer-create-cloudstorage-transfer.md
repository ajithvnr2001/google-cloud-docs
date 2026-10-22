---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-create-cloudstorage-transfer/
title: Create a data transfer configuration \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:50.237938+00:00
---

# Create a data transfer configuration  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-create-cloudstorage-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a data transfer configuration Stay organized with collections  Save and categorize content based on your preferences. 

Creates a transfer configuration in the BigQuery Data Transfer Service to schedule recurring data transfers from a supported data source into a BigQuery dataset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Load Cloud Storage data into BigQuery](https://docs.cloud.google.com/bigquery/docs/cloud-storage-transfer)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html);
    import com.google.cloud.bigquery.datatransfer.v1.[TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    // Sample to create google cloud storage transfer config
    public class CreateCloudStorageTransfer {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "MY_PROJECT_ID";
        String datasetId = "MY_DATASET_ID";
        String tableId = "MY_TABLE_ID";
        // GCS Uri
        String sourceUri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv";
        String fileFormat = "CSV";
        String fieldDelimiter = ",";
        String skipLeadingRows = "1";
        Map<String, Value> params = new HashMap<>();
        params.put(
            "destination_table_name_template", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(tableId).build());
        params.put("data_path_template", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(sourceUri).build());
        params.put("write_disposition", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("APPEND").build());
        params.put("file_format", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(fileFormat).build());
        params.put("field_delimiter", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(fieldDelimiter).build());
        params.put("skip_leading_rows", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(skipLeadingRows).build());
        [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig =
            [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html).newBuilder()
                .setDestinationDatasetId(datasetId)
                .setDisplayName("Your Google Cloud Storage Config Name")
                .setDataSourceId("google_cloud_storage")
                .setParams([Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder().[putAllFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html#com_google_protobuf_Struct_Builder_putAllFields_java_util_Map_java_lang_String_com_google_protobuf_Value__)(params).build())
                .setSchedule("every 24 hours")
                .build();
        createCloudStorageTransfer(projectId, transferConfig);
      }
    
      public static void createCloudStorageTransfer(String projectId, [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig)
          throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) client = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html) parent = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html).of(projectId);
          [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html) request =
              [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html#com_google_cloud_bigquery_datatransfer_v1_ProjectName_toString__)())
                  .setTransferConfig(transferConfig)
                  .build();
          [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) config = client.createTransferConfig(request);
          System.out.println("Cloud storage transfer created successfully :" + config.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html#com_google_cloud_bigquery_datatransfer_v1_TransferConfig_getName__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("Cloud storage transfer was not created." + ex.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {DataTransferServiceClient} =
      require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Creates a transfer configuration for a Google Cloud Storage transfer.
     *
     * This sample demonstrates how to create a transfer configuration that appends
     * data from Google Cloud Storage to a BigQuery dataset.
     *
     * @param {string} projectId The Google Cloud project ID. (for example, 'example-project-id')
     * @param {string} location The BigQuery location where the transfer config should be created. (for example, 'us-central1')
     * @param {string} sourceDataCloudStorageUri The source data to be transferred into BigQuery.
     *   Expects a Cloud Storage object URI. (for example, 'gs://example-bucket/example-data.csv')
     * @param {string} destinationDatasetId The destination BigQuery dataset ID. (for example, 'example_dataset')
     * @param {string} destinationTableName The destination table in the BigQuery dataset. (for example, 'example_destination_table')
     * @param {string} serviceAccountName The service account used by the data transfer process to read data from Google Cloud Storage.
     *   Make sure it has IAM read access to the sourceDataCloudStorageUri [example IAM role: roles/storage.objectViewer]. (for example, 'data-transfer-service-account@example-project-id.iam.gserviceaccount.com')
     */
    async function createTransferConfig(
      projectId,
      location,
      sourceDataCloudStorageUri,
      destinationDatasetId,
      destinationTableName,
      serviceAccountName,
    ) {
      const transferConfig = {
        destinationDatasetId,
        displayName: 'Example Cloud Storage Transfer',
        dataSourceId: 'google_cloud_storage',
        // Params are in google.protobuf.Struct format.
        params: {
          fields: {
            data_path_template: {stringValue: sourceDataCloudStorageUri},
            destination_table_name_template: {stringValue: destinationTableName},
            file_format: {stringValue: 'CSV'},
            skip_leading_rows: {stringValue: '1'},
          },
        },
      };
    
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        transferConfig,
        serviceAccountName,
      };
    
      try {
        const [config] = await client.createTransferConfig(request);
        console.log(`Created transfer config: ${config.name}`);
        console.log(`  Display Name: ${config.displayName}`);
        console.log(`  Data Source ID: ${config.dataSourceId}`);
        console.log(`  Destination Dataset ID: ${config.destinationDatasetId}`);
      } catch (err) {
        if (err.code === status.INVALID_ARGUMENT) {
          console.error(
            `Error: Invalid argument provided for creating Migration '${transferConfig.displayName}'. ` +
              `Details: ${err.message}. Make sure request parameters are valid.`,
          );
          console.error(err);
        } else {
          console.error('Error creating transfer config:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest)
    from google.protobuf import struct_pb2
    
    client = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    
    def create_transfer_config(
        project_id: str,
        location: str,
        source_cloud_storage_uri: str,
        destination_dataset_id: str,
        destination_table_name: str,
        service_account: str = None,
    ) -> None:
        """Creates a transfer configuration for a Google Cloud Storage transfer.
    
        This sample demonstrates how to create a transfer configuration for a
        one-time Google Cloud Storage transfer. It specifies the source data path,
        destination table, and other parameters for the transfer.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the transfer config, for example "us-central1"
            source_data_path: The Cloud Storage URL of the source data, for example "gs://example-bucket/example-data.csv"
            destination_dataset_id: The BigQuery dataset ID to which data is transferred.
            destination_table_name: The BigQuery table name to which data is transferred.
                Cloud Storage transfers support runtime parameters https://docs.cloud.google.com/bigquery/docs/gcs-transfer-parameters
            service_account: The optional IAM Service Account to use as the transfer owner. Otherwise, the current user is the owner.
        """
    
        parent = f"projects/{project_id}/locations/{location}"
        data_source_id = "google_cloud_storage"
        params = struct_pb2.Struct()
        params.update(
            {
                "data_path_template": source_cloud_storage_uri,
                "destination_table_name_template": destination_table_name,
                "file_format": "CSV",
                "skip_leading_rows": "1",  # assumes the first line in the CSV is the header
            }
        )
        transfer_config = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[TransferConfig](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig.html)(
            display_name="My Cloud Storage Data Transfer",
            data_source_id=data_source_id,
            destination_dataset_id=destination_dataset_id,
            params=params,
        )
    
        try:
            request = [bigquery_datatransfer_v1](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest).[CreateTransferConfigRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.CreateTransferConfigRequest.html)(
                parent=parent,
                transfer_config=transfer_config,
                service_account_name=service_account,
            )
    
            response = client.[create_transfer_config](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_create_transfer_config)(request=request)
            print(f"Created transfer config: {response.name}")
        except google.api_core.exceptions.InvalidArgument as e:
            print(
                f"Error: Could not create transfer config due to an invalid argument: {e}. Please check the destination dataset and other parameters."
            )
        except google.api_core.exceptions.GoogleAPICallError as e:
            print(f"Error: Could not create transfer config: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
