---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api/
title: Use the API to import conversations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:08.005292+00:00
---

# Use the API to import conversations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Use the API to import conversations Stay organized with collections  Save and categorize content based on your preferences. 

Learn how you can import audio and transcript files with their metadata using the API. You can import a single file using the `UploadConversation` API, or you can bulk import all the files from a Cloud Storage bucket using the `IngestConversations` API.

The two request commands `UploadConversation` and `IngestConversations` support the following functions:

Request command | Number of files | Speech-to-Text | Redaction | Metadata ingestion | Automatic analysis  
---|---|---|---|---|---  
UploadConversation | 1 | ✔ | ✔ | ✔ | With analysis rules or the upload conversation analysis percentage in project [settings](/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings#analysisconfig)  
IngestConversations | All files in a bucket | ✔ | ✔ | ✔ | With analysis rules only  
  
## Prerequisites

  1. Enable the [Cloud Storage, Speech-to-Text, Sensitive Data Protection, and Customer Experience Insights APIs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) on the Google Cloud project that you use for Dialogflow.
  2. Save your conversation data (dual-channel audio and transcript files) in a Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) using the [standard storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard). 
     1. Follow the [Cloud storage quickstart](https://docs.cloud.google.com/storage/docs/quickstart-console) instructions to create a bucket.
     2. Set the [bucket location](https://docs.cloud.google.com/storage/docs/locations) to a location nearest to your location. 
     3. Note the following information you need when providing conversation data: 
        * Bucket name
        * Location ID, format: `us-west1`
        * Object path, format: `gs://<bucket>/<object>`
  3. Give the Speech-to-Text and Customer Experience Insights [service agents](https://docs.cloud.google.com/iam/docs/service-agents) access to the objects in your Cloud Storage bucket. See this [troubleshooting page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues) for help with service accounts.
  4. If you opt to import conversation metadata, ensure that metadata files are in their own bucket and the metadata filenames match their corresponding conversation filename.

For example, a conversation with the Cloud Storage URI `gs://transcript-bucket-name/conversation.mp3`, must have a corresponding metadata file such as `gs://metadata-bucket-name/conversation.json`.


**Note:** Unlike the `UploadConversation` API, the `IngestConversations` API does not support the import of transcripts together with audio or the linking of audio with transcripts. If you have both conversation audio and transcripts, make sure to save them in separate buckets.

## Conversation data

Conversation data consists of voice or chat transcripts and audio.

### Transcripts

Chat transcripts must be supplied in JSON-formatted files, where each file contains data for a single conversation. Your JSON-formatted text files include the [conversation data format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format).

Voice transcripts can be supplied in the conversation data format or as the returned [speech recognition result](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rpc/google.cloud.speech.v2#speechrecognitionresult) of a Speech-to-Text API transcription. The response is identical for synchronous and asynchronous recognition across all Speech-to-Text API versions.

### Audio

Customer Experience Insights uses Cloud Speech-to-Text [batch recognition](https://docs.cloud.google.com/speech-to-text/v2/docs/batch-recognize) to transcribe audio. CX Insights configures Speech-to-Text transcription settings with [Recognizer](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.Recognizer) resources. You can create a custom recognizer in the request, or if you don't provide a recognizer either in **Settings** or in the request, CX Insights creates a default `ccai-insights-recognizer` in your project.

The CX Insights recognizer transcribes English speech using the telephony model, and the default language is en-US. For a full list of Speech-to-Text support per region, language, model, and recognition feature, refer to the Speech-to-Text [language support docs](https://docs.cloud.google.com/speech-to-text/v2/docs/speech-to-text-supported-languages). 

**Note:** CX Insights requires the presence of word-time offsets, which are a type of Speech-to-Text [recognition feature](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rpc/google.cloud.speech.v2#recognitionfeatures).

Before your first audio import to CX Insights, assess whether you would like to:

  * Use a custom Speech-to-Text transcription configuration.
  * Analyze the (optionally) redacted conversations.



You can configure these actions to run by default in each `UploadConversation` or `IngestConversation` request by setting the proper fields in the project [Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings) resource. The speech and redaction settings can also be overridden per-request. If you don't specify any speech settings, CX Insights will use the default speech settings and won't redact the transcripts.

**Note:** The audio ingest operations will skip any JSON files in the Cloud Storage bucket that you provide.

### Redaction

Sensitive Data Protection does not redact transcripts unless you explicitly supply redaction configs in the project [Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings), the [UploadConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/upload#request-body), or in the [IngestConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/ingest#request-body). Sensitive Data Protection supports both [inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect) and [de-identification templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid) for redaction.

**Note:** To ensure that you don't import any personally identifiable information to CX Insights, you should sanitize your data yourself before you import it.

### Configure project settings

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.settings.update`



Redaction and speech can be configured for `UploadConversation` and `IngestConversations` requests by setting the corresponding project settings parameters. These configurations can also be set individually per request, which overrides the project settings. The `analysis_percentage` configured in an [analysis rule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/analysis-rule) overrides the `upload_conversation_analysis_percentage` configured through project [settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Settings).

Save the request body in a file called `request.json`, and execute the following command:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d @request.json \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/settings?updateMask=redaction_config,speech_config,analysis_config.upload_conversation_analysis_percentage"
    

**Note:** If you have other fields set, you can replace the updateMask with `redaction_config`, `speech_config`, or `analysis_config` `upload_conversation_analysis_percentage` to modify only those fields.

### Metadata

Import metadata in a single-file or as a bulk import.

#### Include metadata directly in the request

For single-file imports only, your [quality metadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#qualitymetadata) can be included directly in the curl command for `UploadConversationsRequest`.
    
    
    curl --request POST \
      'https://contactcenterinsights.googleapis.com/v1/projects/project-id/locations/location-id/conversations:upload' \
       --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
       --header 'Accept: application/json' \
       --header 'Content-Type: application/json' \
       --data '{
               "conversation":{
                "qualityMetadata":{
                   "agentInfo":[{"agentId":"agent-id","displayName":"agent-name"}]
                 },
                "dataSource":{"gcsSource":{"transcriptUri":"transcript-uri"}}}
              }'
      

#### Import metadata from Cloud Storage files

Supply conversation metadata files as JSON-formatted files. For bulk-imports, supply a bucket specified in the `gcs_source.metadata_bucket_uri` field of the `IngestConversationsRequest`. For single imports, supply an object path in the `data_source.metadata_uri` field of the `UploadConversationRequest`.

**Note:** The names of metadata files provided in a bucket for bulk import are expected to match their corresponding conversation object name, for example `gs://conversations/conversation.mp3` will be matched to `gs://metadata/conversation.json`.

CX Insights populates conversation quality metadata found in the file, but you can also create [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata).

For example, to specify a custom conversation ID for each conversation in your dataset, specify custom metadata on the conversation object within Cloud Storage. Set the key to `ccai_insights_conversation_id`. The value is your custom conversation ID. Custom conversation IDs can also be provided within the metadata file.

If you provide any custom metadata in the `custom_metadata_keys` field of an `IngestConversationsRequest`, CX Insights stores that custom metadata in the conversation [labels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#resource:-conversation). It supports up to 100 labels.

See the following example of a valid metadata file containing the [`Conversation.quality_metadata`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#resource:-conversation) resource, as well as a custom conversation ID and the conversation start time:
    
    
    {
      "customer_satisfaction_rating": 5,
      "agent_info": [
        {
          "agent_id": "123456",
          "display_name": "Agent Name",
          "team": "Agent Team",
          "disposition_code": "resolved"
        }
      ],
      "custom_key": "custom value"
      "conversation_id": "custom-conversation-id"
      "start_time": "%Y-%m-%d%ET%H:%M:%E*S%Ez"
    }
    

## Import a single audio file

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.upload`



The [`UploadConversation` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/upload) creates a long-running operation that transcribes and optionally redacts your conversations. An audio file will be transcribed if the conversation contains only an `audio_uri` in the `DataSource`. Otherwise, the provided `transcript_uri` will be read and used.

Request JSON body:
    
    
    { 
      "conversation": { 
        "data_source": { 
          "gcs_source": { "audio_uri": AUDIO_URI }
        }
      },
      "redaction_config": {
        "deidentify_template": DEIDENTIFY_TEMPLATE,
        "inspect_template": INSPECT_TEMPLATE
      },
      "speech_config": {
        "speech_recognizer": RECOGNIZER_NAME
      }
    }
    

Save the request body in a file called `request.json`, and execute the following command:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d @request.json \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations:upload"
    

## Bulk import

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.create`

**Note:** Conversations already ingested into CX Insights will be skipped in subsequent bulk import attempts. File contents are not scanned for duplication comparison.**Note:** CX Insights only allows one bulk import operation.

### REST

Refer to the [`conversations:ingest`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/ingest) API endpoint for complete details.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud Platform project ID.
  * GCS_BUCKET_URI: the Cloud Storage URI that points to the bucket containing the conversation transcripts. May contain a prefix. For example gs://BUCKET_NAME or gs://BUCKET_NAME/PREFIX. Wildcards are not supported. 
  * MEDIUM: set to either `PHONE_CALL` or `CHAT` depending on the data type. If unspecified the default value is `PHONE_CALL`.
  * AGENT_ID: Optional. Agent Id for the entire bucket.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:ingest

Request JSON body: 
    
    
    {
      "gcsSource":  {
        "bucketUri": "GCS_BUCKET_URI",
        "bucketObjectType": "AUDIO"
      },
      "transcriptObjectConfig": { "medium": "PHONE_CALL" },
      "conversationConfig": {
        "agentId": "AGENT_ID",
        "agentChannel": "AGENT_CHANNEL",
        "customerChannel": "CUSTOMER_CHANNEL"
      }
    }
    
    Or
    
    {
      "gcsSource":  {
        "bucketUri": "GCS_BUCKET_URI",
        "bucketObjectType": "TRANSCRIPT"
      },
      "transcriptObjectConfig": { "medium": "MEDIUM" },
      "conversationConfig": {"agentId": "AGENT_ID"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:ingest"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:ingest" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1main.IngestConversationsMetadata",
        "createTime": "...",
        "request": {
          "parent": "projects/PROJECT_ID/locations/us-central1",
          "gcsSource": {
            "bucketUri": "GCS_BUCKET_URI",
            "bucketObjectType": "BUCKET_OBJECT_TYPE"
          },
          "transcriptObjectConfig": {
            "medium": "MEDIUM"
          },
          "conversationConfig": {
            "agentId": "AGENT_ID"
          }
        }
      }
    }
    
    

## Poll the operation

Both the `UploadConversation` and `IngestConversation` requests return a long-running operation. Long-running methods are asynchronous, and the operation might not yet be completed when the method returns a response. You can poll the operation to check on its status. See the [long-running operations page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) for details and code samples.

## Speech-to-Text quotas

Customer Experience Insights uses two different Speech-to-Text APIs: `BatchRecognize` and `GetOperation`. Customer Experience Insights makes a `BatchRecognize`request to start the Speech-to-Text transcription and a `GetOperation` request to monitor whether or not the transcription is finished. To start `BatchRecognize` operations, a `BatchRecognize` request is made to use a per-minute, per-region quota. To monitor the operations, a `GetOperation` request is made to use a per-minute, per-region quota.

For a single `UploadConversation` call, Customer Experience Insights consumes one `BatchRecognize`, but possibly more `GetOperation` requests, depending on the duration of the task. For a bulk import, Customer Experience Insights consumes 100 requests of each type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
