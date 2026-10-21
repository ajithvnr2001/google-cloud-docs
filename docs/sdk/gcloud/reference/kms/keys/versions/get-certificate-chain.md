---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain/
title: gcloud kms keys versions get-certificate-chain \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:49.248954+00:00
---

# gcloud kms keys versions get-certificate-chain  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms keys versions get-certificate-chain Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms keys versions get-certificate-chain - get a certificate chain for a given version 
SYNOPSIS
    

`gcloud kms keys versions get-certificate-chain` `VERSION` [`--certificate-chain-type`=`CERTIFICATE_CHAIN_TYPE`; default="all"] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--output-file`=`OUTPUT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Returns the PEM-format certificate chain for the specified key version. The optional flag `output-file` indicates the path to store the PEM. If not specified, the PEM will be printed to stdout. 
EXAMPLES
     The following command saves the Cavium certificate chain for CryptoKey ``frodo`` Version 2 to ``/tmp/my/cavium.pem``: 
    
    
    gcloud kms keys versions get-certificate-chain 2 --key=frodo --keyring=fellowship --location=us-east1 --certificate-chain-type=cavium --output-file=/tmp/my/cavium.pem

POSITIONAL ARGUMENTS
    

`VERSION`
     Name of the version from which to get the certificate chain. 
FLAGS
    

`--certificate-chain-type`=`CERTIFICATE_CHAIN_TYPE`; default="all"
     Certificate chain to retrieve. `CERTIFICATE_CHAIN_TYPE` must be one of: `all`, `cavium`, `google-card`, `google-partition`. 
`--key`=`KEY`
     The containing key. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--output-file`=`OUTPUT_FILE`
     Path to the output file to store PEM. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms keys versions get-certificate-chain](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/get-certificate-chain)
    
    
    [gcloud beta kms keys versions get-certificate-chain](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/get-certificate-chain)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
