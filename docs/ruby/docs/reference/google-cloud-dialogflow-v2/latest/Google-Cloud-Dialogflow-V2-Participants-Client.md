---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Participants::Client (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:58.579260+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Participants::Client (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Participants::Client (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::Participants::Client.

Client for the Participants service.

Service for managing [Participants](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant "Google::Cloud::Dialogflow::V2::Participant \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::V2::Participants::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Participants Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration "Google::Cloud::Dialogflow::V2::Participants::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Participants clients
    ::Google::Cloud::Dialogflow::V2::Participants::Client.configure do |config|
      config.timeout = 10.0
    end

### #analyze_content
    
    
    def analyze_content(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse
    def analyze_content(participant: nil, text_input: nil, audio_input: nil, event_input: nil, suggestion_input: nil, reply_audio_config: nil, query_params: nil, assist_query_params: nil, cx_parameters: nil, request_id: nil) -> ::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

**Overloads**
    
    
    def analyze_content(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse

Pass arguments to `analyze_content` via a request object, either of type [AnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentRequest "Google::Cloud::Dialogflow::V2::AnalyzeContentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::AnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def analyze_content(participant: nil, text_input: nil, audio_input: nil, event_input: nil, suggestion_input: nil, reply_audio_config: nil, query_params: nil, assist_query_params: nil, cx_parameters: nil, request_id: nil) -> ::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse

Pass arguments to `analyze_content` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **participant** (::String) — Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 
  * **text_input** ([::Google::Cloud::Dialogflow::V2::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-TextInput), ::Hash) — The natural language text to be processed.

Note: The following parameters are mutually exclusive: `text_input`, `audio_input`, `event_input`, `suggestion_input`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **audio_input** ([::Google::Cloud::Dialogflow::V2::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AudioInput), ::Hash) — The natural language speech audio to be processed.

Note: The following parameters are mutually exclusive: `audio_input`, `text_input`, `event_input`, `suggestion_input`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **event_input** ([::Google::Cloud::Dialogflow::V2::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EventInput), ::Hash) — An input event to send to Dialogflow.

Note: The following parameters are mutually exclusive: `event_input`, `text_input`, `audio_input`, `suggestion_input`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **suggestion_input** ([::Google::Cloud::Dialogflow::V2::SuggestionInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestionInput), ::Hash) — An input representing the selection of a suggestion.

Note: The following parameters are mutually exclusive: `suggestion_input`, `text_input`, `audio_input`, `event_input`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **reply_audio_config** ([::Google::Cloud::Dialogflow::V2::OutputAudioConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-OutputAudioConfig), ::Hash) — Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling AnalyzeContent. If this configuration is not supplied, speech synthesis is disabled. 
  * **query_params** ([::Google::Cloud::Dialogflow::V2::QueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryParameters), ::Hash) — Parameters for a Dialogflow virtual-agent query. 
  * **assist_query_params** ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters), ::Hash) — Parameters for a human assist query. 
  * **cx_parameters** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct), ::Hash) — Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.

Note: this field should only be used if you are connecting to a Dialogflow CX agent. 

  * **request_id** (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `request_id` is provided. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::AnalyzeContentRequest.new
    
    # Call the analyze_content method.
    result = client.analyze_content request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::AnalyzeContentResponse.
    p result

### #bidi_streaming_analyze_content
    
    
    def bidi_streaming_analyze_content(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentResponse>

Bidirectional endless streaming version of [StreamingAnalyzeContent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client#Google__Cloud__Dialogflow__V2__Participants__Client_streaming_analyze_content_instance_ "Google::Cloud::Dialogflow::V2::Participants::Client#streaming_analyze_content \(method\)").

**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-BidiStreamingAnalyzeContentRequest), ::Hash>) — An enumerable of [BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-BidiStreamingAnalyzeContentRequest "Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentRequest \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-BidiStreamingAnalyzeContentResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-BidiStreamingAnalyzeContentResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the bidi_streaming_analyze_content method to start streaming.
    output = client.bidi_streaming_analyze_content input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentRequest.new
    input << Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentRequest.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::Dialogflow::V2::BidiStreamingAnalyzeContentResponse
    output.each do |current_response|
      p current_response
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Participants Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client#Google__Cloud__Dialogflow__V2__Participants__Client_configure_class_ "Google::Cloud::Dialogflow::V2::Participants::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration "Google::Cloud::Dialogflow::V2::Participants::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration)) 



### #create_participant
    
    
    def create_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant
    def create_participant(parent: nil, participant: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Creates a new participant in a conversation.

**Overloads**
    
    
    def create_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `create_participant` via a request object, either of type [CreateParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateParticipantRequest "Google::Cloud::Dialogflow::V2::CreateParticipantRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::CreateParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateParticipantRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_participant(parent: nil, participant: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `create_participant` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource identifier of the conversation adding the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. 
  * **participant** ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant), ::Hash) — Required. The participant to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::CreateParticipantRequest.new
    
    # Call the create_participant method.
    result = client.create_participant request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Participant.
    p result

### #get_participant
    
    
    def get_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant
    def get_participant(name: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Retrieves a conversation participant.

**Overloads**
    
    
    def get_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `get_participant` via a request object, either of type [GetParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetParticipantRequest "Google::Cloud::Dialogflow::V2::GetParticipantRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetParticipantRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_participant(name: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `get_participant` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetParticipantRequest.new
    
    # Call the get_participant method.
    result = client.get_participant request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Participant.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Participants client object.

**Yields**

  * (config) — Configure the Participants client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::V2::Participants::Client.new do |config|
      config.timeout = 10.0
    end

### #list_participants
    
    
    def list_participants(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Participant>
    def list_participants(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Participant>

Returns the list of all participants in the specified conversation.

**Overloads**
    
    
    def list_participants(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Participant>

Pass arguments to `list_participants` via a request object, either of type [ListParticipantsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListParticipantsRequest "Google::Cloud::Dialogflow::V2::ListParticipantsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ListParticipantsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListParticipantsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_participants(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Participant>

Pass arguments to `list_participants` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The conversation to list all participants from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. 
  * **page_size** (::Integer) — Optional. The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous list request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ListParticipantsRequest.new
    
    # Call the list_participants method.
    result = client.list_participants request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::Participant.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #streaming_analyze_content
    
    
    def streaming_analyze_content(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentResponse>

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST).

The top-level message sent to the client by the server is `StreamingAnalyzeContentResponse`. Multiple response messages can be returned in order. The first one or more messages contain the `recognition_result` field. Each result represents a more complete transcript of what the user said. The next message contains the `reply_text` field and potentially the `reply_audio` field. The message can also contain the `automated_agent_reply` field.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingAnalyzeContentRequest), ::Hash>) — An enumerable of [StreamingAnalyzeContentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingAnalyzeContentRequest "Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentRequest \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingAnalyzeContentResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingAnalyzeContentResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the streaming_analyze_content method to start streaming.
    output = client.streaming_analyze_content input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentRequest.new
    input << Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentRequest.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::Dialogflow::V2::StreamingAnalyzeContentResponse
    output.each do |current_response|
      p current_response
    end

### #streaming_reactive_companion_suggestions
    
    
    def streaming_reactive_companion_suggestions(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsResponse>

External streaming API for direct human-agent-to-bot chats.

**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingReactiveCompanionSuggestionsRequest), ::Hash>) — An enumerable of [StreamingReactiveCompanionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingReactiveCompanionSuggestionsRequest "Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsRequest \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingReactiveCompanionSuggestionsResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-StreamingReactiveCompanionSuggestionsResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the streaming_reactive_companion_suggestions method to start streaming.
    output = client.streaming_reactive_companion_suggestions input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsRequest.new
    input << Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsRequest.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::Dialogflow::V2::StreamingReactiveCompanionSuggestionsResponse
    output.each do |current_response|
      p current_response
    end

### #suggest_articles
    
    
    def suggest_articles(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse
    def suggest_articles(parent: nil, latest_message: nil, context_size: nil, assist_query_params: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse

Gets suggested articles for a participant based on specific historical messages.

**Overloads**
    
    
    def suggest_articles(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse

Pass arguments to `suggest_articles` via a request object, either of type [SuggestArticlesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestArticlesRequest "Google::Cloud::Dialogflow::V2::SuggestArticlesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::SuggestArticlesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestArticlesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def suggest_articles(parent: nil, latest_message: nil, context_size: nil, assist_query_params: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse

Pass arguments to `suggest_articles` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 
  * **latest_message** (::String) — Optional. The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation.

Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 

  * **context_size** (::Integer) — Optional. Max number of messages prior to and including [latest_message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestArticlesRequest#Google__Cloud__Dialogflow__V2__SuggestArticlesRequest_latest_message_instance_ "Google::Cloud::Dialogflow::V2::SuggestArticlesRequest#latest_message \(method\)") to use as context when compiling the suggestion. By default 20 and at most 50. 
  * **assist_query_params** ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters), ::Hash) — Parameters for a human assist query. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestArticlesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestArticlesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestArticlesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::SuggestArticlesRequest.new
    
    # Call the suggest_articles method.
    result = client.suggest_articles request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::SuggestArticlesResponse.
    p result

### #suggest_faq_answers
    
    
    def suggest_faq_answers(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse
    def suggest_faq_answers(parent: nil, latest_message: nil, context_size: nil, assist_query_params: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse

Gets suggested faq answers for a participant based on specific historical messages.

**Overloads**
    
    
    def suggest_faq_answers(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse

Pass arguments to `suggest_faq_answers` via a request object, either of type [SuggestFaqAnswersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestFaqAnswersRequest "Google::Cloud::Dialogflow::V2::SuggestFaqAnswersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestFaqAnswersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def suggest_faq_answers(parent: nil, latest_message: nil, context_size: nil, assist_query_params: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse

Pass arguments to `suggest_faq_answers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 
  * **latest_message** (::String) — Optional. The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation.

Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 

  * **context_size** (::Integer) — Optional. Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 20 and at most 50. 
  * **assist_query_params** ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters), ::Hash) — Parameters for a human assist query. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestFaqAnswersResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestFaqAnswersResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::SuggestFaqAnswersRequest.new
    
    # Call the suggest_faq_answers method.
    result = client.suggest_faq_answers request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::SuggestFaqAnswersResponse.
    p result

### #suggest_knowledge_assist
    
    
    def suggest_knowledge_assist(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse
    def suggest_knowledge_assist(parent: nil, latest_message: nil, context_size: nil, previous_suggested_query: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse

Gets knowledge assist suggestions based on historical messages.

**Overloads**
    
    
    def suggest_knowledge_assist(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse

Pass arguments to `suggest_knowledge_assist` via a request object, either of type [SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest "Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def suggest_knowledge_assist(parent: nil, latest_message: nil, context_size: nil, previous_suggested_query: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse

Pass arguments to `suggest_knowledge_assist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the participant to fetch suggestions for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 
  * **latest_message** (::String) — Optional. The name of the latest conversation message to compile suggestions for. If empty, it will be the latest message of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 
  * **context_size** (::Integer) — Optional. Max number of messages prior to and including [latest_message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest#Google__Cloud__Dialogflow__V2__SuggestKnowledgeAssistRequest_latest_message_instance_ "Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest#latest_message \(method\)") to use as context when compiling the suggestion. The context size is by default 100 and at most 100. 
  * **previous_suggested_query** (::String) — Optional. The previously suggested query for the given conversation. This helps identify whether the next suggestion we generate is reasonably different from the previous one. This is useful to avoid similar suggestions within the conversation. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest.new
    
    # Call the suggest_knowledge_assist method.
    result = client.suggest_knowledge_assist request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistResponse.
    p result

### #suggest_smart_replies
    
    
    def suggest_smart_replies(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse
    def suggest_smart_replies(parent: nil, current_text_input: nil, latest_message: nil, context_size: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse

Gets smart replies for a participant based on specific historical messages.

**Overloads**
    
    
    def suggest_smart_replies(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse

Pass arguments to `suggest_smart_replies` via a request object, either of type [SuggestSmartRepliesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestSmartRepliesRequest "Google::Cloud::Dialogflow::V2::SuggestSmartRepliesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestSmartRepliesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def suggest_smart_replies(parent: nil, current_text_input: nil, latest_message: nil, context_size: nil) -> ::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse

Pass arguments to `suggest_smart_replies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 
  * **current_text_input** ([::Google::Cloud::Dialogflow::V2::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-TextInput), ::Hash) — The current natural language text segment to compile suggestion for. This provides a way for user to get follow up smart reply suggestion after a smart reply selection, without sending a text message. 
  * **latest_message** (::String) — The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation.

Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 

  * **context_size** (::Integer) — Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 20 and at most 50. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestSmartRepliesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestSmartRepliesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::SuggestSmartRepliesRequest.new
    
    # Call the suggest_smart_replies method.
    result = client.suggest_smart_replies request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::SuggestSmartRepliesResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_participant
    
    
    def update_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant
    def update_participant(participant: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Updates the specified participant.

**Overloads**
    
    
    def update_participant(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `update_participant` via a request object, either of type [UpdateParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateParticipantRequest "Google::Cloud::Dialogflow::V2::UpdateParticipantRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::UpdateParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateParticipantRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_participant(participant: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::V2::Participant

Pass arguments to `update_participant` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **participant** ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant), ::Hash) — Required. The participant to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The mask to specify which fields to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participant)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Participants::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::UpdateParticipantRequest.new
    
    # Call the update_participant method.
    result = client.update_participant request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Participant.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
