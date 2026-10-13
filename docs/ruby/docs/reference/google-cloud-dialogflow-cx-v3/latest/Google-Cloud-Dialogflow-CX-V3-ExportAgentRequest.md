---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:21.386409+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest.

The request message for [Agents.ExportAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_export_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#export_agent \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent_uri
    
    
    def agent_uri() -> ::String

**Returns**

  * (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized agent is returned inline.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). 




### #agent_uri=
    
    
    def agent_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized agent is returned inline.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). 




**Returns**

  * (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized agent is returned inline.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). 




### #data_format
    
    
    def data_format() -> ::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-DataFormat)) — Optional. The data format of the exported agent. If not specified, `BLOB` is assumed. 



### #data_format=
    
    
    def data_format=(value) -> ::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-DataFormat)) — Optional. The data format of the exported agent. If not specified, `BLOB` is assumed. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-DataFormat)) — Optional. The data format of the exported agent. If not specified, `BLOB` is assumed. 



### #environment
    
    
    def environment() -> ::String

**Returns**

  * (::String) — Optional. Environment name. If not set, draft environment is assumed. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



### #environment=
    
    
    def environment=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Environment name. If not set, draft environment is assumed. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



**Returns**

  * (::String) — Optional. Environment name. If not set, draft environment is assumed. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



### #git_destination
    
    
    def git_destination() -> ::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-GitDestination)) — Optional. The Git branch to export the agent to. 



### #git_destination=
    
    
    def git_destination=(value) -> ::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-GitDestination)) — Optional. The Git branch to export the agent to. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-GitDestination)) — Optional. The Git branch to export the agent to. 



### #include_bigquery_export_settings
    
    
    def include_bigquery_export_settings() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to include BigQuery Export setting. 



### #include_bigquery_export_settings=
    
    
    def include_bigquery_export_settings=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to include BigQuery Export setting. 



**Returns**

  * (::Boolean) — Optional. Whether to include BigQuery Export setting. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the agent to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the agent to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



**Returns**

  * (::String) — Required. The name of the agent to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
