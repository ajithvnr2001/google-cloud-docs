---
url: https://docs.cloud.google.com/alloydb/docs/instance-view/
title: View instance details \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:54.133342+00:00
---

# View instance details  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  View instance details Stay organized with collections  Save and categorize content based on your preferences. 

To inspect the status, IP address, machine type, active database flags, and zone distribution of an instance in an AlloyDB for PostgreSQL cluster, you can view its instance details.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section and view the details about your instance.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To view details about an instance, use the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command.
    
    
    gcloud alloydb instances describe INSTANCE_ID \
     --region=REGION_ID \
     --cluster=CLUSTER_ID \
     --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The instance's region ID.
  * `CLUSTER_ID`: The ID of the instance's cluster.
  * `PROJECT_ID`: The ID of the instance's project.



## Determine a primary instance's zones

For the sake of high availability, an AlloyDB primary instance comprises two virtual machine (VM) instances: an active VM which responds to requests, and a standby VM. These VMs run within [two different zones of the instance's region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

You can determine which zones your primary instance's VMs run in by following the steps in the previous section, and then examining a particular part of the command output or Google Cloud console display:

### Console

In the Google Cloud console, go to the **Clusters** page:

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

The **Location** column displays the zone of each primary instance's active VM.

Note that the same column displays only the region ID for clusters and read-pool instances. For example, a cluster with a **Location** of `us-central1` might have a primary instance displaying its active VM's full zone ID of `us-central1-f`.

The **Instances in your cluster** section of a cluster's detail page displays this same information, in the primary instance's **Location** field. This field also lists the standby VM's location, labeled as "secondary zone".

### gcloud

After running the command described in the previous section, locate the following fields in the command's output:

  * `writableNode`: The active VM's zone ID

  * `nodes`: The standby VM's zone ID




For example, the following partial output indicates that the primary instance's active VM runs in zone `us-central1-f`, while its standby is in `us-central1-c`:
    
    
    nodes:
    - zoneId: us-central1-c
    reconciling: false
    state: READY
    uid: 3477b790-21bc-4338-a09e-339912e3b28e
    updateTime: '2022-08-09T21:22:16.671268941Z'
    writableNode:
      zoneId: us-central1-f
    

## Determine a read pool instance's nodes

When viewing the details of a read pool instance by using the gcloud CLI, you can see further information about its constituent nodes with the optional `--view=FULL` argument. For more information, see [Troubleshoot read pool queries](https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
