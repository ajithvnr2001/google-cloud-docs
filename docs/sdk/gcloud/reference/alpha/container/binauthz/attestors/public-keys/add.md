---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestors/public-keys/add/
title: gcloud alpha container binauthz attestors public-keys add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:42.617663+00:00
---

# gcloud alpha container binauthz attestors public-keys add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestors/public-keys/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container binauthz attestors public-keys add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container binauthz attestors public-keys add - add a public key to an Attestor 
SYNOPSIS
    

`gcloud alpha container binauthz attestors public-keys add` `--attestor`=`ATTESTOR` (`--pgp-public-key-file`=`PATH_TO_FILE` | (`--keyversion`=`KEYVERSION` : `--keyversion-key`=`KEYVERSION_KEY` `--keyversion-keyring`=`KEYVERSION_KEYRING` `--keyversion-location`=`KEYVERSION_LOCATION` `--keyversion-project`=`KEYVERSION_PROJECT`) | `--pkix-public-key-algorithm`=`PKIX_PUBLIC_KEY_ALGORITHM` `--pkix-public-key-file`=`PATH_TO_FILE`) [`--comment`=`COMMENT`] [`--public-key-id-override`=`PUBLIC_KEY_ID_OVERRIDE`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To add a new KMS public key to an existing Attestor `my_attestor`: 
    
    
    gcloud alpha container binauthz attestors public-keys add --attestor=my_attestor --keyversion-project=foo --keyversion-location=us-west1 --keyversion-keyring=aring --keyversion-key=akey --keyversion=1

To add a new PGP public key to an existing Attestor `my_attestor`: 
    
    
    gcloud alpha container binauthz attestors public-keys add --attestor=my_attestor --pgp-public-key-file=my_key.pub

REQUIRED FLAGS
    

Attestor resource - The attestor to which the public key should be added. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--attestor` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--attestor`=`ATTESTOR`
     ID of the attestor or fully qualified identifier for the attestor. 

To set the `name` attribute: 

  * provide the argument `--attestor` on the command line. 


Exactly one of these must be specified: 

PGP key definition 
`--pgp-public-key-file`=`PATH_TO_FILE`
     The path to the file containing the ASCII-armored PGP public key to add. Use a full or relative path to a local file containing the value of pgp_public_key_file. 
Cloud KMS key definition 
CryptoKeyVersion resource - The Cloud KMS (Key Management Service) CryptoKeyVersion whose public key will be added to the attestor. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--keyversion`=`KEYVERSION`
     ID of the CryptoKeyVersion or fully qualified identifier for the CryptoKeyVersion. 

To set the `version` attribute: 

  * provide the argument `--keyversion` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--keyversion-key`=`KEYVERSION_KEY`
     The key of the CryptoKeyVersion. 

To set the `key` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-key` on the command line. 


`--keyversion-keyring`=`KEYVERSION_KEYRING`
     The keyring of the CryptoKeyVersion. 

To set the `keyring` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-keyring` on the command line. 


`--keyversion-location`=`KEYVERSION_LOCATION`
     The location of the CryptoKeyVersion. 

To set the `location` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-location` on the command line. 


`--keyversion-project`=`KEYVERSION_PROJECT`
     Project ID of the Google Cloud project for the CryptoKeyVersion. 

To set the `project` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


PKIX key definition 
`--pkix-public-key-algorithm`=`PKIX_PUBLIC_KEY_ALGORITHM`
     The signing algorithm of the associated key. This will be used to verify the signatures associated with this key. `PKIX_PUBLIC_KEY_ALGORITHM` must be one of: `ec-sign-p256-sha256`, `ec-sign-p384-sha384`, `ec-sign-p521-sha512`, `ecdsa-p256-sha256`, `ecdsa-p384-sha384`, `ecdsa-p521-sha512`, `ml-dsa-65`, `rsa-pss-2048-sha256`, `rsa-pss-3072-sha256`, `rsa-pss-4096-sha256`, `rsa-pss-4096-sha512`, `rsa-sign-pkcs1-2048-sha256`, `rsa-sign-pkcs1-3072-sha256`, `rsa-sign-pkcs1-4096-sha256`, `rsa-sign-pkcs1-4096-sha512`, `rsa-sign-pss-2048-sha256`, `rsa-sign-pss-3072-sha256`, `rsa-sign-pss-4096-sha256`, `rsa-sign-pss-4096-sha512`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--pkix-public-key-file`=`PATH_TO_FILE`
     The path to the file containing the PKIX public key to add. Use a full or relative path to a local file containing the value of pkix_public_key_file. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--comment`=`COMMENT`
     The comment describing the public key. 
`--public-key-id-override`=`PUBLIC_KEY_ID_OVERRIDE`
     If provided, the ID to replace the default API-generated one. All IDs must be valid URIs as defined by RFC 3986 (https://tools.ietf.org/html/rfc3986). 

When creating Attestations to be verified by this key, one must always provide this custom ID as the public key ID. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container binauthz attestors public-keys add](https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/public-keys/add)
    
    
    [gcloud beta container binauthz attestors public-keys add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/attestors/public-keys/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
