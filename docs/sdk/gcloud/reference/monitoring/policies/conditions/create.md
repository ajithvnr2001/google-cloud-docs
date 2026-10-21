---
url: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/conditions/create/
title: gcloud monitoring policies conditions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:32.569181+00:00
---

# gcloud monitoring policies conditions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/conditions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud monitoring policies conditions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud monitoring policies conditions create - create a condition in an alerting policy 
SYNOPSIS
    

`gcloud monitoring policies conditions create` `ALERT_POLICY` [`--aggregation`=`AGGREGATION` `--condition-display-name`=`CONDITION_DISPLAY_NAME` `--condition-filter`=`CONDITION_FILTER` `--duration`=`DURATION` `--if`=`IF_VALUE` `--trigger-count`=`TRIGGER_COUNT` | `--trigger-percent`=`TRIGGER_PERCENT`] [`--condition`=`CONDITION` | `--condition-from-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a condition in an alerting policy. 
POSITIONAL ARGUMENTS
    

Alert Policy resource - Name of the Alert Policy to add a condition to. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `alert_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ALERT_POLICY`
     ID of the Alert Policy or fully qualified identifier for the Alert Policy. 

To set the `policy` attribute: 

  * provide the argument `alert_policy` on the command line. 


FLAGS
    

Condition Settings. This will add a condition to the created policy. If any conditions are already specified, this condition will be appended. 
`--aggregation`=`AGGREGATION`
     Specifies an Aggregation message as a JSON/YAML value to be applied to the condition. For more information about the format: <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies>
`--condition-display-name`=`CONDITION_DISPLAY_NAME`
     The display name for the condition. 
`--condition-filter`=`CONDITION_FILTER`
     Specifies the "filter" in a metric absence or metric threshold condition. 
`--duration`=`DURATION`
     The duration (e.g. "60s", "2min", etc.) that the condition must hold in order to trigger as true. 
`--if`=`IF_VALUE`
     One of "absent", "< THRESHOLD", "> THRESHOLD" where "THRESHOLD" is an integer or float. 
At most one of these can be specified: 

`--trigger-count`=`TRIGGER_COUNT`
     The absolute number of time series that must fail the predicate for the condition to be triggered. 
`--trigger-percent`=`TRIGGER_PERCENT`
     The percentage of time series that must fail the predicate for the condition to be triggered. 
At most one of these can be specified: 

`--condition`=`CONDITION`
     The condition as a string. In either JSON or YAML format. 
`--condition-from-file`=`PATH_TO_FILE`
     The path to a JSON or YAML file containing the condition. Use a full or relative path to a local file containing the value of condition. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha monitoring policies conditions create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/conditions/create)
    
    
    [gcloud beta monitoring policies conditions create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/policies/conditions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
