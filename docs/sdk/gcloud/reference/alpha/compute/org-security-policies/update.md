---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/update/
title: gcloud alpha compute org-security-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:19.868751+00:00
---

# gcloud alpha compute org-security-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute org-security-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute org-security-policies update - update a Compute Engine organization security policy 
SYNOPSIS
    

`gcloud alpha compute org-security-policies update` `SECURITY_POLICY` [`--description`=`DESCRIPTION`] [`--json-custom-content-types`=[`CONTENT_TYPE`,…]] [`--json-parsing`=`JSON_PARSING`] [`--log-level`=`LOG_LEVEL`] [`--organization`=`ORGANIZATION`] [`--user-ip-request-headers`=[`USER_IP_REQUEST_HEADER`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute org-security-policies update` is used to update organization security policies. An organization security policy is a set of rules that controls access to various resources. 
EXAMPLES
     To update an organization security policy with ID ``123456789`` to change the description to ``New description``, run: 
    
    
    gcloud alpha compute org-security-policies update 123456789 --description='New description'

POSITIONAL ARGUMENTS
    

`SECURITY_POLICY`
     Short name or ID of the security policy to update. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the organization security policy. 
`--json-custom-content-types`=[`CONTENT_TYPE`,…]
     A comma-separated list of custom Content-Type header values to apply JSON parsing for preconfigured WAF rules. Only applicable when JSON parsing is enabled, like ``\--json-parsing=STANDARD``. When configuring a Content-Type header value, only the type/subtype needs to be specified, and the parameters should be excluded. 
`--json-parsing`=`JSON_PARSING`
     The JSON parsing behavior for this rule. Must be one of the following values: [DISABLED, STANDARD, STANDARD_WITH_GRAPHQL]. `JSON_PARSING` must be one of: `DISABLED`, `STANDARD`, `STANDARD_WITH_GRAPHQL`. 
`--log-level`=`LOG_LEVEL`
     The level of detail to display for WAF logging. `LOG_LEVEL` must be one of: `NORMAL`, `VERBOSE`. 
`--organization`=`ORGANIZATION`
     Organization in which the organization security policy is to be updated. Must be set if SECURITY_POLICY is the short name. 
`--user-ip-request-headers`=[`USER_IP_REQUEST_HEADER`,…]
     A comma-separated list of request header names to use for resolving the caller's user IP address. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute org-security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/update)
    
    
    [gcloud beta compute org-security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/update)
    
    
    [gcloud preview compute org-security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
