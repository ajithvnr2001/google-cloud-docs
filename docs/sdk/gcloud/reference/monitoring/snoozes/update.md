---
url: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update/
title: gcloud monitoring snoozes update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:33:12.236701+00:00
---

# gcloud monitoring snoozes update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud monitoring snoozes update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud monitoring snoozes update - updates a snooze 
SYNOPSIS
    

`gcloud monitoring snoozes update` `SNOOZE` [`--snooze-from-file`=`PATH_TO_FILE`] [`--fields`=[`field`,…] | `--display-name`=`DISPLAY_NAME` `--end-time`=`END_TIME` `--start-time`=`START_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a snooze. 

If `--snooze-from-file` is specified, then the update rules depend on the value of the (optional) `--fields` flag: 

  * If `--fields` is specified, then only the specified fields of the snooze are updated. 
  * Else, all fields of the snooze are replaced. The updated snooze can be modified further using the flags from the Snooze Settings group below. 



Otherwise, the snooze will be updated with the values specified in the flags from the Snooze Settings group. 

For information about the JSON/YAML format of a snooze: <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes>

EXAMPLES
     To update a snooze time interval with command-line options, run: 
    
    
    gcloud monitoring snoozes update MY-SNOOZE --start-time=START_TIME --end-time=END_TIME

To update a snooze display name with a file, run: 
    
    
    gcloud monitoring snoozes update --snooze-from-file=MY-FILE --fields=display_name

Sample contents of MY-FILE: 
    
    
    criteria:
      policies:
      - projects/MY-PROJECT/alertPolicies/MY-POLICY
    interval:
      startTime: '2024-03-01T08:00:00Z'
      endTime: '2024-03-08T04:59:59.500Z'
    displayName: New Snooze with New Display Name

POSITIONAL ARGUMENTS
    

Snooze resource - Name of the Snooze to be updated. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `snooze` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SNOOZE`
     ID of the Snooze or fully qualified identifier for the Snooze. 

To set the `snooze` attribute: 

  * provide the argument `snooze` on the command line. 


FLAGS
    

`--snooze-from-file`=`PATH_TO_FILE`
     The path to a JSON or YAML file containing the snooze. Use a full or relative path to a local file containing the value of snooze. 
At most one of these can be specified: 

`--fields`=[`field`,…]
     The list of fields to update. Must specify `--snooze-from-file` if using this flag. 
Or at least one of these can be specified: 

Snooze Settings. If any of these are specified, they will overwrite fields in the `--snooze-from-file` flags if specified. 
`--display-name`=`DISPLAY_NAME`
     The display name for the Snooze. 
`--end-time`=`END_TIME`
     The end time for the Snooze. 
`--start-time`=`START_TIME`
     The start time for the Snooze. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha monitoring snoozes update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/snoozes/update)
    
    
    [gcloud beta monitoring snoozes update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/snoozes/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
