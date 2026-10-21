---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-shared-cluster/
title: Delete a shared cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:57.858943+00:00
---

# Delete a shared cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-shared-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete a shared cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster)

This document explains how to delete a shared Kubernetes cluster from a Google Distributed Cloud (GDC) air-gapped zone. Deleting a shared cluster removes all its workloads, node pools, control plane nodes, and corresponding resources within the cluster. Since a shared cluster can span multiple projects, deleting a shared cluster could affect multiple projects.

This document is for audiences such as IT administrators within the platform administrator group, who are responsible for managing container workloads within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To delete a shared cluster, ask your Organization IAM Admin to grant you the **User Cluster Admin** (`user-cluster-admin`) role. This role isn't bound to a namespace.

## Delete a shared cluster and its resources

Complete the following steps to delete a shared cluster and its resources:

###  Console 

  1. Verify that all persistent volume claims (PVC) are deleted from your shared cluster. For more information, see [Delete persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/delete-persistent-storage).

  2. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your organization.

Shared clusters are organization-scoped resources. If you select a project instead, you'll view standard clusters, which are project-scoped. For more information, see the [resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster).

  3. In the navigation menu, select **Kubernetes Engine > Clusters**.

  4. In the cluster list, click the cluster that you want to delete.

  5. Click delete **Delete Cluster**.

  6. When prompted, type the given confirmation phrase and click **Delete** to delete the cluster.

The deletion can take up to 60 minutes.




###  API 

  1. Verify that all persistent volume claims (PVC) are deleted from your shared cluster. For more information, see [Delete persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/delete-persistent-storage).

  2. Remove the `Cluster` custom resource from the GDC zone:
         
         kubectl delete clusters.cluster.gdc.goog/SHARED_CLUSTER_NAME \
             -n platform \
             --kubeconfig MANAGEMENT_API_SERVER
         

Replace the following:

     * `SHARED_CLUSTER_NAME`: the name of the cluster to delete.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the Kubernetes cluster is hosted. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

The deletion can take up to 60 minutes. If you want the deletion process to run in the background, append the `--wait=false` parameter to the command.




###  Terraform 

  1. Verify that all persistent volume claims (PVC) are deleted from your shared cluster. For more information, see [Delete persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/delete-persistent-storage).

  2. Remove the resource using Terraform:
         
         terraform destroy -target kubernetes_manifest.cluster-create
         




The deletion can take up to 60 minutes.

## What's next

  * [Kubernetes cluster overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters)
  * [Design access boundaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Design workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
