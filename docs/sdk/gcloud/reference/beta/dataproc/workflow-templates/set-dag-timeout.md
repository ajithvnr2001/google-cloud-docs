---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-dag-timeout/
title: gcloud beta dataproc workflow-templates set-dag-timeout \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:09:01.100383+00:00
---

# gcloud beta dataproc workflow-templates set-dag-timeout  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-dag-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc workflow-templates set-dag-timeout Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc workflow-templates set-dag-timeout - set DAG timeout on a workflow template 
SYNOPSIS
    

`gcloud beta dataproc workflow-templates set-dag-timeout` (`TEMPLATE` : `--region`=`REGION`) `--dag-timeout`=`DAG_TIMEOUT` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Set DAG timeout on a workflow template. 
EXAMPLES
     To add a DAG timeout of 2h (or update an existing one to 2h) on a workflow template named ``my-workflow-template`` in region ``us-central1``, run: 
    
    
    gcloud beta dataproc workflow-templates set-dag-timeout my-workflow-template --region=us-central1 --dag-timeout=2h"

POSITIONAL ARGUMENTS
    

Template resource - The name of the workflow template to set the DAG timeout on. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TEMPLATE`
     ID of the template or fully qualified identifier for the template. 

To set the `template` attribute: 

  * provide the argument `template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Dataproc region for the template. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `template` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


REQUIRED FLAGS
    

`--dag-timeout`=`DAG_TIMEOUT`
     The duration for which a DAG of jobs can run before being auto-cancelled, such as "10m" or "16h". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc workflow-templates set-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-dag-timeout)
    
    
    [gcloud alpha dataproc workflow-templates set-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-dag-timeout)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
