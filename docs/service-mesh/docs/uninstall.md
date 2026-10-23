---
url: https://docs.cloud.google.com/service-mesh/docs/uninstall/
title: Uninstall in-cluster Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:05.590438+00:00
---

# Uninstall in-cluster Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/uninstall/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Uninstall in-cluster Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

This page explains how to uninstall in-cluster Cloud Service Mesh if you are using the Istio APIs. If you are using Compute Engine APIs, no steps are necessary. See the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview) to understand the differences.

Following these instructions to uninstall in-cluster Cloud Service Mesh removes all configurations.

If you are uninstalling managed Cloud Service Mesh, follow the [managed uninstallation guide](https://docs.cloud.google.com/service-mesh/docs/uninstall-managed) instead.

If you are migrating from in-cluster to managed, follow the [Migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster) instead.

## Impact of removing Cloud Service Mesh

Before you uninstall Cloud Service Mesh, consider the capabilities that are removed from your cluster and workloads. When you remove Cloud Service Mesh proxies from your workloads and restart them, your applications revert to standard Kubernetes networking behavior.

### Security

When you remove Cloud Service Mesh, you lose the following security features:

  * **Mutual TLS (mTLS) encryption** : Traffic between services is no longer encrypted in transit with mTLS certificates managed by the mesh.
  * **Authorization policies** : Mesh `AuthorizationPolicy` custom resources are no longer enforced. You must configure Kubernetes `NetworkPolicy` resources or application-level authentication and authorization to restrict traffic.



### Observability

When you remove Cloud Service Mesh, you lose the following observability features:

  * **Telemetry and metrics** : Automatic collection of Layer 7 metrics (such as request rates, error rates, and latency) stops. Mesh telemetry is no longer automatically ingested into Cloud Monitoring. Standard GKE metrics are unaffected.
  * **Dashboards and SLOs** : Preconfigured Cloud Service Mesh dashboards and Service Level Objective (SLO) monitoring in the Google Cloud console are no longer populated.
  * **Access logging and tracing** : Sidecar proxy access logs with client mTLS identities and automated distributed traces are no longer generated.



### Service discovery and networking resiliency

When you remove Cloud Service Mesh, you lose the following networking and resiliency features:

  * **Network resiliency** : Workloads lose sidecar-level resiliency features, including automatic retries, configurable request timeouts, circuit breakers, outlier detection, and connection pool management. Applications must manage connection failures and retries directly.
  * **Multi-cluster service discovery** : Cross-cluster endpoint discovery and routing across multiple clusters in a fleet no longer function through the mesh. Services can only discover endpoints within their local cluster using standard DNS.



## Uninstall Cloud Service Mesh

Use the following commands to uninstall all Cloud Service Mesh components.

  1. To prevent interrupting application traffic:

     * Downgrade any STRICT mTLS policies to PERMISSIVE.
     * Remove any AuthorizationPolicy that may block traffic.
  2. Disable sidecar auto-injection on your namespace(s), if it is enabled. Run the following command to display namespace labels:
         
         kubectl get namespace YOUR_NAMESPACE --show-labels
         

The output is similar to the following:
         
         NAME   STATUS   AGE     LABELS
          demo   Active   4d17h   istio.io/rev=asm-181-5

If you see `istio.io/rev=` in the output under the `LABELS` column, remove it:
         
         kubectl label namespace YOUR_NAMESPACE istio.io/rev-
         

If you see `istio-injection` in the output under the `LABELS` column, remove it:
         
         kubectl label namespace YOUR_NAMESPACE istio-injection-
         

If you don't see either the `istio.io/rev` or `istio-injection` labels, then auto-injection wasn't enabled on the namespace.

**Note:** You should also check resources including Deployments, StatefulSets, ReplicaSets, DaemonSets, Jobs and CronJobs also for injection.
  3. Restart your workloads that have sidecars injected to remove the proxies.

  4. Delete the `validatingwebhooksconfiguration` and `mutatingwebhookconfiguration` from your cluster, if they exist:
         
         kubectl delete validatingwebhookconfiguration,mutatingwebhookconfiguration -l operator.istio.io/component=Pilot,istio.io/owned-by!=mesh.googleapis.com
         

  5. Once all workloads come up and no proxies are observed, then you can safely delete the in-cluster control plane to stop billing.

To remove the in-cluster control plane, run the following command:
         
         istioctl uninstall --purge
         

If there are no other control planes, you can delete the `istio-system` namespace to get rid of all Cloud Service Mesh resources. Otherwise, delete the services corresponding to the Cloud Service Mesh revisions. This avoids deleting shared resources, such as CRDs.

  6. Optionally, Remove Istio CRs, Isto CRDs, istio-(revision) configmap, asm-options configmap, `istio-system` and `asm-system` namespaces to remove service mesh from the cluster or use them in another Istio API compatible service mesh.

     1. Remove Istio CRs:
            
            kubectl delete gateways,virtualservices,destinationrules,serviceentries,envoyfilters,sidecars,peerauthentications,requestauthentications,authorizationpolicies,telemetries,wasmplugins,proxyconfigs --all --all-namespaces
            

     2. Remove Istio CRDs:
            
            kubectl get crds -o name | grep --color=never 'istio.io' | xargs kubectl delete
            

     3. Remove istio-(revision) configmap. You can skip this step if you delete the `istio-system` namespace.
            
            kubectl delete configmap istio-RELEASE_CHANNEL -n istio-system
            

Replace RELEASE_CHANNEL with your release channel

     4. Remove `istio-system` namespace:
            
            kubectl delete namespace istio-system --ignore-not-found=true
            

     5. Remove `asm-system` namespace:
            
            kubectl delete namespace asm-system --ignore-not-found=true
            

        1. Check if the deletions were successful:
               
               kubectl get ns
                ```
               
               The output should indicate a `Terminating` state and return as shown,
               otherwise you might have to manually delete any remaining resources in
               the namespaces and try again.
               
               ```sh
                NAME                 STATUS       AGE
                istio-system         Terminating  71m
                asm-system           Terminating  71m
                ```
               

  7. If you will delete your clusters, or have already deleted them, ensure that each cluster is [unregistered](https://docs.cloud.google.com/anthos/fleet-management/docs/unregister) from your fleet.

  8. If you plan to stop using Cloud Service Mesh at the fleet level, disable the service mesh feature for your fleet host project.
         
         gcloud container hub mesh disable --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.




Once you've completed these steps, all Cloud Service Mesh components, including proxies, in-cluster certificate authorities, and RBAC roles and bindings, are systematically removed from the cluster. During the installation process, a Google-owned service account is granted the necessary permissions to establish the service mesh resources within the cluster. These uninstall instructions don't revoke these permissions, allowing for a seamless re-activation of Cloud Service Mesh in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
