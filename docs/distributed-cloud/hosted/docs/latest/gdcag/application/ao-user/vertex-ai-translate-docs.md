---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translate-docs/
title: Try translating formatted documents \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:24.013121+00:00
---

# Try translating formatted documents  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translate-docs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Try translating formatted documents Stay organized with collections  Save and categorize content based on your preferences. 

[Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation) and [Optical Character Recognition (OCR)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr) services combine to provide a document processing feature called Document Translate.

Document Translate directly translates formatted documents such as PDF files. Compared to plain [text translations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation), the feature preserves the original formatting and layout in your translated documents, helping you retain much of the original context, like paragraph breaks.

Document Translate supports document translations inline, from storage buckets, and in batch.

This page guides you through an interactive experience using the document processing feature on Google Distributed Cloud (GDC) air-gapped to translate documents while preserving their format.

## Supported formats

Document Translate supports the following input file types and their associated output file types:

**Inputs** | **Document MIME type** | **Output**  
---|---|---  
PDF | `application/pdf` | PDF, DOCX  
DOC | `application/msword` | DOC, DOCX  
DOCX | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | DOCX  
PPT | `application/vnd.ms-powerpoint` | PPT, PPTX  
PPTX | `application/vnd.openxmlformats-officedocument.presentationml.presentation` | PPTX  
XLS | `application/vnd.ms-excel` | XLS, XLSX  
XLSX | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` | XLSX  
  
## Original and scanned PDF document translations

Document Translate supports original and scanned PDF files, including translations to or from right-to-left languages. Also, Document Translate preserves hyperlinks, font size, and font color from files.

## Before you begin

Before you can start using the document processing feature, you must have a project named `dt-project`. The custom resource of the project must look like in the following example:
    
    
    apiVersion: resourcemanager.gdc.goog/v1
    kind: Project
    metadata:
      labels:
        atat.config.google.com/clin-number: CLIN_NUMBER
        atat.config.google.com/task-order-number: TASK_ORDER_NUMBER
      name: dt-project
      namespace: platform
    

Furthermore, you must [enable both the Vertex AI Translation and OCR pre-trained APIs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis) and have the appropriate credentials. Consider [installing the Vertex AI Translation and OCR client libraries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries) to facilitate API calls. For more information about prerequisites, see [Set up a translation project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-translation).

## Translate a document from a storage bucket

To translate a document that is stored in a bucket, you use the Vertex AI Translation API.

This section describes how to translate a document from a bucket and store the result to another output bucket path. The response also returns a byte stream. You can specify the MIME type; if you don't, Document Translate determines it by using the input file's extension.

Document Translate supports language auto-detection for documents stored in buckets. If you don't specify a source language code, Document Translate detects the language for you. The detected language is included in the output in the `detectedLanguageCode` field.

Follow these steps to translate a document from a storage bucket:

  1. [Configure the gdcloud CLI for object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/install-configure-storage-cli).
  2. [Create a storage bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/create-storage-buckets) in the `dt-project` namespace. Use a `Standard` storage class.

You can create the storage bucket by deploying a `Bucket` resource in the `dt-project` namespace:
         
         apiVersion: object.gdc.goog/v1
           kind: Bucket
           metadata:
             name: dt-bucket
             namespace: dt-project
           spec:
             description: bucket for document vision service
             storageClass: Standard
             bucketPolicy:
               lockingPolicy:
                 defaultObjectRetentionDays: 90
         

  3. Grant `read` and `write` permissions on the bucket to the service account (`ai-translation-system-sa`) used by the Vertex AI Translation service.

You can follow these steps to create the role and role binding using custom resources:

     1. Create the role by deploying a `Role` resource in the `dt-project` namespace:
            
            apiVersion: rbac.authorization.k8s.io/v1
              kind: Role
              metadata:
                name: dvs-reader-writer
                namespace: dt-project
              rules:
                -
                  apiGroups:
                    - object.gdc.goog
                  resources:
                    - buckets
                  verbs:
                    - read-object
                    - write-object
            

     2. Create the role binding by deploying a `RoleBinding` resource in the `dt-project` namespace:
            
            apiVersion: rbac.authorization.k8s.io/v1
              kind: RoleBinding
              metadata:
                name: dvs-reader-writer-rolebinding
                namespace: dt-project
              roleRef:
                apiGroup: rbac.authorization.k8s.io
                kind: Role
                name: dvs-reader-writer
              subjects:
                -
                  kind: ServiceAccount
                  name: ai-translation-system-sa
                  namespace: g-vai-translation-sie
            

  4. Upload your document to the storage bucket you created. For more information, see [Upload and download storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects#upload_objects_to_storage_buckets).

  5. Make a request to the Vertex AI Translation pre-trained API:

###  curl 

Follow these steps to make a `curl` request:

     1. Save the following `request.json` file:
            
            cat <<- EOF > request.json
            {
              "parent": "projects/PROJECT_ID/locations/PROJECT_ID",
              "source_language_code": "SOURCE_LANGUAGE",
              "target_language_code": "TARGET_LANGUAGE",
              "document_input_config": {
                "mime_type": "application/pdf",
                "s3_source": {
                  "input_uri": "s3://INPUT_FILE_PATH"
                }
              },
              "document_output_config": {
                "mime_type": "application/pdf"
              },
              "enable_rotation_correction": "true"
            }
            EOF
            

Replace the following:

        * `PROJECT_ID`: your project ID.
        * `SOURCE_LANGUAGE`: the language in which your document is written. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
        * `TARGET_LANGUAGE`: the language or languages into which you want to translate your document. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
        * `INPUT_FILE_PATH`: the path of your document file in the storage bucket.

Modify the `mime_type` value according to your document.

     2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

     3. Make the request:
            
            curl -vv --data-binary @- -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT:443/v3/projects/PROJECT_ID/locations/PROJECT_ID:translateDocument < request.json
            

Replace the following:

        * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
        * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
        * `PROJECT_ID`: your project ID.




## Translate a document inline

This section describes how to send a document inline as part of the API request. You must include the MIME type for inline document translations.

Document Translate supports language auto-detection for inline text translations. If you don't specify a source language code, Document Translate detects the language for you. The detected language is included in the output in the `detectedLanguageCode` field.

Make a request to the Vertex AI Translation pre-trained API:

###  curl 

Follow these steps to make a `curl` request:

  1. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  2. Make the request:



    
    
    echo '{"parent": "projects/PROJECT_ID/locations/PROJECT_ID","source_language_code": "SOURCE_LANGUAGE", "target_language_code": "TARGET_LANGUAGE", "document_input_config": { "mime_type": "application/pdf", "content": "'$(base64 -w 0 INPUT_FILE_PATH)'" }, "document_output_config": { "mime_type": "application/pdf" }, "enable_rotation_correction": "true"}' | curl --data-binary @- -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID/locations/PROJECT_ID:translateDocument
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `SOURCE_LANGUAGE`: the language in which your document is written. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
  * `TARGET_LANGUAGE`: the language or languages into which you want to translate your document. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
  * `INPUT_FILE_PATH`: the path of your document file locally.
  * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
  * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status)



## Translate documents in batch

Batch translation lets you translate multiple files into multiple languages in a single request. For each request, you can send up to 100 files with a total content size of up to 1 GB or 100 million Unicode codepoints, whichever limit is hit first. You can specify a particular translation model for each language.

For more information, see [`batchTranslateDocument`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument).

### Translate multiple documents

The following example includes multiple input configurations. Each input configuration is a pointer to a file in a storage bucket.

Make a request to the Vertex AI Translation pre-trained API:

###  curl 

Follow these steps to make a `curl` request:

  1. Save the following request body in a file named `request.json`:
         
         {
           "source_language_code": "SOURCE_LANGUAGE",
           "target_language_codes": ["TARGET_LANGUAGE", ...],
           "input_configs": [
             {
               "s3_source": {
                 "input_uri": "s3://INPUT_FILE_PATH_1"
               }
             },
             {
               "s3_source": {
                 "input_uri": "s3://INPUT_FILE_PATH_2"
               }
             },
             ...
           ],
           "output_config": {
             "s3_destination": {
               "output_uri_prefix": "s3://OUTPUT_FILE_PREFIX"
             }
           }
         }
         

Replace the following:

     * `SOURCE_LANGUAGE`: the language code of the input documents. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the target language or languages to translate the input documents to. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `INPUT_FILE_PATH`: the storage bucket location and filename of one or more input documents.
     * `OUTPUT_FILE_PREFIX`: the storage bucket location where all output documents are stored.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           "https://ENDPOINT:443/v3/projects/PROJECT_ID/locations/PROJECT_ID:batchTranslateDocument"
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.



The response contains the ID for a long-running operation:
    
    
    {
    "name": "projects/PROJECT_ID/operations/OPERATION_ID",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
      "state": "RUNNING"
    }
    }
    

### Translate and convert an original PDF file

The following example translates and converts an original PDF file to a DOCX file. You can specify multiple inputs of various file types; they don't all have to be original PDF files. However, scanned PDF files cannot be included when including a conversion; the request is rejected and no translations are done. Only original PDF files are translated and converted to DOCX files. For example, if you include PPTX files, they are translated and returned as PPTX files.

If you regularly translate a mix of scanned and original PDF files, we recommend that you organize them into separate buckets. That way, when you request a batch translation and conversion, you can exclude the bucket that contains scanned PDF files instead of having to exclude individual files.

Make a request to the Vertex AI Translation pre-trained API:

###  curl 

Follow these steps to make a `curl` request:

  1. Save the following request body in a file named `request.json`:
         
         {
           "source_language_code": "SOURCE_LANGUAGE",
           "target_language_codes": ["TARGET_LANGUAGE", ...],
           "input_configs": [
             {
               "s3_source": {
                 "input_uri": "s3://INPUT_FILE_PATH_1"
               }
             },
             {
               "s3_source": {
                 "input_uri": "s3://INPUT_FILE_PATH_2"
               }
             },
             ...
           ],
           "output_config": {
             "s3_destination": {
               "output_uri_prefix": "s3://OUTPUT_FILE_PREFIX"
             }
           },
           "format_conversions": {
             "application/pdf": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
           }
         }
         

Replace the following:

     * `SOURCE_LANGUAGE`: the language code of the input documents. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the target language or languages to translate the input documents to. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `INPUT_FILE_PATH`: the storage bucket location and filename of one or more input documents.
     * `OUTPUT_FILE_PREFIX`: the storage bucket location where all output documents are stored.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           "https://ENDPOINT:443/v3/projects/PROJECT_ID/locations/PROJECT_ID:batchTranslateDocument"
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.



The response contains the ID for a long-running operation:
    
    
    {
    "name": "projects/PROJECT_ID/operations/OPERATION_ID",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
      "state": "RUNNING"
    }
    }
    

### Use a glossary

You can include a [glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-glossary) to handle domain-specific terminology. If you specify a glossary, you must specify the source language. The following example uses a glossary. You can specify up to 10 target languages with their own glossary.

If you specify a glossary for some target languages, the system doesn't use any glossary for the unspecified languages.

Make a request to the Vertex AI Translation pre-trained API:

###  curl 

Follow these steps to make a `curl` request:

  1. Save the following request body in a file named `request.json`:
         
         {
           "source_language_code": "SOURCE_LANGUAGE",
           "target_language_codes": ["TARGET_LANGUAGE", ...],
           "input_configs": [
             {
               "s3_source": {
                 "input_uri": "s3://INPUT_FILE_PATH"
               }
             }
           ],
           "output_config": {
             "s3_destination": {
               "output_uri_prefix": "s3://OUTPUT_FILE_PREFIX"
             }
           },
           "glossaries": {
             "TARGET_LANGUAGE": {
               "glossary": "projects/GLOSSARY_PROJECT_ID"
             },
             ...
           }
         }
         

Replace the following:

     * `SOURCE_LANGUAGE`: the language code of the input documents. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the target language or languages to translate the input documents to. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `INPUT_FILE_PATH`: the storage bucket location and filename of one or more input documents.
     * `OUTPUT_FILE_PREFIX`: the storage bucket location where all output documents are stored.
     * `GLOSSARY_PROJECT_ID`: the project ID where the glossary is located.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           "https://ENDPOINT:443/v3/projects/PROJECT_ID/locations/PROJECT_ID:batchTranslateDocument"
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.



The response contains the ID for a long-running operation:
    
    
    {
    "name": "projects/PROJECT_ID/operations/OPERATION_ID",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateDocumentMetadata",
      "state": "RUNNING"
    }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
