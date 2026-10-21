---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/identity-providers/create/
title: gcloud alpha edge-cloud identity-providers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:30:56.702089+00:00
---

# gcloud alpha edge-cloud identity-providers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/identity-providers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud identity-providers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud identity-providers create - creates an identity provider for a Google Destributed Cloud zone 
SYNOPSIS
    

`gcloud alpha edge-cloud identity-providers create` (`IDENTITY_PROVIDER` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--zone`=`ZONE` (`--oidc-config`=`OIDC_CONFIG` | `--saml-config`=`SAML_CONFIG`) [`--async`] [`--proxy`=`PROXY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates an identity provider for a Google Destributed Cloud zone. 
EXAMPLES
     To create an OIDC identity provider called `sample-identity-provider` in organization `sample-org`, location `us-central1` with the contents of `test-config.json` on zone `us-central1-edge-sample-zone`: 
    
    
    gcloud alpha edge-cloud identity-providers create sample-identity-provider --location=us-central1 --organization=sample-org --oidc-config=test-config.json --zone=us-central1-edge-sample-zone

POSITIONAL ARGUMENTS
    

IdentityProvider resource - Identity Provider The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`IDENTITY_PROVIDER`
     ID of the identityProvider or fully qualified identifier for the identityProvider. 

To set the `identity_provider` attribute: 

  * provide the argument `identity_provider` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `identity_provider` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization name. 

To set the `organization` attribute: 

  * provide the argument `identity_provider` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


REQUIRED FLAGS
    

`--zone`=`ZONE`
     Google Distributed Cloud zone name. 
Exactly one of these must be specified: 

`--oidc-config`=`OIDC_CONFIG`
     OIDC Identity Provider configuration file. 
`--saml-config`=`SAML_CONFIG`
     SAML Identity Provider configuration file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--proxy`=`PROXY`
     Identity Provider proxy endpoint. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `edgecontainer/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/edge-cloud>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
