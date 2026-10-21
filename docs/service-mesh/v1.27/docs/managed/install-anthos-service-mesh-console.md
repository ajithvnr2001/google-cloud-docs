---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/install-anthos-service-mesh-console/
title: Quickstart: Provision managed Cloud Service Mesh on a GKE cluster in the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:32.725107+00:00
---

# Quickstart: Provision managed Cloud Service Mesh on a GKE cluster in the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/install-anthos-service-mesh-console/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Provision managed Cloud Service Mesh on a GKE cluster in the Google Cloud console

Cloud Service Mesh is Google's service mesh offering, based on open source [Istio](https://istio.io/). The Cloud Service Mesh feature in the GKE UI allows users to easily provision [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview#managed_anthos_service_mesh) on a new GKE cluster or an existing GKE cluster. With managed Cloud Service Mesh Google hosts and manages the control plane and, optionally, the data plane for the mesh and handles its upgrades, scaling, and security in a backward-compatible manner.

Cloud Service Mesh provides a uniform way to connect, manage, and secure microservices. It supports managing traffic flows between services, enforcing access policies, and aggregating telemetry data, all without requiring changes to the microservice code. Cloud Service Mesh also provides a set of management capabilities to simplify lifecycle management of the mesh.

You configure Istio access control, routing rules, and other features by using a custom Kubernetes API, either via kubectl or the Istio command-line tool istioctl, which provides extra validation.

For more information, see [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Provision Cloud Service Mesh

The steps required to provision Cloud Service Mesh depend on whether you are creating a new GKE cluster or provisioning Cloud Service Mesh on an existing GKE cluster.

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

### Create a GKE cluster with Cloud Service Mesh

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=servicemesh--servicemesh_ui_autopilot_start)

* * *

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. Click **Configure** next to your preferred option between GKE Standard and GKE Autopilot.




### Standard

In the **Cluster basics** section, complete the following:

  1. Enter the **Name** for your cluster.
  2. For the **Location type** , select **Regional** , and then select the desired [region](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/supported-features-mcp#regions) for your cluster.

**Important:** We support > 90% of GKE cluster regions, but there are a few that are still not supported. See [Regions](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/supported-features-mcp#regions) for a full list of supported regions.
  3. From the navigation pane, under **Cluster** , click **Features**.

  4. In the **Cloud Service Mesh** section, check the box next to **Enable Cloud Service Mesh**.

After you check the box, a screen detailing the requirements appears. The requirements include:

     * **[Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/gke)** is enabled on the cluster.
     * Cloud Service Mesh uses Cloud Monitoring to provide automatic telemetry and logs.
     * **[Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)** is enabled on the cluster.
     * Cloud Service Mesh uses Workload Identity to provide secure access to required Google APIs and resources.
     * In order to secure, monitor, and manage the service mesh, the [`mesh.googleapis.com` API](https://docs.cloud.google.com/service-mesh/v1.27/docs/unified-install/project-cluster-setup#required_apis) is enabled (if it hasn't been already).

     * The Cluster is registered to the [project's Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the [Cloud Service Mesh Fleet feature](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components) is enabled.

     * The managed control plane is provisioned and set up to use a revision that matches the GKE channel configured on the cluster.

  5. Click **Make changes** to automatically enable the requirements.

  6. Click **Create**.




### Autopilot

In the **Cluster basics** section, complete the following:

  1. Enter the **Name** for your cluster.
  2. Select the desired **Region** for your cluster.

**Important:** We support > 90% of GKE cluster regions, but there are a few that are still not supported. See [Regions](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/supported-features-mcp#regions) for a full list of supported regions.
  3. Expand the **Advanced Options** section dropdown.

  4. In the **Cloud Service Mesh** section, check the box next to **Enable Cloud Service Mesh**.

After you check the box, a screen detailing the requirements appears. The requirements include:

     * In order to secure, monitor, and manage the service mesh, the [`mesh.googleapis.com` API](https://docs.cloud.google.com/service-mesh/v1.27/docs/unified-install/project-cluster-setup#required_apis) is enabled (if it hasn't been already).

     * The Cluster is registered to the [project's Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the [Cloud Service Mesh Fleet feature](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components) is enabled.

     * The managed control plane is provisioned and set up to use a revision that matches the GKE channel configured on the cluster.

  5. Click **Make changes** to automatically enable the requirements.

  6. Click **Create**.




### Provision Cloud Service Mesh on an existing GKE cluster

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Select the cluster that you would like to provision Cloud Service Mesh on.

  3. In the **Features** section, click the edit button next to Cloud Service Mesh.

After you click the edit button, a screen detailing the requirements will appear. The requirements include:

     * **[Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/gke)** is enabled on the cluster.

       * Cloud Service Mesh uses Cloud Monitoring to provide automatic telemetry and logs.
     * **[Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)** is enabled on the cluster.

       * Cloud Service Mesh uses Workload Identity to provide secure access to required Google APIs and resources.
     * In order to secure, monitor, and manage the service mesh, the [`mesh.googleapis.com` API](https://docs.cloud.google.com/service-mesh/v1.27/docs/unified-install/project-cluster-setup#required_apis) is enabled (if it hasn't been already).

     * The Cluster is registered to the [project's Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the [Cloud Service Mesh Fleet feature](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components) is enabled (if it hasn't been already).

     * The managed control plane is provisioned and set up to use a revision that matches the GKE channel configured on the cluster.

  4. Click **Make changes** to automatically enable the requirements.




## Next steps

Enabling Cloud Service Mesh on your cluster is only the first step. To fully take advantage of service mesh functionality, complete the following tasks:

  1. (Required) [Inject sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.27/docs/anthos-service-mesh-proxy-injection) to enhance network security, reliability and observability.

  2. (Highly recommended) [Deploy gateways](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/gateways#deploy_gateways) to manage ingress and egress traffic.

  3. (Highly recommended) [Configuring transport security](https://docs.cloud.google.com/service-mesh/v1.27/docs/security/configuring-mtls) to secure your mesh.

  4. (Optional) [Enable Managed Data Plane](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/provision-managed-anthos-service-mesh#apply_the_google-managed_data_plane_optional) to automatically upgrade the proxies.




## Troubleshooting

To address problems when provisioning Cloud Service Mesh, see [Resolving issues enabling Cloud Service Mesh through Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-ui-onboarding).

## What's next

  * To find out more about Managed Cloud Service Mesh, see [Provisioning managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/provision-managed-anthos-service-mesh)
  * For a quick introduction to the gcloud CLI used in this tutorial, see [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference)
  * To find out how to explore Cloud Service Mesh in the Google Cloud console, see [Exploring Cloud Service Mesh in the Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.27/docs/observability/explore-dashboard)
  * To explore Cloud Service Mesh optional features, such as Cloud Trace, distroless proxy images, and end user authentication, see [Enable optional features on managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/managed/enable-managed-anthos-service-mesh-optional-features)
  * To learn more about Security in Cloud Service Mesh, see [Cloud Service Mesh Security Overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/security/security-overview) and [Cloud Service Mesh Security Best Practices](https://docs.cloud.google.com/service-mesh/v1.27/docs/security/anthos-service-mesh-security-best-practices)
  * To find out more about Telemetry in Cloud Service Mesh, see [Observability Overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/observability-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
