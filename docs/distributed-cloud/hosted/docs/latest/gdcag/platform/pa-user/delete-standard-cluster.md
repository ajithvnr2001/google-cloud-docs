---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-standard-cluster/
title: Delete a standard cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:59.127928+00:00
---

# Delete a standard cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-standard-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete a standard cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to delete a standard Kubernetes cluster from a Google Distributed Cloud (GDC) air-gapped zone. Deleting a standard cluster removes all its workloads, node pools, control plane nodes, and corresponding resources within the cluster. Since a standard cluster is confined to a single project, the deletion doesn't affect any other projects.

This document is for audiences such as application developers within the application operator group, who are responsible for managing container workloads within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To delete a standard cluster, ask your Project IAM Admin to grant you the **Standard Cluster Admin** (`standard-cluster-admin`) role. This role is bound to your project namespace. For more information, see [Manage access to standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters).

## Delete a standard cluster and its resources

Complete the following steps to delete a shared cluster and its resources:

###  Console 

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project.

Standard clusters are project-scoped resources. If you select an organization instead, you'll view shared clusters, which are organization-scoped. For more information, see the [resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster).

  2. In the navigation menu, select **Kubernetes Engine > Clusters**.

  3. In the cluster list, click the cluster that you want to delete.

  4. Click delete **Delete Cluster**.

  5. When prompted, type the given confirmation phrase and click **Delete** to delete the cluster.

The deletion can take up to 45 minutes.




###  API 

  1. Verify that all persistent volume claims (PVC) are deleted from your standard cluster. For more information, see [Delete persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/delete-persistent-storage).

  2. Remove the `Cluster` custom resource from the GDC zone:
         
         kubectl delete clusters.cluster.gdc.goog/STANDARD_CLUSTER_NAME \
             --namespace PROJECT_NAME \
             --kubeconfig MANAGEMENT_API_SERVER
         

The deletion can take up to 45 minutes. If you want the deletion process to run in the background, append the `--wait=false` parameter to the command.

Replace the following:

     * `STANDARD_CLUSTER_NAME`: the name of the cluster to delete.
     * `PROJECT_NAME`: the name of the project that manages the cluster.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the cluster is hosted. If you have not yet generated a kubeconfig file for the management API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).



###  Terraform 

  1. Verify that all persistent volume claims (PVC) are deleted from your standard cluster. For more information, see [Delete persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/delete-persistent-storage).

  2. Remove the resource using Terraform:
         
         terraform destroy -target kubernetes_manifest.cluster-create
         

The deletion can take up to 45 minutes.




## What's next

  * [Kubernetes cluster overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters)
  * [Design access boundaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Design workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
