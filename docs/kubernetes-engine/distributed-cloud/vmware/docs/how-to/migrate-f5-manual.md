---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual/
title: Migrate configuration settings for your F5 BIG-IP load balancer \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:44.251846+00:00
---

# Migrate configuration settings for your F5 BIG-IP load balancer  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate configuration settings for your F5 BIG-IP load balancer Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

1.29: Preview  
1.28: Not available  


This document shows how to migrate the configuration settings for your F5 BIG-IP load balancer integration to manual load balancing mode for clusters at version 1.29. If your clusters are at version 1.30 or higher, we recommend that you follow the instructions in [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

Using F5 BIG-IP in manual load balancing mode gives you the flexibility to upgrade your F5 agents independently without affecting the functionality of your F5 load balancer or your Kubernetes services. If you migrate to the manual configuration, you can obtain updates directly from F5 to ensure optimal performance and security.

**Note:** If you choose to change the settings in your cluster configuration files to use [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance) for F5 BIG-IP, this doesn't mean your load balancing is manual. With either bundled or manual F5 load balancing, load balancer agents help you manage the load balancing configuration automatically.

This migration is required in the following circumstances:

  * You want to enable new features like Controlplane V2 and you also need access to F5.

  * You need capabilities provided by a version of BIG-IP CIS Container Ingress Services (CIS) Controller higher than v1.14.




If the preceding circumstances don't apply to you, you can continue to use the bundled configuration for F5 BIG-IP load balancing.

Either way, we continue to officially support F5 as a load balancer solution. 

## Support for the F5 BIG-IP load balancer

We support the use of F5 BIG-IP with load balancer agents, which consist of the following two controllers:

  * F5 Controller (pod prefix: `load-balancer-f5`): reconciles `LoadBalancer` type Kubernetes Services into [F5 Common Controller Core Library (CCCL) ConfigMap](https://community.f5.com/kb/technicalarticles/introduction-to-f5-common-controller-core-library-cccl/281882) format.

  * F5 BIG-IP CIS Controller v1.14 (pod prefix: `k8s-bigip-ctlr-deployment`): translates ConfigMaps into F5 load balancer configurations.




These agents streamline the configuration of F5 load balancers within your Kubernetes cluster. By creating a Service of type `LoadBalancer`, the controllers automatically configure the F5 load balancer to direct traffic to your cluster nodes.

However, the bundled solution comes with limitations:

  * The expressiveness of the Service API is limited. You can't configure the BIG-IP controller as you like, or use advanced F5 features. F5 already provides [better support](https://clouddocs.f5.com/containers/latest/userguide/loadbalancer/#overview-of-service-type-loadbalancer) of Service API natively.

  * The implementation uses the legacy CCCL ConfigMap API and 1.x CIS. However, F5 now provides the newer [AS3](https://clouddocs.f5.com/containers/latest/userguide/config-map.html) ConfigMap API and [2.x CIS](https://clouddocs.f5.com/containers/latest/reference/release-notes.html#release-notes-2-17-1).




The CIS controller in the Google Distributed Cloud bundle has remained at v1.14 due to compatibility issues with the F5 upgrade guidance for CIS v2.x. Therefore, to give you the flexibility to address security vulnerabilities and access the latest features, we are transitioning the F5 agents from being bundled components to being independently installed. If you migrate, you can continue using the existing agents without disruption and your previously created services remain operational.

For newly created [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance) clusters with F5 as the load balancing solution, you need to install the controllers yourself. Similarly, if your cluster has been migrated from bundled F5 and you'd like to use a newer version of the CIS Controller, you need to install the controllers yourself.

## Requirements

Following are the requirements for the migration:

  * The admin cluster and all user clusters must be version 1.29 or higher.

  * You must be using static IP addresses for your admin and user cluster nodes. The IP addressing type is set in the [`network.ipMode.type`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field) field, and it is immutable. If this field is set to DHCP, you can't migrate the clusters.




## Update the user cluster configuration file

Make the following changes to the user cluster configuration file:

  1. Change [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-kind-field) to `"ManualLB"`.

  2. Keep the same values for the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) and the [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field) fields.

  3. Configure the `nodePort` used for HTTP traffic sent to the ingress VIP.

     1. Get the current HTTP `nodePort` value:
            
            kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
                get svc istio-ingress -n gke-system -oyaml | grep http2 -A 1

Replace `USER_CLUSTER_KUBECONFIG` with the path of the user cluster kubeconfig file.

     2. Add the value from the previous command to the `loadBalancer.manualLB.ingressHTTPNodePort` field, for example:
            
            loadBalancer:
              manualLB:
                ingressHTTPNodePort: 30243

  4. Configure the `nodePort` used for HTTPS traffic sent to the ingress VIP:

     1. Get the current HTTPS `nodePort` value:
            
            kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
                get svc istio-ingress -n gke-system -oyaml | grep https -A 1

     2. Add the value from the previous command to the `loadBalancer.manualLB.ingressHTTPSNodePort` field, for example:
            
            loadBalancer:
              manualLB:
                ingressHTTPSNodePort: 30879

  5. Configure the `nodePort` for the Kubernetes API server:

     1. Get the current `nodePort` value for the Kubernetes API server:
            
            kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                get svc kube-apiserver -n USER_CLUSTER_NAME -oyaml | grep kube-apiserver-port -A 1

Replace the following:

        * `ADMIN_CLUSTER_KUBECONFIG` with the path of the **admin** cluster kubeconfig file.

        * `USER_CLUSTER_NAME`: name of the user cluster.

     2. Add the value from the previous command to the `loadBalancer.manualLB.controlPlaneNodePort` field, for example:
            
            loadBalancer:
              manualLB:
                controlPlaneNodePort: 30968

  6. Configure the `nodePort` for the Konnectivity server:

     1. Get the current `nodePort` value for the Konnectivity server:
            
            kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                get svc kube-apiserver -n USER_CLUSTER_NAME -oyaml | grep konnectivity-server-port -A 1

     2. Add the value from the previous command to the `loadBalancer.manualLB.konnectivityServerNodePort` field, for example:
            
            loadBalancer:
              manualLB:
                konnectivityServerNodePort: 30563

  7. Delete the entire [`loadBalancer.f5BigIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-f5bigip-section) section.




## Update the user cluster

Run the following command to migrate the cluster:
    
    
    gkectl update cluster \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.




## Update the admin cluster configuration file

Make the following changes to the admin cluster configuration file:

  1. Change [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-kind-field) to `"ManualLB"`.

  2. Keep the same value for the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field.

  3. Check the value of the [`adminMaster.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-replicas-field) field. If the value is 3, the admin cluster is highly available (HA). If the value is 1, the admin cluster is non-HA.

  4. Do the following steps only for non-HA admin clusters:

     1. Get the value of the `nodePort` for the Kubernetes API server:
            
            kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                get svc kube-apiserver -n kube-system -oyaml | grep nodePort

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of the admin cluster kubeconfig file.

     2. Add the value from the previous command to the `loadBalancer.manualLB.controlPlaneNodePort` field, for example:
            
            loadBalancer:
              manualLB:
                controlPlaneNodePort: 30968

  5. Run the following command to see if there's an add-ons `nodePort`:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             get deploy monitoring-operator -n kube-system -oyaml | grep admin-ingress-nodeport

If the previous command outputs a value, add it to the `loadBalancer.manualLB.addonsNodePort` field, for example:
         
         loadBalancer:
           manualLB:
             addonsNodePort: 31405

  6. Delete the entire [`loadBalancer.f5BigIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-f5bigip-section) section.




## Update the admin cluster

Run the following command to update the cluster:
    
    
    gkectl update admin \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config ADMIN_CLUSTER_CONFIG

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.




## Verify that legacy F5 resources still exist

After updating your clusters to use manual load balancing, traffic to your clusters isn't interrupted because the existing F5 resources still exist, as you can see by running the following command:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
      api-resources --verbs=list -o name   | xargs -n 1 kubectl --kubeconfig CLUSTER_KUBECONFIG get --show-kind --ignore-not-found --selector=onprem.cluster.gke.io/legacy-f5-resource=true -A

Replace `CLUSTER_KUBECONFIG` with either the path of the admin cluster or user cluster kubeconfig file.

The expected output is similar to the following:

**Admin cluster** :
    
    
    Warning: v1 ComponentStatus is deprecated in v1.19+
    NAMESPACE     NAME                        TYPE     DATA   AGE
    kube-system   secret/bigip-login-xt697x   Opaque   4      13h
    NAMESPACE     NAME                              SECRETS   AGE
    kube-system   serviceaccount/bigip-ctlr         0         13h
    kube-system   serviceaccount/load-balancer-f5   0         13h
    NAMESPACE     NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
    kube-system   deployment.apps/k8s-bigip-ctlr-deployment   1/1     1            1           13h
    kube-system   deployment.apps/load-balancer-f5            1/1     1            1           13h
    NAME                                                                                ROLE                                       AGE
    clusterrolebinding.rbac.authorization.k8s.io/bigip-ctlr-clusterrole-binding         ClusterRole/bigip-ctlr-clusterrole         13h
    clusterrolebinding.rbac.authorization.k8s.io/load-balancer-f5-clusterrole-binding   ClusterRole/load-balancer-f5-clusterrole   13h
    NAME                                                                 CREATED AT
    clusterrole.rbac.authorization.k8s.io/bigip-ctlr-clusterrole         2024-03-25T04:37:34Z
    clusterrole.rbac.authorization.k8s.io/load-balancer-f5-clusterrole   2024-03-25T04:37:34Z
    

**User cluster** :
    
    
    Warning: v1 ComponentStatus is deprecated in v1.19+
    NAMESPACE     NAME                        TYPE     DATA   AGE
    kube-system   secret/bigip-login-sspwrd   Opaque   4      14h
    NAMESPACE     NAME                              SECRETS   AGE
    kube-system   serviceaccount/bigip-ctlr         0         14h
    kube-system   serviceaccount/load-balancer-f5   0         14h
    NAMESPACE     NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
    kube-system   deployment.apps/k8s-bigip-ctlr-deployment   1/1     1            1           14h
    kube-system   deployment.apps/load-balancer-f5            1/1     1            1           14h
    NAME                                                                                ROLE                                       AGE
    clusterrolebinding.rbac.authorization.k8s.io/bigip-ctlr-clusterrole-binding         ClusterRole/bigip-ctlr-clusterrole         14h
    clusterrolebinding.rbac.authorization.k8s.io/load-balancer-f5-clusterrole-binding   ClusterRole/load-balancer-f5-clusterrole   14h
    NAME                                                                 CREATED AT
    clusterrole.rbac.authorization.k8s.io/bigip-ctlr-clusterrole         2024-03-25T05:16:40Z
    clusterrole.rbac.authorization.k8s.io/load-balancer-f5-clusterrole   2024-03-25T05:16:41Z
    

## Check your load balancer

After the migration, you shouldn't need to change any settings in your load balancer because you kept the same VIPs and `nodePort` values. The following tables describe the mappings from VIPs to node IP addresses:`nodePort`.

### HA admin cluster

#### Traffic to control plane nodes

Google Distributed Cloud automatically handles load balancing of the control plane traffic for HA admin clusters. Although you don't need to configure a mapping in the load balancer, you must specify an IP address in the `loadBalancer.vips.controlPlaneVIP` field.

#### Traffic to services in the add-on nodes

If your admin cluster had a value for `addonsNodePort`, you should see a mapping to the IP addresses and `nodePort` value for traffic to services in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



You should have this mapping for all nodes in the admin cluster, both the control plane nodes and the add-on nodes.

### Non-HA admin cluster

#### Control plane traffic

The following shows the mapping to the IP address and `nodePort` value for the control plane node:

  * (`controlPlaneVIP`:443) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)



You should have this mapping for all nodes in the admin cluster, both the control plane node and the add-on nodes.

#### Traffic to services in the add-on nodes

If your admin cluster had a value for `addonsNodePort`, you should have the following mapping to the IP addresses and `nodePort` values for services running in add-on nodes:

  * (`addonsVIP`:8443) -> (NODE_IP_ADDRESSES:`addonsNodePort`)



You should have this mapping for all nodes in the admin cluster, both the control plane node and the add-on nodes.

### User cluster

#### Control plane traffic

The following shows the mapping to the IP addresses and `nodePort` values for control plane traffic:

  * (`controlPlaneVIP`:`443`) -> (NODE_IP_ADDRESSES:`controlPlaneNodePort`)
  * (`controlPlaneVIP`:`8132`) -> (NODE_IP_ADDRESSES:`konnectivityServerNodePort`)



You should have this mapping for all nodes in the _admin_ cluster, both the admin cluster and the user cluster control plane nodes.

#### Data plane traffic

The following shows the mapping to the IP addresses and `nodePort` values for data plane traffic:

  * (`ingressVIP`:`80`) -> (NODE_IP_ADDRESSES:`ingressHTTPNodePort`)
  * (`ingressVIP`:`443`) -> (NODE_IP_ADDRESSES:`ingressHTTPSNodePort`)



**Note:** The healthcheck to `ingressVIP` will fail until you configure at least one ingress. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
