---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/webhook/
title: Implement webhooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:07.840145+00:00
---

# Implement webhooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/webhook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Implement webhooks Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides various samples for implementing [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) as well as webhook troubleshooting recommendations.

## Set a session parameter

The following samples show how to set a session parameter.

### Go

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

See the [Webhooks quick start](https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook). 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO: Change class name to Example
    // TODO: Uncomment the line below before running cloud function
    // package com.example;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.GsonBuilder;
    import com.google.gson.JsonObject;
    import java.io.BufferedWriter;
    
    public class WebhookConfigureSessionParameters implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        JsonObject orderParameter = new JsonObject();
        orderParameter.addProperty("order_number", "12345");
    
        JsonObject parameterObject = new JsonObject();
        parameterObject.add("parameters", orderParameter);
    
        // Creates webhook response object
        JsonObject webhookResponse = new JsonObject();
        webhookResponse.add("session_info", parameterObject);
    
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String jsonResponseObject = gson.toJson(webhookResponse);
    
        /** { "session_info": { "parameters": { "order_number": "12345" } } } */
        BufferedWriter writer = response.getWriter();
        // Sends the webhookResponseObject
        writer.write(jsonResponseObject.toString());
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('configureSessionParams', (request, response) => {
      // Session parameter configured by the webhook
      const orderNumber = 123;
    
      const jsonResponse = {
        sessionInfo: {
          parameters: {
            orderNumber: orderNumber,
          },
        },
      };
    
      response.send(jsonResponse);
    });

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    # TODO (developer): change entry point to configure_session_params in Cloud Function
    
    
    @functions_framework.http
    def configure_session_params(request):
        """Webhook to validate or configure new session parameters."""
    
        order_number = 123
    
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "orderNumber": order_number,
                },
            },
        }
    
        return json_response
    
    

## Return a fulfillment response

The following samples show how to return a fulfillment response.

**Note:** It is a best practice to set session parameters instead of fulfillment responses. This allows the agent fulfillment to consistently control dynamic responses.

### Go

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

See the [Webhooks quick start](https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook). 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO: Change class name to Example
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
    
    public class BasicWebhook implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        Gson gson = new GsonBuilder().create();
        JsonObject parsedRequest = gson.fromJson(request.getReader(), JsonObject.class);
    
        // For more information on the structure of this object https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment
        String requestTag = parsedRequest.getAsJsonObject("fulfillmentInfo")
            .getAsJsonPrimitive("tag").toString();
        JsonObject responseObject = null;
        String defaultIntent = "\"Default Welcome Intent\"";
        String secondIntent = "\"get-agent-name\"";
        String responseText = "";
    
        // Compares the Intent Tag to provide the correct response 
        if (requestTag.equals(defaultIntent)) {
          responseText = "\"Hello from a Java GCF Webhook\"";
        } else if (requestTag.equals(secondIntent)) {
          responseText = "\"My name is Flowhook\"";
        } else {
          responseText = "\"Sorry I didn't get that\"";
        }
    
        // Constructing the response jsonObject 
        responseObject =
            JsonParser
                .parseString(
                    "{ \"fulfillment_response\": { \"messages\": [ { \"text\": { \"text\": ["
                        + responseText
                        + "] } } ] } }")
                .getAsJsonObject();
        BufferedWriter writer = response.getWriter();
    
        //Sends the responseObject
        writer.write(responseObject.toString());
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('handleWebhook', (request, response) => {
      const tag = request.body.fulfillmentInfo.tag;
      let text = '';
    
      if (tag === 'Default Welcome Intent') {
        text = 'Hello from a GCF Webhook';
      } else if (tag === 'get-name') {
        text = 'My name is Flowhook';
      } else {
        text = `There are no fulfillment responses defined for "${tag}"" tag`;
      }
    
      const jsonResponse = {
        fulfillment_response: {
          messages: [
            {
              text: {
                //fulfillment text response to be sent to the agent
                text: [text],
              },
            },
          ],
        },
      };
    
      response.send(jsonResponse);
    });

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    # TODO(developer): change entry point to handle_webhook in cloud function
    
    
    @functions_framework.http
    def handle_webhook(request):
        req = request.get_json()
    
        tag = req["fulfillmentInfo"]["tag"]
    
        if tag == "Default Welcome Intent":
            text = "Hello from a GCF Webhook"
        elif tag == "get-name":
            text = "My name is Flowhook"
        else:
            text = f"There are no fulfillment responses defined for {tag} tag"
    
        # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
        # Please see https://googleapis.dev/python/dialogflow/latest/dialogflow_v2/types.html?highlight=webhookresponse#google.cloud.dialogflow_v2.types.WebhookResponse for an overview
        res = {"fulfillment_response": {"messages": [{"text": {"text": [text]}}]}}
    
        # Returns json
        return res
    
    

## Set form parameters as required

The following samples show how to flag a parameter as required.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO: Change class name to Example
    // TODO: Uncomment the line below before running cloud function
    // package com.example;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.GsonBuilder;
    import com.google.gson.JsonArray;
    import com.google.gson.JsonObject;
    import java.io.BufferedWriter;
    
    public class ConfigureWebhookToSetFormParametersAsOptionalOrRequired implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        JsonObject parameterObject = new JsonObject();
        parameterObject.addProperty("display_name", "order_number");
        parameterObject.addProperty("required", "true");
        parameterObject.addProperty("state", "VALID");
    
        JsonArray parameterInfoList = new JsonArray();
        parameterInfoList.add(parameterObject);
    
        JsonObject parameterInfoObject = new JsonObject();
        parameterInfoObject.add("parameter_info", parameterInfoList);
    
        JsonObject formInfo = new JsonObject();
        formInfo.add("form_info", parameterInfoObject);
    
        // Constructs the webhook response object
        JsonObject webhookResponse = new JsonObject();
        webhookResponse.add("page_info", formInfo);
    
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String jsonResponseObject = gson.toJson(webhookResponse);
    
        /* {
         *   "page_info": {
         *     "form_info": {
         *       "parameter_info": [
         *         {
         *           "display_name": "order_number",
         *           "required": "true",
         *           "state": "VALID"
         *         }
         *       ]
         *     }
         *   }
         * }
         */
    
        BufferedWriter writer = response.getWriter();
    
        // Sends the responseObject
        writer.write(jsonResponseObject.toString());
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('configureOptionalFormParam', (request, response) => {
      // The value of the parameter that the webhook will set as optional or required.
      // Note that the webhook cannot add or remove any form parameter
    
      const jsonResponse = {
        pageInfo: {
          formInfo: {
            parameterInfo: [
              {
                displayName: 'order-number',
                // if required: false, the agent will not reprompt for this parameter, even if the state is 'INVALID'
                required: true,
                state: 'VALID',
              },
            ],
          },
        },
      };
    
      // Info about form parameter that is sent in the webhook response:
      console.log(
        'Parameter Info: \n',
        jsonResponse.pageInfo.formInfo.parameterInfo[0]
      );
    
      response.send(jsonResponse);
    });

## Validate a form parameter

The following samples show how to validate a form parameter.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO: Change class name to Example
    // TODO: Uncomment the line below before running cloud function
    // package com.example;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.GsonBuilder;
    import com.google.gson.JsonArray;
    import com.google.gson.JsonObject;
    import java.io.BufferedWriter;
    
    public class WebhookValidateFormParameter implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        JsonObject sessionInfo = new JsonObject();
        JsonObject sessionParameter = new JsonObject();
    
        sessionParameter.addProperty("order_number", "null");
        sessionInfo.add("parameters", sessionParameter);
    
        JsonObject parameterObject = new JsonObject();
        parameterObject.addProperty("display_name", "order_number");
        parameterObject.addProperty("required", "true");
        parameterObject.addProperty("state", "INVALID");
        parameterObject.addProperty("value", "123");
    
        JsonArray parameterInfoList = new JsonArray();
        parameterInfoList.add(parameterObject);
    
        JsonObject parameterInfoObject = new JsonObject();
        parameterInfoObject.add("parameter_info", parameterInfoList);
    
        JsonObject pageInfo = new JsonObject();
        pageInfo.add("form_info", parameterInfoObject);
    
        // Constructs the webhook response object
        JsonObject webhookResponse = new JsonObject();
        webhookResponse.add("page_info", pageInfo);
        webhookResponse.add("session_info", sessionInfo);
    
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String jsonResponseObject = gson.toJson(webhookResponse);
    
        /**
         * { "page_info": { "form_info": { "parameter_info": [ { "display_name": "order_number",
         * "required": "true", "state": "INVALID", "value": "123" } ] } }, "session_info": {
         * "parameters": { "order_number": "null" } } }
         */
        BufferedWriter writer = response.getWriter();
    
        // Sends the responseObject
        writer.write(jsonResponseObject.toString());
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('validateParameter', (request, response) => {
      // Webhook will validate or invalidate parameter based on logic configured by the user.
      // Access parameter values through the webhook request via `request.body.pageInfo.formInfo.parameterInfo[]`
      const jsonResponse = {
        page_info: {
          form_info: {
            parameter_info: [
              {
                displayName: 'orderNumber',
                required: true,
                state: 'INVALID',
                value: 123,
              },
            ],
          },
        },
        sessionInfo: {
          parameters: {
            // Set session parameter to null if the form parameter is 'INVALID' and your agent needs to reprompt the user
            orderNumber: null,
          },
        },
      };
    
      response.send(jsonResponse);
    });

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    @functions_framework.http
    def validate_parameter(request):
        """Webhook will validate or invalidate parameter based on logic configured by the user."""
        return {
            "page_info": {
                "form_info": {
                    "parameter_info": [
                        {
                            "displayName": "orderNumber",
                            "required": True,
                            "state": "INVALID",
                            "value": 123,
                        },
                    ],
                },
            },
            "sessionInfo": {
                "parameters": {
                    # Set session parameter to None if the form parameter is 'INVALID' and your agent needs to reprompt the user
                    "orderNumber": None,
                },
            },
        }
    
    

## Log session ID

The following sample shows how to log the `session ID` from a webhook request.

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import re
    
    import functions_framework
    
    
    @functions_framework.http
    def log_session_id_for_troubleshooting(request):
        """Webhook will log session id corresponding to request."""
    
        req = request.get_json()
        # You can read more about SessionInfo at https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/SessionInfo
        # Use a regex pattern to get the session ID
        session_id_regex = r".+\/sessions\/(.+)"
        session = req["sessionInfo"]["session"]
        regex_match = re.search(session_id_regex, session)
        session_id = regex_match.group(1)
    
        # Instead of printing, use the logging tools available to you
        print(f"Debug Node: session ID = {session_id}")
    
        # Return a generic response
        res = {
            "fulfillment_response": {
                "messages": [{"text": {"text": [f"Request Session ID: {session_id}"]}}]
            }
        }
    
        # Returns json
        return res
    
    

## Troubleshooting

### Life of a webhook call

Webhook calls are always initiated by Dialogflow CX and go to a web server through HTTPS. Generic web service webhooks calls originate from an Internet IP address that belongs to Google and can reach web servers (webhook servers) that are available in the public Internet. On the other hand, Service Directory webhooks always start from an internal Google Cloud address and can only reach webhook servers in private networks within Google Cloud.

### Useful logs for debugging webhooks

Debugging webhook issues usually involves gathering the Cloud Logging Dialogflow CX logs and the webhook server logs. If the webhook server is implemented using Cloud Run functions, its logs would be in Cloud Logging. Otherwise, the logs would typically reside where the webhook server runs.

Standard webhook logs contain a `detectIntentResponseId` field with a UUID which can be useful to trace a particular call in webhook servers. This log exists in the Dialogflow CX Cloud Logging logs when Cloud logging is enabled.

### Common webhook issues

Some errors that can be found in the Dialogflow CX logs for webhooks calls are:

#### Webhook server hostname resolution error

Dialogflow CX looked up the hostname of a Generic webhook and the hostname does not exist in the DNS. Make sure the hostname is registered in the public DNS. If the hostname is new, it might take some time for the record to propagate. Cloud Logging message: `State: URL_ERROR, Reason: ERROR_DNS`.

#### Webhook server returns a client-side error

Apart from `ERROR_DNS` this state indicates a 4xx response from the webhook server. This can be an unauthorized status (401 - `ERROR_AUTHENTICATION`) or that the URL was not found in the webhook server (404 - `ERROR_NOT_FOUND`). Cloud Logging message: `State: URL_ERROR`.

#### Dialogflow agent times out before the webhook server returns a response

Dialogflow CX reached the webhook timeout limit before the web server finished. The two possible approaches here are reducing the webhook server processing time or increasing the time Dialogflow CX waits for the webhook. Reducing the processing time usually brings best results although it is non-trivial in many cases. Consider that there is maximum time out limit for webhooks and that end callers or users would need to wait for longer to get an answer from the agent before increasing this setting. Cloud Logging message: `State: URL_TIMEOUT, Reason: TIMEOUT_WEB`.

#### gRPC times out before the webhook server returns a response

The time limit set by gRPC in the Dialogflow CX API call was reached before the webhook call finished. This limit is set usually at the integration level and is independent of the Dialogflow CX parameters and webhook timeout limits. For more information on gRPC deadlines see <https://grpc.io/docs/guides/deadlines/>. Cloud Logging message: `State: URL_REJECTED, Reason: REJECTED_DEADLINE_EXCEEDED`.

#### Dialogflow couldn't contact the webhook server

The webhook server couldn't be reached because of a network error or the connection was established and the webhook server returned HTTP status 5xx indicating an issue while it was processing the request. Make sure Dialogflow CX can reach the webhook server address at the networking level. If the request appears in the webhook server logs, find why the call returned a 5xx error. Cloud Logging message: `State: URL_UNREACHABLE`.

### Tracing webhook calls

A standard webhook call can be correlated between the Dialogflow CX and a webhook server using the session ID, `detectIntentResponse` ID, the trace ID for Cloud Run functions and a timestamp of the call. Flexible webhook tracing can be done using the timestamp of the call and the session parameter values specified in the webhook definition at design time. For more information on standard and flexible webhooks requests, see [Webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook).

The session ID appears in the `sessionInfo.session` field of the [WebhookRequest](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-request). This session ID should be unique for each conversation, and it can help you compare agent logs against webhook logs for requests using the same session ID. The previous Log session ID section shows how to log the session ID from a webhook.

In addition, if you are hosting your webhook on [Cloud Run functions](https://docs.cloud.google.com/functions) or a similar Google Cloud serverless option, you can use the `trace` field from [log entries](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as a log filter. A single execution of a function results in multiple log entries with the same trace value.

The next example uses both the session ID and the trace value to associate a particular Dialogflow CX agent error log with the corresponding Cloud Run functions webhook log entries. The example uses [Cloud Logging Filters](https://docs.cloud.google.com/logging/docs/view/building-queries) for an agent that has enabled [Cloud Logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging#enable).

### 1\. Filter Dialogflow CX logs for a particular agent's error logs

Use the following Cloud Logging filter to filter your Dialogflow CX logs for a particular agent's error logs:
    
    
    labels.location_id="global"
    labels.agent_id="AGENT_ID"
    severity=ERROR
    

A webhook log error entry looks like the following:
    
    
    {
      "insertId": "-j4gkkre31e2o",
      "jsonPayload": {
        "code": 14,
        "message": "Error calling webhook 'https://us-central1-PROJECT_ID.cloudfunctions.net/function-webhook': State: URL_UNREACHABLE, Reason: UNREACHABLE_5xx, HTTP status code: 500"
      },
      "labels": {
        "agent_id": "e9e01392-1351-42dc-9b15-b583fb2d2881",
        "environment_id": "",
        "location_id": "global",
        "session_id": "07c899-a86-78b-a77-569625b37"
      },
      "logName": "projects/PROJECT_ID/logs/dialogflow-runtime.googleapis.com%2Frequests",
      "receiveTimestamp": "2024-10-28T21:49:04.288439054Z",
      "resource": {
        "labels": {
          "project_id": "PROJECT_ID"
        },
        "type": "global",
      },
      "severity": "ERROR",
      "timestamp": "2024-10-28T21:49:04.132548Z"
    }
    

Note the `labels.session_id` field which contains the session ID. You will use the session ID in the next step.

### 2\. Filter Cloud Run functions logs by session ID

Use the following Cloud Logging filter to filter your Cloud Run functions logs by session ID:

**Note:** This filter assumes you have logged the session ID using the exact same text as in the preceding Log session ID sample.
    
    
    resource.type = "cloud_run_revision"
    resource.labels.service_name = "CLOUD_RUN_FUNCTION_NAME"
    resource.labels.location = "CLOUD_RUN_FUNCTION_REGION"
    textPayload="Debug Node: session ID = SESSION_ID"
    

The resulting logs correspond to webhook logs made during the provided [session](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session). For example:
    
    
    {
      "insertId": "671c42940007ebebdbb1d56e",
      "labels": {
        "execution_id": "pgy8jvvblovs",
        "goog-managed-by": "cloudfunctions",
        "instance_id": "004940b3b8e3d975a4b11a4ed7d1ded4ce3ed37467ffc5e2a8f13a1908db928f8200b01cc554a5eda66ffc9d23d76dd75cec1619a07cb5751fa2e8a93bc6cfc3df86dfa0650a"
      },
      "logName": "projects/PROJECT_ID/logs/run.googleapis.com%2Fstdout",
      "receiveTimestamp": "2024-10-26T01:15:00.523313187Z",
      "resource": {
        "labels": {
          "configuration_name": "function-webhook",
          "location": "us-central1",
          "project_id": "PROJECT_ID",
          "revision_name": "function-webhook-00001-jiv",
          "service_name": "function-webhook",
        },
        "type": "cloud_run_revision"
      },
      "spanId": "6938366936362981595",
      "trace": "d1b54fbc8945dd59bdcaed37d7d5e185",
      "textPayload": "Debug Node: session ID = 07c899-a86-78b-a77-569625b37",
      "timestamp": "2024-10-26T01:15:00.519147Z"
    }
    

Note the `trace` field which is used in the next step.

### 3\. Filter Cloud Function logs for a particular trace

Use the following Cloud Logging filter to filter Cloud Function logs for a particular trace:
    
    
    resource.type = "cloud_run_revision"
    resource.labels.service_name = "CLOUD_RUN_FUNCTION_NAME"
    resource.labels.location = "CLOUD_RUN_FUNCTION_REGION"
    trace="projects/PROJECT_ID/traces/TRACE_ID"
    

where `TRACE_ID` is the last segment of trace. For example the `TRACE_ID` for `projects/PROJECT_ID/traces/e41eefc1fac48665b442bfa400cc2f5e` is `e41eefc1fac48665b442bfa400cc2f5e`.

The result is the webhook server log generated during the execution of the webhook request associated with the session ID from step 1 and with the trace from step 2. The log would look like the following.
    
    
    {
      "insertId": "671c42940008465e29f5faf0",
      "httpRequest": {
        "requestMethod": "POST",
        "requestUrl": "https://us-central1-TEST_PROJECT.cloudfunctions.net/function-webhook",
        "requestSize": "2410",
        "status": 200,
        "responseSize": "263",
        "userAgent": "Google-Dialogflow",
        "remoteIp": "8.34.210.1",
        "serverIp": "216.239.36.1",
        "latency": "0.166482342s",
        "protocol": "HTTP/1.1"
      },
      "resource": {
        "type": "cloud_run_revision",
        "labels": {
          "project_id": "PROJECT_ID",
          "service_name": "function-webhook",
          "location": "us-central1",
          "revision_name": "function-webhook-00001-jiv",
          "configuration_name": "function-webhook"
        }
      },
      "timestamp": "2024-10-26T01:15:00.352197Z",
      "severity": "INFO",
      "labels": {
        "instanceId": "004940b3b813af8a656c92aac1bd07ffad5165f1353e1e346b6161c14bcde225f68f4a88ceedc08aa9020f387b1b59471f73de45f2882a710ced37dea921f05ad962347690be",
        "goog-managed-by": "cloudfunctions"
      },
      "logName": "projects/test-project-12837/logs/run.googleapis.com%2Frequests",
      "trace": "projects/test-project-12837/traces/d1b54fbc8945dd59bdcaed37d7d5e185",
      "receiveTimestamp": "2024-10-26T01:15:00.548931586Z",
      "spanId": "604a07f7b33b18db",
      "traceSampled": true
    }
    

[ Previous arrow_back  Detect intent  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/detect-intent-stream)

[ Next Manage agents with the API  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/agent-create-api)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
