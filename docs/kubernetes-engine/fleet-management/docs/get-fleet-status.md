---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status/
title: Get fleet membership status \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:57.284754+00:00
---

# Get fleet membership status  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Get fleet membership status Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to get the fleet membership status of your clusters, including listing all your fleet members, and getting membership details such as the cluster's [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) or if it has [fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) enabled. You can use this information to validate that you have successfully registered a cluster, or to perform other fleet-level tasks.

You can view clusters that have been successfully registered by using the gcloud CLI or the Google Cloud console. Some additional status details are available only by using the gcloud CLI.

### Console

### Required roles

Ensure you have the [minimum permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) to view fleet clusters in the Google Cloud console.

A cluster's fleet registration status is shown in the following pages:

  * The GKE clusters page displays the fleet name in the cluster list's **Fleet** column.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  * The GKE cluster details page shows the cluster's [unique membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) in the **GKE Hub Membership** field.

  * If you have running workloads on the cluster, the fleet name is also displayed on the GKE workloads page, in the workload list's **Fleet** column.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)




### gcloud

The following commands provide information about fleet members:

  * List all registered clusters in a project:
        
        gcloud container fleet memberships list \
          --project=PROJECT_ID
        

In the command output, the `Name` column lists the [membership names](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) of registered clusters. The membership name might be the same as the cluster name depending on the membership name that was chosen when the cluster was registered. The `EXTERNAL_ID` column lists the clusters' UIDs in the `kube-system` namespace. You can find a cluster's UID with the following command: `kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'`

**Note:** Depending on the version, admin clusters in Google Distributed Cloud deployments on VMware might not be in the command output. If you don't know the membership name of the admin cluster, run the following command on your admin workstation to get the membership name: `kubectl describe membership membership --kubeconfig ADMIN_CLUSTER_KUBECONFIG`
  * View fleet membership details about a cluster:
        
        gcloud container fleet memberships describe MEMBERSHIP_NAME \
          --project=PROJECT_ID
        

This command returns complete details of your cluster's fleet membership, including when it was registered and if it has [fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) enabled.




## What's next

Learn more about working with, and connecting to fleet clusters in the following guides:

  * [Manage identity for authenticating to clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure#manage_identity)
  * [Work with fleet clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console)
  * [Work with fleet clusters from the command line](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/command-line)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
