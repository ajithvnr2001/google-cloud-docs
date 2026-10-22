---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/reasoning/
title: Reasoning for Grok Models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:55.285591+00:00
---

# Reasoning for Grok Models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/reasoning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Reasoning for Grok Models Stay organized with collections  Save and categorize content based on your preferences. 

Grok models support a "thinking" mode that allows them to perform step-by-step reasoning before providing a final answer. This is useful for tasks requiring transparent logic, like mathematical proofs, intricate code debugging, or multi-step agent planning.

## Grok guidance

  * The reasoning token count is outputted in the `reasoning_tokens` field, separated from the `completion_tokens`.
  * The response doesn't have the `reasoning_content` field. All response texts are outputted in the `content` field.
  * Grok reasoning models don't support `reasoning_effort`.



_Example request:_
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://aiplatform.googleapis.com/v1/projects/test-project/locations/global/endpoints/openapi/chat/completions -d '{
      "model": "xai/grok-4.1-fast-reasoning",
      "messages": [{
        "role": "user",
        "content": "Who are you?"
      }],
    }'
    

_Example response:_
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "logprobs": null,
          "message": {
            "content": "I am Grok, an AI assistant built by xAI...",
            "role": "assistant"
          }
        }
      ],
      "created": 1775523905,
      "id": "knTMaJC0EJfM5OMP7I3xkAk",
      "model": "xai/grok-4.1-fast-reasoning",
      "object":"chat.completion",
      "system_fingerprint":"fp_39c5j0a324",
      "usage":{
        "completion_tokens":50,
        "completion_tokens_details":{
          "accepted_prediction_tokens":0,
          "audio_tokens":0,
          "reasoning_tokens":124,
          "rejected_prediction_tokens":0
        },
        "cost_in_usd_ticks":0,
        "num_sources_used":0,
        "prompt_tokens":663,
        "prompt_tokens_details":{"audio_tokens":0,"cached_tokens":654,"image_tokens":0,"text_tokens":663},
        "total_tokens":837
      }
    }
    

## What's next

  * Learn about [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/function-calling).
  * Learn about [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/capabilities/structured-output).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
