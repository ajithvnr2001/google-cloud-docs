---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/use-llama/
title: Request Llama predictions \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:41:00.909328+00:00
---

# Request Llama predictions  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/use-llama/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Request Llama predictions Stay organized with collections  Save and categorize content based on your preferences. 

You can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names:

  * For Llama 4 Maverick 17B-128E, use `llama-4-maverick-17b-128e-instruct-maas`
  * For Llama 4 Scout 17B-16E, use `llama-4-scout-17b-16e-instruct-maas`
  * For Llama 3.3 70B, use `llama-3.3-70b-instruct-maas`



To learn how to make streaming and non-streaming calls to Llama models, see [Call MaaS APIs for open models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis).

To see an example of evaluating Llama 3.1 models by using Automatic side-by-side (AutoSxS) evaluation, run the "Evaluate Llama 3.1 models using Agent Platform AutoSxS" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_openai_api_llama3_1.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_openai_api_llama3_1.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_openai_api_llama3_1.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_openai_api_llama3_1.ipynb)

### Before you begin

To use Llama models with Gemini Enterprise Agent Platform, you must perform the following steps. The Agent Platform API (`aiplatform.googleapis.com`) must be enabled to use Gemini Enterprise Agent Platform. If you already have an existing project with the Agent Platform API enabled, you can use that project instead of creating a new project.

**Note:** To use the Llama 4 Model-as-a-Service endpoints, you must accept the end-user license agreement (EULA) on the model card.

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

  8. Go to one of the following Model Garden model cards, then click **Enable** : 
     * [Go to the Llama 4 Maverick 17B-128E model card](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama-4-maverick-17b-128e-instruct-maas)
     * [Go to the Llama 4 Scout 17B-16E model card](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama-4-maverick-17b-128e-instruct-maas)
     * [Go to the Llama 3.3 70B model card](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama-3.3-70b-instruct-maas)



### Make a streaming call to a Llama model

The following sample makes a streaming call to a Llama model.

### REST

After you set up your environment, you can use REST to test a text prompt. The following sample sends a request to the publisher model endpoint. 

Before using any of the request data, make the following replacements: 

  * LOCATION: A region that supports Llama models.
  * MODEL: The model name you want to use.
  * ROLE: The role associated with a message. You can specify a `user` or an `assistant`. The first message must use the `user` role. The models operate with alternating `user` and `assistant` turns. If the final message uses the `assistant` role, then the response content continues immediately from the content in that message. You can use this to constrain part of the model's response.
  * CONTENT: The content, such as text, of the `user` or `assistant` message.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.

  * STREAM: A boolean that specifies whether the response is streamed or not. Stream your response to reduce the end-use latency perception. Set to `true` to stream the response and `false` to return the response all at once.
  * ENABLE_LLAMA_GUARD: A boolean that specifies whether to enable Llama Guard on your inputs and outputs. By default, Llama Guard is enabled and flags responses if it determines they are unsafe.



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions

Request JSON body: 
    
    
    {
      "model": "meta/MODEL",
      "messages": [
        {
          "role": "ROLE",
          "content": "CONTENT"
        }
      ],
      "max_tokens": MAX_OUTPUT_TOKENS,
      "stream": true,
      "extra_body": {
        "google": {
          "model_safety_settings": {
            "enabled": ENABLE_LLAMA_GUARD,
            "llama_guard_settings": {}
          }
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions" | Select-Object -Expand Content

You should receive a JSON response similar to the following.

#### Response
    
    
    data: {
      "choices": [
        {
          "delta": {
            "content": "CONTENT",
            "role": "assistant",
            "refusal: "REFUSAL_REASON" #If using Llama Guard and response was flagged by Llama Guard
          },
          "index": 0
        }
      ],
      "model": "meta/MODEL_NAME",
      "object": "chat.completion.chunk"
    }
    
    data: {
      "choices": [
        {
          "delta": {
            "content": "CONTENT",
            "role": "assistant"
          },
          "finish_reason": "stop",
          "index": 0
        }
      ],
      "model": "meta/MODEL_NAME",
      "object": "chat.completion.chunk",
      "usage": {
        "completion_tokens": 131,
        "prompt_tokens": 14,
        "total_tokens": 145
      }
    }
    

### Make a unary call to a Llama model

The following sample makes a unary call to a Llama model.

### REST

After you set up your environment, you can use REST to test a text prompt. The following sample sends a request to the publisher model endpoint. 

Before using any of the request data, make the following replacements: 

  * LOCATION: A region that supports Llama models.
  * MODEL: The model name you want to use.
  * ROLE: The role associated with a message. You can specify a `user` or an `assistant`. The first message must use the `user` role. The models operate with alternating `user` and `assistant` turns. If the final message uses the `assistant` role, then the response content continues immediately from the content in that message. You can use this to constrain part of the model's response.
  * CONTENT: The content, such as text, of the `user` or `assistant` message.
  * MAX_OUTPUT_TOKENS: Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. 

Specify a lower value for shorter responses and a higher value for potentially longer responses.

  * STREAM: A boolean that specifies whether the response is streamed or not. Stream your response to reduce the end-use latency perception. Set to `true` to stream the response and `false` to return the response all at once.
  * ENABLE_LLAMA_GUARD: A boolean that specifies whether to enable Llama Guard on your inputs and outputs. By default, Llama Guard is enabled and flags responses if it determines they are unsafe.



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions

Request JSON body: 
    
    
    {
      "model": "meta/MODEL",
      "messages": [
        {
          "role": "ROLE",
          "content": "CONTENT"
        }
      ],
      "max_tokens": MAX_OUTPUT_TOKENS,
      "stream": false,
      "extra_body": {
        "google": {
          "model_safety_settings": {
            "enabled": ENABLE_LLAMA_GUARD,
            "llama_guard_settings": {}
          }
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/endpoints/openapi/chat/completions" | Select-Object -Expand Content

You should receive a JSON response similar to the following.

#### Response
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "content": "CONTENT",
            "role": "assistant",
            "refusal: "REFUSAL_REASON" #If using Llama Guard and response was flagged by Llama Guard
          }
        }
      ],
      "model": "meta/llama3-405b-instruct-maas",
      "object": "chat.completion",
      "usage": {
        "completion_tokens": 367,
        "prompt_tokens": 14,
        "total_tokens": 381
      }
    }
    

### Flagged responses

By default, Llama Guard 3 8B is enabled on all predictions that you make with Llama 3.3 and Llama 3.1 models. By default, Llama Guard 3 11B vision is enabled on all predictions that you make with for Llama 3.2 models. Llama Guard helps safeguard responses by checking inputs and outputs. If Llama Guard determines they are unsafe, it flags the response.

If you want to disable Llama Guard, modify the model safety setting. For more information, see the `model_safety_settings` field in the streaming or unary example.

### Use Vertex AI Studio

For Llama models, you can use Vertex AI Studio to quickly prototype and test generative AI models in the Google Cloud console. As an example, you can use Vertex AI Studio to compare Llama model responses with other supported models such as Google's Gemini.

## Llama model region availability and quotas

For Llama models, a quota applies for each region where the model is available. The quota is specified in queries per minute (QPM).

Model | Region | Quotas | Context length  
---|---|---|---  
Llama 4 Maverick 17B-128E  
`us-east5` | 


|  524,288   
Llama 4 Scout 17B-16E  
`us-east5` | 


|  1,310,720   
Llama 3.3 70B  
`us-central1` | 


|  128,000   
  
If you want to increase any of your quotas for Agent Platform, you can use the Google Cloud console to request a quota increase. To learn more about quotas, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
