---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-pending/
title: Append pending records \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:20.609445+00:00
---

# Append pending records  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-pending/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Append pending records Stay organized with collections  Save and categorize content based on your preferences. 

Use the JSON stream writer to append pending records.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch load data using the Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api-batch)
  * [Batch load data using the Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api-batch-load)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutureCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.bigquery.storage.v1.[AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest.html);
    import com.google.cloud.bigquery.storage.v1.[BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html);
    import com.google.cloud.bigquery.storage.v1.[CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html);
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html);
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.StorageException.html);
    import com.google.cloud.bigquery.storage.v1.[FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse.html);
    import com.google.cloud.bigquery.storage.v1.[JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html);
    import com.google.cloud.bigquery.storage.v1.[StorageError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError.html);
    import com.google.cloud.bigquery.storage.v1.[TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html);
    import com.google.cloud.bigquery.storage.v1.[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.protobuf.Descriptors.DescriptorValidationException;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.Phaser;
    import javax.annotation.concurrent.GuardedBy;
    import org.json.JSONArray;
    import org.json.JSONObject;
    import org.threeten.bp.Duration;
    
    public class WritePendingStream {
    
      public static void runWritePendingStream()
          throws DescriptorValidationException, InterruptedException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
    
        writePendingStream(projectId, datasetName, tableName);
      }
    
      public static void writePendingStream(String projectId, String datasetName, String tableName)
          throws DescriptorValidationException, InterruptedException, IOException {
        [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html) client = [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html).create();
        [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable = [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html).of(projectId, datasetName, tableName);
    
        DataWriter writer = new DataWriter();
        // One time initialization.
        writer.initialize(parentTable, client);
    
        try {
          // Write two batches of fake data to the stream, each with 10 JSON records.  Data may be
          // batched up to the maximum request size:
          // https://cloud.google.com/bigquery/quotas#write-api-limits
          long offset = 0;
          for (int i = 0; i < 2; i++) {
            // Create a JSON object that is compatible with the table schema.
            JSONArray jsonArr = new JSONArray();
            for (int j = 0; j < 10; j++) {
              JSONObject record = new JSONObject();
              record.put("col1", String.format("batch-record %03d-%03d", i, j));
              jsonArr.put(record);
            }
            writer.append(jsonArr, offset);
            offset += jsonArr.length();
          }
        } catch (ExecutionException e) {
          // If the wrapped exception is a StatusRuntimeException, check the state of the operation.
          // If the state is INTERNAL, CANCELLED, or ABORTED, you can retry. For more information, see:
          // https://grpc.github.io/grpc-java/javadoc/io/grpc/StatusRuntimeException.html
          System.out.println("Failed to append records. \n" + e);
        }
    
        // Final cleanup for the stream.
        writer.cleanup(client);
        System.out.println("Appended records successfully.");
    
        // Once all streams are done, if all writes were successful, commit all of them in one request.
        // This example only has the one stream. If any streams failed, their workload may be
        // retried on a new stream, and then only the successful stream should be included in the
        // commit.
        [BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest.html) commitRequest =
            [BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest.html).newBuilder()
                .setParent(parentTable.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_toString__)())
                .[addWriteStreams](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest.Builder.html#com_google_cloud_bigquery_storage_v1_BatchCommitWriteStreamsRequest_Builder_addWriteStreams_java_lang_String_)(writer.getStreamName())
                .build();
        [BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse.html) commitResponse = client.[batchCommitWriteStreams](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html#com_google_cloud_bigquery_storage_v1_BigQueryWriteClient_batchCommitWriteStreams__org_jspecify_annotations_Nullable_com_google_cloud_bigquery_storage_v1_TableName_)(commitRequest);
        // If the response does not have a commit time, it means the commit operation failed.
        if (commitResponse.[hasCommitTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse.html#com_google_cloud_bigquery_storage_v1_BatchCommitWriteStreamsResponse_hasCommitTime__)() == false) {
          for ([StorageError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError.html) err : commitResponse.[getStreamErrorsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse.html#com_google_cloud_bigquery_storage_v1_BatchCommitWriteStreamsResponse_getStreamErrorsList__)()) {
            System.out.println(err.getErrorMessage());
          }
          throw new RuntimeException("Error committing the streams");
        }
        System.out.println("Appended and committed records successfully.");
      }
    
      // A simple wrapper object showing how the stateful stream writer should be used.
      private static class DataWriter {
    
        private [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html) streamWriter;
        // Track the number of in-flight requests to wait for all responses before shutting down.
        private final Phaser inflightRequestCount = new Phaser(1);
    
        private final Object lock = new Object();
    
        @GuardedBy("lock")
        private RuntimeException error = null;
    
        void initialize([TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable, [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html) client)
            throws IOException, DescriptorValidationException, InterruptedException {
          // Initialize a write stream for the specified table.
          // For more information on WriteStream.Type, see:
          // https://googleapis.dev/java/google-cloud-bigquerystorage/latest/com/google/cloud/bigquery/storage/v1/WriteStream.Type.html
          [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html) stream = [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html).newBuilder().setType([WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html).Type.PENDING).build();
    
          // Configure in-stream automatic retry settings.
          // Error codes that are immediately retried:
          // * ABORTED, UNAVAILABLE, CANCELLED, INTERNAL, DEADLINE_EXCEEDED
          // Error codes that are retried with exponential backoff:
          // * RESOURCE_EXHAUSTED
          [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html) retrySettings =
              [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                  .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(500))
                  .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.1)
                  .[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxAttempts_int_)(5)
                  .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMinutes(1))
                  .build();
    
          [CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html) createWriteStreamRequest =
              [CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest.html).newBuilder()
                  .setParent(parentTable.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_toString__)())
                  .setWriteStream(stream)
                  .build();
          [WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html) writeStream = client.[createWriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html#com_google_cloud_bigquery_storage_v1_BigQueryWriteClient_createWriteStream__org_jspecify_annotations_Nullable_com_google_cloud_bigquery_storage_v1_TableName_com_google_cloud_bigquery_storage_v1_WriteStream_)([createWriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html#com_google_cloud_bigquery_storage_v1_BigQueryWriteClient_createWriteStream__org_jspecify_annotations_Nullable_com_google_cloud_bigquery_storage_v1_TableName_com_google_cloud_bigquery_storage_v1_WriteStream_)Request);
    
          // Use the JSON stream writer to send records in JSON format.
          // For more information about JsonStreamWriter, see:
          // https://cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter
          streamWriter =
              [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html).newBuilder(writeStream.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getName__)(), writeStream.[getTableSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.html#com_google_cloud_bigquery_storage_v1_WriteStream_getTableSchema__)())
                  .setRetrySettings(retrySettings)
                  .build();
        }
    
        public void append(JSONArray data, long offset)
            throws DescriptorValidationException, IOException, ExecutionException {
          synchronized (this.lock) {
            // If earlier appends have failed, we need to reset before continuing.
            if (this.error != null) {
              throw this.error;
            }
          }
          // Append asynchronously for increased throughput.
          ApiFuture<AppendRowsResponse> future = streamWriter.[append](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_append_com_google_gson_JsonArray_)(data, offset);
          [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[addCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_addCallback_com_google_api_core_ApiFuture_V__com_google_api_core_ApiFutureCallback___super_V__)(
              future, new AppendCompleteCallback(this), MoreExecutors.directExecutor());
          // Increase the count of in-flight requests.
          inflightRequestCount.register();
        }
    
        public void cleanup([BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html) client) {
          // Wait for all in-flight requests to complete.
          inflightRequestCount.arriveAndAwaitAdvance();
    
          // Close the connection to the server.
          streamWriter.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_close__)();
    
          // Verify that no error occurred in the stream.
          synchronized (this.lock) {
            if (this.error != null) {
              throw this.error;
            }
          }
    
          // Finalize the stream.
          [FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse.html) finalizeResponse =
              client.[finalizeWriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html#com_google_cloud_bigquery_storage_v1_BigQueryWriteClient_finalizeWriteStream__org_jspecify_annotations_Nullable_com_google_cloud_bigquery_storage_v1_WriteStreamName_)(streamWriter.getStreamName());
          System.out.println("Rows written: " + finalizeResponse.[getRowCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse.html#com_google_cloud_bigquery_storage_v1_FinalizeWriteStreamResponse_getRowCount__)());
        }
    
        public String getStreamName() {
          return streamWriter.[getStreamName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_getStreamName__)();
        }
    
        static class AppendCompleteCallback implements ApiFutureCallback<AppendRowsResponse> {
    
          private final DataWriter parent;
    
          public AppendCompleteCallback(DataWriter parent) {
            this.parent = parent;
          }
    
          public void onSuccess([AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html) response) {
            System.out.format("Append %d success\n", response.[getAppendResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html#com_google_cloud_bigquery_storage_v1_AppendRowsResponse_getAppendResult__)().getOffset().getValue());
            done();
          }
    
          public void onFailure(Throwable throwable) {
            synchronized (this.parent.lock) {
              if (this.parent.error == null) {
                [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.StorageException.html) storageException = [Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).[toStorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html#com_google_cloud_bigquery_storage_v1_Exceptions_toStorageException_com_google_rpc_Status_java_lang_Throwable_)(throwable);
                this.parent.error =
                    (storageException != null) ? storageException : new RuntimeException(throwable);
              }
            }
            System.out.format("Error: %s\n", throwable.toString());
            done();
          }
    
          private void done() {
            // Reduce the count of in-flight requests.
            this.parent.inflightRequestCount.arriveAndDeregister();
          }
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
    use google_cloud_bigquery::write::PendingWriter;
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
        // Create a writer for a pending stream
        let writer: PendingWriter<Arrow> = client
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
                // Write the batch to the pending stream
                writes.spawn(writer.append(batch).set_offset(10 * i).send());
            }
        }
        let results: Result<Vec<_>, _> = writes.join_all().await.into_iter().collect();
        let _ = results?;
    
        // Finalize the stream, preventing further writes
        let resp = writer.finalize().await?;
        println!(
            "Successfully finalized the stream with {} rows",
            resp.row_count
        );
    
        // Commit the stream to BigQuery
        let resp = writer.commit().await?;
        println!("Successfully committed the rows. {resp:?}");
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
