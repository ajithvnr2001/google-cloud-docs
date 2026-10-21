---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-ocr-document/
title: Process a document using a Document OCR processor \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:17.362122+00:00
---

# Process a document using a Document OCR processor  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-process-ocr-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Process a document using a Document OCR processor Stay organized with collections  Save and categorize content based on your preferences. 

Sends an online processing request to a Document OCR processor and parses the response. Extracts and prints full text, page dimensions, detected languages, paragraphs, blocks, lines, and tokens.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enterprise Document OCR](https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr)
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
    
    public class ProcessOcrDocument {
      public static void processOcrDocument()
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-project-location"; // Format is "us" or "eu".
        String processerId = "your-processor-id";
        String filePath = "path/to/input/file.pdf";
        processOcrDocument(projectId, location, processerId, filePath);
      }
    
      public static void processOcrDocument(
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
          System.out.printf("Full document text: '%s'\n", escapeNewlines(text));
    
          // Read the text recognition output from the processor
          List<Document.Page> pages = documentResponse.getPagesList();
          System.out.printf("There are %s page(s) in this document.\n", pages.size());
    
          for (Document.Page page : pages) {
            System.out.printf("Page %d:\n", page.getPageNumber());
            printPageDimensions(page.getDimension());
            printDetectedLanguages(page.getDetectedLanguagesList());
            printParagraphs(page.getParagraphsList(), text);
            printBlocks(page.getBlocksList(), text);
            printLines(page.getLinesList(), text);
            printTokens(page.getTokensList(), text);
          }
        }
      }
    
      private static void printPageDimensions(Document.Page.Dimension dimension) {
        String unit = dimension.getUnit();
        System.out.printf("    Width: %.1f %s\n", dimension.getWidth(), unit);
        System.out.printf("    Height: %.1f %s\n", dimension.getHeight(), unit);
      }
    
      private static void printDetectedLanguages(
          List<Document.Page.DetectedLanguage> detectedLangauges) {
        System.out.println("    Detected languages:");
        for (Document.Page.DetectedLanguage detectedLanguage : detectedLangauges) {
          String languageCode = detectedLanguage.getLanguageCode();
          float confidence = detectedLanguage.getConfidence();
          System.out.printf("        %s (%.2f%%)\n", languageCode, confidence * 100.0);
        }
      }
    
      private static void printParagraphs(List<Document.Page.Paragraph> paragraphs, String text) {
        System.out.printf("    %d paragraphs detected:\n", paragraphs.size());
        Document.Page.Paragraph firstParagraph = paragraphs.get(0);
        String firstParagraphText = getLayoutText(firstParagraph.getLayout().getTextAnchor(), text);
        System.out.printf("        First paragraph text: %s\n", escapeNewlines(firstParagraphText));
        Document.Page.Paragraph lastParagraph = paragraphs.get(paragraphs.size() - 1);
        String lastParagraphText = getLayoutText(lastParagraph.getLayout().getTextAnchor(), text);
        System.out.printf("        Last paragraph text: %s\n", escapeNewlines(lastParagraphText));
      }
    
      private static void printBlocks(List<Document.Page.Block> blocks, String text) {
        System.out.printf("    %d blocks detected:\n", blocks.size());
        Document.Page.Block firstBlock = blocks.get(0);
        String firstBlockText = getLayoutText(firstBlock.getLayout().getTextAnchor(), text);
        System.out.printf("        First block text: %s\n", escapeNewlines(firstBlockText));
        Document.Page.Block lastBlock = blocks.get(blocks.size() - 1);
        String lastBlockText = getLayoutText(lastBlock.getLayout().getTextAnchor(), text);
        System.out.printf("        Last block text: %s\n", escapeNewlines(lastBlockText));
      }
    
      private static void printLines(List<Document.Page.Line> lines, String text) {
        System.out.printf("    %d lines detected:\n", lines.size());
        Document.Page.Line firstLine = lines.get(0);
        String firstLineText = getLayoutText(firstLine.getLayout().getTextAnchor(), text);
        System.out.printf("        First line text: %s\n", escapeNewlines(firstLineText));
        Document.Page.Line lastLine = lines.get(lines.size() - 1);
        String lastLineText = getLayoutText(lastLine.getLayout().getTextAnchor(), text);
        System.out.printf("        Last line text: %s\n", escapeNewlines(lastLineText));
      }
    
      private static void printTokens(List<Document.Page.Token> tokens, String text) {
        System.out.printf("    %d tokens detected:\n", tokens.size());
        Document.Page.Token firstToken = tokens.get(0);
        String firstTokenText = getLayoutText(firstToken.getLayout().getTextAnchor(), text);
        System.out.printf("        First token text: %s\n", escapeNewlines(firstTokenText));
        Document.Page.Token lastToken = tokens.get(tokens.size() - 1);
        String lastTokenText = getLayoutText(lastToken.getLayout().getTextAnchor(), text);
        System.out.printf("        Last token text: %s\n", escapeNewlines(lastTokenText));
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
    
      // Read the text recognition output from the processor
      // For a full list of Document object attributes,
      // please reference this page: https://googleapis.dev/nodejs/documentai/latest/index.html
      const {document} = result;
      const {text} = document;
    
      // Read the text recognition output from the processor
      console.log(`Full document text: ${JSON.stringify(text)}`);
      console.log(`There are ${document.pages.length} page(s) in this document.`);
      for (const page of document.pages) {
        console.log(`Page ${page.pageNumber}`);
        printPageDimensions(page.dimension);
        printDetectedLanguages(page.detectedLanguages);
        printParagraphs(page.paragraphs, text);
        printBlocks(page.blocks, text);
        printLines(page.lines, text);
        printTokens(page.tokens, text);
      }
    }
    
    const printPageDimensions = dimension => {
      console.log(`    Width: ${dimension.width}`);
      console.log(`    Height: ${dimension.height}`);
    };
    
    const printDetectedLanguages = detectedLanguages => {
      console.log('    Detected languages:');
      for (const lang of detectedLanguages) {
        const code = lang.languageCode;
        const confPercent = lang.confidence * 100;
        console.log(`        ${code} (${confPercent.toFixed(2)}% confidence)`);
      }
    };
    
    const printParagraphs = (paragraphs, text) => {
      console.log(`    ${paragraphs.length} paragraphs detected:`);
      const firstParagraphText = getText(paragraphs[0].layout.textAnchor, text);
      console.log(
        `        First paragraph text: ${JSON.stringify(firstParagraphText)}`
      );
      const lastParagraphText = getText(
        paragraphs[paragraphs.length - 1].layout.textAnchor,
        text
      );
      console.log(
        `        Last paragraph text: ${JSON.stringify(lastParagraphText)}`
      );
    };
    
    const printBlocks = (blocks, text) => {
      console.log(`    ${blocks.length} blocks detected:`);
      const firstBlockText = getText(blocks[0].layout.textAnchor, text);
      console.log(`        First block text: ${JSON.stringify(firstBlockText)}`);
      const lastBlockText = getText(
        blocks[blocks.length - 1].layout.textAnchor,
        text
      );
      console.log(`        Last block text: ${JSON.stringify(lastBlockText)}`);
    };
    
    const printLines = (lines, text) => {
      console.log(`    ${lines.length} lines detected:`);
      const firstLineText = getText(lines[0].layout.textAnchor, text);
      console.log(`        First line text: ${JSON.stringify(firstLineText)}`);
      const lastLineText = getText(
        lines[lines.length - 1].layout.textAnchor,
        text
      );
      console.log(`        Last line text: ${JSON.stringify(lastLineText)}`);
    };
    
    const printTokens = (tokens, text) => {
      console.log(`    ${tokens.length} tokens detected:`);
      const firstTokenText = getText(tokens[0].layout.textAnchor, text);
      console.log(`        First token text: ${JSON.stringify(firstTokenText)}`);
      const firstTokenBreakType = tokens[0].detectedBreak.type;
      console.log(`        First token break type: ${firstTokenBreakType}`);
      const lastTokenText = getText(
        tokens[tokens.length - 1].layout.textAnchor,
        text
      );
      console.log(`        Last token text: ${JSON.stringify(lastTokenText)}`);
      const lastTokenBreakType = tokens[tokens.length - 1].detectedBreak.type;
      console.log(`        Last token break type: ${lastTokenBreakType}`);
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
    
    
    def process_document_ocr_sample(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version: str,
        file_path: str,
        mime_type: str,
    ) -> None:
        # Optional: Additional configurations for Document OCR Processor.
        # For more information: https://cloud.google.com/document-ai/docs/enterprise-document-ocr
        process_options = documentai.[ProcessOptions](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessOptions.html)(
            ocr_config=documentai.[OcrConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.OcrConfig.html)(
                enable_native_pdf_parsing=True,
                enable_image_quality_scores=True,
                enable_symbol=True,
                # OCR Add Ons https://cloud.google.com/document-ai/docs/ocr-add-ons
                premium_features=documentai.[OcrConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.OcrConfig.html).[PremiumFeatures](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.OcrConfig.PremiumFeatures.html)(
                    compute_style_info=True,
                    enable_math_ocr=False,  # Enable to use Math OCR Model
                    enable_selection_mark_detection=True,
                ),
            )
        )
        # Online processing request to Document AI
        document = process_document(
            project_id,
            location,
            processor_id,
            processor_version,
            file_path,
            mime_type,
            process_options=process_options,
        )
    
        text = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text)
        print(f"Full document text: {[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text)}\n")
        print(f"There are {len([document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).pages)} page(s) in this document.\n")
    
        for page in [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).pages:
            print(f"Page {[page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).page_number}:")
            print_page_dimensions([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).dimension)
            print_detected_languages([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).detected_languages)
    
            print_blocks([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).blocks, text)
            print_paragraphs([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).paragraphs, text)
            print_lines([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).lines, text)
            print_tokens([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).tokens, text)
    
            if [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).symbols:
                print_symbols([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).symbols, text)
    
            if [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).image_quality_scores:
                print_image_quality_scores([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).image_quality_scores)
    
            if [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).visual_elements:
                print_visual_elements([page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).visual_elements, text)
    
    
    def print_page_dimensions(dimension: documentai.Document.Page.[Dimension](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.Dimension.html)) -> None:
        print(f"    Width: {str(dimension.width)}")
        print(f"    Height: {str(dimension.height)}")
    
    
    def print_detected_languages(
        detected_languages: Sequence[documentai.Document.Page.[DetectedLanguage](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.DetectedLanguage.html)],
    ) -> None:
        print("    Detected languages:")
        for lang in detected_languages:
            print(f"        {lang.language_code} ({lang.confidence:.1%} confidence)")
    
    
    def print_blocks(blocks: Sequence[documentai.Document.Page.Block], text: str) -> None:
        print(f"    {len(blocks)} blocks detected:")
        first_block_text = layout_to_text(blocks[0].layout, text)
        print(f"        First text block: {repr(first_block_text)}")
        last_block_text = layout_to_text(blocks[-1].layout, text)
        print(f"        Last text block: {repr(last_block_text)}")
    
    
    def print_paragraphs(
        paragraphs: Sequence[documentai.Document.Page.Paragraph], text: str
    ) -> None:
        print(f"    {len(paragraphs)} paragraphs detected:")
        first_paragraph_text = layout_to_text(paragraphs[0].layout, text)
        print(f"        First paragraph text: {repr(first_paragraph_text)}")
        last_paragraph_text = layout_to_text(paragraphs[-1].layout, text)
        print(f"        Last paragraph text: {repr(last_paragraph_text)}")
    
    
    def print_lines(lines: Sequence[documentai.Document.Page.Line], text: str) -> None:
        print(f"    {len(lines)} lines detected:")
        first_line_text = layout_to_text(lines[0].layout, text)
        print(f"        First line text: {repr(first_line_text)}")
        last_line_text = layout_to_text(lines[-1].layout, text)
        print(f"        Last line text: {repr(last_line_text)}")
    
    
    def print_tokens(tokens: Sequence[documentai.Document.Page.Token], text: str) -> None:
        print(f"    {len(tokens)} tokens detected:")
        first_token_text = layout_to_text(tokens[0].layout, text)
        first_token_break_type = tokens[0].detected_break.type_.name
        print(f"        First token text: {repr(first_token_text)}")
        print(f"        First token break type: {repr(first_token_break_type)}")
        if tokens[0].style_info:
            print_style_info(tokens[0].style_info)
    
        last_token_text = layout_to_text(tokens[-1].layout, text)
        last_token_break_type = tokens[-1].detected_break.type_.name
        print(f"        Last token text: {repr(last_token_text)}")
        print(f"        Last token break type: {repr(last_token_break_type)}")
        if tokens[-1].style_info:
            print_style_info(tokens[-1].style_info)
    
    
    def print_symbols(
        symbols: Sequence[documentai.Document.Page.Symbol], text: str
    ) -> None:
        print(f"    {len(symbols)} symbols detected:")
        first_symbol_text = layout_to_text(symbols[0].layout, text)
        print(f"        First symbol text: {repr(first_symbol_text)}")
        last_symbol_text = layout_to_text(symbols[-1].layout, text)
        print(f"        Last symbol text: {repr(last_symbol_text)}")
    
    
    def print_image_quality_scores(
        image_quality_scores: documentai.Document.Page.[ImageQualityScores](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.ImageQualityScores.html),
    ) -> None:
        print(f"    Quality score: {image_quality_scores.quality_score:.1%}")
        print("    Detected defects:")
    
        for detected_defect in image_quality_scores.detected_defects:
            print(f"        {detected_defect.type_}: {detected_defect.confidence:.1%}")
    
    
    def print_style_info(style_info: documentai.Document.Page.Token.[StyleInfo](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.Token.StyleInfo.html)) -> None:
        """
        Only supported in version `pretrained-ocr-v2.0-2023-06-02`
        """
        print(f"           Font Size: {style_info.font_size}pt")
        print(f"           Font Type: {style_info.font_type}")
        print(f"           Bold: {style_info.bold}")
        print(f"           Italic: {style_info.italic}")
        print(f"           Underlined: {style_info.underlined}")
        print(f"           Handwritten: {style_info.handwritten}")
        print(
            f"           Text Color (RGBa): {style_info.text_color.red}, {style_info.text_color.green}, {style_info.text_color.blue}, {style_info.text_color.alpha}"
        )
    
    
    def print_visual_elements(
        visual_elements: Sequence[documentai.Document.Page.[VisualElement](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document.Page.VisualElement.html)], text: str
    ) -> None:
        """
        Only supported in version `pretrained-ocr-v2.0-2023-06-02`
        """
        checkboxes = [x for x in visual_elements if "checkbox" in x.type]
        math_symbols = [x for x in visual_elements if x.type == "math_formula"]
    
        if checkboxes:
            print(f"    {len(checkboxes)} checkboxes detected:")
            print(f"        First checkbox: {repr(checkboxes[0].type)}")
            print(f"        Last checkbox: {repr(checkboxes[-1].type)}")
    
        if math_symbols:
            print(f"    {len(math_symbols)} math symbols detected:")
            first_math_symbol_text = layout_to_text(math_symbols[0].layout, text)
            print(f"        First math symbol: {repr(first_math_symbol_text)}")
    
    
    
    
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
