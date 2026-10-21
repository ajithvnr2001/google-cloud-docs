---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/sentiment/
title: Detect intent with sentiment analysis \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:48.535150+00:00
---

# Detect intent with sentiment analysis  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/sentiment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Detect intent with sentiment analysis Stay organized with collections  Save and categorize content based on your preferences. 

Sentiment analysis inspects user input and identifies the prevailing subjective opinion to determine a user's attitude as positive, negative, or neutral. When making a detect intent request, you can enable sentiment analysis, and the response will contain sentiment analysis values.

The Natural Language API is used by Dialogflow to perform this analysis. For more information on the API and documentation on interpreting Dialogflow sentiment analysis results, see the following:

  * [Sentiment Analysis](https://cloud.google.com/natural-language/docs/basics#sentiment_analysis)
  * [Interpreting sentiment analysis values](https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values)

**Note:** In cases where the sentiment analysis score is 0, the returned `sentimentAnalysisResult` field will be empty. If you prefer explicit 0 values in the response, see the `$outputDefaults` [system parameter](https://cloud.google.com/apis/docs/system-parameters#definitions).

## Supported languages

For a list of supported languages, see the **sentiment** column on the [Languages](https://docs.cloud.google.com/dialogflow/docs/reference/language) page. If you request sentiment analysis for an unsupported language, your detect intent request does not fail, but the `QueryResult.diagnostic_info` field contains error information.

## Before you begin

This feature is only applicable when using the API for [end-user interactions](https://docs.cloud.google.com/dialogflow/docs/api-overview). If you are using an [integration](https://docs.cloud.google.com/dialogflow/docs/integrations), you can skip this guide. 

Before you begin, complete the following steps:

  * Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  * Perform [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).



## Create an agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Sign in to the console if prompted. For more information, see the [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console). 
  3. In the sidebar menu, expand **Loading agents**. 
  4. Click **Create new agent**. 
  5. Enter the agent name, default language, and default time zone. 
  6. Enter an existing project. To let the Dialogflow console create a project, select **Create a new Google project**. 
  7. Click **Create**. 



## Agent settings for sentiment analysis

You can trigger sentiment analysis per detect intent request, or you can configure your agent to always return sentiment analysis results.

**Note:** Even if an agent is configured to use sentiment analysis, [Actions on Google](https://developers.google.com/actions/dialogflow/) requests won't receive sentiment analysis results.

To enable sentiment analysis for all queries:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select the settings _settings_ icon next to the agent name.
  4. Select the **Advanced** tab.
  5. Turn on **Enable sentiment analysis for the current query**.



## Use the Dialogflow simulator

You can interact with the agent and receive sentiment analysis results using the [Dialogflow simulator](https://docs.cloud.google.com/dialogflow/docs/console#simulator):

  1. Enter "Thank you for helping me."
  2. View the **SENTIMENT** section at the bottom of the simulator. It shows a positive sentiment score.
  3. Enter "It didn't work at all." in the simulator.
  4. View the **SENTIMENT** section at the bottom of the simulator. It shows a negative sentiment score.

**Note:** When a very negative sentiment is returned, you can hand off unsatisfied users to live agents, or understand which intents lead to the most negative customer sentiment. An example of a handoff implementation can be found on [GitHub](https://github.com/dialogflow/agent-human-handoff-nodejs).

## Detect intent

To detect intent, call the `detectIntent` method on the [`Sessions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#sessions) type.

### REST

Call the `detectIntent` method and provide the `sentimentAnalysisRequestConfig` field. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * SESSION_ID: a session ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent

Request JSON body: 
    
    
    {
      "queryParams": {
        "sentimentAnalysisRequestConfig": {
          "analyzeQueryTextSentiment": true
        }
      },
      "queryInput": {
        "text": {
          "text": "please reserve an amazing meeting room for six people",
          "languageCode": "en-US"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "responseId": "747ee176-acc5-46be-8d9a-b7ef9c2b9199",
      "queryResult": {
        "queryText": "please reserve an amazing meeting room for six people",
        "action": "room.reservation",
        "parameters": {
          "date": "",
          "duration": "",
          "guests": 6,
          "location": "",
          "time": ""
        },
        "fulfillmentText": "I can help with that. Where would you like to reserve a room?",
        ...
        "sentimentAnalysisResult": {
          "queryTextSentiment": {
            "score": 0.8,
            "magnitude": 0.8
          }
        }
      }
    }
    

Notice that the `sentimentAnalysisResult` field contains `score` and `magnitude` values. 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.v2.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html);
    import com.google.cloud.dialogflow.v2.[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryParameters.html);
    import com.google.cloud.dialogflow.v2.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html);
    import com.google.cloud.dialogflow.v2.[SentimentAnalysisRequestConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisRequestConfig.html);
    import com.google.cloud.dialogflow.v2.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html);
    import com.google.cloud.dialogflow.v2.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html);
    import com.google.cloud.dialogflow.v2.[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html);
    import com.google.common.collect.Maps;
    import java.io.IOException;
    import java.util.List;
    import java.util.Map;
    
    public class DetectIntentWithSentimentAnalysis {
    
      public static Map<String, QueryResult> detectIntentSentimentAnalysis(
          String projectId, List<String> texts, String sessionId, String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        Map<String, QueryResult> queryResults = Maps.newHashMap();
        // Instantiates a client
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html).create()) {
          // Set the session name using the sessionId (UUID) and projectID (my-project-id)
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html) session = [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html).of(projectId, sessionId);
          System.out.println("Session Path: " + session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)());
    
          // Detect intents for each text input
          for (String text : texts) {
            // Set the text (hello) and language code (en-US) for the query
            [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html).Builder textInput =
                [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html).newBuilder().setText(text).setLanguageCode(languageCode);
    
            // Build the query with the TextInput
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html) queryInput = [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html).newBuilder().setText(textInput).build();
    
            //
            [SentimentAnalysisRequestConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisRequestConfig.html) sentimentAnalysisRequestConfig =
                [SentimentAnalysisRequestConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisRequestConfig.html).newBuilder().[setAnalyzeQueryTextSentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisRequestConfig.Builder.html#com_google_cloud_dialogflow_v2_SentimentAnalysisRequestConfig_Builder_setAnalyzeQueryTextSentiment_boolean_)(true).build();
    
            [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryParameters.html) queryParameters =
                [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryParameters.html).newBuilder()
                    .[setSentimentAnalysisRequestConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryParameters.Builder.html#com_google_cloud_dialogflow_v2_QueryParameters_Builder_setSentimentAnalysisRequestConfig_com_google_cloud_dialogflow_v2_SentimentAnalysisRequestConfig_)(sentimentAnalysisRequestConfig)
                    .build();
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html) detectIntentRequest =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html).newBuilder()
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)())
                    .setQueryInput(queryInput)
                    .setQueryParams(queryParameters)
                    .build();
    
            // Performs the detect intent request
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html) response = sessionsClient.detectIntent(detectIntentRequest);
    
            // Display the query result
            [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html#com_google_cloud_dialogflow_v2_DetectIntentResponse_getQueryResult__)();
    
            System.out.println("====================");
            System.out.format("Query Text: '%s'\n", queryResult.[getQueryText](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getQueryText__)());
            System.out.format(
                "Detected Intent: %s (confidence: %f)\n",
                queryResult.[getIntent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntent__)().getDisplayName(), queryResult.[getIntentDetectionConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntentDetectionConfidence__)());
            System.out.format(
                "Fulfillment Text: '%s'\n",
                queryResult.[getFulfillmentMessagesCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessagesCount__)() > 0
                    ? queryResult.[getFulfillmentMessages](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessages_int_)(0).getText()
                    : "Triggered Default Fallback Intent");
            System.out.format(
                "Sentiment Score: '%s'\n",
                queryResult.[getSentimentAnalysisResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getSentimentAnalysisResult__)().getQueryTextSentiment().getScore());
    
            queryResults.put(text, queryResult);
          }
        }
        return queryResults;
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Dialogflow client library
    const dialogflow = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)').v2;
    
    // Instantiate a DialogFlow client.
    const sessionClient = new dialogflow.[SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'ID of GCP project associated with your Dialogflow agent';
    // const sessionId = `user specific ID of session, e.g. 12345`;
    // const query = `phrase(s) to pass to detect, e.g. I'd like to reserve a room for six people`;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    // Define session path
    const sessionPath = sessionClient.projectAgentSessionPath(
      projectId,
      sessionId
    );
    
    async function detectIntentandSentiment() {
      // The text query request.
      const request = {
        session: sessionPath,
        queryInput: {
          text: {
            text: query,
            languageCode: languageCode,
          },
        },
        queryParams: {
          sentimentAnalysisRequestConfig: {
            analyzeQueryTextSentiment: true,
          },
        },
      };
    
      // Send request and log result
      const responses = await sessionClient.detectIntent(request);
      console.log('Detected intent');
      const result = responses[0].queryResult;
      console.log(`  Query: ${result.queryText}`);
      console.log(`  Response: ${result.fulfillmentText}`);
      if (result.intent) {
        console.log(`  Intent: ${result.intent.displayName}`);
      } else {
        console.log('  No intent matched.');
      }
      if (result.sentimentAnalysisResult) {
        console.log('Detected sentiment');
        console.log(
          `  Score: ${result.sentimentAnalysisResult.queryTextSentiment.score}`
        );
        console.log(
          `  Magnitude: ${result.sentimentAnalysisResult.queryTextSentiment.magnitude}`
        );
      } else {
        console.log('No sentiment Analysis Found');
      }

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_intent_with_sentiment_analysis(project_id, session_id, texts, language_code):
        """Returns the result of detect intent with texts as inputs and analyzes the
        sentiment of the query text.
    
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        from google.cloud import dialogflow
    
        session_client = dialogflow.SessionsClient()
    
        session_path = session_client.[session_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_session_path)(project_id, session_id)
        print("Session path: {}\n".format(session_path))
    
        for text in texts:
            text_input = dialogflow.[TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TextInput.html)(text=text, language_code=language_code)
    
            query_input = dialogflow.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryInput.html)(text=text_input)
    
            # Enable sentiment analysis
            sentiment_config = dialogflow.[SentimentAnalysisRequestConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SentimentAnalysisRequestConfig.html)(
                analyze_query_text_sentiment=True
            )
    
            # Set the query parameters with sentiment analysis
            query_params = dialogflow.[QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryParameters.html)(
                sentiment_analysis_request_config=sentiment_config
            )
    
            response = session_client.[detect_intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_detect_intent)(
                request={
                    "session": session_path,
                    "query_input": query_input,
                    "query_params": query_params,
                }
            )
    
            print("=" * 20)
            print("Query text: {}".format(response.query_result.query_text))
            print(
                "Detected intent: {} (confidence: {})\n".format(
                    response.query_result.intent.display_name,
                    response.query_result.intent_detection_confidence,
                )
            )
            print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
            # Score between -1.0 (negative sentiment) and 1.0 (positive sentiment).
            print(
                "Query Text Sentiment Score: {}\n".format(
                    response.query_result.sentiment_analysis_result.query_text_sentiment.score
                )
            )
            print(
                "Query Text Sentiment Magnitude: {}\n".format(
                    response.query_result.sentiment_analysis_result.query_text_sentiment.magnitude
                )
            )
    
    

[ Previous arrow_back  Detect intent with audio output  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-tts)

[ Next Long-running operations  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/long-running-operations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
