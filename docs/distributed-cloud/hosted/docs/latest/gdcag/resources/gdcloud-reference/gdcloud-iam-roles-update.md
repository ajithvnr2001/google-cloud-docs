---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-update/
title: gdcloud iam roles update \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:32.658957+00:00
---

# gdcloud iam roles update  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam roles update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam roles update - Update a custom role.

## SYNOPSIS
    
    
    gdcloud iam roles update ROLE_NAME
        { --file=ROLE_FILE |
        [--description=DESCRIPTION]
        [--title=TITLE]
        [--permissions=[permissions1,...]]
        [--stage=[ALPHA | BETA | GA | DISABLED]]
        [--projects=[project1,...]]
        } [flags]
    

## DESCRIPTION

Update a custom role with narrowly-defined permissions for a project or organization scope. This role grants only the minimum access necessary to perform specific tasks, adhering to the principle of least privilege.

### EXAMPLES
    
    
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
    

### OPTIONAL FLAGS
    
    
          --description string                               Overrides description of the CustomRole custom resource.
          --file string                                      Path to a file containing YAML configuration for a CustomRole custom resource. If set, the gdcloud CLI updates the CustomRole from the YAML configuration and ignores the other flags. The YAML file can contain any combination of the following fields: 'title', 'description', 'permissions', 'stage', and 'projects'. The 'permissions' field, if provided, must adhere to the 'iamRoleName:apiGroup:resource:verb' or 'iamRoleName:apiGroup:resource:resourceName:verb' format (no wildcards). All fields are optional during an update but must follow the format and restrictions of their corresponding command-line flags.
          --permissions iamRoleName:apiGroup:resource:verb   Overrides a list of permissions granted to this CustomRole. Each permission must be specified in one of the following formats: iamRoleName:apiGroup:resource:verb (for resource that don't have individual name) or `iamRoleName:apiGroup:resource:resourceName:verb` (for resource with specific name). Wildcards (`*`) are explicitly prohibited in any part of the permission string (apiGroup, resource, verb, or resourceName) to enforce the principle of least privilege.
          --projects strings                                 Comma-separated list of project IDs where the CustomRole will be applied. When updating project-scoped custom roles, the specified projects are merged with existing projects, unless the existing projects contain a wildcard (*). In that case, the wildcard is preserved, indicating that the role applies to all projects. Required when updating project-scoped custom roles; not applicable for 'organization' scope. Example: --projects=project-id-1,project-id-2,project-id-3.
          --stage string                                     Overrides release stage of the CustomRole (ALPHA, BETA, GA or DISABLED). Use DISABLED to disable the CustomRole.
          --title string                                     Overrides title of the CustomRole custom resource.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
