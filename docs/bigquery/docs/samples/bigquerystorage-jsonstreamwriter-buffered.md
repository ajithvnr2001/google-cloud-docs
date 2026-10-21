---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-buffered/
title: Append buffered records \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:43.221735+00:00
---

# Append buffered records  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-buffered/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Append buffered records Stay organized with collections  Save and categorize content based on your preferences. 

Use the JSON stream writer to append records in buffered mode

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.bigquery.storage.v1.[AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html);
    import com.google.cloud.bigquery.storage.v1.[CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html);
    import com.google.cloud.bigquery.storage.v1.[FinalizeWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest.html);
    import com.google.cloud.bigquery.storage.v1.[FlushRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsRequest.html);
    import com.google.cloud.bigquery.storage.v1.[FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html);
    import com.google.cloud.bigquery.storage.v1.[TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html);
    import com.google.cloud.bigquery.storage.v1.[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html);
    import com.google.protobuf.[Descriptors](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.html).[DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html);
    import com.google.protobuf.[Int64Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import org.json.JSONArray;
    import org.json.JSONObject;
    import org.threeten.bp.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class WriteBufferedStream {
    
      public static void runWriteBufferedStream()
          throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), InterruptedException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
    
        writeBufferedStream(projectId, datasetName, tableName);
      }
    
      public static void writeBufferedStream(String projectId, String datasetName, String tableName)
          throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), InterruptedException, IOException {
        try ([BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html) client = [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html).create()) {
          // Initialize a write stream for the specified table.
          // For more information on WriteStream.Type, see:
          // https://googleapis.dev/java/google-cloud-bigquerystorage/latest/com/google/cloud/bigquery/storage/v1/WriteStream.Type.html
          [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html) stream = [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html).newBuilder().setType([WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html).Type.BUFFERED).build();
          [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable = [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html).of(projectId, datasetName, tableName);
          [CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html) createWriteStreamRequest =
              [CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html).newBuilder()
                  .setParent(parentTable.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_toString__)())
                  .setWriteStream(stream)
                  .build();
          [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html) writeStream = client.createWriteStream(createWriteStreamRequest);
    
          // Configure in-stream automatic retry settings.
          // Error codes that are immediately retried:
          // * ABORTED, UNAVAILABLE, CANCELLED, INTERNAL, DEADLINE_EXCEEDED
          // Error codes that are retried with exponential backoff:
          // * RESOURCE_EXHAUSTED
          [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html) retrySettings =
              [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                  .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMillis(500))
                  .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.1)
                  .[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxAttempts_int_)(5)
                  .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMinutes(1))
                  .build();
    
          // Use the JSON stream writer to send records in JSON format.
          // For more information about JsonStreamWriter, see:
          // https://cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter
          try ([JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html) writer =
              [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html).newBuilder(writeStream.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getName__)(), writeStream.[getTableSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getTableSchema__)())
                  .setRetrySettings(retrySettings)
                  .build()) {
            // Write two batches to the stream, each with 10 JSON records.
            for (int i = 0; i < 2; i++) {
              JSONArray jsonArr = new JSONArray();
              for (int j = 0; j < 10; j++) {
                // Create a JSON object that is compatible with the table schema.
                JSONObject record = new JSONObject();
                record.put("col1", String.format("buffered-record %03d", i));
                jsonArr.put(record);
              }
              ApiFuture<AppendRowsResponse> future = writer.append(jsonArr);
              [AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html) response = future.get();
            }
            // Flush the buffer.
            [FlushRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsRequest.html) flushRowsRequest =
                [FlushRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsRequest.html).newBuilder()
                    .setWriteStream(writeStream.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getName__)())
                    .setOffset([Int64Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html).of(10 * 2 - 1)) // Advance the cursor to the latest record.
                    .build();
            [FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse.html) flushRowsResponse = client.flushRows(flushRowsRequest);
            // You can continue to write to the stream after flushing the buffer.
          }
          // Finalize the stream after use.
          [FinalizeWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest.html) finalizeWriteStreamRequest =
              [FinalizeWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest.html).newBuilder().setName(writeStream.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getName__)()).build();
          client.finalizeWriteStream(finalizeWriteStreamRequest);
          System.out.println("Appended and committed records successfully.");
        } catch (ExecutionException e) {
          // If the wrapped exception is a StatusRuntimeException, check the state of the operation.
          // If the state is INTERNAL, CANCELLED, or ABORTED, you can retry. For more information, see:
          // https://grpc.github.io/grpc-java/javadoc/io/grpc/StatusRuntimeException.html
          System.out.println(e);
        }
      }
    }

### Rust
    
    
    use anyhow::Result;
    use arrow::datatypes::{DataType, Field, Schema};
    use arrow::ipc::writer::StreamWriter;
    use arrow_json::ReaderBuilder;
    use google_cloud_bigquery::client::Write;
    use google_cloud_bigquery::model::{ArrowRecordBatch, ArrowSchema};
    use google_cloud_bigquery::write::BufferedWriter;
    use google_cloud_bigquery::write::format::Arrow;
    use std::sync::Arc;
    use tokio::task::JoinSet;
    
    // The client library doesn't support a built-in JSON API surface.
    //
    // This example demonstrates how to write JSON data to BigQuery by first
    // converting it to Arrow record batches using the `arrow-json` crate.
    
    pub async fn sample(project_id: &str, dataset_id: &str, table_id: &str) -> anyhow::Result<()> {
        let client = Write::builder().build().await?;
    
        // Define the table schema
        let schema = Arc::new(Schema::new(vec![
            Field::new("string", DataType::Utf8, false),
            Field::new("int", DataType::Int64, false),
        ]));
    
        // Initialize an IPC stream writer and extract the serialized schema
        let mut ipc_writer = StreamWriter::try_new(Vec::new(), &schema)?;
        let schema_buf = std::mem::take(ipc_writer.get_mut());
    
        let table = format!("projects/{project_id}/datasets/{dataset_id}/tables/{table_id}");
        // Create a writer for a buffered stream
        let writer: BufferedWriter<Arrow> = client
            .create_stream(table)
            .build_arrow(ArrowSchema::new().set_serialized_schema(schema_buf))
            .await?;
    
        // Create a decoder to convert JSON to Arrow
        let mut decoder = ReaderBuilder::new(schema).build_decoder()?;
    
        let mut writes = JoinSet::new();
        for i in 0..100 {
            for j in 0..10 {
                // Generate example data (JSON bytes)
                let json = format!(r#"{{"string": "batch {i}", "int": {}}}"#, 10 * i + j);
                let _ = decoder.decode(json.as_bytes())?;
            }
            if let Some(batch) = decoder.flush()? {
                // Serialize the batch
                let batch = {
                    ipc_writer.write(&batch)?;
                    let batch_bytes = std::mem::take(ipc_writer.get_mut());
                    ArrowRecordBatch::new().set_serialized_record_batch(batch_bytes)
                };
                // Write the batch to the buffered stream
                writes.spawn(writer.append(batch).set_offset(10 * i).send());
            }
        }
        let results: Result<Vec<_>, _> = writes.join_all().await.into_iter().collect();
        let _ = results?;
    
        // Flush the buffered rows. Note that the flush offset is inclusive.
        let resp = writer.flush(999).await?;
        println!("Successfully flushed up to offset {}", resp.offset);
    
        // Finalize the stream, preventing further writes
        let resp = writer.finalize().await?;
        println!(
            "Successfully finalized the stream with {} rows",
            resp.row_count
        );
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
