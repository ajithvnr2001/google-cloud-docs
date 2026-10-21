---
url: https://docs.cloud.google.com/translate/docs/advanced/translate-documents/
title: Translate documents \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:58.986365+00:00
---

# Translate documents  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/translate-documents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Translate documents

Cloud Translation - Advanced provides a Document Translation API for directly translating formatted documents such as PDF and DOCX. Compared to plain text translations, Document Translation preserves the original formatting and layout in your translated documents, helping you retain much of the original context like paragraph breaks.

The following sections describe how to translate documents and use Document Translation with other Cloud Translation - Advanced features like glossaries and AutoML Translation models. Document Translation supports both online and batch translation requests.

For plain text and HTML translations, see [Translating text](https://docs.cloud.google.com/translate/docs/advanced/translating-text-v3).

## Supported file formats

Document Translation support the following input file types and their associated output file types.

Inputs | Document MIME type | Output  
---|---|---  
DOC* | application/msword | DOC, DOCX  
DOCX* | application/vnd.openxmlformats-officedocument.wordprocessingml.document | DOCX  
PDF† | application/pdf | PDF, DOCX  
PPT | application/vnd.ms-powerpoint | PPT, PPTX  
PPTX | application/vnd.openxmlformats-officedocument.presentationml.presentation | PPTX  
XLS | application/vnd.ms-excel | XLS, XLSX  
XLSX | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | XLSX  
  
*Content inside text boxes aren't translated and remain in the source language.

†Document Translation supports both native and scanned PDF documents with some differences. For optimal format handling, use native PDF files when possible. Translating scanned PDF files results in some formatting loss. Complex PDF layouts can also result in some formatting loss, which can include data tables, multi-column layouts, and graphs with labels or legends.

If you have PDF content in the DOCX or PPTX format, we recommend that you translate content by using those formats before converting them to PDFs. In general, Document Translation preserves a document's layout and style of DOCX and PPTX files better than PDF files. After a document translation, you can then convert the results to PDF files.

## Native and scanned PDF document translations

Document Translation supports both native and scanned PDF files, including translations to or from right-to-left languages. Support for PDF to DOCX conversions is available for batch document translations on native PDF files only. Also, Document Translation preserves hyperlinks, font size, and font color for native PDF files only (for both synchronous and batch translations).

If you translate a PDF file with a mix of scanned and native PDF content, the scanned content isn't translated.

## Before you begin

Before you can start using the Cloud Translation API, you should complete the [Cloud Translation setup](https://docs.cloud.google.com/translate/docs/setup) page, which includes creating a project, enabling the Cloud Translation API, and setting up authentication. The setup page also provides instructions for installing client libraries for common programming languages, which is optional.

### Required permissions

For requests that require Cloud Storage access, such as batch Document Translation, you might require Cloud Storage permissions to read input files or send output files to a bucket. For example, to read input files from a bucket, you must have at least read object permissions (provided by the role `roles/storage.objectViewer`) on the bucket. For more information about Cloud Storage roles, see the Cloud Storage [documentation](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Translate documents (online)

Online translation provides real-time processing (synchronous processing) of a single file.

For PDFs, the file size can be up to 20 MB and up to 300 pages for native PDFs (requires the `isTranslateNativePdfOnly` field to be `true`). If you enable the `enableShadowRemovalNativePdf` field, the limit is 20 pages. For scanned PDFs, the limit is 20 pages.

For other document types, the file sizes can be up to 20 MB with no page limits.

### Translate a document from Cloud Storage

The following example translates a file from a Cloud Storage bucket and outputs the result to a Cloud Storage bucket. The response also returns a byte stream. You can specify the MIME type; if you don't, Document Translation determines it by using the input file's extension.

If you don't specify a source language code, Document Translation detects the language for you. The detected language is included in the output in the `detectedLanguageCode` field.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: The numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: Region where you want to run this operation. For example, `us-central1`.
  * SOURCE_LANGUAGE: (Optional) The language code of the input document. If known, set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language to translate the input document to. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * INPUT_FILE_PATH: The Cloud Storage location and file name of the input document.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where the output document will be stored.
  * IS_NATIVE: (Optional) For native PDF documents, a boolean value that indicates whether your request uses the native or scanned PDF page limit. If true, the page limit is increased to 300 pages for native PDF documents only. If false or unspecified, the scanned PDF page limit is used (20 pages).



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_code": "TARGET_LANGUAGE",
      "document_input_config": {
        "gcsSource": {
          "inputUri": "gs://INPUT_FILE_PATH"
        }
      },
      "document_output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      },
      "isTranslateNativePdfOnly": IS_NATIVE
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "documentTranslation": {
        "byteStreamOutputs": ["BYTE_STREAM"],
        "mimeType": "MIME_TYPE"
      },
      "model": "projects/PROJECT_NUMBER/locations/LOCATION/models/general/nmt"
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const inputUri = 'path_to_your_file';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v3beta1;
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    const documentInputConfig = {
      gcsSource: {
        inputUri: inputUri,
      },
    };
    
    async function translateDocument() {
      // Construct request
      const request = {
        parent: translationClient.locationPath(projectId, location),
        documentInputConfig: documentInputConfig,
        sourceLanguageCode: 'en-US',
        targetLanguageCode: 'sr-Latn',
      };
    
      // Run request
      const [response] = await translationClient.translateDocument(request);
    
      console.log(
        `Response: Mime Type - ${response.documentTranslation.mimeType}`
      );
    }
    
    translateDocument();

### Translate a document inline

The following example sends a document inline as part of the request. You must include the MIME type for inline document translations.

If you don't specify a source language code, Document Translation detects the language for you. The detected language is included in the output in the `detectedLanguageCode` field.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: The numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: Region where you want to run this operation. For example, `us-central1`.
  * SOURCE_LANGUAGE: (Optional) The language code of the input document. If known, set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language to translate the input document to. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * MIME_TYPE: The format of the source document, such as `application/pdf`.
  * INPUT_BYTE_STREAM: The input document's content represented as a stream of bytes.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where the output document will be stored.
  * IS_NATIVE: (Optional) For native PDF documents, a boolean value that indicates whether your request uses the native or scanned PDF page limit. If true, the page limit is increased to 300 pages for native PDF documents only. If false or unspecified, the scanned PDF page limit is used (20 pages).



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_code": "TARGET_LANGUAGE",
      "document_input_config": {
        "mimeType": "MIME_TYPE",
        "content": "INPUT_BYTE_STREAM"
      },
      "document_output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      },
      "isTranslateNativePdfOnly": IS_NATIVE
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "documentTranslation": {
        "byteStreamOutputs": ["BYTE_STREAM"],
        "mimeType": "MIME_TYPE"
      },
      "model": "projects/PROJECT_NUMBER/locations/LOCATION/models/general/nmt"
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3beta1 as translate
    
    
    def translate_document(
        project_id: str,
        file_path: str,
    ) -> translate.TranslationServiceClient:
        """Translates a document.
    
        Args:
            project_id: The GCP project ID.
            file_path: The path to the file to be translated.
    
        Returns:
            The translated document.
        """
    
        client = translate.TranslationServiceClient()
        location = "us-central1"
        parent = f"projects/{project_id}/locations/{location}"
    
        # Supported file types: https://cloud.google.com/translate/docs/supported-formats
        with open(file_path, "rb") as document:
            document_content = document.read()
    
        document_input_config = {
            "content": document_content,
            "mime_type": "application/pdf",
        }
    
        response = client.translate_document(
            request={
                "parent": parent,
                "target_language_code": "fr-FR",
                "document_input_config": document_input_config,
            }
        )
    
        # To output the translated document, uncomment the code below.
        # f = open('/tmp/output', 'wb')
        # f.write(response.document_translation.byte_stream_outputs[0])
        # f.close()
    
        # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
        # and its output mime type will be the same as the input file's mime type
        print(
            f"Response: Detected Language Code - {response.document_translation.detected_language_code}"
        )
    
        return response
    
    

### Use an AutoML model or a glossary

Instead of the Google-managed model, you can use your own AutoML Translation models to translate documents. In addition to specifying a model, you can also include a glossary to handle domain-specific terminology. If you specify a model or a glossary, you must specify the source language. The following example uses an AutoML model and a glossary. If the model or glossary are in a different project, you must have the corresponding IAM permission to access those resources.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: The numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: Region where you want to run this operation, such as `us-central1`. The location must match the region where your model, glossary, or both are located.
  * SOURCE_LANGUAGE: The language code of the input document. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language to translate the input document to. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * INPUT_FILE_PATH: The Cloud Storage location and file name of the input document.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where the output document will be stored.
  * MODEL_PROJECT_ID: The project ID where the model is located.
  * MODEL_LOCATION: The region where the model is located.
  * MODEL_ID: The ID of the model to use.
  * GLOSSARY_PROJECT_ID: The project ID where the glossary is located.
  * GLOSSARY_LOCATION: The region where the glossary is located.
  * GLOSSARY_ID: The ID of the glossary to use.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_code": "TARGET_LANGUAGE",
      "document_input_config": {
        "gcsSource": {
          "inputUri": "gs://INPUT_FILE_PATH"
        }
      },
      "document_output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      },
      "model": "projects/MODEL_PROJECT_ID/locations/MODEL_LOCATION/models/MODEL_ID",
      "glossary_config": {
        "glossary": "projects/GLOSSARY_PROJECT_ID/locations/MODEL_LOCATION/glossaries/GLOSSARY_ID"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "documentTranslation": {
        "byteStreamOutputs": ["BYTE_STREAM"],
        "mimeType": "MIME_TYPE"
      },
      "glossary_document_translation": {
        "byteStreamOutputs": ["BYTE_STREAM_USING_GLOSSARY"],
        "mimeType": "MIME_TYPE"
      },
      "model": "projects/MODEL_PROJECT_ID/locations/MODEL_LOCATION/models/MODEL_ID",
      "glossaryConfig": {
        "glossary": "projects/GLOSSARY_PROJECT_ID/locations/MODEL_LOCATION/glossaries/GLOSSARY_ID"
      }
    }
    

## Translate documents (batch)

Batch translation allows you to translate multiple files into multiple languages in a single request. For each request, you can send up to 100 files with a total content size of up to 1 GB or 100 million Unicode codepoints, whichever limit is hit first. You can specify a particular translation model for each language.

### Translate multiple documents

The following example includes multiple input configurations. Each input configuration is a pointer to a file in a Cloud Storage bucket.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: Region where you want to run this operation. For example, `us-central1`.
  * SOURCE_LANGUAGE: The language code of the input documents. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language or languages to translate the input documents to. Use the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * INPUT_FILE_PATH: The Cloud Storage location and file name of one or more input documents.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where all output documents are stored.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_codes": ["TARGET_LANGUAGE", ...],
      "input_configs": [
        {
          "gcsSource": {
            "inputUri": "gs://INPUT_FILE_PATH_1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://INPUT_FILE_PATH_2"
          }
        },
        ...
      ],
      "output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument" | Select-Object -Expand Content

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
        "state": "RUNNING"
      }
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'us-central1';
    // const inputUri = 'path_to_your_files';
    // const outputUri = 'path_to_your_output_bucket';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v3beta1;
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    const documentInputConfig = {
      gcsSource: {
        inputUri: inputUri,
      },
    };
    
    async function batchTranslateDocument() {
      // Construct request
      const request = {
        parent: translationClient.locationPath(projectId, location),
        documentInputConfig: documentInputConfig,
        sourceLanguageCode: 'en-US',
        targetLanguageCodes: ['sr-Latn'],
        inputConfigs: [
          {
            gcsSource: {
              inputUri: inputUri,
            },
          },
        ],
        outputConfig: {
          gcsDestination: {
            outputUriPrefix: outputUri,
          },
        },
      };
    
      // Batch translate documents using a long-running operation.
      // You can wait for now, or get results later.
      const [operation] = await translationClient.batchTranslateDocument(request);
    
      // Wait for operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Total Pages: ${response.totalPages}`);
    }
    
    batchTranslateDocument();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3beta1 as translate
    
    
    def batch_translate_document(
        input_uri: str,
        output_uri: str,
        project_id: str,
        timeout: int = 180,
    ) -> translate.BatchTranslateDocumentResponse:
        """Batch translate documents.
    
        Args:
            input_uri: Google Cloud Storage location of the input document.
            output_uri: Google Cloud Storage location of the output document.
            project_id: The GCP project ID.
            timeout: The timeout for this request.
    
        Returns:
            Translated document response
        """
        client = translate.TranslationServiceClient()
    
        # The ``global`` location is not supported for batch translation
        location = "us-central1"
    
        # Google Cloud Storage location for the source input. This can be a single file
        # (for example, ``gs://translation-test/input.docx``) or a wildcard
        # (for example, ``gs://translation-test/*``).
        # Supported file types: https://cloud.google.com/translate/docs/supported-formats
        gcs_source = {"input_uri": input_uri}
    
        batch_document_input_configs = {
            "gcs_source": gcs_source,
        }
        gcs_destination = {"output_uri_prefix": output_uri}
        batch_document_output_config = {"gcs_destination": gcs_destination}
        parent = f"projects/{project_id}/locations/{location}"
    
        # Supported language codes: https://cloud.google.com/translate/docs/language
        operation = client.batch_translate_document(
            request={
                "parent": parent,
                "source_language_code": "en-US",
                "target_language_codes": ["fr-FR"],
                "input_configs": [batch_document_input_configs],
                "output_config": batch_document_output_config,
            }
        )
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout)
    
        print(f"Total Pages: {response.total_pages}")
    
        return response
    
    

### Translate and convert a native PDF file

The following example translates and converts a native PDF file to a DOCX file. You can specify multiple inputs of various file types; they don't all have to be native PDF files. However, scanned PDF files cannot be included when including a conversion; the request is rejected and no translations are done. Only native PDF files are translated and converted to DOCX files. For example, if you include PPTX files, they are translated and returned as PPTX files.

If you regularly translate a mix of scanned and native PDF files, we recommend that you organize them into separate Cloud Storage buckets. That way, when you request a batch translation and conversion, you can easily exclude the bucket that contains scanned PDF files instead of having to exclude individual files.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: Region where you want to run this operation. For example, `us-central1`.
  * SOURCE_LANGUAGE: The language code of the input documents. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language or languages to translate the input documents to. Use the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * INPUT_FILE_PATH: The Cloud Storage location and file name of one or more native PDF files.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where all output documents are stored.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_codes": ["TARGET_LANGUAGE", ...],
      "input_configs": [
        {
          "gcsSource": {
            "inputUri": "gs://INPUT_FILE_PATH_1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://INPUT_FILE_PATH_2"
          }
        },
        ...
      ],
      "output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      },
      **"format_conversions": {
        "application/pdf": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
      }**
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:batchTranslateDocument" | Select-Object -Expand Content

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
        "state": "RUNNING"
      }
    }
    

### Use an AutoML model or a glossary

Instead of the Google-managed model, you can use your own AutoML Translation models to translate documents. In addition to specifying a model, you can also include a glossary to handle domain-specific terminology. If you specify a model or a glossary, you must specify the source language. The following example uses an AutoML model and a glossary. You can specify up to 10 target languages with their own model and glossary.

If you specify a model for some target languages and not others, Document Translation uses the Google-managed model for the unspecified languages. Similarly, if you specify a glossary for some target languages, Document Translation doesn't use any glossary for the unspecified languages.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: Region where you want to run this operation, such as `us-central1`. The location must match the region where your model, glossary, or both are located.
  * SOURCE_LANGUAGE: The language code of the input documents. Set to one of the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * TARGET_LANGUAGE: The target language or languages to translate the input documents to. Use the language codes listed in [Language support](https://docs.cloud.google.com/translate/docs/languages).
  * INPUT_FILE_PATH: The Cloud Storage location and file name of one or more input documents.
  * OUTPUT_FILE_PREFIX: The Cloud Storage location where all output documents are stored.
  * MODEL_PROJECT_ID: The project ID where the model is located.
  * MODEL_LOCATION: The region where the model is located.
  * MODEL_ID: The ID of the model to use.
  * GLOSSARY_PROJECT_ID: The project ID where the glossary is located.
  * GLOSSARY_LOCATION: The region where the glossary is located.
  * GLOSSARY_ID: The ID of the glossary to use.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument

Request JSON body: 
    
    
    {
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_codes": "[TARGET_LANGUAGE, ...]",
      "input_configs": [
        {
          "gcsSource": {
            "inputUri": "gs://INPUT_FILE_PATH"
          }
        }
      ],
      "output_config": {
        "gcsDestination": {
          "outputUriPrefix": "gs://OUTPUT_FILE_PREFIX"
        }
      },
      "models": {
        "TARGET_LANGUAGE": "projects/MODEL_PROJECT_ID/locations/MODEL_LOCATION/models/MODEL_ID",
        ...
      },
      "glossaries": {
        "TARGET_LANGUAGE": {
          "glossary": "projects/GLOSSARY_PROJECT_ID/locations/MODEL_LOCATION/glossaries/GLOSSARY_ID"
        },
        ...
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION:translateDocument" | Select-Object -Expand Content

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
        "state": "RUNNING"
      }
    }
    

## Overlapping text

In some cases, **native PDF translations** might include translated text overlaid on the source text. This issue is referred to as shadow text.

In certain cases, you can remove shadow text by enabling the [`enableShadowRemovalNativePdf`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#request-body) option. If you enable this option, the response latency increases and, for online document translations, the page limit is reduced to 20. You can only know if your document requires shadow text removal only after it has been translated.

In other cases, if the `enableShadowRemovalNativePdf` option doesn't work, convert the PDF to an image and then translate it. Typically, these cases include multiple layers text, like when selectable text is on top of a background image that also includes text. Converting the PDF to an image enables Cloud Translation to process the document as a scanned PDF. To do the conversion, you can use Chrome (print as image) or other third-party tools.

## Text orientation

For **scanned PDF translations** , the source text must be oriented horizontally. If, for example, a scanned document includes text that is sloping up or down, Cloud Translation might not correctly parse all the text, which results in incorrect or incomplete translations.

If your documents aren't consistently oriented, you can have Cloud Translation orient them for you. In your translation request, enable the [`enableRotationCorrection`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#request-body) option so that text is correctly oriented before translation.

## What's next

  * Document Translation is priced per page. For more information, see [Pricing](https://cloud.google.com/translate/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
