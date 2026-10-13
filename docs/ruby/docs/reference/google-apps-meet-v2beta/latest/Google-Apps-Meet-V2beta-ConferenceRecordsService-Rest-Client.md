---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client/
title: Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:31.172965+00:00
---

# Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.0  0.3.2  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2BETA API class Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.

REST client for the ConferenceRecordsService service.

REST API for services dealing with conference records.

## Inherits

  * Object 



## Includes

  * [Google::Apps::Meet::V2beta::ConferenceRecordsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ConferenceRecordsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration "Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ConferenceRecordsService clients
    ::Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ConferenceRecordsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client#Google__Apps__Meet__V2beta__ConferenceRecordsService__Rest__Client_configure_class_ "Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration "Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration)) 



### #get_conference_record
    
    
    def get_conference_record(request, options = nil) -> ::Google::Apps::Meet::V2beta::ConferenceRecord
    def get_conference_record(name: nil) -> ::Google::Apps::Meet::V2beta::ConferenceRecord

Gets a conference record by conference ID.

**Overloads**
    
    
    def get_conference_record(request, options = nil) -> ::Google::Apps::Meet::V2beta::ConferenceRecord

Pass arguments to `get_conference_record` via a request object, either of type [GetConferenceRecordRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetConferenceRecordRequest "Google::Apps::Meet::V2beta::GetConferenceRecordRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetConferenceRecordRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetConferenceRecordRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_conference_record(name: nil) -> ::Google::Apps::Meet::V2beta::ConferenceRecord

Pass arguments to `get_conference_record` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the conference. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::ConferenceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecord)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::ConferenceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecord)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetConferenceRecordRequest.new
    
    # Call the get_conference_record method.
    result = client.get_conference_record request
    
    # The returned object is of type Google::Apps::Meet::V2beta::ConferenceRecord.
    p result

### #get_participant
    
    
    def get_participant(request, options = nil) -> ::Google::Apps::Meet::V2beta::Participant
    def get_participant(name: nil) -> ::Google::Apps::Meet::V2beta::Participant

Gets a participant by participant ID.

**Overloads**
    
    
    def get_participant(request, options = nil) -> ::Google::Apps::Meet::V2beta::Participant

Pass arguments to `get_participant` via a request object, either of type [GetParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetParticipantRequest "Google::Apps::Meet::V2beta::GetParticipantRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetParticipantRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetParticipantRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_participant(name: nil) -> ::Google::Apps::Meet::V2beta::Participant

Pass arguments to `get_participant` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the participant. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Participant)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Participant)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetParticipantRequest.new
    
    # Call the get_participant method.
    result = client.get_participant request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Participant.
    p result

### #get_participant_session
    
    
    def get_participant_session(request, options = nil) -> ::Google::Apps::Meet::V2beta::ParticipantSession
    def get_participant_session(name: nil) -> ::Google::Apps::Meet::V2beta::ParticipantSession

Gets a participant session by participant session ID.

**Overloads**
    
    
    def get_participant_session(request, options = nil) -> ::Google::Apps::Meet::V2beta::ParticipantSession

Pass arguments to `get_participant_session` via a request object, either of type [GetParticipantSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetParticipantSessionRequest "Google::Apps::Meet::V2beta::GetParticipantSessionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetParticipantSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetParticipantSessionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_participant_session(name: nil) -> ::Google::Apps::Meet::V2beta::ParticipantSession

Pass arguments to `get_participant_session` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the participant. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::ParticipantSession](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ParticipantSession)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::ParticipantSession](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ParticipantSession)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetParticipantSessionRequest.new
    
    # Call the get_participant_session method.
    result = client.get_participant_session request
    
    # The returned object is of type Google::Apps::Meet::V2beta::ParticipantSession.
    p result

### #get_recording
    
    
    def get_recording(request, options = nil) -> ::Google::Apps::Meet::V2beta::Recording
    def get_recording(name: nil) -> ::Google::Apps::Meet::V2beta::Recording

Gets a recording by recording ID.

**Overloads**
    
    
    def get_recording(request, options = nil) -> ::Google::Apps::Meet::V2beta::Recording

Pass arguments to `get_recording` via a request object, either of type [GetRecordingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetRecordingRequest "Google::Apps::Meet::V2beta::GetRecordingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetRecordingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetRecordingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_recording(name: nil) -> ::Google::Apps::Meet::V2beta::Recording

Pass arguments to `get_recording` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the recording. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Recording](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Recording)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Recording](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Recording)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetRecordingRequest.new
    
    # Call the get_recording method.
    result = client.get_recording request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Recording.
    p result

### #get_smart_note
    
    
    def get_smart_note(request, options = nil) -> ::Google::Apps::Meet::V2beta::SmartNote
    def get_smart_note(name: nil) -> ::Google::Apps::Meet::V2beta::SmartNote

Gets smart notes by smart note ID.

**Overloads**
    
    
    def get_smart_note(request, options = nil) -> ::Google::Apps::Meet::V2beta::SmartNote

Pass arguments to `get_smart_note` via a request object, either of type [GetSmartNoteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetSmartNoteRequest "Google::Apps::Meet::V2beta::GetSmartNoteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetSmartNoteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetSmartNoteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_smart_note(name: nil) -> ::Google::Apps::Meet::V2beta::SmartNote

Pass arguments to `get_smart_note` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the smart note. Format: conferenceRecords/{conference_record}/smartNotes/{smart_note} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::SmartNote](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SmartNote)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::SmartNote](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SmartNote)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetSmartNoteRequest.new
    
    # Call the get_smart_note method.
    result = client.get_smart_note request
    
    # The returned object is of type Google::Apps::Meet::V2beta::SmartNote.
    p result

### #get_transcript
    
    
    def get_transcript(request, options = nil) -> ::Google::Apps::Meet::V2beta::Transcript
    def get_transcript(name: nil) -> ::Google::Apps::Meet::V2beta::Transcript

Gets a transcript by transcript ID.

**Overloads**
    
    
    def get_transcript(request, options = nil) -> ::Google::Apps::Meet::V2beta::Transcript

Pass arguments to `get_transcript` via a request object, either of type [GetTranscriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetTranscriptRequest "Google::Apps::Meet::V2beta::GetTranscriptRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetTranscriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetTranscriptRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_transcript(name: nil) -> ::Google::Apps::Meet::V2beta::Transcript

Pass arguments to `get_transcript` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the transcript. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Transcript](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Transcript)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Transcript](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Transcript)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetTranscriptRequest.new
    
    # Call the get_transcript method.
    result = client.get_transcript request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Transcript.
    p result

### #get_transcript_entry
    
    
    def get_transcript_entry(request, options = nil) -> ::Google::Apps::Meet::V2beta::TranscriptEntry
    def get_transcript_entry(name: nil) -> ::Google::Apps::Meet::V2beta::TranscriptEntry

Gets a `TranscriptEntry` resource by entry ID.

Note: The transcript entries returned by the Google Meet API might not match the transcription found in the Google Docs transcript file. This can occur when 1) we have interleaved speakers within milliseconds, or 2) the Google Docs transcript file is modified after generation.

**Overloads**
    
    
    def get_transcript_entry(request, options = nil) -> ::Google::Apps::Meet::V2beta::TranscriptEntry

Pass arguments to `get_transcript_entry` via a request object, either of type [GetTranscriptEntryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetTranscriptEntryRequest "Google::Apps::Meet::V2beta::GetTranscriptEntryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetTranscriptEntryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetTranscriptEntryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_transcript_entry(name: nil) -> ::Google::Apps::Meet::V2beta::TranscriptEntry

Pass arguments to `get_transcript_entry` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the `TranscriptEntry`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::TranscriptEntry](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-TranscriptEntry)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::TranscriptEntry](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-TranscriptEntry)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetTranscriptEntryRequest.new
    
    # Call the get_transcript_entry method.
    result = client.get_transcript_entry request
    
    # The returned object is of type Google::Apps::Meet::V2beta::TranscriptEntry.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ConferenceRecordsService REST client object.

**Yields**

  * (config) — Configure the ConferenceRecordsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecordsService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_conference_records
    
    
    def list_conference_records(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ConferenceRecord>
    def list_conference_records(page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ConferenceRecord>

Lists the conference records. By default, ordered by start time and in descending order.

**Overloads**
    
    
    def list_conference_records(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ConferenceRecord>

Pass arguments to `list_conference_records` via a request object, either of type [ListConferenceRecordsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListConferenceRecordsRequest "Google::Apps::Meet::V2beta::ListConferenceRecordsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListConferenceRecordsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListConferenceRecordsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_conference_records(page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ConferenceRecord>

Pass arguments to `list_conference_records` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **page_size** (::Integer) — 

Optional. Maximum number of conference records to return. The service might return fewer than this value. If unspecified, at most 25 conference records are returned. The maximum value is 100; values above 100 are coerced to

    1. Maximum might change in the future.
  * **page_token** (::String) — Optional. Page token returned from previous List Call. 
  * **filter** (::String) — 

Optional. User specified filtering condition in [EBNF format](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). The following are the filterable fields:

    * `space.meeting_code`
    * `space.name`
    * `start_time`
    * `end_time`

For example, consider the following filters:

    * `space.name = "spaces/NAME"`
    * `space.meeting_code = "abc-mnop-xyz"`
    * `start_time>="2024-01-01T00:00:00.000Z" AND start_time<="2024-01-02T00:00:00.000Z"`
    * `end_time IS NULL`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::ConferenceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecord)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::ConferenceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConferenceRecord)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListConferenceRecordsRequest.new
    
    # Call the list_conference_records method.
    result = client.list_conference_records request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::ConferenceRecord.
      p item
    end

### #list_participant_sessions
    
    
    def list_participant_sessions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ParticipantSession>
    def list_participant_sessions(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ParticipantSession>

Lists the participant sessions of a participant in a conference record. By default, ordered by join time and in descending order. This API supports `fields` as standard parameters like every other API. However, when the `fields` request parameter is omitted this API defaults to `'participantsessions/*, next_page_token'`.

**Overloads**
    
    
    def list_participant_sessions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ParticipantSession>

Pass arguments to `list_participant_sessions` via a request object, either of type [ListParticipantSessionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListParticipantSessionsRequest "Google::Apps::Meet::V2beta::ListParticipantSessionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListParticipantSessionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListParticipantSessionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_participant_sessions(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::ParticipantSession>

Pass arguments to `list_participant_sessions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}/participants/{participant}`
  * **page_size** (::Integer) — Optional. Maximum number of participant sessions to return. The service might return fewer than this value. If unspecified, at most 100 participants are returned. The maximum value is 250; values above 250 are coerced to 250. Maximum might change in the future. 
  * **page_token** (::String) — Optional. Page token returned from previous List Call. 
  * **filter** (::String) — Optional. User specified filtering condition in [EBNF format](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). The following are the filterable fields:

    * `start_time`
    * `end_time`

For example, `end_time IS NULL` returns active participant sessions in the conference record. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::ParticipantSession](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ParticipantSession)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::ParticipantSession](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ParticipantSession)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListParticipantSessionsRequest.new
    
    # Call the list_participant_sessions method.
    result = client.list_participant_sessions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::ParticipantSession.
      p item
    end

### #list_participants
    
    
    def list_participants(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Participant>
    def list_participants(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Participant>

Lists the participants in a conference record. By default, ordered by join time and in descending order. This API supports `fields` as standard parameters like every other API. However, when the `fields` request parameter is omitted, this API defaults to `'participants/*, next_page_token'`.

**Overloads**
    
    
    def list_participants(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Participant>

Pass arguments to `list_participants` via a request object, either of type [ListParticipantsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListParticipantsRequest "Google::Apps::Meet::V2beta::ListParticipantsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListParticipantsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListParticipantsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_participants(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Participant>

Pass arguments to `list_participants` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}`
  * **page_size** (::Integer) — Maximum number of participants to return. The service might return fewer than this value. If unspecified, at most 100 participants are returned. The maximum value is 250; values above 250 are coerced to 250. Maximum might change in the future. 
  * **page_token** (::String) — Page token returned from previous List Call. 
  * **filter** (::String) — Optional. User specified filtering condition in [EBNF format](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). The following are the filterable fields:

    * `earliest_start_time`
    * `latest_end_time`

For example, `latest_end_time IS NULL` returns active participants in the conference. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Participant)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Participant](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Participant)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListParticipantsRequest.new
    
    # Call the list_participants method.
    result = client.list_participants request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::Participant.
      p item
    end

### #list_recordings
    
    
    def list_recordings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Recording>
    def list_recordings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Recording>

Lists the recording resources from the conference record. By default, ordered by start time and in ascending order.

**Overloads**
    
    
    def list_recordings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Recording>

Pass arguments to `list_recordings` via a request object, either of type [ListRecordingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListRecordingsRequest "Google::Apps::Meet::V2beta::ListRecordingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListRecordingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListRecordingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_recordings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Recording>

Pass arguments to `list_recordings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}`
  * **page_size** (::Integer) — Maximum number of recordings to return. The service might return fewer than this value. If unspecified, at most 10 recordings are returned. The maximum value is 100; values above 100 are coerced to 100. Maximum might change in the future. 
  * **page_token** (::String) — Page token returned from previous List Call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Recording](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Recording)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Recording](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Recording)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListRecordingsRequest.new
    
    # Call the list_recordings method.
    result = client.list_recordings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::Recording.
      p item
    end

### #list_smart_notes
    
    
    def list_smart_notes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::SmartNote>
    def list_smart_notes(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::SmartNote>

Lists the set of smart notes from the conference record. By default, ordered by start time and in ascending order.

**Overloads**
    
    
    def list_smart_notes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::SmartNote>

Pass arguments to `list_smart_notes` via a request object, either of type [ListSmartNotesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListSmartNotesRequest "Google::Apps::Meet::V2beta::ListSmartNotesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListSmartNotesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListSmartNotesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_smart_notes(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::SmartNote>

Pass arguments to `list_smart_notes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}`
  * **page_size** (::Integer) — Optional. Maximum number of smart notes to return. The service might return fewer than this value. If unspecified, at most 10 smart notes are returned. The maximum value is 100; values above 100 are coerced to 100. Maximum might change in the future. 
  * **page_token** (::String) — Optional. Page token returned from previous List Call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::SmartNote](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SmartNote)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::SmartNote](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SmartNote)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListSmartNotesRequest.new
    
    # Call the list_smart_notes method.
    result = client.list_smart_notes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::SmartNote.
      p item
    end

### #list_transcript_entries
    
    
    def list_transcript_entries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::TranscriptEntry>
    def list_transcript_entries(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::TranscriptEntry>

Lists the structured transcript entries per transcript. By default, ordered by start time and in ascending order.

Note: The transcript entries returned by the Google Meet API might not match the transcription found in the Google Docs transcript file. This can occur when 1) we have interleaved speakers within milliseconds, or 2) the Google Docs transcript file is modified after generation.

**Overloads**
    
    
    def list_transcript_entries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::TranscriptEntry>

Pass arguments to `list_transcript_entries` via a request object, either of type [ListTranscriptEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListTranscriptEntriesRequest "Google::Apps::Meet::V2beta::ListTranscriptEntriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListTranscriptEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListTranscriptEntriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_transcript_entries(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::TranscriptEntry>

Pass arguments to `list_transcript_entries` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}/transcripts/{transcript}`
  * **page_size** (::Integer) — Maximum number of entries to return. The service might return fewer than this value. If unspecified, at most 10 entries are returned. The maximum value is 100; values above 100 are coerced to 100. Maximum might change in the future. 
  * **page_token** (::String) — Page token returned from previous List Call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::TranscriptEntry](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-TranscriptEntry)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::TranscriptEntry](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-TranscriptEntry)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListTranscriptEntriesRequest.new
    
    # Call the list_transcript_entries method.
    result = client.list_transcript_entries request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::TranscriptEntry.
      p item
    end

### #list_transcripts
    
    
    def list_transcripts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Transcript>
    def list_transcripts(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Transcript>

Lists the set of transcripts from the conference record. By default, ordered by start time and in ascending order.

**Overloads**
    
    
    def list_transcripts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Transcript>

Pass arguments to `list_transcripts` via a request object, either of type [ListTranscriptsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListTranscriptsRequest "Google::Apps::Meet::V2beta::ListTranscriptsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListTranscriptsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListTranscriptsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_transcripts(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Transcript>

Pass arguments to `list_transcripts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `conferenceRecords/{conference_record}`
  * **page_size** (::Integer) — Maximum number of transcripts to return. The service might return fewer than this value. If unspecified, at most 10 transcripts are returned. The maximum value is 100; values above 100 are coerced to 100. Maximum might change in the future. 
  * **page_token** (::String) — Page token returned from previous List Call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Transcript](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Transcript)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Transcript](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Transcript)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::ConferenceRecordsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListTranscriptsRequest.new
    
    # Call the list_transcripts method.
    result = client.list_transcripts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::Transcript.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
