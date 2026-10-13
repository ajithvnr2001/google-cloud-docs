---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create/
title: gcloud dataproc workflow-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:18.645302+00:00
---

# gcloud dataproc workflow-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataproc workflow-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataproc workflow-templates create - create a workflow template 
SYNOPSIS
    

`gcloud dataproc workflow-templates create` (`TEMPLATE` : `--region`=`REGION`) [`--dag-timeout`=`DAG_TIMEOUT`] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a workflow template. 
EXAMPLES
     To create a workflow template named ``my-workflow-template`` in region ``us-central1`` with label params 'key1'='value1' and 'key2'='value2', run: 
    
    
    gcloud dataproc workflow-templates create my-workflow-template --region=us-central1 --labels="key1=value1,key2=value2"

POSITIONAL ARGUMENTS
    

Template resource - The name of the workflow template to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--dag-timeout`=`DAG_TIMEOUT`
     The duration for which a DAG of jobs can run before being auto-cancelled, such as "10m" or "16h". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--kms-key`=`KMS_KEY`
     The KMS key used to encrypt sensitive data in the workflow template. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/create)
    
    
    [gcloud beta dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
