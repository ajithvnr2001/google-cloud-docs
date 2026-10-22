---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles/
title: gdcloud iam roles \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:39.693275+00:00
---

# gdcloud iam roles  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam roles Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam roles - Manage custom roles for projects or organizations.

## SYNOPSIS
    
    
    gdcloud iam roles COMMAND [flags]
    

## DESCRIPTION

Manage custom roles for projects or organizations. This command provides a unified way to operate custom roles, allowing you to define roles for customized access level.

### EXAMPLES
    
    
    To create an organization-level custom role with specific permissions, run:
    
        gdcloud iam roles create org-viewer --scope=organization --title="Organization Viewer" --description="Grants read-only access to storage buckets and compute instances at the organization level" --permissions=storageAdmin:compute:instances.get,storageAdmin:storage:buckets.list --stage=<BETA|GA|ALPHA>
    
    To create a project-level custom role for deploying resources in specific project namespaces, run:
    
        gdcloud iam roles create project-resource-manager --scope=project --title="Project Resource Manager" --description="Allows managing compute instances and disks within specific projects" --permissions=storageAdmin:compute:instances.get,storageAdmin:compute:disks.create --stage=<BETA|GA|ALPHA> --projects=project-id-1,project-id-2...
    
    To create a project-level custom role applicable to all projects, run:
    
        gdcloud iam roles create project-instance-operator --scope=project --title="Project Instance Operator" --description=""Grants permissions to start and stop compute instances across all projects" --permissions=admin:compute:instances.start,admin:compute:instances.stop --stage=<BETA|GA|ALPHA>
    
    To create a custom role in a specific system namespace, run:
    
        gdcloud iam roles create iam-role-manager --scope=organization --title="IAM Role Manager" --description="Allows creating and updating IAM roles" --permissions=iamAdmin:iam:roles:create,iamAdmin:iam:roles:update --stage=<BETA|GA|ALPHA> --namespace=<namespace-name>
    
    To create a custom role from a YAML configuration file, run:
    
        gdcloud iam roles create my_role --file=ROLE_FILE
    
    To describe a role at organization scope, run:
    
        gdcloud iam roles describe org-role
    
    To describe a role at project scope, run:
    
        gdcloud iam roles describe project-role --project my-project
    
    To delete a custom role at organization scope, run:
    
        gdcloud iam roles delete org-role
    
    To delete a custom role at project scope, run:
    
        gdcloud iam roles delete project-role --project my-project
    
    To update an organization-level custom role with specific permissions, run:
    
        gdcloud iam roles update org-viewer --permissions=storageAdmin:compute:instances.get,storageAdmin:storage:buckets.list
    
    To update a project-level custom role for deploying resources in specific project namespaces, run:
    
        gdcloud iam roles update project-resource-manager --permissions=storageAdmin:compute:instances.get,storageAdmin:compute:disks.create --projects=project-id-1,project-id-2
    
    To update a project-level custom role applicable to all projects, run:
    
        gdcloud iam roles update project-instance-operator --permissions=admin:compute:instances.start,admin:compute:instances.stop
    
    To update title and description of a custom role, run:
    
        gdcloud iam roles update org-viewer --title="Organization Viewer v2" --description="Grants read-only access to storage buckets and compute instances at the organization level v2"
    
    To add additional projects to an existing project-level custom role, run:
    
        gdcloud iam roles update project-resource-manager --projects=project-id-3,project-id-4
    
    To update a custom role from a YAML configuration file, run:
    
        gdcloud iam roles update my_role --file=ROLE_FILE
    
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
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

### COMMANDS

`COMMAND` is one of the following:
    
    
    create
        Create a custom role.
    delete
        Delete a custom role.
    describe
        Describe a role[custom/predefined].
    list
        List roles[custom/predefined/all].
    update
        Update a custom role.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
