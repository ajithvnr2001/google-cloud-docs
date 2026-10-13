---
url: https://docs.cloud.google.com/resource-manager/docs/analyze-move/
title: Analyze project move \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:31.488841+00:00
---

# Analyze project move  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/analyze-move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Analyze project move Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use the Cloud Asset Inventory Analyze Move API to get a detailed report on warnings and blockers from a list of critical policies systems prior to actually moving your project.

## Enable APIs

Select or create a project as your API consumer project, enable [Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

This consumer project can be different from the project you plan to analyze and migrate. Consumer project will be used to generate credentials to make API request.

The next section describes the required roles and permissions that must be granted on the source project you plan to analyze.

## Required Permissions

To perform a project move analysis, you need a role that grants the `cloudasset.assets.analyzeMove` permission, such as **Cloud Asset Viewer** or **Viewer**. You can grant this role on the project, or on its parent folder or organization resource.

To receive analysis on a service, you also need roles related to those services. These permissions include the following:

  * If you want to view the inherited allow policies from the source project's parent organization resource, you need the `resourcemanager.organizations.getIamPolicy` permission on the source project's parent organization resource.

  * If you want to view the inherited allow policies from the source project's parent folder, you need the `resourcemanager.folders.getIamPolicy` permission on the source project's parent folder.

  * If you want to view the allow policies on the project, you need the `resourcemanager.projects.getIamPolicy` permission on the source project.

  * If you want to view the inherited deny policies from the source project's parent organization resource, you need the `iam.denypolicies.get` permission on the source project's parent organization resource.

  * If you want to view the organization policies that are inherited on this project, you need the `orgpolicy.policy.get` permission on the source project.

  * If you want to view the Compute Engine firewall policies that are inherited on this project, you need the `compute.organizations.setSecurityPolicy` permission on the source folder or organization resource. Although this permission contains "set", it is required to retrieve and view the inherited security policies.

  * If you want to view the inherited tags on this project, you need the `resourcemanager.hierarchyNodes.listEffectiveTags` permission on the source project or its ancestor nodes.




## Perform the analysis

You can use the Google Cloud CLI or the API to analyze the migration of a resource from its current place in the resource hierarchy.

**Note:** This API does not perform any checks on the destination organization resource. Even if the destination organization resource specified in the API call does not exist, the analysis of the project to be moved is still performed.

###  gcloud 

To analyze the impacts of migrating a project from its current position in the resource hierarchy, use the `gcloud asset analyze-move` command:
    
    
    gcloud asset analyze-move --project=PROJECT_ID \
      (--destination-folder=FOLDER_ID \
        | --destination-organization=ORGANIZATION_ID)
    

To analyze the impacts of moving a project to a different **folder** , run the command with `--destination-folder`:
    
    
    gcloud asset analyze-move --project=PROJECT_ID \
      --destination-folder=FOLDER_ID
    

To analyze the impacts of moving a project to a different **organization** , run the command with `--destination-organization`:
    
    
    gcloud asset analyze-move --project=PROJECT_ID \
      --destination-organization=ORGANIZATION_ID
    

Where:

  * `PROJECT_ID` is the unique project ID of the project you are migrating. For example, `--myProject123`.

  * `FOLDER_ID` is the numerical folder ID of the destination folder on which to perform the analysis. For example, `45678901123`.

  * `ORGANIZATION_ID` is the numerical organization ID of the destination organization on which to perform the analysis. For example, `78901123456`.


**Note:** Exactly one of FOLDER_ID or ORGANIZATION_ID must be specified.

###  API 

To analyze the impacts of migrating a project from its current position in the resource hierarchy without performing the move, use the [cloudasset.analyzeMove](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove) method:
    
    
    GET https://cloudasset.googleapis.com/v1/{resource=*/*}: \
      analyzeMove?destinationParent=DESTINATION_NAME
    

Where:

  * `resource` is the name of the resource on which to perform the analysis. Only project resources are supported, so this must be the Project ID or a Project Number. For example, `projects/my-project-id` or `projects/12345`.

  * `DESTINATION_NAME` is the name of the Google Cloud folder or organization resource to reparent the target resource. The analysis will be performed on the impacts of moving the resource to the specified destination parent. The destination must be a folder number or an organization resource number. For example, `folders/123` or `organizations/123`.




## Move analysis responses

The response you receive from the Move Analysis API is grouped by service name. Under each service is a list of warnings and blockers applicable to this project migration. Any blockers being returned by this analysis means that the project migration will be blocked at run time if you proceed with the move before resolving them.

**Note:** Analysis results may not include functionality for services and features that are in preview. If your projects are part of any preview, please refer to that feature's user guide.

## Troubleshooting errors

If there is an error returned by the Move Analysis API, it includes a standard [gRPC code](https://grpc.github.io/grpc/core/md_doc_statuscodes.html), as well as a message that describes the reason for the failure of the Move Analysis API to analyze the project.

The following table describes the error codes that could potentially be returned by the Move Analysis API:

Error name | Error code | Description  
---|---|---  
Invalid argument  | 3  | Returned if you call the API on a project with an invalid argument, such as an incorrect resource name.  
Permission denied  | 7  | Returned if you do not have the permissions necessary to perform the analysis or the source project does not exist.  
Internal  | 13  | Returned if there is an issue with a call to a policy system such as Identity and Access Management or organization policy. This does not indicate that the migration is not possible, and you can retry the analysis after checking the service for an outage.  
Unavailable  | 14  | Returned if an internal system is out of sync. This does not indicate that the migration is not possible, and you can retry the analysis.  
Unauthenticated  | 16  | Returned if you have not provided the correct credentials to perform this analysis.  
  
#### Example error message

The following example demonstrates the error code returned for a user that does not have the `cloudasset.assets.analyzeMove` permission on the project to be migrated:
    
    
    {
      "error": {
      "code": 403,
      "message": "Failed to fetch Project: projects/test-project-service-3 to perform
                  move analysis.",
      "status": "PERMISSION_DENIED"}
    }
    

Some of the policy systems may fail to analyze the resource move. The following example demonstrates the error returned from the Hierarchical Firewall service when the user does not have `compute.organizations.setSecurityPolicy` permission on the project to be migrated:
    
    
    {
      "moveAnalysis": [{
        "displayName": "name hidden",
        "analysis": {
          "warnings": [{
            "detail": "details hidden"
          }]
        }
      }, {
        "displayName": "name hidden",
        "analysis": {
          "warnings": [{
            "detail": "details hidden"
          }]
        }
      }, {
        "displayName": "Hierarchical Firewall",
        "error": {
          "code": 7,
          "message": "Failed to retrieve inherited security policies to perform
                      analysis. Required 'compute.organizations.setSecurityPolicy'
                      permission for {resource ID}"
         }}]
    }
    

## What's next

The Move Analysis API provides details that help mitigate blockers and other issues when moving a project from one organization resource to another. For more information about migrating projects between organization resources, see [Migrate projects between organization resources](https://docs.cloud.google.com/resource-manager/docs/project-migration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
