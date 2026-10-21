---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/rules/describe/
title: gcloud compute org-security-policies rules describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:25:12.820145+00:00
---

# gcloud compute org-security-policies rules describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/rules/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute org-security-policies rules describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute org-security-policies rules describe - describe a Compute Engine organization security policy rule 
SYNOPSIS
    

`gcloud compute org-security-policies rules describe` `PRIORITY` `--security-policy`=`SECURITY_POLICY` [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute org-security-policies rules describe` is used to describe organization security policy rule. 
EXAMPLES
     To describe a rule with priority ``10`` in an organization security policy with ID ``123456789``, run: 
    
    
    gcloud compute org-security-policies rules describe 10 --security-policy=123456789

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the security policy rule to describe. 
REQUIRED FLAGS
    

`--security-policy`=`SECURITY_POLICY`
     short name of the security policy into which the rule should be described. 
OPTIONAL FLAGS
    

`--organization`=`ORGANIZATION`
     Organization which the organization security policy belongs to. Must be set if SECURITY_POLICY is short name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute org-security-policies rules describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/rules/describe)
    
    
    [gcloud beta compute org-security-policies rules describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/rules/describe)
    
    
    [gcloud preview compute org-security-policies rules describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/rules/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
