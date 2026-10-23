---
url: https://docs.cloud.google.com/looker/docs/looker-core-lineage/
title: Track data lineage with Knowledge Catalog \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:19.697969+00:00
---

# Track data lineage with Knowledge Catalog  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-lineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Track data lineage with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to track data lineage for your Looker (Google Cloud core) instance using Knowledge Catalog.

**Data lineage** is the process of tracking how data flows through your systems. By integrating Looker (Google Cloud core) with Knowledge Catalog, you can visualize the end-to-end journey of your data from its source in BigQuery through the Looker semantic layer (LookML views and Explores) to downstream consumption in dashboards, Looks, and AI or data agents.

This visibility provides bidirectional lineage tracking for data governance, impact analysis, and audit workflows:

  * **Downstream impact analysis:** Predict which dashboards, Explores, and downstream consumers are affected before you make schema or model changes. For example, before dropping a column in a BigQuery table, you can check the lineage graph to see which Looker dashboards might break.
  * **Upstream data audit:** Trace the origin, transformations, and chain of custody of the metrics that are displayed in executive dashboards and Looks.



## Before you begin

To use data lineage with Looker (Google Cloud core), you must meet the following prerequisites:

  1. **Looker (Google Cloud core):** Data lineage is supported for all [edition types](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions) of Looker (Google Cloud core) instances. Looker (original) instances don't integrate with Knowledge Catalog.
  2. **Required Permissions:** To view lineage graphs, you need the following IAM roles:

     * **Looker Schema Viewer** (`roles/looker.schemaViewer`) on the project that's hosting the Looker (Google Cloud core) instance. This role is required to view Looker (Google Cloud core)-specific metadata that populates the side panel when viewing a lineage graph.

**Note:** You can add the Looker Schema Viewer role only by using Google Cloud CLI. 
           
           gcloud projects add-iam-policy-binding YOUR_PROJECT_ID
           --member=PRINCIPAL_TYPE:PRINCIPAL_ID
           --role=roles/looker.schemaViewer

For more information, see the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) documentation.
     * **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) or equivalent permissions to view Knowledge Catalog assets

     * **Data Lineage Viewer** (`roles/datalineage.viewer`) to read lineage data


**Caution:** SQL table references in LookML must match the exact casing of the corresponding BigQuery tables. For example, if a BigQuery table name is lowercase, the LookML reference must also be lowercase. Case discrepancies prevent downstream lineage from populating in the lineage graph.

## Enable data lineage

To enable data lineage, complete each of the following steps:

  1. **Enable the Knowledge Catalog integration for Looker (Google Cloud core):** The integration between your Looker (Google Cloud core) instance and Knowledge Catalog is enabled by default in the Google Cloud console. If the integration has been disabled, you must enable it again. See [Enable the integration](https://docs.cloud.google.com/looker/docs/looker-core-dataplex#enable) for instructions.
  2. **Enable the Knowledge Catalog Lineage preview feature inside Looker:** The [**Knowledge Catalog Lineage** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#dataplex-lineage) is disabled by default on the **Preview Features** page of the **Admin** panel within your Looker (Google Cloud core) instance.
  3. **Enable the Data Lineage API:** You must enable the **Data Lineage API** (`datalineage.googleapis.com`) on any Google Cloud projects that host your Looker (Google Cloud core) instance and your BigQuery data. 

[Enable the Data Lineage API](https://console.cloud.google.com/apis/enableflow?apiid=datalineage.googleapis.com)

  4. **Enable service-level lineage ingestion:** [Ensure](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion) that the lineage and Looker (Google Cloud core) service-level integration is enabled. Service-level lineage adheres to the following default states: 
     * To prevent future pricing implications, Looker (Google Cloud core) service-level lineage ingestion is disabled by default for projects that, at the preview release date of this feature, had the Data Lineage API enabled and hosted at least one Looker (Google Cloud core) instance.
     * Service-level lineage ingestion is enabled by default for Looker (Google Cloud core) instances created after the preview release date of this feature in projects with the Data Lineage API enabled.



To view the lineage configuration for a Google Cloud project, see the [Get current configuration](https://docs.cloud.google.com/dataplex/docs/use-lineage#get-current-configuration) documentation. If the integration with Looker (Google Cloud core) is disabled, the command will return output similar to the following:
    
    
        {
        "name": "projects/123456789012/locations/global/config",
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "LOOKER_CORE"
              },
              "lineageEnablement": {
                "enabled": false
              }
            }
          ]
        },
        "etag": "Wb35wDxTTLd6Z+QAL+Yd4g=="
      }

The project ID in the response will reflect the ID in your request. The `etag` field is a checksum that is generated by the server and that is based on the current value of the configuration.

## View data lineage

Once the integration is enabled and the initial sync is complete (which may take up to 24 hours), you can view lineage in the Knowledge Catalog console.

  1. In the Google Cloud console, go to the **Knowledge Catalog** page. 

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)

  2. Click **Search** in the left navigation pane.
  3. Search for a BigQuery table or a Looker (Google Cloud core) asset (like a dashboard or an Explore). 
     * You can use the **Filters** panel to filter by **System** > **Looker**.
  4. Click the name of the asset to open its details page.
  5. Click the **Lineage** tab.



The lineage graph displays the asset as a central node, with upstream sources to the left and downstream consumers to the right. This bidirectional layout lets you evaluate downstream impacts to the right, or trace upstream provenance and source tables to the left.

### Interpret the lineage graph

The lineage graph consists of **nodes** and **links** :

  * **Nodes:** Represent data assets. Supported Looker (Google Cloud core) assets include the following: 
    * **Looker dashboard**
    * **Looker dashboard element** (tile)
    * **Looker Look**
    * **LookML Explore**
    * **LookML view**
  * **Links:** Represent the flow of data. For example, a link from a BigQuery table to a LookML view indicates that the view selects data from that table.



### Identify asset owners

To find out who owns a downstream asset that might be impacted by a change, follow these steps:

  1. In the lineage graph, click the node for the asset (for example, a Looker dashboard).
  2. An information panel opens on the right side of the screen.
  3. Look for the **Aspects** section to find the **Owner** (email address).



## Filter the lineage list

When in the **List** view for lineage, you can filter entities by property name or value. For example, complex LookML models can generate large lineage graphs with many intermediate entities. To focus on business impact, you could filter by entity type by following these steps:

  1. In the **Lineage** tab, toggle to the **List** view.
  2. Locate the **Filter** options in the toolbar.
  3. In the **Entity** filter, enter **Looker Dashboard** and **Looker Look** to filter out intermediate types like **LookML View** and **Looker Explore**.



The entity list updates to show only the selected asset types, making it easier to identify user-facing content.

## Limitations

The Looker (Google Cloud core) lineage integration has the following limitations during the preview release:

  * **Data Sources:** In the preview, lineage is supported only for **BigQuery** data sources.
  * **Granularity:** Lineage is provided at the object level (table, view, Explore, dashboard). **Column-level lineage** is not supported.
  * **Latency:** Lineage data is not real-time. The synchronization process typically takes four hours. However, synchronization may take up to eight hours, depending on the timing of Looker metadata exports and lineage data consumption. Changes made in Looker or BigQuery may take some time to appear in the lineage graph.
  * **Complex SQL:** LookML that's defined with complex custom SQL (for example, Liquid templates, derived tables with complex joins) may not be fully parsed, potentially resulting in disconnected nodes.



## Pricing

During the preview release, there is no charge for data lineage features that are used with this integration.

When data lineage becomes generally available, pricing will be incurred. To prevent future pricing implications, Looker (Google Cloud core) lineage ingestion is disabled by default for projects that, at the preview release date of this feature, had the Data Lineage API enabled and hosted at least one Looker (Google Cloud core) instance.

For more information, see the [Knowledge Catalog pricing page](https://cloud.google.com/dataplex/pricing).

## What's next

  * [Manage metadata resources with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex)
  * [Learn more about data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
