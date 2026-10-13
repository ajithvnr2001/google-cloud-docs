---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Paths/
title: Gemini Enterprise for Customer Experience V1BETA API - Module Google::Cloud::Ces::V1beta::AgentService::Paths (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:15.707732+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Module Google::Cloud::Ces::V1beta::AgentService::Paths (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Module Google::Cloud::Ces::V1beta::AgentService::Paths (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API module Google::Cloud::Ces::V1beta::AgentService::Paths.

Path helper methods for the AgentService API.

## Extended By

  * [Google::Cloud::Ces::V1beta::AgentService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Paths)



## Included In

  * [Google::Cloud::Ces::V1beta::AgentService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Client)
  * [Google::Cloud::Ces::V1beta::AgentService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Paths)
  * [Google::Cloud::Ces::V1beta::AgentService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Rest-Client)



## Methods 

### #agent_path
    
    
    def agent_path(project:, location:, app:, agent:) -> ::String

Create a fully-qualified Agent resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/agents/{agent}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **agent** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #app_path
    
    
    def app_path(project:, location:, app:) -> ::String

Create a fully-qualified App resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #app_version_path
    
    
    def app_version_path(project:, location:, app:, version:) -> ::String

Create a fully-qualified AppVersion resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/versions/{version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #changelog_path
    
    
    def changelog_path(project:, location:, app:, changelog:) -> ::String

Create a fully-qualified Changelog resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/changelogs/{changelog}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **changelog** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #conversation_path
    
    
    def conversation_path(project:, location:, app:, conversation:) -> ::String

Create a fully-qualified Conversation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **conversation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #dataset_path
    
    
    def dataset_path(project:, location:, dataset:) -> ::String

Create a fully-qualified Dataset resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/datasets/{dataset}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **dataset** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #deidentify_template_path
    
    
    def deidentify_template_path(organization:, location:, deidentify_template:) -> ::String
    def deidentify_template_path(project:, location:, deidentify_template:) -> ::String

Create a fully-qualified DeidentifyTemplate resource string.

**Overloads**
    
    
    def deidentify_template_path(organization:, location:, deidentify_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **deidentify_template** (String) 


    
    
    def deidentify_template_path(project:, location:, deidentify_template:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **deidentify_template** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #deployment_path
    
    
    def deployment_path(project:, location:, app:, deployment:) -> ::String

Create a fully-qualified Deployment resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **deployment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #dialogflow_agent_path
    
    
    def dialogflow_agent_path(project:, location:, agent:) -> ::String

Create a fully-qualified DialogflowAgent resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/agents/{agent}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **agent** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #engine_path
    
    
    def engine_path(project:, location:, collection:, engine:) -> ::String

Create a fully-qualified Engine resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **collection** (String) 
  * **engine** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #evaluation_run_path
    
    
    def evaluation_run_path(project:, location:, app:, evaluation_run:) -> ::String

Create a fully-qualified EvaluationRun resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluation_run}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **evaluation_run** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #example_path
    
    
    def example_path(project:, location:, app:, example:) -> ::String

Create a fully-qualified Example resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/examples/{example}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **example** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #guardrail_path
    
    
    def guardrail_path(project:, location:, app:, guardrail:) -> ::String

Create a fully-qualified Guardrail resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **guardrail** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #inspect_template_path
    
    
    def inspect_template_path(organization:, location:, inspect_template:) -> ::String
    def inspect_template_path(project:, location:, inspect_template:) -> ::String

Create a fully-qualified InspectTemplate resource string.

**Overloads**
    
    
    def inspect_template_path(organization:, location:, inspect_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **inspect_template** (String) 


    
    
    def inspect_template_path(project:, location:, inspect_template:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/inspectTemplates/{inspect_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **inspect_template** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #secret_version_path
    
    
    def secret_version_path(project:, secret:, secret_version:) -> ::String

Create a fully-qualified SecretVersion resource string.

The resource will be in the following format:

`projects/{project}/secrets/{secret}/versions/{secret_version}`

**Parameters**

  * **project** (String) 
  * **secret** (String) 
  * **secret_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #security_settings_path
    
    
    def security_settings_path(project:, location:) -> ::String

Create a fully-qualified SecuritySettings resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/securitySettings`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_path
    
    
    def service_path(project:, location:, namespace:, service:) -> ::String

Create a fully-qualified Service resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **namespace** (String) 
  * **service** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #tool_path
    
    
    def tool_path(project:, location:, app:, tool:) -> ::String

Create a fully-qualified Tool resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/tools/{tool}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **tool** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #toolset_path
    
    
    def toolset_path(project:, location:, app:, toolset:) -> ::String

Create a fully-qualified Toolset resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **toolset** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
