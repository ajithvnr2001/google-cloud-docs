---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/import-rules/
title: gcloud beta compute firewall-policies import-rules \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:54.486726+00:00
---

# gcloud beta compute firewall-policies import-rules  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/import-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute firewall-policies import-rules Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute firewall-policies import-rules - import Compute Engine organization firewall policy rules 
SYNOPSIS
    

`gcloud beta compute firewall-policies import-rules` `FIREWALL_POLICY` [`--organization`=`ORGANIZATION`] [`--source`=`SOURCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Imports Firewall Policy rules configuration from a file. 
EXAMPLES
     Firewall Policy rules can be imported by running: 
    
    
    gcloud beta compute firewall-policies import-rules FIREWALL_POLICY --source=<path-to-file> --organization=<organization>

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     Short name or ID of the firewall policy to imports rules to. 
FLAGS
    

`--organization`=`ORGANIZATION`
     Organization in which the organization firewall policy rules import to. Must be set if FIREWALL_POLICY is short name. 
`--source`=`SOURCE`
     Path to a YAML file containing configuration export data. Alternatively, you may omit this flag to read from standard input. For a schema describing the export/import format, see: $CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/beta/FirewallPolicy.yaml. 
    
    
    Note: $CLOUDSDKROOT represents the Google Cloud CLI's installation directory.

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute firewall-policies import-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/import-rules)
    
    
    [gcloud alpha compute firewall-policies import-rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules)
    
    
    [gcloud preview compute firewall-policies import-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/import-rules)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
