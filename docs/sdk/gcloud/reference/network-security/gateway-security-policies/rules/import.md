---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/import/
title: gcloud network-security gateway-security-policies rules import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:22.461042+00:00
---

# gcloud network-security gateway-security-policies rules import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security gateway-security-policies rules import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security gateway-security-policies rules import - import Gateway Security Policy Rule 
SYNOPSIS
    

`gcloud network-security gateway-security-policies rules import` (`GATEWAY_SECURITY_POLICY_RULE` : `--gateway-security-policy`=`GATEWAY_SECURITY_POLICY` `--location`=`LOCATION`) [`--async`] [`--source`=`SOURCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Import a Gateway Security Policy Rule. 
EXAMPLES
     To import a Gateway Security Policy Rule from a YAML file, run: 
    
    
    gcloud network-security gateway-security-policies rules import my-rule --source=my-rule.yaml --location={region} --gateway-security-policy={policy-name}

POSITIONAL ARGUMENTS
    

Gateway security policy rule resource - Name of the Gateway Security Policy Rule to import. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `gateway_security_policy_rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GATEWAY_SECURITY_POLICY_RULE`
     ID of the gateway security policy rule or fully qualified identifier for the gateway security policy rule. 

To set the `gateway_security_policy_rule` attribute: 

  * provide the argument `gateway_security_policy_rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--gateway-security-policy`=`GATEWAY_SECURITY_POLICY`
     Id of the gateway security policy. 

To set the `gateway-security-policy` attribute: 

  * provide the argument `gateway_security_policy_rule` on the command line with a fully specified name; 
  * provide the argument `--gateway-security-policy` on the command line. 


`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `gateway_security_policy_rule` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--source`=`SOURCE`
     Path to a YAML file containing the configuration export data. The YAML file must not contain any output-only fields. Alternatively, you may omit this flag to read from standard input. For a schema describing the export/import format, see: $CLOUDSDKROOT/lib/googlecloudsdk/schemas/… 

$CLOUDSDKROOT is can be obtained with the following command: 
    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format='value(installation.sdk_root)'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security gateway-security-policies rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/gateway-security-policies/rules) import
    
    
    [gcloud beta network-security gateway-security-policies rules import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/gateway-security-policies/rules/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
