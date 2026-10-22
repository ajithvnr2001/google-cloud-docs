---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-quickstart/
title: Quickstart \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:00.924564+00:00
---

# Quickstart  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Process a document using Document AI.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Document AI client libraries](https://docs.cloud.google.com/document-ai/docs/libraries)
  * [Quickstart: Process documents by using client libraries](https://docs.cloud.google.com/document-ai/docs/process-documents-client-libraries)



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
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"os"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	"cloud.google.com/go/documentai/apiv1/documentaipb"
    	"google.golang.org/api/option"
    )
    
    func main() {
    	projectID := flag.String("project_id", "PROJECT_ID", "Cloud Project ID")
    	location := flag.String("location", "us", "The Processor location")
    	// Create a Processor before running sample
    	processorID := flag.String("processor_id", "aaaaaaaa", "The Processor ID")
    	filePath := flag.String("file_path", "invoice.pdf", "The path to the file to parse")
    	mimeType := flag.String("mime_type", "application/pdf", "The mimeType of the file")
    	flag.Parse()
    
    	ctx := context.Background()
    
    	endpoint := fmt.Sprintf("%s-documentai.googleapis.com:443", *location)
    	client, err := documentai.[NewDocumentProcessorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_NewDocumentProcessorClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		fmt.Println(fmt.Errorf("error creating Document AI client: %w", err))
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_Close)()
    
    	// Open local file.
    	data, err := os.ReadFile(*filePath)
    	if err != nil {
    		fmt.Println(fmt.Errorf("os.ReadFile: %w", err))
    	}
    
    	req := &documentaipb.ProcessRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/processors/%s", *projectID, *location, *processorID),
    		Source: &documentaipb.ProcessRequest_RawDocument{
    			RawDocument: &documentaipb.RawDocument{
    				Content:  data,
    				MimeType: *mimeType,
    			},
    		},
    	}
    	resp, err := client.ProcessDocument(ctx, req)
    	if err != nil {
    		fmt.Println(fmt.Errorf("processDocument: %w", err))
    	}
    
    	// Handle the results.
    	document := resp.GetDocument()
    	fmt.Printf("Document Text: %s", document.GetText())
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
    
    public class QuickStart {
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processorId = "your-processor-id";
        String filePath = "path/to/input/file.pdf";
        quickStart(projectId, location, processorId, filePath);
      }
    
      public static void quickStart(
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
    // apiEndpoint regions available: eu-documentai.googleapis.com, us-documentai.googleapis.com (Required if using eu based processor)
    // const client = new DocumentProcessorServiceClient({apiEndpoint: 'eu-documentai.googleapis.com'});
    const client = new [DocumentProcessorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)();
    
    async function quickstart() {
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
    }

### PHP

For more information, see the [Document AI PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-document-ai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Include the autoloader for libraries installed with Composer.
    require __DIR__ . '/vendor/autoload.php';
    
    # Import the Google Cloud client library.
    use Google\Cloud\DocumentAI\V1\Client\DocumentProcessorServiceClient;
    use Google\Cloud\DocumentAI\V1\RawDocument;
    use Google\Cloud\DocumentAI\V1\ProcessRequest;
    
    # TODO(developer): Update the following lines before running the sample.
    # Your Google Cloud Platform project ID.
    $projectId = 'YOUR_PROJECT_ID';
    
    # Your Processor Location.
    $location = 'us';
    
    # Your Processor ID as hexadecimal characters.
    # Not to be confused with the Processor Display Name.
    $processorId = 'YOUR_PROCESSOR_ID';
    
    # Path for the file to read.
    $documentPath = 'resources/invoice.pdf';
    
    # Create Client.
    $client = new DocumentProcessorServiceClient();
    
    # Read in file.
    $handle = fopen($documentPath, 'rb');
    $contents = fread($handle, filesize($documentPath));
    fclose($handle);
    
    # Load file contents into a RawDocument.
    $rawDocument = (new RawDocument())
        ->setContent($contents)
        ->SetMimeType('application/pdf');
    
    # Get the Fully-qualified Processor Name.
    $fullProcessorName = $client->processorName($projectId, $location, $processorId);
    
    # Send a ProcessRequest and get a ProcessResponse.
    $request = (new ProcessRequest())
        ->setName($fullProcessorName)
        ->setRawDocument($rawDocument);
    
    $response = $client->processDocument($request);
    
    # Show the text found in the document.
    printf('Document Text: %s', $response->getDocument()->getText());

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import [documentai_v1](https://docs.cloud.google.com/python/docs/reference/documentai/latest)
    
    # TODO(developer): Create a processor of type "OCR_PROCESSOR".
    
    # TODO(developer): Update and uncomment these variables before running the sample.
    # project_id = "MY_PROJECT_ID"
    
    # Processor ID as hexadecimal characters.
    # Not to be confused with the Processor Display Name.
    # processor_id = "MY_PROCESSOR_ID"
    
    # Processor location. For example: "us" or "eu".
    # location = "MY_PROCESSOR_LOCATION"
    
    # Path for file to process.
    # file_path = "/path/to/local/pdf"
    
    # Set `api_endpoint` if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
    # Initialize Document AI client.
    client = [documentai_v1](https://docs.cloud.google.com/python/docs/reference/documentai/latest).[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
    # Get the Fully-qualified Processor path.
    full_processor_name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
    # Get a Processor reference.
    request = [documentai_v1](https://docs.cloud.google.com/python/docs/reference/documentai/latest).[GetProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GetProcessorRequest.html)(name=full_processor_name)
    processor = client.[get_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_get_processor)(request=request)
    
    # `processor.name` is the full resource name of the processor.
    # For example: `projects/{project_id}/locations/{location}/processors/{processor_id}`
    print(f"Processor Name: {processor.name}")
    
    # Read the file into memory.
    with open(file_path, "rb") as image:
        image_content = image.read()
    
    # Load binary data.
    # For supported MIME types, refer to https://cloud.google.com/document-ai/docs/file-types
    raw_document = [documentai_v1](https://docs.cloud.google.com/python/docs/reference/documentai/latest).[RawDocument](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.RawDocument.html)(
        content=image_content,
        mime_type="application/pdf",
    )
    
    # Send a request and get the processed document.
    request = [documentai_v1](https://docs.cloud.google.com/python/docs/reference/documentai/latest).[ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessRequest.html)(name=processor.name, raw_document=raw_document)
    result = client.[process_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_process_document)(request=request)
    document = result.[document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html)
    
    # Read the text recognition output from the processor.
    # For a full list of `Document` object attributes, reference this page:
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    print("The document contains the following text:")
    print([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Document AI quickstart
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location_id [String] Your Processor Location (e.g. "us")
    # @param processor_id [String] Your Processor ID (e.g. "a14dae8f043b60bd")
    # @param file_path [String] Path to Local File (e.g. "invoice.pdf")
    # @param mime_type [String] Refer to https://cloud.google.com/document-ai/docs/file-types (e.g. "application/pdf")
    #
    def quickstart project_id:, location_id:, processor_id:, file_path:, mime_type:
      # Create the Document AI client.
      client = ::Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new do |config|
        config.endpoint = "#{location_id}-documentai.googleapis.com"
      end
    
      # Build the resource name from the project.
      name = client.processor_path(
        project: project_id,
        location: location_id,
        processor: processor_id
      )
    
      # Read the bytes into memory
      content = File.binread file_path
    
      # Create request
      request = Google::Cloud::DocumentAI::V1::ProcessRequest.new(
        skip_human_review: true,
        name: name,
        raw_document: {
          content: content,
          mime_type: mime_type
        }
      )
    
      # Process document
      response = client.process_document request
    
      # Handle response
      puts response.document.text
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
