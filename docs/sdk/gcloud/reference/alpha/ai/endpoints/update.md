---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/update/
title: gcloud alpha ai endpoints update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:21.887571+00:00
---

# gcloud alpha ai endpoints update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai endpoints update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai endpoints update - update an existing Vertex AI endpoint 
SYNOPSIS
    

`gcloud alpha ai endpoints update` (`ENDPOINT` : `--region`=`REGION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--clear-traffic-split` | `--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`--disable-request-response-logging` | `--request-response-logging-rate`=`REQUEST_RESPONSE_LOGGING_RATE` `--request-response-logging-table`=`REQUEST_RESPONSE_LOGGING_TABLE`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To update an endpoint ``123`` under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud alpha ai endpoints update 123 --project=example --region=us-central1 --display-name=new_name

POSITIONAL ARGUMENTS
    

Endpoint resource - The endpoint to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `name` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the endpoint. 

To set the `region` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the endpoint. 
`--display-name`=`DISPLAY_NAME`
     Display name of the endpoint. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha ai endpoints update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha ai endpoints update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--clear-traffic-split`
     Clears the traffic split map. If the map is empty, the endpoint is to not accept any traffic at the moment. 
`--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]
     List of pairs of deployed model id and value to set as traffic split. 
At most one of these can be specified: 

`--disable-request-response-logging`
     Disable prediction request & response logging. 
Or at least one of these can be specified: 

`--request-response-logging-rate`=`REQUEST_RESPONSE_LOGGING_RATE`
     Prediction request & response sampling rate for logging to BigQuery table. 
`--request-response-logging-table`=`REQUEST_RESPONSE_LOGGING_TABLE`
     BigQuery table uri for prediction request & response logging. 

You can provide table uri that does not exist, it will be created for you. 

Value should be provided in format: bq://``PROJECT_ID``/``DATASET``/``TABLE``

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai endpoints update](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/update)
    
    
    [gcloud beta ai endpoints update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
