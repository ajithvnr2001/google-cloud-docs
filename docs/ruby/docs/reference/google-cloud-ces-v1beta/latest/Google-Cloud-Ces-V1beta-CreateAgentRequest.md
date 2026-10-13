---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateAgentRequest/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::CreateAgentRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:46.793813+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::CreateAgentRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateAgentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::CreateAgentRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::CreateAgentRequest.

Request message for [AgentService.CreateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Client#Google__Cloud__Ces__V1beta__AgentService__Client_create_agent_instance_ "Google::Cloud::Ces::V1beta::AgentService::Client#create_agent \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent
    
    
    def agent() -> ::Google::Cloud::Ces::V1beta::Agent

**Returns**

  * ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — Required. The agent to create. 



### #agent=
    
    
    def agent=(value) -> ::Google::Cloud::Ces::V1beta::Agent

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — Required. The agent to create. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — Required. The agent to create. 



### #agent_id
    
    
    def agent_id() -> ::String

**Returns**

  * (::String) — Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent. 



### #agent_id=
    
    
    def agent_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent. 



**Returns**

  * (::String) — Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the app to create an agent in. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the app to create an agent in. 



**Returns**

  * (::String) — Required. The resource name of the app to create an agent in. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
