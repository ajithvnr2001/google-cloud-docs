---
url: https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete/
title: gcloud certificate-manager dns-authorizations delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:56:06.789408+00:00
---

# gcloud certificate-manager dns-authorizations delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud certificate-manager dns-authorizations delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud certificate-manager dns-authorizations delete - delete a DNS Authorization 
SYNOPSIS
    

`gcloud certificate-manager dns-authorizations delete` (`DNS_AUTHORIZATION` : `--location`=`LOCATION`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a DNS Authorization. 
EXAMPLES
     To delete a DNS Authorization called `my-authorization`, run: 
    
    
    gcloud certificate-manager dns-authorizations delete my-authorization

POSITIONAL ARGUMENTS
    

DnsAuthorization resource - The name of the DNS Authorization to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dns_authorization` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DNS_AUTHORIZATION`
     ID of the dnsAuthorization or fully qualified identifier for the dnsAuthorization. 

To set the `dns_authorization` attribute: 

  * provide the argument `dns_authorization` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Certificate Manager location. 

To set the `location` attribute: 

  * provide the argument `dns_authorization` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * default value of location is [global]. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `certificatemanager/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/certificate-manager/docs/overview>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha certificate-manager dns-authorizations delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/dns-authorizations/delete)
    
    
    [gcloud beta certificate-manager dns-authorizations delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/dns-authorizations/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
