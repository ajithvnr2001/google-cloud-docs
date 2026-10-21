---
url: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set/
title: Define and manage your high-value resource set \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:04.510149+00:00
---

# Define and manage your high-value resource set  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Define and manage your high-value resource set Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows you how to create, edit, delete, and view resource value configurations.

Use resource value configurations to create your high-value resource set. Your high-value resource set determines which of your resource instances (referred to as _resources_) the attack path simulations consider _high-value resources_.

You can define resource value configurations for the resources on Google Cloud. Also, in the Enterprise (Deprecated) service tier, you can define configurations for resources on the other cloud service providers that Security Command Center is connected to.

When attack path simulations run, they identify attack paths and calculate attack exposure scores for resources that are designated as high-value resources and for `Vulnerability` class, `Misconfiguration` class, and `Toxic combination` class findings.

Attack path simulations run on a schedule, and new results are available up to every 48 hours. Simulation runs aren't triggered by the creation, modification, or deletion of resources or resource value configurations.

For an introduction to high-value resource sets and resource value configurations, see [High-value resource sets](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value-resource-sets).

## Before you begin

To get the permissions that you need to view and work with resource value configurations, ask your administrator to grant you the following IAM roles on your organization: 

  * [Resource value config editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigEditor) (`roles/securitycenter.resourceValueConfigEditor`)
  * [Resource value config viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsViewer) (`roles/securitycenter.resourceValueConfigsViewer`)
  * [Security Center Settings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a resource value configuration

You create resource value configurations by using the **Attack path simulation** tab on the Security Command Center **Settings** page in the Google Cloud console.

To create a resource value configuration, click the tab for your cloud service provider and follow the steps:

### Google Cloud

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens.

  3. Click **Create new configuration**. The **Create resource value configuration** panel opens.

  4. In the **Name** field, specify a name for this resource value configuration.

  5. Optional: Enter a description of the configuration.

  6. Under **Cloud provider** , select **Google Cloud**.

  7. In the **Select scope** field, click **Select** and use the project browser to select a project, folder, or the organization. This configuration applies only to resource instances in the specified scope.

  8. Click the **Select resource type** field, and then select a resource type or **Any**. The configuration applies to instances of the selected resource type or, if you select **Any** , to instances of [all supported resource types](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#supported-high-value-resource-types). **Any** is the default.

**Note:** If you select **Any** and enable the **Include discovery insights from Sensitive Data Protection** option, then for all [supported resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-by-data-sensitivity-resource-types), the system automatically sets resource values based on data sensitivity classifications from Sensitive Data Protection.
  9. Optional: In the **Label** section, click **Add label** to specify one or more labels. When a label is specified, the configuration only applies to resources that include the label in their metadata.

If you apply a new label to any resources, it can take several hours before the label is available for matching by a configuration.

  10. Optional: In the **Tag** section, click **Add tag** to specify one or more tags. When a tag is specified, the configuration only applies to resources that include the tag in their metadata.

If you define a new tag for a resource, it can take several hours before the tag is available for matching by a configuration.

  11. Set the [priority value](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values) for the matching resources by specifying one of the following options:

     * Optional: If you use the [Sensitive Data Protection discovery service](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), enable Security Command Center to automatically set the priority value of [supported data resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#resource_types_supported_with_data-sensitivity_classifications) based on data-sensitivity classifications from Sensitive Data Protection:

       1. Click the slider next to **Include discovery insights from Sensitive Data Protection**.
       2. In the first **Assign resource value** field, select the priority value to assign to matching resources that contain high-sensitivity data.
       3. In the second **Assign resource value** field, select the priority value to assign to matching resources that contain medium-sensitivity data.
     * In the **Assign resource value** field, select a value to assign to the resource instances. This value is relative to the other resource instances in your high-value resource set. The value is used during the calculation of attack exposure scores.

  12. Click **Save**.




### AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Before Security Command Center can generate attack exposure scores and attack paths for the resources that you specify in a resource value configuration, Security Command Center must be connected to AWS. For more information, see [Multicloud support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#aps-multicloud).

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens.

  3. Click **Create new configuration**. The **Create resource value configuration** panel opens.

  4. In the **Name** field, specify a name for this resource value configuration.

  5. Optional: Enter a description of the configuration.

  6. Under **Cloud provider** , select **Amazon Web Services**.

  7. Optional: In the **Account ID** field, enter a 12-digit AWS account ID. If unspecified, the resource value configuration applies to all AWS accounts that are specified in the [AWS connection configuration](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

  8. Optional: In the **Region** field, enter an AWS region. For example, `us-east-1`. If unspecified, the resource value configuration applies to all AWS regions.

  9. Click the **Select resource type** field, then select a resource type or **Any**. The configuration applies to instances of the selected resource type or, if you select **Any** , to [all supported resource types](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#aps-support-for-aws-resources). **Any** is the default.

**Note:** If you select **Any** and enable the **Include discovery insights from Sensitive Data Protection** option, then for all [supported AWS resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-by-data-sensitivity-aws-resource-types), the system automatically sets resource values based on data sensitivity classifications from Sensitive Data Protection.
  10. Optional: In the **Tag** section, click **Add tag** to specify one or more tags. When you define a tag, the connector scans only resources that include the tag in their metadata.

If you define a new tag for a resource, it can take several hours before the tag is available for matching by a configuration.

  11. In the **Assign resource value** field, select a [priority value](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values) for the matching resources by specifying one of the following options:

     * Optional: If you use the [Sensitive Data Protection discovery service](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), enable Security Command Center to automatically set the priority value of [supported AWS data resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#aws-data-sensitivity-classifications) based on data-sensitivity classifications from Sensitive Data Protection:

       1. Click the slider next to **Include discovery insights from Sensitive Data Protection**.
       2. In the first **Assign resource value** field, select the priority value to assign to matching resources that contain high-sensitivity data.
       3. In the second **Assign resource value** field, select the priority value to assign to matching resources that contain medium-sensitivity data.
     * In the **Assign resource value** field, select a value to assign to the resource instances. This value is relative to other resource instances in your high-value resource set. The value is used during the calculation of attack exposure scores.

  12. Click **Save**.




### Azure

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Before Security Command Center can generate attack exposure scores and attack paths for the Azure resources that you specify in a resource value configuration, Security Command Center must be connected to Azure. For more information, see [Multicloud support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#aps-multicloud).

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens.

  3. Click **Create new configuration**. The **Create resource value configuration** panel opens.

  4. In the **Name** field, specify a name for this resource value configuration.

  5. Optional: For **Description** , enter a description of the configuration.

  6. Under **Cloud provider** , select **Microsoft Azure**.

  7. Optional: In **Subscription ID** , enter a 36-digit Azure subscription ID. If unspecified, the resource value configuration applies to all subscriptions that are specified in the Azure [connector configuration](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure).

  8. Optional: In the **Select location** field, select an Azure location—for example, `East US 2`. If you don't set a location, the resource value configuration applies to all locations that are specified in the Azure connector configuration.

  9. Click **Select resource type** , and then select a resource type or **Any**. The configuration applies to instances of the selected resource type or, if you select **Any** , to [all supported resource types](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#azure-resource). **Any** is the default.

  10. Optional: In the **Tag** section, click **Add tag** to specify one or more tags. When a tag is specified, the configuration only applies to resources that include the tag in their metadata.

If you define a new tag for a resource, it can take several hours before the tag is available for matching by a configuration.

  11. In the **Assign resource value** field, select a [priority value](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values).

  12. Click **Save**.




The new configuration is reflected in the attack exposure scores and attack paths only after the next attack path simulation runs.

When you view the high-value resource set, you can see the resource value configurations that match the resources in the set. For more information, see View the configurations that match a high-value resource.

For information about how to configure Sensitive Data Protection to send data sensitivity classifications to Security Command Center, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc) in the Sensitive Data Protection documentation.

## Edit a configuration

Except for the name, you can update any specification in a resource value configuration.

These steps assume that you know the name of the resource value configuration that you want to edit. If you know only the name of the relevant resource, see View the configurations that match a high-value resource instead.

To update an existing resource value configuration, follow these steps:

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens with the existing configurations displayed.

  3. In the **Configuration name** column, click the name of the configuration that you need to update. The **Edit resource value configuration** page opens.

  4. Update the specifications in the configuration as needed.

  5. Click **Save**.




The changes are reflected in the attack exposure scores and attack paths only after the next attack path simulation runs.

## Delete a configuration

To delete a resource value configuration, follow these steps:

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens.

  3. Under **Resource value configurations** on the right side of the row for the configuration you need to delete, display the actions menu by clicking the vertical dots. If you don't see the vertical dots, scroll to the right.

  4. From the displayed action menu, select **Delete**.

  5. In the confirmation dialog, select **Confirm**.

The configuration is deleted.




## View a configuration

You can view all existing resource value configurations on the **Attack path simulation** page in Security Command Center **Settings**.

  1. To view a particular resource value configuration, go to the **Attack path simulation** page:

[Go to Attack path simulations](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens.

  3. Under **Resource value configurations** on the **Attack path simulation** page, scroll the list of resource value configurations until you find the configuration that you need.

  4. To see the configuration properties, click the name of the configuration. The properties are displayed on the **Edit resource value configuration** page.




## View the configurations that match a high-value resource

You can view all the configurations that match the resources that are in the high-value resource set. This feature is useful if you want to review the rules that determined the resource values of your high-value resource set.

To view the configurations that match a high-value resource, follow these steps:

  1. [View the high-value resource set](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#hvr).
  2. Find the resource whose configurations you want to view. The matching configurations for that resource are listed in the **Matching configurations** column. The configurations are listed in descending order based on the resource value that they assign to the resource—`High`, `Medium`, or `Low`.
  3. To see the properties of a configuration, click its name. The properties are displayed on the **Edit resource value configuration** page.

A configuration that was recently deleted remains visible—but not clickable—until the next attack path simulation runs.

  4. Optional: Edit the configuration and click **Save**.




## Troubleshooting

If you receive errors after creating, editing, or deleting resource value configurations, check for `SCC Error` class findings in the Google Cloud console by following these steps:

  1. Go to the **Findings** page in the Google Cloud console:

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. In the **Quick filters** panel, go to the **Finding class** section and select **SCC Error**.

  3. In the **Findings query results** panel, scan the findings for the following `SCC Error` findings and click on the category name:

     * `APS no resource value configs match any resources`
     * `APS resource value assignment limit exceeded`

The finding details panel opens.

  4. In the finding details panel, review the information in the **Next steps** section.




To review the remediation instructions for the attack path simulation `SCC Error` findings in the documentation, see:

  * [APS no resource value configs match any resources](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#aps_no_rvcs_match_resources)
  * [APS resource value assignment limit exceeded](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#aps_value_assignment_limit_exceeded)



## What's next

For information about working with Security Command Center findings, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
