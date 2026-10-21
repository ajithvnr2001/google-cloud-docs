---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe/
title: gcloud privateca certificates describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:14.242255+00:00
---

# gcloud privateca certificates describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca certificates describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca certificates describe - get metadata for a certificate 
SYNOPSIS
    

`gcloud privateca certificates describe` (`CERTIFICATE` : `--issuer-location`=`ISSUER_LOCATION` `--issuer-pool`=`ISSUER_POOL`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Returns metadata for the given certificate. 
EXAMPLES
     To get metadata for the 'frontend-server-tls' certificate: 
    
    
    gcloud privateca certificates describe frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1

To download the PEM-encoded certificate for the 'frontend-server-tls' certificate to a file called 'frontend-server-tls.crt': 
    
    
    gcloud privateca certificates describe frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --format="value(pemCertificate)" > ./frontend-server-tls.crt

POSITIONAL ARGUMENTS
    

CERTIFICATE resource - The certificate for which to obtain metadata. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `certificate` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE`
     ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE. 

To set the `certificate` attribute: 

  * provide the argument `certificate` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--issuer-location`=`ISSUER_LOCATION`
     The location of the CERTIFICATE. 

To set the `issuer-location` attribute: 

  * provide the argument `certificate` on the command line with a fully specified name; 
  * provide the argument `--issuer-location` on the command line; 
  * set the property `privateca/location`. 


`--issuer-pool`=`ISSUER_POOL`
     The ID of the issuing CA Pool. 

To set the `issuer-pool` attribute: 

  * provide the argument `certificate` on the command line with a fully specified name; 
  * provide the argument `--issuer-pool` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `privateca/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
