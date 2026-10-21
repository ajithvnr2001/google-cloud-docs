---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-certificates/create/
title: gcloud preview compute ssl-certificates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:43:02.327377+00:00
---

# gcloud preview compute ssl-certificates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-certificates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute ssl-certificates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute ssl-certificates create - create a Compute Engine SSL certificate 
SYNOPSIS
    

`gcloud preview compute ssl-certificates create` `NAME` (`--domains`=`DOMAIN`,[`DOMAIN`,…] | `--certificate`=`LOCAL_FILE_PATH` `--private-key`=`LOCAL_FILE_PATH`) [`--description`=`DESCRIPTION`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute ssl-certificates create` creates SSL certificate resources, which you can use in a target HTTPS or target SSL proxy. An SSL certificate resource consists of a certificate and private key. The private key is encrypted before it is stored. 

You can create either a managed or a self-managed SslCertificate resource. A managed SslCertificate is provisioned and renewed for you. A self-managed certificate is created by passing the certificate obtained from Certificate Authority through `--certificate` and `--private-key` flags. 

EXAMPLES
     To create a self-managed certificate resource 'my-cert' from a certificate placed under path 'foo/cert' and a private key placed under path 'foo/pk', run: 
    
    
    gcloud preview compute ssl-certificates create my-cert --certificate=foo/cert --private-key=foo/pk

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the SSL certificate to create. 
REQUIRED FLAGS
    

Flags for managed or self-managed certificate. 

Exactly one of these must be specified: 

`--domains`=`DOMAIN`,[`DOMAIN`,…]
     List of domains to create a managed certificate for. 
Or at least one of these can be specified: 

Flags for self-managed certificate 
`--certificate`=`LOCAL_FILE_PATH`
     Path to a local certificate file to create a self-managed certificate. The certificate must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-key`=`LOCAL_FILE_PATH`
     Path to a local private key file. The private key must be in PEM format and must use RSA or ECDSA encryption. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the SSL certificate. 
At most one of these can be specified: 

`--global`
     If set, the SSL certificate is global. 
`--region`=`REGION`
     Region of the SSL certificate to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute ssl-certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create)
    
    
    [gcloud alpha compute ssl-certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-certificates/create)
    
    
    [gcloud beta compute ssl-certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssl-certificates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
