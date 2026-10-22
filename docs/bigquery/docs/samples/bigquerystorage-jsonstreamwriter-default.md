---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-default/
title: Append records using default client \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:38.767273+00:00
---

# Append records using default client  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-jsonstreamwriter-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Append records using default client Stay organized with collections  Save and categorize content based on your preferences. 

Use the JSON stream writer to append records using default client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Stream data using the Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api-streaming)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutureCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.batching.[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html);
    import com.google.api.gax.core.[FixedExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.FixedExecutorProvider.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.cloud.bigquery.storage.v1.[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.html);
    import com.google.cloud.bigquery.storage.v1.[AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryWriteSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteSettings.html);
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html);
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).AppendSerializationError;
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).MaximumRequestCallbackWaitTimeExceededException;
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).StorageException;
    import com.google.cloud.bigquery.storage.v1.[Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).StreamWriterClosedException;
    import com.google.cloud.bigquery.storage.v1.[JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html);
    import com.google.cloud.bigquery.storage.v1.[TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[Descriptors](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.html).[DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html);
    import java.io.IOException;
    import java.util.Map;
    import java.util.concurrent.Executors;
    import java.util.concurrent.Phaser;
    import java.util.concurrent.atomic.AtomicInteger;
    import javax.annotation.concurrent.GuardedBy;
    import org.json.JSONArray;
    import org.json.JSONObject;
    import org.threeten.bp.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class WriteToDefaultStream {
    
      public static void runWriteToDefaultStream()
          throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), InterruptedException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        writeToDefaultStream(projectId, datasetName, tableName);
      }
    
      private static [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) buildByteString() {
        byte[] bytes = new byte[] {1, 2, 3, 4, 5};
        return [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(bytes);
      }
    
      // Create a JSON object that is compatible with the table schema.
      private static JSONObject buildRecord(int i, int j) {
        JSONObject record = new JSONObject();
        StringBuilder sbSuffix = new StringBuilder();
        for (int k = 0; k < j; k++) {
          sbSuffix.append(k);
        }
        [record](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.Distribution.html#com_google_api_gax_core_Distribution_record_int_).put("test_string", String.format("record %03d-%03d %s", i, j, sbSuffix.toString()));
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteString = buildByteString();
        [record](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.Distribution.html#com_google_api_gax_core_Distribution_record_int_).put("test_bytes", byteString);
        [record](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.Distribution.html#com_google_api_gax_core_Distribution_record_int_).put(
            "test_geo",
            "POLYGON((-124.49 47.35,-124.49 40.73,-116.49 40.73,-116.49 47.35,-124.49 47.35))");
        return record;
      }
    
      public static void writeToDefaultStream(String projectId, String datasetName, String tableName)
          throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), InterruptedException, IOException {
        [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable = [TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html).of(projectId, datasetName, tableName);
    
        DataWriter writer = new DataWriter();
        // One time initialization for the worker.
        [writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_writer_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_WriteChannelConfiguration_).[initialize](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.telemetry.HttpTracingRequestInitializer.html#com_google_cloud_bigquery_telemetry_HttpTracingRequestInitializer_initialize_com_google_api_client_http_HttpRequest_)(parentTable);
    
        // Write two batches of fake data to the stream, each with 10 JSON records.  Data may be
        // batched up to the maximum request size:
        // https://cloud.google.com/bigquery/quotas#write-api-limits
        for (int i = 0; i < 2; i++) {
          JSONArray jsonArr = new JSONArray();
          for (int j = 0; j < 10; j++) {
            JSONObject record = buildRecord(i, j);
            jsonArr.put(record);
          }
    
          [writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_writer_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_WriteChannelConfiguration_).append(new AppendContext(jsonArr));
        }
    
        // Final cleanup for the stream during worker teardown.
        [writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_writer_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_WriteChannelConfiguration_).cleanup();
        verifyExpectedRowCount(parentTable, 12L);
        System.out.println("Appended records successfully.");
      }
    
      private static void verifyExpectedRowCount([TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable, long expectedRowCount)
          throws InterruptedException {
        String queryRowCount =
            "SELECT COUNT(*) FROM `"
                + parentTable.[getProject](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_getProject__)()
                + "."
                + parentTable.[getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_getDataset__)()
                + "."
                + parentTable.[getTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_getTable__)()
                + "`";
        [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig = [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(queryRowCount).build();
        [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
        [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)(queryConfig);
        long countRowsActual =
            Long.parseLong(results.[getValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_getValues__)().iterator().next().get("f0_").getStringValue());
        if (countRowsActual != expectedRowCount) {
          throw new RuntimeException(
              "Unexpected row count. Expected: " + expectedRowCount + ". Actual: " + countRowsActual);
        }
      }
    
      private static class AppendContext {
    
        JSONArray data;
    
        AppendContext(JSONArray data) {
          this.data = data;
        }
      }
    
      private static class DataWriter {
    
        private static final int MAX_RECREATE_COUNT = 3;
    
        private [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html) client;
    
        // Track the number of in-flight requests to wait for all responses before shutting down.
        private final Phaser inflightRequestCount = new Phaser(1);
        private final Object lock = new Object();
        private [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html) streamWriter;
    
        @GuardedBy("lock")
        private RuntimeException error = null;
    
        private AtomicInteger recreateCount = new AtomicInteger(0);
    
        private [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html) createStreamWriter(String tableName)
            throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), IOException, InterruptedException {
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
    
          // Use the JSON stream writer to send records in JSON format. Specify the table name to write
          // to the default stream.
          // For more information about JsonStreamWriter, see:
          // https://googleapis.dev/java/google-cloud-bigquerystorage/latest/com/google/cloud/bigquery/storage/v1/JsonStreamWriter.html
          return [JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html).newBuilder(tableName, client)
              .setExecutorProvider([FixedExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.FixedExecutorProvider.html).create(Executors.newScheduledThreadPool(10)))
              .setChannelProvider(
                  [BigQueryWriteSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteSettings.html).defaultGrpcTransportProviderBuilder()
                      .setKeepAliveTime(org.threeten.bp.Duration.ofMinutes(1))
                      .setKeepAliveTimeout(org.threeten.bp.Duration.ofMinutes(1))
                      .setKeepAliveWithoutCalls(true)
                      .setChannelsPerCpu(2)
                      .build())
              .setEnableConnectionPool(true)
              // This will allow connection pool to scale up better.
              .setFlowControlSettings(
                  [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html).newBuilder().setMaxOutstandingElementCount(100L).build())
              // If value is missing in json and there is a default value configured on bigquery
              // column, apply the default value to the missing value field.
              .setDefaultMissingValueInterpretation(
                  [AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.html).MissingValueInterpretation.DEFAULT_VALUE)
              .setRetrySettings(retrySettings)
              .build();
        }
    
        public void initialize([TableName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html) parentTable)
            throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), IOException, InterruptedException {
          // Initialize client without settings, internally within stream writer a new client will be
          // created with full settings.
          client = [BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html).create();
    
          streamWriter = createStreamWriter(parentTable.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableName.html#com_google_cloud_bigquery_storage_v1_TableName_toString__)());
        }
    
        public void append(AppendContext appendContext)
            throws [DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html), IOException, InterruptedException {
          synchronized (this.lock) {
            if (!streamWriter.[isUserClosed](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_isUserClosed__)()
                && streamWriter.[isClosed](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_isClosed__)()
                && recreateCount.getAndIncrement() < MAX_RECREATE_COUNT) {
              streamWriter = createStreamWriter(streamWriter.[getStreamName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_getStreamName__)());
              this.error = null;
            }
            // If earlier appends have failed, we need to reset before continuing.
            if (this.error != null) {
              throw this.error;
            }
          }
          // Append asynchronously for increased throughput.
          ApiFuture<AppendRowsResponse> future = streamWriter.[append](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_append_com_google_gson_JsonArray_)([append](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_append_com_google_gson_JsonArray_)Context.data);
          [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[addCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_addCallback_com_google_api_core_ApiFuture_V__com_google_api_core_ApiFutureCallback___super_V__)(
              future, new AppendCompleteCallback(this, appendContext), MoreExecutors.directExecutor());
    
          // Increase the count of in-flight requests.
          inflightRequestCount.register();
        }
    
        public void cleanup() {
          // Wait for all in-flight requests to complete.
          inflightRequestCount.arriveAndAwaitAdvance();
    
          client.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient.html#com_google_cloud_bigquery_storage_v1_BigQueryWriteClient_close__)();
          // Close the connection to the server.
          streamWriter.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.html#com_google_cloud_bigquery_storage_v1_JsonStreamWriter_close__)();
    
          // Verify that no error occurred in the stream.
          synchronized (this.lock) {
            if (this.error != null) {
              throw this.error;
            }
          }
        }
    
        static class AppendCompleteCallback implements ApiFutureCallback<AppendRowsResponse> {
    
          private final DataWriter parent;
          private final AppendContext appendContext;
    
          public AppendCompleteCallback(DataWriter parent, AppendContext appendContext) {
            this.parent = parent;
            this.appendContext = appendContext;
          }
    
          public void onSuccess([AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.html) response) {
            System.out.format("Append success\n");
            this.parent.recreateCount.set(0);
            done();
          }
    
          public void onFailure(Throwable throwable) {
            if (throwable instanceof AppendSerializationError) {
              AppendSerializationError ase = (AppendSerializationError) throwable;
              Map<Integer, String> rowIndexToErrorMessage = ase.getRowIndexToErrorMessage();
              if (rowIndexToErrorMessage.size() > 0) {
                // Omit the faulty rows
                JSONArray dataNew = new JSONArray();
                for (int i = 0; i < appendContext.data.length(); i++) {
                  if (!rowIndexToErrorMessage.containsKey(i)) {
                    dataNew.put(appendContext.data.get(i));
                  } else {
                    // process faulty rows by placing them on a dead-letter-queue, for instance
                  }
                }
    
                // Retry the remaining valid rows, but using a separate thread to
                // avoid potentially blocking while we are in a callback.
                if (dataNew.length() > 0) {
                  try {
                    this.parent.append(new AppendContext(dataNew));
                  } catch ([DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html) e) {
                    throw new RuntimeException(e);
                  } catch (IOException e) {
                    throw new RuntimeException(e);
                  } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                  }
                }
                // Mark the existing attempt as done since we got a response for it
                done();
                return;
              }
            }
    
            boolean resendRequest = false;
            if (throwable instanceof MaximumRequestCallbackWaitTimeExceededException) {
              resendRequest = true;
            } else if (throwable instanceof StreamWriterClosedException) {
              if (!parent.streamWriter.isUserClosed()) {
                resendRequest = true;
              }
            }
            if (resendRequest) {
              // Retry this request.
              try {
                this.parent.append(new AppendContext(appendContext.data));
              } catch ([DescriptorValidationException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html) e) {
                throw new RuntimeException(e);
              } catch (IOException e) {
                throw new RuntimeException(e);
              } catch (InterruptedException e) {
                throw new RuntimeException(e);
              }
              // Mark the existing attempt as done since we got a response for it
              done();
              return;
            }
    
            synchronized (this.parent.lock) {
              if (this.parent.error == null) {
                StorageException storageException = [Exceptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.html).toStorageException(throwable);
                this.parent.error =
                    (storageException != null) ? storageException : new RuntimeException(throwable);
              }
            }
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
        // Create a writer for the default stream
        let writer = client
            .open_default_stream(table)
            .build_arrow(ArrowSchema::new().set_serialized_schema(schema_buf))
            .await?;
    
        // Create a decoder to convert JSON to Arrow
        let mut decoder = ReaderBuilder::new(schema).build_decoder()?;
    
        let mut writes = JoinSet::new();
        for i in 0..100 {
            for j in 0..10 {
                // Generate example data (JSON bytes).
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
                // Write the batch to BigQuery
                writes.spawn(writer.append(batch).send());
            }
        }
        let results: Result<Vec<_>, _> = writes.join_all().await.into_iter().collect();
        let _ = results?;
        println!("Successfully wrote 100 record batches of 10 rows each.");
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
