---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/
title: gcloud alpha network-security security-profiles threat-prevention \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:07:16.176477+00:00
---

# gcloud alpha network-security security-profiles threat-prevention  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-security security-profiles threat-prevention Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-security security-profiles threat-prevention - manage Security Profiles - Threat Prevention Profile 
SYNOPSIS
    

`gcloud alpha network-security security-profiles threat-prevention` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage Security Profiles - Threat Prevention Profile. 
EXAMPLES
     To create a Security Profile with the name `my-security-profile` which includes location as global or region specified and organization ID, optional description as `New Security Profile`, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention create my-security-profile --description="New Security Profile"

To add an override, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention add-override my-security-profile --severities=MEDIUM --action=ALLOW
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To update an override, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention update-override my-security-profile --severities=MEDIUM --action=ALLOW
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To list overrides, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention list-overrides my-security-profile
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To delete an override, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention delete-override my-security-profile --severities=MEDIUM
    
    
    `my-security-profile` is the name of the Security Profile in the
    format organizations/{organizationID}/locations/{location}/securityProfiles/
    {security_profile_id} where organizationID is the organization ID to which
    the changes should apply, location either global or region specified and
    security_profile_id the Security Profile Identifier.

To list Security Profiles in specified location and organization, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention list --location=global

To describe a Security Profile called `my-security-profile`, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention describe my-security-profile

To delete a Security Profile called `my-security-profile` which includes location as global or region specified and organization ID, run: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention delete my-security-profile

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-override](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/add-override)`
     `(ALPHA)` Add overrides to Threat Prevention Profile. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/create)`
     `(ALPHA)` Create a new Threat Prevention Profile. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/delete)`
     `(ALPHA)` Delete a Threat Prevention Profile. 
`[delete-override](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/delete-override)`
     `(ALPHA)` Delete overrides of Threat Prevention Profile. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/describe)`
     `(ALPHA)` Describe a Threat Prevention Security Profile. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/list)`
     `(ALPHA)` List Threat Prevention Security Profiles. 
`[list-overrides](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/list-overrides)`
     `(ALPHA)` List overrides of Threat Prevention Profile. 
`[update-override](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/threat-prevention/update-override)`
     `(ALPHA)` Update Overrides of Threat Prevention Profile. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention)
    
    
    [gcloud beta network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
