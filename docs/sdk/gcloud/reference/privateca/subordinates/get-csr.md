---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/get-csr/
title: gcloud privateca subordinates get-csr \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:59.089336+00:00
---

# gcloud privateca subordinates get-csr  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/get-csr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca subordinates get-csr Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca subordinates get-csr - get the CSR for a subordinate certificate authority that has not yet been activated 
SYNOPSIS
    

`gcloud privateca subordinates get-csr` (`CERTIFICATE_AUTHORITY` : `--location`=`LOCATION` `--pool`=`POOL`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Gets the PEM-encoded CSR for a subordinate certificate authority that is awaiting user activation. The CSR should be signed by the issuing Certificate Authority and uploaded back using the `subordinates activate` command. 
EXAMPLES
     To download the CSR for the 'server-tls-1' CA into a file called 'server-tls-1.csr': 
    
    
    gcloud privateca subordinates get-csr server-tls-1 --location=us-west1 --pool=my-pool > server-tls-1.csr

POSITIONAL ARGUMENTS
    

CERTIFICATE AUTHORITY resource - The certificate authority for which to get the CSR. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_AUTHORITY`
     ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the CERTIFICATE_AUTHORITY. 

To set the `certificate_authority` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CERTIFICATE_AUTHORITY. 

To set the `location` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


`--pool`=`POOL`
     The parent CA Pool of the CERTIFICATE_AUTHORITY. 

To set the `pool` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--pool` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
