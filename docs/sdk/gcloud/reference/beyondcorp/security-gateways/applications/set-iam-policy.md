---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/applications/set-iam-policy/
title: gcloud beyondcorp security-gateways applications set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:55:43.315257+00:00
---

# gcloud beyondcorp security-gateways applications set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/applications/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beyondcorp security-gateways applications set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beyondcorp security-gateways applications set-iam-policy - set the IAM policy for a security gateway application 
SYNOPSIS
    

`gcloud beyondcorp security-gateways applications set-iam-policy` (`APPLICATION` : `--location`=`LOCATION` `--security-gateway`=`SECURITY_GATEWAY`) `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Sets the IAM policy for the given security gateway application. 
EXAMPLES
     The following command will read an IAM policy defined in a JSON file 'policy.json' and set it for the security gateway application with ID ``my-security-gateway-application``: 
    
    
    gcloud beyondcorp security-gateways applications set-iam-policy my-security-gateway-application policy.json --location=global

POSITIONAL ARGUMENTS
    

Application resource - The security gateway application for which to set the IAM policy. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION`
     ID of the application or fully qualified identifier for the application. 

To set the `application` attribute: 

  * provide the argument `application` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the application resource. We support only global location. 

To set the `location` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--security-gateway`=`SECURITY_GATEWAY`
     The securityGateway id of the application resource. 

To set the `security-gateway` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--security-gateway` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `beyondcorp/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta beyondcorp security-gateways applications](https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/applications) set-iam-policy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
