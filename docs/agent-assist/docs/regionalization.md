---
url: https://docs.cloud.google.com/agent-assist/docs/regionalization/
title: Regionalization and data residency \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:33:33.988725+00:00
---

# Regionalization and data residency  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/regionalization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Regionalization and data residency Stay organized with collections  Save and categorize content based on your preferences. 

Agent Assist provides [data residency](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud) to keep your [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) physically within a specified geographical region or location. When you specify a region, your data-at-rest is not stored outside that region. Pricing is the same for all regions.

Specifying a region is particularly helpful in the following use cases:

  * Your system has regulatory or policy requirements that govern where your data must reside.
  * Your network latencies might be improved when the data is in the same region as your customers. For example, if Belgium customers use `europe-west1`, they can expect better latency.

**Important:** The [AI/ML data location](https://cloud.google.com/terms/data-residency) (data residency for ML processing, or DRZ) commitment is only supported in locations in the US and EU. When requests are made to multi-region APIs, ML processing for generative models may occur in any of those regions. For non-AI/ML data (in use or transit) or data outside US and EU multi-regions, the DRZ commitment doesn't apply. For details, see the [Vertex AI documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations).

## Available regions

Country grouping | Geographical location | Region ID | Data store region ID  
---|---|---|---  
Americas | Iowa | `us-central1` | `us` (multi-region)  
Americas | South Carolina | `us-east1` |   
Americas | Oregon | `us-west1` |   
Americas | Montreal | `northamerica-northeast1` | `global` (multi-region)  
Americas | United States multi-region | `us` * | `us` (multi-region) *  
Europe | Belgium | `europe-west1` | `eu` (multi-region)  
Europe | London | `europe-west2` |   
Europe | Frankfurt | `europe-west3` |   
Europe | Eemshaven | `europe-west4` | `eu` (multi-region)  
Europe | Zurich | `europe-west6` | `eu` (multi-region)  
Asia Pacific | Singapore | `asia-southeast1` |   
Asia Pacific | Jakarta | `asia-southeast2` | `global` (multi-region)  
Asia Pacific | Tokyo | `asia-northeast1` |   
Asia Pacific | Mumbai | `asia-south1` |   
Asia Pacific | Sydney | `australia-southeast1` |   
Global | Global multi-region (global serving, [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) in United States) | `global` (preferred) or no region (default) ¶ | `global` (multi-region) ¶  
Symbol | Description  
---|---  
* | Vertex AI does not support the 'us' multi-region location. As a result, using Agent Assist's Generative AI features in 'us' multi-region will rely on the respective existing US single region endpoints.  
¶ | Calls to the `global` region might have higher latency when called from outside of the US. Prefer a more specific region that is closer to your services and users, if possible.  
  
## Available features for regional serving

Region ID | Companion Agent | Summarization with custom sections v6.0/5.0/4.0 | Summarization automatic evaluation | Sentiment analysis (v3) | (Proactive) Generative Knowledge Assist | Build your own assist (Preview) | AI coach  
---|---|---|---|---|---|---|---  
`us-central1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`us-east1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`us-west1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`us` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
`northamerica-northeast1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`europe-west1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`europe-west2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`europe-west3` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`europe-west4` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`europe-west6` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
`asia-southeast1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`asia-southeast2` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
`asia-northeast1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`asia-south1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`australia-southeast1` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
`global` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
  
## Data-at-rest

All Agent Assist developer user and end-user data is included in data-at-rest. For example:

  * [Knowledge bases](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base) and [knowledge documents](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents).
  * [Conversation profiles](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversation_profiles).
  * [Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversations) and message histories.
  * [Conversion participants](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#participants).
  * Suggestions returned by Agent Assist.
  * [Feedbacks](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/feedback).



## Limitations

The following limitations apply:

  * The **Agent Assist console** doesn't support regionalization. You can only implement regionalization by calling the API directly.
  * [Model training](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training) does not support regionalization. Your data may get routed outside the region during this process.
  * [API Explorer](https://developers.google.com/explorer-help/), found on many [REST reference documents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest), only supports the `global` region for API calls.

  * [CCAI Transcription](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription) only supports multi-region data in use and data at rest (if not using the Speech Adaptation feature) in EU, US, North America (Canada).

  * Only the following regions are supported for data stores, used by (Proactive) Generative Knowledge Assist feature: `global`, `us` multi-region, and `eu` multi-region.

  * [Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview#gwgs) (GWGS) does not support Data Residency (DRZ). When enabled, this control does not apply to search requests. For more information, see [Gemini Enterprise Agent Platform security controls](https://cloud.google.com/vertex-ai/generative-ai/docs/security-controls).




## Specify a region using the API

To use regionalization you must specify a region for every API request.

Required fields:

  * Provide the region ID for the `location` URL path parameter.

  * For the `global` region, use `dialogflow.googleapis.com` for the hostname. For all other regions, use `[region-id]-dialogflow.googleapis.com` for the hostname.




For example:

  * `dialogflow.googleapis.com/v2/projects/project_id/locations/global/knowledgeBases/knowledge_base_id`

  * `us-central1-dialogflow.googleapis.com/v2/projects/project_id/locations/us-central1/knowledgeBases/knowledge_base_id`




To use [client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/reference-index), the following steps are required:

  * Set the service endpoint to: `REGION_ID-dialogflow.googleapis.com`.
  * Set the resource name with the correct location, for example:
        
        projects/project_id/locations/region_id/knowledgeBases/knowledge_base_id
        




## Credentials

We recommend that you use the GOOGLE_APPLICATION_CREDENTIALS environment variable to provide your client libraries with credentials. See the [Dialogflow setup instructions](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup#auth-env) for more information about setting this variable.

If you instead need to provide manual credentials in your code, one additional step is required before you can call a regionalized endpoint. You must set the scope to https://www.googleapis.com/auth/cloud-platform when you generate your authentication credentials. The following example demonstrates how to do this in Java when creating a `GoogleCredentials` object:
    
    
        GoogleCredentials.fromStream(new FileInputStream("credential_file"))
          .createScoped("https://www.googleapis.com/auth/cloud-platform")
    

## Cloud Logging

See the [Cloud Logging documentation](https://docs.cloud.google.com/dialogflow/es/docs/logging) to control the region where your logs are stored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
