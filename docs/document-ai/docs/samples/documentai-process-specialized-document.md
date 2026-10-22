---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-specialized-document/
title: Process a document using a Specialized processor \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:25.148229+00:00
---

# Process a document using a Specialized processor  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-specialized-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Process a document using a Specialized processor Stay organized with collections  Save and categorize content based on your preferences. 

Sends an online processing request to a Specialized processor and parses the response. Extracts and prints entities, normalized values, confidence, and properties.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Handle processing response](https://docs.cloud.google.com/document-ai/docs/handle-response)



## Code sample

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1beta3.Document;
    import com.google.cloud.documentai.v1beta3.DocumentProcessorServiceClient;
    import com.google.cloud.documentai.v1beta3.DocumentProcessorServiceSettings;
    import com.google.cloud.documentai.v1beta3.ProcessRequest;
    import com.google.cloud.documentai.v1beta3.ProcessResponse;
    import com.google.cloud.documentai.v1beta3.RawDocument;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ProcessSpecializedDocument {
      public static void processSpecializedDocument()
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processerId = "your-processor-id";
        String filePath = "path/to/input/file.pdf";
        processSpecializedDocument(projectId, location, processerId, filePath);
      }
    
      public static void processSpecializedDocument(
          String projectId, String location, String processorId, String filePath)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests. After completing all of your
        // requests, call
        // the "close" method on the client to safely clean up any remaining background
        // resources.
        String endpoint = String.format("%s-documentai.googleapis.com:443", location);
        DocumentProcessorServiceSettings settings =
            DocumentProcessorServiceSettings.newBuilder().setEndpoint(endpoint).build();
        try (DocumentProcessorServiceClient client = DocumentProcessorServiceClient.create(settings)) {
          // The full resource name of the processor, e.g.:
          // projects/project-id/locations/location/processor/processor-id
          // You must create new processors in the Cloud Console first
          String name =
              String.format("projects/%s/locations/%s/processors/%s", projectId, location, processorId);
    
          // Read the file.
          byte[] imageFileData = Files.readAllBytes(Paths.get(filePath));
    
          // Convert the image data to a Buffer and base64 encode it.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) content = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(imageFileData);
    
          RawDocument document =
              RawDocument.newBuilder().setContent(content).setMimeType("application/pdf").build();
    
          // Configure the process request.
          ProcessRequest request =
              ProcessRequest.newBuilder().setName(name).setRawDocument(document).build();
    
          // Recognizes text entities in the PDF document
          ProcessResponse result = client.processDocument(request);
          Document documentResponse = result.getDocument();
    
          System.out.println("Document processing complete.");
    
          // Read fields specificly from the specalized US drivers license processor:
          // https://cloud.google.com/document-ai/docs/processors-list#processor_us-driver-license-parser
          // retriving data from other specalized processors follow a similar pattern.
          // For a complete list of processors see:
          // https://cloud.google.com/document-ai/docs/processors-list
          //
          // OCR and other data is also present in the quality processor's response.
          // Please see the OCR and other samples for how to parse other data in the
          // response.
          for (Document.Entity entity : documentResponse.getEntitiesList()) {
            // Fields detected. For a full list of fields for each processor see
            // the processor documentation:
            // https://cloud.google.com/document-ai/docs/processors-list
            String entityType = entity.getType();
            // some other value formats in addition to text are availible
            // e.g. dates: `entity.getNormalizedValue().getDateValue().getYear()`
            // check for normilized value with `entity.hasNormalizedValue()`
            String entityTextValue = escapeNewlines(entity.getTextAnchor().getContent());
            float entityConfidence = entity.getConfidence();
            System.out.printf(
                "    * %s: %s (%.2f%% confident)\n",
                entityType, entityTextValue, entityConfidence * 100.0);
          }
        }
      }
    
      private static String escapeNewlines(String s) {
        return s.replace("\n", "\\n").replace("\r", "\\r");
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
    // const processorId = 'YOUR_PROCESSOR_ID'; // Create processor in Cloud Console
    // const filePath = '/path/to/local/pdf';
    
    const {DocumentProcessorServiceClient} =
      require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1beta3;
    
    // Instantiates a client
    const client = new [DocumentProcessorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)();
    
    async function processDocument() {
      // The full resource name of the processor, e.g.:
      // projects/project-id/locations/location/processor/processor-id
      // You must create new processors in the Cloud Console first
      const name = `projects/${projectId}/locations/${location}/processors/${processorId}`;
    
      // Read the file into memory.
      const fs = require('fs').promises;
      const imageFile = await fs.readFile(filePath);
    
      // Convert the image data to a Buffer and base64 encode it.
      const encodedImage = Buffer.from(imageFile).toString('base64');
    
      const request = {
        name,
        rawDocument: {
          content: encodedImage,
          mimeType: 'application/pdf',
        },
      };
    
      // Recognizes text entities in the PDF document
      const [result] = await client.processDocument(request);
    
      console.log('Document processing complete.');
    
      // Read fields specificly from the specalized US drivers license processor:
      // https://cloud.google.com/document-ai/docs/processors-list#processor_us-driver-license-parser
      // retriving data from other specalized processors follow a similar pattern.
      // For a complete list of processors see:
      // https://cloud.google.com/document-ai/docs/processors-list
      //
      // OCR and other data is also present in the quality processor's response.
      // Please see the OCR and other samples for how to parse other data in the
      // response.
      const {document} = result;
      for (const entity of document.entities) {
        // Fields detected. For a full list of fields for each processor see
        // the processor documentation:
        // https://cloud.google.com/document-ai/docs/processors-list
        const key = entity.type;
        // some other value formats in addition to text are availible
        // e.g. dates: `entity.normalizedValue.dateValue.year`
        const textValue =
          entity.textAnchor !== null ? entity.textAnchor.content : '';
        const conf = entity.confidence * 100;
        console.log(
          `* ${JSON.stringify(key)}: ${JSON.stringify(textValue)}(${conf.toFixed(
            2
          )}% confident)`
        );
      }
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional, Sequence
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION" # Format is "us" or "eu"
    # processor_id = "YOUR_PROCESSOR_ID" # Create processor before running sample
    # processor_version = "rc" # Refer to https://cloud.google.com/document-ai/docs/manage-processor-versions for more information
    # file_path = "/path/to/local/pdf"
    # mime_type = "application/pdf" # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
    
    
    def process_document_entity_extraction_sample(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version: str,
        file_path: str,
        mime_type: str,
    ) -> None:
        # Online processing request to Document AI
        document = process_document(
            project_id, location, processor_id, processor_version, file_path, mime_type
        )
    
        # Print extracted entities from entity extraction processor output.
        # For a complete list of processors see:
        # https://cloud.google.com/document-ai/docs/processors-list
        #
        # OCR and other data is also present in the processor's response.
        # Refer to the OCR samples for how to parse other data in the response.
    
        print(f"Found {len([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).entities)} entities:")
        for entity in [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).entities:
            print_entity(entity)
            # Print Nested Entities (if any)
            for prop in [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).properties:
                print_entity(prop)
    
    
    
    
    def print_entity(entity: documentai.Document.Entity) -> None:
        # Fields detected. For a full list of fields for each processor see
        # the processor documentation:
        # https://cloud.google.com/document-ai/docs/processors-list
        key = [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).type_
    
        # Some other value formats in addition to text are available
        # e.g. dates: `entity.normalized_value.date_value.year`
        text_value = [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).text_anchor.content or [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).mention_text
        confidence = [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).confidence
        normalized_value = [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).normalized_value.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text)
        print(f"    * {repr(key)}: {repr(text_value)} ({confidence:.1%} confident)")
    
        if normalized_value:
            print(f"    * Normalized Value: {repr(normalized_value)}")
    
    
    
    
    def process_document(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version: str,
        file_path: str,
        mime_type: str,
        process_options: Optional[documentai.[ProcessOptions](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessOptions.html)] = None,
    ) -> documentai.Document:
        # You must set the `api_endpoint` if you use a location other than "us".
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(
            client_options=ClientOptions(
                api_endpoint=f"{location}-documentai.googleapis.com"
            )
        )
    
        # The full resource name of the processor version, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
        # You must create a processor before running this sample.
        name = client.[processor_version_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_version_path)(
            project_id, location, processor_id, processor_version
        )
    
        # Read the file into memory
        with open(file_path, "rb") as image:
            image_content = image.read()
    
        # Configure the process request
        request = documentai.[ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessRequest.html)(
            name=name,
            raw_document=documentai.[RawDocument](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.RawDocument.html)(content=image_content, mime_type=mime_type),
            # Only supported for Document OCR processor
            process_options=process_options,
        )
    
        result = client.[process_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_process_document)(request=request)
    
        # For a full list of `Document` object attributes, reference this page:
        # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
        return result.[document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
