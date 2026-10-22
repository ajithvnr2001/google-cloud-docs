---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-service-accounts-add-iam-policy-binding/
title: gdcloud iam service-accounts add-iam-policy-binding \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:50.183076+00:00
---

# gdcloud iam service-accounts add-iam-policy-binding  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-service-accounts-add-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud iam service-accounts add-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam service-accounts add-iam-policy-binding - Grant a Role/ProjectRole/ClusterRole/OrganizationRole to a service account.

## SYNOPSIS
    
    
    gdcloud iam service-accounts add-iam-policy-binding [flags]
    

## DESCRIPTION

Grant a Role, ProjectRole, ClusterRole or OrganizationRole to a project's service account. The name of the binding will be auto generated so you don't need to provide a name.

### EXAMPLES
    
    
      To grant the project role of name "pr-test" for project's service account "psa-test" in project "iam-test", run:
    
        gdcloud iam service-accounts add-iam-policy-binding --role=ProjectRole/pr-test --iam-account=psa-test --project=iam-test
    
    

### REQUIRED FLAGS
    
    
          --iam-account string   Project's service account to bind with the role. The flag is required to run the command.
          --role string          Role to bind with the service account in the format of "RoleType/NAME" where RoleType is one of the Kubernetes type in Role, ProjectRole, ClusterRole or OrganizationRole, and NAME is the name of the role. The flag is required to run the command.
    

### OPTIONAL FLAGS
    
    
          --role-namespace string   Namespace of Role to bind with the service account. This is only applicable for multizone enabled environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
