---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update/
title: gcloud privateca pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:16.842675+00:00
---

# gcloud privateca pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca pools update - update an existing CA Pool 
SYNOPSIS
    

`gcloud privateca pools update` (`CA_POOL` : `--location`=`LOCATION`) [`--encryption-key`=`ENCRYPTION_KEY`] [`--issuance-policy`=`ISSUANCE_POLICY`] [`--no-publish-ca-cert`] [`--no-publish-crl`] [`--publishing-encoding-format`=`PUBLISHING_ENCODING_FORMAT`; default="pem"] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To update labels on a CA pool: 
    
    
    gcloud privateca pools update my-pool --location=us-west1 --update-labels=foo=bar

To disable publishing CRLs on a CA pool: 
    
    
    gcloud privateca pools update my-pool --location=us-west1 --no-publish-crl

POSITIONAL ARGUMENTS
    

CA POOL resource - The ca pool to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
`--publish-ca-cert`
     If this is enabled, the following will happen: 1) The CA certificates will be written to a known location within the CA distribution point. 2) The AIA extension in all issued certificates will point to the CA cert URL in that distribution point. 

If this gets disabled, the AIA extension will not be written to any future certificates issued by this CA. However, an existing bucket will not be deleted, and the CA certificates will not be removed from that bucket. 

Note that the same bucket may be used for the CRLs if --publish-crl is set. 

Enabled by default, use `--no-publish-ca-cert` to disable. 

`--publish-crl`
     If this gets enabled, the following will happen: 1) CRLs will be written to a known location within the CA distribution point. 2) The CDP extension in all future issued certificates will point to the CRL URL in that distribution point. 

If this gets disabled, the CDP extension will not be written to any future certificates issued by CAs in this pool, and new CRLs will not be published to that bucket (which affects existing certs). However, an existing bucket will not be deleted, and any existing CRLs will not be removed from that bucket. 

Note that the same bucket may be used for the CA cert if --publish-ca-cert is set. 

CRL publication is not supported for CAs in the DevOps tier. 

Enabled by default, use `--no-publish-crl` to disable. 

`--publishing-encoding-format`=`PUBLISHING_ENCODING_FORMAT`; default="pem"
     The encoding format of the content published to storage buckets. `PUBLISHING_ENCODING_FORMAT` must be one of: `der`, `pem`. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud privateca pools update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud privateca pools update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
