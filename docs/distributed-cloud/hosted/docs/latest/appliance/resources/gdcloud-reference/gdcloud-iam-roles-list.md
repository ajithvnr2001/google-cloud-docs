---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-roles-list/
title: gdcloud iam roles list \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:37.143670+00:00
---

# gdcloud iam roles list  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-roles-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud iam roles list Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam roles list - List roles[custom/predefined/all].

## SYNOPSIS
    
    
    gdcloud iam roles list (custom | predefined | all) [--project=PROJECT] [flags]
    

## DESCRIPTION

This command lists the roles of a specified type: 'custom', 'predefined' or 'all'. Optionally, you can specify a project to filter the results.

### EXAMPLES
    
    
    To list all roles, run:
    
        gdcloud iam roles list
    
    To list predefined roles, run:
    
        gdcloud iam roles list --type=predefined
    
    To list custom roles, run:
    
        gdcloud iam roles list --type=custom
    
    To list all roles for a specific project, run:
    
        gdcloud iam roles list --project=my-project
    
    To list predefined roles for a specific project, run:
    
        gdcloud iam roles list --type=predefined --project=my-project
    
    To list custom roles for a specific project, run:
    
        gdcloud iam roles list --type=custom --project=my-project
    

### OPTIONAL FLAGS
    
    
          --type string   Type of roles to list. Valid values are 'custom', 'predefined', or 'all'. (default "all")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
