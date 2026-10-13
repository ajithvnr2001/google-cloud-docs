---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadCancelledError/
title: gapic-common - Class Gapic::Rest::ResumableUpload::UploadCancelledError (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:16.317910+00:00
---

# gapic-common - Class Gapic::Rest::ResumableUpload::UploadCancelledError (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadCancelledError/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::ResumableUpload::UploadCancelledError (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::ResumableUpload::UploadCancelledError.

Raised when the upload session was cancelled and will accept no further data.

Reachable today only for a cancellation this client did not request: the server reports an established session as cancelled while a chunk, a finalize, or a recovery query is in flight, because another process, another client, or a server-side policy ended it. Client-initiated cancellation is not part of the public API yet, and this error is also what that will raise.

Deliberately does not include [HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle "Gapic::Rest::ResumableUpload::HasResumeHandle \(module\)"). A cancelled session is gone server-side, so there is nothing to resume and retrying against it cannot succeed; a new upload must be started instead.

## Inherits

  * [Gapic::Common::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-Error)



## Methods 

### #initialize
    
    
    def initialize(message = "Upload session was cancelled") -> UploadCancelledError

Initializes a new UploadCancelledError.

**Parameter**

  * **message** (String) — Cancellation message 



**Returns**

  * ([UploadCancelledError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-UploadCancelledError)) — a new instance of UploadCancelledError 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
