---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-asset-inventory-services/
title: Asset inventory services for VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:08.197061+00:00
---

# Asset inventory services for VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-asset-inventory-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Asset inventory services for VMware Engine

Cloud Asset Inventory provides inventory services based on a time series database that lets you to search, export, and analyze asset metadata associated with the onboarded resources. Cloud Asset Inventory is a fully managed inventory service where you can control the access to Cloud Asset Inventory data down to each resource and policy type. This lets you benefit from the power of a centralized inventory, and also achieve least privilege when needed.

Key VMware Engine resources or assets are available through the Cloud Asset API and are also available using the Cloud Asset Inventory UI under Identity and Access Management on your Google Cloud console. The Cloud Asset API resources include:

  * [PrivateCloud](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds)
  * [Cluster](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters)
  * [VMwareEngineNetwork](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks)
  * [NetworkPeering](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings)
  * [PrivateConnection](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections)
  * [NetworkPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies)
  * [ExternalAccessRule](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules)
  * [ExternalAddress](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.externalAddresses)



For these resources, the Cloud Asset Inventory UI and Cloud Asset API enable the following features:

  * **Search and visibility:** Search asset metadata, including IAM policies associated with it by using a custom query language.

    * [SearchAllResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources): Searches all Google Cloud resources within the specified scope, such as project, folder, or organization.
    * [SearchAllIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies): Searches all IAM policies within the specified scope, such as project, folder, or organization.
    * [ListAssets](https://docs.cloud.google.com/asset-inventory/docs/listing-assets): View a paginated list of the assets at a given timestamp.
    * [QueryAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets): Issue a job that queries assets using a SQL statement compatible with BigQuery SQL.
    * These API also enable you to use the Global Search on the Google Cloud console to find VMware Engine resources. Use the global search bar to search for the name of any VMware Engine resource that's available through the Cloud Asset API. The resource displays in the list of results.

To search VMware Engine resources or IAM policies using the Cloud Asset Inventory console, do the following:

    1. Go to the **Asset Inventory** page in the Google Cloud console.

[Go to Asset Inventory](https://console.cloud.google.com/iam-admin/asset-inventory/policies)

    1. To set the scope of your search, open the Projects list box in the menu bar, and then select the organization, folder, or project to query.

    2. Select the **Resource** or **IAM Policy** tab.

    3. For **Filter results** , check the box next to the chosen filters.

The resources or policies matching the query are listed in the **Result** table.

To view the query as a Google Cloud CLI command, select **View query**.

To export the results, select **Download CSV**.

  * **Monitoring and analysis:** You can export all asset metadata at a certain timestamp or export event change history during a specific timeframe. Further, you can also monitor asset changes by subscribing to real-time notifications.

    * [ExportAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/exportAssets): Exports assets with time and resource types to a given Cloud Storage location or BigQuery table.
    * [BatchGetAssetsHistory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory): Batch gets the update history of assets that overlap a time window.
    * [Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds): An asset feed used to export asset updates to a destination. Set up Pub/Sub channels to get real-time updates on any asset config change, reduce the frequency of exports, and achieve continuous monitoring.

To analyze which IAM policies have access to which Google Cloud resources using the Cloud Asset Inventory console, do the following:

    1. In the Google Cloud console, go to the **Policy Analyzer** page.

[ Go to the Policy Analyzer page](https://console.cloud.google.com/iam-admin/analyzer)

    2. In the **Analyze policies** section, find the pane labeled **Custom query** and click **Create custom query** in that pane.

    3. In the **Select query scope** field, select the project, folder, or organization that you want to scope the query to. Policy Analyzer will analyze access for that project, folder, or organization, as well as any resources within that project, folder, or organization.

    4. Choose the resource to check and the role or permission to check for:

       1. In the **Parameter 1** field, select **Resource** from the drop-down menu.
       2. In the **Resource** field, enter the full resource name of the resource that you want to analyze access for. If you don't know the full resource name, start typing the display name of the resource, then select the resource from the list of resources provided.
       3. Click add **Add selector**.
       4. In the **Parameter 2** field, select either **Role** or **Permission**.
       5. In the **Select a role** or **Select a permission** field, select the role or permission that you want to check for.
       6. Optional: To check for additional roles and permissions, continue adding **Role** and **Permission** selectors until all the roles and permissions that you want to check for are listed.
    5. Optional: Click **Continue** , then select any [advanced options](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#options) that you want to enable for this query.

    6. In the **Custom query** pane, click **Analyze > Run query**. The report page shows the query parameters you entered, and a results table of all principals with the specified roles or permissions on the specified resource.

Policy analysis queries in the Google Cloud console can take one minute to run. After one minute, the Google Cloud console stops the query and displays all available results. If the query didn't finish in that time, the Google Cloud console displays a banner indicating that the results are incomplete. To get more results for these queries, [export the results to BigQuery](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-bigquery). 

You can generate a visualization of your query by clicking **Visualize results**. For more information, see [Visualize results](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#visualize-results) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). 

  * **IAM policy analysis:** [Analyze policy APIs](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy) to find out who has access to what.

    * [AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy): Analyzes IAM policies to answer which identities have what accesses on which resources.
    * [AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning): Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Cloud Storage or a BigQuery destination.



## What's next

  * Find the list of [resources available using Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types) and search for VMware.
  * Learn more about what you can do with [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
