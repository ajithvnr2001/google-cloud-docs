---
url: https://docs.cloud.google.com/resource-manager/docs/troubleshooting-project-deletion/
title: Troubleshooting project deletion \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:14:40.175067+00:00
---

# Troubleshooting project deletion  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/troubleshooting-project-deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Troubleshooting project deletion Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe common errors that can block the deletion of a project, and what you can do to resolve them. If you are having issues, try using the Google Cloud CLI to shut down a project, and note any error message you receive.

## Liens

If there is a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on a project, that project cannot be deleted until the lien is removed. If you have the `resourcemanager.projects.get` permission on the project, you can list the liens applied to a project with the `liens list` gcloud CLI command.

For more information about liens, see [protecting projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

## Cloud Endpoints

Cloud Endpoints are special resources that are considered child resources under a project. This can block the deletion of a project where Endpoints exist.

The following example shows an attempt to delete a project using the Google Cloud CLI failing due to the existence of Endpoints under the project:
    
    
    @cloudshell:~ ($project)$ gcloud projects delete $project
    Your project will be deleted.
    
    Do you want to continue (Y/n)?  Y
    
    ERROR: (gcloud.projects.delete) FAILED_PRECONDITION: active child resource
    - '@type':type.googleapis.com/google.rpc.PreconditionFailure
     violations:
     - description: active child resource
       subject: services/$service
    - '@type':type.googleapis.com/google.rpc.ResourceInfo
     resourceName: projects/$project
     resourceType: PROJECT
    

To resolve this issue, [delete the Endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/delete) before you attempt to delete the project.

For more information about Endpoints, see the [Cloud Endpoints documentation](https://docs.cloud.google.com/endpoints/docs).

## Management projects

If a project is designated as a management project for an app-enabled folder, you can't delete the project directly. This can block the deletion of a project with an error message similar to the following:
    
    
    ERROR: (gcloud.projects.delete) FAILED_PRECONDITION: Deletion is not allowed
    because this project is the management project for the folder it resides in.
    

To resolve this issue, you can disable application management on the parent folder. Disabling application management automatically deletes the management project.

To disable application management using the gcloud CLI, run the following command:
    
    
    gcloud resource-manager capabilities update folders/FOLDER_ID/capabilities/app-management --no-enable
    

For instructions on disabling application management using the Google Cloud console, see [Managing applications in a folder](https://docs.cloud.google.com/resource-manager/docs/manage-applications#disable-application-management).

### Workaround for orphaned states

In some cases, a parent folder's application management might appear to be disabled, but the associated project remains blocked with the same error. To unlink the project from the folder in this scenario, you can clear the App Hub boundary CRM node.

**Note:** This command is in alpha and its usage or flags might change.

To clear the boundary using the gcloud CLI, run the following command:
    
    
    gcloud alpha apphub boundary update --project=PROJECT_ID --location=global --crm-node=''
    

## Shared Virtual Private Cloud

If a project has shared Virtual Private Cloud (VPC) enabled or has service projects attached, a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) will block the deletion of the project.

For more details and instructions on how to detach service projects and disable shared VPC, see [Deprovisioning shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc#deleting_projects).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
