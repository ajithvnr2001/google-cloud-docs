---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-arrow-quickstart/
title: Download table data in the Arrow data format \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:14.763788+00:00
---

# Download table data in the Arrow data format  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-arrow-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Download table data in the Arrow data format Stay organized with collections  Save and categorize content based on your preferences. 

Download table data using the Arrow data format and deserialize the data into row objects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Storage API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/storage/libraries)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.bigquery.storage.v1.[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.html);
    import com.google.cloud.bigquery.storage.v1.[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html);
    import com.google.cloud.bigquery.storage.v1.[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html);
    import com.google.cloud.bigquery.storage.v1.[DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html);
    import com.google.cloud.bigquery.storage.v1.[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html);
    import com.google.cloud.bigquery.storage.v1.[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).[TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).[TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html);
    import com.google.common.base.Preconditions;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import org.apache.arrow.memory.BufferAllocator;
    import org.apache.arrow.memory.RootAllocator;
    import org.apache.arrow.vector.FieldVector;
    import org.apache.arrow.vector.VectorLoader;
    import org.apache.arrow.vector.VectorSchemaRoot;
    import org.apache.arrow.vector.ipc.ReadChannel;
    import org.apache.arrow.vector.ipc.message.MessageSerializer;
    import org.apache.arrow.vector.types.pojo.[Field](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Field.html);
    import org.apache.arrow.vector.types.pojo.Schema;
    import org.apache.arrow.vector.util.ByteArrayReadableSeekableByteChannel;
    
    public class StorageArrowSample {
    
      /*
       * SimpleRowReader handles deserialization of the Apache Arrow-encoded row batches transmitted
       * from the storage API using a generic datum decoder.
       */
      private static class SimpleRowReader implements AutoCloseable {
    
        BufferAllocator allocator = new RootAllocator(Long.MAX_VALUE);
    
        // Decoder object will be reused to avoid re-allocation and too much garbage collection.
        private final VectorSchemaRoot root;
        private final VectorLoader loader;
    
        public SimpleRowReader([ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema.html) arrowSchema) throws IOException {
          Schema schema =
              MessageSerializer.deserializeSchema(
                  new ReadChannel(
                      new ByteArrayReadableSeekableByteChannel(
                          arrowSchema.getSerializedSchema().toByteArray())));
          Preconditions.checkNotNull(schema);
          List<FieldVector> vectors = new ArrayList<>();
          for ([Field](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Field.html) field : schema.getFields()) {
            vectors.add(field.createVector(allocator));
          }
          root = new VectorSchemaRoot(vectors);
          loader = new VectorLoader(root);
        }
    
        /**
         * Sample method for processing Arrow data which only validates decoding.
         *
         * @param batch object returned from the ReadRowsResponse.
         */
        public void processRows([ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.html) batch) throws IOException {
          org.apache.arrow.vector.ipc.message.[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.html) deserializedBatch =
              MessageSerializer.deserializeRecordBatch(
                  new ReadChannel(
                      new ByteArrayReadableSeekableByteChannel(
                          batch.[getSerializedRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.html#com_google_cloud_bigquery_storage_v1_ArrowRecordBatch_getSerializedRecordBatch__)().toByteArray())),
                  allocator);
    
          loader.load(deserializedBatch);
          // Release buffers from batch (they are still held in the vectors in root).
          deserializedBatch.close();
          System.out.println(root.contentToTSVString());
          // Release buffers from vectors in root.
          root.clear();
        }
    
        @Override
        public void close() {
          root.close();
          allocator.close();
        }
      }
    
      public static void main(String... args) throws Exception {
        // Sets your Google Cloud Platform project ID.
        // String projectId = "YOUR_PROJECT_ID";
        String projectId = args[0];
        Integer snapshotMillis = null;
        if (args.length > 1) {
          snapshotMillis = Integer.parseInt(args[1]);
        }
    
        try ([BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html) client = [BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html).create()) {
          String parent = String.format("projects/%s", projectId);
    
          // This example uses baby name data from the public datasets.
          String srcTable =
              String.format(
                  "projects/%s/datasets/%s/tables/%s",
                  "bigquery-public-data", "usa_names", "usa_1910_current");
    
          // We specify the columns to be projected by adding them to the selected fields,
          // and set a simple filter to restrict which rows are transmitted.
          [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html) options =
              [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html).newBuilder()
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("name")
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("number")
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("state")
                  .[setRowRestriction](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_setRowRestriction_java_lang_String_)("state = \"WA\"")
                  .build();
    
          // Start specifying the read session we want created.
          [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).Builder sessionBuilder =
              [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).newBuilder()
                  .setTable(srcTable)
                  // This API can also deliver data serialized in Apache Avro format.
                  // This example leverages Apache Arrow.
                  .[setDataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setDataFormat_com_google_cloud_bigquery_storage_v1_DataFormat_)([DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html).ARROW)
                  .[setReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setReadOptions_com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_)(options);
    
          // Optionally specify the snapshot time.  When unspecified, snapshot time is "now".
          if (snapshotMillis != null) {
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) t =
                [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
                    .setSeconds(snapshotMillis / 1000)
                    .setNanos((int) ((snapshotMillis % 1000) * 1000000))
                    .build();
            [TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html) modifiers = [TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html).newBuilder().[setSnapshotTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableModifiers_Builder_setSnapshotTime_com_google_protobuf_Timestamp_)(t).build();
            sessionBuilder.[setTableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setTableModifiers_com_google_cloud_bigquery_storage_v1_ReadSession_TableModifiers_)(modifiers);
          }
    
          // Begin building the session creation request.
          [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html).Builder builder =
              [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html).newBuilder()
                  .setParent(parent)
                  .[setReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setReadSession_com_google_cloud_bigquery_storage_v1_ReadSession_)(sessionBuilder)
                  .[setMaxStreamCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setMaxStreamCount_int_)(1);
    
          [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html) session = client.createReadSession(builder.build());
          // Setup a simple reader and start a read session.
          try (SimpleRowReader reader = new SimpleRowReader(session.[getArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getArrowSchema__)())) {
    
            // Assert that there are streams available in the session.  An empty table may not have
            // data available.  If no sessions are available for an anonymous (cached) table, consider
            // writing results of a query to a named table rather than consuming cached results
            // directly.
            Preconditions.checkState(session.[getStreamsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreamsCount__)() > 0);
    
            // Use the first stream to perform reading.
            String streamName = session.[getStreams](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreams_int_)(0).getName();
    
            [ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html) readRowsRequest =
                [ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html).newBuilder().[setReadStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.Builder.html#com_google_cloud_bigquery_storage_v1_ReadRowsRequest_Builder_setReadStream_java_lang_String_)(streamName).build();
    
            // Process each block of rows as they arrive and decode using our simple row reader.
            ServerStream<ReadRowsResponse> stream = client.readRowsCallable().call(readRowsRequest);
            for ([ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.html) response : stream) {
              Preconditions.checkState(response.hasArrowRecordBatch());
              reader.processRows(response.getArrowRecordBatch());
            }
          }
        }
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
