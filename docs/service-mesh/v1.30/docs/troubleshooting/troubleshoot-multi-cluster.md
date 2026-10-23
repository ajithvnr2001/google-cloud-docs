---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-multi-cluster/
title: Resolving multi-cluster issues \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:24.781672+00:00
---

# Resolving multi-cluster issues  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-multi-cluster/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving multi-cluster issues

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

## Missing secrets

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.30/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This section only applies to the in-cluster control plane and the managed control plane with the Istiod implementation.

Cloud Service Mesh relies on a kubeconfig file embedded in the Kubernetes secret for proper remote endpoint discovery. Without the secrets, users will always see requests hit pods in the local cluster during cross-cluster load balancing.

Verify the secret has been created by running the following command in every cluster:
    
    
    kubectl get secret istio-remote-secret-CLUSTER_NAME_i -n istio-system
    

Verify the expected output:
    
    
    NAME                                   TYPE     DATA   AGE
    istio-remote-secret-CLUSTER_NAME_i   Opaque   1      44s
    

To recover from this, delete all the remote secrets and re-run the `create-mesh` command.

## Unreachable API server

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.30/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This section only applies to in-cluster control plane and managed (istiod implementation).

The control plane of Cloud Service Mesh needs to reach the API server of the remote cluster. The following situations can cause the remote cluster to become unreachable: 

  * The remote cluster is deleted.
  * The remote cluster is a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) that does not have [global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#enabling_control_plane_private_endpoint_global_access) enabled.
  * The remote cluster is a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) with [Master Authorized Network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) enabled but the Cloud Service Mesh control plane IP has not been properly allowed using the allow list.



Given an unreachable API server, Istiod will output error messages in the log. Users will always see requests hit the local pod during cross-cluster load balancing.

In the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) interface, set the query `resource.type` to `istio_control_plane`.

Check to see if there are any invalid secret errors.

To recover from this problem, fix the underlying API server reachability issue. Next, delete all the remote secrets in every cluster and re-run the `create-mesh` command.

## Missing firewall rule

Without the proper firewall rule, users will experience a 10-second delay followed by a timeout when doing cross-cluster load balancing.

To recover from this, follow the steps outlined in [Create firewall rule](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/gke-install-multi-cluster#create_firewall_rule).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
