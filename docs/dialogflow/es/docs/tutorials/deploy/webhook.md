---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/webhook/
title: Create a webhook service \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:34.171198+00:00
---

# Create a webhook service  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Create a webhook service Stay organized with collections  Save and categorize content based on your preferences. 

The prebuilt agent you created in the last step cannot provide dynamic data like account balances, because everything is hardcoded into the agent. In this step of the tutorial, you will create a [webhook](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-overview) that can provide dynamic data to the agent. [Cloud Run functions](https://docs.cloud.google.com/functions/docs) are used to host the webhook in this tutorial due to their simplicity, but there are many other ways that you could host a webhook service. The example also uses the Go programming language, but you can use any [language supported by Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/exec).

## Create the Function

Cloud Run functions can be created with the Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), [open console](https://console.cloud.google.com/)). To create a function for this tutorial:

  1. It is important that your Dialogflow agent and the function are both in the same project. This is the easiest way for Dialogflow to have [secure access to your function](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook#gcf). Before creating the function, select your project from the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Open the Cloud Run functions overview page.

[Go to Cloud Run functions overview](https://console.cloud.google.com/functions/list)

  3. Click **Create Function** , and set the following fields:

     * **Environment** : 1st gen
     * **Function name** : tutorial-banking-webhook
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
         
         package estwh
         
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
         
         type queryResult struct {
         	Action     string         `json:"action"`
         	Parameters map[string]any `json:"parameters"`
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
         
         // accountBalanceCheck handles the similar named action
         func accountBalanceCheck(ctx context.Context, request webhookRequest) (
         	webhookResponse, error) {
         	account := request.QueryResult.Parameters["account"].(string)
         	account = strings.ToLower(account)
         	var table string
         	if account == "savings account" {
         		table = "Savings"
         	} else {
         		table = "Checking"
         	}
         	s := "Your balance is $0"
         	if client != nil {
         		// A Spanner client exists, so access the database.
         		// See: https://pkg.go.dev/cloud.google.com/go/spanner#ReadOnlyTransaction.ReadRow
         		row, err := client.Single().ReadRow(ctx,
         			table,
         			spanner.Key{1}, // The account ID
         			[]string{"Balance"})
         		if err != nil {
         			if spanner.ErrCode(err) == codes.NotFound {
         				log.Printf("Account %d not found", 1)
         			} else {
         				return webhookResponse{}, err
         			}
         		} else {
         			// A row was returned, so check the value
         			var balance int64
         			err := row.Column(0, &balance)
         			if err != nil {
         				return webhookResponse{}, err
         			}
         			s = fmt.Sprintf("Your balance is $%.2f", float64(balance)/100.0)
         		}
         	}
         	response := webhookResponse{
         		FulfillmentMessages: []message{
         			{
         				Text: text{
         					Text: []string{s},
         				},
         			},
         		},
         	}
         	return response, nil
         }
         
         // Define a type for handler functions.
         type handlerFn func(ctx context.Context, request webhookRequest) (
         	webhookResponse, error)
         
         // Create a map from action to handler function.
         var handlers map[string]handlerFn = map[string]handlerFn{
         	"account.balance.check": accountBalanceCheck,
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
         
         	// Get the action from the request, and call the corresponding
         	// function that handles that action.
         	action := request.QueryResult.Action
         	if fn, ok := handlers[action]; ok {
         		response, err = fn(r.Context(), request)
         	} else {
         		err = fmt.Errorf("Unknown action: %s", action)
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

Now that the webhook exists as a service, you need to associate this webhook with your agent. This is done via fulfillment. To enable and manage fulfillment for your agent:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select the pre-built agent you just created.
  3. Select **Fulfillment** in the left sidebar menu.
  4. Toggle the **Webhook** field to **Enabled**.
  5. Provide the URL that you copied from above. Leave all other fields blank.
  6. Click **Save** at the bottom of the page.



![Screenshot of enabling fulfillment.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/fulfillment-webhook-form.png)

Now that fulfillment is enabled for the agent, you need to enable fulfillment for an intent:

  1. Select **Intents** in the left sidebar menu.
  2. Select the **account.balance.check** intent.
  3. Scroll down to the **Fulfillment** section.
  4. Toggle **Enable webhook call for this intent** to on.
  5. Click **Save**.



## Try the agent

Your agent is now ready to try. Click the **Test Agent** button to open the simulator. Attempt to have the following conversation with the agent:

Conversational turn | You | Agent  
---|---|---  
1 | Hello | Hello, thanks for choosing ACME Bank.  
2 | I want to know my account balance | What account do you want the balance for: savings or checking?  
3 | Checking | Here's your latest balance: $0.00  
  
At conversational turn #3, you supplied "checking" as the account type. The **account.balance.check** intent has a parameter called **account**. This parameter is set to "checking" in this conversation. The intent also has an action value of "account.balance.check". The webhook service is called, and it is passed the parameter and action values.

If you examine the webhook code above, you see that this action triggers a similar named function to be called. The function determines the account balance. The function checks whether specific environment variables are set with information for connecting to the database. If these environment variables are not set, the function uses a hardcoded account balance. In upcoming steps, you will alter the environment for the function so that it retrieves data from a database.

## Troubleshooting

The webhook code includes logging statements. If you are having issues, try viewing the logs for your function.

## More information

For more information about the steps above, see:

  * [Cloud Run functions Go quickstart](https://docs.cloud.google.com/functions/docs/console-quickstart-1st-gen)



[ Previous arrow_back  Create a prebuilt agent  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/prebuilt)

[ Next Query a database  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/database)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
