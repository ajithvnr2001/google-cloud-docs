---
url: https://docs.cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam/
title: gcloud policy-troubleshoot iam \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:01:47.788625+00:00
---

# gcloud policy-troubleshoot iam  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/policy-troubleshoot/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud policy-troubleshoot iam Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud policy-troubleshoot iam - troubleshoot the IAM Policy 
SYNOPSIS
    

`gcloud policy-troubleshoot iam` `RESOURCE` `--permission`=`PERMISSION` `--principal-email`=`PRINCIPAL_EMAIL` [`--destination-ip`=`DESTINATION_IP`] [`--destination-port`=`DESTINATION_PORT`] [`--request-time`=`REQUEST_TIME`] [`--resource-name`=`RESOURCE_NAME`] [`--resource-service`=`RESOURCE_SERVICE`] [`--resource-type`=`RESOURCE_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Performs a check on whether a principal is granted a permission on a resource and how that access is determined according to the resource's effective IAM policy interpretation. 
EXAMPLES
     To troubleshoot a permission of a principal on a resource, run: 
    
    
    gcloud policy-troubleshoot iam //cloudresourcemanager.googleapis.com/projects/project-id --principal-email=my-iam-account@somedomain.com --permission=resourcemanager.projects.get

See <https://cloud.google.com/iam/help/allow-policies/overview> for more information about IAM policies. 

POSITIONAL ARGUMENTS
    

`RESOURCE`
     Full resource name that access is checked against. See: <https://cloud.google.com/iam/docs/resource-names>. 
REQUIRED FLAGS
    

`--permission`=`PERMISSION`
     Cloud IAM permission to check, e.g. "resourcemanager.projects.get". 
`--principal-email`=`PRINCIPAL_EMAIL`
     Email address that identifies the principal to check. Only Google Accounts and service accounts are supported. 
OPTIONAL FLAGS
    

`--destination-ip`=`DESTINATION_IP`
     The request destination IP address to use when checking conditional bindings. For example, `198.1.1.1`. 
`--destination-port`=`DESTINATION_PORT`
     The request destination port to use when checking conditional bindings. For example, 8080. 
`--request-time`=`REQUEST_TIME`
     The request timestamp to use when checking conditional bindings. This string must adhere to UTC format (RFC 3339). For example,2021-01-01T00:00:00Z. See: <https://tools.ietf.org/html/rfc3339>
`--resource-name`=`RESOURCE_NAME`
     The resource name value to use when checking conditional bindings. See: <https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name>. 
`--resource-service`=`RESOURCE_SERVICE`
     The resource service value to use when checking conditional bindings. See: <https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-service>
`--resource-type`=`RESOURCE_TYPE`
     The resource type value to use when checking conditional bindings. See: <https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-type>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `policytroubleshooter/v2alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha policy-troubleshoot iam](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/policy-troubleshoot/iam)
    
    
    [gcloud beta policy-troubleshoot iam](https://docs.cloud.google.com/sdk/gcloud/reference/beta/policy-troubleshoot/iam)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
