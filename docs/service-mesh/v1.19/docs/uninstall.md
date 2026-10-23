---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/uninstall/
title: Uninstall Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:26.622463+00:00
---

# Uninstall Cloud Service Mesh  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/uninstall/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Uninstall Cloud Service Mesh

This page explains how to uninstall Cloud Service Mesh.

**Warning:** Following these instructions to uninstall Cloud Service Mesh removes all configurations regardless of control plane type (in-cluster or managed).

## Uninstall Cloud Service Mesh

Use the following commands to uninstall all Cloud Service Mesh components. These commands also delete the `istio-system` namespace and all custom resource definitions (CRDs), including any CRDs that you applied.

**Warning:** If you created CRDs, make sure you have copies of them before proceeding through the following steps.

  1. To prevent interruption of application traffic:

     * Downgrade any STRICT mTLS policies to PERMISSIVE.
     * Remove any AuthorizationPolicy that may block traffic.
  2. Disable Automatic Management on this cluster (whether you applied it directly or using the fleet-default configuration):
         
         gcloud container fleet mesh update --management manual
         

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

  5. If you're using managed Cloud Service Mesh, remove any `controlplanerevision` resources in the cluster:
         
         kubectl delete controlplanerevision RELEASE_CHANNEL -n istio-system
         

Where RELEASE_CHANNEL is the [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) you provisioned, such as `asm-managed`, `asm-managed-rapid`, or `asm-managed-stable`.

  6. Delete webhooks from your cluster, if they exist.

### In-cluster Cloud Service Mesh

Delete the `validatingwebhooksconfiguration` and `mutatingwebhookconfiguration`.
         
         kubectl delete validatingwebhookconfiguration,mutatingwebhookconfiguration -l operator.istio.io/component=Pilot
         

### Managed Cloud Service Mesh

A. Delete the `validatingwebhooksconfiguration`.
         
         kubectl delete validatingwebhookconfiguration istiod-istio-system-mcp
         

B. Delete the `mutatingwebhookconfiguration`.

**Note:** Use the `RELEASE_CHANNEL` according to the [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/release-channels) you provisioned. For example, Regular(`istiod-asm-managed`), Rapid (`istiod-asm-managed-rapid`), and Stable (`istiod-asm-managed-stable`).
         
         kubectl delete mutatingwebhookconfiguration istiod-RELEASE_CHANNEL
         

  7. Once all workloads come up and no proxies are observed, then you can safely delete the in-cluster control plane to stop billing. If you deployed a managed control plane, then it is automatically deleted with the previous step.

To remove the in-cluster control plane, run the command below:
         
         istioctl x uninstall --purge
         

If there are no other control planes, you can delete the `istio-system` namespace to get rid of all Cloud Service Mesh resources. Otherwise, delete the services corresponding to the Cloud Service Mesh revisions. This avoids deleting shared resources, such as CRDs.

  8. Delete the `istio-system` and `asm-system` namespaces:
         
         kubectl delete namespace istio-system asm-system --ignore-not-found=true
         

  9. Check if the deletions were successful:
         
         kubectl get ns
         

The output should indicate a `Terminating` state and return as shown, otherwise you might have to manually delete any remaining resources in the namespaces and try again.
         
         NAME                 STATUS       AGE
          istio-system         Terminating  71m
          asm-system           Terminating  71m
         

     1. If you will delete your clusters, or have already deleted them, ensure that each cluster is [unregistered](https://docs.cloud.google.com/anthos/fleet-management/docs/unregister) from your fleet.
  10. If you have enabled managed Cloud Service Mesh fleet-default configuration and want to disable it for future clusters, disable it. You can skip this step if you're only uninstalling from a single cluster.
         
         gcloud container hub mesh disable --fleet-default-member-config --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.

  11. If you're using managed Cloud Service Mesh, delete the `mdp-controller` deployment:
         
         kubectl delete deployment mdp-controller -n kube-system
         

  12. Check to see if the `istio-cni-plugin-config` configmap is present:
         
         kubectl get configmap istio-cni-plugin-config -n kube-system
         

If present, delete the `istio-cni-plugin-config` configmap:
         
         kubectl delete configmap istio-cni-plugin-config -n kube-system
         

**Warning:** The network reliability of your GKE cluster may be impacted if you don't delete this configmap.
  13. Delete the `istio-cni-node` daemonset:
         
         kubectl delete daemonset istio-cni-node -n kube-system
         




Upon completion of these steps, all Cloud Service Mesh components, including proxies, in-cluster certificate authorities, and RBAC roles and bindings, are systematically removed from the cluster. During the installation process, a Google-owned service account is granted the necessary permissions to establish the service mesh resources within the cluster. These uninstall instructions don't revoke these permissions, allowing for a seamless re-activation of Cloud Service Mesh in the future.

**Note:** The `istio-system` namespace and config maps may also continue to be recreated. If you require all of these artifacts to get removed, [contact support](https://docs.cloud.google.com/service-mesh/v1.19/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
