---
url: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook/
title: Webhook service \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:35.777563+00:00
---

# Webhook service  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Webhook service Stay organized with collections  Save and categorize content based on your preferences. 

To use fulfillment in a production system, you must implement and deploy a webhook service. To handle fulfillment, your webhook service must accept JSON requests and return JSON responses as specified in this guide. The detailed processing flow for fulfillment and webhooks is described in the [Fulfillment overview document](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview).

## Webhook service requirements

Your webhook service must meet the following requirements:

  * Handle HTTPS requests. HTTP is not supported. If you host your webhook service on Google Cloud using a [Compute](https://cloud.google.com/products/compute) or [Serverless Computing](https://docs.cloud.google.com/serverless) solution, see the product documentation for serving with HTTPS. For other hosting options, see [Get an SSL certificate for your domain](https://support.google.com/domains/answer/7630973).
  * Ensure the webhook service URL is publicly accessible.
  * Handle POST requests with a JSON `WebhookRequest` body.
  * Respond to `WebhookRequest` requests with a JSON `WebhookResponse` body.



## Authentication

**Note:** Webhook source IPs are in the subset of those listed at <https://www.gstatic.com/ipranges/goog.json> that exclude those at <https://www.gstatic.com/ipranges/cloud.json>. Beyond this, Dialogflow can't make any guarantees about IP ranges for machines that send webhook requests. Instead of restricting access by IP range, use one of the following authentication methods:X | Item  
---|---  
Login username and password | For webhook settings, you can specify optional login username and password values. If supplied, Dialogflow adds an authorization HTTP header to webhook requests. This header is of the form: `"authorization: Basic <base 64 encoding of the string username:password>"`.  
Authentication headers | For webhook settings, you can specify optional HTTP header key-value pairs. If supplied, Dialogflow adds these HTTP headers to webhook requests. It is common to provide a single pair with a key of `authorization`.  
Cloud Run functions built-in authentication | You can use the built-in authentication when using Cloud Run functions. To use this type of authentication, don't supply username, password, or authorization headers. If you supply any of these fields, they won't be used for the _built-in_ authentication.  
Service identity tokens | You can use service identity tokens for authentication. If you don't supply login username, login password, or a header with a key of `authorization`, Dialogflow automatically assumes that service identity tokens should be used and adds an authorization HTTP header to webhook requests. This header is of the form: `"authorization: Bearer <identity token>"`.  
Mutual TLS authentication | See the [Mutual TLS authentication](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-mtls) documentation.  
**Note:** It's important to secure your webhook service so that only you or your Dialogflow agent are authorized to make requests.

## Webhook request

When an intent configured for fulfillment is matched, Dialogflow sends an HTTPS POST webhook request to your webhook service. The body of this request is a JSON object with information about the matched intent.

In addition to the end-user query, many integrations also send information about the end-user. For example, an ID that uniquely identifies the user. This information can be accessed using the `originalDetectIntentRequest` field in the webhook request, which contains the information sent from the integration platform.

To learn more, see the [`WebhookRequest`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#webhookrequest) reference documentation.

The following is a sample request:
    
    
    {
      "responseId": "response-id",
      "session": "projects/project-id/agent/sessions/session-id",
      "queryResult": {
        "queryText": "End-user expression",
        "parameters": {
          "param-name": "param-value"
        },
        "allRequiredParamsPresent": true,
        "fulfillmentText": "Response configured for matched intent",
        "fulfillmentMessages": [
          {
            "text": {
              "text": [
                "Response configured for matched intent"
              ]
            }
          }
        ],
        "outputContexts": [
          {
            "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 5,
            "parameters": {
              "param-name": "param-value"
            }
          }
        ],
        "intent": {
          "name": "projects/project-id/agent/intents/intent-id",
          "displayName": "matched-intent-name"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "en"
      },
      "originalDetectIntentRequest": {}
    }
    

## Webhook response

After your webhook receives a request, it must send a response. The body of this response is a JSON object that contains the following information:

  * The [response](https://docs.cloud.google.com/dialogflow/docs/intents-responses) that Dialogflow returns to the end-user.
  * Updates to [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) active for the conversation.
  * A [follow-up event](https://docs.cloud.google.com/dialogflow/docs/events-overview) to trigger an intent match.
  * A [custom payload](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#custom) to be sent to the [integration](https://docs.cloud.google.com/dialogflow/docs/integrations) or [detect intent client](https://docs.cloud.google.com/dialogflow/docs/api-overview#detect-intent).



The following limitations apply to your response:

  * Respond within 10 seconds for [Google Assistant](https://docs.cloud.google.com/dialogflow/docs/integrations/aog) applications or 5 seconds for other applications; otherwise, the request times out.
  * Keep the response size to 64 KiB or less.



To learn more, see the [`WebhookResponse`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#webhookresponse) reference documentation.

### Text response

The following is an example of a [text response](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#text):
    
    
    {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              "Text response from webhook"
            ]
          }
        }
      ]
    }
    

### Card response

The following is an example of a [card response](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#card):
    
    
    {
      "fulfillmentMessages": [
        {
          "card": {
            "title": "card title",
            "subtitle": "card text",
            "imageUri": "https://example.com/images/example.png",
            "buttons": [
              {
                "text": "button text",
                "postback": "https://example.com/path/for/end-user/to/follow"
              }
            ]
          }
        }
      ]
    }
    

### Google Assistant response

The following is an example of a [Google Assistant response](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#aog):
    
    
    {
      "payload": {
        "google": {
          "expectUserResponse": true,
          "richResponse": {
            "items": [
              {
                "simpleResponse": {
                  "textToSpeech": "this is a Google Assistant response"
                }
              }
            ]
          }
        }
      }
    }
    

### Context

The following is an example that sets [output context](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#output_contexts):
    
    
    {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              "Text response from webhook"
            ]
          }
        }
      ],
      "outputContexts": [
        {
          "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
          "lifespanCount": 5,
          "parameters": {
            "param-name": "param-value"
          }
        }
      ]
    }
    

### Event

The following is an example that invokes a [custom event](https://docs.cloud.google.com/dialogflow/docs/events-custom):
    
    
    {
      "followupEventInput": {
        "name": "event-name",
        "languageCode": "en-US",
        "parameters": {
          "param-name": "param-value"
        }
      }
    }
    

### Session entity

The following is an example that sets a [session entity](https://docs.cloud.google.com/dialogflow/docs/entities-session):
    
    
    {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              "Choose apple or orange"
            ]
          }
        }
      ],
      "sessionEntityTypes":[
        {
          "name":"projects/project-id/agent/sessions/session-id/entityTypes/fruit",
          "entities":[
            {
              "value":"APPLE_KEY",
              "synonyms":[
                "apple",
                "green apple",
                "crabapple"
              ]
            },
            {
              "value":"ORANGE_KEY",
              "synonyms":[
                "orange"
              ]
            }
          ],
          "entityOverrideMode":"ENTITY_OVERRIDE_MODE_OVERRIDE"
        }
      ]
    }
    

### Custom payload

The following is an example that provides a custom payload:
    
    
    {
      "fulfillmentMessages": [
        {
          "payload": {
            "facebook": { // for Facebook Messenger integration
              "attachment": {
                "type": "",
                "payload": {}
              }
            },
            "slack": { // for Slack integration
              "text": "",
              "attachments": []
            },
            "richContent": [ // for Dialogflow Messenger integration
              [
                {
                  "type": "image",
                  "rawUrl": "https://example.com/images/logo.png",
                  "accessibilityText": "Example logo"
                }
              ]
            ],
            // custom integration payload here
          }
        }
      ]
    }
    

## Enable and manage fulfillment

To enable and manage fulfillment for your agent with the console:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Fulfillment** in the sidebar menu.
  4. Toggle the **Webhook** field to **Enabled**.
  5. Provide the details for your webhook service in the form. If your webhook doesn't require authentication, leave the authentication fields blank.
  6. Click **Save**.



![Screenshot of enabling fulfillment.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/fulfillment-webhook-form.png)

To enable and manage fulfillment for your agent with the API, see the [agent reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#agents). The `getFulfillment` and `updateFulfillment` methods let you manage fulfillment settings.

To enable fulfillment for an intent with the console:

  1. Select **Intents** in the left sidebar menu.
  2. Select an intent.
  3. Go to the **Fulfillment** section.
  4. Toggle **Enable webhook call for this intent** to On.
  5. Click **Save**.



To enable fulfillment for an intent with the API, see the [intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents) and set the `webhookState` field to `WEBHOOK_STATE_ENABLED`.

## Webhook errors

If your webhook service encounters an error, it should return one of the following HTTP status codes:

  * `400`: Bad request
  * `401`: Unauthorized
  * `403`: Forbidden
  * `404`: Not found
  * `500`: Internal server error
  * `503`: Service unavailable



In any of the following error situations, Dialogflow responds to the end user with the built-in response configured for the matched intent:

  * The response timeout was exceeded.
  * An error status code was received.
  * The response is invalid.
  * The webhook service is unavailable.



In addition, if a [detect intent API call](https://docs.cloud.google.com/dialogflow/docs/api-overview#detect-intent) triggers the intent match, the `status` field in the detect intent response contains the webhook error information. For example:
    
    
    "status": {
        "code": 206,
        "message": "Webhook call failed. <details of the error...>"
    }
    

### Automatic retries

Dialogflow ES includes internal mechanisms that automatically retry on certain webhook errors to improve robustness. Only non-terminal errors are retried, such as timeout or connection errors.

To reduce the likelihood of duplicated calls:

  * Set longer webhook timeout thresholds.
  * Support idempotency in your webhook logic or deduplicate requests.



## Using Cloud Run functions

You can use Cloud Run functions for fulfillment in several ways. The Dialogflow [inline editor](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor) integrates with [Cloud Run functions](https://docs.cloud.google.com/functions/docs). When you use the inline editor to create and edit your webhook code, Dialogflow establishes a secure connection to your Cloud Function.

You can also use a Cloud Function not created by the inline editor. If the Cloud Function resides in the same project as your agent, your agent can call your webhook without needing any special configuration.

However, you must manually set up this integration in the following two situations:

  1. The **Dialogflow Service Agent** [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) with the following address must exist for your agent project: 
         
         service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

This special service account and the associated key is normally created automatically when you create the first agent for a project. If your agent was created before May 10, 2021, you may need to trigger creation of this special service account with the following: 
     1. Create a new agent for the project.
     2. Execute the following command: 
            
            gcloud beta services identity create --service=dialogflow.googleapis.com --project=agent-project-id

  2. If your webhook function resides in a different project than the agent, you must provide the **Cloud Functions Invoker** [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) to the **Dialogflow Service Agent** service account in your function's project.



## Service identity tokens

When Dialogflow calls a webhook, it provides a [Google identity token](https://developers.google.com/identity/sign-in/web/backend-auth) with the request. Any webhook can optionally validate the token using Google client libraries or open-source libraries like [github.com/googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs). For example, you can verify the `email` of the ID token as: 
    
    
    service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

## Samples

The following samples show how to receive a `WebhookRequest` and send a `WebhookResponse`. These samples use intents created in the [quickstart](https://docs.cloud.google.com/dialogflow/docs/quick/build-agent).

### Go

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"encoding/json"
    	"fmt"
    	"log"
    	"net/http"
    )
    
    type intent struct {
    	DisplayName string `json:"displayName"`
    }
    
    type queryResult struct {
    	Intent intent `json:"intent"`
    }
    
    type text struct {
    	Text []string `json:"text"`
    }
    
    type message struct {
    	Text text `json:"text"`
    }
    
    // webhookRequest is used to unmarshal a WebhookRequest JSON object. Note that
    // not all members need to be defined--just those that you need to process.
    // As an alternative, you could use the types provided by
    // the Dialogflow protocol buffers:
    // https://godoc.org/google.golang.org/genproto/googleapis/cloud/dialogflow/v2#WebhookRequest
    type webhookRequest struct {
    	Session     string      `json:"session"`
    	ResponseID  string      `json:"responseId"`
    	QueryResult queryResult `json:"queryResult"`
    }
    
    // webhookResponse is used to marshal a WebhookResponse JSON object. Note that
    // not all members need to be defined--just those that you need to process.
    // As an alternative, you could use the types provided by
    // the Dialogflow protocol buffers:
    // https://godoc.org/google.golang.org/genproto/googleapis/cloud/dialogflow/v2#WebhookResponse
    type webhookResponse struct {
    	FulfillmentMessages []message `json:"fulfillmentMessages"`
    }
    
    // welcome creates a response for the welcome intent.
    func welcome(request webhookRequest) (webhookResponse, error) {
    	response := webhookResponse{
    		FulfillmentMessages: []message{
    			{
    				Text: text{
    					Text: []string{"Welcome from Dialogflow Go Webhook"},
    				},
    			},
    		},
    	}
    	return response, nil
    }
    
    // getAgentName creates a response for the get-agent-name intent.
    func getAgentName(request webhookRequest) (webhookResponse, error) {
    	response := webhookResponse{
    		FulfillmentMessages: []message{
    			{
    				Text: text{
    					Text: []string{"My name is Dialogflow Go Webhook"},
    				},
    			},
    		},
    	}
    	return response, nil
    }
    
    // handleError handles internal errors.
    func handleError(w http.ResponseWriter, err error) {
    	w.WriteHeader(http.StatusInternalServerError)
    	fmt.Fprintf(w, "ERROR: %v", err)
    }
    
    // HandleWebhookRequest handles WebhookRequest and sends the WebhookResponse.
    func HandleWebhookRequest(w http.ResponseWriter, r *http.Request) {
    	var request webhookRequest
    	var response webhookResponse
    	var err error
    
    	// Read input JSON
    	if err = json.NewDecoder(r.Body).Decode(&request); err != nil {
    		handleError(w, err)
    		return
    	}
    	log.Printf("Request: %+v", request)
    
    	// Call intent handler
    	switch intent := request.QueryResult.Intent.DisplayName; intent {
    	case "Default Welcome Intent":
    		response, err = welcome(request)
    	case "get-agent-name":
    		response, err = getAgentName(request)
    	default:
    		err = fmt.Errorf("Unknown intent: %s", intent)
    	}
    	if err != nil {
    		handleError(w, err)
    		return
    	}
    	log.Printf("Response: %+v", response)
    
    	// Send response
    	if err = json.NewEncoder(w).Encode(&response); err != nil {
    		handleError(w, err)
    		return
    	}
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO: add GSON dependency to Pom file
    // (https://mvnrepository.com/artifact/com.google.code.gson/gson/2.8.5)
    // TODO: Uncomment the line bellow before running cloud function
    // package com.example;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.GsonBuilder;
    import com.google.gson.JsonObject;
    import com.google.gson.JsonParser;
    import java.io.BufferedWriter;
    
    public class Example implements HttpFunction {
    
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        JsonParser parser = new JsonParser();
        Gson gson = new GsonBuilder().create();
    
        JsonObject job = gson.fromJson(request.getReader(), JsonObject.class);
        String str =
            job.getAsJsonObject("queryResult")
                .getAsJsonObject("intent")
                .getAsJsonPrimitive("displayName")
                .toString();
        JsonObject o = null;
        String a = '"' + "Default Welcome Intent" + '"';
        String b = '"' + "get-agent-name" + '"';
        String responseText = "";
    
        if (str.equals(a)) {
          responseText = '"' + "Hello from a Java GCF Webhook" + '"';
        } else if (str.equals(b)) {
          responseText = '"' + "My name is Flowhook" + '"';
        } else {
          responseText = '"' + "Sorry I didn't get that" + '"';
        }
    
        o =
            parser
                .parse(
                    "{\"fulfillmentMessages\": [ { \"text\": { \"text\": [ "
                        + responseText
                        + " ] } } ] }")
                .getAsJsonObject();
    
        BufferedWriter writer = response.getWriter();
        writer.write(o.toString());
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // TODO: Add handleWebhook to 'Entry point' in the Google Cloud Function
    functions.http('handleWebhook', (request, response) => {
      const tag = request.body.queryResult.intent.displayName;
    
      let jsonResponse = {};
      if (tag === 'Default Welcome Intent') {
        //fulfillment response to be sent to the agent if the request tag is equal to "welcome tag"
        jsonResponse = {
          fulfillment_messages: [
            {
              text: {
                //fulfillment text response to be sent to the agent
                text: ['Hello from a GCF Webhook'],
              },
            },
          ],
        };
      } else if (tag === 'get-name') {
        //fulfillment response to be sent to the agent if the request tag is equal to "welcome tag"
        jsonResponse = {
          fulfillment_messages: [
            {
              text: {
                //fulfillment text response to be sent to the agent
                text: ['My name is Flowhook'],
              },
            },
          ],
        };
      } else {
        jsonResponse = {
          //fulfillment text response to be sent to the agent if there are no defined responses for the specified tag
          fulfillment_messages: [
            {
              text: {
                ////fulfillment text response to be sent to the agent
                text: [
                  `There are no fulfillment responses defined for "${tag}"" tag`,
                ],
              },
            },
          ],
        };
      }
      response.send(jsonResponse);
    });

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # TODO: change the default Entry Point text to handleWebhook
    import functions_framework
    
    
    @functions_framework.http
    def handleWebhook(request):
        req = request.get_json()
    
        responseText = ""
        intent = req["queryResult"]["intent"]["displayName"]
    
        if intent == "Default Welcome Intent":
            responseText = "Hello from a GCF Webhook"
        elif intent == "get-agent-name":
            responseText = "My name is Flowhook"
        else:
            responseText = f"There are no fulfillment responses defined for Intent {intent}"
    
        # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
        res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}
    
        return res
    
    

[ Previous arrow_back  Inline editor  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor)

[ Next Webhook for slot filling  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook-slot-filling)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
