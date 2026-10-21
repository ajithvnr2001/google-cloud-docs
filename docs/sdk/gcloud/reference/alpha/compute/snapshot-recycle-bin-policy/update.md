---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-recycle-bin-policy/update/
title: gcloud alpha compute snapshot-recycle-bin-policy update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:10:39.571263+00:00
---

# gcloud alpha compute snapshot-recycle-bin-policy update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-recycle-bin-policy/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute snapshot-recycle-bin-policy update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute snapshot-recycle-bin-policy update - update the project's or organization's snapshot recycle bin policy 
SYNOPSIS
    

`gcloud alpha compute snapshot-recycle-bin-policy update` (`--remove-rule`=`RULE_KEY` | [`--standard-snapshots-retention-duration-days`=`STANDARD_SNAPSHOTS_RETENTION_DURATION_DAYS` : `--set-rule`=`RULE_KEY`]) [`--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the project's or organization's snapshot recycle bin policy. 
EXAMPLES
     To set retention days for the default rule to 10 days for a project: 
    
    
    gcloud alpha compute snapshot-recycle-bin-policy update --set-rule=default --standard-snapshots-retention-duration-days=10

To set retention days for the default rule to 6 days for organization 123456789: 
    
    
    gcloud alpha compute snapshot-recycle-bin-policy update --organization=123456789 --set-rule=default --standard-snapshots-retention-duration-days=6

To set retention days for a tag-based rule '12345/env/prod' to 5 days for a project: 
    
    
    gcloud alpha compute snapshot-recycle-bin-policy update --set-rule='12345/env/prod' --standard-snapshots-retention-duration-days=5

To remove rule '12345/env/prod' for a project: 
    
    
    gcloud alpha compute snapshot-recycle-bin-policy update --remove-rule='12345/env/prod'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--remove-rule`=`RULE_KEY`
     Key of the rule to remove. Rule keys are 'default' or tag-based keys like '12345/env/prod'. 
Or at least one of these can be specified: 

`--standard-snapshots-retention-duration-days`=`STANDARD_SNAPSHOTS_RETENTION_DURATION_DAYS`
     Retention duration in days for standard snapshots. Must be provided with \--set-rule. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--set-rule`=`RULE_KEY`
     Key of the rule to set. Rule keys are 'default' or tag-based keys like '12345/env/prod'. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--organization`=`ORGANIZATION`
     Organization ID to apply this policy to. 
`--project`=`PROJECT`
     Project ID to apply this policy to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute snapshot-recycle-bin-policy update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshot-recycle-bin-policy/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
