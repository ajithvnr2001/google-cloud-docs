---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/export/
title: gcloud network-security gateway-security-policies export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:22.099503+00:00
---

# gcloud network-security gateway-security-policies export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security gateway-security-policies export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security gateway-security-policies export - export Gateway Security Policy 
SYNOPSIS
    

`gcloud network-security gateway-security-policies export` (`GATEWAY_SECURITY_POLICY` : `--location`=`LOCATION`) [`--destination`=`DESTINATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export a Gateway Security Policy. 
EXAMPLES
     To export a Gateway Security Policy, run: 
    
    
    gcloud network-security gateway-security-policies export my-gateway-security-policy --destination=my-gateway-security-policy-list.yaml --location=global

POSITIONAL ARGUMENTS
    

Gateway security policy resource - Name of the Gateway Security Policy to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `gateway_security_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GATEWAY_SECURITY_POLICY`
     ID of the gateway security policy or fully qualified identifier for the gateway security policy. 

To set the `gateway_security_policy` attribute: 

  * provide the argument `gateway_security_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `gateway_security_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--destination`=`DESTINATION`
     Path to a YAML file where the configuration will be exported. The exported data will not contain any output-only fields. Alternatively, you may omit this flag to write to standard output. For a schema describing the export/import format, see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/… 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security gateway-security-policies export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/gateway-security-policies/export)
    
    
    [gcloud beta network-security gateway-security-policies export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/gateway-security-policies/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
