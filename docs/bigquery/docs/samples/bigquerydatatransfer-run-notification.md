---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-run-notification/
title: Create a transfer configuration with run notifications \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:54.405339+00:00
---

# Create a transfer configuration with run notifications  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-run-notification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a transfer configuration with run notifications Stay organized with collections  Save and categorize content based on your preferences. 

Create a transfer configuration, where notifications are sent to Cloud Pub/Sub when a transfer run succeeds or fails.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Data Transfer Service run notifications](https://docs.cloud.google.com/bigquery/docs/transfer-run-notifications)



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
    
    // Sample to get run notification
    public class RunNotification {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "MY_PROJECT_ID";
        final String datasetId = "MY_DATASET_ID";
        final String pubsubTopicName = "MY_TOPIC_NAME";
        final String query =
            "SELECT CURRENT_TIMESTAMP() as current_time, @run_time as intended_run_time, "
                + "@run_date as intended_run_date, 17 as some_integer";
        Map<String, Value> params = new HashMap<>();
        params.put("query", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(query).build());
        params.put(
            "destination_table_name_template",
            [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("my_destination_table_{run_date}").build());
        params.put("write_disposition", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("WRITE_TRUNCATE").build());
        params.put("partitioning_field", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().build());
        [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig =
            [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html).newBuilder()
                .setDestinationDatasetId(datasetId)
                .setDisplayName("Your Scheduled Query Name")
                .setDataSourceId("scheduled_query")
                .setParams([Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder().[putAllFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html#com_google_protobuf_Struct_Builder_putAllFields_java_util_Map_java_lang_String_com_google_protobuf_Value__)(params).build())
                .setSchedule("every 24 hours")
                .setNotificationPubsubTopic(pubsubTopicName)
                .build();
        runNotification(projectId, transferConfig);
      }
    
      public static void runNotification(String projectId, [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) transferConfig)
          throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html) parent = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html).of(projectId);
          [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html) request =
              [CreateTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ProjectName.html#com_google_cloud_bigquery_datatransfer_v1_ProjectName_toString__)())
                  .setTransferConfig(transferConfig)
                  .build();
          [TransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html) config = dataTransferServiceClient.createTransferConfig(request);
          System.out.println(
              "\nScheduled query with run notification created successfully :" + config.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TransferConfig.html#com_google_cloud_bigquery_datatransfer_v1_TransferConfig_getName__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("\nScheduled query with run notification was not created." + ex.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    transfer_config_name = "projects/1234/locations/us/transferConfigs/abcd"
    pubsub_topic = "projects/PROJECT-ID/topics/TOPIC-ID"
    from google.cloud import bigquery_datatransfer
    from google.protobuf import field_mask_pb2
    
    transfer_client = bigquery_datatransfer.[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    transfer_config = bigquery_datatransfer.[TransferConfig](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig.html)(name=transfer_config_name)
    transfer_config.notification_pubsub_topic = pubsub_topic
    update_mask = field_mask_pb2.FieldMask(paths=["notification_pubsub_topic"])
    
    transfer_config = transfer_client.[update_transfer_config](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_update_transfer_config)(
        {"transfer_config": transfer_config, "update_mask": update_mask}
    )
    
    print(f"Updated config: '{transfer_config.name}'")
    print(f"Notification Pub/Sub topic: '{transfer_config.notification_pubsub_topic}'")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
