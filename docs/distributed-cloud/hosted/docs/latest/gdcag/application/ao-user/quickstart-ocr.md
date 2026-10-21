---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-ocr/
title: Detect text in images \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:18:06.050327+00:00
---

# Detect text in images  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Detect text in images Stay organized with collections  Save and categorize content based on your preferences. 

The Optical Character Recognition (OCR) service of Vertex AI on Google Distributed Cloud (GDC) air-gapped detects text in images using the `BatchAnnotateImages` API method. The service supports JPEG and PNG files for images.

This page shows you how to detect image text using the OCR API on Distributed Cloud.

## Before you begin

To detect text in images, contact your Project IAM Admin to request the **AI OCR Developer** (`ai-ocr-developer`) role in your project namespace.

For more information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

Before you can start using the OCR API, you must have a project with the OCR API enabled and have the appropriate credentials. You can also install client libraries to help you make calls to the API. For more information, see [Set up a character recognition project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-ocr).

## Detect text from JPEG and PNG files

The `BatchAnnotateImages` method detects text from a batch of JPEG or PNG files. You send the file from which you want to detect text directly as content in the API request. The system returns the resulting detected text in JSON format in the API response.

You must specify values for the fields in the JSON body of your API request. The following table contains a description of the request body fields you must provide when you use the `BatchAnnotateImages` API method for your text detection requests:

**Request body fields** | **Field description**  
---|---  
`content` |  The images with text to detect. You provide the Base64 representation (ASCII string) of your binary image data.  
**Note:** You can only process images that are stored locally in your Distributed Cloud environment.  
`type` |  The type of text detection you need from the image.  
  
Specify one of the two annotation features:  


  * `TEXT_DETECTION` detects and extracts text from any image. The JSON response includes the extracted string, individual words, and their bounding boxes.
  * `DOCUMENT_TEXT_DETECTION` also extracts text from an image, but the service optimizes the response for dense text and documents. The JSON includes page, block, paragraph, word, and break information.

For more information about these annotation features, see [Optical character recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr#ocr-features).   
`language_hints` |  Optional. List of languages to use for the text detection.  
  
The system interprets an empty value for this field as automatic language detection.  
  
You don't need to set the `language_hints` field for languages based on the Latin alphabet.  
  
If you know the language of the text in the image, setting a hint improves results. **How do language hints work?** The `language_hints` format uses the following `BCP 47` language tag formatting guidelines:  `language` ["-" `script`] ["-" `region`] *("-" `variant`) *("-" `extension`) ["-" `privateuse`]. For example, the language hint "`en`-`t`-`i0`-`handwrit`" specifies English language (`en`), transform extension singleton (`t`), input method engine transform extension code (`i0`), and handwriting transform code (`handwrit`). This roughly says the language is "English transformed from handwriting." You don't need to specify a script code because the "`en`" language implies `Latn`.  For a list of supported languages, see [ Supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr-supported-langs).  
  
For information about the complete JSON representation, see [`AnnotateImageRequest`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageRequest).

### Make an API request

Make a request to the OCR pre-trained API using the REST API method. Otherwise, interact with the OCR pre-trained API from a Python script to detect text from JPEG or PNG files.

**Note:** The `BatchAnnotateImages` API method only supports a single request per batch call.

The following examples show how to detect text in an image using OCR:

###  REST 

Follow these steps to detect text in images using the REST API method:

  1. Save the following `request.json` file for your request body:
         
         cat <<- EOF > request.json
         {
           "requests": [
             {
               "image": {
                 "content": BASE64_ENCODED_IMAGE
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
               }
             }
           ]
         }
         EOF
         

Replace the following:

     * `BASE64_ENCODED_IMAGE`: the Base64 representation (ASCII string) of your binary image data. This string begins with characters that look similar to `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`.
     * `FEATURE_TYPE`: the type of text detection you need from the image. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `LANGUAGE_HINT`: the BCP 47 language tags to use as language hints for text detection, such as `en-t-i0-handwrit`. This field is optional and the system interprets an empty value as automatic language detection.
  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:

### curl
         
         curl -X POST \
           -H "Authorization: Bearer TOKEN" \
           -H "x-goog-user-project: projects/PROJECT_ID" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           https://ENDPOINT/v1/images:annotate
         

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
      -Uri "ENDPOINT/v1/images:annotate" | Select-Object -Expand Content
    

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).




### Python

Follow these steps to use the OCR service from a Python script to detect text in an image:

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
           image = {"content": "BASE64_ENCODED_IMAGE"}
           features = [{"type_": vision.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.FEATURE_TYPE}]
           # Each requests element corresponds to a single image. To annotate more
           # images, create a request element for each image and add it to
           # the array of requests
           req = {"image": image, "features": features}
         
           metadata = [("x-goog-user-project", "projects/PROJECT_ID")]
         
           resp = vc.annotate_image(req,metadata=metadata)
         
           print(resp)
         
         if __name__=="__main__":
           creds = main()
           vision_func(creds)
         

Replace the following:

     * `ENDPOINT`: the OCR endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `BASE64_ENCODED_IMAGE`: the Base64 representation (ASCII string) of your binary image data. This string begins with characters that look similar to `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`.
     * `FEATURE_TYPE`: the type of text detection you need from the image. Allowed values are `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`.
     * `PROJECT_ID`: your project ID.
  5. Save the Python script.

  6. Run the Python script to detect text in the image:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `vision.py`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
