---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui/
title: Use the console to import and analyze a conversation \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:22.673784+00:00
---

# Use the console to import and analyze a conversation  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Use the console to import and analyze a conversation Stay organized with collections  Save and categorize content based on your preferences. 

You can import a single or multiple conversation files from a Cloud Storage bucket to Customer Experience Insights. You can view and analyze conversations in Customer Experience Insights after you import them. This guide walks you through the process of importing and analyzing a single conversation using the [CX Insights console](https://ccai.cloud.google.com/insights/projects).

## Before you begin

[Enable the following APIs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) for your Google Cloud project:

  * Cloud Storage
  * Speech-to-Text
  * CX Insights



## Upload to Cloud Storage

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `storage.objects.list`
  * `storage.objects.create`



### Chat Conversation

The transcript of a chat conversation must be supplied as a JSON-formatted file that matches the [CCAI conversation data format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format). Follow these steps to add a chat transcript.

  1. Upload the conversation's chat transcript as an [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) in your Cloud Storage bucket.
  2. Make a note of the object path, which is formatted as `gs://<bucket>/<object>`.



### Voice conversation

  1. Upload the conversation audio or transcript as an [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) in your Cloud Storage bucket.
  2. Make a note of the object path, formatted as `gs://<bucket>/<object>`.

**Note:** Audio transcript files can be provided in the [CCAI conversation data format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format) or they can be the returned [speech recognition result](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rpc/google.cloud.speech.v2#speechrecognitionresult) of a Speech-to-Text API transcription.

The response is identical for synchronous recognition and asynchronous recognition across all Speech-to-Text API versions. Other transcription formats aren't supported and result in an error during import.

CX Insights only supports audio with two channels. More or fewer channels will result in an error during conversation analysis.

## Import a conversation from Cloud Storage

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.projects.get`
  * `contactcenterinsights.conversations.upload`



  1. Navigate to the CX Insights console and sign in with your Google Account.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Enter your project ID.

  3. Click **Conversation Hub** > **Import**.

  4. Select your conversation type, either **Voice** or **Chat**.

  5. Click **Next**.




### Chat conversation

Follow these steps to import your chat conversation transcript.

  1. For the Cloud Storage resource, select one of the following options:

     * **File** to import a single transcript file.
     * **Bucket** to import all transcript files within a folder in a Cloud Storage bucket.
  2. Enter the path for the transcript file or folder in the **Transcript URI** field.

  3. Click **Next**.

  4. For the conversation data, enter the agent ID in the **Agent ID** field. This is the unique identifier used by CX Insights for the agent in the conversation.




### Voice conversation

Follow these steps to import your audio conversation data.

#### Import a single conversation

  1. For the Cloud Storage resource, select **File** to import a single audio file and a single transcript file.
  2. Enter the path for the audio file in the **Audio URI** field.
  3. For the transcript settings, select **Provide a transcript** and enter the path for the transcript file in the **Transcript URI** field.
  4. Click **Next**.
  5. Enter the agent ID in the **Agent ID** field. CX Insights uses this unique identifier for the agent in the conversation.
  6. Select either **1** or **2** to indicate the audio track the agent is on.



#### Import multiple conversations

**Note:** CX Insights does not support the bulk import of transcripts together with audio or the linking of audio with transcripts. If you have both conversation audio and transcripts, make sure to save them in separate buckets.

  1. For the Cloud Storage resource, select **Bucket** to import all the files from a folder within a Cloud Storage bucket.
  2. Enter the path for the folder containing your audio files in the **Audio URI** field.
  3. For the transcript settings, select **Use default STT config in Settings** to automatically transcribe audio files. Select **Provide a transcript** to import all your transcript files.
  4. Enter the path for the folder containing transcript files in the **Transcript URI** field.
  5. Click **Next**.
  6. Enter the agent ID in the **Agent ID** field. This is the unique identifier used by CX Insights for the agent in the conversation.
  7. Select either **1** or **2** to indicate the audio track the agent is on.



After you enter the required information, click **Import** to import the conversation into CX Insights. You should receive a notification indicating when the conversation has been successfully imported.

**Note:** If the [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) field is not set, CX Insights uses the default language `en-us`.

## Analyze a conversation

After you import a conversation object in CX Insights, you can analyze it to produce useful insights. A single conversation object can be analyzed many times, and each separate analysis creates a new analysis object. If the [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) field is not set, CX Insights will automatically infer it. Refer to the [language support](https://docs.cloud.google.com/gemini-enterprise-cx/insights/languages) documentation for a list of languages supported for analysis.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.projects.get`
  * `contactcenterinsights.conversations.list`
  * `contactcenterinsights.conversations.get`
  * `contactcenterinsights.analyses.create`



  1. Click the name of your conversation in the conversation list view table.
  2. After the conversation details page loads, click **Analyze**.
  3. The analysis may take some time. You can leave the page and come back later.
  4. After the analysis is complete, you can view the results on the conversation details page.



## View your conversations

You can view your Customer Experience Insights conversations and analyses in the console. When an operation reports completion, a new table entry for the conversation and analysis appears. If a conversation has multiple analyses, the console displays the results from the most recent analysis.

To view the conversation cover page:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.projects.get`
  * `contactcenterinsights.conversations.list`



  1. Navigate to the CX Insights console and sign in with your Google Account.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Enter your project ID.




Before you import any conversations, the page is empty. After you import conversations, the results appear on this page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
