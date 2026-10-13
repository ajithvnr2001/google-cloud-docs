---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TraceBlock/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::TraceBlock (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:06.670271+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::TraceBlock (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TraceBlock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::TraceBlock (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::TraceBlock.

The trace block tracks a sequence of actions taken by the agent in a flow or a playbook.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #actions
    
    
    def actions() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::Action>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Action)>) — The actions performed by the agent and the user during this session. 



### #actions=
    
    
    def actions=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::Action>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Action)>) — The actions performed by the agent and the user during this session. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Action)>) — The actions performed by the agent and the user during this session. 



### #complete_time
    
    
    def complete_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of the end of the trace block. 



### #end_state
    
    
    def end_state() -> ::Google::Cloud::Dialogflow::CX::V3::OutputState

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::OutputState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-OutputState)) — Optional. Output only. The end state of the trace block. 



### #flow_trace_metadata
    
    
    def flow_trace_metadata() -> ::Google::Cloud::Dialogflow::CX::V3::FlowTraceMetadata

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTraceMetadata)) — Metadata of the flow trace.

Note: The following fields are mutually exclusive: `flow_trace_metadata`, `playbook_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #flow_trace_metadata=
    
    
    def flow_trace_metadata=(value) -> ::Google::Cloud::Dialogflow::CX::V3::FlowTraceMetadata

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::FlowTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTraceMetadata)) — Metadata of the flow trace.

Note: The following fields are mutually exclusive: `flow_trace_metadata`, `playbook_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTraceMetadata)) — Metadata of the flow trace.

Note: The following fields are mutually exclusive: `flow_trace_metadata`, `playbook_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #input_parameters
    
    
    def input_parameters() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of input parameters of the trace block. 



### #input_parameters=
    
    
    def input_parameters=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of input parameters of the trace block. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of input parameters of the trace block. 



### #output_parameters
    
    
    def output_parameters() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of output parameters of the trace block. 



### #output_parameters=
    
    
    def output_parameters=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of output parameters of the trace block. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. A list of output parameters of the trace block. 



### #playbook_trace_metadata
    
    
    def playbook_trace_metadata() -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookTraceMetadata

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTraceMetadata)) — Metadata of the playbook trace.

Note: The following fields are mutually exclusive: `playbook_trace_metadata`, `flow_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #playbook_trace_metadata=
    
    
    def playbook_trace_metadata=(value) -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookTraceMetadata

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTraceMetadata)) — Metadata of the playbook trace.

Note: The following fields are mutually exclusive: `playbook_trace_metadata`, `flow_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTraceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTraceMetadata)) — Metadata of the playbook trace.

Note: The following fields are mutually exclusive: `playbook_trace_metadata`, `flow_trace_metadata`, `speech_processing_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #speech_processing_metadata
    
    
    def speech_processing_metadata() -> ::Google::Cloud::Dialogflow::CX::V3::SpeechProcessingMetadata

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SpeechProcessingMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechProcessingMetadata)) — Metadata of the speech-to-text and speech-to-text processing.

Note: The following fields are mutually exclusive: `speech_processing_metadata`, `playbook_trace_metadata`, `flow_trace_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #speech_processing_metadata=
    
    
    def speech_processing_metadata=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SpeechProcessingMetadata

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SpeechProcessingMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechProcessingMetadata)) — Metadata of the speech-to-text and speech-to-text processing.

Note: The following fields are mutually exclusive: `speech_processing_metadata`, `playbook_trace_metadata`, `flow_trace_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SpeechProcessingMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechProcessingMetadata)) — Metadata of the speech-to-text and speech-to-text processing.

Note: The following fields are mutually exclusive: `speech_processing_metadata`, `playbook_trace_metadata`, `flow_trace_metadata`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of the start of the trace block. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
