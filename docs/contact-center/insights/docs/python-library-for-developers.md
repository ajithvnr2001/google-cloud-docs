---
url: https://docs.cloud.google.com/contact-center/insights/docs/python-library-for-developers/
title: Customer Experience Insights devkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:12:53.908312+00:00
---

# Customer Experience Insights devkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/python-library-for-developers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Customer Experience Insights devkit Stay organized with collections  Save and categorize content based on your preferences. 

The CX Insights devkit is a high-level API designed to extend the Google Python client for CX Insights. As a developer or someone maintaining code, you can use the CX Insights devkit to scale a wide range of tasks.

## Use cases

Actions you can perform include the following:

  * Ingest single conversations with metadata.
  * Ingest many conversations in bulk with metadata.
  * Transcribe mono audio files using Speech-to-Text (STT) V1.
  * Create recognizers using STT V2.
  * Set up BigQuery export.
  * Change CX Insights global settings.
  * Transform transcript data format from Genesys Cloud to CX Insights.
  * Transform transcript data format from AWS to CX Insights.



## Get started

To get started with the [devkit](https://github.com/GoogleCloudPlatform/conversational-insights-devkit), follow these steps for environment setup and authentication.

### Step 1: Set up a virtual environment

Before using the devkit, follow these steps to set up your Google Cloud credentials and install the necessary dependencies.

  1. Use the following code to authenticate your account with the Google Cloud CLI. 
         
         gcloud auth login
         gcloud auth application-default login
         

  2. Set your Google Cloud project with the following code. Replace project name with your actual Google Cloud project ID. 
         
         gcloud config set project 

  3. Create and activate a Python virtual environment with the following code. You must use a virtual environment to manage your project dependencies. 
         
         python3 -m venv venv
         source ./venv/bin/activate
         

  4. Install your dependencies. In your project directory, check for a `requirements.txt` file containing the devkit's dependencies, and install them by running the following code. 
         
         pip install -r requirements.txt
         




### Step 2: Account authentication

Authentication methods for the Python devkit vary depending on your environment.

#### Google Colaboratory

  * If you're using the CX Insights devkit in a Google Colaboratory notebook, you can authenticate by adding the following code to the top of your user-managed notebooks: 
        
        project_id = ''
        

  * Doing so launches an interactive prompt letting you authenticate with Google Cloud in a browser. 
        
        !gcloud auth application-default login --no-launch-browser
        

  * Authenticating sets your active project to the `project_id`. 
        
        !gcloud auth application-default set-quota-project $project_id
        




#### Cloud Run functions

When using the CX Insights devkit with Cloud Run functions, the devkit automatically picks up the default environment credentials that these services use.

  * **Add devkit to the requirements TXT file** : Verify that it's listed in your Cloud Run functions service's `requirements.txt` file.
  * **Identity and Access Management role** : Verify that the Cloud Run functions service account has the appropriate Dialogflow IAM role assigned.



#### Local Python environment

Similar to Cloud Run functions, this devkit picks up your local authentication credentials if you're using the gcloud CLI.

  1. Install gcloud CLI. If you haven't already, install the Google Cloud SDK. It includes the gcloud CLI.
  2. Initialize gcloud CLI with the following code. 
         
         gcloud init
         

  3. Sign in to Google Cloud with the following code. 
         
         gcloud auth login
         

  4. Verify an active account with the following code. This command authenticates your principal Google Cloud account with the gcloud CLI. The CX Insights devkit can then fetch the credentials from your setup. 
         
         gcloud auth list
         




## Devkit contents

The CX Insights devkit contains the following resources.

### Core folder

The core folder is synonymous with the core resource types found in most classes. It has the high-level building blocks of the devkit and general functionalities like authentication and global configurations. These classes and methods are used to build higher-level methods or custom tools and applications.

### Common folder

The common folder contains wrappers built around the methods implemented in the Google Cloud SDK. The idea here is to add a new level of simplicity to existing implementations. You can perform the following actions with the Common folder.

  * Manipulate global configurations from CX Insights.
  * Ingest conversations (single and bulk) with metadata.
  * Create or list blobs in a Cloud Storage bucket.
  * Create transcriptions from audios using STT V1 and V2.
  * Transcribe mono audio files with STT V1.



### Workflows folder

The workflows folder contains classes and methods designed to perform actions that CX Insights doesn't support, such as the following.

  * Format transcripts from Genesys Cloud to CX Insights.
  * Format transcripts from AWS to Customer Experience Insights.
  * Recognize roles in a transcript using Gemini.



### Annotate an audio conversation

The following Python script transcribes an audio file, assigns speaker roles, then sends the enriched conversation data to CX Insights for analysis.
    
    
        def audio_with_role_recognition():
          # 1. Reset Insights Settings
          reset_insights_settings()
          # Verifies a clean state for CX Insights settings before starting the test.
          # This function is assumed to be defined elsewhere and handles resetting global configurations.
    
          # 2. Initialize Speech-to-Text V2 Client
          sp = speech.V2(
              project_id = _PROBER_PROJECT_ID
          )
          # Initializes a client for interacting with the Google Cloud Speech-to-Text API (V2).
          # _PROBER_PROJECT_ID: The Google Cloud Project ID where the STT recognizer resides.
    
          # 3. Create Transcription
          transcript = sp.create_transcription(
              audio_file_path = _MONO_SHORT_AUDIO_LOCATION,
              recognizer_path = 'projects/<project_id>/locations/<region>/recognizers/<recognizer_id>'
          )
          # Sends an audio file for transcription using a specific STT V2 recognizer.
          # audio_file_path: Local path to the mono audio file to be transcribed.
          # recognizer_path: Full resource path to the STT V2 recognizer to be used for transcription.
          #                  Example: 'projects/YOUR_PROJECT_NUMBER/locations/global/recognizers/YOUR_RECOGNIZER_ID'
    
    
          # Verifies that the returned 'transcript' object is of the expected type from the Speech-to-Text V2 API.
    
          # 4. Format Transcription
          ft = format.Speech()
          # Initializes a formatting utility for speech-related data.
    
          transcript = ft.v2_recognizer_to_dict(transcript)
          # Transforms the STT V2 `RecognizeResponse` object into a more manageable Python dictionary format,
          # which is often easier to work with for subsequent processing steps like role recognition.
    
          # 5. Initialize Google Cloud Storage Client
          gcs = storage.Gcs(
            project_name = _PROBER_PROJECT_ID,
            bucket_name = _TMP_PROBER_BUCKET
          )
          # Initializes a Google Cloud Storage client.
          # project_name: The Google Cloud Project ID.
          # bucket_name: The name of the Google Cloud Storage bucket where the processed transcript will be temporarily stored.
    
          # 6. Generate Unique File Name
          file_name = f'{uuid.uuid4()}.json'
          # Creates a unique file name for the JSON transcript using a UUID (Universally Unique Identifier).
          # This prevents naming conflicts when uploading multiple transcripts to the same Google Cloud Storage bucket.
    
          # 7. Perform Role Recognition
          role_recognizer = rr.RoleRecognizer()
          # Initializes the RoleRecognizer component, likely part of the Customer Experience Insights DevKit,
          # responsible for identifying speaker roles (e.g., agent, customer) within a conversation.
    
          roles = role_recognizer.predict_roles(conversation=transcript)
          # Predicts the roles of speakers in the transcribed conversation.
          # conversation: The transcribed conversation in a dictionary format.
    
          transcript = role_recognizer.combine(transcript, roles)
          # Integrates the recognized roles back into the original transcript data structure.
          # This step enriches the transcript with speaker role metadata.
    
          # 9. Upload Processed Transcript to Google Cloud Storage
          gcs.upload_blob(
            file_name = file_name,
            data = transcript
          )
          # Uploads the enriched transcript (as JSON data) to the specified Google Cloud Storage bucket with the generated unique file name.
          # This Google Cloud Storage path will be used as the source for Customer Experience Insights ingestion.
    
          # 10. Construct Google Cloud Storage Path
          gcs_path = f"gs://{_TMP_PROBER_BUCKET}/{file_name}"
          # Forms the full Google Cloud Storage URI for the uploaded transcript, which is required by the Customer Experience Insights Ingestion API.
    
          # 11. Initialize CX Insights Ingestion
          ingestion = insights.Ingestion(
              parent = _PARENT,
              transcript_path = gcs_path
          )
          # Initializes an Ingestion client for CX Insights.
          # parent: The parent resource path for CX Insights, typically in the format:
          #         'projects/YOUR_PROJECT_NUMBER/locations/YOUR_LOCATION'
          # transcript_path: The Google Cloud Storage URI where the conversation transcript is stored.
    
          # 12. Ingest Single Conversation
          operation = ingestion.single()
          # Initiates the ingestion of the single conversation into CX Insights.
          # This returns an operation object, which can be used to monitor the status of the ingestion.
    

### Contributions and feature requests

To make contributions or feature requests, follow these steps:

  1. Create a repository fork on GitHub.
  2. Create your feature branch with the following code. 
         
         git checkout -b feature/AmazingFeature

  3. Commit your changes with the following code. 
         
         git commit -m 'Add some AmazingFeature'

  4. Push changes to the branch with the following code. 
         
         git push origin feature/AmazingFeature

  5. Open a pull request and submit it from your feature branch to the main repository.



## License

The distribution of the CX Insights devkit is under Apache 2.0 License. For details, see the `LICENSE` file in the project repository.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
