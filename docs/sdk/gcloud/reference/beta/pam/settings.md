---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/
title: gcloud beta pam settings \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:04:05.075691+00:00
---

# gcloud beta pam settings  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pam settings Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pam settings - manage Privileged Access Manager Settings 
SYNOPSIS
    

`gcloud beta pam settings` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The `gcloud pam settings` command group lets you manage Privileged Access Manager (PAM) settings. 
EXAMPLES
     To describe the PAM Settings on a project named `sample-project` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe) --project=sample-project --location=global

To describe the PAM Settings on a folder with ID ``FOLDER_ID`` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe) --folder=FOLDER_ID --location=global

To describe the PAM Settings on an organization with ID ``ORGANIZATION_ID`` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe) --organization=ORGANIZATION_ID --location=global

To describe the effective PAM Settings on a project named `sample-project` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe-effective](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe-effective) --project=sample-project --location=global

To describe the effective PAM Settings on a folder with ID ``FOLDER_ID`` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe-effective](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe-effective) --folder=FOLDER_ID --location=global

To describe the effective PAM Settings on an organization with ID ``ORGANIZATION_ID`` and in location `global`, run: 
    
    
    [gcloud beta pam settings describe-effective](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe-effective) --organization=ORGANIZATION_ID --location=global

To export the PAM Settings configured on a project named `sample-project`, and in location `global` to a local YAML file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/export) --project=sample-project --location=global --destination=pam-settings.yaml

To export the PAM Settings configured on a folder with ID ``FOLDER_ID``, and in location `global` to a local YAML file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/export) --folder=FOLDER_ID --location=global --destination=pam-settings.yaml

To export the PAM settings configured for an organization with ID `ORGANIZATION_ID` in location `global` to a local YAML file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/export) --organization=ORGANIZATION_ID --location=global --destination=pam-settings.yaml

To update the PAM Settings on a project named `sample-project` and in location `global`, and the new updated settings configuration stored in a file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/update) --project=sample-project --location=global --settings-file=pam-settings.yaml

To update the PAM Settings on a folder with ID ``FOLDER_ID`` and in location `global`, and the new updated settings configuration stored in a file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/update) --folder=FOLDER_ID --location=global --settings-file=pam-settings.yaml

To update the PAM Settings on an organization with ID ``ORGANIZATION_ID`` and in location `global`, and the new updated settings configuration stored in a file named `pam-settings.yaml`, run: 
    
    
    [gcloud beta pam settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/update) --organization=ORGANIZATION_ID --location=global --settings-file=pam-settings.yaml

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe)`
     `(BETA)` Show details of Privileged Access Manager (PAM) settings on a resource. 
`[describe-effective](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/describe-effective)`
     `(BETA)` Show effective Privileged Access Manager (PAM) settings on a resource. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/export)`
     `(BETA)` Export Privileged Access Manager (PAM) settings configured on a project, folder, or organization to a local YAML file. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/settings/update)`
     `(BETA)` Update Privileged Access Manager (PAM) settings configured on a project, folder, or organization. 
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha pam settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
