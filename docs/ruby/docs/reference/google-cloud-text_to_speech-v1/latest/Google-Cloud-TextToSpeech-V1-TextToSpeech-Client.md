---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client/
title: Cloud Text-to-Speech V1 API - Class Google::Cloud::TextToSpeech::V1::TextToSpeech::Client (v1.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:27.035116+00:00
---

# Cloud Text-to-Speech V1 API - Class Google::Cloud::TextToSpeech::V1::TextToSpeech::Client (v1.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Text-to-Speech V1 API - Class Google::Cloud::TextToSpeech::V1::TextToSpeech::Client (v1.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.1 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.13.0  0.12.2  0.11.1  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.2 

Reference documentation and code samples for the Cloud Text-to-Speech V1 API class Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.

Client for the TextToSpeech service.

Service that implements Google Cloud Text-to-Speech API.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::TextToSpeech::V1::TextToSpeech::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the TextToSpeech Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration "Google::Cloud::TextToSpeech::V1::TextToSpeech::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all TextToSpeech clients
    ::Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the TextToSpeech Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client#Google__Cloud__TextToSpeech__V1__TextToSpeech__Client_configure_class_ "Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration "Google::Cloud::TextToSpeech::V1::TextToSpeech::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new TextToSpeech client object.

**Yields**

  * (config) — Configure the TextToSpeech client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-TextToSpeech-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.new do |config|
      config.timeout = 10.0
    end

### #list_voices
    
    
    def list_voices(request, options = nil) -> ::Google::Cloud::TextToSpeech::V1::ListVoicesResponse
    def list_voices(language_code: nil) -> ::Google::Cloud::TextToSpeech::V1::ListVoicesResponse

Returns a list of Voice supported for synthesis.

**Overloads**
    
    
    def list_voices(request, options = nil) -> ::Google::Cloud::TextToSpeech::V1::ListVoicesResponse

Pass arguments to `list_voices` via a request object, either of type [ListVoicesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-ListVoicesRequest "Google::Cloud::TextToSpeech::V1::ListVoicesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TextToSpeech::V1::ListVoicesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-ListVoicesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_voices(language_code: nil) -> ::Google::Cloud::TextToSpeech::V1::ListVoicesResponse

Pass arguments to `list_voices` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **language_code** (::String) — Optional. Recommended. [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. If not specified, the API will return all supported voices. If specified, the ListVoices call will only return voices that can be used to synthesize this language_code. For example, if you specify `"en-NZ"`, all `"en-NZ"` voices will be returned. If you specify `"no"`, both `"no-\*"` (Norwegian) and `"nb-\*"` (Norwegian Bokmal) voices will be returned. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::TextToSpeech::V1::ListVoicesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-ListVoicesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::TextToSpeech::V1::ListVoicesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-ListVoicesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/text_to_speech/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TextToSpeech::V1::ListVoicesRequest.new
    
    # Call the list_voices method.
    result = client.list_voices request
    
    # The returned object is of type Google::Cloud::TextToSpeech::V1::ListVoicesResponse.
    p result

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #streaming_synthesize
    
    
    def streaming_synthesize(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::TextToSpeech::V1::StreamingSynthesizeResponse>

Performs bidirectional streaming speech synthesis: receives audio while sending text.

**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::TextToSpeech::V1::StreamingSynthesizeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-StreamingSynthesizeRequest), ::Hash>) — An enumerable of [StreamingSynthesizeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-StreamingSynthesizeRequest "Google::Cloud::TextToSpeech::V1::StreamingSynthesizeRequest \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::TextToSpeech::V1::StreamingSynthesizeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-StreamingSynthesizeResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::TextToSpeech::V1::StreamingSynthesizeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-StreamingSynthesizeResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/text_to_speech/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the streaming_synthesize method to start streaming.
    output = client.streaming_synthesize input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::TextToSpeech::V1::StreamingSynthesizeRequest.new
    input << Google::Cloud::TextToSpeech::V1::StreamingSynthesizeRequest.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::TextToSpeech::V1::StreamingSynthesizeResponse
    output.each do |current_response|
      p current_response
    end

### #synthesize_speech
    
    
    def synthesize_speech(request, options = nil) -> ::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse
    def synthesize_speech(input: nil, voice: nil, audio_config: nil, advanced_voice_options: nil) -> ::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse

Synthesizes speech synchronously: receive results after all text input has been processed.

**Overloads**
    
    
    def synthesize_speech(request, options = nil) -> ::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse

Pass arguments to `synthesize_speech` via a request object, either of type [SynthesizeSpeechRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-SynthesizeSpeechRequest "Google::Cloud::TextToSpeech::V1::SynthesizeSpeechRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-SynthesizeSpeechRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def synthesize_speech(input: nil, voice: nil, audio_config: nil, advanced_voice_options: nil) -> ::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse

Pass arguments to `synthesize_speech` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **input** ([::Google::Cloud::TextToSpeech::V1::SynthesisInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-SynthesisInput), ::Hash) — Required. The Synthesizer requires either plain text or SSML as input. 
  * **voice** ([::Google::Cloud::TextToSpeech::V1::VoiceSelectionParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-VoiceSelectionParams), ::Hash) — Required. The desired voice of the synthesized audio. 
  * **audio_config** ([::Google::Cloud::TextToSpeech::V1::AudioConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-AudioConfig), ::Hash) — Required. The configuration of the synthesized audio. 
  * **advanced_voice_options** ([::Google::Cloud::TextToSpeech::V1::AdvancedVoiceOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-AdvancedVoiceOptions), ::Hash) — Optional. Advanced voice options. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-SynthesizeSpeechResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1/latest/Google-Cloud-TextToSpeech-V1-SynthesizeSpeechResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/text_to_speech/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TextToSpeech::V1::TextToSpeech::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TextToSpeech::V1::SynthesizeSpeechRequest.new
    
    # Call the synthesize_speech method.
    result = client.synthesize_speech request
    
    # The returned object is of type Google::Cloud::TextToSpeech::V1::SynthesizeSpeechResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
