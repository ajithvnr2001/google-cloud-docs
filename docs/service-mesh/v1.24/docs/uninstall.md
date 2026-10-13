---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/uninstall/
title: Uninstall Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:07.237632+00:00
---

# Uninstall Cloud Service Mesh  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/uninstall/

You are viewing archived v1.24 Service Mesh documentation.

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
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Uninstall Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

This page explains how to uninstall Cloud Service Mesh if you are using the Istio APIs. If you are using Compute Engine APIs, no steps are necessary. See the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview) to understand the differences.

Following these instructions to uninstall Cloud Service Mesh removes all configurations regardless of control plane type (in-cluster or managed). If you are doing a migration from in-cluster to managed, follow the [Migration guide](https://docs.cloud.google.com/service-mesh/v1.24/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster) instead.

## Uninstall Cloud Service Mesh

Use the following commands to uninstall all Cloud Service Mesh components. These commands also delete the `istio-system` namespace and all custom resource definitions (CRDs), including any CRDs that you applied.

**Warning:** If you created CRDs, make sure you have copies of them before proceeding through the following steps.

  1. To prevent interruption of application traffic:

     * Downgrade any STRICT mTLS policies to PERMISSIVE.
     * Remove any AuthorizationPolicy that may block traffic.
  2. Disable Automatic Management on this cluster (whether you applied it directly or using the fleet-default configuration):
         
         gcloud container fleet mesh update \
              --management manual \
              --memberships MEMBERSHIP_NAME \
              --project FLEET_PROJECT_ID \
              --location MEMBERSHIP_LOCATION
         

Replace the following:

     * MEMBERSHIP_NAME is the membership name listed when you verified that your cluster was registered to the fleet.
     * MEMBERSHIP_LOCATION is the location of your membership (either a region, or `global`).
  3. Disable sidecar auto-injection on your namespace(s), if it is enabled. Run the following command to display namespace labels:
         
         kubectl get namespace YOUR_NAMESPACE --show-labels
         

The output is similar to the following:
         
         NAME   STATUS   AGE     LABELS
          demo   Active   4d17h   istio.io/rev=asm-181-5

If you see `istio.io/rev=` in the output under the `LABELS` column, remove it:
         
         kubectl label namespace YOUR_NAMESPACE istio.io/rev-
         

If you see `istio-injection` in the output under the `LABELS` column, remove it:
         
         kubectl label namespace YOUR_NAMESPACE istio-injection-
         

If you don't see either the `istio.io/rev` or `istio-injection` labels, then auto-injection wasn't enabled on the namespace.

  4. Restart your workloads that have sidecars injected to remove the proxies.

  5. If you're using managed Cloud Service Mesh, check which [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-managed#identify_control_plane_implementation) you have in your cluster, this will help delete relevant resources in further steps.

  6. If you're using managed Cloud Service Mesh, remove all `controlplanerevision` resources in the cluster:
         
         kubectl delete controlplanerevision asm-managed asm-managed-rapid asm-managed-stable -n istio-system --ignore-not-found=true
         

  7. Delete webhooks from your cluster, if they exist.

### In-cluster Cloud Service Mesh

Delete the `validatingwebhooksconfiguration` and `mutatingwebhookconfiguration`.
         
         kubectl delete validatingwebhookconfiguration,mutatingwebhookconfiguration -l operator.istio.io/component=Pilot,istio.io/owned-by!=mesh.googleapis.com
         

### Managed Cloud Service Mesh

A. Delete the `validatingwebhooksconfiguration`.
         
         kubectl delete validatingwebhookconfiguration istiod-istio-system-mcp
         

B. Delete all `mutatingwebhookconfiguration`.

**Note:** Use the `RELEASE_CHANNEL` according to the [release channel](https://docs.cloud.google.com/service-mesh/v1.24/docs/managed/release-channels) you provisioned. For example, Regular(`istiod-asm-managed`), Rapid (`istiod-asm-managed-rapid`), and Stable (`istiod-asm-managed-stable`).
         
         kubectl delete mutatingwebhookconfiguration istiod-RELEASE_CHANNEL
         

  8. Once all workloads come up and no proxies are observed, then you can safely delete the in-cluster control plane to stop billing.

To remove the in-cluster control plane, run the following command:
         
         istioctl uninstall --purge
         

If there are no other control planes, you can delete the `istio-system` namespace to get rid of all Cloud Service Mesh resources. Otherwise, delete the services corresponding to the Cloud Service Mesh revisions. This avoids deleting shared resources, such as CRDs.

  9. Delete the `istio-system` and `asm-system` namespaces:
         
         kubectl delete namespace istio-system asm-system --ignore-not-found=true
         

  10. Check if the deletions were successful:
         
         kubectl get ns
         

The output should indicate a `Terminating` state and return as shown, otherwise you might have to manually delete any remaining resources in the namespaces and try again.
         
         NAME                 STATUS       AGE
          istio-system         Terminating  71m
          asm-system           Terminating  71m
         

  11. If you will delete your clusters, or have already deleted them, ensure that each cluster is [unregistered](https://docs.cloud.google.com/anthos/fleet-management/docs/unregister) from your fleet.

  12. If you enabled managed Cloud Service Mesh fleet-default configuration and want to disable it for future clusters, disable it. You can skip this step if you're only uninstalling from a single cluster.
         
         gcloud container hub mesh disable --fleet-default-member-config --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.

  13. If you plan to stop using Cloud Service Mesh at the fleet level, disable the service mesh feature for your fleet host project.
         
         gcloud container hub mesh disable --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.

  14. If you enabled managed Cloud Service Mesh, check and delete managed resources if they present:

**Note:** If your cluster is an `Autopilot` cluster, you cannot delete resources from the `kube-system` namespace. If you're uninstalling managed Cloud Service Mesh and you're keeping your cluster, [contact Support](https://docs.cloud.google.com/service-mesh/v1.24/docs/getting-support) to ensure that these resources are deleted.
     1. Delete the `mdp-controller` deployment:
            
            kubectl delete deployment mdp-controller -n kube-system
            

     2. If you have the `TRAFFIC_DIRECTOR` control plane implementation, clean up Transparent Health Check resources. Normally these are removed automatically, but you can make sure they are cleaned up by doing the following:

        1. Delete the `snk` daemonset.
               
               kubectl delete daemonset snk -n kube-system
               

        2. Delete the firewall rule.
               
               gcloud compute firewall-rules delete gke-csm-thc-FIRST_8_CHARS_OF_CLUSTER_ID
               

Replace the following:

           * FIRST_8_CHARS_OF_CLUSTER_ID is the first 8 characters of the Cluster ID for your specific cluster.
     3. Check to see if the `istio-cni-plugin-config` configmap is present:
            
            kubectl get configmap istio-cni-plugin-config -n kube-system
            

If present, delete the `istio-cni-plugin-config` configmap:
            
            kubectl delete configmap istio-cni-plugin-config -n kube-system
            

**Warning:** The network reliability of your GKE cluster may be impacted if you don't delete this configmap.
     4. Delete the `istio-cni-node` daemonset:
            
            kubectl delete daemonset istio-cni-node -n kube-system
            

  15. If you're uninstalling managed Cloud Service Mesh, [contact Support](https://docs.cloud.google.com/service-mesh/v1.24/docs/getting-support) to ensure that all Google Cloud resources are cleaned up. The `istio-system` namespace and config maps may also continue to be recreated if you don't follow this step.




Upon completion of these steps, all Cloud Service Mesh components, including proxies, in-cluster certificate authorities, and RBAC roles and bindings, are systematically removed from the cluster. During the installation process, a Google-owned service account is granted the necessary permissions to establish the service mesh resources within the cluster. These uninstall instructions don't revoke these permissions, allowing for a seamless re-activation of Cloud Service Mesh in the future.

**Note:** Some resources (e.g. Network Endpoint Groups or NEGs) will be orphaned after the systematic removal of these components. To err on the side of caution, Cloud Service Mesh must _fail open_ during clean up. This is to ensure that the uninstallation of managed Cloud Service Mesh never has a negative impact other networking resources in your project or on the workloads. To have these orphaned resources removed for the purposes of hygiene or "house cleaning", contact [Google Cloud Support](https://docs.cloud.google.com/service-mesh/v1.24/docs/getting-support)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
