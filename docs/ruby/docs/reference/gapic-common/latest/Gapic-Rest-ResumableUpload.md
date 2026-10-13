---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload/
title: gapic-common - Module Gapic::Rest::ResumableUpload (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:13.574873+00:00
---

# gapic-common - Module Gapic::Rest::ResumableUpload (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Module Gapic::Rest::ResumableUpload (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common module Gapic::Rest::ResumableUpload.

Resumable Upload Protocol implementation for REST transport: session initiation, chunked streaming, automatic retries, progress reporting via [Progress](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__Progress "Gapic::Rest::ResumableUpload::Progress \(constant\)"), and resumption via [ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)").

**This namespace has no callable surface.** Every method and class in it is internal machinery, documented as `@private` and excluded from these docs; what remains visible is the data a caller receives — [Progress](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__Progress "Gapic::Rest::ResumableUpload::Progress \(constant\)"), [ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)"), [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)") — and the error classes listed below. Uploads are driven from [Gapic::ResumableUpload](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload "Gapic::ResumableUpload \(class\)"), which sits above this namespace and coordinates runs against it.

Errors raised from here carry a [ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)") where the upload can still be continued, so the usual shape of handling one is to rescue [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)") and hand the handle back to the coordinator:

#### Error Types

  * [RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError "Gapic::Rest::ResumableUpload::RequestFailedError \(class\)") \- Transport connection failure, timeout, or retries exhausted (includes [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)")).
  * [DeadlineExceededError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-DeadlineExceededError "Gapic::Rest::ResumableUpload::DeadlineExceededError \(class\)") \- Whole-upload timeout exceeded (includes [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)")).
  * [BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError "Gapic::Rest::ResumableUpload::BadResponseError \(class\)") \- Unexpected, malformed, or out-of-phase HTTP response (includes [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)")).
  * [UnseekableStreamError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UnseekableStreamError "Gapic::Rest::ResumableUpload::UnseekableStreamError \(class\)") \- Stream rewinding required on an unseekable stream (includes [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)")).
  * [StreamMismatchError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-StreamMismatchError "Gapic::Rest::ResumableUpload::StreamMismatchError \(class\)") \- Stream content or length does not match resumed upload (includes [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)")).
  * [UploadRejectedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadRejectedError "Gapic::Rest::ResumableUpload::UploadRejectedError \(class\)") \- Server explicitly rejected the upload session (final).
  * [UploadCancelledError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadCancelledError "Gapic::Rest::ResumableUpload::UploadCancelledError \(class\)") \- Upload session was cancelled on the server while the upload was in flight. A cancelled session cannot be resumed, so this error carries no [ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)") (final).
  * [SessionStateError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-SessionStateError "Gapic::Rest::ResumableUpload::SessionStateError \(class\)") \- Upload session lifecycle rule violation, e.g. starting a second run while one is in flight (final).
  * Any other `Gapic::Common::Error` subclass signals a protocol implementation bug rather than a caller or server error (final).



## Example

Uploading, then resuming after a recoverable failure
    
    
    upload = client.upload_media ... # returns a Gapic::ResumableUpload
    begin
      upload.start stream: File.open("movie.mp4", "rb"), upload_size: File.size("movie.mp4")
    rescue Gapic::Rest::ResumableUpload::HasResumeHandle => e
      raise unless e.resume_handle
      upload.resume stream: File.open("movie.mp4", "rb"), resume_handle: e.resume_handle
    end

## Methods 

### #bytes_uploaded
    
    
    def bytes_uploaded() -> Integer

**Returns**

  * (Integer) — Cumulative bytes acknowledged by the server. Note that this is the server-confirmed offset and is not guaranteed to be monotonic — a server rewind during recovery can decrease this value. 



### #chunk_granularity
    
    
    def chunk_granularity() -> Integer, nil

**Returns**

  * (Integer, nil) — Alignment modulus returned by server 



### #chunk_size
    
    
    def chunk_size() -> Integer

**Returns**

  * (Integer) — Resolved effective chunk size in bytes 



### #from_status
    
    
    def from_status() -> Symbol

**Returns**

  * (Symbol) — The protocol status before the transition 



### #in_flight_length
    
    
    def in_flight_length() -> Integer

**Returns**

  * (Integer) — Byte length of in-flight chunk currently being transmitted 



### #initial_body
    
    
    def initial_body() -> String, nil

**Returns**

  * (String, nil) — Request payload for session initiation 



### #initial_headers
    
    
    def initial_headers() -> Hash<String, String>

**Returns**

  * (Hash<String, String>) — Additional headers for initiation, merged over the driver's own headers. Keys in [RESERVED_INITIAL_HEADERS](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__RESERVED_INITIAL_HEADERS "Gapic::Rest::ResumableUpload::RESERVED_INITIAL_HEADERS \(constant\)") are rejected in any casing; use `content_type` and `upload_size` to shape those. 



### #initial_url
    
    
    def initial_url() -> String

**Returns**

  * (String) — Initial endpoint URI for session initiation 



### #instructions
    
    
    def instructions() -> Array<Object>

**Returns**

  * (Array<Object>) — Emitted instructions for the Driver 



### #last_error
    
    
    def last_error() -> StandardError, nil

**Returns**

  * (StandardError, nil) — Terminal exception if in an error or rejected status 



### #next_state
    
    
    def next_state() -> State

**Returns**

  * (State) — The new protocol state snapshot after transition 



### #offset
    
    
    def offset() -> Integer

**Returns**

  * (Integer) — Contiguous bytes acknowledged by server 



### #phase
    
    
    def phase() -> Symbol

**Returns**

  * (Symbol) — Current upload phase, one of {Progress::PHASES} 



### #recipe
    
    
    def recipe() -> Symbol

**Returns**

  * (Symbol) — Selected transition recipe method name 



### #recovery_offset
    
    
    def recovery_offset() -> Integer, nil

**Returns**

  * (Integer, nil) — Server-confirmed offset when the open recovery episode began, or `nil` when no episode is open. A recovery episode is the run of consecutive recovery attempts during which the confirmed offset does not advance; every query in it after the first waits for the next backoff delay. See `design/resumable_upload/implementation-guide.md` section 6.2.1. 



### #shape
    
    
    def shape() -> Symbol

**Returns**

  * (Symbol) — The canonical event shape 



### #start_retry_policy
    
    
    def start_retry_policy() -> Gapic::Common::RetryPolicy, Hash, nil

**Returns**

  * ([Gapic::Common::RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy), Hash, nil) — Retry policy for session initiation 



### #status
    
    
    def status() -> Symbol

**Returns**

  * (Symbol) — Protocol lifecycle status, one of [Rules::STATUSES](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-Rules#Gapic__Rest__ResumableUpload__Rules__STATUSES "Gapic::Rest::ResumableUpload::Rules::STATUSES \(constant\)")



### #total_bytes
    
    
    def total_bytes() -> Integer, nil

**Returns**

  * (Integer, nil) — Total upload size in bytes if known, or `nil`. Always set on the `:completed` phase — the total is known once the transfer finishes, even when `upload_size` was not supplied upfront. 



### #upload_url
    
    
    def upload_url() -> String, nil

**Returns**

  * (String, nil) — Session upload URL returned by the upload backend 



## Constants 

### Progress

**value:** Data.define( :phase, :bytes_uploaded, :total_bytes ) do

# Initializes a new progress snapshot.

#

# @raise [ArgumentError] If the phase is not one of {Progress::PHASES}

# def initialize phase:, bytes_uploaded:, total_bytes: nil

# Must use `self.class::` to access constants from the class scope
    
    
    unless self.class::PHASES.include? phase
      raise ArgumentError, &quot;Invalid phase: #{phase.inspect}. Expected one of #{self.class::PHASES.inspect}&quot;
    end</p>
    
    
    
    super(
      phase:          phase,
      bytes_uploaded: bytes_uploaded,
      total_bytes:    total_bytes
    )
    

end end  
Immutable progress snapshot passed to the `on_progress` callback.

The `on_progress` callback runs synchronously on the same thread as the upload protocol and must not block. Any exception raised inside the callback aborts the upload session and propagates out of [Gapic::ResumableUpload#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)") or [Gapic::ResumableUpload#resume](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_instance_ "Gapic::ResumableUpload#resume \(method\)").

### ResumeHandle

**value:** Data.define( :upload_url, :chunk_size ) do

# Initializes a new resume handle.

#

# @param chunk_size [Integer] Effective chunk size in bytes

# def initialize upload_url:, chunk_size: super( upload_url: upload_url, chunk_size: chunk_size ) end end  
Immutable handle containing parameters necessary to resume an in-progress upload session. These parameters are provided by the server and can be persisted to resume the upload at a later time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
