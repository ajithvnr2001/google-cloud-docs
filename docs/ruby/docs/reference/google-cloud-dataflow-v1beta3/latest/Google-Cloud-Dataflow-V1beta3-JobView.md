---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-JobView/
title: Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::JobView (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:29.826766+00:00
---

# Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::JobView (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-JobView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::JobView (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API module Google::Cloud::Dataflow::V1beta3::JobView.

Selector for how much information is returned in Job responses.

## Constants 

### JOB_VIEW_UNKNOWN

**value:** 0  
The job view to return isn't specified, or is unknown. Responses will contain at least the `JOB_VIEW_SUMMARY` information, and may contain additional information.

### JOB_VIEW_SUMMARY

**value:** 1  
Request summary information only: Project ID, Job ID, job name, job type, job status, start/end time, and Cloud SDK version details.

### JOB_VIEW_ALL

**value:** 2  
Request all information available for this job. When the job is in `JOB_STATE_PENDING`, the job has been created but is not yet running, and not all job information is available. For complete job information, wait until the job in is `JOB_STATE_RUNNING`. For more information, see [JobState](https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#jobstate).

### JOB_VIEW_DESCRIPTION

**value:** 3  
Request summary info and limited job description data for steps, labels and environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
