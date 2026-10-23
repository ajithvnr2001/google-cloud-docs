---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke/
title: Join GKE Windows Server nodes automatically to a Managed Microsoft AD domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:47.731505+00:00
---

# Join GKE Windows Server nodes automatically to a Managed Microsoft AD domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Join GKE Windows Server nodes automatically to a Managed Microsoft AD domain Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to join Windows Server nodes in your Google Kubernetes Engine (GKE) cluster to a Managed Microsoft AD domain using the [automated domain join](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce) feature.

## How Managed Microsoft AD joins Windows Server nodes automatically to a domain

When you create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) in your [GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), you can use the ready-made scripts that are available from Managed Microsoft AD to automatically join your Managed Microsoft AD domain. After GKE creates the node pool, Managed Microsoft AD initiates the domain join request and attempts to join the nodes with your domain. If the domain join request succeeds, Managed Microsoft AD joins the nodes to your domain. If the domain join request fails, the created nodes continue to run. You need to check the logs to identify and fix the issue before creating the node pool again. For more information, see [View debug logs](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#view-logs).

You need to clean up the information about unjoined nodes manually from Managed Microsoft AD in some specific scenarios. For more information, see [Clean up unjoined VMs](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#cleanup-vm).

You can't update an existing node pool with the domain join scripts to automatically join the existing nodes to your domain.

The automated domain join feature doesn't configure the GKE nodes to run with [gMSA](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts) for authentication. However, you can manually [create a gMSA](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-gmsa) in Managed Microsoft AD and configure the GKE nodes to use the gMSA. For information about configuring gMSA for the GKE nodes, see [Configure gMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/).

## Before you begin

  1. [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).

  2. [Create a GKE cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows).

  3. Make sure that the Windows Server nodes run on a [Windows version that Managed Microsoft AD supports](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#windows-domain-join).

  4. [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering) between the Managed Microsoft AD domain and the nodes' network, or have both the Managed Microsoft AD domain and the nodes in the same network.

  5. Create a service account with the Google Cloud Managed Identities Domain Join (`roles/managedidentities.domainJoin`) IAM role on the project that has the Managed Microsoft AD domain. For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).

     * For more information about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role).

     * For information about creating a service account, see [Authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

  6. Set the full `cloud-platform` access scope on the Windows Server nodes. For more information, see [Authorization](https://docs.cloud.google.com/compute/docs/access/service-accounts#authorization).




## Metadata

You need the following metadata keys to join your Windows Server nodes to a domain.

  * `windows-startup-script-url`
  * `managed-ad-domain`
  * Optional: `enable-guest-attributes`
  * Optional: `managed-ad-ou-name`
  * Optional: `managed-ad-force`



For more information about these metadata keys, see [Metadata](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#metadata).

The domain join request fails when the computer account of a Windows Server node already exists in Managed Microsoft AD. For Managed Microsoft AD to reuse the existing computer account during the domain join process, you can use the `managed-ad-force` metadata key when you [create the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add).

## Join Windows Server nodes

You can configure these [metadata keys](https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke#metadata) when you add a Windows Server node pool to your GKE cluster. This section illustrates how to use these metadata keys in gcloud CLI commands when you create a node pool.

However, you can use these metadata keys when you create a node pool using the other available options as well. For more information, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

To create a node pool and join the Windows Server nodes, run the following gcloud CLI command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        "--metadata=windows-startup-script-url=URL,managed-ad-domain=DOMAIN_RESOURCE_PATH,managed-ad-force=TRUE" \
        --service-account=SERVICE_ACCOUNT \
        --image-type=WINDOWS_IMAGE_NAME \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --location=ZONE_OR_REGION \
        --no-enable-autoupgrade
    

You can replace the placeholders in the `--metadata` flag with relevant values as described in the [metadata](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#metadata) section.

For more information about this gcloud CLI command, see [gcloud container node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create).

## What's next

  * [Join a Windows VM automatically to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
