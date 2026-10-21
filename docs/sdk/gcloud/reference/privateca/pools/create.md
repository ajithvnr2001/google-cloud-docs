---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create/
title: gcloud privateca pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:15.713386+00:00
---

# gcloud privateca pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca pools create - create a new CA Pool 
SYNOPSIS
    

`gcloud privateca pools create` (`CA_POOL` : `--location`=`LOCATION`) [`--encryption-key`=`ENCRYPTION_KEY`] [`--issuance-policy`=`ISSUANCE_POLICY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--no-publish-ca-cert`] [`--no-publish-crl`] [`--publishing-encoding-format`=`PUBLISHING_ENCODING_FORMAT`; default="pem"] [`--tier`=`TIER`; default="enterprise"] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a CA pool in the dev ops tier: 
    
    
    gcloud privateca pools create my-pool --location=us-west1 --tier=devops

To create a CA pool and restrict what it can issue: 
    
    
    gcloud privateca pools create my-pool --location=us-west1 --issuance-policy=policy.yaml

To create a CA pool that doesn't publicly publish CA certificates and CRLs: 
    
    
    gcloud privateca pools create my-pool --location=us-west1 --issuance-policy=policy.yaml --no-publish-ca-cert --no-publish-crl

POSITIONAL ARGUMENTS
    

CA POOL resource - The ca pool to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CA_POOL` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CA_POOL`
     ID of the CA_POOL or fully qualified identifier for the CA_POOL. 

To set the `pool` attribute: 

  * provide the argument `CA_POOL` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CA_POOL. 

To set the `location` attribute: 

  * provide the argument `CA_POOL` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


FLAGS
    

`--encryption-key`=`ENCRYPTION_KEY`
     The full resource name of the Cloud KMS key to use for encrypting certificate data at rest. The key must be in the same region as the CA pool. 
`--issuance-policy`=`ISSUANCE_POLICY`
     A YAML file describing this CA Pool's issuance policy. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--publish-ca-cert`
     If this is enabled, the following will happen: 1) The CA certificates will be written to a known location within the CA distribution point. 2) The AIA extension in all issued certificates will point to the CA cert URL in that distribition point. 

Note that the same bucket may be used for the CRLs if --publish-crl is set. 

Enabled by default, use `--no-publish-ca-cert` to disable. 

`--publish-crl`
     If this gets enabled, the following will happen: 1) CRLs will be written to a known location within the CA distribution point. 2) The CDP extension in all future issued certificates will point to the CRL URL in that distribution point. 

Note that the same bucket may be used for the CA cert if --publish-ca-cert is set. 

CRL publication is not supported for CAs in the DevOps tier. 

Enabled by default, use `--no-publish-crl` to disable. 

`--publishing-encoding-format`=`PUBLISHING_ENCODING_FORMAT`; default="pem"
     The encoding format of the content published to storage buckets. `PUBLISHING_ENCODING_FORMAT` must be one of: `der`, `pem`. 
`--tier`=`TIER`; default="enterprise"
     The tier for the Certificate Authority. `TIER` must be one of: `devops`, `enterprise`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
