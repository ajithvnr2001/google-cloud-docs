---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/macos/
title: gcloud alpha auth enterprise-certificate-config create macos \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:35.325665+00:00
---

# gcloud alpha auth enterprise-certificate-config create macos  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/macos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha auth enterprise-certificate-config create macos Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha auth enterprise-certificate-config create macos - create an enterprise-certificate configuration file for MacOS 
SYNOPSIS
    

`gcloud alpha auth enterprise-certificate-config create macos` `--issuer`=`ISSUER` [`--ecp`=`ECP`] [`--ecp-client`=`ECP_CLIENT`] [`--ecp-http-proxy`=`ECP_HTTP_PROXY`] [`--keychain-type`=`KEYCHAIN_TYPE`; default="all"] [`--output-file`=`OUTPUT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command creates a configuration file used by gcloud to use the enterprise-certificate-proxy component for mTLS. 
EXAMPLES
     To create a credential configuration run: 
    
    
    gcloud alpha auth enterprise-certificate-config create macos --issuer=$CERT_ISSUER

REQUIRED FLAGS
    

`--issuer`=`ISSUER`
     The certificate issuer. 
OPTIONAL FLAGS
    

`--ecp`=`ECP`
     Provide a custom path to the enterprise-certificate-proxy binary. This flag must be the full path to the binary. 
`--ecp-client`=`ECP_CLIENT`
     Provide a custom path to the enterprise-certificate-proxy shared client library. This flag must be the full path to the shared library. 
`--ecp-http-proxy`=`ECP_HTTP_PROXY`
     Provide a custom path to the ECP HTTP proxy binary. This flag must be the full path to the binary. 
`--keychain-type`=`KEYCHAIN_TYPE`; default="all"
     Specify the target keychain(s) for certificate lookup.Accepted values are "login", "system", or "all". If omitted,defaults to "all". Use "all" to include custom keychains. 
`--output-file`=`OUTPUT_FILE`
     Override the file path that the enterprise-certificate-proxy configuration is written to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud auth enterprise-certificate-config create macos](https://docs.cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config/create/macos)
    
    
    [gcloud beta auth enterprise-certificate-config create macos](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/enterprise-certificate-config/create/macos)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
