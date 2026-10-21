---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/conditions/update/
title: gcloud alpha monitoring policies conditions update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:14.460086+00:00
---

# gcloud alpha monitoring policies conditions update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/conditions/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha monitoring policies conditions update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha monitoring policies conditions update - update a condition in an alerting policy 
SYNOPSIS
    

`gcloud alpha monitoring policies conditions update` (`CONDITION` : `--policy`=`POLICY`) [`--display-name`=`DISPLAY_NAME`] [`--if`=`IF_VALUE`] [`--trigger-count`=`TRIGGER_COUNT` | `--trigger-percent`=`TRIGGER_PERCENT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a condition in an alerting policy. 
POSITIONAL ARGUMENTS
    

Condition resource - The name of the Condition to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `condition` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONDITION`
     ID of the condition or fully qualified identifier for the condition. 

To set the `condition` attribute: 

  * provide the argument `condition` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     Name of the alerting policy. 

To set the `policy` attribute: 

  * provide the argument `condition` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line. 


FLAGS
    

`--display-name`=`DISPLAY_NAME`
     The display name for the Condition. 
`--if`=`IF_VALUE`
     One of "absent", "< THRESHOLD", "> THRESHOLD" where "THRESHOLD" is an integer or float. 
At most one of these can be specified: 

`--trigger-count`=`TRIGGER_COUNT`
     The absolute number of time series that must fail the predicate for the condition to be triggered. 
`--trigger-percent`=`TRIGGER_PERCENT`
     The percentage of time series that must fail the predicate for the condition to be triggered. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud monitoring policies conditions update](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/conditions/update)
    
    
    [gcloud beta monitoring policies conditions update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/policies/conditions/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
