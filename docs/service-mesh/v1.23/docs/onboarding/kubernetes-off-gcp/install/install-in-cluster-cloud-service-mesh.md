---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh/
title: Install Cloud Service Mesh for Kubernetes workloads off Google Cloud \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:15.555564+00:00
---

# Install Cloud Service Mesh for Kubernetes workloads off Google Cloud  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install Cloud Service Mesh for Kubernetes workloads off Google Cloud

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This page explains how to install unmanaged, in-cluster Cloud Service Mesh for Kubernetes workloads off Google Cloud:

  * Run `asmcli` to do a new installation of Cloud Service Mesh 1.23.6-asm.11.
  * Optionally, deploy an ingress gateway.
  * Deploy or redeploy your workloads to inject sidecar proxies.



If you need to install unmanaged, in-cluster Cloud Service Mesh with an `istiod` control plane on GKE, see [Install in-cluster Cloud Service Mesh on Google Cloud](https://docs.cloud.google.com/service-mesh/v1.23/docs/legacy/in-cluster/install-in-cluster-cloud-service-mesh). Note that for Kubernetes workloads on Google Cloud, we recommend [provisioning a managed control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/provision-control-plane)

For instructions to prepare an offline installation of Cloud Service Mesh, see [Prepare an offline installation of Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/offline-install-cloud-service-mesh) You will need to specify the `--offline` and `--output_dir` options when running `asmcli install`.

## Limitations

Note the following limitations:

  * All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet.

  * The `asmcli` tool must have access to the Google Kubernetes Engine (GKE) endpoint. You can configure access through a ["jump" server](https://en.wikipedia.org/wiki/Jump_server), such as a Compute Engine VM within the Virtual Private Cloud (VPC) giving specific access.




## Before you begin

Before you begin, make sure that you:

  * Review [the prerequisites](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites).
  * Review the information in [Plan the install](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/plan-install).
  * [Install the required tools](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools).
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli).
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions).
  * [Validate project and cluster](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster).

**Warning:** For Cloud Service Mesh to function correctly, deploy `istiod` and `canonical-service-controller-manager` to your cluster. These tools have elevated [role-based access control (RBAC) permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb), such as the ability to modify all deployments and to modify all cluster secrets. These permissions are required for Cloud Service Mesh functions such as injecting sidecars, discovering services, securing traffic, managing ingress gateways, and presenting services dashboards.**Note:** If you need to install Cloud Service Mesh from a private or custom container registry, see [Use a custom overlay for custom registry](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/service-mesh/v1.23/docs/enable-optional-features-in-cluster#use_a_custom_overlay_for_custom_registry).

## Roles required to install in-cluster Cloud Service Mesh

The following table describes the roles that are required to install in-cluster Cloud Service Mesh.

**Role name** | **Role ID** | **Grant location** | **Description**  
---|---|---|---  
GKE Hub Admin | roles/gkehub.admin | Fleet project | Full access to GKE Hubs and related resources.  
Kubernetes Engine Admin | roles/container.admin | Cluster project. Note that this role must be granted in both Fleet and cluster project for cross-project bindings. | Provides access to full management of Container Clusters and their Kubernetes API objects.  
Mesh Config Admin | roles/meshconfig.admin | Fleet and cluster project | Provides permissions required to initialize managed components of Cloud Service Mesh, such as managed control plane and backend permission that allows workloads to talk to Stackdriver without each being individually authorized (for both managed and in-cluster control planes).  
Project IAM Admin | roles/resourcemanager.projectIamAdmin | Cluster project | Provides permissions to administer IAM policies on projects.  
Service Account Admin | roles/iam.serviceAccountAdmin | Fleet project | Authenticate as a service account.  
Service Management Admin | roles/servicemanagement.admin | Fleet project | Full control of Google Service Management resources.  
Service Usage Admin | roles/serviceusage.serviceUsageAdmin | Fleet project | Ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project.(Note 1)  
CA Service Admin [Beta](https://cloud.google.com/products#product-launch-stages) | roles/privateca.admin | Fleet project | Full access to all CA Service resources. (Note 2)  
  
**Notes:**

  1. **Service Usage Admin** \- This role is necessary as a prerequisite to enable the `mesh.googleapis.com` API when initially provisioning managed Cloud Service Mesh. 
  2. **CA Service Admin** \- This role is only required if you are integrating with CA Service. 



## Install Cloud Service Mesh

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

The following outlines how to install Cloud Service Mesh:

  1. Run `asmcli install` to install the in-cluster control plane on a single cluster. See the following sections for command line examples. The examples contain both required arguments and optional arguments that you might find useful. We recommend that you always specify the `output_dir` argument so that you can locate sample gateways and tools such as `istioctl`. See the navigation bar on the right for a list of the examples.

  2. Optionally, install an ingress gateway. By default, `asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. If you need the default `istio-ingressgateway` installed with the in-cluster control plane, include the `--option legacy-default-ingressgateway` argument.

  3. To complete setting up Cloud Service Mesh, you need to enable automatic sidecar injection and deploy or redeploy workloads.

  4. If you are installing Cloud Service Mesh on more than one cluster, run `asmcli install` on each cluster. When you run `asmcli install`, be sure to use the same `FLEET_PROJECT_ID` for each cluster. After Cloud Service Mesh is installed, see the instructions to set up a multi-cluster mesh [off Google Cloud](https://docs.cloud.google.com/service-mesh/v1.23/docs/operate-and-maintain/off-gcp-multi-cluster-setup).

  5. If your clusters are on different networks (as they are in [island mode](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-off-gcp/install/anthos/clusters/docs/bare-metal/latest/reference/flat-vs-island-network#island_mode_network_model) then you should pass a unique network name to `asmcli` using the `--network_id` flag.




### Install default features and Mesh CA

This section shows how to run `asmcli` to install Cloud Service Mesh with the default [supported features](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-in-cluster) for your platform and enable Cloud Service Mesh certificate authority as the certificate authority.

### On-premises

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to install the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca mesh_ca
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)



To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.

**Note:** Prometheus monitoring is enabled by default. Enabling Prometheus and having `enableStackdriverForApplications` set to `true` may incur extra Cloud Monitoring charges. For more information, see [GKE on GDC known issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/known-issues#unexpected-monitoring-billing). To disable Prometheus annotations during Cloud Service Mesh installation, see [disable Prometheus metrics merging feature](https://istio.io/latest/docs/ops/integrations/prometheus/#option-1-metrics-merging).

### AWS

Run the following commands on GKE on AWS to install the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca mesh_ca
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity).



To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.

### Azure

Run the following commands on GKE on Azure to install the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca mesh_ca
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity).



To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.

### Amazon EKS

Run the following commands on Amazon EKS to install the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --option attached-cluster \
           --network_id default \
           --ca mesh_ca
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--option attached-cluster` Changes the default signing utility to be istiod.
     * `--network_id` If you are setting up a multi-network mesh, then set the `--network_id` to a unique value for each cluster in the mesh.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity).



To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.

### Microsoft AKS

Run the following commands on Microsoft AKS to install the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --option attached-cluster \
           --network_id default \
           --ca mesh_ca
         

     * `HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer` Allows registration with GKE GKE Fleet.
**Note:** To allow registration with GKE GKE Fleet, you must use this flag because AKS clusters do not have a publicly-routable OIDC discovery endpoint for the Kubernetes service account token. 
     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--option attached-cluster` Changes the default signing utility to be istiod.
     * `--network_id` If you are setting up a multi-network mesh, then set the `--network_id` to a unique value for each cluster in the mesh.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity).



To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.

### Install default features and Certificate Authority (CA) Service

This section shows how to run `asmcli` to install Cloud Service Mesh with the default [supported features](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features) for your platform and enable CA Service as the certificate authority.

**Platform note:** CA Service is only supported on the following platforms: GKE clusters on Google Cloud, Google Distributed Cloud (software only) for VMware, and Distributed Cloud. If you run `asmcli install` and specify `--ca gcp_cas` on other platforms, the installation appears successful, but your workloads will fail to start. 

In addition to [Cloud Service Mesh certificate authority](https://docs.cloud.google.com/service-mesh/v1.23/docs/security/security-overview#features), you can configure Cloud Service Mesh to use [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). This guide provides you an opportunity to integrate with CA Service, which is recommended for the following use cases:

  * If you need different certificate authorities to sign workload certificates on different clusters.
  * If you need to back your signing keys in a [managed HSM](https://docs.cloud.google.com/kms/docs/hsm).
  * If you are in a highly regulated industry and are subject to compliance.
  * If you want to chain up your Cloud Service Mesh CA to a custom enterprise root certificate to sign workload certificates.



The cost of Cloud Service Mesh certificate authority is included in the [Cloud Service Mesh pricing](https://cloud.google.com/service-mesh/pricing). The CA Service isn't included in the base Cloud Service Mesh price and is [charged separately](https://cloud.google.com/certificate-authority-service/pricing). Additionally, CA Service comes with an [explicit SLA](https://cloud.google.com/certificate-authority-service/sla), but the Cloud Service Mesh certificate authority does not.

#### Configure CA Service

  1. Create the [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool) in the tier `DevOps` and in the same region as the cluster that it serves to avoid excessive latency issues or potential cross-region outages. For more information, see [Workload-optimized tiers](https://docs.cloud.google.com/certificate-authority-service/docs/tiers).
  2. [Create the CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities) to have at least one active certificate authority in the CA pool in the same project as the GKE cluster. Use subordinate CA's to sign Cloud Service Mesh workload certificates. Note down the [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) corresponding to the subordinate CA.
  3. If it is meant to only service certificates for Cloud Service Mesh workloads, set up the following issuance policy for the CA pool:

### policy.yaml
         
         baselineValues:
           keyUsage:
             baseKeyUsage:
               digitalSignature: true
               keyEncipherment: true
             extendedKeyUsage:
               serverAuth: true
               clientAuth: true
           caOptions:
             isCa: false
         identityConstraints:
           allowSubjectPassthrough: false
           allowSubjectAltNamesPassthrough: true
           celExpression:
             expression: subject_alt_names.all(san, san.type == URI && san.value.startsWith("spiffe://PROJECT_ID.svc.id.goog/ns/") )
         

**Note:** As a best practice for multi-cluster meshes, set one subordinate CA pool per unique cluster region. All the subordinate CA pools should chain to the same root CA pool. 
  4. To update the CA pool's issuance policy, use the following command:
         
         gcloud privateca pools update CA_POOL --location ca_region --issuance-policy policy.yaml
         

For information on setting a policy on a pool, see [Using a certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).

  5. If you are using a [certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template), then configure it now. For more information, follow the [CA Service guide](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template#workload-identity) for workload identity certificates. Ensure the certificate template is created in the same region as the CA pool. If there are multiple regions for CA pools, then create a certificate template per region.




#### Configure Cloud Service Mesh to use CA Service

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to install the control plane with default features and Certificate Authority Service. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --kubeconfig KUBECONFIG_FILE \
           --fleet_id FLEET_PROJECT_ID \
           --output_dir DIR_PATH \
           --enable_all \
           --ca gcp_cas \
           --platform multicloud \
           --ca_pool  projects/CA_POOL_PROJECT_ID/locations/ca_region/caPools/CA_POOL
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca gcp_cas` Use Certificate Authority Service as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Certificate Authority Service to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
     * `--ca_pool` The full identifier for the Certificate Authority Service [CA Pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool). If you are using a [certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template), then append the template id separated by `:`. For example: 
           
           --ca_pool projects/CA_POOL_PROJECT_ID/locations/ca_region/caPools/CA_POOL:projects/CA_POOL_PROJECT_ID/locations/ca_region/certificateTemplates/CERT_TEMPLATE_ID
             

To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.




### Install default features with Istio CA

This section explains how to:

  * Generate certificates and keys for the Istio CA that Cloud Service Mesh uses to sign your workloads.
  * Run `asmcli` to install Cloud Service Mesh with default features and enable Istio CA.



By default environments that install Cloud Service Mesh with Istio CA report metrics to Prometheus. If you want to use the Cloud Service Mesh dashboards, you must enable Stackdriver. For more information, see Install with optional features.

For the best security, we highly recommend maintaining an offline root CA and using the subordinate CAs to issue certificates for each cluster. For more information, see [Plug in CA Certificates](https://istio.io/v1.8/docs/tasks/security/cert-management/plugin-ca-cert/). In this configuration, all workloads in the service mesh use the same root certificate authority (CA). Each Cloud Service Mesh CA uses an intermediate CA signing key and certificate, signed by the root CA. When multiple CAs exist within a mesh, this establishes a hierarchy of trust among the CAs. You can repeat these steps to provision certificates and keys for any number of certificate authorities.

**Important:** These steps create certificates and keys using a `make` command that we provide for illustrative purposes only. For the best security, use an offline secure computer and production-ready tools, for example using [HashiCorp Vault](https://www.vaultproject.io/) to securely generate and protect the CA signing key.

The Makefile to generate the certificates is located in the `istio-1.23.6-asm.11` subdirectory in the `--output_dir` directory that you specified in the `asmcli validate` command. If you didn't run `asmcli validate`, or you don't have the downloaded directory locally, you can get the Makefile by [downloading the Cloud Service Mesh installation file](https://docs.cloud.google.com/service-mesh/v1.23/docs/downloading-istioctl) and extracting the contents.

  1. Change to the `istio-1.23.6-asm.11` directory.

  2. Create a directory for the certificates and keys:
         
         mkdir -p certs && \
         pushd certs

  3. Generate a root certificate and key:
         
         make -f ../tools/certs/Makefile.selfsigned.mk root-ca
         

This generates these files:

     * **root-cert.pem** : the root certificate
     * **root-key.pem** : the root key
     * **root-ca.conf** : the configuration for openssl to generate the root certificate
     * **root-cert.csr** : the CSR for the root certificate
  4. Generate an intermediate certificate and key:
         
         make -f ../tools/certs/Makefile.selfsigned.mk cluster1-cacerts

This generates these files in a directory named `cluster1`:

     * **ca-cert.pem** : the intermediate certificates
     * **ca-key.pem** : the intermediate key
     * **cert-chain.pem** : the certificate chain which `istiod` uses
     * **root-cert.pem** : the root certificate
**Note:** You can replace `cluster1` with a different name. For example, `make mycluster-cacerts` creates a directory named `mycluster`.

If you perform these steps using an offline computer, copy the generated directory to a computer with access to the clusters.

  5. Return to the previous directory:
         
         popd

  6. Run `asmcli` to install a mesh using Istio CA:

### On-premises

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to install the control plane with default features and Istio CA. Enter your values in the provided placeholders.

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --ca citadel \
              --ca_cert CA_CERT_FILE_PATH \
              --ca_key CA_KEY_FILE_PATH \
              --root_cert ROOT_CERT_FILE_PATH \
              --cert_chain CERT_CHAIN_FILE_PATH
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate
        * `--ca_key` The key for the intermediate certificate
        * `--root_cert` The root certificate
        * `--cert_chain` The certificate chain

### AWS

Run the following commands on GKE on AWS to install the control plane with default features and Istio CA. Enter your values in the provided placeholders. You can choose to enable Ingress for the public subnet or the private subnet.

### Public

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --ca citadel \
              --ca_cert CA_CERT_FILE_PATH \
              --ca_key CA_KEY_FILE_PATH \
              --root_cert ROOT_CERT_FILE_PATH \
              --cert_chain CERT_CHAIN_FILE_PATH
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate.
        * `--ca_key` The key for the intermediate certificate.
        * `--root_cert` The root certificate.
        * `--cert_chain` The certificate chain.

### Private

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Save the following YAML to a file called `istio-operator-internal-lb.yaml`:
            
            apiVersion: install.istio.io/v1alpha1
            kind: IstioOperator
            spec:
              components:
                ingressGateways:
                - enabled: true
                  k8s:
                    serviceAnnotations:
                      service.beta.kubernetes.io/aws-load-balancer-internal: "true"
                  name: istio-ingressgateway
            

     3. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --ca citadel \
              --ca_cert FILE_PATH \
              --ca_key FILE_PATH \
              --root_cert FILE_PATH \
              --cert_chain FILE_PATH \
              --custom_overlay istio-operator-internal-lb.yaml
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate.
        * `--ca_key` The key for the intermediate certificate.
        * `--root_cert` The root certificate.
        * `--cert_chain` The certificate chain.
        * `--custom_overlay` The name of the overlay file created. For more information about overlay files, see [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#about_the_overlay_files)

### Azure

Run the following commands on GKE on Azure to install the control plane with default features and Istio CA. Enter your values in the provided placeholders. You can choose to enable Ingress for the public subnet or the private subnet.

### Public

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --ca citadel \
              --ca_cert CA_CERT_FILE_PATH \
              --ca_key CA_KEY_FILE_PATH \
              --root_cert ROOT_CERT_FILE_PATH \
              --cert_chain CERT_CHAIN_FILE_PATH
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate.
        * `--ca_key` The key for the intermediate certificate.
        * `--root_cert` The root certificate.
        * `--cert_chain` The certificate chain.

### Private

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Save the following YAML to a file called `istio-operator-internal-lb.yaml`:
            
            apiVersion: install.istio.io/v1alpha1
            kind: IstioOperator
            spec:
              components:
                ingressGateways:
                - enabled: true
                  k8s:
                    serviceAnnotations:
                      service.beta.kubernetes.io/aws-load-balancer-internal: "true"
                  name: istio-ingressgateway
            

     3. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --ca citadel \
              --ca_cert FILE_PATH \
              --ca_key FILE_PATH \
              --root_cert FILE_PATH \
              --cert_chain FILE_PATH \
              --custom_overlay istio-operator-internal-lb.yaml
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate.
        * `--ca_key` The key for the intermediate certificate.
        * `--root_cert` The root certificate.
        * `--cert_chain` The certificate chain.
        * `--custom_overlay` The name of the overlay file created. For more information about overlay files, see [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#about_the_overlay_files)

### Amazon EKS

Run the following commands on Amazon EKS to install the control plane with default features and Istio CA. Enter your values in the provided placeholders.

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Run `asmcli install`:
            
            ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --option attached-cluster \
              --ca citadel \
              --ca_cert CA_CERT_FILE_PATH \
              --ca_key CA_KEY_FILE_PATH \
              --root_cert ROOT_CERT_FILE_PATH \
              --cert_chain CERT_CHAIN_FILE_PATH \
              --network_id default
            

        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `--option attached-cluster` Changes the default signing utility to be istiod.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate
        * `--ca_key` The key for the intermediate certificate
        * `--root_cert` The root certificate
        * `--cert_chain` The certificate chain
        * `--network_id` If you are setting up a multi-network mesh, then set the `--network_id` to a unique value for each cluster in the mesh.

### Microsoft AKS

Run the following commands on Microsoft AKS to install the control plane with default features and Istio CA. Enter your values in the provided placeholders.

     1. Set the current context to your user cluster:
            
            kubectl config use-context CLUSTER_NAME
            

     2. Run `asmcli install`:
            
            HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer ./asmcli install \
              --fleet_id FLEET_PROJECT_ID \
              --kubeconfig KUBECONFIG_FILE \
              --output_dir DIR_PATH \
              --platform multicloud \
              --enable_all \
              --option attached-cluster \
              --ca citadel \
              --ca_cert CA_CERT_FILE_PATH \
              --ca_key CA_KEY_FILE_PATH \
              --root_cert ROOT_CERT_FILE_PATH \
              --cert_chain CERT_CHAIN_FILE_PATH \
              --network_id default
            

        * `HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer` Allows registration with GKE GKE Fleet.
**Note:** To allow registration with GKE GKE Fleet, you must use this flag because AKS clusters do not have a publicly-routable OIDC discovery endpoint for the Kubernetes service account token. 
        * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
        * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
        * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
        * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
        * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
          * Grant required IAM permissions.
          * Enable the required Google APIs.
          * Set a label on the cluster that identifies the mesh.
          * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
        * `--option attached-cluster` Changes the default signing utility to be istiod.
        * `-ca citadel` Use Istio CA as the certificate authority.
        * `--ca_cert` The intermediate certificate
        * `--ca_key` The key for the intermediate certificate
        * `--root_cert` The root certificate
        * `--cert_chain` The certificate chain
        * `--network_id` If you are setting up a multi-network mesh, then set the `--network_id` to a unique value for each cluster in the mesh.




### Install with Istio CA with Google Cloud Observability enabled

If you want to use Cloud Service Mesh dashboards, you must enable Stackdriver.

### On-premises

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to install the control plane with Stackdriver and other optional features features and Istio CA. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
            --fleet_id FLEET_PROJECT_ID \
            --kubeconfig KUBECONFIG_FILE \
            --output_dir DIR_PATH \
            --platform multicloud \
            --enable_all \
            --ca citadel \
            --ca_cert CA_CERT_FILE_PATH \
            --ca_key CA_KEY_FILE_PATH \
            --root_cert ROOT_CERT_FILE_PATH \
            --cert_chain CERT_CHAIN_FILE_PATH
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`. 

To view SLOs and infrastructure metrics in the Cloud Service Mesh UI, you must also perform the first three steps in [Enable application logging and monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#enable_cloud_logging). If logging and monitoring are not enabled and do not receive custom logs and metrics, the Cloud Service Mesh dashboard will not display SLOs, error logs, or CPU and memory metrics.




### AWS

Run the following commands on GKE on AWS to install the control plane with Stackdriver and other optional features and Istio CA. Enter your values in the provided placeholders. You can choose to enable Ingress for the public subnet or the private subnet.

### Public

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert CA_CERT_FILE_PATH \
           --ca_key CA_KEY_FILE_PATH \
           --root_cert ROOT_CERT_FILE_PATH \
           --cert_chain CERT_CHAIN_FILE_PATH \
           --option stackdriver
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate.
     * `--ca_key` The key for the intermediate certificate.
     * `--root_cert` The root certificate.
     * `--cert_chain` The certificate chain.
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`. 



### Private

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Save the following YAML to a file called `istio-operator-internal-lb.yaml`:
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           components:
             ingressGateways:
             - enabled: true
               k8s:
                 serviceAnnotations:
                   service.beta.kubernetes.io/aws-load-balancer-internal: "true"
               name: istio-ingressgateway
         

  3. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
           --custom_overlay istio-operator-internal-lb.yaml \
           --option stackdriver
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate.
     * `--ca_key` The key for the intermediate certificate.
     * `--root_cert` The root certificate.
     * `--cert_chain` The certificate chain.
     * `--custom_overlay` The name of the overlay file created. For more information about overlay files, see [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#about_the_overlay_files)
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`. Alternatively, you can enable Stackdriver using `--custom_overlay stackdriver.yaml`. You must either [ Download the anthos-service-mesh-package](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#downloading_the_anthos-service-mesh_package) or create `stackdriver.yaml` from the [provided manifest](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#stackdriver). 



### Azure

Run the following commands on GKE on Azure to install the control plane with Stackdriver and other optional features and Istio CA. Enter your values in the provided placeholders. You can choose to enable Ingress for the public subnet or the private subnet.

### Public

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert CA_CERT_FILE_PATH \
           --ca_key CA_KEY_FILE_PATH \
           --root_cert ROOT_CERT_FILE_PATH \
           --cert_chain CERT_CHAIN_FILE_PATH \
           --option stackdriver
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate.
     * `--ca_key` The key for the intermediate certificate.
     * `--root_cert` The root certificate.
     * `--cert_chain` The certificate chain.
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`. 



### Private

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Save the following YAML to a file called `istio-operator-internal-lb.yaml`:
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           components:
             ingressGateways:
             - enabled: true
               k8s:
                 serviceAnnotations:
                   service.beta.kubernetes.io/aws-load-balancer-internal: "true"
               name: istio-ingressgateway
         

  3. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
           --custom_overlay istio-operator-internal-lb.yaml \
           --option stackdriver
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate.
     * `--ca_key` The key for the intermediate certificate.
     * `--root_cert` The root certificate.
     * `--cert_chain` The certificate chain.
     * `--custom_overlay` The name of the overlay file created. For more information about overlay files, see [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#about_the_overlay_files)
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`. Alternatively, you can enable Stackdriver using `--custom_overlay stackdriver.yaml`. You must either [ Download the anthos-service-mesh-package](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#downloading_the_anthos-service-mesh_package) or create `stackdriver.yaml` from the [provided manifest](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features#stackdriver). 



### Amazon EKS

Run the following commands on Amazon EKS to install the control plane with Stackdriver and other optional features and Istio CA. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert CA_CERT_FILE_PATH \
           --ca_key CA_KEY_FILE_PATH \
           --root_cert ROOT_CERT_FILE_PATH \
           --cert_chain CERT_CHAIN_FILE_PATH \
           --option stackdriver \
           --option attached-cluster
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`.
     * `--option stackdriver` Changes the default signing utility to be `istiod`.



### Microsoft AKS

Run the following commands on Microsoft AKS to install the control plane with default features and Istio CA. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
         HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer ./asmcli install \
           --fleet_id FLEET_PROJECT_ID \
           --kubeconfig KUBECONFIG_FILE \
           --output_dir DIR_PATH \
           --platform multicloud \
           --enable_all \
           --ca citadel \
           --ca_cert CA_CERT_FILE_PATH \
           --ca_key CA_KEY_FILE_PATH \
           --root_cert ROOT_CERT_FILE_PATH \
           --cert_chain CERT_CHAIN_FILE_PATH \
           --option stackdriver \
           --option attached-cluster
         

     * `HUB_REGISTRATION_EXTRA_FLAGS=--has-private-issuer` Allows registration with GKE GKE Fleet.
**Note:** To allow registration with GKE GKE Fleet, you must use this flag because AKS clusters do not have a publicly-routable OIDC discovery endpoint for the Kubernetes service account token. 
     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `-ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain
     * `--option stackdriver` Enables Stackdriver option. Note that you can also enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`.
     * `--option stackdriver` Changes the default signing utility to be `istiod`.



### Install with optional features

An overlay file is a YAML file containing an `IstioOperator` custom resource (CR) that you pass to `asmcli` to configure the control plane. You can override the default control plane configuration and [enable an optional feature](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features) by passing the YAML file to `asmcli`. You can layer on more overlays, and each overlay file overrides the configuration on the previous layers. As a best practice, we recommend that you save the overlay files in your version control system.

There are two options to enable optional features: [`--option`](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/reference#options) and [`--custom_overlay`](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/reference#options).

Use `--option` to if you don't need to change the overlay file. With this method `asmcli`fetches the file from the [GitHub repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.23/asm/istio/options) for you.

Use `--custom_overlay` when you need to customize the overlay file.

For more information, see [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/enable-optional-features).

Run the following commands on Google Distributed Cloud (software only) for VMware, Google Distributed Cloud (software only) for bare metal, GKE on AWS, GKE on Azure, Amazon EKS, or Microsoft AKS. Enter your values in the provided placeholders.

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install` to install the control plane with an optional feature. To add multiple files, specify `--custom_overlay` and the filename, for example: `--custom_overlayoverlay_file1.yaml --custom_overlay overlay_file2.yaml --custom_overlay overlay_file3.yaml`
         
         ./asmcli install \
         --fleet_id FLEET_PROJECT_ID \
         --kubeconfig KUBECONFIG_FILE \
         --output_dir DIR_PATH \
         --platform multicloud \
         --enable_all \
         --ca mesh_ca \
         --custom_overlay OVERLAY_FILE
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.23/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. Note that `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
     * `--custom_overlay` Specify the name of the overlay file.



## Install gateways

Cloud Service Mesh gives you the option to deploy and manage gateways as part of your service mesh. A gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateways are Envoy proxies that provide you with fine-grained control over traffic entering and leaving the mesh.

  1. Create a namespace for the ingress gateway if you don't already have one. Gateways are user workloads, and as a best practice, they shouldn't be deployed in the control plane namespace. Replace `GATEWAY_NAMESPACE` with the name of your namespace.
         
         kubectl create namespace GATEWAY_NAMESPACE
         

Expected output:
         
         namespace/GATEWAY_NAMESPACE created
         

  2. Enable auto-injection on the gateway. The steps required depend on whether you want to use [default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) (for example, `istio-injection=enabled`) or the [revision label](https://docs.cloud.google.com/service-mesh/v1.23/docs/glossary#revision) on the gateway namespace. The default revision tag and revision label are used by the sidecar injector webhook to associate injected proxies with a particular control plane revision.

### Default (recommended)

     1. If you used a default tag revision to enable auto-injection on the gateway, verify that the default tag exists in the directory that you specified in `--output_dir` and that it is pointing to the newly installed revision.
            
            DIR_PATH/istioctl tag list
            

     2. Apply the default injection labels to the namespace.
            
            kubectl label namespace GATEWAY_NAMESPACE istio-injection=enabled istio.io/rev-
            

### Revision label

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
              "jsonpath={.items[*].metadata.labels['istio\.io/rev']}{'\n'}"
            

The command outputs the revision label that corresponds to the Cloud Service Mesh version, for example: `asm-1236-11`

     2. Apply the revision label to the namespace. In the following command, `REVISION` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace GATEWAY_NAMESPACE \
              istio.io/rev=REVISION --overwrite
            

Expected output:
            
            namespace/GATEWAY_NAMESPACE labeled
            

You can ignore the message `"istio.io/rev" not found` in the output. That means that the namespace didn't previously have the `istio.io/rev` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection fails if a namespace has both the `istio.io/rev` and the `istio-injection` label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly specify both labels. 

If the gateway namespace is not labelled, the `istio-ingressgateway` pods will fail with an `ImagePullBackOff` error when the gateway attempts to pull and the `auto` image. This image should be replaced by the webhook.

  3. Download the example ingress gateway .yaml configuration file from the [`anthos-service-mesh-packages` repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.23/samples/gateways/istio-ingressgateway).

  4. Apply the example ingress gateway .yaml configuration as is, or modify as needed.
         
         kubectl apply -n GATEWAY_NAMESPACE \
           -f CONFIG_PATH/istio-ingressgateway
         

Expected output:
         
         deployment.apps/istio-ingressgateway created
         poddisruptionbudget.policy/istio-ingressgateway created
         horizontalpodautoscaler.autoscaling/istio-ingressgateway created
         role.rbac.authorization.k8s.io/istio-ingressgateway created
         rolebinding.rbac.authorization.k8s.io/istio-ingressgateway created
         service/istio-ingressgateway created
         serviceaccount/istio-ingressgateway created
         




Learn more about [best practices for gateways](https://docs.cloud.google.com/service-mesh/v1.23/docs/operate-and-maintain/gateways).

## Deploy and redeploy workloads

**Warning:** If you are installing sidecars in application pods where CA connectivity through a direct connection is not available (for example, due to firewalls or other restrictive features), then you must [Configure CA connectivity through a proxy](https://docs.cloud.google.com/service-mesh/v1.23/docs/unified-install/options/configure-ca-through-proxy) after installing the in-cluster control plane and before redeploying workloads. 

Cloud Service Mesh uses sidecar proxies to enhance network security, reliability, and observability. With Cloud Service Mesh, these functions are abstracted away from the application's primary container and implemented in a common out-of-process proxy delivered as a separate container in the same Pod.

Your installation isn't complete until you enable automatic sidecar proxy injection (auto-injection) and restart the Pods for any workloads that were running on your cluster before you installed Cloud Service Mesh.

To enable auto-injection, you label your namespaces with the _[default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag)_ if the default tag is set up, or a _[revision label](https://docs.cloud.google.com/service-mesh/v1.23/docs/glossary#revision)_ that was set on `istiod` when you installed Cloud Service Mesh. The default revision tag and revision label are used by the sidecar injector webhook to associate injected sidecars with an `istiod` revision. After adding the label, any existing Pods in the namespace must be restarted for sidecars to be injected.

Before you deploy new workloads in a new namespace, make sure to configure auto-injection so that Cloud Service Mesh can monitor and secure traffic.

  1. The steps required to enable auto-injection depend on whether you want to use default injection labels or the revision label:

### Default (Recommended)

     1. If you used a default tag revision to enable auto-injection on the gateway, verify that the default tag exists in the directory that you specified in `--output_dir` and that it is pointing to the newly installed revision.
            
            DIR_PATH/istioctl tag list
            

     2. Run the following command. `NAMESPACE` is the name of the namespace where you want to enable auto-injection.
            
            kubectl label namespace NAMESPACE istio-injection=enabled istio.io/rev-
            

The default injection labels inject the revision the default tag is pointing to.

### Revision label

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl -n istio-system get pods -l app=istiod --show-labels
            

The output looks similar to the following:
            
            NAME                                READY   STATUS    RESTARTS   AGE   LABELS
            istiod-asm-1236-11-5788d57586-bljj4   1/1     Running   0          23h   app=istiod,istio.io/rev=asm-1236-11,istio=istiod,pod-template-hash=5788d57586
            istiod-asm-1236-11-5788d57586-vsklm   1/1     Running   1          23h   app=istiod,istio.io/rev=asm-1236-11,istio=istiod,pod-template-hash=5788d57586

In the output, under the `LABELS` column, note the value of the `istiod` revision label, which follows the prefix `istio.io/rev=`. In this example, the value is `asm-1236-11`.

     2. Apply the revision label and remove the `istio-injection` label if it exists. In the following command, `NAMESPACE` is the name of the namespace where you want to enable auto-injection, and `REVISION` is the revision label you noted in the previous step.
            
            kubectl label namespace NAMESPACE istio-injection- istio.io/rev=REVISION --overwrite
            

You can ignore the message `"istio-injection not found"` in the output. That means that the namespace didn't previously have the `istio-injection` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  2. If workloads were running on your cluster before you installed Cloud Service Mesh, restart the Pods to trigger re-injection.

How you restart Pods depends on your application and the environment the cluster is in. For example, in your staging environment, you might simply delete all the Pods, which causes them to restart. But in your production environment, you might have a process that implements a [blue-green deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) so that you can safely restart Pods to avoid traffic interruption.

You can use `kubectl` to perform a rolling restart:
         
         kubectl rollout restart deployment -n NAMESPACE
         




## What's next?

  * If you mesh consists of clusters outside of Google Cloud, see [Set up a multi-cluster mesh outside of Google Cloud](https://docs.cloud.google.com/service-mesh/v1.23/docs/operate-and-maintain/off-gcp-multi-cluster-setup).

  * [Configure an external IP address on-premises](https://docs.cloud.google.com/service-mesh/v1.23/docs/operate-and-maintain/external-ip-load-balance).

  * [Deploy the Online Boutique sample application](https://docs.cloud.google.com/service-mesh/v1.23/docs/onlineboutique-install-kpt).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
