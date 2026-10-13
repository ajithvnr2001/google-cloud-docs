---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeployFlowRequest/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::DeployFlowRequest (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:19.410039+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::DeployFlowRequest (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeployFlowRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::DeployFlowRequest (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::DeployFlowRequest.

The request message for [Environments.DeployFlow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environments-Client#Google__Cloud__Dialogflow__CX__V3__Environments__Client_deploy_flow_instance_ "Google::Cloud::Dialogflow::CX::V3::Environments::Client#deploy_flow \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #environment
    
    
    def environment() -> ::String

**Returns**

  * (::String) — Required. The environment to deploy the flow to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



### #environment=
    
    
    def environment=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The environment to deploy the flow to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



**Returns**

  * (::String) — Required. The environment to deploy the flow to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 



### #flow_version
    
    
    def flow_version() -> ::String

**Returns**

  * (::String) — Required. The flow version to deploy. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`. 



### #flow_version=
    
    
    def flow_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The flow version to deploy. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`. 



**Returns**

  * (::String) — Required. The flow version to deploy. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
