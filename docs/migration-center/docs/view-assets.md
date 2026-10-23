---
url: https://docs.cloud.google.com/migration-center/docs/view-assets/
title: View the collected assets \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:21.369136+00:00
---

# View the collected assets  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/view-assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  View the collected assets Stay organized with collections  Save and categorize content based on your preferences. 

After you add your assets to Migration Center with an automatic scan by using one of the available [collection methods](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery#collection_methods), you can review the basic information about your infrastructure directly in Migration Center, both at the asset level, and in aggregate.

## View summary of all the collected assets

To view an aggregated summary about your assets, follow these steps:

  1. In the Google Cloud console, go to the **Summary** page.

[Go to Summary](https://console.cloud.google.com/migration/discovery/overview?gtm_source=documentation&gtm_source_id=view_assets)

  2. The **Summary** page displays a dashboard with high-level information about your assets, including asset types, graphs about the operating system installed, memory, cores, and storage.




## View details for an individual asset

To view the details about a specific asset, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page.

[Go to Assets](https://console.cloud.google.com/migration/discovery/assets?gtm_source=documentation&gtm_source_id=view_assets)

  2. To view the list of assets for an asset type, click an asset type. For example, click **Servers** or **S3**.

To narrow the selection of assets, apply filters in the `Filter` field. Select a property name to filter on and enter a property value. For example, to filter for all assets that belong to a group, set the property name to `Groups`. For the property value, select or enter a group name.

To filter assets with the `Attributes` property, use key-value pairs, using one of the following options:

     * Filter by key only: `Attributes:"key123":""`
     * Filter by a key-value pair: `Attributes:"key1":"value1"`
     * Filter by value only: `Attributes:"":"value123"`

If you know the asset or name, you can also enter it directly in the `Filter` field to search for the asset or property.

  3. From the list of assets, click the asset for which you want to view information about.




On the individual asset page, you can see different information, depending on the asset being a server or a database deployment.

### Available details for servers

On the details page for a server, you can see the basic information about the server, including the name, IP address, and operating system. You can also see the following tabs that provide you additional information about the server:

  * **Insights.** This tab shows the Google Cloud products that you can migrate the server to, and the fit score of the match. For more information about insights, see [View and understand insights](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights).
  * **Details.** This tab shows all the data that was collected about your server, including information about CPU, disks, network, and vCenter.
  * **Metadata.** This tab provides you with additional information about the server, such as the following: 
    * Contributing sources, which is the name of the discovery client or import job that created the asset.
    * Full asset name
    * Asset creation date
    * Date of the last update
  * **Performance.** This tab shows all the aggregated performance data and statistics collected with the Migration Center discovery client, manual file import, and the `mcdc` CLI, such as the following: 
    * Daily input/output operations per second
    * Daily memory usage
    * Daily CPU usage
    * Network bytes received and sent per second



### Available details for databases

On the details page for a database, you can see the basic information about the database, including the name, engine, edition, and version. You can also see the following tabs that provide you additional information about the database deployment:

  * **Insights.** This tab shows the Google Cloud products that you can migrate the database to, and the fit score of the match. For more information about insights, see [View and understand insights](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights). If you click the fit score, you can see the detailed fit assessment for the migration. For more information, see [Detailed fit assessment](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights#detailed-fit-assessment).
  * **Details.** This tab shows all the data that was collected about your database, including the name, CPU, memory, and storage for the server that hosts the database.
  * **Metadata.** This tab shows you the following additional information about the database: 
    * Contributing sources, which is the name of the discovery client or import job that created the asset.
    * Full asset name.
    * Asset creation date.
    * Date of the last update.
  * **Performance.** This tab shows all the aggregated performance data and statistics collected with the database collection scripts, such as: 
    * Daily input/output operations per second
    * Daily memory usage
    * Daily CPU usage
  * **Databases.** This tab shows the details about the databases collected in a particular instance, and the number of schemas, tables, and other database configuration details.



### Available details for AWS assets

For AWS assets, such as S3 buckets, EKS clusters, ELB clusters, ECS clusters, and Lambda functions, you can view basic information about the asset, including its name, original ID, and location.

You can also see the following tabs that provide additional information:

  * **Metadata.** This tab provides you with additional information about the asset, such as: 
    * Labels
    * Attributes
    * Groups
    * Data sources
    * Full asset Name
    * Created
    * Updated
  * **Details.** For S3 buckets, this tab shows the following information: 
    * Versioning
    * Total objects
    * Storage class



For each of the AWS assets, you can also see structured attributes as key-value pairs that are specific to that service. For example, you can see the following structured attributes for an EKS cluster:

  * `cluster_endpoint_access`
  * `cluster_vpc_id`
  * `endpoint`
  * `kubernetes_version`
  * `logging`
  * `platform_version`
  * `role_arn`
  * `status`



## Label assets

Migration Center lets you assign labels to your assets to help you organize your resources. The labels assigned to an asset must meet the [requirements for labels](https://docs.cloud.google.com/resource-manager/docs/labels-overview#requirements).

To assign labels to assets, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page.

[Go to Assets](https://console.cloud.google.com/migration/discovery/assets?gtm_source=documentation&gtm_source_id=view_assets)

  2. On the assets details page, click an asset type.

  3. From the list of assets, click an asset to which you want to assign labels.

  4. On the **Labels** pane, enter a label key and label value.




After you assign labels to assets, you can filter for specific assets by using the label key and value.

## Out of scope assets

Migration Center lets you mark assets as out of scope. This is useful when the discovery client finds and collects data from assets that you don't plan to migrate, for example corporate desktop machines, or assets that you are going to decommission.

After you mark an asset as out of scope, the following happens:

  * The asset is removed from the list of in-scope assets.
  * The asset is never included in the TCO reports and in the **Summary** page for assets.
  * The asset is hidden from the groups that it was included in.
  * Existing labels remain associated with the asset.
  * Asset data continues to be updated.



If you decide to bring an asset back in scope later, the asset retains its metadata and group memberships, and you don't lose any information about the asset.

To mark one or more assets as out of scope, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page.

[Go to Assets](https://console.cloud.google.com/migration/discovery/assets?gtm_source=documentation&gtm_source_id=view_assets)

  2. Select the assets that you want to mark as out of scope, then click **Out of scope**.

  3. In the dialog that appears, enter the reason for marking the asset as out of scope. You can use this to filter out-of-scope assets later.

  4. Click **Confirm**.




To view out-of-scope assets, click the **Out of scope** tab on the **Assets** page.

To put one or more assets back in scope, follow these steps:

  1. From the **Out of scope** tab on the **Assets** page, select the assets that you want to put back in scope, then click **Put back in scope**.
  2. In the dialog that appears, click **Confirm**.



## What's next

  * Learn how to [view and understand insights](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
