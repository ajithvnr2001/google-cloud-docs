---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-batch-process-document/
title: Send a batch process documents request \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:37.021300+00:00
---

# Send a batch process documents request  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-batch-process-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Send a batch process documents request Stay organized with collections  Save and categorize content based on your preferences. 

Sends a batch (asynchronous) processing request to a processor.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Send a processing request](https://docs.cloud.google.com/document-ai/docs/send-request)



## Code sample

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.documentai.v1.[BatchDocumentsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchDocumentsInputConfig.html);
    import com.google.cloud.documentai.v1.[BatchProcessMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessMetadata.html);
    import com.google.cloud.documentai.v1.[BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest.html);
    import com.google.cloud.documentai.v1.[BatchProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessResponse.html);
    import com.google.cloud.documentai.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html);
    import com.google.cloud.documentai.v1.[DocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.html);
    import com.google.cloud.documentai.v1.[DocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.html).[GcsOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings.html);
    import com.google.cloud.documentai.v1.[GcsDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocument.html);
    import com.google.cloud.documentai.v1.[GcsDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocuments.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.File;
    import java.io.FileReader;
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class BatchProcessDocument {
      public static void batchProcessDocument()
          throws IOException, InterruptedException, TimeoutException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processerId = "your-processor-id";
        String outputGcsBucketName = "your-gcs-bucket-name";
        String outputGcsPrefix = "PREFIX";
        String inputGcsUri = "gs://your-gcs-bucket/path/to/input/file.pdf";
        batchProcessDocument(
            projectId, location, processerId, inputGcsUri, outputGcsBucketName, outputGcsPrefix);
      }
    
      public static void batchProcessDocument(
          String projectId,
          String location,
          String processorId,
          String gcsInputUri,
          String gcsOutputBucketName,
          String gcsOutputUriPrefix)
          throws IOException, InterruptedException, TimeoutException, ExecutionException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests. After completing all of your
        // requests, call
        // the "close" method on the client to safely clean up any remaining background
        // resources.
        String endpoint = String.format("%s-documentai.googleapis.com:443", location);
        [DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings.html) settings =
            [DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) client = [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create(settings)) {
          // The full resource name of the processor, e.g.:
          // projects/project-id/locations/location/processor/processor-id
          // You must create new processors in the Cloud Console first
          String name =
              String.format("projects/%s/locations/%s/processors/%s", projectId, location, processorId);
    
          [GcsDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocument.html) gcsDocument =
              [GcsDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocument.html).newBuilder().setGcsUri(gcsInputUri).setMimeType("application/pdf").build();
    
          [GcsDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocuments.html) gcsDocuments = [GcsDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocuments.html).newBuilder().[addDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GcsDocuments.Builder.html#com_google_cloud_documentai_v1_GcsDocuments_Builder_addDocuments_com_google_cloud_documentai_v1_GcsDocument_)(gcsDocument).build();
    
          [BatchDocumentsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchDocumentsInputConfig.html) inputConfig =
              [BatchDocumentsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchDocumentsInputConfig.html).newBuilder().[setGcsDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchDocumentsInputConfig.Builder.html#com_google_cloud_documentai_v1_BatchDocumentsInputConfig_Builder_setGcsDocuments_com_google_cloud_documentai_v1_GcsDocuments_)(gcsDocuments).build();
    
          String fullGcsPath = String.format("gs://%s/%s/", gcsOutputBucketName, gcsOutputUriPrefix);
          [GcsOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig.html) gcsOutputConfig = [GcsOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig.html).newBuilder().setGcsUri(fullGcsPath).build();
    
          [DocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.html) documentOutputConfig =
              [DocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.html).newBuilder().[setGcsOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentOutputConfig.Builder.html#com_google_cloud_documentai_v1_DocumentOutputConfig_Builder_setGcsOutputConfig_com_google_cloud_documentai_v1_DocumentOutputConfig_GcsOutputConfig_)(gcsOutputConfig).build();
    
          // Configure the batch process request.
          [BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest.html) request =
              [BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest.html).newBuilder()
                  .setName(name)
                  .[setInputDocuments](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest.Builder.html#com_google_cloud_documentai_v1_BatchProcessRequest_Builder_setInputDocuments_com_google_cloud_documentai_v1_BatchDocumentsInputConfig_)(inputConfig)
                  .[setDocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest.Builder.html#com_google_cloud_documentai_v1_BatchProcessRequest_Builder_setDocumentOutputConfig_com_google_cloud_documentai_v1_DocumentOutputConfig_)(documentOutputConfig)
                  .build();
    
          OperationFuture<BatchProcessResponse, BatchProcessMetadata> future =
              client.[batchProcessDocumentsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html#com_google_cloud_documentai_v1_DocumentProcessorServiceClient_batchProcessDocumentsAsync__org_jspecify_annotations_Nullable_com_google_api_resourcenames_ResourceName_)(request);
    
          // Batch process document using a long-running operation.
          // You can wait for now, or get results later.
          // Note: first request to the service takes longer than subsequent
          // requests.
          System.out.println("Waiting for operation to complete...");
          future.get();
    
          System.out.println("Document processing complete.");
    
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(gcsOutputBucketName);
    
          // List all of the files in the Storage bucket.
          Page<Blob> blobs = bucket.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_list_com_google_cloud_storage_Storage_BlobListOption____)(Storage.BlobListOption.prefix(gcsOutputUriPrefix + "/"));
          int idx = 0;
          for ([Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob : blobs.iterateAll()) {
            if (!blob.[isDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_isDirectory__)()) {
              System.out.printf("Fetched file #%d\n", ++idx);
              // Read the results
    
              // Download and store json data in a temp file.
              File tempFile = File.createTempFile("file", ".json");
              [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) fileInfo = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(BlobId.of(gcsOutputBucketName, blob.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)Name()));
              fileInfo.[downloadTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_downloadTo_java_io_OutputStream_com_google_cloud_storage_Blob_BlobSourceOption____)(tempFile.toPath());
    
              // Parse json file into Document.
              FileReader reader = new FileReader(tempFile);
              [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).Builder builder = [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).newBuilder();
              [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(reader, builder);
    
              [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html) document = builder.build();
    
              // Get all of the document text as one big string.
              String text = document.[getText](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html#com_google_cloud_documentai_v1_Document_getText__)();
    
              // Read the text recognition output from the processor
              System.out.println("The document contains the following paragraphs:");
              [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) page1 = document.[getPages](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html#com_google_cloud_documentai_v1_Document_getPages_int_)(0);
              List<Document.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html).[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Paragraph.html)> paragraphList = page1.getParagraphsList();
              for ([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html).[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Paragraph.html) paragraph : paragraphList) {
                String paragraphText = getText(paragraph.getLayout().getTextAnchor(), text);
                System.out.printf("Paragraph text:%s\n", paragraphText);
              }
    
              // Form parsing provides additional output about
              // form-formatted PDFs. You must create a form
              // processor in the Cloud Console to see full field details.
              System.out.println("The following form key/value pairs were detected:");
    
              for ([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html).[FormField](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.FormField.html) field : page1.getFormFieldsList()) {
                String fieldName = getText(field.getFieldName().getTextAnchor(), text);
                String fieldValue = getText(field.getFieldValue().getTextAnchor(), text);
    
                System.out.println("Extracted form fields pair:");
                System.out.printf("\t(%s, %s))", fieldName, fieldValue);
              }
    
              // Clean up temp file.
              tempFile.deleteOnExit();
            }
          }
        }
      }
    
      // Extract shards from the text field
      private static String getText([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[TextAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.TextAnchor.html) textAnchor, String text) {
        if (textAnchor.getTextSegmentsList().size() > 0) {
          int startIdx = (int) textAnchor.getTextSegments(0).getStartIndex();
          int endIdx = (int) textAnchor.getTextSegments(0).getEndIndex();
          return text.substring(startIdx, endIdx);
        }
        return "[NO TEXT]";
      }
    }

### Node.js

For more information, see the [Document AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION'; // Format is 'us' or 'eu'
    // const processorId = 'YOUR_PROCESSOR_ID';
    // const gcsInputUri = 'YOUR_SOURCE_PDF';
    // const gcsOutputUri = 'YOUR_STORAGE_BUCKET';
    // const gcsOutputUriPrefix = 'YOUR_STORAGE_PREFIX';
    
    // Imports the Google Cloud client library
    const {DocumentProcessorServiceClient} =
      require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1;
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Instantiates Document AI, Storage clients
    const client = new [DocumentProcessorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)();
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    const {default: PQueue} = require('p-queue');
    
    async function batchProcessDocument() {
      const name = `projects/${projectId}/locations/${location}/processors/${processorId}`;
    
      // Configure the batch process request.
      const request = {
        name,
        inputDocuments: {
          gcsDocuments: {
            documents: [
              {
                gcsUri: gcsInputUri,
                mimeType: 'application/pdf',
              },
            ],
          },
        },
        documentOutputConfig: {
          gcsOutputConfig: {
            gcsUri: `${gcsOutputUri}/${gcsOutputUriPrefix}/`,
          },
        },
      };
    
      // Batch process document using a long-running operation.
      // You can wait for now, or get results later.
      // Note: first request to the service takes longer than subsequent
      // requests.
      const [operation] = await client.batchProcessDocuments(request);
    
      // Wait for operation to complete.
      await operation.promise();
      console.log('Document processing complete.');
    
      // Query Storage bucket for the results file(s).
      const query = {
        prefix: gcsOutputUriPrefix,
      };
    
      console.log('Fetching results ...');
    
      // List all of the files in the Storage bucket
      const [files] = await storage.bucket(gcsOutputUri).[getFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(query);
    
      // Add all asynchronous downloads to queue for execution.
      const queue = new PQueue({concurrency: 15});
      const tasks = files.map((fileInfo, index) => async () => {
        // Get the file as a buffer
        const [file] = await fileInfo.download();
    
        console.log(`Fetched file #${index + 1}:`);
    
        // The results stored in the output Storage location
        // are formatted as a document object.
        const document = JSON.parse(file.toString());
        const {text} = document;
    
        // Extract shards from the text field
        const getText = textAnchor => {
          if (!textAnchor.textSegments || textAnchor.textSegments.length === 0) {
            return '';
          }
    
          // First shard in document doesn't have startIndex property
          const startIndex = textAnchor.textSegments[0].startIndex || 0;
          const endIndex = textAnchor.textSegments[0].endIndex;
    
          return text.substring(startIndex, endIndex);
        };
    
        // Read the text recognition output from the processor
        console.log('The document contains the following paragraphs:');
    
        const [page1] = document.pages;
        const {paragraphs} = page1;
        for (const paragraph of paragraphs) {
          const paragraphText = getText(paragraph.layout.textAnchor);
          console.log(`Paragraph text:\n${paragraphText}`);
        }
    
        // Form parsing provides additional output about
        // form-formatted PDFs. You  must create a form
        // processor in the Cloud Console to see full field details.
        console.log('\nThe following form key/value pairs were detected:');
    
        const {formFields} = page1;
        for (const field of formFields) {
          const fieldName = getText(field.fieldName.textAnchor);
          const fieldValue = getText(field.fieldValue.textAnchor);
    
          console.log('Extracted key value pair:');
          console.log(`\t(${fieldName}, ${fieldValue})`);
        }
      });
      await queue.addAll(tasks);
    }

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import re
    from typing import Optional
    
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import InternalServerError
    from google.api_core.exceptions import RetryError
    from google.cloud import documentai  # type: ignore
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION" # Format is "us" or "eu"
    # processor_id = "YOUR_PROCESSOR_ID" # Create processor before running sample
    # gcs_output_uri = "YOUR_OUTPUT_URI" # Must end with a trailing slash `/`. Format: gs://bucket/directory/subdirectory/
    # processor_version_id = "YOUR_PROCESSOR_VERSION_ID" # Optional. Example: pretrained-ocr-v1.0-2020-09-23
    
    # TODO(developer): You must specify either `gcs_input_uri` and `mime_type` or `gcs_input_prefix`
    # gcs_input_uri = "YOUR_INPUT_URI" # Format: gs://bucket/directory/file.pdf
    # input_mime_type = "application/pdf"
    # gcs_input_prefix = "YOUR_INPUT_URI_PREFIX" # Format: gs://bucket/directory/
    # field_mask = "text,entities,pages.pageNumber"  # Optional. The fields to return in the Document object.
    
    
    def batch_process_documents(
        project_id: str,
        location: str,
        processor_id: str,
        gcs_output_uri: str,
        processor_version_id: Optional[str] = None,
        gcs_input_uri: Optional[str] = None,
        input_mime_type: Optional[str] = None,
        gcs_input_prefix: Optional[str] = None,
        field_mask: Optional[str] = None,
        timeout: int = 400,
    ) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        if gcs_input_uri:
            # Specify specific GCS URIs to process individual documents
            gcs_document = documentai.[GcsDocument](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsDocument.html)(
                gcs_uri=gcs_input_uri, mime_type=input_mime_type
            )
            # Load GCS Input URI into a List of document files
            gcs_documents = documentai.[GcsDocuments](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsDocuments.html)(documents=[gcs_document])
            input_config = documentai.[BatchDocumentsInputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchDocumentsInputConfig.html)(gcs_documents=gcs_documents)
        else:
            # Specify a GCS URI Prefix to process an entire directory
            gcs_prefix = documentai.[GcsPrefix](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsPrefix.html)(gcs_uri_prefix=gcs_input_prefix)
            input_config = documentai.[BatchDocumentsInputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchDocumentsInputConfig.html)(gcs_prefix=gcs_prefix)
    
        # Cloud Storage URI for the Output Directory
        gcs_output_config = documentai.[DocumentOutputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.DocumentOutputConfig.html).[GcsOutputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.DocumentOutputConfig.GcsOutputConfig.html)(
            gcs_uri=gcs_output_uri, field_mask=field_mask
        )
    
        # Where to write results
        output_config = documentai.[DocumentOutputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.DocumentOutputConfig.html)(gcs_output_config=gcs_output_config)
    
        if processor_version_id:
            # The full resource name of the processor version, e.g.:
            # projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}
            name = client.[processor_version_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_version_path)(
                project_id, location, processor_id, processor_version_id
            )
        else:
            # The full resource name of the processor, e.g.:
            # projects/{project_id}/locations/{location}/processors/{processor_id}
            name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        request = documentai.[BatchProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchProcessRequest.html)(
            name=name,
            input_documents=input_config,
            document_output_config=output_config,
        )
    
        # BatchProcess returns a Long Running Operation (LRO)
        operation = client.[batch_process_documents](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_batch_process_documents)(request)
    
        # Continually polls the operation until it is complete.
        # This could take some time for larger files
        # Format: projects/{project_id}/locations/{location}/operations/{operation_id}
        try:
            print(f"Waiting for operation {operation.operation.name} to complete...")
            operation.result(timeout=timeout)
        # Catch exception when operation doesn't finish before timeout
        except (RetryError, InternalServerError) as e:
            print(e.message)
    
        # NOTE: Can also use callbacks for asynchronous processing
        #
        # def my_callback(future):
        #   result = future.result()
        #
        # operation.add_done_callback(my_callback)
    
        # After the operation is complete,
        # get output document information from operation metadata
        metadata = documentai.[BatchProcessMetadata](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchProcessMetadata.html)(operation.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata))
    
        if [metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata).[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state) != documentai.[BatchProcessMetadata](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchProcessMetadata.html).State.SUCCEEDED:
            raise ValueError(f"Batch Process Failed: {[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata).state_message}")
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        print("Output files:")
        # One process per Input Document
        for process in list([metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata).individual_process_statuses):
            # output_gcs_destination format: gs://BUCKET/PREFIX/OPERATION_NUMBER/INPUT_FILE_NUMBER/
            # The Cloud Storage API requires the bucket name and URI prefix separately
            matches = re.match(r"gs://(.*?)/(.*)", process.output_gcs_destination)
            if not matches:
                print(
                    "Could not parse output GCS destination:",
                    process.output_gcs_destination,
                )
                continue
    
            output_bucket, output_prefix = matches.groups()
    
            # Get List of Document Objects from the Output Bucket
            output_blobs = storage_client.[list_blobs](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_blobs)(output_bucket, prefix=output_prefix)
    
            # Document AI may output multiple JSON files per source file
            for blob in output_blobs:
                # Document AI should only output JSON files to GCS
                if blob.[content_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_type) != "application/json":
                    print(
                        f"Skipping non-supported file: {blob.name} - Mimetype: {blob.[content_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_type)}"
                    )
                    continue
    
                # Download JSON File as bytes object and convert to Document Object
                print(f"Fetching {blob.name}")
                document = documentai.Document.from_json(
                    blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)(), ignore_unknown_fields=True
                )
    
                # For a full list of Document object attributes, please reference this page:
                # https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document
    
                # Read the text recognition output from the processor
                print("The document contains the following text:")
                print([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
