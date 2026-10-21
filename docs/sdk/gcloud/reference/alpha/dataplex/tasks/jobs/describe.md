---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/tasks/jobs/describe/
title: gcloud alpha dataplex tasks jobs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:53.090666+00:00
---

# gcloud alpha dataplex tasks jobs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/tasks/jobs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex tasks jobs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex tasks jobs describe - describe a Dataplex job running a particular task 
SYNOPSIS
    

`gcloud alpha dataplex tasks jobs describe` (`JOB` : `--lake`=`LAKE` `--location`=`LOCATION` `--task`=`TASK`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a Dataplex job running a particular task. 

Displays all details of a Dataplex job given a valid job ID. 

EXAMPLES
     To describe a Dataplex job `test-job` running a task `test-task` within lake `test-lake` in location `us-central1`, run: 
    
    
    gcloud alpha dataplex tasks jobs describe test-job --location=us-central1 --lake=test-lake --task=test-task

POSITIONAL ARGUMENTS
    

Job resource - Arguments and flags that define the Dataplex Job running a particular Task you want to retrieve. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `job` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`JOB`
     ID of the job or fully qualified identifier for the job. 

To set the `job` attribute: 

  * provide the argument `job` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--lake`=`LAKE`
     Identifier of the Dataplex lake resource. To set the `lake` attribute: 

  * provide the argument `job` on the command line with a fully specified name; 
  * provide the argument `--lake` on the command line. 


`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `job` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


`--task`=`TASK`
     Identifier of the Dataplex task resource. To set the `task` attribute: 

  * provide the argument `job` on the command line with a fully specified name; 
  * provide the argument `--task` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dataplex/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataplex/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex tasks jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/tasks/jobs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
