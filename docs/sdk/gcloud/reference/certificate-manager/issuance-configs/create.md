---
url: https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create/
title: gcloud certificate-manager issuance-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:56:07.697090+00:00
---

# gcloud certificate-manager issuance-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud certificate-manager issuance-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud certificate-manager issuance-configs create - create a Certificate Issuance Config 
SYNOPSIS
    

`gcloud certificate-manager issuance-configs create` (`CERTIFICATE_ISSUANCE_CONFIG` : `--location`=`LOCATION`) `--ca-pool`=`CA_POOL` [`--async`] [`--description`=`DESCRIPTION`] [`--key-algorithm`=`KEY_ALGORITHM`; default="rsa-2048"] [`--labels`=[`KEY`=`VALUE`,…]] [`--lifetime`=`LIFETIME`; default="P30D"] [`--rotation-window-percentage`=`ROTATION_WINDOW_PERCENTAGE`; default=66] [`--tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Certificate Issuance Config. 
EXAMPLES
     To create a Certificate Issuance Config called `my-cic`, run: 
    
    
    gcloud certificate-manager issuance-configs create my-cic --ca-pool=my-ca-pool

POSITIONAL ARGUMENTS
    

CertificateIssuanceConfig resource - Name of the Certificate Issuance Config to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `certificate_issuance_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_ISSUANCE_CONFIG`
     ID of the certificateIssuanceConfig or fully qualified identifier for the certificateIssuanceConfig. 

To set the `certificate_issuance_config` attribute: 

  * provide the argument `certificate_issuance_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Certificate Manager location. 

To set the `location` attribute: 

  * provide the argument `certificate_issuance_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * default value of location is [global]. 


REQUIRED FLAGS
    

`--ca-pool`=`CA_POOL`
     CA Pool used for issuing certificates. For example: 
    
    
    gcloud certificate-manager issuance-configs create --ca-pool=projects/test-project/locations/us-west1/caPools/my-ca-pool

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Human-readable description of the resource. 
`--key-algorithm`=`KEY_ALGORITHM`; default="rsa-2048"
     Key algorithm to use when generating the private key. Defaults to `rsa-2048`. `KEY_ALGORITHM` must be one of: `ecdsa-p256`, `rsa-2048`. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--lifetime`=`LIFETIME`; default="P30D"
     Lifetime of issued certificates in ISO 8601 format. Use `[gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for details. Defaults to `P30D`. 
`--rotation-window-percentage`=`ROTATION_WINDOW_PERCENTAGE`; default=66
     How long along the lifetime of the ceritificate to renew, expressed as a percentage. Defaults to `66`. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tags KEY=VALUE pairs to bind. Each item must be expressed as `<tag-key-namespaced-name>=<tag-value-short-name>`. 

Example: `123/environment=production,123/costCenter=marketing`

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `certificatemanager/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/certificate-manager/docs/overview>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha certificate-manager issuance-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/create)
    
    
    [gcloud beta certificate-manager issuance-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/issuance-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
