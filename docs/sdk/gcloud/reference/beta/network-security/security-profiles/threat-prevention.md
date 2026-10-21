---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/
title: gcloud beta network-security security-profiles threat-prevention \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:03:37.688192+00:00
---

# gcloud beta network-security security-profiles threat-prevention  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security security-profiles threat-prevention Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security security-profiles threat-prevention - manage Security Profiles - Threat Prevention Profile 
SYNOPSIS
    

`gcloud beta network-security security-profiles threat-prevention` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage Security Profiles - Threat Prevention Profile. 
EXAMPLES
     To create a Security Profile with the name `my-security-profile` which includes location as global or region specified and organization ID, optional description as `New Security Profile`, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention create my-security-profile --description="New Security Profile"

To add an override, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention add-override my-security-profile --severities=MEDIUM --action=ALLOW
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To update an override, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention update-override my-security-profile --severities=MEDIUM --action=ALLOW
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To list overrides, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention list-overrides my-security-profile
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To delete an override, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention delete-override my-security-profile --severities=MEDIUM
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To list Security Profiles in specified location and organization, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention list --location=global

To describe a Security Profile called `my-security-profile`, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention describe my-security-profile

To delete a Security Profile called `my-security-profile` which includes location as global or region specified and organization ID, run: 
    
    
    gcloud beta network-security security-profiles threat-prevention delete my-security-profile

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-override](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/add-override)`
     `(BETA)` Add overrides to Threat Prevention Profile. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/create)`
     `(BETA)` Create a new Threat Prevention Profile. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/delete)`
     `(BETA)` Delete a Threat Prevention Profile. 
`[delete-override](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/delete-override)`
     `(BETA)` Delete overrides of Threat Prevention Profile. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/describe)`
     `(BETA)` Describe a Threat Prevention Security Profile. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/list)`
     `(BETA)` List Threat Prevention Security Profiles. 
`[list-overrides](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/list-overrides)`
     `(BETA)` List overrides of Threat Prevention Profile. 
`[update-override](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/update-override)`
     `(BETA)` Update Overrides of Threat Prevention Profile. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention)
    
    
    [gcloud alpha network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
