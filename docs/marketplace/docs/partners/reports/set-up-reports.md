---
url: https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports/
title: Set up to receive reports \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:30.479118+00:00
---

# Set up to receive reports  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Set up to receive reports Stay organized with collections  Save and categorize content based on your preferences. 

You can receive Cloud Marketplace reports as a queryable BigQuery table, a CSV file, or a Google Sheet. For BigQuery table setup, see Reports in BigQuery.

To receive your Cloud Marketplace reports in CSV format, set up a Google Drive folder, a Cloud Storage bucket, or both. You must be able to adjust the access for the destination you choose. For example, if you use a Drive folder, your Google Cloud account must be either an **Owner** or **Editor** for the folder. If you are an Editor for the folder, then the Owner must not have restricted the folder so only they can adjust the access. If they have restricted the folder, then the Owner will have to set that folder as a destination, or remove the restriction. If your organization restricts who can be added to Google Drive locations or Cloud Storage buckets, your Google Workspace or Cloud Storage administrator must ensure that the destinations can be shared with the `google.com` and `system.gserviceaccount.com` domains.

**Note:** We don't support shared Google Drive locations. If you need to store your reports in a Google Drive location, use a folder located in the top level of your Google Drive.

  * [Learn about sharing permissions for Google Drive](https://support.google.com/drive/answer/2494822).
  * [Learn about restricting access to Google Cloud resources by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).



When you add your report destination, the following accounts are added as editors or storage object administrators, as applicable:

  * The `cloud-marketplace-stats@system.gserviceaccount.com` service account, which uploads reports to the bucket.
  * The `gcp-marketplace-business-operations@google.com` Google group, to debug and troubleshoot issues that you might have with reports.



If you're setting up a Cloud Storage bucket, we recommend that you [use access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) for the bucket. We also recommend that you [remove any retention policies](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) that you might have on the bucket, because the retention policy might prevent reports from being updated until the retention period has passed.

If you use Uniform Bucket Level Access, note that the following organization policies might interfere with access:

  * [Domain Restricted Sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) prevents adding either of these principals into IAM for the bucket's project,
  * [Cross Project Service Account](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts) prevents adding the service account.



To remove these organization policies for your bucket, for the folder or project that holds your bucket, request that your organization policy administrator set the policy to the Google default handling. You can also work around one or both policies by creating an internal group, adding the principals to that group, and then giving that group the required permissions.

**Note:** If your domain administrator has restricted group membership to exclude external members, they might be able to remove that restriction for this new group by using the [following instructions](https://support.google.com/a/answer/11192679).

After you set up a location to store the reports, you must set up how they are delivered.

To set up delivery, use the following steps:

  1. In Producer Portal, open the **Reports** page. The direct link to the page is:
         
         https://console.cloud.google.com/producer-portal/partner-report?project=YOUR_PUBLIC_PROJECT_ID
         

Your public project ID is the ID of the project that hosts the components of your product. You create this project [when you sign up to become a partner](https://docs.cloud.google.com/marketplace/docs/partners/get-started#list-solution).

  2. To add a report destination, click **Add destination** in CSV Export tab.

  3. Under **Destination location** , select whether you want to send reports to a Google Drive folder or a Cloud Storage bucket.

  4. Click **Browse** and select a folder or bucket, as applicable.

  5. Select the report(s) to save in that destination. You can send each report to as many destinations as you need.

  6. If you want additional levels of detail in usage reports, under **Usage report options** , select one or more of these options:

     * **Separate customer usage by location** : Splits your usage and disbursement report by the customers' locations.
     * **Separate customer usage by billing account** : Splits your usage and disbursement report by the customers' Cloud Billing accounts.

For information on what is included in the report, see [Charges and usage reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-charges-usage).

  7. If you want to set up more destinations, repeat these steps.

  8. Optionally, add one or more Cloud Billing accounts to use for testing. To learn about product testing, visit [Testing your published Google Cloud Marketplace products](https://docs.cloud.google.com/marketplace/docs/partners/testing-products).

  9. To save your changes, click **Save**. You must agree to give the Cloud Marketplace accounts access to your report destinations.




## Reports in BigQuery

To receive your Cloud Marketplace reports in BigQuery, follow these steps:

  1. In the Producer Portal **Reports** page, navigate to the **BigQuery Export** tab.

  2. Click **Enable Export**.

  3. If the BigQuery API is not already enabled in your project, a warning message appears. Click **Enable** and wait a few minutes for the change to take effect. Then, click **Enable Export** again.

  4. After you enable the export, allow up to 24 hours for the data to populate. A [linked dataset](https://cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) is created in your project, which you can use to access and analyze your data.




When you enable the BigQuery export, the following reports are available:

  * **Incremental daily insights** : Daily reports on usage.
  * **Incremental monthly insights** : Monthly reports on usage, generated once a month.
  * **Detailed disbursement report** : Financial reconciliation data, generated once a month.



### Costs incurred by partners

Google Cloud Marketplace partners won't incur any BigQuery storage costs as part of enabling this feature for their Producer Portal projects. However, appropriate BigQuery costs will be incurred for any queries on the data such as SQL queries, user-defined functions, scripts, and certain data manipulation language (DML) and data definition language (DDL) statements. Learn more about [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

### BigQuery data retention policy

Once enabled, the system backfills historical data for approximately the last two years. The data retention period for these reports is five years.

### Troubleshooting

If the linked dataset is accidentally deleted, you can recover it by disabling and then re-enabling the export from the **BigQuery Export** tab.

If you see an error message such as `US violates constraint constraints/gcp.resourceLocations on the resource projects/YOUR_PROJECT_ID/datasets/marketplace_report`, your organization has an organization policy constraint that prevents creation of BigQuery datasets in the `US` multi-region. Because BigQuery reports are stored in the `US` multi-region, you must update the location constraint to allow BigQuery datasets to be created in the `US` multi-region. For more information, see [Restricting Resource Locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

## Set up notifications for your reports

To ensure that you receive timely updates from the Google Cloud Marketplace team, we recommend that you set up notifications for your Cloud Marketplace reports. This can help you get your reports as quickly as possible if any of the following occur:

  * Delayed reports.
  * Reports with incomplete or inaccurate data.
  * Reports that had to be regenerated.



To set up notifications for your Cloud Marketplace reports, complete the following steps:

  1. Turn on the [Essential Contacts API](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

  2. In Essential Contacts, add the individuals or groups that you want to receive reporting notifications to the Cloud Billing category.


**Note:** When you set up your organization's essential contacts, you can assign individuals, groups, or a mixture of both individuals and groups as contacts. To ensure that your notifications only go to active employees, and to reduce the impact of personnel changes, we recommend that you assign groups as your organization's contacts, and then control who gets notifications by managing the membership of those groups.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
