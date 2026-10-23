---
url: https://docs.cloud.google.com/application-integration/docs/manage-custom-connector-versions/
title: Manage custom connector version \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:29.918662+00:00
---

# Manage custom connector version  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/manage-custom-connector-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage custom connector version

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Create a custom connector version

To create a custom connector version, follow these steps:

  1. In the [Console](https://console.cloud.google.com/), go to the **Application Integration > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/integrations/custom-connectors)

This displays the list of custom connectors.

  2. Click the custom connector for which you want to add a version. 

The displays the connection details page.

  3. Click **Versions**. 

The page displays all the versions of the connector.

  4. Click **Create**. This displays the **Create new version** page with the new version number. The steps to create a new version are similar to that of creating a new custom connector. It means that you can create a version with direct or indirect connectivity. 
     * For creating a version with direct connectivity, do steps (from step 3 onwards) as documented in [Create a custom connector with direct connectivity](https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector#create-a-custom-connector-with-direct-connectivity).
     * For creating a version with indirect connectivity, do steps (from step 3 onwards) as documented in [Create a custom connector with indirect connectivity](https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector#create-a-custom-connector-with-indirect-connectivity).



## Manage a custom connector version

To edit a custom connector, do the following steps:

  1. In the [Console](https://console.cloud.google.com/), go to the **Application Integration > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/integrations/custom-connectors)

This displays the list of custom connectors.

  2. Click the custom connector that has versions. 

The displays the connection details page.

  3. Click **Versions**. 

The versions for the selected connector appears.

  4. Click more_vert **Actions** to select one of the following options: 
     * **View Details** : To view the custom connector version details.
     * **Deprecate Version** : To deprecate the version.
     * **Delete** : To delete the version.
     * **Export** : To downloads the connector version as a JSON specification file. For more information, see Export and import.



## Export and import

You can share the connector between different Google Cloud projects by exporting and importing the connector specification. You can export any connection version and then import the specification to the same project or different Google Cloud projects. Exporting deprecated connector versions is not supported.

### Required roles and permissions

To get the permissions that you need to export and import a custom connector, ask your administrator to grant you the following IAM roles: 

  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the Cloud Storage bucket
  * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) on the project in which the secret is present. Alternatively, you can also ask your administrator to grant you or the service account, the `secretmanager.secrets.getIamPolicy` and `secretmanager.secrets.setIamPolicy` permissions on the project in which the secret is present.



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Export a custom connector

To export a connector version, follow these steps:

  1. In the [Console](https://console.cloud.google.com/), go to the **Application Integration > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/integrations/custom-connectors)

  2. Click the custom connector that you want to export. The custom connector's overview page opens.
  3. Click **Versions**. A list of versions of the custom connector is displayed.
  4. Click more_vert **More Actions** and then click upload **Export**. A JSON specification file for the custom connector is downloaded.



### Import a custom connector

To import a connector version, follow these steps:

  1. In the [Console](https://console.cloud.google.com/), go to the **Application Integration > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/integrations/custom-connectors)

The **Custom connectors** page appears. 
  2. Click download **Import**.
  3. Browse and select the JSON specification file for the custom connector. If you are importing the connector to a different project, then the **Service account** field is not prefilled. **Note:** Ensure that the connector that you want to import is not deprecated.

Based on whether the connector already exists or not, the following scenarios are possible: 

     * **Connector with the same name doesn't exist:** The **Create custom connector** page appears. The connector version in the imported JSON is prefilled. This version can't be changed.
     * **Connector with the same name exists but the same version doesn't exist:** The **Create version** page for that connector appears. Connector properties like connector type, name, description are prefilled from the existing connector and are not overwritten from the imported JSON. However, the connector version details and name are read from the imported JSON. Only the version name can be edited.
     * **Connector with the same name and version exists:** A warning message appears stating that the version already exists and a new version will be used when you import the JSON specification. If you click **Import** , the **Create version** page for that connector appears. Connector properties like the connector type, name, description are prefilled from the existing connector and are not overwritten by the imported JSON. However, the version details are read from the imported JSON and can be edited. The latest available version number is used for the version name. 
  4. Fill the remaining details and click **Create**. The connector is created with the imported JSON specification.



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
