---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/on-prem-api/
title: Troubleshoot clusters enrolled in the GKE On-Prem API \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:00.499001+00:00
---

# Troubleshoot clusters enrolled in the GKE On-Prem API  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/on-prem-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot clusters enrolled in the GKE On-Prem API Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to investigate issues creating an Google Distributed Cloud user cluster in the Google Cloud console.

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud tools. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the Google Cloud console, and the Google Cloud CLI are clients of the API, and they use the API to create, update, upgrade, and delete clusters in your data center. If you created the cluster using a standard client, the cluster is _enrolled_ in the GKE On-Prem API, which means you can use the standard clients to manage the lifecycle of the cluster (with some exceptions). 

## Cluster creation errors

This section describes some errors that happen during cluster creation in the Google Cloud console.

### Resource already exists error

User cluster creation fails with an error message similar to the following:
    
    
    Resource 'projects/1234567890/[...]/user-cluster1'
    already exists
    Request ID: 129290123128705826
    

This error message indicates that the cluster name is already in use.

One solution to fix this is issue is to delete and recreate the cluster:

  1. [Delete the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/reset-nodes).
  2. Create the cluster again with a another name that doesn't conflict with an existing cluster.



### Conflicting IP addresses error

User cluster creation fails with an error message similar to the following:
    
    
    - Validation Category: Network Configuration
    - [FAILURE] CIDR, VIP and static IP (availability and overlapping): user: user
      cluster control plane VIP "10.251.133.132" overlaps with
      example-cluster1/control plane VIP "10.251.133.132"
    

You can't edit fields such as the **Control plane VIP** and the **Ingress VIP** in the **Load balancer** section of the **Cluster details** page in the Google Cloud console. To fix conflicting IP addresses, delete and recreate the cluster:

  1. [Delete the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/reset-nodes).
  2. Create the cluster again with IP addresses that don't conflict with an existing cluster.



## Remove unhealthy clusters

A cluster can get in an unhealthy state for many reasons, such as:

  * Connectivity issues with the [Connect Agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) or the on-premises environment.
  * The admin cluster for a user cluster was deleted, or there are connectivity issues between the admin and user clusters.



If the console is unable to delete a cluster, use gcloud CLI commands to delete Google Cloud resources from unhealthy clusters. If you haven't updated the gcloud CLI recently, run the following command to update the components:
    
    
    gcloud components update
    

Next, delete the Google Cloud resources.

### User cluster

  1. Delete the user cluster:
         
         gcloud container bare-metal clusters delete USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --force \
           --allow-missing \
           --ignore-errors

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to delete.

     * `PROJECT_ID`: The ID of the project that the cluster is registered to.

     * `REGION`: The Google Cloud location associated with the user cluster. The location is displayed in the console.

The `--force` flag deletes a cluster that has node pools. Without the `--force` flag, you have to [delete the node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/delete) first, and then delete the cluster.

The `--allow-missing` flag allows the command to continue if the cluster isn't found.

The `--ignore-errors` flag removes Google Cloud resources when the admin and user clusters are unreachable. 

This command deletes the cluster if it exists and removes both GKE On-Prem API and fleet membership resources from Google Cloud.

  2. Confirm that the GKE On-Prem API resources have been deleted:
         
         gcloud container bare-metal clusters list \
           --project=PROJECT_ID \
           --location=-

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to a [specific region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api). 

  3. Confirm that the fleet membership resources have been deleted:
         
         gcloud container fleet memberships list \
           --project=PROJECT_ID




### Admin cluster

  1. If you enrolled the admin cluster in the GKE On-Prem API, unenroll it:
         
         gcloud container bare-metal admin-clusters unenroll ADMIN_CLUSTER_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --allow-missing --ignore-errors 
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.
     * `PROJECT_ID`: The ID of the fleet host project.
     * `REGION`: The Google Cloud region.

The `--allow-missing` flag unenrolls the cluster if the fleet membership isn't found.

The `--ignore-errors` flag removes Google Cloud resources when the admin and user clusters are unreachable. 

This command removes the GKE On-Prem API resources from Google Cloud.

  2. Remove the cluster from the fleet:
         
         gcloud container fleet memberships delete ADMIN_CLUSTER_NAME \
          --project=PROJECT_ID \
          --location=global

This command removes fleet membership resources from Google Cloud.

  3. Confirm that the GKE On-Prem API resources have been deleted:
         
         gcloud container fleet memberships delete ADMIN_CLUSTER_NAME --project=FLEET_HOST_PROJECT_ID
         

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to a [specific region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api). 

  4. Confirm that the fleet membership resources have been deleted:
         
         gcloud container fleet memberships list \
           --project=PROJECT_ID




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
