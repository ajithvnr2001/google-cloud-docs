---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-copy-dataset/
title: Copy a dataset \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:45.580099+00:00
---

# Copy a dataset  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-copy-dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Copy a dataset Stay organized with collections  Save and categorize content based on your preferences. 

Create a transfer configuration to copy all tables in a dataset across projects, locations, or both.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets)



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
    
    // Sample to copy dataset from another gcp project
    public class CopyDataset {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        final String destinationProjectId = "MY_DESTINATION_PROJECT_ID";
        final String destinationDatasetId = "MY_DESTINATION_DATASET_ID";
        final String sourceProjectId = "MY_SOURCE_PROJECT_ID";
        final String sourceDatasetId = "MY_SOURCE_DATASET_ID";
        Map<String, Value> params = new HashMap<>();
        params.put("source_project_id", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(sourceProjectId).build());
        params.put("source_dataset_id", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(sourceDatasetId).build());
        [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig =
            [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html).newBuilder()
                .setDestinationDatasetId(destinationDatasetId)
                .setDisplayName("Your Dataset Copy Name")
                .setDataSourceId("cross_region_copy")
                .setParams([Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder().[putAllFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html#com_google_protobuf_Struct_Builder_putAllFields_java_util_Map_java_lang_String_com_google_protobuf_Value__)(params).build())
                .setSchedule("every 24 hours")
                .build();
        copyDataset(destinationProjectId, transferConfig);
      }
    
      public static void copyDataset(String projectId, [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig)
          throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html) parent = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html).of(projectId);
          [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html) request =
              [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html#com_google_cloud_bigquery_datatransfer_v1_ProjectName_toString__)())
                  .setTransferConfig(transferConfig)
                  .build();
          [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) config = dataTransferServiceClient.createTransferConfig(request);
          System.out.println("Copy dataset created successfully :" + config.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html#com_google_cloud_bigquery_datatransfer_v1_TransferConfig_getName__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("Copy dataset was not created." + ex.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import bigquery_datatransfer
    
    transfer_client = bigquery_datatransfer.[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    destination_project_id = "my-destination-project"
    destination_dataset_id = "my_destination_dataset"
    source_project_id = "my-source-project"
    source_dataset_id = "my_source_dataset"
    transfer_config = bigquery_datatransfer.[TransferConfig](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig.html)(
        destination_dataset_id=destination_dataset_id,
        display_name="Your Dataset Copy Name",
        data_source_id="cross_region_copy",
        params={
            "source_project_id": source_project_id,
            "source_dataset_id": source_dataset_id,
        },
        schedule="every 24 hours",
    )
    transfer_config = transfer_client.[create_transfer_config](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_create_transfer_config)(
        parent=transfer_client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_common_project_path)(destination_project_id),
        transfer_config=transfer_config,
    )
    print(f"Created transfer config: {transfer_config.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
