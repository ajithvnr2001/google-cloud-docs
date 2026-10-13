---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-projects-add-iam-policy-binding/
title: gdcloud projects add-iam-policy-binding \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:36.779516+00:00
---

# gdcloud projects add-iam-policy-binding  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-projects-add-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud projects add-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud projects add-iam-policy-binding - Grant a role to a member in a project.

## SYNOPSIS
    
    
    gdcloud projects add-iam-policy-binding PROJECT_ID [flags]
    

## DESCRIPTION

Grant a role to a member in a project. The member can either be a human user or a service account. The name of the binding is auto-generated.

### EXAMPLES
    
    
    To grant the role "pr-test-role" for user "test-user@example.com" with IdP prefix "fop" in project "iam-test", run:
    
        gdcloud projects add-iam-policy-binding iam-test --role=pr-test-role --member=user:fop-test-user@example.com
    
    To grant the role "pr-test-role" for service account "test-sa" of project "test-sa-project" in the project "iam-test", run:
    
        gdcloud projects add-iam-policy-binding iam-test --role=pr-test-role --member=serviceAccount:test-sa-project:test-sa
    
    

### REQUIRED FLAGS
    
    
          --member string   Member to add the binding for, defined by either user:EMAIL or serviceAccount:SERVICE_ACCOUNT_PROJECT:SERVICE_ACCOUNT_NAME. The email should contain the IdP prefix for the user.
          --role string     Role name to assign to the member.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
