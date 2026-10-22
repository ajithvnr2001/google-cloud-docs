---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-organizations/
title: gdcloud organizations \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:27.192323+00:00
---

# gdcloud organizations  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud organizations Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud organizations - Create and manage GDC air-gapped organizations.

## SYNOPSIS
    
    
    gdcloud organizations GROUP | COMMAND [flags]
    

## DESCRIPTION

Create and manage GDC air-gapped organizations. The organization resource represents an organization, such as a company, and is the top-level resource in the GDC air-gapped resource hierarchy. An organization defines a security boundary that encloses infrastructure resources to be administered together so that users can deploy application workloads. Within an organization, service resources such as VMs and storage volumes are logically grouped by projects.

All projects, clusters, and service resources belong to your organization instead of their creators. This means that any resource type for an organization is not deleted if the user who created it leaves the organization. Instead, all resource types follow the organization's lifecycle in the GDC air-gapped configuration.

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

### GROUPS

`GROUP` is one of the following:
    
    
    config
        Edit the Organization YAML file.
    maintenance-window
        Update and view maintenance windows for organization upgrades.
    upgrade
        Command group for GDC air-gapped upgrade
    zonal-configs
        Edit the OrganizationZonalConfig YAML file.
    

### COMMANDS

`COMMAND` is one of the following:
    
    
    add-iam-policy-binding
        Grant a role to a member in an organization
    create
        Create an Organization custom resource from a YAML file.
    describe
        Display information regarding a particular organization.
    list
        List all organizations.
    remove-iam-policy-binding
        Remove a role from a member in an organization
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
