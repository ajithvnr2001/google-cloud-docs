---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle/
title: gapic-common - Module Gapic::Rest::ResumableUpload::HasResumeHandle (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:27.407480+00:00
---

# gapic-common - Module Gapic::Rest::ResumableUpload::HasResumeHandle (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Module Gapic::Rest::ResumableUpload::HasResumeHandle (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common module Gapic::Rest::ResumableUpload::HasResumeHandle.

Mixin providing [ResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload#Gapic__Rest__ResumableUpload__ResumeHandle "Gapic::Rest::ResumableUpload::ResumeHandle \(constant\)") access and uniform formatting for resumable errors.

Every error that may carry a resume handle includes this module, so it doubles as the rescue target for "this upload failed but can be retried from where it stopped":

Included by [RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError "Gapic::Rest::ResumableUpload::RequestFailedError \(class\)"), [DeadlineExceededError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-DeadlineExceededError "Gapic::Rest::ResumableUpload::DeadlineExceededError \(class\)"), [BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError "Gapic::Rest::ResumableUpload::BadResponseError \(class\)"), [UnseekableStreamError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UnseekableStreamError "Gapic::Rest::ResumableUpload::UnseekableStreamError \(class\)") and [StreamMismatchError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-StreamMismatchError "Gapic::Rest::ResumableUpload::StreamMismatchError \(class\)").

Deliberately **not** included by [UploadRejectedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadRejectedError "Gapic::Rest::ResumableUpload::UploadRejectedError \(class\)"), [UploadCancelledError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadCancelledError "Gapic::Rest::ResumableUpload::UploadCancelledError \(class\)") or [SessionStateError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-SessionStateError "Gapic::Rest::ResumableUpload::SessionStateError \(class\)"): the first two mean the session is permanently terminated on the server and the third is a caller misuse, so none of them is retryable. Note also that `resume_handle` may still be `nil` on an including error, for instance when the failure happened before initiation established an upload URL.

## Included In

  * [Gapic::Rest::ResumableUpload::BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError)
  * [Gapic::Rest::ResumableUpload::DeadlineExceededError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-DeadlineExceededError)
  * [Gapic::Rest::ResumableUpload::RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError)
  * [Gapic::Rest::ResumableUpload::StreamMismatchError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-StreamMismatchError)
  * [Gapic::Rest::ResumableUpload::UnseekableStreamError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UnseekableStreamError)



## Example
    
    
    begin
      upload.start stream: io, upload_size: size
    rescue Gapic::Rest::ResumableUpload::HasResumeHandle => e
      retry_later e.resume_handle if e.resume_handle
      raise
    end

## Methods 

### #resume_handle
    
    
    def resume_handle() -> Gapic::Rest::ResumableUpload::ResumeHandle, nil

**Returns**

  * (Gapic::Rest::ResumableUpload::ResumeHandle, nil) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
