---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-async-ocr/
title: Detect text in files \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:18.202608+00:00
---

# Detect text in files  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-async-ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Detect text in files Stay organized with collections  Save and categorize content based on your preferences. 

The Optical Character Recognition (OCR) service of Vertex AI on Google Distributed Cloud (GDC) air-gapped detects text in PDF and TIFF files using the following two API methods:

  * `BatchAnnotateFiles`: Detect text with inline requests.
  * `AsyncBatchAnnotateFiles`: Detect text with offline (asynchronous) requests.

**Note:** The `BatchAnnotateFiles` API method only supports a single request per batch call.

This page shows you how to detect text in files using the OCR API on Distributed Cloud.

## Before you begin

To detect text in files, contact your IAM Project Admin to request the **AI OCR Developer** (`ai-ocr-developer`) role in your project namespace.

For more information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

Before you can start using the OCR API, you must have a project with the OCR API enabled and have the appropriate credentials. You can also install client libraries to help you make calls to the API. For more information, see [Set up a character recognition project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-ocr).

## Detect text with inline requests

The `BatchAnnotateFiles` method detects text from a batch of PDF or TIFF files. You send the file from which you want to detect text directly as content in the API request. The system returns the resulting detected text in JSON format in the API response.

You must specify values for the fields in the JSON body of your API request. The following table contains a description of the request body fields you must provide when you use the `BatchAnnotateFiles` API method for your text detection requests:

**Request body fields** | **Field description**  
---|---  
`content` |  The files with text to detect. You provide the Base64 representation (ASCII string) of your binary file content.  
**Note:** You can only process files that are stored locally in your Distributed Cloud environment.  
`mime_type` | The source file type. You must set it to one of the following values:  


  * `application/pdf` for PDF files
  * `image/tiff` for TIFF files

  
`type` |  The type of text detection you need from the file.  
  
Specify one of the two annotation features:  


  * `TEXT_DETECTION` detects and extracts text from any file. The JSON response includes the extracted string, individual words, and their bounding boxes.
  * `DOCUMENT_TEXT_DETECTION` also extracts text from a file, but the service optimizes the response for dense text and documents. The JSON includes page, block, paragraph, word, and break information.

For more information about these annotation features, see [Optical character recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr#ocr-features).   
`language_hints` |  Optional. List of languages to use for the text detection.  
  
The system interprets an empty value for this field as automatic language detection.  
  
You don't need to set the `language_hints` field for languages based on the Latin alphabet.  
  
If you know the language of the text in the file, setting a hint improves results. **How do language hints work?** The `language_hints` format uses the following `BCP 47` language tag formatting guidelines:  `language` ["-" `script`] ["-" `region`] *("-" `variant`) *("-" `extension`) ["-" `privateuse`]. For example, the language hint "`en`-`t`-`i0`-`handwrit`" specifies English language (`en`), transform extension singleton (`t`), input method engine transform extension code (`i0`), and handwriting transform code (`handwrit`). This roughly says the language is "English transformed from handwriting." You don't need to specify a script code because the "`en`" language implies `Latn`.  For a list of supported languages, see [ Supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr-supported-langs).  
`pages` | Optional. The number of pages from the file to process for text detection.  
  
The maximum number of pages that you can specify is five. If you don't specify the number of pages, the service processes the first five pages of the file.  
  
For information about the complete JSON representation, see [`AnnotateFileRequest`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateFileRequest).

### Make an inline API request

Make a request to the OCR pre-trained API using the REST API method. Otherwise, interact with the OCR pre-trained API from a Python script to detect text from PDF or TIFF files.

**Note:** The `BatchAnnotateFiles` API method only supports a single request per batch call.

The following examples show how to detect text in a file using OCR:

###  REST 

Follow these steps to detect text in files using the REST API method:

  1. Save the following `request.json` file for your request body:
         
         cat <<- EOF > request.json
         {
           "requests": [
             {
               "input_config": {
                 "content": BASE64_ENCODED_FILE,
                 "mime_type": "application/pdf"
               },
               "features": [
                 {
                   "type": "FEATURE_TYPE"
                 }
               ],
               "image_context": {
                 "language_hints": [
                   "LANGUAGE_HINT_1",
                   "LANGUAGE_HINT_2",
                   ...
                 ]
               },
               "pages": []
             }
           ]
         }
         EOF
         

Replace the following:

     * `BASE64_ENCODED_FILE`: the Base64 representation (ASCII string) of your binary file content. This string begins with characters that look similar to `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`.
     * `FEATURE_TYPE`: the type of text detection you need from the file. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `LANGUAGE_HINT`: the BCP 47 language tags to use as language hints for text detection, such as `en-t-i0-handwrit`. This field is optional and the system interprets an empty value as automatic language detection.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:

### curl
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "x-goog-user-project: projects/PROJECT_ID" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           https://ENDPOINT/v1/files:annotate
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `PROJECT_ID`: your project ID.
     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

### PowerShell
    
    $headers = @{
      "Authorization" = "Bearer TOKEN"
      "x-goog-user-project" = "projects/PROJECT_ID"
    }
    
    Invoke-WebRequest
      -Method POST
      -Headers $headers
      -ContentType: "application/json; charset=utf-8"
      -InFile request.json
      -Uri "ENDPOINT/v1/files:annotate" | Select-Object -Expand Content
    

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).




### Python

Follow these steps to use the OCR service from a Python script to detect text in a file:

  1. [Install the latest version of the OCR client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

  2. [Set the required environment variables on a Python script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-ocr#set-env-var).

  3. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  4. Add the following code to the Python script you created:
         
         from google.cloud import vision
         import google.auth
         from google.auth.transport import requests
         from google.api_core.client_options import ClientOptions
         
         audience = "https://ENDPOINT:443"
         api_endpoint="ENDPOINT:443"
         
         def vision_client(creds):
           opts = ClientOptions(api_endpoint=api_endpoint)
           return vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)(credentials=creds, client_options=opts)
         
         def main():
           creds = None
           try:
             creds, project_id = google.auth.default()
             creds = creds.with_gdch_audience(audience)
             req = requests.Request()
             creds.refresh(req)
             print("Got token: ")
             print(creds.token)
           except Exception as e:
             print("Caught exception" + str(e))
             raise e
           return creds
         
         def vision_func(creds):
           vc = vision_client(creds)
           input_config = {"content": "BASE64_ENCODED_FILE"}
           features = [{"type_": vision.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.FEATURE_TYPE}]
           # Each requests element corresponds to a single file. To annotate more
           # files, create a request element for each file and add it to
           # the array of requests
           req = {"input_config": input_config, "features": features}
         
           metadata = [("x-goog-user-project", "projects/PROJECT_ID")]
         
           resp = vc.annotate_file(req,metadata=metadata)
         
           print(resp)
         
         if __name__=="__main__":
           creds = main()
           vision_func(creds)
         

Replace the following:

     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `BASE64_ENCODED_FILE`: the Base64 representation (ASCII string) of your file content. This string begins with characters that look similar to `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`.
     * `FEATURE_TYPE`: the type of text detection you need from the file. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `PROJECT_ID`: your project ID.
  5. Save the Python script.

  6. Run the Python script to detect text in the file:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `vision.py`.




## Detect text with offline requests

The `AsyncBatchAnnotateFiles` method detects text from a batch of PDF or TIFF files by performing an offline (asynchronous) request. The files might contain multiple pages and multiple images per page. The source files must be in a storage bucket of your Distributed Cloud project. The system saves the resulting detected text in JSON format to a storage bucket.

The OCR service initiates the offline processing and returns the ID of the long-running process that performs text detection on the file. You can use the returned ID to track the status of the offline processing. If there are too many ongoing operations, the offline processing might not start immediately.

You must specify values for the fields in the JSON body of your API request. The following table contains a description of the request body fields you must provide when you use the `AsyncBatchAnnotateFiles` API method for your text detection requests:

**Request body fields** | **Field description**  
---|---  
`gcs_source.uri` | The URI path to a valid source file (PDF or TIFF) in a storage bucket of your Distributed Cloud project.  
  
This file contains the text that you want to detect.  
  
The requesting user or service account must at least have read privileges to the file.  
`mime_type` | The source file type. You must set it to one of the following values:  


  * `application/pdf` for PDF files
  * `image/tiff` for TIFF files

  
`type` |  The type of text detection you need from the file.  
  
Specify one of the two annotation features:  


  * `TEXT_DETECTION` detects and extracts text from any file. The JSON response includes the extracted string, individual words, and their bounding boxes.
  * `DOCUMENT_TEXT_DETECTION` also extracts text from a file, but the service optimizes the response for dense text and documents. The JSON includes page, block, paragraph, word, and break information.

For more information about these annotation features, see [Optical character recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr#ocr-features).   
`gcs_destination.uri` | The URI path to a storage bucket of your Distributed Cloud project to save output files to.  
  
This location is where you want to store the detection results.  
  
The requesting user or service account must have write permission to the bucket.  
  
### Store the source file in a storage bucket

Before sending a request, you must ensure the OCR service account has read permissions to your input bucket and write permissions to your output bucket.

The input and output buckets can be different and in different project namespaces. We recommend using the same input and output buckets to prevent errors, such as storing the results in erroneous buckets.

Follow these steps to store the file from which you want to detect text in a storage bucket:

  1. [Configure the gdcloud CLI for object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/install-configure-storage-cli).
  2. [Create a storage bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/create-storage-buckets) in your project namespace.Use a `Standard` storage class.

You can create the storage bucket by deploying a `Bucket` resource in the project namespace:
         
         apiVersion: object.gdc.goog/v1
         kind: Bucket
         metadata:
           name: ocr-async-bucket
           namespace: PROJECT_NAMESPACE
         spec:
           description: bucket for async ocr
           storageClass: Standard
           bucketPolicy:
             lockingPolicy:
               defaultObjectRetentionDays: 90
         

  3. Grant `read` and `write` permissions on the bucket to the service account (`g-vai-ocr-sie-sa`) used by the OCR service.

You can follow these steps to create the role and role binding using custom resources:

     1. Create the role by deploying a `Role` resource in the project namespace:
            
            apiVersion: rbac.authorization.k8s.io/v1
              kind: Role
              metadata:
                name: ocr-async-reader-writer
                namespace: PROJECT_NAMESPACE
              rules:
                -
                  apiGroups:
                    - object.gdc.goog
                  resources:
                    - buckets
                  verbs:
                    - read-object
                    - write-object
            

     2. Create the role binding by deploying a `RoleBinding` resource in the project namespace:
            
            apiVersion: rbac.authorization.k8s.io/v1
              kind: RoleBinding
            
              metadata:
                name: ocr-async-reader-writer-rolebinding
                namespace: PROJECT_NAMESPACE
              roleRef:
                apiGroup: rbac.authorization.k8s.io
                kind: Role
                name: ocr-async-reader-writer
              subjects:
                -
                  kind: ServiceAccount
                  name: g-vai-ocr-sie-sa
                  namespace: g-vai-ocr-sie
            

  4. Upload your file to the storage bucket you created. For more information, see [Upload and download storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects#upload_objects_to_storage_buckets).




### Make an offline API request

Make a request to the OCR pre-trained API using the REST API method. Otherwise, interact with the OCR pre-trained API from a Python script to detect text from PDF or TIFF files.

The following examples show how to detect text in a file using OCR:

###  REST 

Follow these steps to detect text in files using the REST API method:

  1. Save the following `request.json` file for your request body:
         
         cat <<- EOF > request.json
         {
           "parent": PROJECT_ID,
           "requests":[
             {
               "input_config": {
                 "gcs_source": {
                   "uri": "SOURCE_FILE"
                 },
                 "mime_type": "application/pdf"
               },
               "features": [
                 {
                   "type": "FEATURE_TYPE"
                 }
               ],
               "output_config": {
                 "gcs_destination": {
                   "uri": "DESTINATION_BUCKET"
                 }
               }
             }
           ]
         }
         EOF
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `SOURCE_FILE`: the URI path to a valid source file (PDF or TIFF) in a storage bucket of your Distributed Cloud project.
     * `FEATURE_TYPE`: the type of text detection you need from the file. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `DESTINATION_BUCKET`: the URI path to a storage bucket of your Distributed Cloud project to save output files to.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:

### curl
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "x-goog-user-project: projects/PROJECT_ID" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           https://ENDPOINT/v1/files:asyncBatchAnnotate
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `PROJECT_ID`: your project ID.
     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

### PowerShell
    
    $headers = @{
      "Authorization" = "Bearer TOKEN"
      "x-goog-user-project" = "projects/PROJECT_ID"
    }
    
    Invoke-WebRequest
      -Method POST
      -Headers $headers
      -ContentType: "application/json; charset=utf-8"
      -InFile request.json
      -Uri "ENDPOINT/v1/files:asyncBatchAnnotate" | Select-Object -Expand Content
    

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).




### Python

Follow these steps to use the OCR service from a Python script to detect text in a file:

  1. [Install the latest version of the OCR client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

  2. [Set the required environment variables on a Python script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-ocr#set-env-var).

  3. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  4. Add the following code to the Python script you created:
         
         from google.cloud import vision
         import google.auth
         from google.auth.transport import requests
         from google.api_core.client_options import ClientOptions
         
         audience = "https://ENDPOINT:443"
         api_endpoint="ENDPOINT:443"
         
         def vision_func_async(creds):
           vc = vision_client(creds)
           features = [{"type_": vision.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.FEATURE_TYPE}]
           input_config = {"gcs_source":{"uri":SOURCE_FILE},"mime_type": "application/pdf"}
           output_config = {"gcs_destination": {"uri": DESTINATION_BUKET}}
           req = {"input_config": input_config, "output_config": output_config, "features":features}
           reqs = {"requests":[req],"parent":PROJECT_ID}
         
           metadata = [("x-goog-user-project", "projects/PROJECT_ID")]
         
           operation = vc.async_batch_annotate_files(request=reqs, metadata=metadata)
           lro = operation.operation
           resp = operation.result()
         
         def main():
           creds = None
           try:
             creds, project_id = google.auth.default()
             creds = creds.with_gdch_audience(audience)
             req = requests.Request()
             creds.refresh(req)
             print("Got token: ")
             print(creds.token)
           except Exception as e:
             print("Caught exception" + str(e))
             raise e
           return creds
         
         if __name__=="__main__":
           creds = main()
           vision_func_async(creds)
         

Replace the following:

     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `FEATURE_TYPE`: the type of text detection you need from the file. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `SOURCE_FILE`: the URI path to a valid source file (PDF or TIFF) in a storage bucket of your Distributed Cloud project.
     * `DESTINATION_BUCKET`: the URI path to a storage bucket of your Distributed Cloud project to save output files to.
     * `PROJECT_ID`: your project ID.
  5. Save the Python script.

  6. Run the Python script to detect text in the file:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `vision.py`.




You can use the operation name that the `AsyncBatchAnnotateFiles` method returned to check the status of the operation.

### Get the status of the operation

The `get` method returns the latest state of a long-running operation such as the offline request for text detection. Use this method to check the operation status as in the following example:
    
    
    curl -X GET "http://ENDPOINT/v1/OPERATION_NAME"
    

Replace `OPERATION_NAME` with the operation name that the `AsyncBatchAnnotateFiles` method returned when you made the offline request.

### List operations

The `list` method returns a list of the operations that match a specified filter in the request. The method can return operations from a specific project. To call the list method, specify your project ID and the OCR endpoint as in the following example:
    
    
    curl -X GET "http://ENDPOINT/v1/PROJECT_ID?page_size=10"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
