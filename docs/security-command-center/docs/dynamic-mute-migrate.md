---
url: https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate/
title: Migrate from static to dynamic mute rules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:53.041687+00:00
---

# Migrate from static to dynamic mute rules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Migrate from static to dynamic mute rules Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to migrate your existing static mute rules to dynamic mute rules.

We recommend using dynamic mute rules exclusively in your mute rule configurations because they are more flexible than static mute rules. Compared to static mute rules, dynamic mute rules have three key benefits:

  * **Dynamic mute rules apply to existing and new findings**. Dynamic mute rules automatically mute both existing and new or updated findings that match your filter criteria.
  * **Dynamic mute rules offer an expiration option**. Dynamic mute rules also allow you to set a custom expiration period to temporarily match specific findings. If no expiration period is set, dynamic mute rules mute findings indefinitely until they no longer match the rule.
  * **Dynamic mute rules automatically unmute findings**. When any of the following occurs, Security Command Center automatically unmutes the finding:

    * The dynamic mute rule expires.
    * The properties of a finding change to no longer match your filter criteria.
    * The filter criteria change to no longer match the finding.



We don't recommend using static and dynamic mute rules simultaneously. Static mute rules override dynamic mute rules when they are applied to the same finding. As a result, dynamic mute rules won't work as intended, which can create confusion when managing your findings.

If you want to use dynamic mute rules exclusively, the following sections describe the permissions and steps necessary to migrate your static mute rules.

## Required roles

To get the permissions that you need to perform the dynamic mute migration process, ask your administrator to grant you the following IAM roles on your Google Cloud organization, folder, or project: 

  * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
  * [Security Center Settings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)
  * [Security Center Mute Configurations Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsViewer) (`roles/securitycenter.muteConfigsViewer`)
  * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
  * [Security Center Admin Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)
  * [Security Center Settings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)
  * [Security Center Mute Configurations Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)
  * [Security Center Findings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Migrate to dynamic mute rules

To use dynamic mute rules exclusively, complete the following steps to create dynamic mute rules and ensure existing muted findings remain muted after migration.

  1. **Create new dynamic mute rules**. You can't modify a mute rule's type after it has been created. Therefore, you must create one dynamic mute rule for each static mute rule you want to retain. Each new dynamic mute rule name must be unique from the existing mute rules. Security Command Center might take a few hours to apply the dynamic mute rules to the appropriate findings. For instructions on how to create a dynamic mute rule, see [Create a mute rule](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#create_a_mute_rule).
  2. **Validate the mute state of applicable findings**. To validate that the dynamic mute rules have been applied appropriately, you can use the `muteInfo` attribute in the Security Command Center API to list the applicable findings and inspect their mute fields. This helps you to determine whether the applicable findings are using dynamic or static mute rules.

For example, use `muteInfo.dynamicMuteRecords` in a query to list the applicable findings that are being muted by the new dynamic mute rule:
         
         contains(muteInfo.dynamicMuteRecords, muteConfig =
           "organizations/123/muteConfigs/my-dynamic-rule")
         

For more information about how to list findings, see [Listing security findings using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).

  3. **Delete all static mute rules**. Applicable future findings are covered by the new dynamic rules you created. Delete all your existing static mute rules to ensure they won't override the new dynamic mute rules for new findings. For instructions on how to delete a mute rule, see [Delete mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#delete-mute-rules). Deleting static mute rules does not change the static mute state of existing findings.

  4. **Reset the static mute state on all findings**. To reset the static mute state of existing findings in bulk, perform one of the following actions:

     * Use either the [`gcloud scc findings bulk-mute`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute) command or the `bulkMute` API method with the `muteState` attribute set to `UNDEFINED`. For the `--filter` flag or `filter` field, use a finding filter that matches the findings that were muted by the static mute rule you deleted.

The following example uses the `gcloud scc findings bulk-mute` command. If you deleted a static mute rule with the filter `category="OPEN_SSH_PORT"`, you can reset the mute state of findings that match that filter by running the following command:
           
           gcloud scc findings bulk-mute --organization=ORGANIZATION_ID --filter="category=\"OPEN_SSH_PORT\"" --mute-state=UNDEFINED
           

Replace `ORGANIZATION_ID` with the ID of your organization. You can replace `--organization` with `--project` or `--folder` depending on the scope of the findings you need to reset.

For more instructions on how to perform bulk mute operations, see [Mute or reset multiple existing findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#bulk_mute_findings).

     * If the bulk mute operation times out, clear the static mute state from all findings. Do so by updating your bulk mute filter to use less granular filters that cover all relevant findings.

Consider the following example of a filter in a static mute rule:
           
           filter: "category = \"OPEN_SSH_PORT\" AND (resource.parentDisplayName = \"organizations/123\" OR resource.parentDisplayName = \"folder/456\")"
           

To clear the mute state on all findings that match the criteria of this static mute rule filter, you can modify the filter by removing the additional conditions that follow the finding category. For this example, the result would be as follows:
           
           filter: "category = \"OPEN_SSH_PORT""
           

If you have manually set the mute state for any findings, this method might also reset the mute state of those findings.

For more information about updating a mute rule, see [Update mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#update-mute-rules).




If you need help migrating your static mute rules to dynamic mute rules, contact [support](https://docs.cloud.google.com/security-command-center/docs/getting-support).

## What's next

Learn more about [creating and managing mute rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
