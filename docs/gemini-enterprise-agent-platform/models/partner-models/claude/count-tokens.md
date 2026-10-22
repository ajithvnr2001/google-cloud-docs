---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/count-tokens/
title: Count tokens for Claude models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:53.979136+00:00
---

# Count tokens for Claude models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/count-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Count tokens for Claude models Stay organized with collections  Save and categorize content based on your preferences. 

The `count-tokens` endpoint lets you determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage.

There is no cost for using the `count-tokens` endpoint.

## Supported Claude models

The following models support count tokens:

  * [Anthropic's Claude Sonnet 5.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-sonnet-5-5)
  * [Anthropic's Claude Fable 5.1 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-fable-5-1)
  * [Anthropic's Claude Sonnet 5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-sonnet-5)
  * [Anthropic's Claude Opus 5.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-5-5)
  * [Anthropic's Claude Opus 5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-5)
  * [Anthropic's Claude Fable 5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-fable-5)
  * [Anthropic's Claude Opus 4.8 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-4-8)
  * [Anthropic's Claude Opus 4.7 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-4-7)
  * [Anthropic's Claude Opus 4.6 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-4-6)
  * [Anthropic's Claude Sonnet 4.6 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-sonnet-4-6)
  * [Anthropic's Claude Opus 4.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-opus-4-5)
  * [Anthropic's Claude Sonnet 4.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-sonnet-4-5)
  * [Anthropic's Claude Haiku 5.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-haiku-5-5)
  * [Anthropic's Claude Haiku 4.5 on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-haiku-4-5)
  * [Claude 3.5 Haiku on Google Cloud](https://console.cloud.google.com/agent-platform/publishers/anthropic/model-garden/claude-3-5-haiku)



## Supported regions

The following regions support count tokens:

  * `global`
  * `us`
  * `eu`
  * `asia-southeast1`



## Count tokens in basic messages

To count tokens, send a `rawPredict` request to the `count-tokens` endpoint. The body of the request must contain the model ID of the model you want to count tokens against.

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: A region that supports Anthropic Claude models. To use the global endpoint, see [Specify the global endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models#global).
  * MODEL: The model to count tokens against.
  * ROLE: The role associated with a message. You can specify a `user` or an `assistant`. The first message must use the `user` role. Claude models operate with alternating `user` and `assistant` turns. If the final message uses the `assistant` role, then the response content continues immediately from the content in that message. You can use this to constrain part of the model's response.
  * CONTENT: The content, such as text, of the `user` or `assistant` message.



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/anthropic/models/count-tokens:rawPredict

Request JSON body: 
    
    
    {
      "model": "MODEL",
      "messages": [
        {
          "role": "user",
          "content":"how many tokens are in this request?"
        }
      ],
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/anthropic/models/count-tokens:rawPredict"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/anthropic/models/count-tokens:rawPredict" | Select-Object -Expand Content

You should receive a JSON response similar to the following.

#### Response
    
    
    { "input_tokens": 14 }
    

For information on how to count tokens in messages with tools, images, and PDFs, see [Anthropic's documentation](https://docs.anthropic.com/en/docs/build-with-claude/token-counting).

## Quotas

By default, the quota for the `count-tokens` endpoint is 2000 requests per minute.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
