---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/responses/
title: Call Responses API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:29.946504+00:00
---

# Call Responses API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Call Responses API Stay organized with collections  Save and categorize content based on your preferences. 

XAI's Grok models on Gemini Enterprise Agent Platform support the [Responses API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints.responses) for generating responses.

This page shows how to make calls to Grok models using the Responses API.

## Before you begin

To use Grok models with Gemini Enterprise Agent Platform, you must perform the following steps. The Gemini Enterprise Agent Platform API (`aiplatform.googleapis.com`) must be enabled.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)


**Note:** Setting `store` to `true` and the `previous_response_id` parameter for stateful API calls are not supported for Grok models at this time, and `store` defaults to `false`. Support is planned for an upcoming release. When support is added, the default behavior will change to `store: true`, and `previous_response_id` will be enabled. If you want to prevent your responses from being stored after this change, explicitly set `store` to `false` (or `False` in Python) in your requests. 

## Make a non-streaming call to the Responses API

The following samples show how to make a non-streaming call to the Responses API:

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

Before running this sample, make sure to set the `OPENAI_BASE_URL` environment variable or set up oauth credentials. For more information, see [Authentication and credentials](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/auth-and-credentials).
    
    
    from openai import OpenAI
    client = OpenAI()
    response = client.responses.create(
        model="MODEL",
        input="INPUT",
        max_output_tokens=MAX_OUTPUT_TOKENS,
        stream=False,
    )
    print(response)

  * MODEL: The model name you want to use, for example `xai/grok-4.20-reasoning`.
  * INPUT: The prompt or input for the model.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.




### REST

After you set up your environment, you can use REST to test a text prompt. The following sample sends a request to the publisher model endpoint. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * MODEL: The model name you want to use, for example `xai/grok-4.20-reasoning`.
  * INPUT: The prompt or input for the model.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.




HTTP method and URL: 
    
    
    POST https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses

Request JSON body: 
    
    
    {
      "model": "MODEL",
      "input": "INPUT",
      "max_output_tokens": MAX_OUTPUT_TOKENS,
      "stream": false
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses" | Select-Object -Expand Content

The following example shows a complete curl request:
    
    
    curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses" \
      -d '{
        "model": "xai/grok-4.20-reasoning",
        "input": "Explain black holes in one short sentence.",
        "max_output_tokens": 100,
        "stream": false
      }'

Based on the Responses API definition, a non-streaming response will contain a unique ID, model metadata, usage statistics, and an output array containing the generated text.
    
    
    {
      "background": false,
      "completed_at": 1778892918,
      "created_at": 1778892916,
      "error": null,
      "frequency_penalty": 0,
      "id": "c8AHavnIMP6UifEPgIfcgAg",
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": null,
      "max_tool_calls": null,
      "metadata": {
        "system_fingerprint": "fp_39c5j0a3e9"
      },
      "model": "MODEL",
      "object": "response",
      "output": [
        {
          "content": [
            {
              "annotations": [],
              "logprobs": [],
              "text": "OUTPUT_TEXT",
              "type": "output_text"
            }
          ],
          "id": "msg_c8AHavnIMP6UifEPgIfcgAg",
          "role": "assistant",
          "status": "completed",
          "type": "message"
        }
      ],
      "parallel_tool_calls": true,
      "presence_penalty": 0,
      "previous_response_id": null,
      "prompt_cache_key": null,
      "reasoning": {
        "effort": "medium",
        "summary": "detailed"
      },
      "safety_identifier": null,
      "service_tier": "default",
      "status": "completed",
      "store": false,
      "temperature": 0.7,
      "text": {
        "format": {
          "type": "text"
        }
      },
      "tool_choice": "auto",
      "tools": [],
      "top_logprobs": 0,
      "top_p": 0.95,
      "truncation": "disabled",
      "usage": {
        "extra_properties": {
          "google": {
            "traffic_type": "ON_DEMAND"
          }
        },
        "input_tokens": 335,
        "input_tokens_details": {
          "cached_tokens": 320
        },
        "num_server_side_tools_used": 0,
        "num_sources_used": 0,
        "output_tokens": 305,
        "output_tokens_details": {
          "reasoning_tokens": 284
        },
        "total_tokens": 640
      },
      "user": null
    }
    

## Make a streaming call to the Responses API

The following samples show how to make a streaming call to the Responses API: 

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

Before running this sample, make sure to set the `OPENAI_BASE_URL` environment variable or set up oauth credentials. For more information, see [Authentication and credentials](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/auth-and-credentials).
    
    
    from openai import OpenAI
    client = OpenAI()
    stream = client.responses.create(
        model="MODEL",
        input="INPUT",
        max_output_tokens=MAX_OUTPUT_TOKENS,
        stream=True,
    )
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="")

  * MODEL: The model name you want to use, for example `xai/grok-4.20-reasoning`.
  * INPUT: The prompt or input for the model.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.




### REST

After you set up your environment, you can use REST to test a text prompt. The following sample sends a request to the publisher model endpoint. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * MODEL: The model name you want to use, for example `xai/grok-4.20-reasoning`.
  * INPUT: The prompt or input for the model.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.




HTTP method and URL: 
    
    
    POST https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses

Request JSON body: 
    
    
    {
      "model": "MODEL",
      "input": "INPUT",
      "max_output_tokens": MAX_OUTPUT_TOKENS,
      "stream": true
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/endpoints/openapi/responses" | Select-Object -Expand Content

## What's next

  * Learn more about [Grok models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok).
  * Learn how to use [Function calling with the Responses API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/function-calling#responses-api).
  * Learn how to use [Structured output with the Responses API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/structured-output#responses-api). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
