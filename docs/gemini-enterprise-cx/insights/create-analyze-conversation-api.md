---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api/
title: Analyze a conversation using the API \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:24.896488+00:00
---

# Analyze a conversation using the API  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Analyze a conversation using the API Stay organized with collections  Save and categorize content based on your preferences. 

Conversations can be viewed in Customer Experience Insights after a corresponding conversation object has been created. This how-to guide walks you through the process of analyzing a conversation using the REST API. If preferred, you can also perform these actions using the CX Insights [console](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui).

## Prerequisites

  1. Enable the [Cloud Storage and Insights APIs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) on your Google Cloud project.
  2. [Import your conversation data](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api).



### Chat conversation

  1. Import the conversation's chat transcript as an [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) in your Cloud Storage bucket.

  2. Make a note of the object path, with the format `gs://<bucket>/<object>`.




The chat transcript file must be supplied as a JSON-formatted file that matches the [CCAI conversation data format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format).

### Voice conversation

  1. [Import all the files](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api) from a Cloud Storage bucket. Audio and transcript files must be imported as [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) in your Cloud Storage bucket.

  2. Make a note of the two object paths, with the format `gs://<bucket>/<object>`.




The transcript files must be the returned result of a Cloud Speech-to-Text API transcription. Specifically, they must match the [response](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize#response-body) returned from audio recognition, which is identical for synchronous recognition and asynchronous recognition across all Speech-to-Text API versions. Other transcription formats are unsupported and will result in an error during conversation analysis.

**Note:** Only audio with two channels is supported. Otherwise, an error occurs during conversation analysis.

## Analyze a conversation

Once a `Conversation` object is created in CX Insights, it must be analyzed in order to produce useful results. A single conversation can be analyzed many times, and each separate analysis creates a new `Analysis` object.

An analysis runs a series of [annotators](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#Analysis.CallAnnotation) against your conversation data and returns the results in the response. By default, the analysis will run all available annotators. Optionally, you can configure the analysis to run [specified annotators only](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api#optional_configure_an_analysis).

An analysis is a long-running operation. Calling the `CreateAnalysis` method creates an `Operation` object that represents the long-running process. After the operation is complete, the `Operation` object contains the result. You can poll the `Operation` object to check for completion.

**Note:** If the [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) field is not set, CX Insights will automatically infer it. Only English (all dialects) is supported for analyses.

### Create a new analysis

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



### REST

Refer to the [`conversations.analyses:create`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/create) API endpoint for complete details.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * CONVERSATION_ID: the ID of the conversation you want to analyze. This value was returned in the `createConversation` response.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID"
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contact_center_insights_v1
    
    
    def create_analysis(conversation_name: str) -> contact_center_insights_v1.Analysis:
        """Creates an analysis.
    
        Args:
            conversation_name:
                The parent resource of the analysis.
                Format is 'projects/{project_id}/locations/{location_id}/conversations/{conversation_id}'.
                For example, 'projects/my-project/locations/us-central1/conversations/123456789'.
    
        Returns:
            An analysis.
        """
        # Construct an analysis.
        analysis = contact_center_insights_v1.Analysis()
    
        # Call the Insights client to create an analysis.
        insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
        analysis_operation = insights_client.create_analysis(
            parent=conversation_name, analysis=analysis
        )
        analysis = analysis_operation.result(timeout=86400)
        print(f"Created {analysis.name}")
        return analysis
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html);
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import java.io.IOException;
    
    public class CreateAnalysis {
    
      public static void main(String[] args) throws Exception, IOException {
        // TODO(developer): Replace this variable before running the sample.
        String conversationName =
            "projects/my_project_id/locations/us-central1/conversations/my_conversation_id";
    
        createAnalysis(conversationName);
      }
    
      public static [Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html) createAnalysis(String conversationName) throws Exception, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct an analysis.
          [Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html) analysis = [Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html).newBuilder().build();
    
          // Call the Insights client to create an analysis.
          [Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html) response = client.[createAnalysisAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html#com_google_cloud_contactcenterinsights_v1_ContactCenterInsightsClient_createAnalysisAsync__org_jspecify_annotations_Nullable_com_google_cloud_contactcenterinsights_v1_ConversationName_com_google_cloud_contactcenterinsights_v1_Analysis_)(conversationName, analysis).get();
          System.out.printf("Created %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis.html#com_google_cloud_contactcenterinsights_v1_Analysis_getName__)());
          return response;
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const conversationName = 'projects/my_project_id/locations/us-central1/conversations/my_conversation_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function createAnalysis() {
      try {
        const [operation] = await client.createAnalysis({
          parent: conversationName,
        });
    
        // Wait for the operation to complete.
        const [analysis] = await operation.promise();
        console.info(`Created ${analysis.name}`);
      } catch (err) {
        console.error(`createAnalysis failed: ${JSON.stringify(err, null, 2)}`);
        process.exitCode = 1;
      }
    }
    createAnalysis();

### (Optional) Configure an analysis

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



### REST

Refer to the [`conversations.analyses:create`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/create) API endpoint for complete details. Include any annotators that you want to run in the `annotatorSelector` object and set them to `true`. Any annotators not included will default to `false`. If you don't specify any annotators in the `annotatorSelector` object all annotators will be run.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * PHRASE_MATCHER(s): The fully qualified phrase matcher resource names of the phrase matchers you want to use for the phrase matcher annotator. If left empty, all active phrase matchers will run.
  * ISSUE_MODEL(s): The fully qualified resource names of the issue models you want to use for the issue model annotator. Only works if run_issue_model_annotator is true. If left empty, all deployed issue models will run. Currently limited to 1 deployed model.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses

Request JSON body: 
    
    
    {
      "annotatorSelector": {
        "run_interruption_annotator": {true/false},
        "run_silence_annotator": {true/false},
        "run_phrase_matcher_annotator": {true/false},
        "phrase_matchers": PHRASE_MATCHER(s),
        "run_sentiment_annotator": {true/false},
        "run_entity_annotator": {true/false},
        "run_intent_annotator": {true/false},
        "run_issue_model_annotator": {true/false}
        "issue_models": ISSUE_MODEL(s)
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses"

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
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID/analyses" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID"
    }
    

## Poll the operation

Creating an analysis returns a long-running operation. Long-running methods are asynchronous, and the operation might not be completed when the method returns a response. You can poll the operation to check on its status. See the [long-running operations page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) for details and code samples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
