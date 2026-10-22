---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts/
title: gdcloud iam service-accounts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:27.660984+00:00
---

# gdcloud iam service-accounts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam service-accounts Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam service-accounts - Manage project's service accounts and keys.

## SYNOPSIS
    
    
    gdcloud iam service-accounts GROUP | COMMAND [flags]
    

## DESCRIPTION

Create, list, delete project's service accounts, or grant permissions for a project's service account. A subcommand group "gdcloud iam service-accounts keys" manages service accounts' credentials. You must have the "project-iam-admin" role in a project to manage the service accounts and keys for that project.

### EXAMPLES
    
    
      To list all the service accounts from project "iam-test", run:
    
        gdcloud iam service-accounts list --project=iam-test
    
      To create a service account of name "psa-test" for project "iam-test", run:
    
        gdcloud iam service-accounts create psa-test --project=iam-test
    
      To delete a service account of name "psa-test" from project "iam-test", run:
    
        gdcloud iam service-accounts delete psa-test --project=iam-test
    
      To grant the project role of name "pr-test" for project's service account "psa-test" in project "iam-test", run:
    
        gdcloud iam service-accounts add-iam-policy-binding --role=ProjectRole/pr-test --iam-account=psa-test --role-namespace=iam-test
    
        or
    
        gdcloud iam service-accounts add-iam-policy-binding --role=ProjectRole/pr-test --iam-account=psa-test --project=iam-test
    
        "--project" and "--role-namespace" flags are mutually exclusive.
    
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

### GROUPS

`GROUP` is one of the following:
    
    
    keys
        Manage keys for a project's service account.
    

### COMMANDS

`COMMAND` is one of the following:
    
    
    add-iam-policy-binding
        Grant a Role/ProjectRole/ClusterRole/OrganizationRole to a service account.
    create
        Create a new service account for a project.
    delete
        Delete a service account from a project.
    list
        List all the service accounts from a project
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
