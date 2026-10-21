---
url: https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption/
title: Modify data residency or data encryption configuration \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:58.490893+00:00
---

# Modify data residency or data encryption configuration  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Modify data residency or data encryption configuration Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

You can modify your organization's [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and [data encryption](https://docs.cloud.google.com/security-command-center/docs/cmek) configuration on the Standard and Premium tiers after you activate Security Command Center for your organization. Specifically, you can do the following:

  * Enable or disable data residency and change the data location.
  * Change the data encryption configuration to use Google-managed encryption keys or Cloud Key Management Service keys.
  * Change the Cloud KMS key.



## Limitations

The following limitations apply to this capability:

  * You can perform a data migration only once per week. If you plan to change the data location or data encryption multiple times, make the changes at least one week apart.

  * This feature is not supported if Security Command Center is [activated at the project level only](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project).

  * During data migration, `notificationConfigs` resources with the [v1 structure](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.notificationConfigs) are updated to the [v2 structure](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.notificationConfigs).

The [`source_properties`](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) field isn't supported with the v2 API. If needed, update export configurations for [Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) and [BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query).

For more information, see [Migrate to v2 of the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api#export-config).




## Before you begin

Before you change the configuration, complete the following:

  1. Plan for the change.
  2. Ensure you have the required roles.
  3. Create or locate the Cloud Key Management Service keys if you're changing the data location or keys.
  4. Prepare mute rules and export configurations if you're changing the data location.



### Plan for the change

If you're migrating from the default `global` data location, read [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) to learn how Security Command Center supports data residency.

If you plan to change the data encryption from Google-managed encryption keys to a Cloud KMS key, read [Enable CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek) to learn about using customer-managed encryption keys (CMEKs) with Security Command Center.

Plan the configuration change during a time when you aren't performing bulk exports. If you started a bulk export, wait until after that process completes.

After you change the configuration, the data migration process can take between 4 hours and 24 hours, depending on the volume of findings. During this time, Security Command Center and [enabled built-in detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) are temporarily paused:

  * Security Command Center doesn't generate or update findings. Findings sent to Security Command Center from integrated or third-party services aren't received.
  * Data exports from Security Command Center to other resources are paused.
  * Security Command Center pages in the console aren't accessible.
  * The following Security Command Center APIs are unavailable:

    * `securitycenter.googleapis.com`
    * `securitycentermanagement.googleapis.com`

If an API method is called during migration, it returns a `FAILED_PRECONDITION` error with the message `API access is temporarily unavailable due to an ongoing data migration`.




When the migration is complete, Security Command Center and built-in services restart automatically.

If Security Command Center integrates with other products, expect these connections to be disrupted during the migration.

When you change the data residency configuration, specific fields are updated with the new location identifier (for example from `global` to `us`). This affects the following resources:

  * Findings: `name` and `canonicalNames` values.
  * Mute rules: `name` value in the [`MuteConfig`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.muteConfigs).



Plan to update finding search queries, external systems, and scripts that depend on these field values.

If your organization is enrolled in the data residency Preview program and you're updating the configuration for the first time, see Considerations when updating the Preview configuration for additional information.

### Required roles

To get the permissions that you need to migrate Security Command Center data location or data encryption, ask your administrator to grant you the [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create or locate the Cloud Key Management Service keys

Create a key project and Cloud Key Management Service keys if either of the following applies:

  * You plan to change the Cloud Key Management Service keys.

  * You plan to change the data residency configuration while using Cloud Key Management Service keys. In this case, you must select the Cloud Key Management Service keys again.




For more information, see [Enable CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek).

### Prepare mute rules and export configurations

If you plan to change the data location, update the following configurations that depend on field values with a location identifier:

  * Finding mute rules
  * Pub/Sub continuous exports



Change the field values to use the new location identifier (for example, from `global` to `us`).

### Considerations when updating the Preview configuration

**Important:** The following information applies only to organizations that are enrolled in the Preview program and are updating the data residency configuration for the first time.

The first time you use this feature, you must update the data residency configuration to the General Availability configuration. You can't use the feature for the first time to change data encryption only, without updating the data residency configuration.

During the update, data is migrated from a multi-region configuration to the single location that you select.

After data is migrated, you might see the following:

  * Dashboard panes that present data over time might show incorrect aggregate measures for dates before the migration. Some data might not have been mapped and merged to the single location.

  * If the migration process identifies a duplicate finding when merging data across regions, it migrates only the finding version with the most recent `eventTime`.




## Change the configuration and start the migration

You can use either the global or jurisdictional Google Cloud console to change the data residency or data encryption configuration. Keep the following in mind when choosing a console:

  * **Selecting the CMEK key** : The **Cloud KMS** key menu displays only keys that are in the same jurisdiction as the console. If you use the `global` console, the menu displays all keys.
  * **Getting notifications** : Google Cloud console notifications notifications appear for only the user who started the data residency migration and only in the same console used to configure the settings (either global or jurisdictional).



You can change the data residency configuration, the data encryption configuration, or both.

  1. In the Google Cloud console, go to the **Settings > Setup details**.

[Go to Setup details](https://console.cloud.google.com/projectselector2/security/command-center/config/integrated-services?supportedpurview=organizationId)

  2. Select the organization where Security Command Center is activated.

  3. Click **Manage data residency and encryption**.

  4. Under **Manage data residency** , enable or disable data residency. If you enable data residency, select the **Data location**. If you don't change the existing selection, the data migration process doesn't change the location identifiers in finding and resource field values.

**Caution:** Security Command Center doesn't validate your data residency location against any organization policies that enforce the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), `gcp.resourceLocations`. When you configure data residency, you must select a location that's consistent with your organization policies. 
  5. Click **Continue**.

  6. Under **Manage data encryption** , select the **Encryption** configuration.

     * Select **Google-managed encryption key** or **Cloud KMS** key.
     * If you select **Cloud KMS** key, do the following:

       * Click **Browse** to select the project where the keys are stored.
       * Select the **customer-managed key**.

If the organization uses Cloud KMS keys and you changed the data residency configuration, you must re-select the key project and Cloud Key Management Service key.

  7. Review the changes, and then click **Start migration**. Click **Cancel** to return and change the selections.

  8. In the **Start data migration** dialog, confirm by entering the organization ID, and then clicking **Confirm data migration**.

  9. The data migration status page appears, indicating that the migration is in progress.

Security Command Center pages aren't accessible while data migration is in progress. If you attempt to access Security Command Center during migration, you'll see the migration status page.

  10. When the migration is complete, the status page displays a link to open the console in the newly configured location.




## Verify capabilities after the data migration

After the migration completes, ensure that Security Command Center, related services, and integrations work as expected.

  * Verify that Security Command Center is available and previously enabled services are enabled.

  * Review and verify that data export configurations specify the correct resources:

    * BigQuery export configurations specify the correct dataset. See [Streaming BigQuery exports](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query).

    * Pub/Sub export configurations define the correct topic. See [Finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

**Important:** If you change the data location and export findings to other systems, you'll see duplicate findings because findings were changed during the migration to include the updated location identifier.
  * If you changed the data residency configuration, update the following:

    * [Mute rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings): update rules that depend on the finding `name` or `canonicalName`.

    * Update filters and finding queries that depend on finding `name` or `canonicalName` to specify the new location.

    * Verify that finding queries work as expected.

  * Verify that integrations with other Google Cloud services, such as Cloud Hub, Application Design Center, GKE security posture dashboard, or Google SecOps data ingestion are working as expected.




## What's next

  * Learn about [Regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints).
  * Learn about [Notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).
  * Learn about [Exporting data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
