---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-export-data/
title: Overview of exporting Security Command Center data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:23.689255+00:00
---

# Overview of exporting Security Command Center data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-export-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of exporting Security Command Center data Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes two methods for exporting Security Command Center data using the Google Cloud console:

  * One-time exports for existing findings, assets, and security marks
  * Continuous exports that automatically export new findings to Pub/Sub



Exportable Security Command Center data includes assets, findings, and security marks.

You can also export findings to [BigQuery](https://docs.cloud.google.com/bigquery/docs) or [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). For more information, see the following resources:

  * [Stream findings to BigQuery for analysis](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query)
  * [Bulk export findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query)
  * [Export logs to Logging](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging)



**Note:** We don't recommend using API list calls for programmatic data exports. Because API list calls return up to 1,000 findings per call and require pagination, they are inefficient for large data exports. In enterprise-scale environments with millions of findings, use [Bulk export findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query) for compliance reporting, historical trend analysis, and custom dashboards.

## One-time exports

One-time exports let you manually transfer and download current and historical findings and assets.

For findings, you can use the Google Cloud console to transfer data in JSON, JSONL, or CSV format to a [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) bucket. You can also download a limited number of findings to your workstation in CSV format.

For assets, you can download the data from the console to your local workstation as a CSV file.

### Before you begin

Before you initiate a one-time export, you must obtain specific Identity and Access Management (IAM) roles and permissions and familiarize yourself with data residency limitations.

#### Required roles

To get the permissions that you need to perform one-time exports, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you want to export data from: 

  * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
  * Export findings to a Cloud Storage bucket: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform one-time exports. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform one-time exports:

  * `securitycenter.assets.group`
  * `securitycenter.assets.list`
  * `securitycenter.findings.group`
  * `securitycenter.findings.list`
  * `securitycenter.sources.get`
  * `securitycenter.sources.list`
  * `securitycenter.userinterfacemetadata.get`
  * Perform exports for organization-level activations: `resourcemanager.organizations.get`
  * Perform exports for project-level activations: `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

#### Data residency limitations for one-time exports

You cannot include any of your data that is subject to data residency control in the filter of a one-time export to Cloud Storage.

If you specify a property that contains controlled data in the finding filter, Security Command Center returns an error message when you attempt the export.

### Export data using the Google Cloud console

Using the Google Cloud console, you can do the following:

  * Export findings to a Cloud Storage bucket
  * Export findings to a CSV file
  * Export assets to a CSV file



#### Export findings to a Cloud Storage bucket

This section describes how to export Security Command Center data to a Cloud Storage bucket. When you click **Export** on the **Findings** page in the Google Cloud console, Security Command Center automatically gets credentials or permissions to write to the Cloud Storage bucket.

You can export a JSON file, a JSONL file, or a CSV file to an existing Cloud Storage bucket or create a bucket during the export process. You can export all current findings, or select the filters you want to use before you export.

**Note:** You can't export findings to a Cloud Storage bucket that has a [retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) set.

  1. In the Google Cloud console, go to the Security Command Center **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select a project, folder, or organization.

  3. Select the findings that you need to export by applying filters to the findings query. For more information about creating filters, see [Find and view specific findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query).

  4. When you're done creating a filter, click **Export** , and then, under **One-time** , click **Cloud storage**.

  5. On the **Export** page, configure the export:

     1. In the **Export to** section, specify the following fields: 
        1. In the **Project name** field, specify the project that contains the Cloud Storage bucket.
        2. In the **Export path** field, which only appears after you specify a project, click **Browse**.
        3. On the **Select object** panel, select an existing Cloud Storage bucket or [create a storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
        4. After you select or create a bucket, under **Filename** , enter a name for the export file.
        5. Click **Select**.
     2. In the **Export criteria** section, specify the following fields: 
        1. Click **Group results by** , and select how you want to group the export data.
        2. Click in the **Format** field and select **JSON** , **JSONL** , or **CSV**.
        3. Click in the **Time range** field and select the time period from which to export findings.
     3. In the **Findings query** section, confirm the query appears as you expect.
     4. Below the query, confirm that the number and type of matching findings are what you expect.
     5. Click **Export**.

If you selected an existing file in the bucket, the **Confirm Overwrite** dialog displays.

     * To overwrite the existing file, click **Confirm**.
     * To change the file you're writing to, click **Cancel** , then click **Browse** in the **Export path** box and select or create a different file.



The configured data is saved to the Cloud Storage bucket that you specified.

##### Download exported data from a Cloud Storage bucket

To download the exported JSON, JSONL, or CSV data, perform the following steps:

  1. Go to the **Storage browser** page in the Google Cloud console.

[Go to Storage browser](https://console.cloud.google.com/storage/browser)

  2. Select your project, and then click the bucket to which you exported data.

  3. Select the checkbox next to the export file, and then click **Download**.

  4. On the **Save File** dialog, select the location where you want to save the file, and then click **Save**.




The JSON, JSONL, or CSV file is downloaded to the location that you specified.

#### Export findings to a CSV file

To configure the export, you can filter findings by category, severity, and other properties. All findings that match the filter are included in the CSV file.

You can download up to 1,000 findings directly to your workstation. If the number of findings exceeds 1,000, you are prompted to refine your query to get fewer results. Alternatively, you can export the data to a Cloud Storage bucket.

**Note:** The system exports finding records with a default set of columns, which might not match what you see in the console. That is, hiding or displaying columns doesn't change which columns are exported. Similarly, changing the number of rows displayed per page—which you can do in the Google Cloud console—has no effect on the exported content.

To download finding data to a CSV file, follow these steps:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select a project, folder, or organization.

  3. Optional: To refine the selection of findings that you want to export, [Find and view specific findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query).

  4. Click **Export > CSV**. The CSV file is downloaded to your local workstation.




#### Export assets to a CSV file

You can download asset data to a CSV file from the **Assets** page in the Google Cloud console.

To download asset data to a CSV file, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Select a project, folder, or organization.

  3. Optional: Use the **Quick filters** panel or the **Filter** field of the asset results panel to select the assets you need to export. For more information about filtering assets, see [Filter assets](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#filter-assets).

  4. Click **Export > Download CSV**. The data for the assets in the results panel are downloaded to your workstation.




## Continuous exports

Continuous exports simplify the process of automatically exporting Security Command Center findings into Pub/Sub. When new findings are written, they are automatically exported to designated Pub/Sub topics in near real time, letting you integrate them into your existing workflow.

To learn more about Pub/Sub, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview).

### Before you begin

Before you initiate a continuous export, you must obtain specific IAM roles and permissions and familiarize yourself with both data residency limitations and Pub/Sub compatibility.

#### Required roles

To get the permissions that you need to create and manage continuous exports, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you want to export data from: 

  * View continuous exports: [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) 
  * View, create, and manage continuous exports: [Security Center Admin Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage continuous exports. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage continuous exports:

  * View or publish Pub/Sub topics: 
    * `pubsub.topics.publish`
    * `pubsub.topics.list`
  * View the continuous exports page: 
    * `securitycenter.notificationconfig.get`
    * `securitycenter.notificationconfig.list`
  * Manage continuous exports: 
    * `securitycenter.notificationconfig.create`
    * `securitycenter.notificationconfig.update`
    * `securitycenter.notificationconfig.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

#### Data residency and continuous exports

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for Security Command Center, the configurations that define continuous exports to Pub/Sub—`notificationConfig` resources—are subject to data residency control and are stored in a [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) that you select.

To export findings in a Security Command Center location to Pub/Sub, you must configure the continuous export in the same Security Command Center location as the findings.

Because the filters that are used in continuous exports can contain data that is subject to residency controls, make sure you specify the correct location before you create them. Security Command Center does not restrict which location you create exports in.

Continuous exports are stored only in the location in which they are created and cannot be viewed or edited in other locations.

After you create a continuous export, you can't change its location. To change the location, you need to delete the continuous export and recreate it in the new location.

To learn how to use Security Command Center when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints). 

#### Compatibility with Pub/Sub message storage policies

Pub/Sub lets you set a message storage policy. This policy ensures that Pub/Sub stores and processes messages only in the set of Google Cloud regions that you specify, regardless of where the publish or subscribe requests originate.

However, continuous exports are incompatible with the `enforceInTransit` option of message storage policies. When you configure continuous exports, don't choose a Pub/Sub topic that has a message storage policy with `enforceInTransit` enabled; such a topic might not receive finding notifications from Security Command Center.

For more information, see [Message storage policy overview](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#message_storage_policy_overview).

### Create a continuous export to Pub/Sub

Continuous exports let you automate the export of all _future_ findings to Pub/Sub or create filters to export future findings that meet specific criteria. You can filter findings by category, source, asset type, security marks, severity, state, and other variables.

Your organization can create a maximum of 500 continuous exports.

To create an export for Pub/Sub, do the following:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select a project, folder, or organization.

  3. In the **Findings query results** field, select the findings to export by using either of the following methods:

     * By clicking **Add Filter** to select the properties of the findings you need to export.

The **Add filter** menu lets you choose supported finding attributes and values.

       1. In the **Select filter** menu, select a finding attribute or type its name in the **Search finding attributes** box. A list of the available sub-attributes displays.
       2. Select a sub-attribute. A selection field displays where you can build the query statement using the sub-attribute you selected, a query operator, and one or more values for the sub-attribute. 
       3. Select the operator and one or more values for the sub-attribute from the panel. For more information about query operators and functions that they use, see [Query operators in the **Add filters** menu](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#query_operators_in_the_add_filters_menu).

If you want to start over, click **Reset**.

       4. Click **Apply**.

The menu closes and your query is updated.

       5. Repeat until the findings query contains all the attributes you want.
     * By manually coding the finding query in the query editor. You can use standard SQL operators `AND`,`OR`, equals (`=`), has (`:`), and not (`-`) to specify the finding properties and values of the findings you need to export.

As you type in your query, an autocomplete menu appears, where you can select filter names and functions.

For example, the following query mutes low-severity and medium-severity `anomalous IAM grant` findings in `prod-project`, and excludes resource types where the name has the substring `compute`:
           
           severity="LOW" OR severity="MEDIUM" AND category="Persistence:
           IAM Anomalous Grant" AND resource.project_display_name="prod-project"
           AND -resource.type:"compute"

For more examples on filtering findings, see [Filtering notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).

  4. Review the resulting query for accuracy. To make changes, delete or add properties and filter values as needed.

  5. Click **Refresh matching findings**. A table displays findings that match your query. For more information about querying findings, see [Edit a findings query in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).

  6. Click **Export** , and then, under **Continuous** , click **Pub/Sub**.

  7. Review your filter to ensure it's correct and, if necessary, return to the **Findings** page to modify it.

  8. Under **Continuous export name** , enter a name for the export.

  9. Under **Continuous export description** , enter a description for the export.

  10. Under **Export to** , select a project for your export. You can't create a project on this page. To create a new project, see [Creating a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

  11. Under **Pub/Sub topic** , select the topic where you want to export findings. To create a topic, do the following:

     1. Select **Create a topic**.
     2. Enter a **Topic ID** , and then select other options as needed:

        1. Learn about [Creating and managing schemas](https://docs.cloud.google.com/pubsub/docs/schemas).
        2. Learn about [using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek) with Pub/Sub.
     3. Click **Create Topic**.

  12. Optional: To receive notifications when findings are deleted from Security Command Center due to data retention policies, select the **Receive retention deletion notifications** checkbox.

  13. Click **Save**. You see a confirmation and are returned to the findings page.

  14. Follow the guide to [create a subscription](https://docs.cloud.google.com/pubsub/docs/admin#creating_subscriptions) for your Pub/Sub topic.




The Pub/Sub export configuration is complete. To publish notifications, a service account is created for you in the form of `service-org-ORGANIZATION_ID@gcp-sa-scc-notification.iam.gserviceaccount.com`. This service account is automatically granted the `roles/securitycenter.notificationServiceAgent` role at the **organization** level. This service account role is required for notifications to function.

#### Test continuous exports

To confirm that an export is working, perform the following steps to toggle findings between active and inactive states.

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Click **Edit query**. The **Query editor** opens.

  3. Edit the query so that both so that both active and inactive findings are displayed. The following query omits the `state` property to display all findings except those that are muted:
         
         NOT mute="MUTED"

     1. If necessary, use the **Query editor** to re-enter filter variables that match the export filter you're testing.
     2. Select a finding and then click **Change Active State > Inactive**.
     3. Select the finding again that you marked inactive, click **Change Active State > Active**. A notification is sent for the newly active finding.
     4. Go to the Pub/Sub page in the Google Cloud console.

[Go to Pub/Sub](https://console.cloud.google.com/cloudpubsub)

     1. In the list of topics, click the name of your topic.
     2. Go to the **Messages** tab and select your subscription from the list to see the finding notification.
     3. Optional: Click **Pull** to refresh messages.



### Manage continuous exports

To view, edit, or delete exports, do the following:

  1. In the Google Cloud console, go to the Security Command Center **Settings** page.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/)

  2. Select a project, folder, or organization.

  3. Select **Continuous exports**. You see a list of continuous exports for your project, folder, or organization.




On the **Continuous exports** page in **Settings** , you can create, view, edit, and delete continuous exports.

#### View related findings

To see findings that match an export filter, do the following:

On the **Continuous exports** page, next to the name of an export, select **More** more_vert, and then click **View related filters**.

The **Findings** page loads with findings that match the export filter.

#### Edit continuous exports

  1. On the **Continuous exports** page, click the name of the export you want to view or modify, or click **More** more_vert.
  2. Select **Edit**.
  3. Enter a new description, change the project that exports are saved to, enter a new Pub/Sub topic, or select or clear the **Receive retention deletion notifications** checkbox.
  4. When done, click **Save**.

**Note:** Enabling or disabling the **Receive retention deletion notifications** option on an existing export configuration applies only to future deletion events. Findings that were deleted prior to enabling the option don't retroactively export deletion notifications. You can't change the name of an export or modify an export filter. To use a different name or filter, you must create a new export.

#### Delete continuous exports

  1. On the **Continuous exports** page, click the name of the export you want to delete.
  2. Click _delete_ **Delete**.
  3. In the dialog, click **Delete**. The export is deleted.



## What's next

  * Learn more about [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).
  * Learn how to [enable real-time chat notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
