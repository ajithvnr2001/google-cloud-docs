---
url: https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook/
title: Create a webhook \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:32.775477+00:00
---

# Create a webhook  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Create a webhook Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to use a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook), so your agent can be more dynamic. [Cloud Functions](https://docs.cloud.google.com/functions/docs) are used to host the webhook due to their simplicity, but there are many other ways that you could host a webhook service. The example also uses the Go programming language, but you can use any [language supported by Cloud Functions](https://docs.cloud.google.com/functions/docs/concepts/exec). You will not need to edit the code for this guide.

The example webhook code does the following:

  * Reads parameter values from the webhook request.
  * Writes a parameter value to the webhook response.
  * Provides a text response in the webhook response.



## Before you begin

If you don't plan on using webhooks, you can skip this quickstart.

You should do the following before reading this guide:

  1. Read [flow basics](https://docs.cloud.google.com/dialogflow/cx/docs/basics).
  2. Perform [setup steps](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup).
  3. Perform steps in the [Build an agent using flows](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent) quickstart guide. Steps below continue working on the same agent. If you no longer have that agent, you can [download the agent](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/agent-shirts-1-flow.zip) and [restore it](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export).



## Create the Cloud Function

Cloud Functions can be created with the Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), [open console](https://console.cloud.google.com/)). To create a function for this guide:

  1. It is important that your Dialogflow CX agent and the function are both in the same project. This is the easiest way for Dialogflow CX to have [secure access to your function](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#cloud-run). To select your project, [go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard).
  2. Go to the [Cloud Functions overview page](https://console.cloud.google.com/functions/list).
  3. Click **Create Function** , and set the following fields: 
     * **Environment** : 1st gen
     * **Function name** : shirts-agent-webhook
     * **Region** : If you specified a region for your agent, use the same region.
     * **HTTP Trigger type** : HTTP
     * **URL** : Click the copy button here and save the value. You will need this URL when configuring the webhook.
     * **Authentication** : Require authentication
     * **Require HTTPS** : checked
  4. Click **Save**.
  5. Click **Next** (You do not need special runtime, build, connections, or security settings).
  6. Set the following fields: 
     * **Runtime** : Select the latest Go runtime.
     * **Source code** : Inline Editor
     * **Entry point** : HandleWebhookRequest
  7. Replace the code with the following:
         
         // Package cxwh contains an example Dialogflow CX webhook
         package cxwh
         
         import (
         	"encoding/json"
         	"fmt"
         	"log"
         	"net/http"
         )
         
         type fulfillmentInfo struct {
         	Tag string `json:"tag"`
         }
         
         type sessionInfo struct {
         	Session    string         `json:"session"`
         	Parameters map[string]any `json:"parameters"`
         }
         
         type text struct {
         	Text []string `json:"text"`
         }
         
         type responseMessage struct {
         	Text text `json:"text"`
         }
         
         type fulfillmentResponse struct {
         	Messages []responseMessage `json:"messages"`
         }
         
         // webhookRequest is used to unmarshal a WebhookRequest JSON object. Note that
         // not all members need to be defined--just those that you need to process.
         // As an alternative, you could use the types provided by the Dialogflow protocol buffers:
         // https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3#WebhookRequest
         type webhookRequest struct {
         	FulfillmentInfo fulfillmentInfo `json:"fulfillmentInfo"`
         	SessionInfo     sessionInfo     `json:"sessionInfo"`
         }
         
         // webhookResponse is used to marshal a WebhookResponse JSON object. Note that
         // not all members need to be defined--just those that you need to process.
         // As an alternative, you could use the types provided by the Dialogflow protocol buffers:
         // https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3#WebhookResponse
         type webhookResponse struct {
         	FulfillmentResponse fulfillmentResponse `json:"fulfillmentResponse"`
         	SessionInfo         sessionInfo         `json:"sessionInfo"`
         }
         
         // confirm handles webhook calls using the "confirm" tag.
         func confirm(request webhookRequest) (webhookResponse, error) {
         	// Create a text message that utilizes the "size" and "color"
         	// parameters provided by the end-user.
         	// This text message is used in the response below.
         	t := fmt.Sprintf("You can pick up your order for a %s %s shirt in 5 days.",
         		request.SessionInfo.Parameters["size"],
         		request.SessionInfo.Parameters["color"])
         
         	// Create session parameters that are populated in the response.
         	// The "cancel-period" parameter is referenced by the agent.
         	// This example hard codes the value 2, but a real system
         	// might look up this value in a database.
         	p := map[string]any{"cancel-period": "2"}
         
         	// Build and return the response.
         	response := webhookResponse{
         		FulfillmentResponse: fulfillmentResponse{
         			Messages: []responseMessage{
         				{
         					Text: text{
         						Text: []string{t},
         					},
         				},
         			},
         		},
         		SessionInfo: sessionInfo{
         			Parameters: p,
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
         
         	// Get the tag from the request, and call the corresponding
         	// function that handles that tag.
         	// This example only has one possible tag,
         	// but most agents would have many.
         	switch tag := request.FulfillmentInfo.Tag; tag {
         	case "confirm":
         		response, err = confirm(request)
         	default:
         		err = fmt.Errorf("Unknown tag: %s", tag)
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

  8. Click **Deploy**.

  9. Wait until the status indicator shows that the function has successfully deployed. While waiting, examine the code you just deployed. Code comments describe important details.




## Create the webhook

Now that the webhook exists as a Cloud function, you will associate this webhook with your agent. To create the webhook for your agent:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Webhooks**.
  6. Click **Create**.
  7. Complete the following fields: 
     * **Display name** : shirts-agent-webhook
     * **Webhook URL** : Provide the webhook URL you saved when creating the function.
     * **Subtype** : Standard.
     * All other fields use default values.
  8. Click **Save**.



## Use the webhook

Now that the webhook is available to the agent, you will make use of the webhook in [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). The **Order Confirmation** page has an entry fulfillment, which currently has a static text response. To update the fulfillment to use your webhook:

  1. Select the **Build** tab.
  2. Click the **Order Confirmation** page to expand the page on the agent builder graph.
  3. Click the **Entry Fulfillment** field on the page to open the fulfillment panel.
  4. Delete the existing text response under the **Agent says** heading. When you hover the text, the delete _delete_ button appears.
  5. Click **Enable webhook**.
  6. Select the `shirts-agent-webhook` option from the **Webhook** dropdown menu.
  7. Enter `confirm` for the **Tag** field.
  8. Click **Save**.
  9. Close the fulfillment panel.



![Agent graph screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-webhook-entry-fulfillment.png)

The deployed webhook code sends a response that creates a [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) named `cancel-period`. Update the agent to reference this parameter in the final agent response for the same **Order Confirmation** page:

  1. Click the condition [route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) shown with a `true` condition to open the route panel.
  2. Scroll down to the **Fulfillment** section of the route panel, and add the following text response under the **Agent says** heading: `You can cancel your order within $session.params.cancel-period days. Goodbye.`
  3. Click **Save**.
  4. Close the route panel.



![Agent graph screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-webhook-route.png)

## Test the agent in the simulator

Your agent and webhook are ready to test with the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator):

  1. Click **Test Agent**.
  2. Enter `I want to buy a large red shirt` and press enter.



Since you provided both a size and color, you gave the agent everything it needs to create a shirt order, so it transitions directly to the **Order Confirmation** page.

![Agent graph screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-webhook-simulator.png)

The following describes the agent responses:

Response | Explanation  
---|---  
Okay, let's start a new order. | When the **New Order** page became active, the entry fulfillment was called. The response was triggered from this fulfillment.  
You have selected a large, red shirt. | When all form parameters have been provided for the **New Order** page, the condition route checking for form completion is called. The response was triggered from the fulfillment for this route. This route also transitions to the **Order Confirmation** page.  
You can pick up your order for a large red shirt in 5 days. | The entry fulfillment for the **Order Confirmation** page calls the webhook. See the `confirm` function in the webhook code. That function creates this text response, and it uses the parameters provided in the webhook request.  
You can cancel your order within 2 days. Goodbye. | The **Order Confirmation** page has a condition route with a condition that is always true. This response is triggered by the fulfillment for that route. Note that the response makes use of the parameter set by the webhook in the webhook response.  
  
[ Previous arrow_back  Build an agent using flows  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent)

[ Next Interactions with an integration  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
