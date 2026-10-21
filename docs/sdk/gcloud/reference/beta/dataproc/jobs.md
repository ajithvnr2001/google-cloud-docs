---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/
title: gcloud beta dataproc jobs \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:53.637763+00:00
---

# gcloud beta dataproc jobs  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc jobs Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc jobs - submit and manage Dataproc jobs 
SYNOPSIS
    

`gcloud beta dataproc jobs` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Submit and manage Dataproc jobs. 
EXAMPLES
     To learn about the types of jobs that can be submitted, run: 
    
    
    [gcloud beta dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit)

To view the output of a job as it runs, run: 
    
    
    [gcloud beta dataproc jobs wait](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/wait) job_id

To cancel an active job, run: 
    
    
    [gcloud beta dataproc jobs kill](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/kill) job_id

To view the details of a job, run: 
    
    
    [gcloud beta dataproc jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/describe) job_id

To see the list of all jobs, run: 
    
    
    [gcloud beta dataproc jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/list)

To delete the record of an inactive job, run: 
    
    
    [gcloud beta dataproc jobs delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/delete) job_id

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[submit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit)`
     `(BETA)` Submit Dataproc jobs to execute on a cluster. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/delete)`
     `(BETA)` Delete the record of an inactive job. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/describe)`
     `(BETA)` View the details of a job. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/get-iam-policy)`
     `(BETA)` Get IAM policy for a job. 
`[kill](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/kill)`
     `(BETA)` Kill an active job. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/list)`
     `(BETA)` List jobs in a project. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/set-iam-policy)`
     `(BETA)` Set IAM policy for a job. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/update)`
     `(BETA)` Update the labels for a job. 
`[wait](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/wait)`
     `(BETA)` View the output of a job as it runs or after it completes. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc jobs](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs)
    
    
    [gcloud alpha dataproc jobs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
