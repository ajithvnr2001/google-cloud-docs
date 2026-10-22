---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs/
title: View audit logs \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.130828+00:00
---

# View audit logs  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  View audit logs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to monitor the activity and health of your cluster in Cluster Director by using Cloud Logging audit logs.

Cluster Director integrates with Logging to provide detailed logs of your cluster operations and the Slurm environment. You can use these logs to monitor cluster operations, monitor the behavior of the Slurm scheduler, or troubleshoot issues. To learn more about using audit logs in Google Cloud, see [Logging overview](https://docs.cloud.google.com/logging/docs/overview).

## Before you begin

When you access and use the Google Cloud console, you don't need to authenticate. You can automatically use Google Cloud services and APIs.

### Required roles

To get the permissions that you need to view audit logs, ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View audit logs

To monitor the health and activity of your cluster, use one of the following log options:

  * To quickly track cluster creation, update, or delete operations view pre-configured audit logs.

  * To view detailed system activity in your cluster and Slurm environment, view filtered component logs.




### View pre-configured audit logs

To view pre-configured audit logs for Cluster Director by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to view the details of. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  4. In the **Compute** section, in the **Logging** row, click **View logs**. The **Logs Explorer** page appears, and filters are automatically applied to display pre-configured audit logs for your cluster.




### View custom component logs

To create and view logs for specific components of your cluster, such as controller or compute nodes, you can use filtering queries in the Logs Explorer by using the Google Cloud console. To do so, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If the **Query** pane isn't visible, click the **Show query** toggle to the on position.

  3. In the **Query** pane, enter a query to filter your logs by. Based on the logs that you want to view, you can use one or more of the following queries:

     * **View cluster operations logs** : to track cluster create, update, or delete operations that are sent to the Cluster Director API, use one of the following queries:

       * To view a list of all cluster creation operations in your project, use the following query:
             
             logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
             protoPayload.serviceName="hypercomputecluster.googleapis.com"
             protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.CreateCluster"
             

       * To view a list of all cluster update operations in your project, use the following query:
             
             logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
             protoPayload.serviceName="hypercomputecluster.googleapis.com"
             protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster"
             

       * To view a list of cluster update operations for a specific cluster, use the following query:
             
             logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
             protoPayload.serviceName="hypercomputecluster.googleapis.com"
             protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster"
             protoPayload.resourceName="projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME"
             

       * To view a list of cluster delete operations in your project, use the following query:
             
             logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
             protoPayload.serviceName="hypercomputecluster.googleapis.com"
             protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.DeleteCluster"
             

     * **View cluster nodes logs** : to view detailed system and Slurm activity from the cluster nodes, use one of the following queries:

       * To view the logs for a controller node, use the following query:
             
             labels.clusterName = "CLUSTER_NAME"
             labels.hostname = "CLUSTER_NAME-controller"
             

       * To view the logs for your nodeset nodes, use the following query:
             
             labels.clusterName = "CLUSTER_NAME"
             labels.hostname = "CLUSTER_NAME-nodeset"
             

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `REGION`: the region where your cluster exists.

     * `CLUSTER_NAME`: the name of your cluster.




For more information about writing queries for filtering logs, see [Write advanced queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-by-expression).

## What's next

  * [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
