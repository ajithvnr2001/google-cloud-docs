---
url: https://docs.cloud.google.com/apigee/docs/apihub/add-iam-conditions/
title: Add IAM conditions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:49.043037+00:00
---

# Add IAM conditions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/add-iam-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Add IAM conditions Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

Identity and Access Management (IAM) Conditions lets you to define and enforce conditional access control for Google Cloud resources, including API hub resources. For more information about IAM Conditions, see [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). 

In API hub, you can enforce conditional access based on the following [IAM resource condition attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource):

  * **resource.service condition attribute** : Use to configure conditional access based on the Google Cloud service being used. For example, you can set a condition limiting a user's access to resources that use the `apihub.googleapis.com`. For a list of supported values, see [Resource service values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-service). 
  * **resource.type condition attribute** : Use to configure conditional access based on the type of resource being accessed. For example, you can set a condition limiting a user's access to `apihub.googleapis.com/Api`. For a list of supported values, see [Resource type values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-type).
  * **resource.name condition attribute** : Use to configure conditional access based on all or part of the name of a resource. For a list of supported API hub name formats, see [Resource name format](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).
  * **Resource tags** : Use to configure conditional access based on the [tags](https://docs.cloud.google.com/apigee/docs/apihub/attach-manage-tags) attached to a resource. For example, you can set a condition that grants a role only for resources that have the tag `env: prod` attached.



## Add IAM condition

To add an IAM condition to a existing principal (user, group, or service account), perform the following steps:

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select your project, folder, or organization. 
  3. From the list of principals, find the principal for which you want to add the IAM condition, and click edit (**Edit principal**). 

The **Edit access** pane appears.

  4. Find the role to which you want to add the IAM condition and click **\+ Add IAM Condition**. 
  5. In the **Add condition** pane, provide the following information: 
     1. **Title:** Enter a name for the condition that you're adding to the role.
     2. **Description:** (Optional) Enter a description for the condition.
     3. You can add a condition using either the **Condition builder** or the **Condition editor**. 

The **Condition builder** provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The **Condition editor** provides a text-based interface to manually enter a condition expression using [CEL](https://docs.cloud.google.com/iam/docs/conditions-overview#cel) syntax.

For detailed instructions about how to use the **Condition builder** or the **Condition editor** , see [Configure resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access).

     4. Click **Save** to apply the condition. 
  6. Click **Save** again from the **Edit access** pane to update the principal.



## Examples of using IAM conditions for API hub

### Example 1: Access control for all API resources starting with a prefix or based on a [Tag](https://docs.cloud.google.com/apigee/docs/apihub/attach-manage-tags).

The following condition expression defines access control as follows:

  * Access to API resources starting with prefix. This includes access to all API resources (API versions, deployments, specifications, operations, and definitions) under that prefix.
  * Access to API resources that have a specific tag applied, regardless of their name.
  * Default role-based non-conditional access to other API hub resources.


    
    
      (
        resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION/apis/API_ID_PREFIX") ||
        resource.matchTagId("tagKeys/TAG_KEY", "tagValues/TAG_VALUE") ||
        (
          resource.type != "apihub.googleapis.com/Api" &&
          resource.type != "apihub.googleapis.com/Version" &&
          resource.type != "apihub.googleapis.com/Spec" &&
          resource.type != "apihub.googleapis.com/ApiOperation" &&
          resource.type != "apihub.googleapis.com/Definition"
        )
      )

Replace the following: 

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The API hub location.
  * `API_ID_PREFIX`: The prefix for the API resource name.
  * `TAG_KEY`: The key of the tag to use for conditional access.
  * `TAG_VALUE`: The value of the tag to use for conditional access.



### Example 2: Access control for multiple APIs with IAM conditions based on resource type.

The following condition expression defines access control as follows:

  * Access to the API hub API resources starting with prefix.
  * Access to the API hub version resource starting with a specified version ID.
  * Access to the API hub spec resources starting with a specified spec ID.
  * Default role-based non-conditional access to other API hub resources.


    
    
      (
        resource.service == "apihub.googleapis.com" &&
        resource.type == "apihub.googleapis.com/Api" &&
        resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION/apis/API1_ID_PREFIX")
      ) ||
      (
        resource.service == "apihub.googleapis.com" &&
        resource.type == "apihub.googleapis.com/Version" &&
        resource.name == "projects/PROJECT_ID/locations/LOCATION/apis/API2_ID/versions/API2_VERSION_ID"
      ) ||
      (
        resource.service == "apihub.googleapis.com" &&
        resource.type == "apihub.googleapis.com/Spec" &&
        resource.name == "projects/PROJECT_ID/locations/LOCATION/apis/API3_ID/versions/API3_VERSION_ID/specs/API3_SPEC_ID"
      ) ||
      (
        resource.type != "apihub.googleapis.com/Api" &&
        resource.type != "apihub.googleapis.com/Version" &&
        resource.type != "apihub.googleapis.com/Spec" &&
        resource.type != "apihub.googleapis.com/ApiOperation" &&
        resource.type != "apihub.googleapis.com/Definition"
      )

Replace the following: 

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The API hub location.
  * `API1_ID_PREFIX`: The prefix for the first API resource name.
  * `API2_ID`: The ID of the second API resource.
  * `API2_VERSION_ID`: The ID of the second API version resource.
  * `API3_ID`: The ID of the third API resource.
  * `API3_VERSION_ID`: The ID of the third API version resource.
  * `API3_SPEC_ID`: The ID of the third API spec resource.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
