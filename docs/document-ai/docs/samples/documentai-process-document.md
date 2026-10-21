---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-document/
title: Send an online processing request \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:19.944780+00:00
---

# Send an online processing request  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Send an online processing request Stay organized with collections  Save and categorize content based on your preferences. 

Online (synchronous) requests let send a single document for processing.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Send a processing request](https://docs.cloud.google.com/document-ai/docs/send-request)



## Code sample

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System;
    using System.IO;
    
    public class QuickstartSample
    {
        public Document Quickstart(
            string projectId = "your-project-id",
            string locationId = "your-processor-location",
            string processorId = "your-processor-id",
            string localPath = "my-local-path/my-file-name",
            string mimeType = "application/pdf"
        )
        {
            // Create client
            var client = new [DocumentProcessorServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClientBuilder.html)
            {
                Endpoint = $"{locationId}-documentai.googleapis.com"
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClientBuilder.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClientBuilder_Build)();
    
            // Read in local file
            using var fileStream = File.OpenRead(localPath);
            var rawDocument = new [RawDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.RawDocument.html)
            {
                Content = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromStream_System_IO_Stream_)(fileStream),
                MimeType = mimeType
            };
    
            // Initialize request argument(s)
            var request = new [ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessRequest.html)
            {
                Name = [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html).[FromProjectLocationProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html#Google_Cloud_DocumentAI_V1_ProcessorName_FromProjectLocationProcessor_System_String_System_String_System_String_)(projectId, locationId, processorId).ToString(),
                RawDocument = rawDocument
            };
    
            // Make the request
            var response = client.ProcessDocument(request);
    
            var document = response.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessResponse.html#Google_Cloud_DocumentAI_V1_ProcessResponse_Document);
            Console.WriteLine(document.Text);
            return document;
        }
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings.html);
    import com.google.cloud.documentai.v1.[ProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest.html);
    import com.google.cloud.documentai.v1.[ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse.html);
    import com.google.cloud.documentai.v1.[RawDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.RawDocument.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ProcessDocument {
      public static void processDocument()
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processerId = "your-processor-id";
        String filePath = "path/to/input/file.pdf";
        processDocument(projectId, location, processerId, filePath);
      }
    
      public static void processDocument(
          String projectId, String location, String processorId, String filePath)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
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
    
          // Read the file.
          byte[] imageFileData = Files.readAllBytes(Paths.get(filePath));
    
          // Convert the image data to a Buffer and base64 encode it.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) content = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(imageFileData);
    
          [RawDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.RawDocument.html) document =
              [RawDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.RawDocument.html).newBuilder().setContent(content).setMimeType("application/pdf").build();
    
          // Configure the process request.
          [ProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest.html) request =
              [ProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest.html).newBuilder().setName(name).[setRawDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest.Builder.html#com_google_cloud_documentai_v1_ProcessRequest_Builder_setRawDocument_com_google_cloud_documentai_v1_RawDocument_)(document).build();
    
          // Recognizes text entities in the PDF document
          [ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse.html) result = client.processDocument(request);
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html) documentResponse = result.[getDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse.html#com_google_cloud_documentai_v1_ProcessResponse_getDocument__)();
    
          // Get all of the document text as one big string
          String text = documentResponse.[getText](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html#com_google_cloud_documentai_v1_Document_getText__)();
    
          // Read the text recognition output from the processor
          System.out.println("The document contains the following paragraphs:");
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.html) firstPage = documentResponse.[getPages](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html#com_google_cloud_documentai_v1_Document_getPages_int_)(0);
          List<Document.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.html).[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Paragraph.html)> paragraphs = firstPage.getParagraphsList();
    
          for ([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.html).[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Paragraph.html) paragraph : paragraphs) {
            String paragraphText = getText(paragraph.getLayout().getTextAnchor(), text);
            System.out.printf("Paragraph text:\n%s\n", paragraphText);
          }
    
          // Form parsing provides additional output about
          // form-formatted PDFs. You must create a form
          // processor in the Cloud Console to see full field details.
          System.out.println("The following form key/value pairs were detected:");
    
          for ([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.html).[FormField](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.FormField.html) field : firstPage.getFormFieldsList()) {
            String fieldName = getText(field.getFieldName().getTextAnchor(), text);
            String fieldValue = getText(field.getFieldValue().getTextAnchor(), text);
    
            System.out.println("Extracted form fields pair:");
            System.out.printf("\t(%s, %s))\n", fieldName, fieldValue);
          }
        }
      }
    
      // Extract shards from the text field
      private static String getText([Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.html).[TextAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.TextAnchor.html) textAnchor, String text) {
        if (textAnchor.getTextSegmentsList().size() > 0) {
          int startIdx = (int) textAnchor.getTextSegments(0).getStartIndex();
          int endIdx = (int) textAnchor.getTextSegments(0).getEndIndex();
          return text.[substring](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_substring_int_)(startIdx, endIdx);
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
    // const processorId = 'YOUR_PROCESSOR_ID'; // Create processor in Cloud Console
    // const filePath = '/path/to/local/pdf';
    
    const {DocumentProcessorServiceClient} =
      require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1;
    
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
      const {document} = result;
    
      // Get all of the document text as one big string
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
    }

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION" # Format is "us" or "eu"
    # processor_id = "YOUR_PROCESSOR_ID" # Create processor before running sample
    # file_path = "/path/to/local/pdf"
    # mime_type = "application/pdf" # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
    # field_mask = "text,entities,pages.pageNumber"  # Optional. The fields to return in the Document object.
    # processor_version_id = "YOUR_PROCESSOR_VERSION_ID" # Optional. Processor version to use
    
    
    def process_document_sample(
        project_id: str,
        location: str,
        processor_id: str,
        file_path: str,
        mime_type: str,
        field_mask: Optional[str] = None,
        processor_version_id: Optional[str] = None,
    ) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        if processor_version_id:
            # The full resource name of the processor version, e.g.:
            # `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
            name = client.[processor_version_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_version_path)(
                project_id, location, processor_id, processor_version_id
            )
        else:
            # The full resource name of the processor, e.g.:
            # `projects/{project_id}/locations/{location}/processors/{processor_id}`
            name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        # Read the file into memory
        with open(file_path, "rb") as image:
            image_content = image.read()
    
        # Load binary data
        raw_document = documentai.[RawDocument](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.RawDocument.html)(content=image_content, mime_type=mime_type)
    
        # For more information: https://cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions
        # Optional: Additional configurations for processing.
        process_options = documentai.[ProcessOptions](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessOptions.html)(
            # Process only specific pages
            individual_page_selector=documentai.[ProcessOptions](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessOptions.html).[IndividualPageSelector](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessOptions.IndividualPageSelector.html)(
                pages=[1]
            )
        )
    
        # Configure the process request
        request = documentai.[ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessRequest.html)(
            name=name,
            raw_document=raw_document,
            field_mask=field_mask,
            process_options=process_options,
        )
    
        result = client.[process_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_process_document)(request=request)
    
        # For a full list of `Document` object attributes, reference this page:
        # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
        document = result.[document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html)
    
        # Read the text recognition output from the processor
        print("The document contains the following text:")
        print([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
