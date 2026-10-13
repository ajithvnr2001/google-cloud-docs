---
url: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/provision-managed-anthos-service-mesh-asmcli/
title: Provision managed Cloud Service Mesh with asmcli \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:04.355300+00:00
---

# Provision managed Cloud Service Mesh with asmcli  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/provision-managed-anthos-service-mesh-asmcli/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Provision managed Cloud Service Mesh with asmcli

**Deprecated:** Provisioning managed Cloud Service Mesh with asmcli will be deprecated on **Aug 22, 2024** and support will end in **February 2025**. This change only affects Google Cloud clusters. Off-Google Cloud clusters will continue to use asmcli as normal.

## Overview

Managed Cloud Service Mesh with `asmcli` is a managed control plane and a managed data plane that you simply configure. Google handles their reliability, upgrades, scaling and security for you in a backward-compatible manner. This guide explains how to set up or migrate applications to managed Cloud Service Mesh in a single or multi-cluster configuration with `asmcli`.

**Note:** We recommend the [fleet feature API option to configure managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh), but you can also use this guide to configure managed Cloud Service Mesh using the `asmcli` tool.

To learn about the supported features and limitations of managed Cloud Service Mesh, see [Managed Cloud Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp).

## Prerequisites

As a starting point, this guide assumes that you have:

  * [A Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)
  * [A Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * Obtained the [required permissions](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#roles-required) to provision Cloud Service Mesh
  * The `asmcli` installation tool, `kpt`, and other tools specified in [Install the required tools](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-dependent-tools#install_required_tools)

For a faster provisioning, your clusters must have [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled. If Workload Identity isn't enabled, the provision will automatically enable it. 




## Requirements

  * One or more clusters with a [supported version of GKE](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp#environments), in one of the supported [regions](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp#regions).
  * Note that managed Cloud Service Mesh uses GKE release channels to balance between stability and upgrade speed. New changes to Cloud Service Mesh in-cluster components (including CNI, MDPC, proxies, and Istio CRDs) will rollout to clusters that subscribe GKE rapid channel first. They will then be promoted to GKE regular channel, and finally the GKE stable channel, once they demonstrate enough stability. 
    * Best practice is to provision a subset of your fleet clusters in an earlier GKE release channel to ensure they receive updates to the Cloud Service Mesh components first.
    * Managed Cloud Service Mesh doesn't support changing GKE release channels.
    * If you do change the GKE release channel, Cloud Service Mesh won't prevent the operation. Cloud Service Mesh automatically updates the in-cluster components (CNI, MDPC, default injected proxy version and Istio CRDs) to align with the current GKE release channel.
  * Ensure that your cluster has enough capacity for the required components that managed Cloud Service Mesh installs in the cluster. 
    * The `mdp-controller` deployment in `kube-system` namespace requests cpu: 50m, memory: 128Mi.
    * The `istio-cni-node` daemonset in `kube-system` namespace requests cpu: 100m, memory: 100Mi on each node.
  * Ensure that the organizational policy `constraints/compute.disableInternetNetworkEndpointGroup` is disabled. If the policy is enabled, ServiceEntry may not work.
  * Ensure that the client machine that you provision managed Cloud Service Mesh from has network connectivity to the API server. 
  * Your clusters must be [registered to a fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/register/gke). This step can be done separately prior to the provision or as part of the provision by passing the `--enable-registration` and `--fleet-id` flags. 
  * Your project must have the Service Mesh fleet feature enabled. You could enable it as part of the provision by passing `--enable-gcp-components`, or by running the following command:
        
        gcloud container fleet mesh enable --project=FLEET_PROJECT_ID
        

where FLEET_PROJECT_ID is the project-id of the fleet host project. 

  * GKE Autopilot is only supported with GKE version 1.21.3+.

  * Cloud Service Mesh can use multiple GKE clusters in a single-project single-network environment or a multi-project single-network environment.

    * If you join clusters that are not in the same project, they must be registered to the same [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the clusters must be in a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) configuration together on the same network.
    * For a single-project multi-cluster environment, the fleet project can be the same as the cluster project. For more information about fleets, see [Fleets Overview](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview).
    * For a multi-project environment, we recommend that you host the fleet in a separate project from the cluster projects. If your organizational policies and existing configuration allow it, we recommend that you use the shared VPC project as the fleet host project. For more information, see [Setting up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc). 
    * If your organization uses VPC Service Controls _and_ you are provisioning Cloud Service Mesh on GKE clusters with a release greater or equal to 1.22.1-gke.10, then you may need to take additional configuration steps: 
      * If you are provisioning Cloud Service Mesh on the _regular or stable_ [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel), then you **must use the additional`--use-vpcsc` flag** when applying the managed control plane and follow the [VPC Service Controls (preview) guide](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc). Otherwise, the provision will fail security controls.
      * If you are provisioning Cloud Service Mesh on the _rapid_ [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel), then you **do not need to use the additional`--use-vpcsc` flag** when applying the managed control plane, but you do need to follow the [VPC Service Controls (GA) guide](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc-ga). 



## Roles required to install Cloud Service Mesh

The following table describes the roles that are required to install managed Cloud Service Mesh.

**Role name** | **Role ID** | **Grant location** | **Description**  
---|---|---|---  
GKE Hub Admin | roles/gkehub.admin | Fleet project | Full access to GKE Hubs and related resources.  
Service Usage Admin | roles/serviceusage.serviceUsageAdmin | Fleet project | Ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project. (Note 1)  
CA Service Admin [Beta](https://cloud.google.com/products#product-launch-stages) | roles/privateca.admin | Fleet project | Full access to all CA Service resources. (Note 2)  
  
## Roles required to run Cloud Service Mesh

The following table describes the roles that are required by the service account to run managed Cloud Service Mesh. If your network or cluster projects differ from the fleet host project, you need to give the service account in the fleet project access to these roles in the other projects.

**Role name** | **Role ID** | **Grant location** | **Description**  
---|---|---|---  
Anthos Service Mesh Service Agent | roles/anthosservicemesh.serviceAgent | Fleet project |   
Mesh Managed Control Plane Service Agent (legacy) | roles/meshcontrolplane.serviceAgent | Fleet project | This is a legacy role that was part of older installations of Cloud Service Mesh. If your installation has this service role, you can leave it as is. New installations don't need this role.  
  
## Limitations

**Caution:** Note the following fleet-specific limitations: \- All clusters in a particular Cloud Service Mesh must be registered to the same fleet. The clusters cannot be registered to different fleets. \- All clusters in a project that includes a Cloud Service Mesh cluster must be registered to the same fleet.

We recommend that you review the list of [Cloud Service Mesh supported features and limitations](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp). In particular, note the following:

  * Workload pods running with [`hostNetwork: true`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#podspec-v1-core) are not supported.

  * The `IstioOperator` API isn't supported since its main purpose is to control in-cluster components.

**Note:** You can still enable optional features without using the IstioOperator API, see [Enabling optional features on managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed-service-mesh-optional-features).


  * For GKE Autopilot clusters, cross-project setup is only supported with GKE 1.23 or later.

  * For GKE Autopilot clusters, in order to adapt to the [GKE Autopilot resource limit](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#default_contaizner_resource_requests), the default proxy resource requests and limits are set to 500m CPU and 512 Mb memory. You can override the default values using custom injection.

  * For GKE Autopilot clusters, there may be warnings for Cloud Service Mesh components "DaemonSet has no nodes selected" until the clusters' NodePool scales.

  * During the provisioning process for a managed control plane, Istio CRDs are provisioned in the specified cluster. If there are existing Istio CRDs in the cluster, they will be overwritten.

  * [Istio CNI](https://istio.io/latest/docs/setup/additional-setup/cni/) and Traffic Director are not compatible with GKE Sandbox. Therefore, managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` implementation does not support clusters with GKE Sandbox enabled.

  * The `asmcli` tool must have access to the Google Kubernetes Engine (GKE) endpoint. You can configure access through a ["jump" server](https://en.wikipedia.org/wiki/Jump_server), such as a Compute Engine VM within the Virtual Private Cloud (VPC) giving specific access.




## Before you begin

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

### Configure gcloud

Complete the following steps even if you are using Cloud Shell.

  1. Authenticate with the Google Cloud CLI:
         
         gcloud auth login --project PROJECT_ID
         

where PROJECT_ID is the unique identifier of your cluster project. Run the following command to get your PROJECT_ID:
         
         gcloud projects list --filter="<PROJECT ID>" --format="value(PROJECT_NUMBER)"
            ```
         

  2. Update the components:
         
         gcloud components update
         

  3. Configure `kubectl` to point to the cluster.

**Note:** Use `--region` instead of `--zone`, if the cluster is a regional cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
              --zone CLUSTER_LOCATION \
              --project PROJECT_ID
         




### Download the installation tool

**Important:** The `asmcli` tool only supports Linux operating systems.

  1. Download the **latest** version of the tool to the current working directory:
         
         curl https://storage.googleapis.com/csm-artifacts/asm/asmcli > asmcli
         

  2. Make the tool executable:
         
         chmod +x asmcli
         




## Configure each cluster

Use the following steps to configure managed Cloud Service Mesh for each cluster in your mesh.

### Apply the managed control plane

**Note:** Alternatively, you can use the fleet API and `gcloud` instead of `asmcli` to set up managed Cloud Service Mesh. For more information, see [Configure managed Cloud Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet).

Before you apply the managed control plane, you must [select a release channel](https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/select-a-release-channel#how_to_select_a_release_channel). Your Cloud Service Mesh channel is determined by your GKE cluster channel at time of provisioning managed Cloud Service Mesh. Note that multiple channels in the same cluster at the same time is not supported.

Run the installation tool for each cluster that will use managed Cloud Service Mesh. We recommend that you include both of the following options:

**Warning:** The following options are **required**. For a full list of options, see the [`asmcli` reference page](https://docs.cloud.google.com/service-mesh/docs/unified-install/reference).

  * `--enable-registration --fleet_id FLEET_PROJECT_ID` These two flags register the cluster to a fleet, where the FLEET_ID is the project-id of the fleet host project. If using a single-project, the FLEET_PROJECT_ID is the same as PROJECT_ID, the fleet host project and the cluster project are the same. In more complex configurations like multi-project, we recommend using a separate fleet host project.

  * `--enable-all`. This flag enables both required components and registration.




The `asmcli` tool configures the managed control plane directly using tools and logic inside of the CLI tool. Use the set of instructions below depending on your [preferred CA](https://docs.cloud.google.com/service-mesh/docs/unified-install/plan-install#choose_a_certificate_authority).

**Warning:** For Cloud Service Mesh to function correctly, you will deploy an `istio-cni-node` DaemonSet to your nodes with elevated [role-based access control (RBAC) permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb), such as the ability to modify all deployments and create configmaps. These permissions are required for `istio-cni-node` to manage the pod lifecycle and configuration.

#### Certificate Authorities

Select a Certificate Authority to use for your mesh.

### Mesh CA

Run the following command to install the control plane with default features and Mesh CA. Enter your values in the provided placeholders.
    
    
      ./asmcli install \
          -p PROJECT_ID \
          -l LOCATION \
          -n CLUSTER_NAME \
          --fleet_id FLEET_PROJECT_ID \
          --managed \
          --verbose \
          --output_dir DIR_PATH \
          --enable-all
    

### CA Service

  1. Follow the steps in [Configure Certificate Authority Service](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#configure).
  2. Run the following command to install the control plane with default features and [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). Enter your values in the provided placeholders.

**Note:** When using Certificate Authority Service as part of an MCP multi-cluster mesh, all clusters must have their respective subordinate CA pools chain to the same root CA pool. Otherwise, all of them will need to use the same CA pool.
    
    
      ./asmcli install \
          -p PROJECT_ID \
          -l LOCATION \
          -n CLUSTER_NAME \
          --fleet_id FLEET_PROJECT_ID \
          --managed \
          --verbose \
          --output_dir DIR_PATH \
          --enable-all \
          --ca gcp_cas \
          --ca_pool pool_name
    

The tool downloads all the files for configuring the managed control plane to the specified `--output_dir`, installing the `istioctl` tool and sample applications. The steps in this guide assume that you run `istioctl` from the `--output_dir` location you specified when running `asmcli install`, with `istioctl` present in its `<Istio release dir>/bin` subdirectory.

If you rerun `asmcli` on the same cluster, it overwrites the existing control plane configuration. Be sure to specify the same options and flags if you want the same configuration.

### Verify the control plane has been provisioned

After a few minutes, verify that the control plane status is `ACTIVE`:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

The output is similar to:
    
    
    membershipStates:
      projects/746296320118/locations/us-central1/memberships/demo-cluster-1:
        servicemesh:
          controlPlaneManagement:
            details:
            - code: REVISION_READY
              details: 'Ready: asm-managed'
            state: ACTIVE
          ...
        state:
          code: OK
          description: 'Revision(s) ready for use: asm-managed.'
    

If the status does not reach `ACTIVE`` in a few minutes, then refer to [Check the managed control plane status](https://docs.cloud.google.com/service-mesh/docs/managed/troubleshoot-managed-anthos-service-mesh#control_plane_status) for more information about possible errors.

### Zero-touch upgrades

Once the managed control plane is installed, Google will automatically upgrade it when new releases or patches become available.

## Managed data plane

If you use managed Cloud Service Mesh, Google fully manages upgrades of your proxies.

With the managed data plane feature enabled, the sidecar proxies and injected gateways are actively and automatically updated in conjunction with the managed control plane by restarting workloads to re-inject new versions of the proxy. This starts after the control plane has been upgraded and normally completes within 2 weeks after starting.

If [disabled](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/managed-data-plane#disable_the_managed_data_plane_optional), proxy management is done passively - driven by the natural lifecycle of the pods in the cluster and must be manually triggered by the user to control the update rate.

The managed data plane upgrades proxies by evicting pods that are running earlier versions of the proxy. The evictions are done gradually, honoring the pod disruption budget and controlling the rate of change.

For more information, see [Managed data plane](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/managed-data-plane).

## Configure endpoint discovery (only for multi-cluster installations)

If your mesh has only one cluster, skip these multi-cluster steps and proceed to Deploy applications or Migrate applications.

Before you continue, ensure that Cloud Service Mesh is configured on each cluster.

**Note:** For more information on endpoint discovery, refer to [Endpoint discovery with multiple control planes](https://istio.io/v1.31/docs/ops/deployment/deployment-models/#endpoint-discovery-with-multiple-control-planes).

### Public clusters

#### Configure endpoint discovery between public clusters

If you are operating on public clusters (non-private clusters), you can either [Configure endpoint discovery between public clusters](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gke-install-multi-cluster#configure_endpoint_discovery_between_clusters) or more simply [Enable endpoint discovery between public clusters](https://docs.cloud.google.com/service-mesh/docs/managed/multi-cluster#endpoint-discovery-declarative-api).

### Private clusters

#### Configure endpoint discovery between private clusters

When using GKE [private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept), you must configure the [cluster control plane endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#endpoints_in_private_clusters) to be the public endpoint instead of the private endpoint. Please refer to [Configure endpoint discovery between private clusters](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gke-install-multi-cluster#private-clusters-endpoint).

For an example application with two clusters, see [HelloWorld service example](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gke-install-multi-cluster#install_the_helloworld_service).

**Note:** The **HelloWorld service** example uses [Docker Hub](https://hub.docker.com/). In a private cluster, the container runtime can pull container images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) by default. The container runtime cannot pull images from any other container image registry on the internet. You can download the image and push to Artifact Registry or use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide outbound internet access for certain private nodes. For more information, see [Migrate external containers](https://docs.cloud.google.com/container-registry/docs/migrate-external-containers) and [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#pulling_images).

## Deploy applications

Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation).

### Managed (TD)

  1. Apply the default injection label to the namespace:


    
    
    kubectl label namespace NAMESPACE \
        istio.io/rev- istio-injection=enabled --overwrite
    

### Managed (Istiod)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    
      kubectl label namespace NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

  1. Run the following command to locate the available release channels:
         
         kubectl -n istio-system get controlplanerevision
         

The output is similar to the following:
         
         NAME                AGE
         asm-managed-rapid   6d7h
         

NOTE: If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

  2. Apply the revision label to the namespace:
         
         kubectl label namespace NAMESPACE \
             istio-injection- istio.io/rev=REVISION_LABEL --overwrite
         




Validate that the namespace label is applied correctly using the following command.
    
    
      kubectl get namespace -L istio-injection
    

Example output:
    
    
      NAME                 STATUS   AGE     ISTIO-INJECTION
      default              Active   5m9s    enabled
    

At this point, you have successfully configured managed Cloud Service Mesh. If you have any existing workloads in labeled namespaces, then restart them so they get proxies injected.

If you deploy an application in a multi-cluster setup, replicate the Kubernetes and control plane configuration in all clusters, unless you plan to limit that particular config to a subset of clusters. The configuration applied to a particular cluster is the source of truth for that cluster.

### Customize injection (optional)

You can override default values and customize injection settings but this can lead to unforeseen configuration errors and resulting issues with sidecar containers. Before you customize injection, read the information after the sample for notes on particular settings and recommendations.

Per-pod configuration is available to override these options on individual pods. This is done by adding an `istio-proxy` container to your pod. The sidecar injection will treat any configuration defined here as an override to the default injection template.

For example, the following configuration customizes a variety of settings, including lowering the CPU requests, adding a volume mount, and adding a `preStop` hook:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example
    spec:
      containers:
      - name: hello
        image: alpine
      - name: istio-proxy
        image: auto
        resources:
          requests:
            cpu: "200m"
            memory: "256Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
        volumeMounts:
        - mountPath: /etc/certs
          name: certs
        lifecycle:
          preStop:
            exec:
              command: ["sleep", "10"]
      volumes:
      - name: certs
        secret:
          secretName: istio-certs
    

In general, any field in a pod can be set. However, care must be taken for certain fields:

  * Kubernetes requires the `image` field to be set before the injection has run. While you can set a specific image to override the default one, we recommend that you set the `image` to `auto`, which will cause the sidecar injector to automatically select the image to use.
  * Some fields in `containers` are dependent on related settings. For example, must be less than or equal to the CPU limit. If both fields are not properly configured, the pod may fail to start.
  * Kubernetes lets you set both `requests` and `limits` for resources in your Pod `spec`. **GKE Autopilot** only considers `requests`. For more information, see [Setting resource limits in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#resource-limits).



Additionally, certain fields are configurable by annotations on the Pod, although it is recommended to use the above approach to customizing settings. Take additional care for the following annotations:

  * For GKE Standard, if `sidecar.istio.io/proxyCPU` is set, make sure to explicitly set `sidecar.istio.io/proxyCPULimit`. Otherwise the sidecar's CPU limit will be set as unlimited.
  * For GKE Standard, if `sidecar.istio.io/proxyMemory` is set, make sure to explicitly set `sidecar.istio.io/proxyMemoryLimit`. Otherwise the sidecar's memory limit will be set as unlimited.
  * For GKE Autopilot, configuring resource `requests` and `limits` using annotations might overprovision resources. Use the image template approach to avoid. See [Resource modification examples in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#examples).



For example, see the below resources annotation:
    
    
    spec:
      template:
        metadata:
          annotations:
            sidecar.istio.io/proxyCPU: "200m"
            sidecar.istio.io/proxyCPULimit: "200m"
            sidecar.istio.io/proxyMemory: "256Mi"
            sidecar.istio.io/proxyMemoryLimit: "256Mi"
    

### Verify control plane metrics

You can view the version of the control plane and data plane in Metrics Explorer.

To verify that your configuration works as expected:

  1. In the Google Cloud console, view the control plane metrics:

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesFilter%22:%7B%22filter%22:%22metric.type%3D%5C%22istio.io%2Fcontrol%2Fproxy_clients%5C%22%20resource.type%3D%5C%22k8s_container%5C%22%20resource.label.%5C%22container_name%5C%22%3D%5C%22cr-asm-managed%5C%22%22,%22minAlignmentPeriod%22:%2260s%22,%22unitOverride%22:%221%22,%22aggregations%22:%5B%7B%22perSeriesAligner%22:%22ALIGN_MEAN%22,%22crossSeriesReducer%22:%22REDUCE_SUM%22,%22groupByFields%22:%5B%22metric.label.%5C%22revision%5C%22%22,%22metric.label.%5C%22proxy_version%5C%22%22%5D%7D,%7B%22crossSeriesReducer%22:%22REDUCE_NONE%22%7D%5D%7D,%22targetAxis%22:%22Y1%22,%22plotType%22:%22LINE%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221h%22%7D%7D&_ga=2.261487630.2032095789.1614618451-1055500661.1611702119)

  2. Choose your workspace and add a custom query using the following parameters:

     * **Resource type** : Kubernetes Container
     * **Metric** : Proxy Clients
     * **Filter** : `container_name="cr-REVISION_LABEL"`
     * **Group By** : `revision` label and `proxy_version` label
     * **Aggregator** : sum
     * **Period** : 1 minute

When you run Cloud Service Mesh with both a Google-managed and an in-cluster control plane, you can tell the metrics apart by their container name. For example, managed metrics have `container_name="cr-asm-managed"`, while unmanaged metrics have `container_name="discovery"`. To display metrics from both, remove the Filter on `container_name="cr-asm-managed"`.

  3. Verify the control plane version and proxy version by inspecting the following fields in Metrics Explorer:

     * The **revision** field indicates the control plane version.
     * The **proxy_version** field indicates the `proxy_version`.
     * The **value** field indicates the number of connected proxies.

For the current channel to Cloud Service Mesh version mapping, see [Cloud Service Mesh versions per channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel).




## Migrate applications to managed Cloud Service Mesh

**Warning:** During the migration process, Istio CRDs are installed in the specified cluster. If there are existing Istio CRDs in the cluster, they will be overwritten.

### Prepare for migration

To prepare to migrate applications from in-cluster Cloud Service Mesh to managed Cloud Service Mesh, perform the following steps:

  1. Run the tool as indicated in the Apply the Google-managed control plane section.

  2. (Optional) If you want to use the Google-managed data plane, enable data plane management:
         
         kubectl annotate --overwrite controlplanerevision REVISION_TAG \
           mesh.cloud.google.com/proxy='{"managed":"true"}'
         




### Migrate applications

To migrate applications from in-cluster Cloud Service Mesh to managed Cloud Service Mesh, perform the following steps:

  1. Replace the current namespace label. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation).



### Managed (TD)

  1. Apply the default injection label to the namespace:


    
    
    kubectl label namespace NAMESPACE \
        istio.io/rev- istio-injection=enabled --overwrite
    

### Managed (Istiod)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    
      kubectl label namespace NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

  1. Run the following command to locate the available release channels:
         
         kubectl -n istio-system get controlplanerevision
         

The output is similar to the following:
         
         NAME                AGE
         asm-managed-rapid   6d7h
         

NOTE: If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

  2. Apply the revision label to the namespace:
         
         kubectl label namespace NAMESPACE \
             istio-injection- istio.io/rev=REVISION_LABEL --overwrite
         




  1. Perform a rolling upgrade of deployments in the namespace:
         
         kubectl rollout restart deployment -n NAMESPACE
         

  2. Test your application to verify that the workloads function correctly.

  3. If you have workloads in other namespaces, repeat the previous steps for each namespace.

  4. If you deployed the application in a multi-cluster setup, replicate the Kubernetes and Istio configuration in all clusters, unless there is a desire to limit that configuration to a subset of clusters only. The configuration applied to a particular cluster is the source of truth for that cluster.




If you are satisfied that your application works as expected, you can remove the in-cluster `istiod` after you switch all namespaces to the managed control plane, or keep them as a backup - `istiod` will automatically scale down to use fewer resources. To remove, skip to Delete old control plane.

If you encounter problems, you can identify and resolve them by using the information in [Resolving managed control plane issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-managed-service-mesh) and if necessary, roll back to the previous version.

### Delete old control plane

After you install and confirm that all namespaces use the Google-managed control plane, you can delete the old control plane.
    
    
    kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod -n istio-system --ignore-not-found=true
    

If you used `istioctl kube-inject` instead of automatic injection, or if you installed additional gateways, check the metrics for the control plane, and verify that the number of connected endpoints is zero.

### Roll back

Perform the following steps if you need to roll back to the previous control plane version:

  1. Update workloads to be injected with the previous version of the control plane. In the following command, the revision value `asm-191-1` is used only as an example. Replace the example value with the revision label of your previous control plane.
         
         kubectl label namespace NAMESPACE istio-injection- istio.io/rev=asm-191-1 --overwrite
         

  2. Restart the Pods to trigger re-injection so the proxies have the previous version:
         
         kubectl rollout restart deployment -n NAMESPACE
         




The managed control plane will automatically scale to zero and not use any resource when not in use. The mutating webhooks and provisioning will remain and do not affect cluster behavior.

The gateway is now set to the `asm-managed` revision. To roll back, re-run the Cloud Service Mesh install command, which will re-deploy gateway pointing back to your in-cluster control plane:
    
    
    kubectl -n istio-system rollout undo deploy istio-ingressgateway
    

Expect this output on success:
    
    
    deployment.apps/istio-ingressgateway rolled back
    

## Uninstall

Managed control plane auto-scales to zero when no namespaces are using it. For detailed steps, see [Uninstall Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/uninstall).

## Troubleshooting

To identify and resolve problems when using managed control plane, see [Resolving managed control plane issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-managed-service-mesh).

## What's next?

  * Learn about [release channels](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh).
  * [Migrate from `IstioOperator`](https://docs.cloud.google.com/service-mesh/legacy/migrate-istio-operator).
  * [Migrate a gateway to managed control plane](https://docs.cloud.google.com/service-mesh/docs/gateways#upgrading_gateways).
  * Learn how to [Enable optional managed Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features), such as: 
    * [Envoy access logs](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features#envoy_access_logs)
    * [Tracing](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features#enable_cloud_tracing)
    * [Distroless images](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features#distroless_proxy_image)
    * [End user authentication](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features#end_user_authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
