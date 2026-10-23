---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/ca-migration/
title: Canary-based Migration to Mesh CA \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:14.031820+00:00
---

# Canary-based Migration to Mesh CA  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/ca-migration/

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

# Canary-based Migration to Mesh CA

**Note:** This guide describes how to migrate from Istio CA to Mesh CA with a canary-based approach that involves minimal or no downtime. To migrate your CA with minimal downtime and without migrating control-planes, see [In-place CA Migration](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/in-place-ca-migration).

Migrating to Cloud Service Mesh certificate authority (Mesh CA) from [Istio CA](https://istio.io/docs/tasks/security/cert-management/plugin-ca-cert/) (also known as _Citadel_) requires migrating the [root of trust](https://docs.cloud.google.com/service-mesh/v1.20/docs/glossary#trust_domain). Prior to Cloud Service Mesh 1.10, if you wanted to migrate from Istio on Google Kubernetes Engine (GKE) to Cloud Service Mesh with Mesh CA, you needed to schedule downtime because Cloud Service Mesh was not able to load multiple root certificates. Therefore, during the migration, the newly deployed workloads trust the new root certificate, while others trust the old root certificate. Workloads using certificates signed by different root certificates can't authenticate with each other. This means that [mutual TLS](https://docs.cloud.google.com/service-mesh/v1.20/docs/glossary#mutual_tls) (mTLS) traffic is interrupted during the migration. The entire cluster only fully recovers when the control plane and all workloads in all namespaces are redeployed with Mesh CA's certificate. If your mesh has multiple clusters with workloads that send requests to workloads on another cluster, all workloads on those clusters need to be updated as well.

Use the steps in this guide for the following use cases:

  * Migrate from Istio on GKE to the Cloud Service Mesh 1.31.1-asm.19 in-cluster control plane with Mesh CA.
  * Upgrade from Cloud Service Mesh 1.15 or a 1.16 patch release with Istio CA to the Cloud Service Mesh 1.31.1-asm.19 in-cluster control plane with Mesh CA.



## Limitations

  * All GKE clusters must be in the _same_ Google Cloud project.



## Prerequisites

Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.20/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools) to: 

  * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.20/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.20/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.20/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.20/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster)



## Required tools

During the migration, you run a Google-provided tool, `migrate_ca`, to validate the following for each Pod in the cluster:

  * The root certificate for Istio CA and Mesh CA.
  * The workload mTLS certificate issued by Istio CA and by Mesh CA.
  * The trust domains configured by Istio CA and Mesh CA.



This tool has the following dependencies:

  * `awk`
  * `grep`
  * `istioctl` Running the `asmcli install` downloads the version of `istioctl` that matches the version of Cloud Service Mesh that you are installing.
  * `jq`
  * `kubectl`
  * `openssl`



## Overview of the migration

To migrate to Mesh CA, you follow the [revision-based](https://docs.cloud.google.com/service-mesh/v1.20/docs/glossary#revision) migration process (also referred to as a "canary upgrade"). With a revision-based migration, a new control plane revision is deployed alongside the existing control plane. You then gradually move your workloads to the new revision, which lets you monitor the effect of the migration through the process. During the migration process, authentication and authorization are fully functional between workloads using the Mesh CA and workloads using the Istio CA.

The following is an outline of the migration to Mesh CA:

  1. Distribute the Mesh CA root of trust.

     1. Install a new control plane revision that uses the Istio CA with an option that will distribute the Mesh CA root of trust.

     2. Migrate workloads to the new control plane, namespace by namespace, and test your application. When all workloads are successfully migrated to the new control plane, remove the old control plane.

  2. Migrate to Mesh CA. Now that all sidecar proxies are configured with the old root of trust and the Mesh CA root of trust, you can migrate to Mesh CA without downtime. Again, you follow the revision-based migration process:

     1. Install a control plane revision with Mesh CA enabled.

     2. Migrate workloads to the new control plane revision, namespace by namespace, and test your application. When all workloads are successfully migrated to the new control plane, remove the old control plane.

     3. Remove CA secrets in the cluster that are associated with the old CA and restart the new control plane.




## Distribute the Mesh CA root of trust

Before you can migrate to Mesh CA, _all_ GKE clusters in the mesh must have Cloud Service Mesh 1.10 or later, and all clusters must be configured with a control plane option that triggers the root of trust for Mesh CA to be distributed to the proxies of all workloads on the cluster. When the process is finished, each proxy is configured with both the old and the new root of trusts. With this scheme, when you migrate to Mesh CA, workloads using Mesh CA will be able to authenticate with workloads using the old CA.

### Install a new control plane revision

Install a control plane revision with an option that distributes the Mesh CA root of trust.

  1. Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools) to get ready to use a Google-provided tool, `asmcli`, to install the new control plane revision.

  2. Make sure you have the version of `asmcli` that installs Cloud Service Mesh 1.11 or higher:
         
         ./asmcli --version
         

  3. Run `asmcli install`. In the following command, replace the placeholders with your values.
         
         ./asmcli install \
            --fleet_id FLEET_PROJECT_ID \
            --kubeconfig KUBECONFIG_FILE \
            --enable_all \
            --ca citadel \
            --ca_cert CA_CERT_FILE_PATH \
            --ca_key CA_KEY_FILE_PATH \
            --root_cert ROOT_CERT_FILE_PATH \
            --cert_chain CERT_CHAIN_FILE_PATH \
            --option ca-migration-citadel \
            --revision_name REVISION_1 \
            --output_dir DIR_PATH
         



  * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
  * `--kubeconfig` The path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. 
  * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains, `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
  * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference#enablement_flags) Allows the tool to: 
    * Grant required IAM permissions.
    * Enable the required Google APIs.
    * Set a label on the cluster that identifies the mesh.
    * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.

  * `-ca citadel` To avoid downtime, specify Istio CA (the `citadel` option corresponds to Istio CA). Don't switch to Mesh CA at this point.
  * `--ca_cert` The intermediate certificate.
  * `--ca_key` The key for the intermediate certificate
  * `--root_cert` The root certificate.
  * `--cert_chain` The certificate chain.
  * `--option ca-migration-citadel` When you [redeploy your workloads](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-anthos-service-mesh#deploy_and_redeploy_workloads), this option triggers the new root of trust to be distributed to the sidecar proxies of the workloads.
  * `REVISION_1`: Recommended. A [revision label](https://docs.cloud.google.com/service-mesh/v1.20/docs/revisions-overview) is a key-value pair that is set on the control plane. The revision label key is always `istio.io/rev`. By default, the tool sets the value for the revision label based on the Cloud Service Mesh version, for example: `asm-1311-19`. We recommend that you include this option and replace `REVISION_1` with a name that describes the installation, such as `asm-1311-19-distribute-root`. The name must be a DNS-1035 label, and it must consist of lower case alphanumeric characters or `-`, start with an alphabetic character, and end with an alphanumeric character (such as `my-name` or `abc-123`).



### Migrate workloads to the new control plane

To finish distributing the new root of trust, you need to label your namespaces with the revision label `istio.io/rev=<var>REVISION_1</var>-distribute-root` and restart your workloads. When testing your workloads after restarting them, you run a tool to validate that the sidecar proxy is configured with both the old and new root of trust for Mesh CA.

  1. Set the current context for `kubectl`. In the following command, change `--region` to `--zone` if you have a single-zone cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --project=PROJECT_ID \
             --region=CLUSTER_LOCATION
         

  2. Download the validation tool:
         
         curl https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-service-mesh-packages/master/scripts/ca-migration/migrate_ca > migrate_ca
         

  3. Set the executable bit on the tool:
         
         chmod +x migrate_ca
         

  4. The `migrate_ca` tool calls `istioctl`, which is version dependent. The `asmcli` tool adds a symlink to `istioctl` in the directory you specified for `--output_dir`. Make sure that directory is at the beginning of your path. In the following command, replace `ISTIOCTL_PATH` with the directory that contains `istioctl` that the tool downloaded.
         
         export PATH=ISTIOCTL_PATH:$PATH
         which istioctl
         echo $PATH
         

  5. Get the revision label that is on `istiod` and the `istio-ingressgateway`.
         
         kubectl get pod -n istio-system -L istio.io/rev
         

The output is similar to the following:
         
         NAME                                                             READY   STATUS    RESTARTS   AGE   REV
         istio-ingressgateway-5fd454f8ff-t7w9x                            1/1     Running   0          36m   default
         istio-ingressgateway-asm-195-2-distribute-root-c6ccfbdbd-z2s9p   1/1     Running   0          18m   asm-195-2-distribute-root
         istio-ingressgateway-asm-195-2-distribute-root-c6ccfbdbd-zr2cs   1/1     Running   0          18m   asm-195-2-distribute-root
         istiod-68bc495f77-shl2h                                          1/1     Running   0          36m   default
         istiod-asm-195-2-distribute-root-6f764dbb7c-g9f8c                1/1     Running   0          18m   asm-195-2-distribute-root
         istiod-asm-195-2-distribute-root-6f764dbb7c-z7z9s                1/1     Running   0          18m   asm-195-2-distribute-root

     1. In the output, under the `REV` column, note the value of the revision label for the new revision, which matches the revision label that you specified when you ran `asmcli install`. In this example, the value is `asm-1311-19-distribute-root`.

     2. You need to delete the old revision of `istiod` when you finish moving workloads to the new revision. Note the value in the revision label for the old `istiod` revision. The example output shows a migration from Istio, which is using the `default` revision.

  6. Add the revision label to a namespace and remove the `istio-injection` label (if it exists). In the following command, replace `NAMESPACE` with the namespace to label.
         
         kubectl label namespace NAMESPACE istio.io/rev=REVISION_1 istio-injection- --overwrite

If you see `"istio-injection not found"` in the output, you can ignore it. That means that the namespace didn't previously have the `istio-injection` label. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  7. Restart the Pods to trigger re-injection.
         
         kubectl rollout restart deployment -n NAMESPACE
         

  8. Test your application to verify that the workloads are working correctly.

  9. If you have workloads in other namespaces, repeat the steps to label the namespace and restart Pods.

  10. Validate that the sidecar proxies for all workloads on the cluster are configured with both the old and new root certificates:
         
         ./migrate_ca check-root-cert
         

Expected output:
         
         Namespace: foo
         httpbin-66cdbdb6c5-pmzps.foo trusts [CITADEL MESHCA]
         sleep-64d7d56698-6tmjm.foo trusts [CITADEL MESHCA]

  11. If you need to migrate gateways, follow the steps in [Canary Upgrades (advanced)](https://docs.cloud.google.com/service-mesh/v1.20/docs/gateways#canary_upgrades_advanced) to install new gateway deployments. Keep the following points in mind:

     * Use `REVISION_1` as the revision label.
     * Deploy the gateway resources in the same namespace as the gateway from the older installation **to perform zero-downtime migration**. Ensure that the service resources pointing to the older gateway should include the newer deployments now as well.
     * Do not delete the older gateway deployments until you are sure your application is working properly (after the next step).
  12. If you are satisfied that your application is working as expected, continue with the steps to transition to the new version of `istiod`. If there's an issue with your application, follow the steps to rollback.

### Complete the transition

If you are satisfied that your application is working as expected, remove the old control plane to complete the transition to the new version.

     1. Change to the directory where the files from the `anthos-service-mesh` GitHub repository are located.

     2. Configure the validating webhook to use the new control plane.
            
            kubectl apply -f asm/istio/istiod-service.yaml
            

     3. Delete the old `istio-ingressgateway`Deployment. The command that you run depends on whether you are migrating from Istio or upgrading from a previous version of Cloud Service Mesh:

### Migrate

If you migrated from Istio, the old `istio-ingressgateway` doesn't have a revision label.
            
            kubectl delete deploy/istio-ingressgateway -n istio-system
            

### Upgrade

If you upgraded from a previous Cloud Service Mesh version, in the following command, replace `OLD_REVISION` with the revision label for the previous version of the `istio-ingressgateway`.
            
            kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=OLD_REVISION -n istio-system --ignore-not-found=true
            

     4. Delete the old revision of `istiod`. The command that you use depends on whether you are migrating from Istio or upgrading from a previous version of Cloud Service Mesh.

### Migrate

If you migrated from Istio, the old `istio-ingressgateway` doesn't have a revision label.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod -n istio-system --ignore-not-found=true
            

### Upgrade

If you upgraded from a previous Cloud Service Mesh version, in the following command, make sure that `OLD_REVISION` matches the revision label for the previous version of `istiod`.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-OLD_REVISION -n istio-system --ignore-not-found=true
            

     5. Remove the old version of the `IstioOperator` configuration.
            
            kubectl delete IstioOperator installed-state-OLD_REVISION -n istio-system
            

The expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-OLD_REVISION" deleted

### Rollback

If you encountered an issue when testing your application with the new version of `istiod`, follow these steps to rollback to the previous version:

     1. Delete the new gateway deployments installed as part of step 11.

     2. Relabel your namespace to enable auto-injection with the previous version of `istiod`. The command that you use depends on whether you used a revision label or `istio-injection=enabled` with the previous version.

        * If you used a revision label for auto-injection:
              
              kubectl label namespace NAMESPACE istio.io/rev=OLD_REVISION --overwrite
              

        * If you used `istio-injection=enabled`:
              
              kubectl label namespace NAMESPACE istio.io/rev- istio-injection=enabled --overwrite
              

Expected output:
    
    namespace/NAMESPACE labeled

     3. Confirm that the revision label on the namespace matches the revision label on the previous version of `istiod`:
            
            kubectl get ns NAMESPACE --show-labels
            

     4. Restart the Pods to trigger re-injection so the proxies have the previous version:
            
            kubectl rollout restart deployment -n NAMESPACE
            

     5. Remove the new `istio-ingressgateway` Deployment.
            
            kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=REVISION_1 -n istio-system --ignore-not-found=true
            

     6. Remove the new revision of `istiod`.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-REVISION_1 -n istio-system --ignore-not-found=true
            

     7. Remove the new `IstioOperator` configuration.
            
            kubectl delete IstioOperator installed-state-asm-1311-19-distribute-root -n istio-system
            

Expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-asm-1311-19-distribute-root" deleted




## Migrate to Mesh CA

Now that the sidecar proxies for all workloads are configured with both the old root of trust and the new root of trust for Mesh CA, the steps to migrate to Mesh CA are similar to those that you did to distribute the Mesh CA root of trust:

### Install a new control plane with Mesh CA enabled

You use `asmcli install` to install a new control plane revision that has Mesh CA enabled.

  1. If you customized the previous installation, you need to specify the same [overlay files](https://docs.cloud.google.com/service-mesh/v1.20/docs/glossary#overlay_file) when you run `asmcli install`.

  2. Run `asmcli install`. In the following command, replace the placeholders with your values.
         
         ./asmcli install \
            --fleet_id FLEET_PROJECT_ID \
            --kubeconfig KUBECONFIG_FILE \
            --output_dir DIR_PATH \
            --enable_all \
            --ca mesh_ca \
            --root_cert ROOT_CERT_FILE_PATH \
            --cert_chain CERT_CHAIN_FILE_PATH
            --option ca-migration-meshca \
           --revision_name REVISION_2 \
           --output_dir DIR_PATH \
           OVERLAYS
         

       * `--fleet_id` The project ID of the [ fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
       * `--kubeconfig` The path to the [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here. 
       * `--output_dir` Include this option to specify a directory where `asmcli` downloads the `anthos-service-mesh` package and extracts the installation file, which contains `istioctl`, samples, and manifests. Otherwise `asmcli` downloads the files to a `tmp` directory. You can specify either a relative path or a full path. The environment variable `$PWD` doesn't work here.
       * [ `--enable_all`](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference#enablement_flags) Allows the tool to: 
         * Grant required IAM permissions.
         * Enable the required Google APIs.
         * Set a label on the cluster that identifies the mesh.
         * [ Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.

       * `--ca mesh_ca` You can now switch to Mesh CA since the Mesh CA root of trust has been distributed.
       * `REVISION_2` Recommended. Replace `REVISION_2` with a name that describes the installation, such as `asm-1311-19-meshca-ca-migration`. The name must be a DNS-1035 label, and it must consist of lower case alphanumeric characters or `-`, start with an alphabetic character, and end with an alphanumeric character (such as `my-name` or `abc-123`). 
       * `--option ca-migration-migration` When you [redeploy your workloads](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-anthos-service-mesh#deploy_and_redeploy_workloads), this option configures the proxies to use the Mesh CA root of trust.



### Migrate workloads to the new control plane

To finish the installation, you need to label your namespaces with the new revision label and restart your workloads.

  1. Get the revision label that is on `istiod` and the `istio-ingressgateway`.
         
         kubectl get pod -n istio-system -L istio.io/rev
         

The output is similar to the following:
         
         NAME                                                                          READY   STATUS    RESTARTS   AGE   REV
         istio-ingressgateway-asm-1311-19-distribute-root-65d884685d-6hrdk      1/1     Running   0          67m   asm-1311-19-distribute-root
         istio-ingressgateway-asm-1311-19-distribute-root65d884685d-94wgz       1/1     Running   0          67m   asm-1311-19-distribute-root
         istio-ingressgateway-asm-1311-19-meshca-ca-migration-8b5fc8767-gk6hb   1/1     Running   0          5s    asm-1311-19-meshca-ca-migration
         istio-ingressgateway-asm-1311-19-meshca-ca-migration-8b5fc8767-hn4w2   1/1     Running   0          20s   asm-1311-19-meshca-ca-migration
         istiod-asm-1311-19-distribute-root-67998f4b55-lrzpz                    1/1     Running   0          68m   asm-1311-19-distribute-root
         istiod-asm-1311-19-distribute-root-67998f4b55-r76kr                    1/1     Running   0          68m   asm-1311-19-distribute-root
         istiod-asm-1311-19-meshca-ca-migration-5cd96f88f6-n7tj9                1/1     Running   0          27s   asm-1311-19-meshca-ca-migration
         istiod-asm-1311-19-meshca-ca-migration-5cd96f88f6-wm68b                1/1     Running   0          27s   asm-1311-19-meshca-ca-migration

     1. In the output, under the `REV` column, note the value of the revision label for the new version. In this example, the value is `asm-1311-19-meshca-ca-migration`.

     2. Also note the value in the revision label for the old `istiod` version. You need this to delete the old version of `istiod` when you finish moving workloads to the new version. In the example, the value of the revision label for the previous revision is `asm-1311-19-distribute-root`.

  2. Add the new revision label to a namespace In the following command, replace `NAMESPACE` with the namespace to label.
         
         kubectl label namespace NAMESPACE istio.io/rev=REVISION_2 --overwrite
         

  3. Restart the Pods to trigger re-injection.
         
         kubectl rollout restart deployment -n NAMESPACE
         

  4. Test your application to verify that the workloads are working correctly. Make sure that mTLS communication works between workloads in the older namespace and workloads in the newer namespace.

  5. If you have workloads in other namespaces, repeat the steps to label the namespace and restart Pods.

  6. Follow the steps outlined in [In-place upgrades](https://docs.cloud.google.com/service-mesh/v1.20/docs/gateways#upgrading_gateways) to upgrade the older gateway deployments installed in step 11 of the previous section to the latest revision `REVISION_2`.

  7. If you are satisfied that your application is working as expected, continue with the steps to transition to the new control plane. If there's an issue with your application, follow the steps to rollback.

### Complete the transition

If you are satisfied that your application is working as expected, remove the old control plane to complete the transition to the new version.

     1. Change to the directory where the files from the `anthos-service-mesh` GitHub repository are located.

     2. Configure the validating webhook to use the new control plane.
            
            kubectl apply -f asm/istio/istiod-service.yaml
            

     3. Delete the old `istio-ingressgateway`Deployment. In the following command, replace `OLD_REVISION` with the revision label for the previous version of the `istio-ingressgateway`.
            
            kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=OLD_REVISION -n istio-system --ignore-not-found=true
            

     4. Delete the old `istiod` revision. In the following command, replace `OLD_REVISION` with the revision label for the previous version of `istiod`.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-OLD_REVISION -n istio-system --ignore-not-found=true
            

     5. Remove the old `IstioOperator` configuration.
            
            kubectl delete IstioOperator installed-state-OLD_REVISION -n istio-system
            

The expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-OLD_REVISION" deleted

### Rollback

If you encountered an issue when testing your application with the new `istiod` revision, follow these steps to rollback to the previous revision:

     1. Follow the steps in [In-place upgrades](https://docs.cloud.google.com/service-mesh/v1.20/docs/gateways#upgrading_gateways) to downgrade the gateway deployments previously upgraded in step 6 of this section to the older revision `REVISION_1`.

     2. Relabel your namespace to enable auto-injection with the previous `istiod` revision.
            
            kubectl label namespace NAMESPACE istio.io/rev=OLD_REVISION --overwrite
            

Expected output:
            
            namespace/NAMESPACE labeled

     3. Confirm that the revision label on the namespace matches the revision label on the previous version of `istiod`:
            
            kubectl get ns NAMESPACE --show-labels
            

     4. Restart the Pods to trigger re-injection so the proxies have the previous version:
            
            kubectl rollout restart deployment -n NAMESPACE
            

     5. Remove the new `istio-ingressgateway` Deployment.
            
            kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=REVISION_2 -n istio-system --ignore-not-found=true
            

     6. Remove the new version of `istiod`. Make sure that the revision label in the following command matches your revision.
            
            kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-REVISION_2 -n istio-system --ignore-not-found=true
            

     7. Remove the new version of the `IstioOperator` configuration.
            
            kubectl delete IstioOperator installed-state-REVISION_2 -n istio-system
            

Expected output is similar to the following:
            
            istiooperator.install.istio.io "installed-state-REVISION_2" deleted




### Remove the CA secrets and restart the new control plane

  1. Preserve secrets just in case you need them:
         
         kubectl get secret/cacerts -n istio-system -o yaml > save_file_1
         kubectl get secret/istio-ca-secret -n istio-system -o yaml > save_file_2
         

  2. Remove the CA secrets in the cluster associated with the old CA:
         
         kubectl delete secret cacerts istio-ca-secret -n istio-system --ignore-not-found
         

  3. Restart the newly installed control plane. This makes sure the old root of trust is cleaned up from all workloads running in the mesh.
         
         kubectl rollout restart deployment -n istio-system
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
