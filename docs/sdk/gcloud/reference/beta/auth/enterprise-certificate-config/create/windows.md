---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/enterprise-certificate-config/create/windows/
title: gcloud beta auth enterprise-certificate-config create windows \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:13.808439+00:00
---

# gcloud beta auth enterprise-certificate-config create windows  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/enterprise-certificate-config/create/windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta auth enterprise-certificate-config create windows Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta auth enterprise-certificate-config create windows - create an enterprise-certificate configuration file for Windows 
SYNOPSIS
    

`gcloud beta auth enterprise-certificate-config create windows` `--issuer`=`ISSUER` `--provider`=`PROVIDER` `--store`=`STORE` [`--ecp`=`ECP`] [`--ecp-client`=`ECP_CLIENT`] [`--ecp-http-proxy`=`ECP_HTTP_PROXY`] [`--output-file`=`OUTPUT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a configuration file used by gcloud to use the enterprise-certificate-proxy component for mTLS. 
EXAMPLES
     To create a credential configuration run: 
    
    
    gcloud beta auth enterprise-certificate-config create windows --issuer=$CERT_ISSUER --store=$STORE --provider=$PROVIDER

REQUIRED FLAGS
    

`--issuer`=`ISSUER`
     The certificate issuer. 
`--provider`=`PROVIDER`
     The Windows secure store provider. 
`--store`=`STORE`
     The Windows secure store. 
OPTIONAL FLAGS
    

`--ecp`=`ECP`
     Provide a custom path to the enterprise-certificate-proxy binary. This flag must be the full path to the binary. 
`--ecp-client`=`ECP_CLIENT`
     Provide a custom path to the enterprise-certificate-proxy shared client library. This flag must be the full path to the shared library. 
`--ecp-http-proxy`=`ECP_HTTP_PROXY`
     Provide a custom path to the ECP HTTP proxy binary. This flag must be the full path to the binary. 
`--output-file`=`OUTPUT_FILE`
     Override the file path that the enterprise-certificate-proxy configuration is written to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud auth enterprise-certificate-config create windows](https://docs.cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/windows)
    
    
    [gcloud alpha auth enterprise-certificate-config create windows](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/windows)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
