---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/safety/
title: Safety classifiers for Claude in Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:26.744454+00:00
---

# Safety classifiers for Claude in Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/safety/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Safety classifiers for Claude in Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform includes a safety classifier that filters requests to all hosted Anthropic models that may contain images that include Child Sexual Abuse Material (CSAM). Gemini Enterprise Agent Platform's suspected CSAM safety classifier is separate from the Trust and Safety (T&S) filters shipped directly with Anthropic's models.

This document covers which parts of the request and response that the suspected CSAM safety classifier filters and what happens when the classifier blocks a request.

Safety and content filters act as a barrier to prevent harmful output, but they don't directly influence the model's behavior. To learn more about model steerability, see [System instructions for safety](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/safety-system-instructions).

## Unsafe prompts

The suspected CSAM classifier filters only the images in requests to Anthropic models in Gemini Enterprise Agent Platform. The suspected CSAM classifier doesn't filter the model's outputs.

Requests that trigger the suspected CSAM classifier are blocked and return a `200` HTTP status code with the following message:
    
    
    {
      "promptFeedback": {
        "blockReason": "PROHIBTED_CONTENT"
      }
    }
    

If the request is blocked by the classifier, the request stream is cancelled and the following message is returned:
    
    
    "event": "vertex-block-event",
    "data": {"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"}}
    

## Location availability

The suspected CSAM classifier is available in all [supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#genai-partner-models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
