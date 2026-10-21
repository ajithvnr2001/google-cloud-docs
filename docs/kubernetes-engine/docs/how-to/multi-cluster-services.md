---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services/
title: Configuring multi-cluster Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:52:19.508119+00:00
---

# Configuring multi-cluster Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configuring multi-cluster Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to enable and use multi-cluster Services (MCS). By using MCS, you can discover and invoke Kubernetes [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) across multiple Google Kubernetes Engine (GKE) clusters. MCS helps you build highly available and geographically distributed applications by making your Services resilient and scalable. When you export a Service with MCS, that Service is available across all of the clusters in your [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

This document is for Network engineers who manage networking across their clusters and teams. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more information about how MCS works and its benefits, see [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services).

**Note:** This document shows you how to configure MCS with a single project. For multi-project Shared VPC set-up, follow [Setting up multi-cluster Services with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks#two-service-projects-iam).

## Google Cloud resources managed by MCS

MCS manages the following components of Google Cloud:

  * **Cloud DNS** : MCS configures [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) zones and records for each exported Service in your [fleet clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation). This lets you connect to Services that are running in other clusters. These zones and records are created, read, updated, and deleted based on the Services that you choose to export across clusters.

**Note:** Using Cloud DNS incurs additional charges. You are billed according to [Cloud DNS pricing](https://cloud.google.com/dns/pricing).
  * **Firewall rules** : MCS configures firewall rules that let Pods communicate with each other across clusters within your fleet. Firewall rules are created, read, updated, and deleted based on the clusters that you add to your fleet. These rules are similar to the rules that GKE creates to enable communication between Pods within a GKE cluster.

  * **Traffic Director control plane** : MCS uses the [Traffic Director control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane-overview) to keep track of endpoints and their health across clusters.




## Requirements

MCS has the following requirements:

  * For MCS to function correctly, GKE deploys the `gke-mcs-importer` Pod to your nodes with elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb). These permissions allow the importer to manage endpoints, services, and ServiceImports to propagate service metadata across clusters in your fleet. The importer doesn't have permission to view or modify your deployments.

  * MCS only supports exporting services from VPC-native GKE clusters on Google Cloud. For more information, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). You cannot use non VPC-native GKE Standard clusters.

  * Connectivity between clusters depends on clusters running within the same VPC network, in peered or Shared VPC networks. If clusters are in separate, non-connected networks, calls to external services will be blocked. We recommend that you enable MCS in projects where the clusters are in the same VPC network. However, a fleet can't contain clusters from more than one Shared VPC network.

To set up MCS on a cross-project fleet with a Shared VPC, follow [Setting up multi-cluster Services with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks#two-service-projects-iam).

  * While a fleet might span multiple Google Cloud projects and VPC networks, a single multi-cluster service must be exported from a single project and a single VPC network.

  * MCS is not supported with [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

  * Clusters must have the `HttpLoadBalancing` add-on enabled. Ensure that the `HttpLoadBalancing` add-on is enabled. The `HttpLoadBalancing` add-on is enabled by default and shouldn't be disabled.




## Pricing

Multi-cluster Services is included as part of the [GKE cluster management fee](https://cloud.google.com/kubernetes-engine/pricing#google-kubernetes-engine-pricing) and has no extra cost for usage. You must enable the Traffic Director API, but MCS does not incur any Cloud Service Mesh endpoint charges.

## Before you begin

Before you start, make sure you have performed the following tasks:

  1. Install the [Google Cloud SDK](https://docs.cloud.google.com/sdk/downloads).

  2. Enable the Google Kubernetes Engine API:

[Enable Google Kubernetes Engine API](https://console.cloud.google.com/apis/library/container.googleapis.com?q=kubernetes%20engine)

  3. Connect your VPC networks with [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  4. Enable the MCS, fleet (hub), Resource Manager, Traffic Director, Cloud DNS, and connect gateway APIs:
         
         gcloud services enable \
             multiclusterservicediscovery.googleapis.com \
             gkehub.googleapis.com \
             cloudresourcemanager.googleapis.com \
             trafficdirector.googleapis.com \
             dns.googleapis.com \
             connectgateway.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the project ID from the project where you plan to register your clusters to a fleet.

**Note:** Non-project owners must be granted the `serviceusage.services.enable` permission before they can enable APIs.**Note:** To function properly, MCS requires the `connectgateway.googleapis.com` API. This API is enabled by default in Google Cloud projects, but make sure that it wasn't manually disabled.



## Enabling MCS in your project

MCS requires that participating GKE clusters be registered into the same fleet. Once the MCS feature is enabled for a fleet, any clusters can export Services between clusters in the fleet.

## Enabling MCS on your GKE cluster

  1. Enable the MCS feature for your project's fleet:
         
         gcloud container fleet multi-cluster-services enable \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID from the project where you plan to register your clusters to a fleet. This is your _fleet host project_.

Enabling multi-cluster services in the fleet host project creates or ensures that the `service-PROJECT_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com` service account exists.

  2. [Register your GKE clusters to the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke). We strongly recommend that you register your cluster with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled. If you do not enable Workload Identity Federation for GKE, you need to register the cluster with a Google Cloud service account for authentication, and complete the additional steps in Authenticating service accounts.

To register your cluster with Workload Identity Federation for GKE, run the following command:
         
         gcloud container fleet memberships register MEMBERSHIP_NAME \
            --gke-cluster CLUSTER_LOCATION/CLUSTER_NAME \
            --enable-workload-identity \
            --project PROJECT_ID
         

Replace the following:

     * `MEMBERSHIP_NAME`: the [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) that you choose to uniquely represent the cluster in the fleet. Typically, a cluster's fleet membership name is the cluster's name, but you might need to specify a new name if another cluster with the original name already exists in the fleet.
     * `CLUSTER_LOCATION`: the zone or region where the cluster is located.
     * `CLUSTER_NAME`: the name of the cluster.
  3. Grant the required Identity and Access Management (IAM) permissions for MCS Importer:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gke-mcs/sa/gke-mcs-importer" \
             --role "roles/compute.networkViewer"
         

Replace the following:

     * `PROJECT_ID`: the project ID from the fleet host project.
     * `PROJECT_NUMBER`: the project number from the fleet host project.
  4. Ensure that each cluster in the fleet has a namespace to share Services in. If needed, create a namespace by using the following command:
         
         kubectl create ns NAMESPACE
         

Replace `NAMESPACE` with a name for the namespace.

**Note:** Since Services are not imported to clusters where their exporting namespace is not present, create a Service's namespace in any clusters from which a Service will be consumed. If a namespace is missing, you can add the namespace at any time, but might take up to five minutes for a previously exported Service to be imported to a newly created namespace.
  5. To verify that MCS is enabled, run the following command:
         
         gcloud container fleet multi-cluster-services describe \
             --project PROJECT_ID
         

The output is similar to the following:
         
         createTime: '2021-08-10T13:05:23.512044937Z'
         membershipStates:
           projects/PROJECT_ID/locations/global/memberships/MCS_NAME:
             state:
               code: OK
               description: Firewall successfully updated
               updateTime: '2021-08-10T13:14:45.173444870Z'
         name: projects/PROJECT_NAME/locations/global/features/multiclusterservicediscovery
         resourceState:
           **state: ACTIVE**
         spec: {}
         

If the value of `state` is not `ACTIVE`, see the troubleshooting section.




### Authenticating service accounts

**Important:** You do not need to do any steps in this section if you registered a cluster to a fleet with Workload Identity Federation for GKE enabled.

If you registered your GKE clusters to a fleet using a service account, you need to take additional steps to authenticate the service account. MCS deploys a component called `gke-mcs-importer`. This component receives endpoint updates from Traffic Director control plane, so as part of enabling MCS you need to grant your [service account](https://docs.cloud.google.com/iam/docs/service-accounts) permission to read information from Cloud Service Mesh.

When you use a service account, you can use the Compute Engine default service account or your own node service account:

  * If you are using a [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), do the following:

    1. Enable the following scopes:

       * `https://www.googleapis.com/auth/compute.readonly`
       * `https://www.googleapis.com/auth/cloud-platform`

To learn more about enabling scopes, see [Changing the service account and access scopes for an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).

    2. Grant the `roles/compute.networkViewer` role on the project to the service account. To learn more about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).

  * If you are using your own node service account, grant the `roles/compute.networkViewer` role on the project to your service account. To learn more about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).




## Using MCS

The following sections show you how to use MCS. MCS uses the [Kubernetes multi-cluster services API](https://github.com/kubernetes/enhancements/tree/master/keps/sig-multicluster/1645-multi-cluster-services-api).

### Registering a Service for export

To register a Service for export to other clusters within your fleet, complete the following steps:

  1. Create a `ServiceExport` object named `export.yaml`:
         
         # export.yaml
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
          namespace: NAMESPACE
          name: SERVICE_EXPORT_NAME
         

Replace the following:

     * `NAMESPACE`: the namespace of the `ServiceExport` object. This namespace must match the namespace of the Service that you are exporting.
     * `SERVICE_EXPORT_NAME`: the name of a Service in your cluster that you want to export to other clusters within your fleet.
  2. Create the `ServiceExport` resource by running the following command:
         
         kubectl apply -f export.yaml
         




The initial export of your Service takes approximately five minutes to sync to clusters registered in your fleet. After a Service is exported, subsequent endpoint syncs happen immediately.

You can export the same Service from multiple clusters to create a single highly available multi-cluster service endpoint with traffic distribution across clusters. Before you export Services that have the same name and namespace, ensure that you want them to be grouped in this manner. We recommend against exporting services in the `default` and `kube-system` namespaces because of the high probability of unintended name conflicts and the resulting unintended grouping. If you are exporting more than five services with the same name and namespace, traffic distribution on imported services might be limited to five exported services.

### Consuming cross-cluster Services

MCS only supports ClusterSetIP and headless Services. Only DNS "A" records are available.

After you create a `ServiceExport` object, the following domain name resolves to your exported Service from any Pod in any fleet cluster:
    
    
     SERVICE_EXPORT_NAME.NAMESPACE.svc.clusterset.local
    

The output includes the following values:

  * `SERVICE_EXPORT_NAME` and `NAMESPACE`: the values you define in your `ServiceExport` object.



For ClusterSetIP Services, the domain resolves to the `ClusterSetIP`. You can find this value by locating the ServiceImport object in a cluster in the namespace that the ServiceExport object was created in. The ServiceImport object is automatically created.

For example:
    
    
    kind: ServiceImport
    apiVersion: net.gke.io/v1
    metadata:
     namespace: EXPORTED-SERVICE-NAMESPACE
     name: SERVICE-EXPORT-TARGET
    status:
     ports:
     - name: https
       port: 443
       protocol: TCP
       targetPort: 443
     **ips: CLUSTER_SET_IP**
    

MCS creates an EndpointSlice object as part of importing a Service into a cluster. By investigating this object you can monitor the progress of a Service import.

**Note:** Starting from GKE version 1.33, the Endpoints API is deprecated. Users should use the EndpointSlice API for endpoint discovery and monitoring.

To find the name of the EndpointSlice object, look up the value of the `net.gke.io/derived-service` annotation on a ServiceImport object corresponding to your imported Service. For example:
    
    
    kind: ServiceImport
    apiVersion: net.gke.io/v1
    annotations: **net.gke.io/derived-service: DERIVED_SERVICE_NAME**
    metadata:
     namespace: EXPORTED-SERVICE-NAMESPACE
     name: SERVICE-EXPORT-TARGET
    

Next, look up the EndpointSlice object to check if MCS has already propagated the endpoints to the importing cluster. The EndpointSlice object is created in the same namespace as the ServiceImport object, under the name stored in the `net.gke.io/derived-service` annotation. For example:
    
    
    kubectl get endpointslice -l kubernetes.io/service-name=DERIVED_SERVICE_NAME -n NAMESPACE
    

Replace the following:

  * `DERIVED_SERVICE_NAME`: the value of the `net.gke.io/derived-service` annotation on the ServiceImport object.
  * `NAMESPACE`: the namespace of the ServiceExport object.



You can find out more on the healthiness status of the endpoints using the Cloud Service Mesh dashboard in Google Cloud console.

For headless Services, the domain resolves to the list of IP addresses of the endpoints in the exporting clusters. Each backend Pod with a hostname is also independently addressable with a domain name of the following form:
    
    
     HOSTNAME.MEMBERSHIP_NAME.LOCATION.SERVICE_EXPORT_NAME.NAMESPACE.svc.clusterset.local
    

The output includes the following values:

  * `SERVICE_EXPORT_NAME` and `NAMESPACE`: the values you define in your `ServiceExport` object.
  * `MEMBERSHIP_NAME`: the [unique identifier in the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership) for the cluster that the Pod is in.
  * `LOCATION`: the location of the membership. Memberships are either `global`, or their location is one of the regions or zones that the Pod is in, such as `us-central1`.
  * `HOSTNAME`: the hostname of the Pod.



You can also address a backend Pod with a hostname exported from a cluster registered with a global Membership, using a domain name of the following format:
    
    
    HOSTNAME.MEMBERSHIP_NAME.SERVICE_EXPORT_NAME.NAMESPACE.svc.clusterset.local
    

## Disabling MCS

To disable MCS, complete the following steps:

  1. For each cluster in your fleet, delete each ServiceExport object that you created:
         
         kubectl delete serviceexport SERVICE_EXPORT_NAME \
             -n NAMESPACE
         

Replace the following:

     * `SERVICE_EXPORT_NAME`: the name of your ServiceExport object.
     * `NAMESPACE`: the namespace of the `ServiceExport` object.

Allow up to one hour for all `ServiceExports` to be fully deleted.

  2. [Unregister your clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) from the fleet if they don't need to be registered for another purpose.

  3. Disable the `multiclusterservicediscovery` feature:
         
         gcloud container fleet multi-cluster-services disable \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID from the project where you registered clusters.

### Verify successful deletion

When you disable the feature, a success message confirms the deletion.

If you see the following message, the feature is disabled:
         
         Waiting for Feature Multi-cluster Services to be deleted...done.
         

### Troubleshoot deletion errors

If you don't delete all `ServiceExport` resources before you disable MCS, or if `ServiceExports` or managed resources haven't finished deleting, you might see an error message.

The following message indicates that associated resources still exist:
         
         Feature has associated resources that should be cleaned up before
         deletion. Check the Feature state details for more information. This check
         can be overridden by setting force=true.
         

To resolve this error, inspect the feature state:
         
         gcloud container fleet multi-cluster-services describe \
             --project PROJECT_ID
         

In the output, inspect the `description` field. There are two possible cases:

     1. `ServiceExports` are not removed.

The message states that `ServiceExport` resources exist in the fleet:
            
            There are N ServiceExport in the Fleet.
            

Ensure that you delete all `ServiceExport` resources. Until all `ServiceExports` are completely deleted, disabling MCS will continue to fail.

Wait one hour and run the command again:
            
            gcloud container fleet multi-cluster-services disable \
            --project PROJECT_ID
            

     2. Managed resources are not removed.

The message states that resources are being removed:
            
            There are no ServiceExports in the Fleet. Managed resources are in the
            process of being removed. See
            https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#troubleshoot
            for more information.
            

The MCS backend must finalize the cleanup process. Occasionally, this process needs to restart, which adds a delay of up to three hours. Until all managed resources are completely deleted, disabling MCS will continue to fail.

Wait three hours and run the command again:
            
            gcloud container fleet multi-cluster-services disable \
            --project PROJECT_ID
            

#### Force disable the feature

You can force disable the `multiclusterservicediscovery` feature.

**Caution:** Force disabling the feature can leave managed resources in your project that continue to incur charges. We do not recommend this action.

To force disable the feature, run the following command:
    
    gcloud container fleet multi-cluster-services disable --force \
        --project PROJECT_ID
    

  4. Disable the API for MCS:
         
         gcloud services disable multiclusterservicediscovery.googleapis.com \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID from the project where you registered clusters.




## Limitations

### Number of clusters, Pods, and Service ports

The following limits are not enforced, and in some cases you can exceed these limits depending on the load in your clusters or project, and the rate of endpoint churn. You might experience performance issues when these limits are exceeded.

In Kubernetes, a Service is uniquely identified by its name and the namespace it belongs to. This name and the namespace pair is called a namespaced name.

  * **Exporting clusters** : A single Service, identified by a namespaced name, can be safely exported from up to **5 clusters** simultaneously. Beyond that limit, it's possible that only a subset of endpoints can be imported to consuming clusters. You can export different Services from different subsets of clusters.

  * **The number of Pods behind a single Service** : It's safe if you keep below **250 Pods** behind a single Service. With relatively static workloads and a small number of multi-cluster Services, it might be possible to significantly exceed this number into thousands of endpoints per Service. As with single cluster Services, all endpoints are watched by `kube-proxy` on every node. When going beyond this limit, especially when exporting from multiple clusters simultaneously, larger nodes might be required.

**Caution:** The limits for multi-cluster Services are not the same as the [limits for single cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters).
  * **The number of multi-cluster Services simultaneously exported** : We recommend that you simultaneously export no more than **250 unique Service ports**.

A unique Service port is identified by a namespaced name and a port number, that is a (name, namespace, port number) tuple. This means:

    * Services with the same namespaced name and port, exported from multiple clusters count as a single unique Service port.

    * Two Services with the same name and port, but different namespaces, for example (name, ns1, port-80) and (name, ns2, port-80) are two different Service ports, counting against two of the 250 unique Service port limit.

    * An exported Service exposing two ports 80 and 443 counts against two of the 250 unique Service port limit, regardless of the number of clusters in the fleet simultaneously exporting this Service.

Each multi-cluster Service counts toward your [Backend Services quota](https://console.cloud.google.com/iam-admin/quotas), and each zone of each exporting cluster creates a [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs). Increasing these quotas doesn't change the stated limit for the total count of unique Service ports.




### Service types

MCS only supports ClusterSetIP and Headless Services. NodePort and LoadBalancer Services are not supported and might lead to an unexpected behaviour.

### Using IPmasq Agent with MCS

MCS operates as expected when you use a default or other non masqueraded Pod IP range.

If you use a custom Pod IP range or a custom IPmasq agent ConfigMap, MCS traffic can be masqueraded. This prevents MCS from working because the firewall rules only allow traffic from Pod IPs.

To avoid this issue, you should either use the default Pod IP range or specify all Pod IP ranges in the `nonMasqueradeCIDRs` field of the [IPmasq agent ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#checking_the_ip-masq-agent_configmap). If you use Autopilot or you must use a non-default Pod IP range and cannot specify all Pod IP ranges in the ConfigMap, you should [use Egress NAT Policy to configure IP masquerade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).

### Reusing port numbers within an MCS Service

You can't reuse the same port number within one MCS Service even if the protocols are different.

This applies both within one Kubernetes Service and across all Kubernetes Services for one MCS Service.

### MCS with clusters in multiple projects

You cannot export a service if that service is already being exported by other clusters in a different project in the fleet with the same name and namespace. You can access the service in other clusters in the fleet in other projects, but those clusters cannot export the same service in the same namespace.

## Troubleshooting

The following sections provide you with troubleshooting tips for MCS.

### Viewing MCS Feature status

Viewing the status of the Feature resource can help you confirm if MCS was configured successfully. You can view the status with the following command:
    
    
    gcloud container fleet multi-cluster-services describe
    

The output is similar to the following:
    
    
    createTime: '2021-08-10T13:05:23.512044937Z'
    membershipStates:
     projects/PROJECT_ID/locations/global/memberships/MCS_NAME:
       state:
         code: OK
         description: Firewall successfully updated
         updateTime: '2021-08-10T13:14:45.173444870Z'
    name: projects/PROJECT_NAME/locations/global/features/multiclusterservicediscovery
    resourceState:
     state: ACTIVE
    spec: {}
    

It consists, among other information, of the overall Feature state under `resourceState` and of individual memberships' status, under `membershipStates`.

If you enabled the MCS feature according to the Enabling MCS on your GKE cluster instruction but the value of the `resourceState.state` is not `ACTIVE`, contact the support.

Status of each membership consists of its path and the `state` field. The latter contains `code` and `description` which are helpful for troubleshooting.

#### Codes in the membership states

A code, represented by the `state.code` field, indicates the member's general state in relation to MCS. There are four possible values:

  * **`OK`** : The membership was successfully added to MCS and is ready to use.

  * **`WARNING`** : MCS is in the process of reconciling membership setup. The description field can provide more information about what caused this code.

  * **`FAILED`** : This membership was not added to MCS. Other memberships in the fleet with an `OK` code are not affected by this `FAILED` membership. The description field can provide more information about what caused this code.

  * **`ERROR`** : This membership is missing resources. Other memberships in the fleet with an `OK` code are not affected by this `ERROR` membership. The description field can provide more information about what caused this code.




#### Descriptions in the membership states

To see information about the membership's state in MCS, check the `state.description` field. This field provides information about the project and hub configuration and the fleet and memberships health status. To view information about individual Services and their configuration, consult the `Status.Conditions` field in the `ServiceExport` object, see the Examining `ServiceExport` section.

The `state.description` field contains the following information:

  * **`Firewall successfully created`** : This message indicates that the member's firewall rule was successfully created and or updated. The membership's code is `OK`.

  * **`Firewall creation pending`** : This message indicates that the member's firewall rule is pending creation or update. The membership's code is `WARNING`. This membership can experience issues updating and connecting to new multi-cluster Services and memberships added while the firewall rule is pending.

  * **`GKE Cluster missing`** : This message indicates that the registered GKE cluster is unavailable and or deleted. The membership's code is `ERROR`. This membership needs to be manually [unregistered from the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) after a GKE cluster is deleted.

  * **`Project that member lives in is missing required permissions and/or has not enabled all required APIs - additional setup steps are required`** : This message indicates there are internal StatusForbidden (403) errors, and the membership's code is `FAILED`. This error occurs in the following scenarios:

    * **You have not enabled the necessary APIs in the member's project.**

If the member cluster lives in a separate project than the fleet, see [cross-project setup](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks) to ensure you have completed all necessary steps. If you have completed all steps, ensure that the following APIs are enabled in the registration project with the following commands:
          
          gcloud services enable multiclusterservicediscovery.googleapis.com --project PROJECT_ID
          gcloud services enable dns.googleapis.com --project PROJECT_ID
          gcloud services enable trafficdirector.googleapis.com --project PROJECT_ID
          gcloud services enable cloudresourcemanager.googleapis.com --project PROJECT_ID
          

Replace `PROJECT_ID` with the project ID from the project where you registered clusters.

    * **The`mcsd` or `gkehub` service account requires more permissions in the member's project.**

The `mcsd` and `gkehub` service accounts should automatically have been created in the fleet host project with all the required permissions. To verify the service accounts exist, run the following commands:
          
          gcloud projects get-iam-policy PROJECT_ID | grep gcp-sa-mcsd
          gcloud projects get-iam-policy PROJECT_ID | grep gcp-sa-gkehub
          

Replace `PROJECT_ID` with the project ID from the fleet host project.

These commands should show you the full name of the `mcsd` and `gkehub` service accounts.

  * **`Multiple VPCs detected in the hub - VPC must be peered with other VPCs for successful connectivity`** : This message occurs when clusters hosted in different VPCs are registered to the same fleet. Membership status is `OK`. A cluster's VPC network is defined by its [NetworkConfig's network](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#networkconfig). Multi-cluster Services require a flat network, and these VPCs must be actively peered for multi-cluster Services to properly connect to each other. To learn more, see [Peer two networks](https://docs.cloud.google.com/vpc/docs/peer-two-networks).

  * **`Member does not exist in the same project as hub - additional setup steps are required, errors may occur if not completed.`** : This message reminds you that cross-project clusters require additional setup steps. Membership status is `OK`. Cross-project memberships are defined as a member cluster that is not in the same project as the fleet. For more information, see [cross-project setup](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks).

  * **`Non-GKE clusters are currently not supported`** : This message reminds you that MCS only supports GKE clusters. Non-GKE clusters cannot be added to MCS. Membership status is `FAILED`.




### Examining `ServiceExport`

To view the status of an individual Service and potential errors, check the `Status.Conditions` field in the `ServiceExport` resource for that Service:
    
    
    kubectl describe serviceexports PROJECT_ID -n NAMESPACE
    

The output is similar to the following:
    
    
    Name:         SERVICE_NAME
    Namespace:    NAMESPACE
    Labels:       <none>
    Annotations:  <none>
    API Version:  net.gke.io/v1
    Kind:         ServiceExport
    Metadata:
      Creation Timestamp:  2024-09-06T15:57:40Z
      Finalizers:
        serviceexport.net.gke.io
      Generation:        2
      Resource Version:  856599
      UID:               8ac44d88-4c08-4b3d-8524-976efc455e4e
    Status:
      Conditions:
        Last Transition Time:  2024-09-06T16:01:53Z
        Status:                True
        Type:                  Initialized
        Last Transition Time:  2024-09-06T16:02:48Z
        Status:                True
        Type:                  Exported
    Events:                    <none>
    

When the MCS controller notices a `ServiceExport` resource, the controller adds the following conditions to the `Status.Conditions` field:

  * **`Initialized`** : True if the MCS Controller has picked up and attempted to reconcile the Service represented by the `ServiceExport`.

  * **`Exported`** : True if the Service represented by the `ServiceExport`has been successfully validated.




Each condition contains mandatory `Type`, `Status`, and `LastTransitionTime` fields. As the MCS controller reconciles and validates the Service, the `Status` field for the corresponding condition changes from `False` to `True`.

#### Errors

If an error occurs with the validation, the controller sets the `Status` field of the `Exported` condition to `False` and adds a `Reason` field and a `Message` field with more information about the error. The `Reason` field can have one of the following values:

  * **`NoMatchingService`** : No Service matching name and namespace of the `ServiceExport` has been found in the given cluster.   
Check whether the Kubernetes Service you intend to export exists in the same cluster. Check whether the name and namespace on both resources (`Service` and `ServiceExport`) match exactly one another.

  * **`Conflict`** : There already exists an exported Service with the same name and namespace that either doesn't match the one being exported by this `ServiceExport` or, it is exported from a different network or project which is not allowed, see Limitations.   
Inspect the `Message` field for the details and consult the Limitations section if necessary. Ensure the name and namespace of the `Service` and `ServiceExport` match one another and all resources are created in the same network and/or project.

  * **`ReadinessProbeError`** : There is a [`readinessProbe`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) configured on a container in a Pod backing the Service. `Kubernetes ReadinessProbes` are translated to [`Google cloud HealthChecks`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) and must conform to the same restrictions.

**Note:** MCS uses a port defined in a container's `readinessProbe` setting as the authoritative port for health checks propagated to the Traffic Director control plane. MCS selects the first container in the oldest aggregated Pod that exposes the Service's targetPort, even if that container's `readinessProbe` is served on a different port. If your Service `targetPort` differs from your `readinessProbe` port, ensure that the `readinessProbe` port is accessible and correctly configured, as this port determines the health status of the Service in Cloud Service Mesh.

Here's how readiness check fields align with health check parameters:

    * `PeriodSeconds` corresponds to `CheckInterval`
    * `TimeoutSeconds` corresponds to `Timeout`
    * `SuccessThreshold` corresponds to `HealthyThreshold`
    * `FailureThreshold` corresponds to `UnhealthyThreshold`

To align `ReadinessProbes` with `HealthCheck` constraints, MCS implements the following:

    * `PeriodSeconds` and `TimeoutSeconds` are capped at 300 seconds; values exceeding this limit trigger an error.
    * `SuccessThreshold` and `FailureThreshold` are capped at 10 seconds; values exceeding this limit trigger an error.
    * An error is reported, and resource creation (potentially all resources) fails if `TimeoutSeconds` is greater than `PeriodSeconds`.

The rationale for such restrictions is to prevent scalability issues, subsequent probes from overlapping, healthcheck/readiness slowness etc. Adjust the parameters of the `readinessProbe` as per the above validations. **It is important to fix such errors for every Service of the fleet** , see Known issues for further explanation.

  * **`ServiceError`** : An error encountered while fetching the corresponding Service.   
This error is usually related to a Google Cloud infrastructure problem. Please contact Google Cloud support if the problem persists.

  * **`PodsError`** : An error encountered while fetching the backend Pod or Pods   
This error is usually related to a Google Cloud infrastructure problem. Please contact Google Cloud support if the problem persists.

  * **`EndpointsError`** : An error encountered while aggregating Endpoints for a Headless Service   
This error is usually related to a Google Cloud infrastructure problem. Please contact Google Cloud support if the problem persists.




The `Message` field provides additional context for the error.

### Common permission issues

  * **Necessary APIs not enabled in the project.**

Make sure you have enabled the required APIs as instructed in the Before you begin section.

For a cross-project fleet, follow the appropriate **Enable required APIs** section in [Setting up multi-cluster Services with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks).

  * **`mcsd` or `gkehub` service account doesn't have sufficient permissions**

For a single-project setup all the necessary permissions are automatically granted to service accounts that are auto-created by GKE Hub and MCS.

For a cross-project fleet, you have to create additional IAM bindings. Follow the appropriate **Create IAM bindings** section in [Setting up multi-cluster Services with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks).




## Known issues

### MCS Services with multiple ports

There is a known issue with multi-cluster Services with multiple (TCP/UDP) ports on GKE Dataplane V2 where some endpoints are not programmed in the dataplane. This issue impacts GKE versions earlier than 1.26.3-gke.400.

As a workaround, when using GKE Dataplane V2, use multiple MCS with a single port instead of one MCS with multiple ports.

### Port number reused within one MCS Service

You can't reuse the same port number within an MCS Service even if the protocols are different.

This applies both within one Kubernetes Service and across all Kubernetes Services for one MCS Service.

### Health check uses default port instead of `containerPort`

When you deploy a Service with a `targetPort` field referencing a named port in a Deployment, MCS configures the default port for the health check instead of the specified `containerPort`.

To avoid this issue, use numerical values in the Service field `ports.targetPort` and the Deployment field `readinessProbe.httpGet.port` instead of named values.

**NOTE:** At the present time, MCS derives the health check port for exported Services from the Pod's `readinessProbe` only.

### Invalid readiness probe for a single Service breaks other Services

There is a known potential `readinessProbe` configuration error described in Examining `ServiceExports`. With the current implementation of MCS, this error, if introduced for a single exported Service, can prevent some or all other Services in the fleet from getting synchronized.

It is important to keep configurations for every Service healthy. If an MCS Service is not getting updated, make sure that **none** of the ServiceExports in any of the clusters in any of the namespaces reports **ReadinessProbeError** as the reason for Status Condition `Exported` being False. See Examining `ServiceExports` to learn how to check the conditions.

## What's next

  * Learn more about [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service).
  * Learn how to [expose apps with Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).
  * Implement a basic [multi-cluster Services example](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/services/multi-cluster/mcs-basic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
