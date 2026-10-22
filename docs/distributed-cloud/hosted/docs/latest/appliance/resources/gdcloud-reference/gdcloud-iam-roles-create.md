---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-roles-create/
title: gdcloud iam roles create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:51.326610+00:00
---

# gdcloud iam roles create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-iam-roles-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud iam roles create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam roles create - Create a custom role.

## SYNOPSIS
    
    
    gdcloud iam roles create ROLE_NAME
        { --file=ROLE_FILE |
        --description=DESCRIPTION
        --title=TITLE
        [--scope=[PROJECT | ORGANIZATION]]
        [--permissions=[permissions1,...]]
        [--stage=[ALPHA | BETA | GA | DISABLED]]
        [--projects=[project1,...]]
        [--namespace=NAMESPACE]
        } [flags]
    

## DESCRIPTION

Create a custom role with narrowly-defined permissions for a project or organization scope. This role grants only the minimum access necessary to perform specific tasks, adhering to the principle of least privilege.

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
    

### REQUIRED FLAGS
    
    
          --description string                               Description of the CustomRole custom resource.
          --permissions iamRoleName:apiGroup:resource:verb   A list of permissions granted to this CustomRole. Each permission must be specified in one of the following formats: iamRoleName:apiGroup:resource:verb (for resource that don't have individual name) or `iamRoleName:apiGroup:resource:resourceName:verb` (for resource with specific name). Wildcards (`*`) are explicitly prohibited in any part of the permission string (apiGroup, resource, verb, or resourceName) to enforce the principle of least privilege.
          --title string                                     Title of the CustomRole custom resource.
    

### OPTIONAL FLAGS
    
    
          --file string        Path to a file containing YAML configuration for a CustomRole custom resource. If set, the gdcloud CLI creates the CustomRole from the YAML configuration and ignores the other flags. The YAML must include 'title', 'description', and 'permissions' (formatted as 'iamRoleName:apiGroup:resource:verb' or 'iamRoleName:apiGroup:resource:resourceName:verb', no wildcards). Optional fields: 'stage', 'scope', 'projects', 'namespace' (if applicable). These fields, if present, must follow the same format as their corresponding command-line flags.
          --namespace string   Namespace of the CustomRole custom resource, required only when defining permissions in organization scope.
          --projects strings   Comma-separated list of project IDs where the CustomRole will be applied. Required when the scope is 'project'; not applicable for 'organization' scope. Example: --projects=project-id-1,project-id-2,project-id-3
          --scope string       Scope of the CustomRole (organization or project). Use 'organization' for system-level permissions and 'project' for project-specific permissions. (default "organization")
          --stage string       Release stage of the CustomRole (ALPHA, BETA, or GA). (default "ALPHA")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
