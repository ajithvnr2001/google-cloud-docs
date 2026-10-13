---
url: https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/webhook/
title: Create a webhook service \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:58.686383+00:00
---

# Create a webhook service  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/webhook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Create a webhook service Stay organized with collections  Save and categorize content based on your preferences. 

The prebuilt agent you created in the last step requires a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook). [Cloud Run functions](https://docs.cloud.google.com/functions/docs) are used to host the webhook in this tutorial due to their simplicity, but there are many other ways that you could host a webhook service. The example also uses the Go programming language, but you can use any [language supported by Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/exec).

## Create the Function

Cloud Run functions can be created with the Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), [open console](https://console.cloud.google.com/)). To create a function for this tutorial:

  1. It is important that your Dialogflow agent and the function are both in the same project. This is the easiest way for Dialogflow to have [secure access to your function](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#cloud-run). Before creating the function, select your project from the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Open the Cloud Run functions overview page.

[Go to Cloud Run functions overview](https://console.cloud.google.com/functions/list)

  3. Click **Create Function** , and set the following fields:

     * **Environment** : 1st gen
     * **Function name** : tutorial-telecommunications-webhook
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
         
         package cxtwh
         
         import (
         	"context"
         	"encoding/json"
         	"fmt"
         	"log"
         	"net/http"
         	"os"
         	"strings"
         
         	"cloud.google.com/go/spanner"
           "google.golang.org/grpc/codes"
         )
         
         // client is a Spanner client, created only once to avoid creation
         // for every request.
         // See: https://cloud.google.com/functions/docs/concepts/go-runtime#one-time_initialization
         var client *spanner.Client
         
         func init() {
         	// If using a database, these environment variables will be set.
         	pid := os.Getenv("PROJECT_ID")
         	iid := os.Getenv("SPANNER_INSTANCE_ID")
         	did := os.Getenv("SPANNER_DATABASE_ID")
         	if pid != "" && iid != "" && did != "" {
         		db := fmt.Sprintf("projects/%s/instances/%s/databases/%s",
         			pid, iid, did)
         		log.Printf("Creating Spanner client for %s", db)
         		var err error
         		// Use the background context when creating the client,
         		// but use the request context for calls to the client.
         		// See: https://cloud.google.com/functions/docs/concepts/go-runtime#contextcontext
         		client, err = spanner.NewClient(context.Background(), db)
         		if err != nil {
         			log.Fatalf("spanner.NewClient: %v", err)
         		}
         	}
         }
         
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
         
         // detectCustomerAnomaly handles same-named tag.
         func detectCustomerAnomaly(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	// Create session parameters that are populated in the response.
         	// This example hard codes values, but a real system
         	// might look up this value in a database.
         	p := map[string]any{
         		"anomaly_detect":        "false",
         		"purchase":              "device protection",
         		"purchase_amount":       "12.25",
         		"bill_without_purchase": "54.34",
         		"total_bill":            "66.59",
         		"first_month":           "January 1",
         	}
         	// Build and return the response.
         	response := webhookResponse{
         		SessionInfo: sessionInfo{
         			Parameters: p,
         		},
         	}
         	return response, nil
         }
         
         // validatePhoneLine handles same-named tag.
         func validatePhoneLine(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	// Create session parameters that are populated in the response.
         	// This example hard codes values, but a real system
         	// might look up this value in a database.
         	p := map[string]any{
         		"domestic_coverage":   "true",
         		"phone_line_verified": "true",
         	}
         	// Build and return the response.
         	response := webhookResponse{
         		SessionInfo: sessionInfo{
         			Parameters: p,
         		},
         	}
         	return response, nil
         }
         
         // cruisePlanCoverage handles same-named tag.
         func cruisePlanCoverage(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	// Get the existing parameter values
         	port := request.SessionInfo.Parameters["destination"].(string)
         	port = strings.ToLower(port)
         	// Check if the port is covered
         	covered := "false"
         	if client != nil {
         		// A Spanner client exists, so access the database.
         		// See: https://pkg.go.dev/cloud.google.com/go/spanner#ReadOnlyTransaction.ReadRow
         		row, err := client.Single().ReadRow(ctx,
         			"Destinations",
         			spanner.Key{port},
         			[]string{"Covered"})
         		if err != nil {
         			if spanner.ErrCode(err) == codes.NotFound {
         				log.Printf("Port %s not found", port)
         			} else {
         				return webhookResponse{}, err
         			}
         		} else {
         			// A row was returned, so check the value
         			var c bool
         			err := row.Column(0, &c)
         			if err != nil {
         				return webhookResponse{}, err
         			}
         			if c {
         				covered = "true"
         			}
         		}
         	} else {
         		// No Spanner client exists, so use hardcoded list of ports.
         		coveredPorts := map[string]bool{
         			"anguilla": true,
         			"canada":   true,
         			"mexico":   true,
         		}
         		_, ok := coveredPorts[port]
         		if ok {
         			covered = "true"
         		}
         	}
         	// Create session parameters that are populated in the response.
         	// This example hard codes values, but a real system
         	// might look up this value in a database.
         	p := map[string]any{
         		"port_is_covered": covered,
         	}
         	// Build and return the response.
         	response := webhookResponse{
         		SessionInfo: sessionInfo{
         			Parameters: p,
         		},
         	}
         	return response, nil
         }
         
         // internationalCoverage handles same-named tag.
         func internationalCoverage(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	// Get the existing parameter values
         	destination := request.SessionInfo.Parameters["destination"].(string)
         	destination = strings.ToLower(destination)
         	// Hardcoded list of covered international monthly destinations
         	coveredMonthly := map[string]bool{
         		"anguilla":  true,
         		"australia": true,
         		"brazil":    true,
         		"canada":    true,
         		"chile":     true,
         		"england":   true,
         		"france":    true,
         		"india":     true,
         		"japan":     true,
         		"mexico":    true,
         		"singapore": true,
         	}
         	// Hardcoded list of covered international daily destinations
         	coveredDaily := map[string]bool{
         		"brazil":    true,
         		"canada":    true,
         		"chile":     true,
         		"england":   true,
         		"france":    true,
         		"india":     true,
         		"japan":     true,
         		"mexico":    true,
         		"singapore": true,
         	}
         	// Check coverage
         	coverage := "neither"
         	_, monthly := coveredMonthly[destination]
         	_, daily := coveredDaily[destination]
         	if monthly && daily {
         		coverage = "both"
         	} else if monthly {
         		coverage = "monthly_only"
         	} else if daily {
         		coverage = "daily_only"
         	}
         	// Create session parameters that are populated in the response.
         	// This example hard codes values, but a real system
         	// might look up this value in a database.
         	p := map[string]any{
         		"coverage": coverage,
         	}
         	// Build and return the response.
         	response := webhookResponse{
         		SessionInfo: sessionInfo{
         			Parameters: p,
         		},
         	}
         	return response, nil
         }
         
         // cheapestPlan handles same-named tag.
         func cheapestPlan(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	// Create session parameters that are populated in the response.
         	// This example hard codes values, but a real system
         	// might look up this value in a database.
         	p := map[string]any{
         		"monthly_cost":   70,
         		"daily_cost":     100,
         		"suggested_plan": "monthly",
         	}
         	// Build and return the response.
         	response := webhookResponse{
         		SessionInfo: sessionInfo{
         			Parameters: p,
         		},
         	}
         	return response, nil
         }
         
         // Define a type for handler functions.
         type handlerFn func(ctx context.Context, request webhookRequest) (
         	webhookResponse, error)
         
         // Create a map from tag to handler function.
         var handlers map[string]handlerFn = map[string]handlerFn{
         	"detectCustomerAnomaly": detectCustomerAnomaly,
         	"validatePhoneLine":     validatePhoneLine,
         	"cruisePlanCoverage":    cruisePlanCoverage,
         	"internationalCoverage": internationalCoverage,
         	"cheapestPlan":          cheapestPlan,
         }
         
         // handleError handles internal errors.
         func handleError(w http.ResponseWriter, err error) {
         	log.Printf("ERROR: %v", err)
         	http.Error(w,
         		fmt.Sprintf("ERROR: %v", err),
         		http.StatusInternalServerError)
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
         	tag := request.FulfillmentInfo.Tag
         	if fn, ok := handlers[tag]; ok {
         		response, err = fn(r.Context(), request)
         	} else {
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

  9. Wait until the status indicator shows that the function has successfully deployed. While waiting, examine the code you just deployed.




## Configure the webhook for your agent

Now that the webhook exists as a service, you will associate this webhook with your agent. To configure the webhook for your agent:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Webhooks**.
  6. Click the existing webhook (created by the prebuilt agent).
  7. Update the **Webhook URL** to the webhook URL you saved when creating the function.
  8. Set the **Subtype** to Standard.
  9. Click **Save**.



## Try the agent

Your agent is now ready to try. Click the **Test Agent** button to open the simulator. Attempt to have the following conversation with the agent:

Conversational turn | You | Agent  
---|---|---  
1 | Hello | Hi! I'm the virtual telecommunications agent. I can help you resolve billing and plan questions, troubleshoot, and add travel and cruise plans. How can I assist you today?  
2 | I want to add a cruise plan | Let me take a look for you. What is your phone number with us?  
3 | 123-123-1234 | How many days is your cruise?  
4 | 7 | Option 1 includes talk and text. It costs $[XX]/day. More info here [URL]. Option 2 includes talk, text and data. It costs $[XX]/day. More info here [URL]. Which cruise plan would you like to add?  
5 | Option 1 | Got it. I've added that plan to your account. While on your cruise, you may also need coverage on land. What port will you be stopping at?  
6 | Mexico | And, how many days are you spending there?  
7 | 3 | Great news! Mexico has free coverage on land. You're all set. Is there anything else I can help you with today?  
  
This particular conversation was managed by the `Cruise Plan` flow.

At conversational turn #6, you provided "Mexico" as your destination port. The destination port and the number of days there are captured as the `destination` and `trip_duration` form parameters of the `Collect Port` page. Browse your agent to find these parameter definitions.

![Screenshot of Collect Port page in Dialogflow counsole](https://docs.cloud.google.com/static/dialogflow/cx/docs/tutorials/deploy/images/collect-port.png)

In the `Collect Port` page, there is a condition route for form completion: `$page.params.status = "FINAL"`. Once the two form parameters have been provided, this route is called. This route calls your webhook and provides the `cruisePlanCoverage` tag to your webhook. If you examine the webhook code above, you see that this tag triggers the same named function to be called.

This function determines whether the provided destination is covered by the plan. The function checks whether specific environment variables are set with information for connecting to the database. If these environment variables are not set, the function uses a hardcoded list of destinations. In upcoming steps, you will alter the environment for the function so that it retrieves data from a database in order to validate plan coverage for destinations.

## Troubleshooting

The webhook code includes logging statements. If you are having issues, try viewing the logs for your function.

## More information

For more information about the steps above, see:

  * [Cloud Run functions Go quickstart](https://docs.cloud.google.com/functions/docs/console-quickstart-1st-gen)



[ Previous arrow_back  Create a prebuilt agent  ](https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/prebuilt)

[ Next Query a database  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/database)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
