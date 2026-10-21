---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:54.762885+00:00
---

# Security bulletins  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Agent Platform.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/feeds/generative-ai-on-vertex-ai-security-bulletins.xml`



## GCP-2025-059

**Published** : 2025-10-21

**Updated:** 2025-10-22

Description | Severity | Notes  
---|---|---  
**2025-10-22 Update:** Added link to CVE. 

* * *

On September 23, 2025, we discovered a technical issue in the Gemini Enterprise API that resulted in a limited amount of responses being misrouted between recipients for certain third-party models when using streaming requests. This issue is now resolved. Google models, e.g. Gemini, were _not_ impacted.  Some internal proxies did not properly handle HTTP requests that have an `Expect: 100-continue` header, resulting in a desynchronization in a streaming response connection, where a response intended for one request was instead delivered as the response for a subsequent request.  **What should I do?** We have implemented fixes to properly address the presence of the `Expect: 100-continue` header, and prevent recurrence of this issue. We have also added testing, monitoring, and alerting so that we can quickly detect an occurrence of this issue to prevent regression. There is no action for customers to take at this time to prevent the unintended behavior from occurring.  The fixes were rolled out for different models on separate schedules, with Anthropic models being remediated by Sep. 26, 12:45 AM PDT and all surfaces remediated by Sep. 28, 07:10 PM PDT. Affected models on Gemini Enterprise API and the time of resolution are listed below: 

  * Anthropic [Partner Model-as-a-Service models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models) (Claude) 
    * The issue has been fixed as of September 26, 2025, at 12:45 AM PDT. 
  * All [Open Model-as-a-Service models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/use-open-models), including: DeepSeek (R1-0528 and V3.1), OpenAI (gpt-oss-120b and gpt-oss-20b), Qwen (Next Instruct 80B, Next Thinking 80B, Qwen 3 Coder, and Qwen 3 235B), Llama (Maverick, Scout, 3.3, 3.2, 3.1 405b, 3.1 70b, and 3.1 8b) 
    * The issue has been fixed as of September 28, 2025, at 2:43 AM PDT. 
  * Mistral and AI21 [Partner Model-as-a-Service models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models)
    * The issue has been fixed as of September 28, 2025, at 11:00 AM PDT. 
  * [Self-deployed models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models) for which the 'StreamRawPredict', 'ChatCompletions', 'GenerateContent', or 'StreamGenerateContent' method was invoked using [public endpoints](https://docs.cloud.google.com/vertex-ai/docs/predictions/create-public-endpoint)
    * The issue has been fixed as of September 28, 2025, at 7:10 PM PDT. 
    * Neither [dedicated](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-dedicated-endpoints) (the default on Model Garden) nor private endpoints were impacted. 

| Medium |  [CVE-2025-11915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-11915)  
  
## GCP-2024-063

**Published** : 2024-12-06

Description | Severity | Notes  
---|---|---  
A vulnerability was discovered in the Agent Platform API serving Gemini multimodal requests, allowing bypass of [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls). An attacker may be able to abuse the [`fileURI`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tuningJobs#FileData) parameter of the API to exfiltrate data.  **What should I do?** No actions needed. We've implemented a fix to return an error message when a media file URL is specified in the fileUri parameter and VPC Service Controls is enabled. Other use cases are unaffected.  **What vulnerabilities are being addressed?** The Agent Platform API serving Gemini multimodal requests lets you include media files by specifying the URL of the media file in the `fileUri` parameter. This capability can be used to bypass VPC Service Controls perimeters. An attacker inside the service perimeter could encode sensitive data in the `fileURI` parameter to bypass the service perimeter.  | Medium | [CVE-2024-12236](https://nvd.nist.gov/vuln/detail/CVE-2024-12236)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
