---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create/
title: gcloud compute ssl-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:49:46.115706+00:00
---

# gcloud compute ssl-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute ssl-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute ssl-policies create - create a new Compute Engine SSL policy 
SYNOPSIS
    

`gcloud compute ssl-policies create` `SSL_POLICY` [`--custom-features`=[`CUSTOM_FEATURES`,…]] [`--description`=`DESCRIPTION`] [`--min-tls-version`=`MIN_TLS_VERSION`; default="1.0"] [`--post-quantum-key-exchange`=`POST_QUANTUM_KEY_EXCHANGE`] [`--profile`=`PROFILE`; default="COMPATIBLE"] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute ssl-policies create` creates a new SSL policy. 

An SSL policy specifies the server-side support for SSL features. An SSL policy can be attached to a TargetHttpsProxy or a TargetSslProxy. This affects connections between clients and the load balancer. SSL policies do not affect the connection between the load balancers and the backends. SSL policies are used by Application Load Balancers and proxy Network Load Balancers. 

POSITIONAL ARGUMENTS
    

`SSL_POLICY`
     Name of the SSL policy to create. 
FLAGS
    

`--custom-features`=[`CUSTOM_FEATURES`,…]
     A comma-separated list of custom features, required when the profile being used is CUSTOM. 

Using CUSTOM profile allows customization of the features that are part of the SSL policy. This flag allows specifying those custom features. 

The list of all supported custom features can be obtained using: 
    
    
    gcloud compute ssl-policies list-available-features

`--description`=`DESCRIPTION`
     An optional, textual description for the SSL policy. 
`--min-tls-version`=`MIN_TLS_VERSION`; default="1.0"
     Minimum TLS version. `MIN_TLS_VERSION` must be one of: 

`1.0`
     TLS 1.0. 
`1.1`
     TLS 1.1. 
`1.2`
     TLS 1.2. 
`1.3`
     TLS 1.3. 
`--post-quantum-key-exchange`=`POST_QUANTUM_KEY_EXCHANGE`
     Whether to use post-quantum key exchange. `POST_QUANTUM_KEY_EXCHANGE` must be one of: 

`DEFAULT`
     Post-quantum key exchange is disabled until it becomes enabled by default on load balancers. 
`DEFERRED`
     Post-quantum key exchange with clients is temporarily disabled. 
`ENABLED`
     Post-quantum key exchange is enabled. 
`--profile`=`PROFILE`; default="COMPATIBLE"
     SSL policy profile. Changing profile from CUSTOM to COMPATIBLE|MODERN|RESTRICTED|FIPS_202205 will clear the custom-features field. `PROFILE` must be one of: 

`COMPATIBLE`
     Compatible profile. Allows the broadest set of clients, even those which support only out-of-date SSL features, to negotiate SSL with the load balancer. 
`CUSTOM`
     Custom profile. Allows customization by selecting only the features which are required. The list of all available features can be obtained using: 
    
    
    gcloud compute ssl-policies list-available-features

`FIPS_202205`
     FIPS_202205 profile. Supports a reduced set of SSL features, intended to meet stricter compliance requirements. 
`MODERN`
     Modern profile. Supports a wide set of SSL features, allowing modern clients to negotiate SSL. 
`RESTRICTED`
     Restricted profile. Supports a reduced set of SSL features, intended to meet stricter compliance requirements. 
At most one of these can be specified: 

`--global`
     If set, the SSL policy is global. 
`--region`=`REGION`
     Region of the SSL policy to create. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute ssl-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-policies/create)
    
    
    [gcloud beta compute ssl-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssl-policies/create)
    
    
    [gcloud preview compute ssl-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
