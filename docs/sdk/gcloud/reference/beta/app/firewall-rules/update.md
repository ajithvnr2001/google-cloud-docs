---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/firewall-rules/update/
title: gcloud beta app firewall-rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:57.434611+00:00
---

# gcloud beta app firewall-rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/firewall-rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app firewall-rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app firewall-rules update - updates a firewall rule 
SYNOPSIS
    

`gcloud beta app firewall-rules update` `PRIORITY` [`--action`=`ACTION`] [`--description`=`DESCRIPTION`] [`--source-range`=`SOURCE_RANGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates a firewall rule. 
EXAMPLES
     To update an App Engine firewall rule, run: 
    
    
    gcloud beta app firewall-rules update 1234 --source-range='2001:db8::/32' --action=allow --description='This is an example rule.'

POSITIONAL ARGUMENTS
    

`PRIORITY`
     An integer between 1 and 2^32-1 which indicates the evaluation order of rules. Lowest priority rules are evaluated first. The handle `default` may also be used to refer to the final rule at priority 2^32-1 which is always present in a set of rules. 
FLAGS
    

`--action`=`ACTION`
     Allow or deny matched traffic. `ACTION` must be one of: `ALLOW`, `DENY`. 
`--description`=`DESCRIPTION`
     A text description of the rule. 
`--source-range`=`SOURCE_RANGE`
     An IP address or range in CIDR notation or the `*` wildcard to match all traffic. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud app firewall-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/app/firewall-rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
