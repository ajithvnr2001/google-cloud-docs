---
url: https://docs.cloud.google.com/gemini/enterprise/docs/upload-content/
title: Upload content to the assistant \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:44.516346+00:00
---

# Upload content to the assistant  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/upload-content/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Upload content to the assistant Stay organized with collections  Save and categorize content based on your preferences. 

You can upload files to the assistant using the API. These files are available when you [chat with the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat). For information about uploading files within the assistant, see [Upload and chat about files](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#upload_and_chat_about_files).

To upload content to the assistant using the API, run the following curl command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID:addContextFile" \
    -d '{
          "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID",
          "fileName": "FILE_NAME",
          "mimeType": "MIME_TYPE",
          "fileContents": "BASE64_ENCODED_FILE",
        }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `APP_ID`: the ID of the app.
  * `SESSION_ID`: the ID of the session. You can obtain this ID from the response of creating a session, as shown in [Store session information and get responses](https://docs.cloud.google.com/gemini/enterprise/docs/answer#store-session).
  * `FILE_NAME`: the name of the file.
  * `MIME_TYPE`: the MIME type of the file.
  * `BASE64_ENCODED_FILE`: the base64 representation (ASCII string) of your data. This string should look similar to the following string: `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`



Example command and response:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: 1234" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/1234/locations/global/collections/default_collection/engines/myapp/sessions/16002628354770206943:addContextFile" \
    -d '{
          "name": "projects/1234/locations/global/collections/default_collection/engines/myapp/sessions/16002628354770206943",
          "fileName": "Hello World.pdf",
          "mimeType": "application/pdf",
          "fileContents": JVBERi0xLjQKJdPr6eEKMSAwIG9iago8PC9UaXRsZSAoSGVsbG8gd29ybGQpCi9Qcm9kdWNlciAoU2tpYS9QREYgbTEzMCBHb29nbGUgRG9jcyBSZW5kZXJlcik+PgplbmRvYmoKMyAwIG9iago8PC..............KMDAwMDAxNDk0NCAwMDAwMCBuIAp0cmFpbGVyCjw8L1NpemUgMTIKL1Jvb3QgNyAwIFIKL0luZm8gMSAwIFI+PgpzdGFydHhyZWYKMTU0NjYKJSVFT0YK",
        }'
    ------------------
    {
      "session": "projects/1234/locations/global/collections/default_collection/engines/myapp/sessions/16002628354770206943",
      "fileId": "11157546467692423460",
      "tokenCount": "258"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
