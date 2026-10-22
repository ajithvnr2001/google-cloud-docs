---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops/
title: Troubleshooting and operations for Multi Cluster Ingress \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:26.892708+00:00
---

# Troubleshooting and operations for Multi Cluster Ingress  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshooting and operations for Multi Cluster Ingress Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Misconfigurations in [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) or its underlying Compute Engine resources can cause multi-cluster load balancing issues, such as incorrect traffic routing, missing Virtual IP addresses (VIPs), or `502` service errors.

Use this document to learn to inspect Compute Engine load balancer resources, diagnose VIP and `502` errors, manage config cluster migrations, and find common error codes.

This information is important for Platform admins and operators who manage Multi Cluster Ingress across multiple Google Kubernetes Engine (GKE) clusters. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand Multi Cluster Ingress resource mapping

The GKE Enterprise Ingress controller manages Compute Engine resources. `MultiClusterIngress` and `MultiClusterService` resources map to different Compute Engine resources, so understanding the relationship between these resources helps you troubleshoot. For example, examine the following `MultiClusterIngress` resource:
    
    
    apiVersion: extensions/v1beta1
    kind: MultiClusterIngress
    metadata:
      name: foo-ingress
    spec:
      template:
        spec:
          rules:
          - host: store.foo.com
            http:
              paths:
              - backend:
                  serviceName: store-foo
                  servicePort: 80
          - host: search.foo.com
            http:
              paths:
              - backend:
                  serviceName: search-foo
                  servicePort: 80
    

### Compute Engine to Multi Cluster Ingress resource mappings

The table below shows the mapping of fleet resources to resources created in the Kubernetes clusters and Google Cloud:

Kubernetes resource | Google Cloud resource | Description  
---|---|---  
MultiClusterIngress | Forwarding rule | HTTP(S) load balancer VIP.  
Target proxy | HTTP/S terminations settings taken from annotations and the TLS block.  
URL map | Virtual host path mapping from the rules section.  
MultiClusterService | Kubernetes Service | Derived resource from template.  
Backend service | A backend service is created for each (Service, ServicePort) pair.  
Network endpoint groups | Set of backend Pods participating in the Service.  
  
## Inspecting Compute Engine load balancer resources

After creating a load balancer, the Multi Cluster Ingress status will contain the names of every Compute Engine resource that was created to construct the load balancer. For example:
    
    
    Name:         shopping-service
    Namespace:    prod
    Labels:       <none>
    Annotations:  <none>
    API Version:  networking.gke.io/v1beta1
    Kind:         MultiClusterIngress
    Metadata:
      Creation Timestamp:  2019-07-16T17:23:14Z
      Finalizers:
        mci.finalizer.networking.gke.io
    Spec:
      Template:
        Spec:
          Backend:
            Service Name:  shopping-service
            Service Port:  80
    Status:
      VIP:  34.102.212.68
      CloudResources:
        Firewalls: "mci-l7"
        ForwardingRules: "mci-abcdef-myforwardingrule"
        TargetProxies: "mci-abcdef-mytargetproxy"
        UrlMap: "mci-abcdef-myurlmap"
        HealthChecks: "mci-abcdef-80-myhealthcheck"
        BackendServices: "mci-abcdef-80-mybackendservice"
        NetworkEndpointGroups: "k8s1-neg1", "k8s1-neg2", "k8s1-neg3"
    

## VIP not created

If you do not see a VIP, then an error may have occurred during its creation. To see if an error did occur, run the following command:
    
    
    kubectl describe mci shopping-service
    

The output may look similar to:
    
    
    Name:         shopping-service
    Namespace:    prod
    Labels:       <none>
    Annotations:  <none>
    API Version:  networking.gke.io/v1beta1
    Kind:         MultiClusterIngress
    Metadata:
      Creation Timestamp:  2019-07-16T17:23:14Z
      Finalizers:
        mci.finalizer.networking.gke.io
    Spec:
      Template:
        Spec:
          Backend:
            Service Name:  shopping-service
            Service Port:  80
    Status:
      VIP:  34.102.212.68
    Events:
      Type     Reason  Age   From                              Message
      ----     ------  ----  ----                              -------
      Warning  SYNC    29s   multi-cluster-ingress-controller  error translating MCI prod/shopping-service: exceeded 4 retries with final error: error translating MCI prod/shopping-service: multiclusterservice prod/shopping-service does not exist
    

In this example, the error was that the user did not create a `MultiClusterService` resource that was referenced by a `MultiClusterIngress`.

## 502 response

If your load balancer acquired a VIP but is consistently serving a 502 response, the load balancer health checks may be failing. Health checks could fail for two reasons:

  1. Application Pods are not healthy (see Cloud console debugging for example).
  2. A misconfigured firewall is blocking Google health checkers from performing health checks.



In the case of #1, make sure that your application is in fact serving a 200 response on the "/" path.

In the case of #2, make sure that a firewall named "mci-default-l7" exists in your VPC. The Ingress controller creates the firewall in your VPC to ensure Google health checkers can reach your backends. If the firewall does not exist, make sure there is no external automation that deletes this firewall upon its creation.

## Traffic not added to or removed from cluster

When adding a new Membership, traffic should reach the backends in the underlying cluster when applicable. Similarly, if a Membership is removed, no traffic should reach the backends in the underlying cluster. If you are not observing this behavior, check for errors on the `MultiClusterIngress` and `MultiClusterService` resource.

Common cases in which this error would occur include adding a new Membership on a GKE cluster that is not in VPC-native mode or adding a new Membership but not deploying an application in the GKE cluster.

  1. Describe the `MultiClusterService`:
         
         kubectl describe mcs zone-svc
         

  2. Describe the `MultiClusterIngress`:
         
         kubectl describe mci zone-mci
         




## Config cluster migration

To understand more about the use cases for migration, see the [Config cluster design concept](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#config_cluster_design).

Config cluster migration can be a disruptive operation if not handled correctly. Follow these guidelines when performing a config cluster migration:

  1. Make sure to use the [static-ip annotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-for-anthos#static) on your `MultiClusterIngress` resources. Failing to do so will result in disrupted traffic while migrating. Ephemeral IPs will be recreated when migrating config clusters.
  2. The `MultiClusterIngress` and `MultiClusterService` resources must be deployed identically to the existing and new config cluster. Differences between them will result in the reconciliation of `MultiClusterService` and `MultiClusterIngress` resources that are different in the new config cluster.
  3. Only a single config cluster is active at any time. Until the config cluster is changed, the `MultiClusterIngress` and `MultiClusterService` resources in the new config cluster will not impact load balancer resources.



To migrate the config cluster, run the following command:
    
    
      gcloud container fleet ingress update \
        --config-membership=projects/project_id/locations/global/memberships/new_config_cluster
    

Verify the command worked by ensuring there are no visible errors in the Feature state:
    
    
      gcloud container fleet ingress describe
    

## Console debugging

In most cases, checking the exact state of the load balancer is helpful when debugging an issue. You can find the load balancer by going to [Load balancing](https://console.cloud.google.com/net-services/loadbalancing/) in the Google Cloud console.

## Error/Warning codes

Multi Cluster Ingress emits error and warning codes on `MultiClusterIngress` and `MultiClusterService` resources as well as the gcloud `multiclusteringress` Description field for known issues. These messages have documented error and warning codes to make it easier to understand what it means when something is not operating as expected. Each code consists of an error ID in the format `AVMBR123` where `123` is a unique number that corresponds to an error or warning and suggestions on how to solve it.

### AVMBR101: `Annotation [NAME] not recognized`

This error displays when an annotation is specified on a `MultiClusterIngress` or `MultiClusterService` manifest that is not recognized. There are a couple reasons why the annotation might not be recognized:

  1. The annotation is not supported in Multi Cluster Ingress. This may be expected if annotating resources that are not expected to be used by the GKE Enterprise Ingress controller.

  2. The annotation is supported, but is misspelled and thus not recognized.




In both cases, please refer to documentation to understand the [supported annotations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress#annotations) and how they are specified.

### AVMBR102: `[RESOURCE_NAME] not found`

This error displays when a supplementary resource is specified in a `MultiClusterIngress` but cannot be found in the Config Membership. For example, this error is thrown when a `MultiClusterIngress` refers to a `MultiClusterService` that cannot be found or a `MultiClusterService` refers to a BackendConfig that cannot be found. There are a couple reasons why a resource could not be found:

  1. It is not in the proper namespace. Ensure that resources which reference each other are all in the same namespace.
  2. The resource name is misspelled.
  3. The resource truly does not exist with the proper namespace + name. In this case, please create it.



### AVMBR103: `[CLUSTER_SELECTOR] is invalid`

This error displays when a cluster selector specified on a `MultiClusterService` is invalid. There are a couple reasons why this selector could be invalid:

  1. The provided string contains a typo.
  2. The provided string refers to a cluster membership that no longer exists in the fleet.



### AVMBR104: `Cannot find NEGs for Service Port [SERVICE_PORT]`

This error is thrown when the NetworkEndpointGroup's (NEGs) for a given `MultiClusterService` and service port pair cannot be found. NEGs are the resources which contain the Pod endpoints in each of your backend clusters. The main reason why the NEGs might not exist is because there was an error creating or updating the Derived Services in your backend clusters. Check the Events on your `MultiClusterService` resource for more information.

### AVMBR105: `Missing GKE Enterprise license.`

This error displays under Feature state, and indicates that the GKE Enterprise API (anthos.googleapis.com) is not enabled.

### AVMBR106: `Derived service is invalid: [REASON].`

This error displays under the events of the `MultiClusterService` resource. One common reason for this error is that the Service resource derived from `MultiClusterService` has an invalid spec.

For example, this `MultiClusterService` does not have any `ServicePort` defined in its spec.
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterService
    metadata:
      name: zone-mcs
      namespace: whereami
    spec:
      clusters:
      - link: "us-central1-a/gke-us"
      - link: "europe-west1-c/gke-eu"
    

### AVMBR107: `Missing GKE cluster resource link in Membership.`

This error displays under Feature state and occurs because there is no GKE cluster underlying the Membership resource. You can verify this by running the following command:
    
    
    gcloud container fleet memberships describe membership-name
    

and ensuring that there is no GKE cluster resource link under the endpoint field.

### AVMBR108: `GKE cluster [NAME] not found.`

This error displays under Feature state and is thrown if the underlying GKE cluster for the Membership does not exist.

### AVMBR109: `[NAME] is not a VPC-native GKE cluster.`

This error displays under Feature state. This error is thrown if the specified GKE cluster is a route-based cluster. The Multi Cluster Ingress controller creates a container-native load balancer using NEGs. Clusters must be VPC-native to use a container-native load balancer.

For more information, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

### AVMBR110: `[IAM_PERMISSION] permission missing for GKE cluster [NAME].`

This error displays under Feature state. There are a couple reasons for this error:

  1. The underlying GKE cluster for the Membership is located in a different project from the Membership itself.
  2. The specified IAM permission was removed from the `MultiClusterIngress` service agent.



### AVMBR111: `Failed to get Config Membership: [REASON].`

This error displays under Feature state. The main reason this error occurs is because the Config Membership was deleted while the Feature is enabled.

You should never need to delete the Config Membership. If you would like to change it, follow the config cluster migration steps.

### AVMBR112: `HTTPLoadBalancing Addon is disabled in GKE Cluster [NAME].`

This error displays under Feature state and occurs when the `HTTPLoadBalancing` addon is disabled in a GKE cluster. You can update your GKE cluster to enable the `HTTPLoadBalancing` addon:
    
    
    gcloud container clusters update name --update-addons=HttpLoadBalancing=ENABLED
    

### AVMBR113: `This resource is orphaned.`

In some cases, the usefulness of a resource depends on it being referenced by another resource. This error is thrown when a Kubernetes resource is created but is not referenced by another resource. For example, you will see this error if you create a `BackendConfig` resource that is not being referenced by a `MultiClusterService`.

**Note:** This error also results from a known issue where Multi Cluster Ingress doesn't recognize when a `BackendConfig` is used by Ingress, but not by Multi Cluster Ingress.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
