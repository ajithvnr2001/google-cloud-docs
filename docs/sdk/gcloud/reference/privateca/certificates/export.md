---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/export/
title: gcloud privateca certificates export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:13.956998+00:00
---

# gcloud privateca certificates export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca certificates export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca certificates export - export a pem-encoded certificate to a file 
SYNOPSIS
    

`gcloud privateca certificates export` (`CERTIFICATE` : `--issuer-location`=`ISSUER_LOCATION` `--issuer-pool`=`ISSUER_POOL`) `--output-file`=`OUTPUT_FILE` [`--include-chain`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To export a single pem-encoded certificate to a file, run the following: 
    
    
    gcloud privateca certificates export my-cert --issuer-pool=my-pool --issuer-location=us-west1 --output-file=cert.pem

To export a pem-encoded certificate along with its issuing chain in the same file, run the following: 
    
    
    gcloud privateca certificates export my-cert --issuer-pool=my-pool --issuer-location=us-west1 --include-chain --output-file=chain.pem

You can omit the --issuer-location flag in both of the above examples if you've already set the privateca/location property. For example: 

$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) privateca/location us-west1 

The following is equivalent to the first example above.
    
    
    
    gcloud privateca certificates export my-cert --issuer-pool=my-pool --output-file=cert.pem

The following is equivalent to the second example above.
    
    
    
    gcloud privateca certificates export my-cert --issuer-pool=my-pool --include-chain --output-file=chain.pem

POSITIONAL ARGUMENTS
    

CERTIFICATE resource - The certificate to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE`
     ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE. 

To set the `certificate` attribute: 

  * provide the argument `CERTIFICATE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--issuer-location`=`ISSUER_LOCATION`
     The location of the CERTIFICATE. 

To set the `issuer-location` attribute: 

  * provide the argument `CERTIFICATE` on the command line with a fully specified name; 
  * provide the argument `--issuer-location` on the command line; 
  * set the property `privateca/location`. 


`--issuer-pool`=`ISSUER_POOL`
     The parent CA Pool of the CERTIFICATE. 

To set the `issuer-pool` attribute: 

  * provide the argument `CERTIFICATE` on the command line with a fully specified name; 
  * provide the argument `--issuer-pool` on the command line. 


REQUIRED FLAGS
    

`--output-file`=`OUTPUT_FILE`
     The path where the resulting PEM-encoded certificate will be written. 
OPTIONAL FLAGS
    

`--include-chain`
     Whether to include the certificate's issuer chain in the exported file. If this is set, the resulting file will contain the pem-encoded certificate and its issuing chain, ordered from leaf to root. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
