---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/uninstall-managed/
title: Uninstall managed Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:31:16.166593+00:00
---

# Uninstall managed Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/uninstall-managed/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Uninstall managed Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview).

This page explains how to uninstall managed Cloud Service Mesh. If you are uninstalling in-cluster Cloud Service Mesh, follow the [in-cluster uninstallation guide](https://docs.cloud.google.com/service-mesh/v1.30/docs/uninstall) instead.

**Warning:** This uninstallation method does not support uninstalling Cloud Service Mesh configured with the Kubernetes Gateway APIs.

If you are using a legacy setup with multiple control planes provisioned, then following these instructions removes all provisioned control planes.

Control planes managed by `asmcli` are not supported for uninstallation, but clusters that have either `asmcli --managed` or mesh API-managed control planes are supported. If you are unsure of the control plane, run the following command:
    
    
    kubectl get controlplanerevisions -n istio-system -l 'app.kubernetes.io/created-by!=asmcli'
    

Uninstallation is supported if any item listed in the output.

**Caution:** Cancelling the uninstallation is not supported. You must wait for the uninstallation to finish before provisioning managed Cloud Service Mesh on GKE.

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

  1. To prevent interruption of application traffic:

     * Downgrade any STRICT mTLS policies to PERMISSIVE.
     * Remove any AuthorizationPolicy that may block traffic.
  2. Disable multi-cluster if there are any other clusters running endpoint discovery on the cluster you are uninstalling.
         
         kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"manual"}}'
         

  3. Find secrets requiring cleanup, then delete them:
         
         kubectl get secrets -n istio-system -l istio/multiCluster=true
         
         
         kubectl delete secret SECRET_NAME
         

Where SECRET_NAME is the name of the secret. Repeat this step for each secret listed.

  4. Disable sidecar auto-injection on your namespace(s), if it is enabled. Run the following command to display namespace labels:
         
         kubectl get namespace YOUR_NAMESPACE --show-labels
         

The output is similar to the following:
         
         NAME   STATUS   AGE     LABELS
          demo   Active   4d17h   istio.io/rev=asm-181-5

     1. If you see `istio.io/rev=` in the output under the `LABELS` column, remove it:
            
            kubectl label namespace YOUR_NAMESPACE istio.io/rev-
            

     2. If you see `istio-injection` in the output under the `LABELS` column, remove it:
            
            kubectl label namespace YOUR_NAMESPACE istio-injection-
            

     3. If you don't see either the `istio.io/rev` or `istio-injection` labels, then auto-injection wasn't enabled on the namespace.

**Note:** You should also check resources including Deployments, StatefulSets, ReplicaSets, DaemonSets, Jobs and CronJobs also for injection.
  5. Restart your workloads that have sidecars injected to remove the proxies.

  6. Verify that no proxies are connected to the managed control plane:
         
         kubectl get pods --all-namespaces -o json | jq -r '
           .items[] |
           select(
              .spec.containers[].env[]? |
              select(.name == "PROXY_CONFIG" and (.value | contains("\"discoveryAddress\":\"meshconfig.googleapis.com:443\"")))
           ) |
           "\(.metadata.namespace)\t\(.metadata.name)"
           '
         

  7. Update the mesh feature membership spec management to `not-installed`:
         
         gcloud alpha container fleet mesh update \
            --project FLEET_PROJECT_ID \
            --memberships MEMBERSHIP_NAME \
            --location MEMBERSHIP_LOCATION \
            --management not-installed
         

Replace the following:

     * MEMBERSHIP_NAME is the membership name listed when you verified that your cluster was registered to the fleet.
     * MEMBERSHIP_LOCATION is the location of your membership (either a region, or `global`).
  8. Verify the mesh feature membership state for control plane state is `DISABLED`.
         
         gcloud container fleet mesh describe --project FLEET_PROJECT_ID
         

The output is similar to:
         
         servicemesh:
            controlPlaneManagement:
              details:
              - code: DISABLED
                details: Control Plane Management is not enabled.
              state: DISABLED
            dataPlaneManagement:
              details:
              - code: DISABLED
                details: Data Plane Management is not enabled.
              state: DISABLED
          state:
            description: 'Please see https://cloud.google.com/service-mesh/v1.30/docs/install for instructions to onboard to Anthos Service Mesh.'
         ...
         

If the control plane state is `DEPROVISIONING`, check again after a few minutes.

     1. If the control plane state is `STALLED`, the uninstallation is blocked from operating because of an internal error condition. If the issue persists, [contact Support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).
  9. Optionally, Remove Istio CRs, Istio CRDs, istio-(revision) configmap, asm-options configmap and `istio-system` namespace to remove service mesh from the cluster or use them in another Istio API compatible service mesh.

     1. Remove Istio CRs:
            
            kubectl delete gateways,virtualservices,destinationrules,serviceentries,envoyfilters,sidecars,peerauthentications,requestauthentications,authorizationpolicies,telemetries,wasmplugins,proxyconfigs --all --all-namespaces
            

     2. Remove Istio CRDs:
            
            kubectl get crds -o name | grep --color=never 'istio.io' | xargs kubectl delete
            

     3. Remove istio-(revision) configmap. You can skip this step if you delete the `istio-system` namespace.
            
            kubectl delete configmap istio-RELEASE_CHANNEL -n istio-system
            

Replace RELEASE_CHANNEL with your release channel (`asm-managed`, `asm-managed-stable`, or `asm-managed-rapid`).

     4. Remove asm-options configmap:
            
            kubectl delete configmap asm-options -n istio-system
            

     5. Remove `istio-system` namespace:
            
            kubectl delete namespace istio-system --ignore-not-found=true
            

     6. Check if the deletions were successful:
            
            kubectl get ns
            

The output should indicate a `Terminating` state and return as shown, otherwise you might have to manually delete any remaining resources in the namespaces and try again.
            
            NAME                 STATUS       AGE
            istio-system         Terminating  71m
            

  10. If you're using Certificate Authority Service, cleanup the permissions and CA pool created while [configuring Certificate Authority Service for Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/certificate-authority-service).

  11. If you enabled managed Cloud Service Mesh fleet-default configuration and want to disable it for future clusters, disable it. You can skip this step if you're only uninstalling from a single cluster.
         
         gcloud container hub mesh disable --fleet-default-member-config --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.

  12. If you plan to stop using Cloud Service Mesh at the fleet level, disable the service mesh feature for your fleet host project.
         
         gcloud container hub mesh disable --project FLEET_PROJECT_ID
         

Where FLEET_PROJECT_ID is the ID of your Fleet Host project.




Upon completion of these steps, all Cloud Service Mesh components, including proxies, certificate authorities, and RBAC roles and bindings, are systematically removed from the cluster. During the installation process, a Google-owned service account is granted the necessary permissions to establish the service mesh resources within the cluster. These uninstall instructions don't revoke these permissions, allowing for a seamless re-activation of Cloud Service Mesh in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
