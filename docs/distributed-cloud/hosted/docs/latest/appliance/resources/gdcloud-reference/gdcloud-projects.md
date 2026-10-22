---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-projects/
title: gdcloud projects \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:01.788782+00:00
---

# gdcloud projects  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud projects Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud projects - Create and manage GDC air-gapped projects.

## SYNOPSIS
    
    
    gdcloud projects COMMAND [flags]
    

## DESCRIPTION

Create and manage GDC air-gapped projects to define logical grouping for your service resources. A project is a key tenancy unit that every service must integrate.

Projects enable segmentation of resources within an organization and provide a lifecycle and policy boundary for managing resources. Resources inside a project can never outlive the project itself or move between projects, ensuring that control is guaranteed for the life of the resource. A project is considered a proper Kubernetes namespace that spans across multiple Kubernetes clusters in an organization.

Kubernetes clusters must be attached to a project to run containerized workloads. However, clusters are organization-scoped and not directly managed by a project.

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

### COMMANDS

`COMMAND` is one of the following:
    
    
    add-iam-policy-binding
        Grant a role to a member in a project.
    create
        Create a project.
    delete
        Delete a project.
    describe
        Display information regarding a particular project.
    get-iam-policy
        List all the iam policy for a project.
    list
        List the projects accessible by the current user in the organization.
    remove-iam-policy-binding
        Remove a role from a member in a project.
    update
        Update a particular project's attributes.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
