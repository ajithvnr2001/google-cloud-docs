---
url: https://docs.cloud.google.com/application-integration/docs/add-iam-conditions/
title: Add IAM conditions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:33.079292+00:00
---

# Add IAM conditions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/add-iam-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add IAM conditions

Identity and Access Management (IAM) Conditions lets you to define and enforce conditional, attribute-based access control for Google Cloud resources, including Application Integration resources. For more information about IAM Conditions, see [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). 

In Application Integration, you can enforce conditional access based on the following attributes:

  * **Date/time attributes:** Use to set temporary (expiring), scheduled, or limited-duration access to Application Integration resources. For example, you can allow a user to access an integration until a specified date. For more information, see [Configuring temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access). 
  * **Resource attributes** : Use to configure conditional access based on a resource name, resource type, or resource service attributes. For example, you can allow a user to manage integrations that are created in a specific region. For a list of supported values. For more information, see [Configuring resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access). 



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

For information about the supported resource attributes for Application Integration, see Resource attribute values

  6. Click **Save** again from the **Edit access** pane to update the principal.



## Resource attribute values

The following table lists the values that the resource type attribute can contain for Application Integration:

Resource name  |  Resource type  | Reference   
---|---|---  
Location  | `integrations.googleapis.com/Location` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1)  
Integration  | `integrations.googleapis.com/Integration` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations)  
IntegrationVersion  | `integrations.googleapis.com/IntegrationVersion` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions)  
Execution  | `integrations.googleapis.com/Execution` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions)  
Suspension  | `integrations.googleapis.com/Suspension` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions.suspensions)  
AuthConfig  | `integrations.googleapis.com/AuthConfig` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.authConfigs)  
  
## Examples of using IAM Condtions for Application Integration

#### Example 1: Limit access to any IntegrationVersion resource in a region 

You can use the following condition expression in the **Condition editor** to limit access to the `[IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions)` resource. Limiting access includes restricting `create`, `delete`, `download`, `get`, `list`, `patch`, `publish`, `unpublish`, and `upload` operations to the integration versions in the region.
    
    
    (resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME")) ||
    resource.type == "integrations.googleapis.com/Location" ||resource.type == "cloudresourcemanager.googleapis.com/Project"

Replace the following: 

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The integration location. See [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).
  * `INTEGRATION_NAME`: Name of the integration.



#### Example 2: Allow access to any IntegrationVersion resource in a region 

You can use the following condition expression in the **Condition editor** to allow access to the `[IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions)` resource:
    
    
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION/") ||
    resource.type == "integrations.googleapis.com/Location" ||
    resource.type == "cloudresourcemanager.googleapis.com/Project"

Replace the following: 

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The integration location. For supported locations, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
