---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-prediction-resume/
title: Resume an incomplete batch inference job \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:42:17.513475+00:00
---

# Resume an incomplete batch inference job  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-prediction-resume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Resume an incomplete batch inference job Stay organized with collections  Save and categorize content based on your preferences. 

If an Agent Platform batch inference job fails, is canceled, or expires, you can resume it by creating a new batch job. The new job processes only the incomplete or failed requests from the previous job and merges the new results with those from the previously completed requests. For example, if the incomplete batch job was 90% complete, the new job processes the remaining 10% of the requests.

To resume a batch job, create a new batch job, supplying the [Cloud Storage file](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-cloud-storage) or [BigQuery table output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-bigquery) as input to the new job.

**Note:** In rare cases where users modify the output file of the job before resuming, the system resumes from the modified output file. The system doesn't validate whether the output file has been modified.

## What's next

  * Learn more about [Batch inference from Cloud Storage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-cloud-storage).
  * Learn more about [Batch inference for BigQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
