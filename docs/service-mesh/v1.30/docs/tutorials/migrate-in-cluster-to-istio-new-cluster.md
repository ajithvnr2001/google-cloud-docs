---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/tutorials/migrate-in-cluster-to-istio-new-cluster/
title: Migrate in-cluster to Istio on a new cluster \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:12.211002+00:00
---

# Migrate in-cluster to Istio on a new cluster  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/tutorials/migrate-in-cluster-to-istio-new-cluster/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate in-cluster to Istio on a new cluster

This tutorial shows you how to migrate an application from an existing Google Kubernetes Engine (GKE) cluster using **in-cluster Cloud Service Mesh** to a new GKE cluster using **open-source Istio**. You will leverage [edge-to-multi-cluster mesh](https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment) capabilities for seamless migration.

**Terminology note** : In this tutorial, **Cloud Service Mesh** refers to Google's in-cluster Cloud Service Mesh, and **Istio** refers to the open-source Istio service mesh.

In this tutorial, you will:

  1. Prepare your existing cluster with in-cluster Cloud Service Mesh for migration.
  2. Provision a new GKE cluster with Istio.
  3. Configure GKE multi-cluster Gateway API on a dedicated cluster and multi-cluster Services to set up routing to mesh ingress.
  4. Execute a canary deployment to split live HTTP traffic between Cloud Service Mesh and Istio.
  5. Complete final cutover to Istio and decommission in-cluster Cloud Service Mesh resources.



## Canary deployment

"Canary deployment" is a technique used in software engineering to test a new version of software or infrastructure before releasing it to all production users. It involves incrementally increasing the percentage of traffic sent to the new target version.

In this tutorial, you will set up a new cluster with Istio and incrementally shift user traffic to it. You will start by directing 0% of user traffic to the new cluster, then 50%, and, finally, 100% to the GKE cluster with Istio. In production environments, you can use smaller and more granular increments (for example, 1%, 5%, 10%, 25%, 50%, 100%). If at any point you notice that the new cluster exhibits errors or performance degradation, you can execute an immediate rollback by setting the traffic percentage back to 0% for the Istio cluster.

### Canary control plane versus canary cluster

There are two primary strategies for migrating between service mesh control planes:

  * **Canary cluster migration (Recommended)** : In this strategy, you create a new cluster in the same Google Cloud project and fleet as your existing cluster, install the target service mesh control plane (Istio) on it, and migrate workloads and ingress traffic to the new cluster.
  * **Canary control plane migration (Unsupported)** : In this strategy, you install the new control plane side-by-side on the same cluster where the initial control plane is installed. This mode of migration is not supported.



In this guide, you will follow the canary cluster migration strategy. Both clusters must reside in the same Google Cloud project

## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Multi-cluster Gateway & multi-cluster Services](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing/pricing)



When you finish this tutorial, you can avoid incurring ongoing costs by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select the Google Cloud project where your in-cluster Cloud Service Mesh is installed.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,multiclusterservicediscovery.googleapis.com)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,multiclusterservicediscovery.googleapis.com)




## Prepare the cluster using in-cluster Cloud Service Mesh for migration

In this section, you will prepare your existing GKE cluster running in-cluster Cloud Service Mesh for migration to a GKE cluster with Istio.

### Ensure in-cluster Cloud Service Mesh cluster is running and ready for migration

  1. Ensure your in-cluster Cloud Service Mesh cluster `GKE_CSM_CLUSTER` is running with the in-cluster `istiod` control plane following the [In-cluster Cloud Service Mesh installation guide](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/install-in-cluster-cloud-service-mesh).

Run the following command to check the installation status:
         
         kubectl get deployment -A -l app=istiod -L istio.io/rev
         

The expected output is similar to the following:
         
         NAMESPACE              NAME                 READY   UP-TO-DATE   AVAILABLE   AGE     REV
         ISTIOD_NAMESPACE      istiod-asm-1295-12   2/2     2            2           4d16h   asm-1295-12
         

  2. Verify there are no errors in the `istiod` control plane using the following command:
         
         kubectl logs -n ISTIOD_NAMESPACE -l app=istiod
         




### Make the cluster migration-ready

  1. Verify that [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is enabled on the cluster and node pool.

**Note:** If you installed Cloud Service Mesh using `asmcli` with the `--enable-workload-identity` or `--enable-all` flag, Workload Identity is already enabled on your cluster and node pool automatically, and you can skip this step.

To verify Workload Identity on the cluster, run the following command:
         
         gcloud container clusters describe "GKE_CSM_CLUSTER" \
             --location="LOCATION" \
             --project="PROJECT_ID" \
             --format="value(workloadIdentityConfig.workloadPool)"
         

Replace GKE_CSM_CLUSTER with your existing cluster name, LOCATION with your cluster location, and PROJECT_ID with your project ID.

Expected output:
         
         PROJECT_ID.svc.id.goog
         

If Workload Identity is missing, see the [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) guide to update your cluster.

  2. Verify your cluster is registered to the fleet:
         
         gcloud container clusters describe "GKE_CSM_CLUSTER" \
             --location="LOCATION" \
             --project="PROJECT_ID" \
             --format="yaml(fleet)"
         

Expected output for a registered cluster:
         
         fleet:
           membership: //gkehub.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/memberships/MEMBERSHIP_NAME
         

If fleet details are empty, see the [fleet membership registration guide](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster_on) to register your cluster with the fleet.

  3. Expose your application using an Ingress gateway by following the [Installing and upgrading gateway](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/gateways) guide.




## Install Istio on a new GKE cluster

In this section, you will provision a new GKE cluster running open-source Istio for the canary cluster migration strategy.

  1. Create a new GKE cluster `GKE_ISTIO_CLUSTER` in the same Google Cloud project (`PROJECT_ID`) as your existing in-cluster Cloud Service Mesh cluster.

**Note:** Both clusters must reside in the same Google Cloud project and be registered to the same fleet. Multi-cluster Gateway and multi-cluster Services (MCS) rely on a shared fleet in the same project to discover service endpoints (`ServiceImport`) and route live traffic across both clusters during migration. This same-project configuration is the officially supported approach for this migration.

When creating the cluster, ensure that you specify `--project` and enable Workload Identity using `--workload-pool=PROJECT_ID.svc.id.goog`:
         
         gcloud container clusters create GKE_ISTIO_CLUSTER \
             --project=PROJECT_ID \
             --location=LOCATION \
             --workload-pool=PROJECT_ID.svc.id.goog
         

If you have already created a cluster, use the [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) guide to enable Workload Identity.

  2. Register your Istio cluster with the fleet:
         
         gcloud container fleet memberships register \
             GKE_ISTIO_CLUSTER \
             --gke-cluster=LOCATION/GKE_ISTIO_CLUSTER \
             --enable-workload-identity \
             --location=LOCATION \
             --project=PROJECT_ID
         

  3. Install Istio following the official [Istio Installation Guide](https://istio.io/latest/docs/setup/getting-started/) with [ingress gateways](https://istio.io/latest/docs/setup/additional-setup/gateway/) deployed for ingress traffic. For a smoother migration, we recommend installing the same version of open-source Istio. If you decide to upgrade open-source Istio, review Istio's [release notes](https://istio.io/latest/news/releases/) for any behavioral changes.

Set up this cluster by installing your applications in the same way as on the GKE cluster using in-cluster Cloud Service Mesh. This guide references the namespace hosting ingress gateways as `ISTIO_INGRESS_NAMESPACE`.

  4. Ensure the cluster is healthy and ready to serve traffic. Application teams are responsible for confirming that all microservices are running cleanly and passing health checks before routing live user traffic.




## Configure multi-cluster Gateway API on a dedicated cluster

In this section, you will configure an external Application Load Balancer (L7XLB) through the GKE Gateway controller to enable ingress traffic to the mesh. During migration, we recommend deploying Gateway API resources on a dedicated GKE config cluster to manage the load balancer. This guide refers to this dedicated config cluster as `GKE_CONFIG_CLUSTER`.

### Prepare the config cluster

Prepare the config cluster to host `Gateway` and `HTTPRoute` APIs by following the [multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-external-multi-cluster-gateway) guide.

### Export Services using multi-cluster Services

Export the `istio-ingressgateway` Service on both mesh clusters using `ServiceExport` as directed in the [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#registering_a_service_for_export) (MCS) guide:

**Note:** Applying `ServiceExport` causes the GKE MCS controller to automatically provision Google Cloud Network Endpoint Groups (NEGs) for the ingress gateway pods.
    
    
    apiVersion: net.gke.io/v1
    kind: ServiceExport
    metadata:
      namespace: NAMESPACE
      name: SERVICE_EXPORT_NAME
    

### Provision Gateway API resources on the config cluster

  1. Follow the [Gateway Edge-to-Mesh guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-external-multi-cluster-gateway#edge-to-mesh) to create the `Gateway` and `HTTPRoute` resources on your dedicated config cluster. A sample configuration looks like the following:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: global-gateway
           namespace: CSM_INGRESS_NAMESPACE
         spec:
           gatewayClassName: gke-l7-global-external-managed-mc
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               namespaces:
                 from: Same
         ---
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: edge-to-mesh-route
           namespace: CSM_INGRESS_NAMESPACE
         spec:
           parentRefs:
           - name: global-gateway
           rules:
           - backendRefs:
             # Backend 1: Cloud Service Mesh Cluster (CSM_INGRESS_NAMESPACE namespace)
             - group: net.gke.io
               kind: ServiceImport
               name: istio-ingressgateway
               namespace: CSM_INGRESS_NAMESPACE
               port: 80
               weight: 100
         

  2. If your `ServiceImport` resources reside in a different namespace than `HTTPRoute`, use [`ReferenceGrant`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#referencegrant) to enable cross-namespace traffic routing:
         
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: ReferenceGrant
         metadata:
           name: allow-csm-ingress-to-ISTIO_INGRESS_NAMESPACE
           namespace: ISTIO_INGRESS_NAMESPACE
         spec:
           from:
           - group: gateway.networking.k8s.io
             kind: HTTPRoute
             namespace: CSM_INGRESS_NAMESPACE
           to:
           - group: net.gke.io
             kind: ServiceImport
         




## Migrate traffic using canary deployment

In this section, you will shift traffic to the new cluster and complete the migration.

### Shift 50% traffic to Istio

In this section, you will execute a canary deployment to slowly migrate traffic. For more information, see the [traffic splitting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gateway-traffic-splitting) guide.

  1. Apply the `HTTPRoute` custom resource in the config cluster to split canary traffic to the Istio cluster:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: edge-to-mesh-route
           namespace: CSM_INGRESS_NAMESPACE
         spec:
           parentRefs:
           - name: global-gateway
           rules:
           - backendRefs:
             # Backend 1: CSM Cluster (CSM_INGRESS_NAMESPACE namespace)
             - group: net.gke.io
               kind: ServiceImport
               name: istio-ingressgateway
               namespace: CSM_INGRESS_NAMESPACE
               port: 80
               weight: 50
             # Backend 2: Istio Cluster (ISTIO_INGRESS_NAMESPACE namespace)
             - group: net.gke.io
               kind: ServiceImport
               name: istio-ingressgateway
               namespace: ISTIO_INGRESS_NAMESPACE
               port: 80
               weight: 50
         

  2. Validate live traffic distribution by executing parallel requests against the Gateway public IP address.

_Expected output_ : Responses are load-balanced across both `GKE_CSM_CLUSTER` and `GKE_ISTIO_CLUSTER`.

In production, as noted earlier, migrate traffic in smaller increments (for example, 1%, 5%, 10%, 25%, 50%, 100%). It can take some time for these weight increments to propagate fully to the load balancer, so verify that traffic is correctly split before incrementing further.




### Complete migration to the Istio cluster

Verify that the application on the Istio cluster operates correctly under canary traffic and all traffic has shifted toward it. After confirming that traffic routing is functioning properly, complete the migration by deleting the `ServiceExport` resource on the in-cluster Cloud Service Mesh cluster:
    
    
    kubectl --context="GKE_CSM_CLUSTER_CONTEXT" delete serviceexport.net.gke.io istio-ingressgateway -n CSM_INGRESS_NAMESPACE
    

The GKE Gateway controller automatically detaches the Network Endpoint Group (NEG) of the Cloud Service Mesh cluster from the Google Cloud load balancer backend service. All incoming client traffic transitions seamlessly to the Istio cluster with zero downtime.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, clean up the deployed components.

  1. Delete `ServiceExport` resources on the Istio cluster:
         
         kubectl --context="GKE_ISTIO_CLUSTER_CONTEXT" delete serviceexport.net.gke.io istio-ingressgateway -n ISTIO_INGRESS_NAMESPACE
         

  2. Unregister fleet memberships:
         
         gcloud container fleet memberships unregister \
             GKE_CSM_CLUSTER \
             --gke-cluster="LOCATION/GKE_CSM_CLUSTER" \
             --project="PROJECT_ID"
         

  3. Delete the in-cluster Cloud Service Mesh cluster:
         
         gcloud container clusters delete GKE_CSM_CLUSTER \
             --location="LOCATION" \
             --project="PROJECT_ID"
         




## What's next

  * Read the foundational architecture guide: [From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service Mesh](https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment).
  * Learn more about [multi-cluster Gateway API patterns](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-gateways).
  * Learn more about [multi-cluster load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).
  * Explore [Istio Mesh Traffic Management Documentation](https://istio.io/latest/docs/concepts/traffic-management/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
