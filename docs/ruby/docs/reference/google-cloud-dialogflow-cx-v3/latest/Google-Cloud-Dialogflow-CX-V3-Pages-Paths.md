---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Paths/
title: Dialogflow CX V3 API - Module Google::Cloud::Dialogflow::CX::V3::Pages::Paths (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:03.581424+00:00
---

# Dialogflow CX V3 API - Module Google::Cloud::Dialogflow::CX::V3::Pages::Paths (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Module Google::Cloud::Dialogflow::CX::V3::Pages::Paths (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API module Google::Cloud::Dialogflow::CX::V3::Pages::Paths.

Path helper methods for the Pages API.

## Extended By

  * [Google::Cloud::Dialogflow::CX::V3::Pages::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Paths)



## Included In

  * [Google::Cloud::Dialogflow::CX::V3::Pages::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client)
  * [Google::Cloud::Dialogflow::CX::V3::Pages::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Paths)
  * [Google::Cloud::Dialogflow::CX::V3::Pages::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Rest-Client)



## Methods 

### #entity_type_path
    
    
    def entity_type_path(project:, location:, agent:, entity_type:) -> ::String

Create a fully-qualified EntityType resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/entityTypes/{entity_type}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **entity_type** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #flow_path
    
    
    def flow_path(project:, location:, agent:, flow:) -> ::String

Create a fully-qualified Flow resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/flows/{flow}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **flow** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #generator_path
    
    
    def generator_path(project:, location:, agent:, generator:) -> ::String

Create a fully-qualified Generator resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/generators/{generator}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **generator** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #intent_path
    
    
    def intent_path(project:, location:, agent:, intent:) -> ::String

Create a fully-qualified Intent resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/intents/{intent}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **intent** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #page_path
    
    
    def page_path(project:, location:, agent:, flow:, page:) -> ::String

Create a fully-qualified Page resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/flows/{flow}/pages/{page}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **flow** (String) 
  * **page** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #playbook_path
    
    
    def playbook_path(project:, location:, agent:, playbook:) -> ::String

Create a fully-qualified Playbook resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **playbook** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #tool_path
    
    
    def tool_path(project:, location:, agent:, tool:) -> ::String

Create a fully-qualified Tool resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **tool** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #transition_route_group_path
    
    
    def transition_route_group_path(project:, location:, agent:, flow:, transition_route_group:) -> ::String
    def transition_route_group_path(project:, location:, agent:, transition_route_group:) -> ::String

Create a fully-qualified TransitionRouteGroup resource string.

**Overloads**
    
    
    def transition_route_group_path(project:, location:, agent:, flow:, transition_route_group:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/flows/{flow}/transitionRouteGroups/{transition_route_group}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **flow** (String) 
  * **transition_route_group** (String) 


    
    
    def transition_route_group_path(project:, location:, agent:, transition_route_group:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/transitionRouteGroups/{transition_route_group}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **transition_route_group** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #webhook_path
    
    
    def webhook_path(project:, location:, agent:, webhook:) -> ::String

Create a fully-qualified Webhook resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}/webhooks/{webhook}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 
  * **webhook** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
