---
url: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create/
title: gcloud monitoring snoozes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:33:11.441565+00:00
---

# gcloud monitoring snoozes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud monitoring snoozes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud monitoring snoozes create - create a new snooze 
SYNOPSIS
    

`gcloud monitoring snoozes create` [`--snooze-from-file`=`PATH_TO_FILE`] [`--criteria-filter`=`CRITERIA_FILTER` `--criteria-policies`=`CRITERIA_POLICIES`,[…] `--display-name`=`DISPLAY_NAME` `--end-time`=`END_TIME` `--start-time`=`START_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new snooze. A snooze can be specified as a JSON/YAML value passed in as a file through the `--snooze-from-file` flag. A snooze can also be specified through command line flags. If a snooze is specified through `--snooze-from-file`, and additional flags are supplied, the flags will override the snooze's settings. 

For information about the JSON/YAML format of a snooze: <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes>

EXAMPLES
     To create a snooze with command-line options, run: 
    
    
    gcloud monitoring snoozes create --criteria-policies=LIST_OF_POLICIES --criteria-filter=FILTER --display-name=DISPLAY_NAME --start-time=START_TIME --end-time=END_TIME

To create a snooze with a file, run: 
    
    
    gcloud monitoring snoozes create --snooze-from-file=MY-FILE

Sample contents of MY-FILE: 
    
    
    criteria:
      policies:
      - projects/MY-PROJECT/alertPolicies/MY-POLICY
      filter: 'resource.labels.zone="us-central1-a" AND resource.labels.instance_id="1234567890"'
    interval:
      startTime: '2024-03-01T08:00:00Z'
      endTime: '2024-03-08T04:59:59.500Z'
    displayName: New Snooze

FLAGS
    

`--snooze-from-file`=`PATH_TO_FILE`
     The path to a JSON or YAML file containing the snooze. Use a full or relative path to a local file containing the value of snooze. 
Snooze Settings. If any of these are specified, they will overwrite fields in the `--snooze-from-file` flags if specified. 
`--criteria-filter`=`CRITERIA_FILTER`
     Optional. When you define a Snooze, you can also define a filter for that snooze. The filter is a string containing one or more key-value pairs. The string uses the standard <https://google.aip.dev/160> filter syntax. If you define a filter for a snooze, then the snooze can only apply to one alert policy. When the snooze is active, incidents won't be created when the incident would have key-value pairs (labels) that match those specified by the filter in the snooze. Snooze filters support resource, metric, and metadata labels. If multiple labels are used, then they must be connected with an AND operator. For example: resource.labels.instance_id="1234567890" AND resource.labels.zone="us-central1-a" AND metric.labels.instance_name="test_group" AND metadata.user_labels.foo="bar" AND metadata.system_labels.region="us-central1" 
`--criteria-policies`=`CRITERIA_POLICIES`,[…]
     The policies that the Snooze applies to. Exactly 1 alert policy is required if `criteria-filter` is specified at the same time. 
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
    
    
    [gcloud alpha monitoring snoozes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/snoozes/create)
    
    
    [gcloud beta monitoring snoozes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/snoozes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
