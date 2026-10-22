---
url: https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status/
title: View VM Manager status for your organization by using Cloud Asset Inventory and BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:58.018195+00:00
---

# View VM Manager status for your organization by using Cloud Asset Inventory and BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  View VM Manager status for your organization by using Cloud Asset Inventory and BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

By exporting VM Manager data from Cloud Asset Inventory to BigQuery, you can run advanced queries to check whether VM Manager is enabled, view OS Config agent versions, and inspect operating system details across all projects in your organization.

This document describes how to use VM Manager, Cloud Asset Inventory, and BigQuery to view VM Manager enablement and operating system status reports for Compute Engine instances across your organization.

## Before you begin

  * [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).
  * Enable the [Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com).
  * [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) to store the exported data.
  * Verify that you have [the permissions required](https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status#required-roles) to view VM Manager status reports across the organization.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




## Required roles

To get the permissions that you need to export resource data and run queries in BigQuery, ask your administrator to grant you the following IAM roles on the project, folder, or organization: 

  * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export resource data and run queries in BigQuery. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export resource data and run queries in BigQuery:

  * `cloudasset.assets.exportOSInventories`
  * `cloudasset.assets.exportResource`
  * `bigquery.datasets.get`
  * `bigquery.tables.create`
  * `bigquery.tables.update`
  * `bigquery.tables.get`
  * `bigquery.jobs.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Export VM Manager data to BigQuery

To export OS inventory and resource data to BigQuery, do the following:

  1. Identify your organization ID:
         
         gcloud projects get-ancestors PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of your project.

  2. Export the OS inventory data collected by VM Manager from the VM instances:
         
         gcloud asset export \
             --content-type=os-inventory \
             --organization=ORGANIZATION_ID \
             --per-asset-type \
             --bigquery-table="projects/BQ_PROJECT_ID/datasets/DATASET_ID/tables/os"
         

Replace the following:

     * `ORGANIZATION_ID`: your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * `BQ_PROJECT_ID`: the project ID where your BigQuery dataset is located.
     * `DATASET_ID`: the name of your BigQuery dataset.
  3. Export the resource metadata to a BigQuery table:
         
         gcloud asset export \
             --content-type=resource \
             --organization=ORGANIZATION_ID \
             --per-asset-type \
             --bigquery-table="projects/BQ_PROJECT_ID/datasets/DATASET_ID/tables/res"
         

Replace the following:

     * `ORGANIZATION_ID`: your organization ID.
     * `BQ_PROJECT_ID`: the project ID where your BigQuery dataset is located.
     * `DATASET_ID`: the ID of your BigQuery dataset.



To learn how to export OS inventory snapshots, see [Export asset snapshot](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery#export).

## Generate a VM Manager status report for your organization

After you export the inventory data, you can run a SQL query in BigQuery to generate a VM Manager status report. This report provides the following information:

  * Whether VM Manager OS inventory data is being reported (`vmm_data`) for each VM instance.
  * The operating system long name (`os_info_reported_by_vmm`) and `osconfig` agent version (`osconfig_agent_version`) reported by each instance.
  * Whether the `osconfig.googleapis.com` API service is enabled (`osconfig_enabled_in_project`) across projects in your hierarchy.



To generate the report, perform the following steps:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste the following SQL script:
         
         SELECT
           vms.project,
           vms.zone,
           vms.instance_name,
           vms.instance_status,
           vms.vmm_data,
           vms.instance_creation_time,
           vms.vmm_info_update_time,
           --  vms.gce_image,
           vms.os_info_reported_by_vmm,
           vms.service_account,
           service.resource.data.state AS osconfig_enabled_in_project,
           vms.osconfig_agent_version
           --  "INFO N/A" as enable_osconfig_metadata_set_in_project,
           --  "INFO N/A" as enable_osconfig_metadata_set_in_instance,
         FROM
         (
           SELECT
             SPLIT(name, '/')[OFFSET(8)] AS instance_name,
             SPLIT(name, '/')[OFFSET(4)] AS project,
             SPLIT(name, '/')[OFFSET(6)] AS zone,
             instances.ancestors,
             instances.resource.data.creationTimestamp AS instance_creation_time,
             instances.resource.data.serviceAccounts[SAFE_OFFSET(0)].email AS service_account,
             CASE WHEN inventory.os_inventory IS NOT NULL THEN TRUE ELSE FALSE END AS vmm_data,
             /*  SPLIT(resource.data.disks[OFFSET(0)].licenses[OFFSET(0)], '/')[OFFSET(9)] as gce_image, */
             inventory.os_inventory.os_info.long_name AS os_info_reported_by_vmm,
             inventory.os_inventory.update_time AS vmm_info_update_time,
             instances.resource.data.status AS instance_status,
             inventory.os_inventory.os_info.osconfig_agent_version
           FROM
             DATASET_ID.res_compute_googleapis_com_Instance AS instances
             LEFT JOIN DATASET_ID.os_compute_googleapis_com_Instance AS inventory
           USING (name)
           --  WHERE instances.resource.data.status = "RUNNING"
         ) AS vms
         LEFT JOIN DATASET_ID.res_serviceusage_googleapis_com_Service AS service
           ON vms.ancestors[OFFSET(0)] = service.resource.data.parent
         WHERE service.resource.data.name = "osconfig.googleapis.com"
         

Replace `DATASET_ID` with the name of your BigQuery dataset.

  3. Click **Run**.




For more information about querying data, see [Running queries](https://docs.cloud.google.com/bigquery/docs/running-queries).

After you generate the report, you can use Data Studio to create a custom dashboard. For more information, see [Analyze data with Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio).

## What's next

  * [Provision VM Manager resources by using Terraform](https://docs.cloud.google.com/compute/vm-manager/docs/terraform).
  * Learn more about [OS inventory in VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management).
  * Learn how to [export asset metadata to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery).
  * Use [Data Studio to visualize BigQuery data](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
