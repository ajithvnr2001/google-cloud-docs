---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/firewall-policies/create/
title: gcloud alpha recaptcha firewall-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:43.160499+00:00
---

# gcloud alpha recaptcha firewall-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/firewall-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha recaptcha firewall-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha recaptcha firewall-policies create - create a Firewall Policy 
SYNOPSIS
    

`gcloud alpha recaptcha firewall-policies create` [`--actions`=`ACTIONS`] [`--condition`=`CONDITION`] [`--description`=`DESCRIPTION`] [`--path`=`PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a reCAPTCHA Firewall Policy. 
EXAMPLES
     To create a new reCAPTCHA firewall policy covering the path "/login/`" for all requests with a reCAPTCHA Lite score of >= 0.5 to allow the requests and set the header 'foo' to the value 'bar': 
    
    
    gcloud alpha recaptcha firewall-policies create --path='/login/*' --condition='recaptcha.assessment_type == AssessmentType.LITE
    && recaptcha.score >= 0.5' --actions=allow,set_header=foo=bar

`
FLAGS
    

`--actions`=`ACTIONS`
     The actions that the caller should take regarding the user. There should be at most 1 terminal action. A terminal action is any action that forces a response, such as Allow, Block or Substitute. If it makes sense for it to happen multple times, such as SetHeader, the action is non-terminal. 

Examples: 

  * Block and set the header with key foo to value bar 
    * \--actions=block,set_header=foo=bar 
  * Substitute with path google.com and set two headers, one with key key1 to value value1 and one with key key2 to value value2 
    * \--actions=substitute=google.com,set_header=key1=value1,set_header=key2=value2 


`--condition`=`CONDITION`
     A CEL (Common Expression Language) conditional expression that specifies if this policy applies to an incoming user request. If this condition evaluates to true and the requested path matched the path pattern, the associated actions should be executed by the caller. The condition string is checked for CEL syntax correctness on creation. For more information, see the CEL spec: <https://github.com/google/cel-spec> and its language definition: <https://github.com/google/cel-spec/blob/master/doc/langdef.md>
`--description`=`DESCRIPTION`
     A description of what this policy aims to achieve, for convenience purposes. The description can at most include 256 UTF-8 characters. 
`--path`=`PATH`
     The path for which this policy applies, specified as a glob pattern. For more information on glob, see the manual page: <https://man7.org/linux/man-pages/man7/glob.7.html>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `recaptchaenterprise/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/recaptcha-enterprise/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud recaptcha firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
