---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering/
title: Understanding cluster resource usage \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:47.548519+00:00
---

# Understanding cluster resource usage  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Understanding cluster resource usage Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to use GKE usage metering to understand the usage profiles of Google Kubernetes Engine (GKE) Standard clusters, and tie usage to individual teams or business units within your organization. GKE usage metering has no impact on billing for your project; it lets you understand resource usage at a granular level.

**Note:** We recommend that you use [GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) instead of GKE usage metering. GKE cost allocation lets you distribute the costs of a cluster to its users.

## Overview

GKE usage metering tracks information about the resource requests and actual resource usage of your cluster's workloads. GKE usage metering tracks information about CPU, GPU, TPU, memory, storage, and optionally network egress. You can differentiate resource usage by using Kubernetes [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/), or a combination of both.

Data is stored in BigQuery, where you can query it directly or export it for analysis with external tools such as [Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio).

GKE usage metering is helpful for scenarios such as the following:

  * Tracking per-tenant resource requests and actual resource consumption in a multi-tenant cluster where each tenant operates within a given namespace.
  * Determining the resource consumption of a workload running in a given cluster, by assigning a unique label to the Kubernetes objects associated with the workload.
  * Identifying workloads whose resource requests differ significantly from their actual resource consumption, so that you can more efficiently allocate resources for each workload.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster. If you need one, [create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



### Limitations

You can use the sample BigQuery queries and Data Studio template to join GKE usage metering data with exported Google Cloud billing data in BigQuery. This lets you estimate a cost breakdown by cluster, namespace, and labels.

GKE usage metering data is purely advisory, and doesn't affect your Google Cloud bill. For billing data, your Google Cloud billing invoice is the sole source of truth.

The following limitations apply:

  * Special contract discounts or credits are not accounted for.
  * Resources created outside the scope of GKE are not tracked by namespace or label.
  * Only labels from Pod and PersistentVolumeClaim objects are tracked by usage reporting.
  * Only [dynamically provisioned PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) are supported.
  * Only pd-standard and pd-ssd [disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types) are supported. GKE usage metering might include costs for regional versions of both disk types under the same SKU. 
  * Data Studio does not support the visualization of [machine types capable of bursting](https://docs.cloud.google.com/compute/docs/machine-types#cpu-bursting).
  * You can only export data to a BigQuery dataset that is in the same project as your cluster. Additionally, the source data and the destination dataset must be in the same region. For more information, see [Data location and transfers](https://docs.cloud.google.com/bigquery/docs/dts-locations).
  * You must not use ports 27304, 47082 and 47083, because these ports are reserved by network egress tracking.
  * Custom `StorageClass` objects are not supported.
  * Network egress metering is not supported for Windows Server nodes.
  * Network egress metering is not supported for Shared VPC or VPC Network Peering.
  * Network egress metering is not supported for clusters with more than 150 nodes.



### Prerequisites

Before you use GKE usage metering, you must meet the following prerequisites:

  * [Billing export for BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) is enabled. Charges are associated with [BigQuery usage](https://cloud.google.com/bigquery/pricing).
  * Version 250.0.0 or later of the Google Cloud CLI is required. Use `gcloud --version` to check.
  * You must [enable the BigQuery API](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service#creating_a_project_and_enabling_the_api) in your Google Cloud project. If you first enabled GKE after July 2018, the API is already enabled.



## Enable GKE usage metering

To enable GKE usage metering, you first create a BigQuery dataset for either a single cluster, multiple clusters in the project, or the entire project. For more information about choosing a mapping between datasets and clusters, see Choosing one or more BigQuery datasets.

Next, you enable GKE usage metering when creating a new cluster or by modifying an existing cluster.

Optionally, you can create a Data Studio dashboard to visualize the resource usage of your clusters.

### Create the BigQuery dataset

To use GKE usage metering for clusters in your Google Cloud project, you first create the BigQuery dataset, and then configure clusters to use it. You can use a single BigQuery dataset to store information about resource usage for multiple clusters in the same project.

Visit [Creating Datasets](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) for more details. Set the `Default table expiration` for the dataset to `Never` so that the table doesn't expire. If a table expires, it is recreated automatically as an empty table.

**Note:** This feature writes to the BigQuery dataset that you provide with the Google service account (`service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`) and with the [Kubernetes Engine Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent).**Warning:** If you delete a BigQuery dataset or table that a cluster is using to log GKE usage metering data, Cloud Logging shows transient warnings such as `Failed to upload a record to BigQuery`. To resolve the warning, re-create the dataset or configure the cluster to use a different dataset. Your historical data will be lost.

### Enable GKE usage metering on your cluster

You can enable GKE usage metering on a cluster by using either the Google Cloud CLI or the Google Cloud console.

Enabling GKE usage metering also enables resource consumption metering by default. To selectively disable resource consumption metering while continuing to track resource requests, see the specific instructions for enabling GKE usage metering using the Google Cloud CLI, in this document.

Network egress metering is disabled by default. To enable it, see the caveats and instructions in Optional: Enable network egress metering in this document.

### gcloud

To enable GKE usage metering on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --resource-usage-bigquery-dataset RESOURCE_USAGE_DATASET
    

Resource consumption metering is enabled by default. To disable it and only track resource requests, add the flag `--no-enable-resource-consumption-metering` to the preceding command. **You also need to modify the example queries in the rest of this topic so that they do not query for resource consumption.**

**Note:** Network egress metering is disabled by default. To enable it, see the caveats and instructions in Optional: Enabling network egress metering in this topic.

You can also change the dataset an existing cluster uses to store its usage metering data by changing the value of the `--resource-usage-bigquery-dataset` flag.

If needed, a table is created within the BigQuery dataset when the cluster is updated.

### Console

**Note:** When using Google Cloud console, it is not possible to enable GKE usage metering while selectively disabling resource consumption metering. If you need to do this, use the `gcloud` instructions instead.

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to modify, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. Under **Features** , click _edit_ **Edit** next to **GKE usage metering**.

  4. Select **Enable GKE usage metering**.

  5. Enter the name of the BigQuery dataset.

  6. Optional: select **Enable network egress metering** after reviewing the caveats and instructions in Optional: Enabling network egress metering.

  7. Click **Save Changes**..




#### Optional: Enable network egress metering

By default, network egress data is not collected or exported. Measuring network egress requires a network metering agent (NMA) running on each node. The NMA runs as a privileged Pod, consumes some resources on the node (CPU, memory, and disk space), and enables the [nf_conntrack_acct sysctl flag](https://www.kernel.org/doc/Documentation/networking/nf_conntrack-sysctl.txt) on the kernel (for connection tracking flow accounting).

If you are comfortable with these caveats, you can enable network egress tracking for use with GKE usage metering. To enable network egress tracking, include the `--enable-network-egress-metering` option when creating or updating your cluster, or select **Enable network egress metering** when enabling GKE usage metering in the Google Cloud console.

To disable network egress metering, add the `--no-enable-network-egress-metering` flag when you update your cluster with the command line. Alternatively, you can clear **Enable network egress metering** in the GKE usage metering section of the cluster in the Google Cloud console.

## Verify that GKE usage metering is enabled

To verify that GKE usage metering is enabled on a cluster, and to confirm which BigQuery dataset stores the cluster's resource usage data, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --format="value(resourceUsageExportConfig)"
    

The output is empty if GKE usage metering is not enabled, and otherwise shows the BigQuery dataset used by the cluster, as in the following example output:
    
    
    bigqueryDestination={u'datasetId': u'test_usage_metering_dataset'}
    

## Choose one or more BigQuery datasets

A dataset can hold GKE usage metering data for one or more clusters in your project. Whether you use one or many datasets depends on your security needs:

  * A single dataset for the entire project simplifies administration.
  * A dataset per cluster lets you delegate granular access to the datasets.
  * A dataset per related group of clusters lets you find the right mix of simplicity and granularity for your needs.



## Visualize GKE usage metering data using a Data Studio dashboard

You can visualize your GKE usage metering data using a [Data Studio dashboard](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio). This lets you filter your data by cluster name, namespace, or label. You can also adjust the reporting period dynamically. If you have experience with Data Studio and BigQuery, you can create a customized dashboard. You can also clone a dashboard that we created specifically for GKE usage metering.

**Note:** You may see discrepancies between GKE usage metering data and Cloud Billing data, due to upload latency. Batches of Cloud Billing data take up to 5 hours to appear in BigQuery, while GKE usage metering data appears in BigQuery roughly every hour.

You can use the dashboard to visualize resource requests and consumption on your clusters over time.

**Note:** Data Studio is not supported by Cloud Customer Care. For more information, see the [Data Studio Help Center](https://support.google.com/looker-studio).

### Prerequisites

  1. Enable [Exporting Google Cloud billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) if it is not already enabled.

During this process, you create a dataset, but the table within the dataset can take up to 5 hours to appear and start populating. When the table appears, its name is `gcp_billing_export_v1_BILLING_ACCOUNT_ID`.

  2. Enable [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering#enabling) on at least one cluster in the project. Note the name you chose for the BigQuery dataset.

  3. Enable [Data Studio](https://lookerstudio.google.com/c/navigation/reporting) if it's not already enabled.

  4. Gather the following information, which is needed to configure the dashboard:

     * Cloud Billing export dataset ID and data table
     * GKE usage metering dataset ID
  5. Ensure that you have version 2.0.58 or later of the [BigQuery CLI](https://docs.cloud.google.com/bigquery/docs/quickstarts/load-data-bq). To check the version, run `bq version`, and `gcloud components update` to update your BigQuery CLI.

  6. The commands in this section should be run in a Linux terminal or in Cloud Shell.




### Create the BigQuery cost breakdown table

  1. Download one of the following query templates:

     * If you enabled consumption metering, download [`this template`](https://docs.cloud.google.com/static/kubernetes-engine/docs/how-to/usage_metering_query_template_request_and_consumption.sql).
     * If you didn't enable consumption metering, download [`this template`](https://docs.cloud.google.com/static/kubernetes-engine/docs/how-to/usage_metering_query_template_request_only.sql).

If you are using Cloud Shell, copy this file into the directory where you perform the following commands.

  2. Run the following command to set environment variables:
         
         export GCP_BILLING_EXPORT_TABLE_FULL_PATH=YOUR_BILLING_EXPORT_TABLE_PATH
         export USAGE_METERING_PROJECT_ID=YOUR_USAGE_METERING_PROJECT_ID
         export USAGE_METERING_DATASET_ID=YOUR_USAGE_METERING_DATASET_ID
         export USAGE_METERING_START_DATE=YOUR_USAGE_METERING_START_DATE
         export COST_BREAKDOWN_TABLE_ID=YOUR_COST_BREAKDOWN_TABLE_ID
         export USAGE_METERING_QUERY_TEMPLATE=YOUR_TEMPLATE_PATH
         export USAGE_METERING_QUERY=YOUR_RENDERED_QUERY_PATH
         

Replace the following:

     * `YOUR_BILLING_EXPORT_TABLE_PATH`: the path to your generated billing export table. This table has a name similar to `PROJECT_ID.DATASET_ID.gcp_billing_export_v1_xxxx`.
     * `YOUR_USAGE_METERING_PROJECT_ID`: the name of your Google Cloud project.
     * `YOUR_USAGE_METERING_DATASET_ID`: the name of the dataset you created in BigQuery, such as `all_billing_data`.
     * `YOUR_USAGE_METERING_START_DATE`: the start date of your query in the form `YYYY-MM-DD`.
     * `YOUR_COST_BREAKDOWN_TABLE_ID`: the name of a new table that you chose, such as `usage_metering_cost_breakdown`. This table is used as input to Data Studio.
     * `YOUR_TEMPLATE_PATH`: the name of the query template you downloaded, either `usage_metering_query_template_request_and_consumption.sql` or `usage_metering_query_template_request_only.sql`.
     * `YOUR_RENDERED_QUERY_PATH`: the name of the path for the rendered query that you choose, such as `cost_breakdown_query.sql`.

As an example, your environment variables might resemble the following:
    
    export GCP_BILLING_EXPORT_TABLE_FULL_PATH=my-billing-project.all_billing_data.gcp_billing_export_v1_xxxx
    export USAGE_METERING_PROJECT_ID=my-billing-project
    export USAGE_METERING_DATASET_ID=all_billing_data
    export USAGE_METERING_START_DATE=2022-05-01
    export COST_BREAKDOWN_TABLE_ID=usage_metering_cost_breakdown
    export USAGE_METERING_QUERY_TEMPLATE=usage_metering_query_template_request_only.sql
    export USAGE_METERING_QUERY=cost_breakdown_query.sql
    

  3. Render the query from the template:
         
         sed \
         -e "s/\${fullGCPBillingExportTableID}/$GCP_BILLING_EXPORT_TABLE_FULL_PATH/" \
         -e "s/\${projectID}/$USAGE_METERING_PROJECT_ID/" \
         -e "s/\${datasetID}/$USAGE_METERING_DATASET_ID/" \
         -e "s/\${startDate}/$USAGE_METERING_START_DATE/" \
         "$USAGE_METERING_QUERY_TEMPLATE" \
         > "$USAGE_METERING_QUERY"
         

  4. Create a new cost breakdown table that refreshes every 24 hours:
         
         bq query \
         --project_id=$USAGE_METERING_PROJECT_ID \
         --use_legacy_sql=false \
         --destination_table=$USAGE_METERING_DATASET_ID.$COST_BREAKDOWN_TABLE_ID \
         --schedule='every 24 hours' \
         --display_name="GKE Usage Metering Cost Breakdown Scheduled Query" \
         --replace=true \
         "$(cat $USAGE_METERING_QUERY)"
         

For more information about scheduling queries, see [Set up scheduled queries](https://docs.cloud.google.com/bigquery/docs/scheduling-queries#set_up_scheduled_queries).




### Create the BigQuery data source

  1. In Data Studio, go to [Data Sources](https://lookerstudio.google.com/c/navigation/datasources).
  2. Click _add_ **Create** , and then click **Data source**.
  3. Select **BigQuery**.
  4. Name your data source. From the toolbar, click the words **Untitled Data Source** to replace the text with a descriptive name.
  5. Select **Custom Query** and then select your project ID.
  6. Paste the following query into the Query Editor:
         
         SELECT
           *
         FROM
           `USAGE_METERING_PROJECT_ID.USAGE_METERING_DATASET_ID.COST_BREAKDOWN_TABLE_ID`
         

  7. Click **Connect**.




### Create the Data Studio dashboard

  1. Copy the [GKE usage metering dashboard](https://lookerstudio.google.com/reporting/1g7Z1hjCIkAHmL4QStbWNvuSUe-eQ-vnk) into your project.
  2. Click _more_vert_ **More options** , and then click content_copy **Make a copy**.
  3. In the **Copy this report** dialog, from the **New data source** list, select the data source that you created.
  4. Click **Copy report**.



The dashboard is created, and you can access it at any time in the list of [Data Studio reports](https://lookerstudio.google.com/c/navigation/reporting) for your project.

### Use the Data Studio dashboard

The dashboard contains multiple reports:

Usage breakdown
    This report contains overall cluster usage ratio among all clusters sending usage metering data to the same BigQuery data source. It also includes detailed information about resource type such as CPU, memory, or network egress by namespace. You can limit the report data to one or more individual clusters or namespaces.
Usage breakdown with unallocated resources
    This report is similar to the usage breakdown report, but spreads unallocated resources proportionally across all namespaces. Unallocated resources include idle resources and any resources that are not allocated by GKE usage metering to specific tenants.
Cost trends * drill down by namespace
    Usage trends among all clusters sending usage metering data to the same BigQuery data source by namespace. You can select one or more individual clusters, namespaces, resources, or SKUs.
Cost trends * drill down by label
    Cost trends among all clusters sending usage metering data to the same BigQuery data source. You can select one or more individual clusters, resources, label names, or label values.
Consumption-based Metering
    Consumption trends among all clusters sending usage metering data to the same BigQuery data source. You can select one or more individual namespaces, label keys, or label values. This report is only populated if resource consumption metering is enabled on at least one cluster.
**Note:** Because of differences in the frequency of data availability between usage metering and Cloud Billing, data shown in the dashboard is not definitive and is informational only.

You can change pages using the navigation menu. You can change the timeframe for a page using the date picker. To share the report with members of your organization, or to revoke access, click _person_add_alt_ **Share Report**.

After you copy the report into your project, you can customize it by using the [Data Studio report editor](https://support.google.com/looker-studio/answer/6371822). Even if the report template provided by Google changes, your copy is unaffected.

## Explore GKE usage metering data using BigQuery

To view data about resource requests using BigQuery, query the `gke_cluster_resource_usage` table within the relevant BigQuery dataset.

To view data about actual resource consumption, query the `gke_cluster_resource_consumption` table. Network egress consumption data remains in the `gke_cluster_resource_usage` because there is no concept of resource requests for egresses.

For more information about using queries in BigQuery, see [Running queries](https://docs.cloud.google.com/bigquery/docs/query-overview#running_queries). The fields in the schema are stable, though more fields may be added in the future.

These queries are simple examples. Customize your query to find the data you need.

### Query for resource requests
    
    
    SELECT
      cluster_name,
      labels,
      usage
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_usage'
    WHERE
      namespace="NAMESPACE"
    

### Query for resource consumption
    
    
    SELECT
      cluster_name,
      labels,
      usage
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_consumption'
    WHERE
      namespace="NAMESPACE"
    

Replace the following:

  * `CLUSTER_GCP_PROJECT`: the name of your Google Cloud project that contains the cluster that you want to query.
  * `USAGE_METERING_DATASET`: the name of your usage metering table.
  * `NAMESPACE`: the name of your namespace.



### More examples

Expand the following sections to see more sophisticated examples.

#### How to query costs, broken down by namespace

These queries ignore a cluster's resource usage when the billing information of the associated cloud resource has not yet been exported to the Google Cloud billing export dataset. This delay happens when the time window of a cloud resource usage record is ahead of the latest record in the exported Google Cloud billing data. The latency for billing export can be up to 5 hours.

##### Resource requests
    
    
    SELECT
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      resource_usage.resource_name,
      resource_usage.sku_id,
      MIN(resource_usage.start_time) AS usage_start_time,
      MAX(resource_usage.end_time) AS usage_end_time,
      SUM(resource_usage.usage.amount * gcp_billing_export.rate) AS cost
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_usage' AS resource_usage
    LEFT JOIN (
      SELECT
        sku.id AS sku_id,
        SUM(cost) / SUM(usage.amount) AS rate,
        MIN(usage_start_time) AS min_usage_start_time,
        MAX(usage_end_time) AS max_usage_end_time
      FROM
        'CLUSTER_GCP_PROJECT.BILLING_DATASET.BILLING_TABLE'
      WHERE
        project.id = "CLUSTER_GCP_PROJECT"
      GROUP BY
        sku_id) AS gcp_billing_export
    ON
      resource_usage.sku_id = gcp_billing_export.sku_id
    WHERE
      resource_usage.start_time >= gcp_billing_export.min_usage_start_time
      AND resource_usage.end_time <= gcp_billing_export.max_usage_end_time
    GROUP BY
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      resource_usage.resource_name,
      resource_usage.sku_id
      

##### Resource consumption
    
    
    SELECT
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      resource_usage.resource_name,
      resource_usage.sku_id,
      MIN(resource_usage.start_time) AS usage_start_time,
      MAX(resource_usage.end_time) AS usage_end_time,
      SUM(resource_usage.usage.amount * gcp_billing_export.rate) AS cost
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_consumption' AS resource_usage
    LEFT JOIN (
      SELECT
        sku.id AS sku_id,
        SUM(cost) / SUM(usage.amount) AS rate,
        MIN(usage_start_time) AS min_usage_start_time,
        MAX(usage_end_time) AS max_usage_end_time
      FROM
        'CLUSTER_GCP_PROJECT.BILLING_DATASET.BILLING_TABLE'
      WHERE
        project.id = "CLUSTER_GCP_PROJECT"
      GROUP BY
        sku_id) AS gcp_billing_export
    ON
      resource_usage.sku_id = gcp_billing_export.sku_id
    WHERE
      resource_usage.start_time >= gcp_billing_export.min_usage_start_time
      AND resource_usage.end_time <= gcp_billing_export.max_usage_end_time
    GROUP BY
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      resource_usage.resource_name,
      resource_usage.sku_id
      

#### How to query costs in a specific time period, broken down by namespace and labels

These queries show the costs for a specific time period, by namespaces labels.

##### Resource requests by time period, grouped by namespaces and labels
    
    
    DECLARE drilldown_label STRING DEFAULT 'DRILLDOWN_LABEL';
    DECLARE project_id STRING default "CLUSTER_GCP_PROJECT";
    
    SELECT
      DATE(start_time) as date,
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      label.value AS label_value,
      resource_usage.resource_name,
      resource_usage.sku_id,
      gcp_billing_export.sku_description,
      SUM(resource_usage.usage.amount) AS usage,
      resource_usage.usage.unit AS usage_unit,
      SUM(resource_usage.usage.amount * gcp_billing_export.rate) AS cost_estimate,
      gcp_billing_export.currency
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_usage' AS resource_usage
    
    -- select only workloads matching the defined "drilldown_label"
      CROSS JOIN UNNEST(labels) AS label WHERE label.key=drilldown_label
    
    -- join with billing table to get pricing information and sku description
      LEFT JOIN (
      SELECT
        DATE(usage_start_time) as date,
        sku.id AS sku_id,
        sku.description AS sku_description,
        SAFE_DIVIDE(SUM(cost), SUM(usage.amount)) AS rate,
        currency
      FROM
        'CLUSTER_GCP_PROJECT.BILLING_DATASET.BILLING_TABLE'
      WHERE
        project.id = project_id
      GROUP BY
        date,
        sku_id,
        sku_description,
        currency) AS gcp_billing_export
      ON DATE(resource_usage.start_time) = gcp_billing_export.date AND resource_usage.sku_id = gcp_billing_export.sku_id
    
    GROUP BY
      date,
      cluster_name,
      cluster_location,
      namespace,
      label_value,
      resource_name,
      sku_id,
      sku_description,
      usage_unit,
      currency
    
    ORDER BY
      date,
      cluster_name,
      cluster_location,
      namespace,
      label_value,
      resource_name
      

##### Resource consumption by time period, grouped by namespaces and labels
    
    
    DECLARE drilldown_label STRING DEFAULT 'DRILLDOWN_LABEL';
    DECLARE project_id STRING default "CLUSTER_GCP_PROJECT";
    
    SELECT
      DATE(start_time) as date,
      resource_usage.cluster_name,
      resource_usage.cluster_location,
      resource_usage.namespace,
      label.value AS label_value,
      resource_usage.resource_name,
      resource_usage.sku_id,
      gcp_billing_export.sku_description,
      SUM(resource_usage.usage.amount) AS usage,
      resource_usage.usage.unit AS usage_unit,
      SUM(resource_usage.usage.amount * gcp_billing_export.rate) AS cost_estimate,
      gcp_billing_export.currency
    FROM
      'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_consumption' AS resource_usage
    
    -- select only workloads matching the defined "drilldown_label"
      CROSS JOIN UNNEST(labels) AS label WHERE label.key=drilldown_label
    
    -- join with billing table to get pricing information and sku description
      LEFT JOIN (
      SELECT
        DATE(usage_start_time) as date,
        sku.id AS sku_id,
        sku.description AS sku_description,
        SAFE_DIVIDE(SUM(cost), SUM(usage.amount)) AS rate,
        currency
      FROM
        'CLUSTER_GCP_PROJECT.BILLING_DATASET.BILLING_TABLE'
      WHERE
        project.id = project_id
      GROUP BY
        date,
        sku_id,
        sku_description,
        currency) AS gcp_billing_export
      ON DATE(resource_usage.start_time) = gcp_billing_export.date AND resource_usage.sku_id = gcp_billing_export.sku_id
    
    GROUP BY
      date,
      cluster_name,
      cluster_location,
      namespace,
      label_value,
      resource_name,
      sku_id,
      sku_description,
      usage_unit,
      currency
    
    ORDER BY
      date,
      cluster_name,
      cluster_location,
      namespace,
      label_value,
      resource_name
      

#### How to show actual resource consumption as a percentage of resource requests, over time

This query shows the ratio of actual CPU consumption to CPU requests, so you can see which Pods request too little or too much CPU compared to actual requirements.
    
    
    WITH
      constraints AS (
        SELECT
          TIMESTAMP(START_TIME) as min_time,
          TIMESTAMP(END_TIME) as max_time,
          "CLUSTER_GCP_PROJECT" as project_id
      ),
      request_based_amount_by_namespace AS (
        SELECT
          namespace,
          resource_name,
          SUM(usage.amount) AS requested_amount,
          usage.unit AS unit
        FROM
          'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_usage' as requested_resource_usage
        INNER JOIN
          constraints
        ON
          requested_resource_usage.start_time >= constraints.min_time
          AND requested_resource_usage.end_time <= constraints.max_time
          AND requested_resource_usage.project.id = constraints.project_id
        GROUP BY
          namespace, resource_name, usage.unit
      ),
      consumption_based_amount_by_namespace AS (
        SELECT
          namespace,
          resource_name,
          SUM(usage.amount) AS consumed_amount,
          usage.unit AS unit
        FROM
          'CLUSTER_GCP_PROJECT.USAGE_METERING_DATASET.gke_cluster_resource_consumption' as consumed_resource_usage
        INNER JOIN
          constraints
        ON
          consumed_resource_usage.start_time >= constraints.min_time
          AND consumed_resource_usage.end_time <= constraints.max_time
          AND consumed_resource_usage.project.id = constraints.project_id
        GROUP BY
          namespace, resource_name, usage.unit
      )
    SELECT
      request_based_amount_by_namespace.namespace,
      request_based_amount_by_namespace.resource_name,
      requested_amount,
      consumed_amount,
      request_based_amount_by_namespace.unit,
      CASE
        WHEN consumed_amount IS NULL THEN NULL
        WHEN requested_amount = 0 THEN NULL
        ELSE consumed_amount / requested_amount END
          AS consumption_to_request_ratio
    FROM
      request_based_amount_by_namespace
      FULL JOIN
      consumption_based_amount_by_namespace
      ON
      request_based_amount_by_namespace.namespace = consumption_based_amount_by_namespace.namespace
      AND
      request_based_amount_by_namespace.resource_name = consumption_based_amount_by_namespace.resource_name
    ORDER BY
      consumption_to_request_ratio
    DESC
      

## GKE usage metering schema in BigQuery

The following table describes the schema for the GKE usage metering tables in the BigQuery dataset. If your cluster is running a version of GKE that supports resource consumption metering and resource requests, an additional table is created with the same schema.

Field | Type | Description | `cluster_location` | `STRING` |  The name of the Compute Engine zone or region in which the GKE cluster resides.   
---|---|---  
`cluster_name` | `STRING` |  The name of the GKE cluster.   
`namespace` | `STRING` |  The Kubernetes namespace from which the usage is generated.   
`resource_name` | `STRING` |  The name of the resource, such as "cpu", "memory", and "storage".   
`sku_id` | `STRING` |  The SKU ID of the underlying Google Cloud cloud resource.   
`start_time` | `TIMESTAMP` |  The UNIX timestamp of when the usage began.   
`end_time` | `TIMESTAMP` |  The UNIX timestamp of when the usage ended.   
`fraction` | `FLOAT` |  The fraction of a cloud resource used by the usage. For a dedicated cloud resource that is solely used by a single namespace, the fraction is always 1.0. For resources shared among multiple namespaces, the fraction is calculated as the requested amount divided by the total capacity of the underlying cloud resource.   
`cloud_resource_size` | `INTEGER` |  The size of the underlying Google Cloud resource. For example, the size of vCPUs on a n1-standard-2 instances is 2.   
`labels.key` | `STRING` |  The key of a Kubernetes label associated with the usage.   
`labels.value` | `STRING` |  The value of a Kubernetes label associated with the usage.   
`project.id` | `STRING` |  The ID of the project in which the GKE cluster resides.   
`usage.amount` | `FLOAT` |  The quantity of `usage.unit` used.   
`usage.unit` | `STRING` |  The base unit in which resource usage is measured. For example, the base unit for standard storage is _byte-seconds_.   
  
The units for GKE usage metering must be interpreted in the following way:

  1. The CPU `usage.unit` is _seconds_ , which is the total CPU time that a Pod requested or utilized. For example, if we have two Pods that each request 30 CPU and run for 15 minutes then the aggregate amount of the request table is 54,000 seconds (2 Pods * 30 CPU * 15 minutes * 60 seconds / minute).

  2. The memory `usage.unit` is _bytes-seconds_ , which is the integral of memory over time that a Pod requested or utilized. For example, if we have two Pods that each request 30 GiB and run for 15 minutes then the aggregate amount of the request table is 5.798+13 byte-seconds (2 Pods * 30 GiB * 15 minutes * 60 seconds / minute * 1073741824 bytes / GiB).




## Understanding when GKE usage metering data is written to BigQuery

There are two conditions when GKE usage metering writes usage records to BigQuery metrics:

  1. The Pod phase changes to `succeeded` or `failed`, or when the Pod is deleted.
  2. The hourly schedule's timestamp to write records is reached while the Pod is still running.

GKE usage metering generates an hourly schedule where it writes Pod usage records to BigQuery for all running Pods. The schedule's timestamp is not the same across all clusters.

If you have multiple Pods running at that timestamp, you'll find multiple usage records with the same `end_time`. These usage records' `end_time` indicate the hourly schedule's timestamp.

Also, if you have multiple Pods that have been running for multiple hours, you also have a set of usage records with an `end_time` that matches the `start_time` of another set of usage records.




## Disable GKE usage metering

### gcloud

To disable GKE usage metering on a cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --clear-resource-usage-bigquery-dataset
    

**Note:** The BigQuery dataset is preserved. You can remove it if you don't need the data and no cluster is using it.

### Console

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to modify, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. Under **Features** , click _edit_ **Edit** next to **GKE usage metering**.

  4. Clear **Enable GKE usage metering**.

  5. Click **Save Changes**.




## What's next

  * Learn how to [track resource consumption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) by namespace and label with cost allocation.
  * Learn how to [view observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).
  * Learn how to [configure metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics).
  * Follow the tutorial about [observability with Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/observability-with-prometheus).
  * Learn about the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
