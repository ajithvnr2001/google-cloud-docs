---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-form-document/
title: Process a document using a Form Parser processor \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:05.919503+00:00
---

# Process a document using a Form Parser processor  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-form-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Process a document using a Form Parser processor Stay organized with collections  Save and categorize content based on your preferences. 

Sends an online processing request to a Form Parser processor and parses the response. Extracts and prints form fields and tables.

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
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ProcessFormDocument {
      public static void processFormDocument()
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processerId = "your-processor-id";
        String filePath = "path/to/input/file.pdf";
        processFormDocument(projectId, location, processerId, filePath);
      }
    
      public static void processFormDocument(
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
    
          // Read the text recognition output from the processor
          // For a full list of Document object attributes,
          // please reference this page:
          // https://googleapis.dev/java/google-cloud-document-ai/latest/index.html
    
          // Get all of the document text as one big string
          String text = documentResponse.getText();
          System.out.printf("Full document text: '%s'\n", removeNewlines(text));
    
          // Read the text recognition output from the processor
          List<Document.Page> pages = documentResponse.getPagesList();
          System.out.printf("There are %s page(s) in this document.\n", pages.size());
    
          for (Document.Page page : pages) {
            System.out.printf("\n\n**** Page %d ****\n", page.getPageNumber());
    
            List<Document.Page.Table> tables = page.getTablesList();
            System.out.printf("Found %d table(s):\n", tables.size());
            for (Document.Page.Table table : tables) {
              printTableInfo(table, text);
            }
    
            List<Document.Page.FormField> formFields = page.getFormFieldsList();
            System.out.printf("Found %d form fields:\n", formFields.size());
            for (Document.Page.FormField formField : formFields) {
              String fieldName = getLayoutText(formField.getFieldName().getTextAnchor(), text);
              String fieldValue = getLayoutText(formField.getFieldValue().getTextAnchor(), text);
              System.out.printf(
                  "    * '%s': '%s'\n", removeNewlines(fieldName), removeNewlines(fieldValue));
            }
          }
        }
      }
    
      private static void printTableInfo(Document.Page.Table table, String text) {
        Document.Page.Table.TableRow firstBodyRow = table.getBodyRows(0);
        int columnCount = firstBodyRow.getCellsCount();
        System.out.printf(
            "    Table with %d columns and %d rows:\n", columnCount, table.getBodyRowsCount());
    
        Document.Page.Table.TableRow headerRow = table.getHeaderRows(0);
        StringBuilder headerRowText = new StringBuilder();
        for (Document.Page.Table.TableCell cell : headerRow.getCellsList()) {
          String columnName = getLayoutText(cell.getLayout().getTextAnchor(), text);
          headerRowText.append(String.format("%s | ", removeNewlines(columnName)));
        }
        headerRowText.setLength(headerRowText.length() - 3);
        System.out.printf("        Collumns: %s\n", headerRowText.toString());
    
        StringBuilder firstRowText = new StringBuilder();
        for (Document.Page.Table.TableCell cell : firstBodyRow.getCellsList()) {
          String cellText = getLayoutText(cell.getLayout().getTextAnchor(), text);
          firstRowText.append(String.format("%s | ", removeNewlines(cellText)));
        }
        firstRowText.setLength(firstRowText.length() - 3);
        System.out.printf("        First row data: %s\n", firstRowText.toString());
      }
    
      // Extract shards from the text field
      private static String getLayoutText(Document.TextAnchor textAnchor, String text) {
        if (textAnchor.getTextSegmentsList().size() > 0) {
          int startIdx = (int) textAnchor.getTextSegments(0).getStartIndex();
          int endIdx = (int) textAnchor.getTextSegments(0).getEndIndex();
          return text.[substring](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_substring_int_)(startIdx, endIdx);
        }
        return "[NO TEXT]";
      }
    
      private static String removeNewlines(String s) {
        return s.replace("\n", "").replace("\r", "");
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
    
      // Read the table and form fields output from the processor
      // The form processor also contains OCR data. For more information
      // on how to parse OCR data please see the OCR sample.
      // For a full list of Document object attributes,
      // please reference this page: https://googleapis.dev/nodejs/documentai/latest/index.html
      const {document} = result;
      const {text} = document;
      console.log(`Full document text: ${JSON.stringify(text)}`);
      console.log(`There are ${document.pages.length} page(s) in this document.`);
    
      for (const page of document.pages) {
        console.log(`\n\n**** Page ${page.pageNumber} ****`);
    
        console.log(`Found ${page.tables.length} table(s):`);
        for (const table of page.tables) {
          const numCollumns = table.headerRows[0].cells.length;
          const numRows = table.bodyRows.length;
          console.log(`Table with ${numCollumns} columns and ${numRows} rows:`);
          printTableInfo(table, text);
        }
        console.log(`Found ${page.formFields.length} form field(s):`);
        for (const field of page.formFields) {
          const fieldName = getText(field.fieldName.textAnchor, text);
          const fieldValue = getText(field.fieldValue.textAnchor, text);
          console.log(
            `\t* ${JSON.stringify(fieldName)}: ${JSON.stringify(fieldValue)}`
          );
        }
      }
    }
    
    const printTableInfo = (table, text) => {
      // Print header row
      let headerRowText = '';
      for (const headerCell of table.headerRows[0].cells) {
        const headerCellText = getText(headerCell.layout.textAnchor, text);
        headerRowText += `${JSON.stringify(headerCellText.trim())} | `;
      }
      console.log(
        `Collumns: ${headerRowText.substring(0, headerRowText.length - 3)}`
      );
      // Print first body row
      let bodyRowText = '';
      for (const bodyCell of table.bodyRows[0].cells) {
        const bodyCellText = getText(bodyCell.layout.textAnchor, text);
        bodyRowText += `${JSON.stringify(bodyCellText.trim())} | `;
      }
      console.log(
        `First row data: ${bodyRowText.substring(0, bodyRowText.length - 3)}`
      );
    };
    
    // Extract shards from the text field
    const getText = (textAnchor, text) => {
      if (!textAnchor.textSegments || textAnchor.textSegments.length === 0) {
        return '';
      }
    
      // First shard in document doesn't have startIndex property
      const startIndex = textAnchor.textSegments[0].startIndex || 0;
      const endIndex = textAnchor.textSegments[0].endIndex;
    
      return text.substring(startIndex, endIndex);
    };
    

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
    
    
    def process_document_form_sample(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version: str,
        file_path: str,
        mime_type: str,
    ) -> documentai.Document:
        # Online processing request to Document AI
        document = process_document(
            project_id, location, processor_id, processor_version, file_path, mime_type
        )
    
        # Read the table and form fields output from the processor
        # The form processor also contains OCR data. For more information
        # on how to parse OCR data please see the OCR sample.
    
        text = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text)
        print(f"Full document text: {repr(text)}\n")
        print(f"There are {len([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).pages)} page(s) in this document.")
    
        # Read the form fields and tables output from the processor
        for page in [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).pages:
            print(f"\n\n**** Page {[page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).page_number} ****")
    
            print(f"\nFound {len([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).tables)} table(s):")
            for table in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).tables:
                num_columns = len(table.header_rows[0].cells)
                num_rows = len(table.body_rows)
                print(f"Table with {num_columns} columns and {num_rows} rows:")
    
                # Print header rows
                print("Columns:")
                print_table_rows(table.header_rows, text)
                # Print body rows
                print("Table body data:")
                print_table_rows(table.body_rows, text)
    
            print(f"\nFound {len([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).form_fields)} form field(s):")
            for field in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).form_fields:
                name = layout_to_text(field.field_name, text)
                value = layout_to_text(field.field_value, text)
                print(f"    * {repr(name.strip())}: {repr(value.strip())}")
    
        # Supported in version `pretrained-form-parser-v2.0-2022-11-10` and later.
        # For more information: https://cloud.google.com/document-ai/docs/form-parser
        if [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).entities:
            print(f"Found {len([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).entities)} generic entities:")
            for entity in [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).entities:
                print_entity(entity)
                # Print Nested Entities
                for prop in [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).properties:
                    print_entity(prop)
    
        return document
    
    
    def print_table_rows(
        table_rows: Sequence[documentai.Document.Page.Table.[TableRow](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.Table.TableRow.html)], text: str
    ) -> None:
        for table_row in table_rows:
            row_text = ""
            for cell in table_row.cells:
                cell_text = layout_to_text(cell.layout, text)
                row_text += f"{repr(cell_text.strip())} | "
            print(row_text)
    
    
    
    
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
    
    
    
    
    def layout_to_text(layout: documentai.Document.Page.[Layout](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.Layout.html), text: str) -> str:
        """
        Document AI identifies text in different parts of the document by their
        offsets in the entirety of the document"s text. This function converts
        offsets to a string.
        """
        # If a text segment spans several lines, it will
        # be stored in different text segments.
        return "".join(
            text[int(segment.start_index) : int(segment.end_index)]
            for segment in layout.text_anchor.text_segments
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
