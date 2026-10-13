---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload/
title: gapic-common - Class Gapic::ResumableUpload (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:15.441024+00:00
---

# gapic-common - Class Gapic::ResumableUpload (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::ResumableUpload (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::ResumableUpload.

Coordinates resumable uploads for a client method that performs them.

A client method that uploads media returns one of these handles instead of a response. No request is sent and no byte is read from the stream until [#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)") or [#resume](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_instance_ "Gapic::ResumableUpload#resume \(method\)") is called on it. Both are synchronous: they block the calling thread for the whole upload and return the decoded response message.

#### Reusable

A handle is reusable, and a failed run is resumed on the same object:

The stream handed to [#resume](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_instance_ "Gapic::ResumableUpload#resume \(method\)") must be positioned at byte 0 of the whole object, not at the server's acknowledged offset; the upload fast-forwards on its own, by seeking on a seekable stream or by reading and discarding on an unseekable one. An unseekable stream therefore has to be freshly opened rather than rewound.

A run that failed in a way the protocol can recover from leaves a [Gapic::Rest::ResumableUpload::ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)") behind, readable from [#resume_handle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_handle_instance_ "Gapic::ResumableUpload#resume_handle \(method\)") and also carried on the error. Persisting that handle lets a later process resume the same upload:

A completed upload is finalized: [#resume_handle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_handle_instance_ "Gapic::ResumableUpload#resume_handle \(method\)") returns `nil` and [#resumable?](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resumable__instance_ "Gapic::ResumableUpload#resumable? \(method\)") returns `false`, so there is no handle to resume from. Calling [#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)") again is permitted and begins a second, unrelated upload.

#### The Two Timeouts

An upload is bounded by two independent budgets, and they are three orders of magnitude apart:

| Budget | Set by | Covers | |---|---|---| | whole upload | `upload_timeout:` on [#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)") and [#resume](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_instance_ "Gapic::ResumableUpload#resume \(method\)") | every request, retry and byte of the run | | initiation request | per-call `timeout` | creating the session |

The per-call `timeout` a client method takes reaches only the initiation request. An upload still transferring bytes an hour later has long outlived it, and that is expected. To bound the run as a whole, pass `upload_timeout:`.

#### Threading

[#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)") and [#resume](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_instance_ "Gapic::ResumableUpload#resume \(method\)") block the calling thread, and the `on_progress` callback runs on that same thread. The readers ([#resume_handle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resume_handle_instance_ "Gapic::ResumableUpload#resume_handle \(method\)"), [#resumable?](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_resumable__instance_ "Gapic::ResumableUpload#resumable? \(method\)"), [#running?](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_running__instance_ "Gapic::ResumableUpload#running? \(method\)")) are guarded by an internal mutex and may be called from another thread mid-run; values read that way are a best-effort snapshot of a state the upload thread is still advancing.

#### Defaults

  * `chunk_size` defaults to 8 MB, then rounds down to a multiple of any chunk granularity the server requires.
  * `upload_timeout` defaults to `upload_size / 1 MB per second` when `upload_size` is known, floored at one hour, and to one hour flat when it is not.



#### Retry Policies

Retry behavior is partitioned across three policies. Only the initiation policy is caller-supplied; the other two are the protocol's own and govern the requests no call option describes.

| Policy | Governs | Default `retry_codes` | |---|---|---| | initiation | session initiation | the 4xx and 5xx sets below | | control plane | `query` and `cancel` | the 4xx and 5xx sets below | | data plane | `upload` and `finalize` | the 5xx set below only |

  * 4xx set: `ALREADY_EXISTS` (HTTP `409`), `RESOURCE_EXHAUSTED` (`429`), `CANCELLED` (`499`).
  * 5xx set: `INTERNAL` (HTTP `500`), `UNAVAILABLE` (`503`), `DEADLINE_EXCEEDED` (`504`).



None of the defaults carries a `retry_predicate`, so one supplied by the caller is consulted as-is, ahead of `retry_codes`. All three share the same backoff: `initial_delay` `1.0` s, `max_delay` `15.0` s, `multiplier` `1.3`.

Some decisions belong to the protocol and are made before a policy is asked:

  * Initiation and control plane requests are re-sent, within the policy's deadline, after a connection or TLS failure, and after a `200` response missing `X-Goog-Upload-Status`.
  * Data plane requests are never re-sent after an outcome that leaves the server offset unknown — a timeout, a connection failure, a missing status header, or any `4xx`. The upload re-queries the session and resumes from the offset the server reports instead.
  * Consecutive recovery attempts that make no progress back off on a single schedule, with the same delays as above; the schedule starts over once the server confirms new bytes.
  * A response carrying `X-Goog-Upload-Status: final` is never retried.



## Inherits

  * Object 



## Examples

Uploading, then resuming after a recoverable failure
    
    
    upload = client.create_media_upload request
    begin
      upload.start stream: File.open("movie.mp4", "rb"), content_type: "video/mp4"
    rescue Gapic::Rest::ResumableUpload::HasResumeHandle => e
      raise unless upload.resumable?
      upload.resume stream: File.open("movie.mp4", "rb")
    end

Resuming an upload started by an earlier process
    
    
    upload = client.create_media_upload
    upload.resume stream:        File.open("movie.mp4", "rb"),
                  resume_handle: Gapic::Rest::ResumableUpload::ResumeHandle.new(
                    upload_url: row[:upload_url], chunk_size: row[:chunk_size]
                  )

## Methods 

### #resumable?
    
    
    def resumable?() -> Boolean

Returns whether the last run left an upload that can be resumed.

**Returns**

  * (Boolean) 



### #resume
    
    
    def resume(stream:, resume_handle: nil, content_type: nil, upload_size: nil, upload_timeout: nil, on_progress: nil) -> Object

Resumes an upload session the server has already created, transferring whatever it has not yet acknowledged.

Blocks the calling thread until the upload completes or fails. A resumed run sends no initiation request, so it takes no initiation arguments and needs no request message.

The target is a [Gapic::Rest::ResumableUpload::ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)"): either the one passed in, or — when `resume_handle` is omitted — the one left behind by this handle's last run. The bare form raises `ArgumentError` when there is none, which covers a handle that has never run, a run that finished successfully, and a run that failed in a way the protocol considers unresumable.

Resuming against a finalized upload URL is undefined behavior: it queries the server and might return the response body or raise an error, depending on the server response.

**Parameters**

  * **stream** (IO) — Binary input stream to upload, positioned at byte 0 of the **whole object** , not at the server's acknowledged offset. The upload fast-forwards on its own, by seeking or by reading and discarding. Not closed after use. 
  * **resume_handle** (Gapic::Rest::ResumableUpload::ResumeHandle, nil) _(defaults to: nil)_ — Upload to resume. Defaults to the one left behind by this handle's last run. 
  * **content_type** (String, nil) _(defaults to: nil)_ — MIME type of the uploaded media. 
  * **upload_size** (Integer, nil) _(defaults to: nil)_ — Total upload bytes, if known upfront. 
  * **upload_timeout** (Numeric, nil) _(defaults to: nil)_ — Budget in seconds for the **whole run**. See [#start](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ResumableUpload#Gapic__ResumableUpload_start_instance_ "Gapic::ResumableUpload#start \(method\)"). 
  * **on_progress** (Proc, nil) _(defaults to: nil)_ — Called as `->(progress)` with a [Gapic::Rest::ResumableUpload::Progress](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__Progress "Gapic::Rest::ResumableUpload::Progress \(constant\)") instance. Runs synchronously on the upload thread and must not block. 



**Returns**

  * (Object) — The final response decoded into the handle's response type. 



**Raises**

  * (ArgumentError) — If there is no upload to resume, if the stream is not positioned at byte 0, or if the client cannot perform REST calls 
  * ([Gapic::Rest::ResumableUpload::SessionStateError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-SessionStateError)) — If a run is already in progress 
  * ([Gapic::Rest::ResumableUpload::RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError)) — If a transport error, timeout, or retry exhaustion occurs 
  * ([Gapic::Rest::ResumableUpload::DeadlineExceededError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-DeadlineExceededError)) — If `upload_timeout` is exceeded 
  * ([Gapic::Rest::ResumableUpload::BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError)) — If an unexpected or malformed HTTP response is received 
  * ([Gapic::Rest::ResumableUpload::UnseekableStreamError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UnseekableStreamError)) — If stream rewinding is required during recovery on an unseekable stream 
  * ([Gapic::Rest::ResumableUpload::StreamMismatchError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-StreamMismatchError)) — If stream content or length does not match the resumed upload 
  * ([Gapic::Rest::ResumableUpload::UploadRejectedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadRejectedError)) — If the server explicitly rejects the upload 
  * ([Gapic::Common::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-Error)) — Any other subclass signals a protocol implementation bug rather than a caller or server error 



### #resume_handle
    
    
    def resume_handle() -> Gapic::Rest::ResumableUpload::ResumeHandle, nil

Returns the handle needed to resume the last run, carrying its upload URL and resolved chunk size.

`nil` before the first run, and after any run that left nothing to resume: a completed upload is finalized, and rejected and cancelled uploads are too.

Each run replaces this value rather than accumulating handles, so it always describes the most recent one. Starting a second upload therefore discards whatever the previous run left behind — persist the handle first if the earlier upload still matters. A call that fails while building its configuration does not count as a run: it never reaches a driver, so the earlier value survives.

**Returns**

  * (Gapic::Rest::ResumableUpload::ResumeHandle, nil) 



### #running?
    
    
    def running?() -> Boolean

Returns whether a run is currently executing.

**Returns**

  * (Boolean) 



### #start
    
    
    def start(stream:, content_type: nil, upload_size: nil, chunk_size: nil, upload_timeout: nil, on_progress: nil) -> Object

Creates an upload session on the server and transfers the stream into it.

Blocks the calling thread until the upload completes or fails. The stream is assumed to be positioned at byte 0 (it is not rewound before reading) and is not closed after use.

**Parameters**

  * **stream** (IO) — Binary input stream to upload, positioned at byte 0. 
  * **content_type** (String, nil) _(defaults to: nil)_ — MIME type of the uploaded media. 
  * **upload_size** (Integer, nil) _(defaults to: nil)_ — Total upload bytes, if known upfront. 
  * **chunk_size** (Integer, nil) _(defaults to: nil)_ — Requested chunk size in bytes, defaulting to 8 MB. The effective size is rounded down to a multiple of any chunk granularity the server requires, or raised to that granularity if it exceeds the requested size. A resumed run has no such argument: it takes its chunk size from the [Gapic::Rest::ResumableUpload::ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)"). 
  * **upload_timeout** (Numeric, nil) _(defaults to: nil)_ — Budget in seconds for the **whole run** — every request, every retry, every byte — not for any single request. The per-call `timeout` a client method takes bounds the initiation request alone. When `nil`, resolves to `upload_size / 1 MB per second` floored at one hour if `upload_size` is known, and to one hour flat otherwise. 
  * **on_progress** (Proc, nil) _(defaults to: nil)_ — Called as `->(progress)` with a [Gapic::Rest::ResumableUpload::Progress](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__Progress "Gapic::Rest::ResumableUpload::Progress \(constant\)") instance. Runs synchronously on the upload thread and must not block; an exception raised inside it aborts the run and propagates out of this method. 



**Returns**

  * (Object) — The final response decoded into the handle's response type. 



**Raises**

  * (ArgumentError) — If the call metadata sets a reserved `X-Goog-Upload-*` protocol header, or if the client cannot perform REST calls 
  * ([Gapic::Rest::ResumableUpload::SessionStateError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-SessionStateError)) — If a run is already in progress 
  * ([Gapic::Rest::ResumableUpload::RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError)) — If a transport error, timeout, or retry exhaustion occurs 
  * ([Gapic::Rest::ResumableUpload::DeadlineExceededError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-DeadlineExceededError)) — If `upload_timeout` is exceeded 
  * ([Gapic::Rest::ResumableUpload::BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError)) — If an unexpected or malformed HTTP response is received 
  * ([Gapic::Rest::ResumableUpload::UnseekableStreamError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UnseekableStreamError)) — If stream rewinding is required during recovery on an unseekable stream 
  * ([Gapic::Rest::ResumableUpload::StreamMismatchError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-StreamMismatchError)) — If stream content or length does not match protocol expectations 
  * ([Gapic::Rest::ResumableUpload::UploadRejectedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadRejectedError)) — If the server explicitly rejects the upload 
  * ([Gapic::Common::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-Error)) — Any other subclass signals a protocol implementation bug rather than a caller or server error 



**Example**
    
    
    response = upload.start stream:         File.open("movie.mp4", "rb"),
                            content_type:   "video/mp4",
                            upload_size:    File.size("movie.mp4"),
                            upload_timeout: 4 * 3600,
                            on_progress:    ->(p) { puts "#{p.phase}: #{p.bytes_uploaded}" }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
