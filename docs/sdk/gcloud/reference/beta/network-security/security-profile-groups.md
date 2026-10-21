---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/
title: gcloud beta network-security security-profile-groups \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:37:05.773485+00:00
---

# gcloud beta network-security security-profile-groups  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security security-profile-groups Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security security-profile-groups - manage Network Security - Security Profile Groups 
SYNOPSIS
    

`gcloud beta network-security security-profile-groups` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage Network Security - Security Profile Groups. 
EXAMPLES
     To create a Security Profile Group with the name `my-security-profile-group` (Either a fully specified path or `--location` and `--organization` flags for SPG should be specified), `--threat-prevention-profile` `my-security-profile` and optional description as `optional description`, run: 
    
    
    [gcloud beta network-security security-profile-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/create) my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-security-profile` --description='optional description'

To delete an Security Profile Group called `my-security-profile-group` (Either a fully specified path or `--location` and `--organization` flags for SPG should be specified) run: 
    
    
    [gcloud beta network-security security-profile-groups delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/delete) my-security-profile-group --organization=1234 --location=global

To show details of a Security Profile Group named `my-security-profile-group` (Either a fully specified path or `--location` and `--organization` flags for SPG should be specified) run: 
    
    
    [gcloud beta network-security security-profile-groups describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/describe) my-security-profile-group --organization=1234 --location=global

To list Security Profile Groups in specified location and organization, run: 
    
    
    [gcloud beta network-security security-profile-groups list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/list) --location=global

To update an SPG with new Threat prevention profile `my-new-security-profile` (Either a fully specified path or `--location` and `--organization` flags for SPG should be specified), run: 
    
    
    [gcloud beta network-security security-profile-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/update) my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-new-security-profile` --description='New Security Profile of type threat prevention'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/create)`
     `(BETA)` Create a new Security Profile Group. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/delete)`
     `(BETA)` Delete a Security Profile Group. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/describe)`
     `(BETA)` Describe a Security Profile Group. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/list)`
     `(BETA)` List Security Profile Groups. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/update)`
     `(BETA)` Update a Security Profile Group. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security security-profile-groups](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups)
    
    
    [gcloud alpha network-security security-profile-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profile-groups)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
