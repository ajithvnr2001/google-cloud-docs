---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade/
title: Upgrade Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:45.335668+00:00
---

# Upgrade Cloud Service Mesh  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This page explains how to:

  * Run `asmcli` to upgrade from Cloud Service Mesh to Cloud Service Mesh 1.22.8.

  * Optionally, deploy an ingress gateway.

  * Do a canary upgrade to migrate your workloads to the new control plane.




The Cloud Service Mesh version that you can upgrade from differs by platform.

###  GKE 

You can upgrade directly to Cloud Service Mesh 1.22.8-asm.5 on Google Kubernetes Engine from the following versions:

1.20+

### On-premises

You can upgrade directly to Cloud Service Mesh 1.22.8-asm.5 on Google Distributed Cloud (software only) for VMware and Google Distributed Cloud (software only) for bare metal from the following versions:

1.20+

###  GKE on AWS 

You can upgrade directly to Cloud Service Mesh 1.22.8-asm.5 on GKE on AWS from the following versions:

1.20+

###  GKE on Azure 

GKE on Azure only supports Cloud Service Mesh 1.16. Upgrades from earlier versions of Cloud Service Mesh are not supported.

### Amazon EKS

If you have Cloud Service Mesh 1.7 installed on EKS, you will need to [install Cloud Service Mesh 1.22](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh) on a new cluster. Upgrades from Cloud Service Mesh 1.7 to Cloud Service Mesh 1.22 aren't supported.

### Microsoft AKS

If you have Cloud Service Mesh 1.7 installed on AKS, you will need to [install Cloud Service Mesh 1.22](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh) on a new cluster. Upgrades from Cloud Service Mesh 1.7 to Cloud Service Mesh 1.22 aren't supported.

## Before you begin

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

Before you begin, make sure that you:

  * Review [the prerequisites](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites).
  * Review the information in [Plan the upgrade](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/kubernetes-off-gcp/plan-upgrade).
  * [Install the required tools](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools).
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli).
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions).
  * [Validate project and cluster](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster).



## Control plane customizations

If you customized the previous installation, you need the same customizations when you upgrade to a new Cloud Service Mesh version or migrate from Istio. If you customized the installation by adding the `--set values` flag to `istioctl install`, you must add those settings to an `IstioOperator` YAML file, referred to as an [overlay file](https://docs.cloud.google.com/service-mesh/v1.22/docs/enable-optional-features-in-cluster). You specify the overlay file by using the `--custom_overlay` option with the filename when you run the script. The script passes the overlay file to `istioctl install`.

**Caution:** Omitting the overlay file results in a successful installation. However, your service mesh has a different configuration than you intended because the omitted values are reset back to the defaults when the control plane and ingress gateway are redeployed.

## Certification Authority

Changing the certificate authority (CA) during an upgrade causes downtime. During the upgrade, mTLS traffic is interrupted until all workloads are switched to using the new control plane with the new CA.

## Upgrade Cloud Service Mesh

The following outlines how to upgrade Cloud Service Mesh:

  1. If you are upgrading a multi-cluster mesh on GKE that uses Cloud Service Mesh certificate authority, run `asmcli create-mesh` to configure the multi-cluster mesh to trust [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity) for no down time cross-cluster load balancing during the upgrade.

  2. Run `asmcli install` to install Cloud Service Mesh on a single cluster. See the following sections for command line examples. The examples contain both required arguments and optional arguments that you might find useful. We recommend that you always specify the `output_dir` argument so that you can easily locate sample gateways and tools such as `istioctl`. See the navigation bar on the right for a list of the examples.

  3. Optionally, install or upgrade an ingress gateway. By default, `asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. If you need the default `istio-ingressgateway` installed with the in-cluster control plane, include the `--option legacy-default-ingressgateway` argument.

  4. To complete setting up Cloud Service Mesh, you need to enable automatic sidecar injection and deploy or redeploy workloads.




### Configure the multi-cluster mesh to trust fleet workload identity

If you are upgrading a multi-cluster mesh on GKE that uses Cloud Service Mesh certificate authority as the certificate authority, you need to run `asmcli create-mesh` before upgrading each cluster. This command configures Cloud Service Mesh certificate authority to use the fleet workload identity pool, `FLEET_PROJECT_ID.svc.id.goog`, as the trust domain after you upgrade. The `asmcli create-mesh` command:

  * Registers all clusters to the same fleet.
  * Configures the mesh to trust the fleet workload identity.
  * Creates remote secrets.



You can either specify the URI for each cluster or the path to the [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).

### Cluster URI

In the following command, replace `FLEET_PROJECT_ID` with the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project) and the cluster URI with the cluster name, zone or region, and project ID for each cluster.
    
    
    ./asmcli create-mesh \
        FLEET_PROJECT_ID \
        PROJECT_ID_1/CLUSTER_LOCATION_1/CLUSTER_NAME_1 \
        PROJECT_ID_2/CLUSTER_LOCATION_2/CLUSTER_NAME_2 # \
        # Add a line for each cluster in the mesh
    

### kubeconfig file

In the following command, replace `FLEET_PROJECT_ID` with the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project) and `PATH_TO_KUBECONFIG` with the path to each `kubeconfig` file.
    
    
    ./asmcli create-mesh \
        FLEET_PROJECT_ID \
        PATH_TO_KUBECONFIG_1 \
        PATH_TO_KUBECONFIG_2 # \
        # Add a line for each cluster in the mesh
    

### Upgrade with default features and Mesh CA

This section shows how to run `asmcli` to upgrade Cloud Service Mesh with the default [supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster) for your platform and enable Cloud Service Mesh certificate authority as the certificate authority.

###  GKE 

Run the following command to upgrade the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.
    
    
    ./asmcli install \
      --project_id PROJECT_ID \
      --cluster_name CLUSTER_NAME \
      --cluster_location CLUSTER_LOCATION \
      --fleet_id FLEET_PROJECT_ID \
      --output_dir DIR_PATH \
      --enable_all \
      --ca mesh_ca
    

  * `--project_id`, `--cluster_name`, and `--cluster_location` Specify the project ID that the cluster is in, the cluster name, and either the cluster zone or region.
  * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). If you don't include this option, `asmcli` uses the project that the cluster was created in when registering the cluster.
  * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. **Note:** Make note of this `--output_dir` directory. You will need to reference it when deploying gateways. 
  * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
    * Grant required IAM permissions.
    * Enable the required Google APIs.
    * Set a label on the cluster that identifies the mesh.
    * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
  * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)



### Other GKE Enterprise clusters

Run the following commands on other GKE Enterprise clusters to upgrade the control plane with default features and Cloud Service Mesh certificate authority. Enter your values in the provided placeholders.

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
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)



### Upgrade default features with CA Service

This section shows how to run `asmcli` to upgrade Cloud Service Mesh with the default [supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster) for your platform and enable [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs).

###  GKE 

Run the following command to upgrade the control plane with default features and Certificate Authority Service. Enter your values in the provided placeholders.
    
    
    ./asmcli install \
      --project_id PROJECT_ID \
      --cluster_name CLUSTER_NAME \
      --cluster_location CLUSTER_LOCATION \
      --fleet_id FLEET_PROJECT_ID \
      --output_dir DIR_PATH \
      --enable_all \
      --ca gcp_cas \
      --ca_pool projects/PROJECT_NAME/locations/ca_region/caPools/CA_POOL
    

  * `--project_id`, `--cluster_name`, and `--cluster_location` Specify the project ID that the cluster is in, the cluster name, and either the cluster zone or region.
  * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). If you don't include this option, `asmcli` uses the project that the cluster was created in when registering the cluster.
  * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. **Note:** Make note of this `--output_dir` directory. You will need to reference it when deploying gateways. 
  * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
    * Grant required IAM permissions.
    * Enable the required Google APIs.
    * Set a label on the cluster that identifies the mesh.
    * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
  * `--ca gcp_cas` Use Certificate Authority Service as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Certificate Authority Service to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
  * `--ca_pool` The full identifier for the Certificate Authority Service [CA Pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).



###  On-premises 

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to upgrade the control plane with default features and Certificate Authority Service. Enter your values in the provided placeholders.

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
          --ca_pool projects/PROJECT_NAME/locations/ca_region/caPools/CA_POOL
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca gcp_cas` Use Certificate Authority Service as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Certificate Authority Service to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
     * `--ca_pool` The full identifier for the Certificate Authority Service [CA Pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).



### Upgrade default features with Istio CA

This section shows how to run `asmcli` to upgrade Cloud Service Mesh with the default [supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster) for your platform and enable Istio CA.

###  GKE 

Run the following command to upgrade the control plane with default features and Istio CA. Enter your values in the provided placeholders.
    
    
    ./asmcli install \
      --project_id PROJECT_ID \
      --cluster_name CLUSTER_NAME \
      --cluster_location CLUSTER_LOCATION \
      --fleet_id FLEET_PROJECT_ID \
      --output_dir DIR_PATH \
      --enable_all \
      --ca citadel
    

  * `--project_id`, `--cluster_name`, and `--cluster_location` Specify the project ID that the cluster is in, the cluster name, and either the cluster zone or region.
  * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). If you don't include this option, `asmcli` uses the project that the cluster was created in when registering the cluster.
  * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. **Note:** Make note of this `--output_dir` directory. You will need to reference it when deploying gateways. 
  * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
    * Grant required IAM permissions.
    * Enable the required Google APIs.
    * Set a label on the cluster that identifies the mesh.
    * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
  * `--ca citadel` Use Istio CA. Changing certificate authorities during an upgrade causes downtime.



### On-premises

Run the following commands on Google Distributed Cloud (software only) for VMware or Google Distributed Cloud (software only) for bare metal to upgrade the control plane with default features and Istio CA. Enter your values in the provided placeholders.

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
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain



### AWS

Run the following commands on GKE on AWS to upgrade the control plane with default features and Istio CA. Enter your values in the provided placeholders. You can choose to enable Ingress for the public subnet or the private subnet.

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
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain



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
           --custom_overlay istio-operator-internal-lb.yaml
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain



### Amazon EKS

Run the following commands on Amazon EKS to upgrade the control plane with default features and Istio CA. Enter your values in the provided placeholders.

**Platform note:** If you have Cloud Service Mesh 1.7 installed on EKS, you will need to install Cloud Service Mesh 1.22 on a new cluster. Upgrades from Cloud Service Mesh 1.7 to Cloud Service Mesh 1.22 aren't supported. 

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
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain



### Microsoft AKS

Run the following commands on Microsoft AKS to upgrade the control plane with default features and Istio CA. Enter your values in the provided placeholders.

**Note:** If you have Cloud Service Mesh 1.7 installed on AKS, you will need to install Cloud Service Mesh 1.22 on a new cluster. Upgrades from Cloud Service Mesh 1.7 to Cloud Service Mesh 1.22 aren't supported.

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
           --ca_cert FILE_PATH \
           --ca_key FILE_PATH \
           --root_cert FILE_PATH \
           --cert_chain FILE_PATH
         

     * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
     * `--kubeconfig` The full path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here. Additionally, relative `kubeconfig` file locations that use a `~` will not work. 
     * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
     * `--platform multicloud` Specifies that the platform is something _other than_ Google Cloud, such as on-premises or multi-cloud. 
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca citadel` Use Istio CA as the certificate authority.
     * `--ca_cert` The intermediate certificate
     * `--ca_key` The key for the intermediate certificate
     * `--root_cert` The root certificate
     * `--cert_chain` The certificate chain



### Upgrade with optional features

An overlay file is a YAML file containing an `IstioOperator` custom resource (CR) that you pass to `asmcli` to configure the control plane. You can override the default control plane configuration and [enable an optional feature](https://docs.cloud.google.com/service-mesh/v1.22/docs/enable-optional-features-in-cluster) by passing the YAML file to `asmcli`. You can layer on more overlays, and each overlay file overrides the configuration on the previous layers.

###  GKE 

Run the following command to install the control plane with an optional feature. To add multiple files, specify `--custom_overlay` and the filename, for example: `--custom_overlayoverlay_file1.yaml --custom_overlay overlay_file2.yaml --custom_overlay overlay_file3.yaml` Enter your values in the provided placeholders.
    
    
    ./asmcli install \
      --project_id PROJECT_ID \
      --cluster_name CLUSTER_NAME \
      --cluster_location CLUSTER_LOCATION \
      --fleet_id FLEET_PROJECT_ID \
      --output_dir DIR_PATH \
      --enable_all \
      --ca mesh_ca \
      --custom_overlay OVERLAY_FILE
    

  * `--project_id`, `--cluster_name`, and `--cluster_location` Specify the project ID that the cluster is in, the cluster name, and either the cluster zone or region.
  * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). If you don't include this option, `asmcli` uses the project that the cluster was created in when registering the cluster.
  * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. **Note:** Make note of this `--output_dir` directory. You will need to reference it when deploying gateways. 
  * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
    * Grant required IAM permissions.
    * Enable the required Google APIs.
    * Set a label on the cluster that identifies the mesh.
    * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
  * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
  * `--custom_overlay` Specify the name of the overlay file.



### Outside Google Cloud

Run the following commands on Google Distributed Cloud (software only) for VMware, Google Distributed Cloud (software only) for bare metal, GKE on AWS, Amazon EKS, or Microsoft AKS. Enter your values in the provided placeholders.

**Platform note:** If you have Cloud Service Mesh 1.7 installed on EKS, you will need to install Cloud Service Mesh 1.22 on a new cluster. Upgrades from Cloud Service Mesh 1.7 to Cloud Service Mesh 1.22 aren't supported. 

  1. Set the current context to your user cluster:
         
         kubectl config use-context CLUSTER_NAME
         

  2. Run `asmcli install`:
         
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
     * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.22/docs/asmcli-reference#enablement_flags) Allows the script to: 
       * Grant required IAM permissions.
       * Enable the required Google APIs.
       * Set a label on the cluster that identifies the mesh.
       * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.
     * `--ca mesh_ca` Use Cloud Service Mesh certificate authority as the certificate authority. Changing certificate authorities during an upgrade causes downtime. `asmcli`configures Cloud Service Mesh certificate authority to use [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity)
     * `--custom_overlay` Specify the name of the overlay file.



## Upgrade gateways

If you have gateways deployed, you will need to upgrade these as well. For a simple upgrade follow the In-place Upgrades section in the [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.22/docs/operate-and-maintain/gateways#in-place_upgrades) guide.

**Warning:** If you installed Cloud Service Mesh with any other method than `asmcli`, the default ingress gateway installed will be removed unless you pass in the `--option legacy-default-ingressgateway` argument.

## Switch to the new control plane

  1. Get the revision label that is on `istiod`.
         
         kubectl get pod -n istio-system -L istio.io/rev
         

The output from the command is similar to the following.
         
         NAME                                                 READY   STATUS    RESTARTS   AGE   REV
         istiod-asm-1228-5-67998f4b55-lrzpz           1/1     Running   0          68m   asm-1215-34
         istiod-asm-1228-5-67998f4b55-r76kr           1/1     Running   0          68m   asm-1215-34
         istiod-1215-34-1-5cd96f88f6-n7tj9    1/1     Running   0          27s   asm-1228-5
         istiod-1215-34-1-5cd96f88f6-wm68b    1/1     Running   0          27s   asm-1228-5

     1. In the output, under the `REV` column, note the value of the revision label for the new version. In this example, the value is `asm-1228-5`.

     2. Also note the value in the revision label for the old `istiod` version. You need this to delete the old version of `istiod` when you finish moving workloads to the new version. In the example output, the value of the revision label for the old version is `asm-1215-34`.

  2. Add the revision label to an application namespace and remove the `istio-injection` label (if it exists). In the following command, change `REVISION` to the value that matches the new revision of `istiod`.
         
         kubectl label namespace NAMESPACE istio.io/rev=REVISION istio-injection- --overwrite

If you see `"istio-injection not found"` in the output, you can ignore it. That means that the namespace didn't previously have the `istio-injection` label. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  3. Restart the Pods to trigger re-injection.
         
         kubectl rollout restart deployment -n NAMESPACE

  4. Test your application to verify that the workloads are working correctly.

  5. If you have workloads in other namespaces, repeat the steps to label the namespace and restart Pods.

  6. If you are satisfied that your application is working as expected, continue with the steps to transition to the new version of `istiod`. If there's an issue with your application, follow the steps to rollback.

### Complete the transition

If you are satisfied that your application is working as expected, remove the old control plane to complete the transition to the new version.

     1. Change to the directory where the files from the `anthos-service-mesh` GitHub repository are located.

     2. Configure the validating webhook to use the new control plane:
            
            kubectl apply -f asm/istio/istiod-service.yaml
            

     3. Move the default tag:
            
            <OUTPUT_DIR>/istioctl tag set default --revision <NEW REVISION NAME>
            

     4. Delete the old version of `istiod`. The command that you use depends on whether you are migrating from Istio or upgrading from a previous version of Cloud Service Mesh.

### Migrate

If you migrated from Istio, the old `istio-ingressgateway` doesn't have a revision label:
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod -n istio-system --ignore-not-found=true
            

### Upgrade

        1. If you upgraded from a previous Cloud Service Mesh version, in the following command, make sure that `OLD_REVISION` matches the revision label for the previous version of `istiod`:
               
               kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-OLD_REVISION -n istio-system --ignore-not-found=true
               

        2. Delete the `validatingwebhookconfiguration` resource for old revision:
               
               kubectl delete validatingwebhookconfiguration istio-validator-OLD_REVISION-istio-system -n istio-system --ignore-not-found
               

     5. Remove the old version of the `IstioOperator` configuration:
            
            kubectl delete IstioOperator installed-state-OLD_REVISION -n istio-system
            

The expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-OLD_REVISION" deleted

### Rollback

If you encountered an issue when testing your application with the new version of `istiod`, follow these steps to rollback to the previous version:

     1. Relabel your namespace to enable auto-injection with the previous version of `istiod`. The command that you use depends on whether you used a revision label or `istio-injection=enabled` with the previous version.

        * If you used a revision label for auto-injection:
              
              kubectl label namespace NAMESPACE istio.io/rev=OLD_REVISION --overwrite
              

        * If you used `istio-injection=enabled`:
              
              kubectl label namespace NAMESPACE istio.io/rev- istio-injection=enabled --overwrite
              

Expected output:
    
    namespace/NAMESPACE labeled

     2. Confirm that the revision label on the namespace matches the revision label on the previous version of `istiod`:
            
            kubectl get ns NAMESPACE --show-labels
            

     3. Restart the Pods to trigger re-injection so the proxies have the previous version:
            
            kubectl rollout restart deployment -n NAMESPACE
            

     4. Remove the new version of `istiod`. Make sure that the value of `REVISION` in the following command is correct.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-REVISION -n istio-system --ignore-not-found=true
            

     5. Remove the new version of the `IstioOperator` configuration.

**Note:** if you upgrade to Cloud Service Mesh 1.21 or later, the `IstioOperator` resource does not exist.
    
    kubectl delete IstioOperator installed-state-REVISION -n istio-system
    

Expected output is similar to the following:
    
    istiooperator.install.istio.io "installed-state-REVISION" deleted

     1. If you didn't include the `--disable_canonical_service` flag, `asmcli` enabled the Canonical Service controller. We recommend that you leave it enabled, but if you need to disable it, see [Enabling and disabling the Canonical Service controller](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service-controller-enable-and-disable).

     2. If you have gateways deployed, make sure to change the revision label on the namespace or deployment to match the previous version of `istiod`. Follow the same process outlined under the In-place Upgrages section in the [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.22/docs/operate-and-maintain/gateways#in-place_upgrades) guide.




## Deploying and redeploying workloads

Your installation (or upgrade) isn't complete until you enable automatic sidecar proxy injection (auto-injection). Migrations from OSS Istio and upgrades follow the revision-based upgrade process (referred to as "canary upgrades" in the Istio documentation). With a revision-based upgrade, the new version of the control plane is installed alongside the existing control plane. You then move some of your workloads to the new version, which lets you monitor the effect of the upgrade with a small percentage of the workloads before migrating all of the traffic to the new version.

The script sets a [revision label](https://docs.cloud.google.com/service-mesh/v1.22/docs/revisions-overview) in the format `istio.io/rev=asm-1228-5` on `istiod`. To enable auto-injection, add a matching revision label to your namespace(s). The revision label is used by the sidecar injector webhook to associate injected sidecars with a particular `istiod` revision. After adding the label, restart the Pods in the namespace for sidecars to be injected.

  1. Get the revision label that is on `istiod` and the `istio-ingressgateway`. In the following command, change the `INGRESS_NAMESPACE` value to the namespace where your ingress gateway is running:
         
         kubectl get pod -n INGRESS_NAMESPACE -L istio.io/rev
         

The output from the command is similar to the following if your ingress gateway name is `istio-ingressgateway`:
         
         NAME                                                READY   STATUS    RESTARTS   AGE   REV
         istio-ingressgateway-65d884685d-6hrdk               1/1     Running   0          67m
         istio-ingressgateway-65d884685d-94wgz               1/1     Running   0          67m
         istio-ingressgateway-asm-182-2-8b5fc8767-gk6hb      1/1     Running   0          5s    asm-1228-5
         istio-ingressgateway-asm-182-2-8b5fc8767-hn4w2      1/1     Running   0          20s   asm-1228-5
         istiod-asm-1228-5-67998f4b55-lrzpz          1/1     Running   0          68m   asm-1215-34
         istiod-asm-1228-5-67998f4b55-r76kr          1/1     Running   0          68m   asm-1215-34
         istiod-asm-1215-34-5cd96f88f6-n7tj9 1/1     Running   0          27s   asm-1228-5
         istiod-asm-1215-34-5cd96f88f6-wm68b 1/1     Running   0          27s   asm-1228-5

     1. In the output, under the `REV` column, note the value of the revision label for the new version. In this example, the value is `asm-1228-5`.

     2. Also note the value in the revision label for the old `istiod` version. You need this to delete the old version of `istiod` when you finish moving workloads to the new version. In the example output, the value of the revision label for the old version is `asm-1215-34`.

  2. Switch the ingress gateway to the new revision. In the following command, change `REVISION` to the value that matches the revision label of the new version. Change the `INGRESS_NAMESPACE` to the namespace where your ingress gateway is running and the `INGRESS_NAME` to the name of your ingress gateway.
         
         kubectl patch service -n istio-system INGRESS_NAMESPACE INGRESS_NAME --type='json' -p='[{"op": "replace", "path": "/spec/selector/service.istio.io~1canonical-revision", "value": "REVISION"}]'

Expected output: `service/istio-ingressgateway patched`

  3. Add the revision label to a namespace and remove the `istio-injection` label (if it exists). In the following command, change `REVISION` to the value that matches the new revision of `istiod`.
         
         kubectl label namespace NAMESPACE istio.io/rev=REVISION istio-injection- --overwrite

If you see `"istio-injection not found"` in the output, you can ignore it. That means that the namespace didn't previously have the `istio-injection` label. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  4. Restart the Pods to trigger re-injection.

**Warning:** Make sure to restart all pods in order to trigger the re-injection of sidecars. Otherwise, the Cloud Service Mesh metric reports may become inconsistent between the old and new proxies in the cluster.
         
         kubectl rollout restart deployment -n NAMESPACE

  5. Test your application to verify that the workloads are working correctly.

  6. If you have workloads in other namespaces, repeat the steps to label the namespace and restart Pods.

  7. If you are satisfied that your application is working as expected, continue with the steps to transition to the new version of `istiod`. If there's an issue with your application, follow the steps to rollback.

### Complete the transition

If you are satisfied that your application is working as expected, remove the old control plane to complete the transition to the new version.

     1. Change to the directory where the files from the `anthos-service-mesh` GitHub repository are located.

     2. Configure the validating webhook to use the new control plane.
            
            kubectl apply -f asm/istio/istiod-service.yaml
            

     3. Move the default tag.
            
            <OUTPUT_DIR>/istioctl tag set default --revision <NEW REVISION NAME> --overwrite
            

     4. Delete the old ingress gateway deployment. The command that you run depends on whether you are migrating from Istio or upgrading from a previous version of Cloud Service Mesh:

### Migrate

If you migrated from Istio, the old `INGRESS_NAME` doesn't have a revision label.
            
            kubectl delete deploy/INGRESS_NAME -n INGRESS_NAMESPACE
            

### Upgrade

If you upgraded from a previous Cloud Service Mesh version, in the following command, replace `OLD_REVISION` with the revision label for the previous version of the `INGRESS_NAME`.
            
            kubectl delete deploy -l app=INGRESS_NAME,istio.io/rev=OLD_REVISION -n INGRESS_NAMESPACE --ignore-not-found=true
            

     5. Delete the old version of `istiod`. The command that you use depends on whether you are migrating from Istio or upgrading from a previous version of Cloud Service Mesh.

### Migrate

If you migrated from Istio, the old `istiod` doesn't have a revision label.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod -n istio-system --ignore-not-found=true
            

If you have the older control plane, which has the `OLD_REVISION` revision label, click the `upgrade` tab and complete the deletion of the istiod control plane with `OLD_REVISION`.

### Upgrade

If you upgraded from a previous Cloud Service Mesh version, in the following command, make sure that `OLD_REVISION` matches the revision label for the previous version of `istiod`.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-OLD_REVISION -n istio-system --ignore-not-found=true
            

Delete the `validatingwebhookconfiguration` resource for the old revision:
            
            kubectl delete validatingwebhookconfiguration istio-validator-OLD_REVISION-istio-system -n istio-system --ignore-not-found=true
            

     6. Remove the old version of the `IstioOperator` configuration.
            
            kubectl delete IstioOperator installed-state-OLD_REVISION -n istio-system --ignore-not-found=true
            

The expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-OLD_REVISION" deleted

### Rollback

If you encountered an issue when testing your application with the new version of `istiod`, follow these steps to rollback to the previous version:

     1. Relabel your namespace to enable auto-injection with the previous version of `istiod`. The command that you use depends on whether you used a revision label or `istio-injection=enabled` with the previous version.

        * If you used a revision label for auto-injection:
              
              kubectl label namespace NAMESPACE istio.io/rev=OLD_REVISION --overwrite
              

        * If you used `istio-injection=enabled`:
              
              kubectl label namespace NAMESPACE istio.io/rev- istio-injection=enabled --overwrite
              

Expected output:
    
    namespace/NAMESPACE labeled

     2. Confirm that the revision label on the namespace matches the revision label on the previous version of `istiod`:
            
            kubectl get ns NAMESPACE --show-labels
            

     3. Restart the Pods to trigger re-injection so the proxies have the previous version:
            
            kubectl rollout restart deployment -n NAMESPACE
            

     4. Remove the new `istio-ingressgateway` Deployment. Make sure that the value of `REVISION` in the following command is correct.
            
            kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=REVISION -n istio-system --ignore-not-found=true
            

     5. Remove the new version of `istiod`. Make sure that the value of `REVISION` in the following command is correct.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-REVISION -n istio-system --ignore-not-found=true
            

     6. Remove the new version of the `IstioOperator` configuration.

**Note:** if you upgrade to Cloud Service Mesh 1.21 or later, the `IstioOperator` resource does not exist.
    
    kubectl delete IstioOperator installed-state-REVISION -n istio-system --ignore-not-found=true
    

Expected output is similar to the following:
    
    istiooperator.install.istio.io "installed-state-REVISION" deleted

     1. If you didn't include the `--disable_canonical_service` flag, the script enabled the Canonical Service controller. We recommend that you leave it enabled, but if you need to disable it, see [Enabling and disabling the Canonical Service controller](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service-controller-enable-and-disable).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
