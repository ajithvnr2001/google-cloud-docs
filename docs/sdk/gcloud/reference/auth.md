---
url: https://docs.cloud.google.com/sdk/gcloud/reference/auth/
title: gcloud auth \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:29.274995+00:00
---

# gcloud auth  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud auth Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud auth - manage oauth2 credentials for the Google Cloud CLI 
SYNOPSIS
    

`gcloud auth` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The `gcloud auth` command group lets you grant and revoke authorization to Google Cloud CLI (`[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI) to access Google Cloud. Typically, when scripting Google Cloud CLI tools for use on multiple machines, using `[gcloud auth activate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)` is recommended. 

For information about authorization and credential types, see [Authorizing the gcloud CLI](https://cloud.google.com/sdk/docs/authorizing). For information about authorizing a service account, see [Authorizing with a service account](https://cloud.google.com/sdk/docs/authorizing#service-account). 

After running `gcloud auth` commands, you can run other commands with `--account`=``ACCOUNT`` to authenticate the command with the credentials of the specified account. For information about `--account` and other `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI global flags, see the [gcloud CLI overview](https://cloud.google.com/sdk/gcloud/reference). 

See `$ [gcloud topic client-certificate](https://docs.cloud.google.com/sdk/gcloud/reference/topic/client-certificate)` to learn how to use Mutual TLS when using gcloud. Mutual TLS can be used for [certificate based access](https://cloud.google.com/beyondcorp-enterprise/docs/securing-resources-with-certificate-based-access) with gcloud. 

EXAMPLES
     To authenticate a user account with `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` and minimal user output, run: 
    
    
    [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) --brief

To list all credentialed accounts and identify the current active account, run: 
    
    
    [gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)

To revoke credentials for a user account (like logging out), run: 
    
    
    [gcloud auth revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke) test@gmail.com

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[application-default](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default)`
     Manage your active Application Default Credentials. 
`[enterprise-certificate-config](https://docs.cloud.google.com/sdk/gcloud/reference/auth/enterprise-certificate-config)`
     Manage enterprise certificate configurations. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[activate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)`
     Authorize access to Google Cloud with a service account. 
`[configure-docker](https://docs.cloud.google.com/sdk/gcloud/reference/auth/configure-docker)`
     Register `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` as a Docker credential helper. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`
     Lists credentialed accounts. 
`[login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`
     Authorize gcloud to access the Cloud Platform with Google user credentials. 
`[print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token)`
     Print an access token for the specified account. 
`[print-identity-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-identity-token)`
     Print an identity token for the specified account. 
`[revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke)`
     Revoke access credentials for an account. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha auth](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth)
    
    
    [gcloud beta auth](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
