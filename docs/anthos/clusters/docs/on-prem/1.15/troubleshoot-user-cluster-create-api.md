---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-user-cluster-create-api/
title: Troubleshoot issues creating a user cluster in the Google Cloud console \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:12.742232+00:00
---

# Troubleshoot issues creating a user cluster in the Google Cloud console  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-user-cluster-create-api/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Troubleshoot issues creating a user cluster in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/troubleshoot-user-cluster-create-api)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/troubleshoot-user-cluster-create-api)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows you how to investigate issues creating an Google Distributed Cloud user cluster in the Google Cloud console.

## The admin cluster isn't displayed on the **Cluster basics** drop-down list

The admin cluster must be registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management) before you can create user clusters in the Google Cloud console. If you don't see the admin cluster on the drop-down list on the **Cluster basics** section in the Google Cloud console, the admin cluster either wasn't registered, or it was registered using the `gcloud container hub memberships register` command.

Check the registration status:

  * In the Google Cloud console, go to the **Anthos** > **Clusters** page, and select the same Google Cloud project in which you attempted to create the user cluster.

[Go to the GKE Enterprise clusters page](https://console.cloud.google.com/anthos/clusters)

    * If the admin cluster **isn't** displayed on the list, see [Register an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#register_an_admin_cluster).

    * If the admin cluster **is** displayed on the list, this indicates that the cluster was registered using the `gcloud container hub memberships register` command. This `gcloud` command doesn't properly register admin clusters.




To fix the registration issue:

  1. On your admin workstation, get the membership name:
         
         kubectl describe membership membership \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  2. Unregister the admin cluster. In the following command, replace:

     * `MEMBERSHIP_NAME` with the membership name from the previous command.
     * `FLEET_HOST_PROJECT_ID` with the ID of your [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). This is the project that you selected when you attempted to create the user cluster in the Google Cloud console.
     * `ADMIN_CLUSTER_KUBECONFIG` with the path to the kubeconfig file for you admin cluster.
     * `ADMIN_CLUSTER_CONTEXT` with the admin cluster's context as it appears in the kubeconfig file. You can get this value from the command line by running `kubectl config current-context`.
    
    gcloud container fleet memberships unregister MEMBERSHIP_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
      --context=ADMIN_CLUSTER_CONTEXT
    

  3. Follow the steps in [Register an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#register_an_admin_cluster) to re-register the cluster.




## Cluster creation errors

This section describes some errors that happen during cluster creation in the Google Cloud console.

### Resource already exist error

User cluster creation fails with an error message similar to the following:
    
    
    Resource 'projects/1234567890/locations/europe-west1/vmwareClusters/user-cluster1'
    already exists
    Request ID: 129290123128705826
    

This error message indicates that the cluster name is already in use.

One solution to fix the issue:

  1. [Delete the cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deleting-a-user-cluster).

  2. Create the cluster again with a another name that doesn't conflict with an existing cluster.




### Anti-affinity groups error

User cluster creation fails with an error message similar to the following:
    
    
    - Validation Category: VCenter
        - [FATAL] Hosts for AntiAffinityGroups: Anti-affinity groups enabled with
        available vsphere host number 1 less than 3, please add more vsphere hosts
        or disable anti-affinity groups.
    

The VMware Distributed Resource Scheduler (DRS) anti-affinity rules require at least 3 physical hosts in your vSphere environment. To fix the issue, disable **Anti-affinity groups** in the **Features** section on the **Cluster details** page for your cluster, as follows:

  1. In the Google Cloud console, go to the GKE Enterprise clusters page.

[Go to the GKE Enterprise clusters page](https://console.cloud.google.com/anthos/clusters)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. In the **Features** section, click edit  **Edit**.

  5. Clear **Enable Anti-affinity groups** , and click **Done**.

  6. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




### Conflicting IP addresses error

User cluster creation fails with an error message similar to the following:
    
    
    - Validation Category: Network Configuration
    - [FAILURE] CIDR, VIP and static IP (availability and overlapping): user: user
      cluster control plane VIP "10.251.133.132" overlaps with
      example-cluster1/control plane VIP "10.251.133.132"
    

Currently, you can't edit fields such as the **Control plane VIP** and the **Ingress VIP** in the **Load balancer** section of the **Cluster details** page in the Google Cloud console. To fix conflicting IP addresses:

  1. [Delete the cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deleting-a-user-cluster).

  2. Create the cluster again with IP addresses that doesn't conflict with an existing cluster.




## Cluster deletion fails to remove cluster from the Cloud console

After [deleting a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deleting-a-user-cluster), it is still displayed in the Google Cloud console. This can happen when the user cluster has lost connectivity to its admin cluster. To fix this issue, follow the steps in Remove Anthos On-Prem API resources.

## Remove GKE On-Prem API resources

The Google Cloud console uses the GKE On-Prem API to manage user cluster lifecycle. You can also [configure user clusters to be managed by the GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-user-cluster). The GKE On-Prem API resources aren't deleted in the following cases:

  * `gkectl` was used to delete a node pool for a user cluster that is managed by the GKE On-Prem API.

  * The admin cluster for a user cluster created in the Cloud console is deleted.




When the GKE On-Prem API resources aren't deleted, the user cluster is still displayed in the Google Cloud console in an unhealthy state. Do the following steps to remove the leftover resources.

  1. Set the following environment variables:
         
         export PROJECT_ID=FLEET_HOST_PROJECT_ID
         export REGION=REGION
         export CLUSTER_NAME=USER_CLUSTER_NAME
         

Replace the following:

     * FLEET_HOST_PROJECT_ID: the project ID that the user cluster was created in, which is also the fleet host project.

     * REGION: the cluster's region. The region is displayed in the console in the cluster's **Details** panel in the **Location** field.

     * USER_CLUSTER_NAME: The name of the cluster.

  2. If the user cluster's node pool was deleted, then the cluster is still registered with a fleet. Delete the fleet membership of the user cluster by running the following command:
         
         gcloud container fleet memberships delete USER_CLUSTER_NAME
         

If the admin cluster was deleted, then the cluster is still registered with a fleet. Delete the fleet membership of the admin cluster by running the following command:
         
         gcloud container fleet memberships delete ADMIN_CLUSTER_NAME
         

See the [`gcloud command reference`](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete) for details.

  3. Delete the GKE On-Prem API metadata:
         
         curl -X DELETE "https://gkeonprem.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/vmwareClusters/${CLUSTER_NAME}:unenroll?force=true&allow_missing=true" \
         -H "Content-Type: application/json" \
         -H "X-GFE-SSL: yes" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
