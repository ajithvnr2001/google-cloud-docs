---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-for-envoy-setup/
title: Prepare to set up Cloud Service Mesh with Envoy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:58.157764+00:00
---

# Prepare to set up Cloud Service Mesh with Envoy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-for-envoy-setup/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare to set up Cloud Service Mesh with Envoy

Setting up Cloud Service Mesh includes the following phases:

  1. Granting permissions, enabling the Traffic Director API, and—if you are using Compute Engine—configuring Cloud DNS.
  2. Deploying your applications with Envoy proxies.
  3. Creating services and routing rules that determine how traffic travels through your service mesh.



This document describes the first phase, and applies when you are using the older APIs. The second and third phases are covered by the platform-specific guides listed in Continue the setup process later in this document.

Before you read this guide, familiarize yourself with the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh//legacy/load-balancing-apis/overview). If you are using the service routing APIs, review the [service routing APIs overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview).

## Prerequisites

Whether you plan to use Cloud Service Mesh to configure Envoy proxies running alongside applications on virtual machine (VM) instances, containers, or a mix of both, you need to first complete the following tasks:

  1. Enable billing.
  2. Decide how you want to install Envoy.
  3. Grant the required permissions.
  4. Enable the Traffic Director API for your project.
  5. If you are using Compute Engine, enable the Cloud DNS API and configure Cloud DNS.
  6. Ensure that the service account used by the Envoy proxies has sufficient permissions to access the Traffic Director API.



The following sections provide instructions for each task.

### Enable billing

Make sure that billing is enabled for your Google Cloud project. For more information, see [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

### Decide how to install Envoy

Cloud Service Mesh lets you install Envoy proxies and manage this infrastructure layer:

  * On Compute Engine, you can automatically add Envoy to applications running on your VMs. You use a VM template that installs Envoy, connects it to Cloud Service Mesh, and configures your VM's networking.

  * On Google Kubernetes Engine (GKE), you can automatically add Envoy sidecar proxies to your services' Pods. You install an Envoy sidecar injector to your cluster, which adds Envoy sidecar proxies, connects them to Cloud Service Mesh, and configures your container's networking.


**Note:** If you need to use your own Envoy binary, you can set up your data plane manually as well. This is a more advanced use case that is supported with Cloud Service Mesh, but it's slightly more complex. For help with manual setup, see our example guides.

Finally, you can also use Envoy deployment solutions from third-party providers with Cloud Service Mesh. One example of such an offering is [GetEnvoy](https://www.getenvoy.io/blog/using-getenvoy-with-traffic-director/), which provides a package manager-based approach to installing and updating your Envoy proxies.

#### About Envoy versioning

Envoy must be version 1.9.1 or later to work with Cloud Service Mesh. We recommend always using the most recent Envoy version to ensure that known security vulnerabilities are mitigated.

If you decide to deploy Envoy by using one of our automated methods, we handle this task for you as follows:

  * When you use automated Envoy deployment with Compute Engine VMs, the Envoy version installed is one that we have validated to work with Cloud Service Mesh. When a new VM is created by using the instance template, the VM receives the latest version that we have validated. If you have a long-running VM, you can [use a rolling update to replace your existing VMs and pick up the latest version](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-vms-options#using_the_managed_instance_group_update_process).

  * When you use the Envoy sidecar injector with GKE, the injector is configured to use a recent version of Envoy that we have validated to work with Cloud Service Mesh. When a sidecar is injected alongside your workload Pod, it receives this version of Envoy. If you want to pick up a more recent version of Envoy, [update the Envoy sidecar injector](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto#installing_the_envoy_sidecar_injector).




For information about specific Envoy versions, see [Version history](https://www.envoyproxy.io/docs/envoy/latest/version_history/version_history#version-history). For information about security vulnerabilities, see [Security Advisories](https://github.com/envoyproxy/envoy/security/advisories?state=published).

### Grant the required IAM permissions

You must have sufficient Identity and Access Management (IAM) permissions to create VM instances and modify a network to configure Cloud Service Mesh. If you have the role of project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`) in the project where you are enabling Cloud Service Mesh, you automatically have the correct permissions.

Otherwise, you must have all of the Compute Engine IAM roles shown in the following table. If you have these roles, you also have their associated permissions, as described in the [Compute Engine IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Set IAM policy for a service account. | [Service Account Admin](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountAdmin)   
(`roles/iam.serviceAccountAdmin`)  
Enable Cloud Service Mesh. | [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage)   
(`roles/serviceusage.serviceUsageAdmin`)  
Create networks, subnets, and load balancer components. | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)   
(`roles/compute.networkAdmin`)  
Add and remove firewall rules. | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)   
(`roles/compute.securityAdmin`)  
Create instances. | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)   
(`roles/compute.instanceAdmin`)  
  
The GKE node pool or Compute Engine VMs must have the [`https://www.googleapis.com/auth/cloud-platform`](https://www.googleapis.com/auth/cloud-platform) scope. For more information, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/docs/troubleshooting#proxies-do-not-connect-to-traffic-director).

With xDS v3, grant the service account used by Cloud Service Mesh Envoy clients the role `roles/trafficdirector.client`.

### Enable the Traffic Director API

###  Console 

  1. In the Google Cloud console, go to the **API Library** page for your project.

[Go to the API Library](https://console.cloud.google.com/project/_/apis/library)

  2. In the **Search for APIs & Services** field, enter `Traffic Director`.

  3. In the search results list, click **Traffic Director API**. If you don't see the Traffic Director API listed, that means that you don't have the necessary permissions to enable the Traffic Director API.

  4. On the **Traffic Director API** page, click **Enable**.




###  gcloud 

Run the following command:
    
    
    gcloud services enable trafficdirector.googleapis.com
    

### Enable the Cloud DNS API and configure Cloud DNS

Use these instructions if you are configuring Cloud Service Mesh on Compute Engine. You must enable the Cloud DNS API and configure Cloud DNS for DNS name resolution.

For background information about Cloud Service Mesh and DNS resolution, see [Cloud Service Mesh and DNS name resolution](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/dns).

First, use the following instructions to enable the Cloud DNS API.

###  Console 

  1. In the Google Cloud console, go to the **API Library** page for your project.

[Go to the API Library](https://console.cloud.google.com/project/_/apis/library)

  2. In the **Search for APIs & Services** field, enter `DNS`.

  3. In the search results list, click **Cloud DNS API**. If you don't see the Cloud DNS API listed, that means that you don't have the necessary permissions to enable the Cloud DNS API.

  4. On the **Cloud DNS API** page, click **Enable**.




###  gcloud 

Run the following command:
    
    
    gcloud services enable dns.googleapis.com
    

Next, configure a Cloud DNS managed private zone. Use the instructions in [Create a private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone).

### Enable the service account to access the Traffic Director API

When you set up your data plane and connect it to Cloud Service Mesh, your xDS clients (for example, Envoy proxies) connect to the `trafficdirector.googleapis.com` xDS server. These xDS clients present a service account identity to the xDS server to ensure that communications between the data plane and the control plane are properly authorized:

  * For a Compute Engine VM, the xDS client uses the service account assigned to the VM.
  * For GKE, if `Workload Identity` is not enabled, the xDS client uses the service account assigned to the underlying GKE node.
  * If `Workload Identity` is enabled, the xDS client uses the Google service account that is bound to the Kubernetes service account that is assigned to the Pod.

**Note:** Unless you modify the configuration, Google Cloud uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

You need the following permissions. Only xDS v3 is supported. If you are using xDS v2, you must migrate to xDS v3. For information about how to migrate, see [Migrate from xDS v2 to xDS v3](https://docs.cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis#migrate_from_xds_v2_to_xds_v3).

When you use xDS v3, the service account used by your clients must have the `trafficdirector.networks.reportMetrics`, `trafficdirector.rateLimitDomains.reportMetrics` and `trafficdirector.networks.getConfigs` permissions. You can use the IAM [Traffic Director Client role](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.client) (`roles/trafficdirector.client`), which wraps these permissions.

###  Console 

  1. In the Google Cloud console, go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/project/_/iam-admin)

  2. Select your project.

  3. Identify the service account to which you want to add a role:

     * If the service account isn't already on the **Members** list, it doesn't have any roles assigned to it. Click **Add** and enter the email address of the service account.
     * If the service account is already on the **Members** list, it has existing roles. Select the service account, and then click the **Roles** tab.
  4. Expand the role. For the service account that you want to edit, click edit**Edit**.

  5. Select the **Other > Cloud Service Mesh Client** role.

  6. To apply the role to the service account, click **Save**.




###  gcloud 

Run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT \
        --member serviceAccount:SERVICE_ACCOUNT_EMAIL \
        --role=roles/trafficdirector.client
    

Replace the following:

  * `PROJECT`: enter `gcloud config get-value project`
  * `SERVICE_ACCOUNT_EMAIL`: the email associated with the service account



## Continue the setup process

Now that you completed the prerequisite steps, you can start to set up your service mesh.

  * [Advanced Cloud Service Mesh configuration options](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-setup).
  * [Configure Envoy bootstrap attributes](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/per-proxy-config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
