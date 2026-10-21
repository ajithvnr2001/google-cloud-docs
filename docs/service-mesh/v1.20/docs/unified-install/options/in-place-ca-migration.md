---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/in-place-ca-migration/
title: In-place CA Migration \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:01.277763+00:00
---

# In-place CA Migration  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/in-place-ca-migration/

You are viewing archived v1.20 Service Mesh documentation.

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
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# In-place CA Migration

**Note:** This guide describes how to migrate your certificate authority (CA) without migrating workloads to a new control plane (in-place) with minimal downtime using a bash-based tool. To migrate from Istio CA to Mesh CA with a canary-based approach that involves minimal or no downtime, see [Canary-based Migration to Mesh CA](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/ca-migration).

If your mesh has multiple clusters with workloads that send requests to workloads on another cluster, then follow all steps in this guide for all the clusters.

Use the steps in this guide for the following use case:

  * Migrate an in-cluster Cloud Service Mesh v1.13 or later control plane with Mesh CA to Certificate Authority Service.
  * Migrate a managed Cloud Service Mesh control plane on a release channel that [maps to v1.13 or later](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) with Mesh CA to Certificate Authority Service.



## Limitations

In-place CA migrations and upgrades are only supported from Cloud Service Mesh v1.13 or later. For managed control plane migrations, ensure the chosen channel [maps to v1.13 or later](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel).

## Prerequisites

Before following the steps in this guide, ensure you have:

  * [Granted cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Configured `gcloud`](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#configure_gcloud)



Additionally, ensure you are currently on Cloud Service Mesh v1.13 or later.

### Required tools

During the migration, you run a Google-provided tool, `migrate_ca`. This tool has the following dependencies:

  * `awk`
  * `grep`
  * `jq`
  * `kubectl`
  * `head`
  * `sed`
  * `tr`
  * [`yq`](https://github.com/mikefarah/yq#install)



Before downloading the `migrate_ca` tool, follow the steps in Prepare for your migration.

## Overview of the migration

During the migration process, authentication and authorization are fully functional between workloads using the previous CA and workloads using the new CA.

The `migrate_ca` migration tool will create a Kubernetes configuration map to track the status of CA migration per installed Cloud Service Mesh revision/channel. This is a privileged resource installed in the `istio-system` namespace.
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      Name: asm-ca-migration-<revision>
    Data:
      revision:
      start_time:
      state_update_time:
      current_state: TRUSTANCHOR_INJECT | MIGRATE_CA | ROLLBACK
      old_ca:
      target_ca:
    

The migration tool will backup the Istio MeshConfig config map before amending it and attempts to migrate the CA configuration using the [`ProxyConfig`](https://istio.io/latest/docs/reference/config/networking/proxy-config/) CRD when possible.

The following is an outline of the CA migration:

**Note:** You must perform the migration steps on each cluster in your mesh.

  1. Prepare for your migration.

  2. Initialize the new CA.

  3. Add mesh-wide trustAnchors for all clusters in the fleet.

  4. Migrate the CA.

  5. Perform a rollback.




## Prepare for your migration

  1. Download the `migrate_ca` bash tool:
         
         curl  https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-service-mesh-packages/main/scripts/migration/ca-migration/migrate_ca > migrate_ca
         

  2. Make the tool executable:
         
         chmod +x migrate_ca
         

  3. Set up the working directory:
         
         ./migrate_ca setup --output_dir OUTPUT_DIR
         

**Note:** If you do not specify a working directory, then a temporary one will be created. You will need to use it as the working directory for all subsequent steps.
  4. Change the working directory to the OUTPUT_DIR specified in the previous step
         
         cd OUTPUT_DIR
         

  5. Run the following command to ensure that all of the prerequisites are met:
         
         ./migrate_ca check-prerequisites
         

  6. Make note of the revision (`ASM_REVISION`) of the control plane associated with the previous CA that is being migrated. The steps required depend on the type of control plane, either in-cluster or managed.

### In-cluster
         
         asm-revision=$(kubectl get deploy -n istio-system -l app=istiod -o \
          "jsonpath={.items[*].metadata.labels[istio\.io/rev']}{'\n'}")
         

### Managed

Refer to the [channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) already installed.

  7. Since the in-place CA migration requires you to restart your workloads, ensure that the [Pod Disruption Budget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) is correctly configured and all applications whose CA needs to be migrated have more than one running Pod.

  8. Ensure that the cluster is already [registered to a fleet](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/anthos-service-mesh-prerequisites#fleet_requirements) and that workload-identity is enabled on the cluster. Then, make note of the fleet project ID as (`FLEET_ID`) for future steps.

  9. The tool accepts `kubeConfig` and `kubeContext` to select the cluster where the operations are performed. If these arguments are not passed in, then the default context/config are used.

     * To add the credentials of a GKE cluster to the `kubeConfig`, use the following command:
           
           gcloud container clusters get-credentials CLUSTER_NAME
           

     * To change the current `kubectl` context or to pass context to the tool, use the following command:
           
           kubectl config get-contexts
           kubectl config use-context CLUSTER_NAME
           




## Initialize the new CA

  1. The steps required to initialize the new CA depend on the new CA to which you are migrating. Perform these steps in every fleet cluster where you want to migrate the CA.

### Mesh CA

Call the utility tool `initialize` sub-command.

If you are specifying custom Kubernetes configurations:
         
         ./migrate_ca initialize --kubeconfig KUBECONFIG --kubecontext KUBECONTEXT --ca mesh_ca --old_ca OLD_CA_TYPE \
          --fleet_id FLEET_ID --revision ASM_REVISION
         

Otherwise:
         
         ./migrate_ca initialize --ca mesh_ca --old_ca OLD_CA_TYPE \
          --fleet_id FLEET_ID --revision ASM_REVISION
          ```
         

### CA Service

a. Follow the steps required to [initialize Certificate Authority Service](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-anthos-service-mesh#configure). Make note of the `CA_POOL`.

b. Call the utility tool `initialize` sub-command:

If you are specifying custom Kubernetes configurations:
         
         ./migrate_ca initialize --kubeconfig KUBECONFIG --context KUBECONTEXT --ca gcp_cas --ca-pool CA_POOL --ca-old OLD_CA_TYPE \
          --fleet-id FLEET_ID --revision ASM_REVISION
         

Otherwise:
         
         ./migrate_ca initialize --ca gcp_cas --ca-pool CA_POOL --ca-old OLD_CA_TYPE \
           --fleet-id FLEET_ID --revision ASM_REVISION
         




## Add mesh-wide trustAnchors for all clusters in the fleet

  1. Repeat the steps below for both the new CA and old CA for all clusters that are part of the fleet.

  2. Download the trustAnchors of the CA:

### Mesh CA
         
         ./migrate_ca download-trust-anchor --ca mesh_ca --ca_cert ROOT_CERT.pem
         

### CA Service

Store the CA certificate in a file:
         
         gcloud privateca pools get-ca-certs POOL_NAME --location=POOL_REGION --project=POOL_PROJECT--output-file ROOT_CERT.pem
         

  3. Add trustAnchors of the CA:
         
         ./migrate-ca add-trust-anchor --ca_cert ROOT_CERT.pem
         

  4. Verify that the trustAnchors have been received by all workloads in the fleet. In the namespaces argument, pass all the namespaces where workloads are deployed:
         
         ./migrate-ca check-trust-anchor --ca_cert ROOT_CERT.pem --namespaces NAMESPACES
         

Expected output:
         
         Check the CA cert in namespace nsa-1-24232                                                                                                                               
         a-v1-597f875788-52c5t.nsa-1-24232 trusts root-cert.pem
         




## Migrate the CA

  1. Migrate the CA configuration. The command required depends on the new CA to which you are migrating.

### Mesh CA
         
         ./migrate_ca migrate-ca --ca mesh_ca
         

### CA Service
         
         ./migrate_ca migrate-ca --ca gcp_cas --ca_pool CA_POOL
         

  2. Restart all the workloads.

**Note:** This step is optional if you have installed the [managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#managed-data-plane). This is because Google manages proxy lifetimes and automatically performs this step during a managed upgrade.

To minimize the risk of TLS traffic downtime, this step should impact the smallest number of workloads first. Only restart workloads that are associated with the control plane revision ASM_REVISION. For example, if all workloads in kubernetes namespace NAMESPACE are associated with the same Cloud Service Mesh control plane.
         
         kubectl rollout restart deployment -n NAMESPACE
         

  3. Verify that mTLS connections work between workloads in the restarted namespace and other workloads before repeating steps 1 and 2 for all namespaces and for all clusters that are part of the fleet. If newer workloads are coming up and mesh traffic is not interrupted, repeat steps 1 and 2 for all namespaces and clusters that are a part of the fleet. Otherwise, proceed to perform a rollback to rollback the newer CA configuration.

  4. Verify that the new CA configuration is being used by all workloads:
         
         ./migrate_ca verify-ca --ca_cert ROOT_CERT.pem --namespaces NAMESPACES
         

Expected output:
         
         Check the CA configuration in namespace nsb-2-76095
         b-v1-8ff557759-pds69.nsb-2-76095 is signed by root-cert.pem
         




## Perform a rollback

  1. Roll back the CA configuration and remove the newly configured trustAnchors:
         
         ./migrate-ca rollback
         

  2. Restart all the workloads. Ensure to only restart workloads that are associated with the control plane revision ASM_REVISION. For instance, if all workloads in kubernetes namespace NAMESPACES are associated with the same Cloud Service Mesh control plane.
         
         kubectl rollout restart deployment -n NAMESPACES
         

  3. (Optional) Verify that the older CA configuration is being used by all workloads.
         
         ./migrate-ca verify-ca --ca_cert older-root-cert.pem
         

  4. Repeat steps 1-3 for all clusters in the fleet where workloads use the ASM_REVISION control plane.




Congratulations! You've successfully performed an in-place CA migration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
