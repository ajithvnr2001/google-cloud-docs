---
url: https://docs.cloud.google.com/dataflow/docs/support/using-unsupported-sdks/
title: Using an unsupported SDK \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:00.424187+00:00
---

# Using an unsupported SDK  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/support/using-unsupported-sdks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Using an unsupported SDK Stay organized with collections  Save and categorize content based on your preferences. 

Submitting jobs from an SDK version past its supported date results in interruptions and a reduction in throughput for long-running batch or streaming jobs. To mitigate potential issues, do the following:

  * [Upgrade the SDK version](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk#update-sdk) (Preferred)
  * Resubmit the job using a temporary token
  * Resume the disrupted job



For a list of all available SDK versions, see the [support status page](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status#apache-beam-sdks-2x).

### Starting jobs with unsupported SDK versions

When you submit a Dataflow job from an SDK version past its supported date, you receive an error message directing you to either [upgrade your SDK version](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk#update-sdk) or to use a temporary token when you submit your job.

The token value in the error message contains the datetime when the token expires as well as the token itself. The expiration date is set for two weeks in the future.

If you want to use the token, resubmit your job using the `unsupported_sdk_temporary_override_token` experiment flag and token value.
    
    
    --experiments=unsupported_sdk_temporary_override_token=TOKEN

If you submit a job using the token after it expires, you receive a different error message informing you of the expired status. You can either upgrade to a supported SDK version or resubmit your job without the token to get a new token.

Tokens are applied at the individual job level, so if you have multiple jobs scheduled, each job must use a unique token.

Tokens shouldn't be used as a permanent way to keep using an unsupported SDK. At some time after the unsupported date of an SDK, all tokens are revoked and all jobs using that unsupported SDK version are rejected. For more information about the support status of each SDK, see [SDK version support status](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status).

### Resuming disrupted jobs

Long-running Dataflow jobs that use unsupported SDKs, such as streaming jobs, are also disrupted and have their throughput significantly reduced. You can identify these disrupted jobs using the following error message in the job logs:

> The workflow was automatically disrupted by the service because it uses an unsupported SDK Apache Beam SDK for Python 2.3.0. Please upgrade to the latest SDK version. To resume the disrupted job temporarily, please use `gcloud alpha dataflow jobs resume-unsupported-sdk --token=TOKEN --region=REGION JOB_ID`. Note that the resumed job by this token will be disrupted again on 2020-08-28T11:21:58-07:00. For a list of supported SDK versions, see: https://cloud.google.com/dataflow/docs/support/sdk-version-support-status.

As the error suggests, you can mitigate the disruption by using the [resume-unsupported-sdk](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/jobs/resume-unsupported-sdk) command. Resuming a disrupted job is a temporary solution. Instead, upgrade your SDK version to avoid further deprecation actions.

Previously resumed jobs return to the disrupted state after the temporary token expires. You can resume any future disruptions in the same way. However, jobs running on unsupported SDK versions can be automatically canceled at some time after the unsupported date.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
