---
url: https://docs.cloud.google.com/alloydb/docs/cluster-list/
title: View the clusters in a project \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:22.963282+00:00
---

# View the clusters in a project  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cluster-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  View the clusters in a project Stay organized with collections  Save and categorize content based on your preferences. 

To monitor database health, performance capacity, and backup coverage across your Google Cloud project, you can list your AlloyDB clusters and inspect their status.

The **Clusters** page of the Google Cloud console displays summary cards and a resource table that provide information about all clusters in a project.

The following summary cards provide an overview of the database health and performance:

  * **Performance**. Displays the number of clusters that are at their performance limits for CPU utilization, connections capacity, and replication lag.

  * **Backups**. Displays the number of clusters without an automated backup policy and the number of clusters whose most recent successfully created backup is older than 24 hours, including clusters without backups.




The resource table provides a list of clusters, instances, and their details. For more information about filtering the resource table, see Filter the resource table.

Each summary card displays multiple metrics that you can click to filter the resource table. For example, when you click **No backups within 24h** in the **Backups** summary card, the resource table filters the information to display only clusters whose backups are not taken in the last 24 hours.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).

  * You must have the `roles/monitoring.admin` role (the Monitoring Admin predefined Identity and Access Management (IAM) role) in the Google Cloud project you are using.

  * You must have one of these IAM roles in the Google Cloud project you are using:

    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## View the list of clusters

You can view the list of clusters, instances, and their details on the **Clusters** page.

### Console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the **Select a project** list, select a Google Cloud project.
  3. Click **Open**.
  4. To filter the resulting list of all of your project's clusters, either by location or another attribute, see Filter the resource table.



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To view the list of clusters, use the [ `gcloud alloydb clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/list) command. 

#### View the list of clusters in all regions

To view the list of clusters in all regions, run the following command: 
    
    
    gcloud alloydb clusters list \
        --project=PROJECT_ID

Replace `PROJECT_ID` with the ID of your project. 

#### View the list of clusters in a specific region

To view the list of clusters in a specific region, run the following command: 
    
    
    gcloud alloydb clusters list \
        --region=REGION_ID \
        --project=PROJECT_ID

Replace the following: 

  * `REGION_ID`: The region whose clusters you want to list.
  * `PROJECT_ID`: The ID of your project.



## Filter the resource table

By default, the resource table lists all clusters, instances, and their details. You can filter the resource table by using the summary cards or the **Filter** list in the resource table.

To filter the resource table, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the **Select a project** list, select a Google Cloud project. 
  3. Click **Open**. 
  4. In the **Clusters** page that opens, choose one of the following methods to filter the resource table view: 
     * Choose a summary card displayed at the top of the page, and click a metric value in the summary card.
     * Go to the resource table that displays the list of clusters, and select properties and values of the resources from the **Filter** list.



### Resource table properties

The **Filter** list in the resource table provides the following properties:

**Properties** | **Description**  
---|---  
**Resource name** | The name of the resource.  
**Resource type** | The type of a resource.  
**Location** | The location of the resource.  
**Read pool nodes** | The number of nodes of read pool instances.  
**Private IP address** | The IP address of a primary or read pool instance.  
**Public IP address** | The public IP address of your instance.  
**High availability** | The clusters or instances that are highly available.  
**CPU%** | The CPU percentage utilization of resources.  
**Memory available** | The amount of memory available for resources.  
**Active connections** | The number of active connections of resources.  
**Replication lag** | The replication lag of resources in seconds.  
**Automated backups** | The clusters whose automated backups are either enabled or disabled.  
**Most recent backup** | The clusters whose backups were created on, before, or after a specific date.  
**Labels** | The labels used for resources that are under a specific cost center or environment.  
**Created** | The date on which the resource was created.  
**Encryption** | The resources with encryption keys that are Google-managed, customer-managed, or customer-supplied.  
**No backups within 24h** | The resources whose backups are not taken in the last 24 hours.  
  
## What's next

  * For information about how to monitor AlloyDB instances, see [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
