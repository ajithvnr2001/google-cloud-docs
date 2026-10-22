---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-recommended-features/
title: Migrate an admin cluster to recommended features \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:03.586030+00:00
---

# Migrate an admin cluster to recommended features  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-recommended-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate an admin cluster to recommended features Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This page shows you how to migrate a version 1.30 or higher admin cluster to these recommended features:

  * The load balancer configuration:

    * The integrated F5 BIG-IP load balancer configuration to `ManualLB`.

or

    * The bundled Seesaw load balancer to MetalLB.

  * Migrate to a high availability (HA) admin cluster from a non-HA admin cluster. Availability is significantly improved with an HA admin cluster while using the same number of VMs. A non-HA admin cluster has one control-plane node and two add-on nodes. An HA admin cluster's three nodes are all control-plane nodes with no add-on nodes.




This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more information about migration planning, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

## Best practices

If you have multiple environments such as test, development, and production, we recommend that you first migrate the least critical environment, such as test. After you verify that the migration was successful, repeat this process for each environment, migrating your production environment last. This lets you validate each migration's success and ensure that your workloads are running properly, before moving to the next more critical environment.

## Requirements

  * The admin cluster must be at version 1.30 or higher.
  * All the user clusters managed by the admin cluster must already be migrated to recommended features, as described in the [Migrate a user cluster to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features).



## Plan for downtime during migration

For the migration, plan for some limited control-plane downtime. The Kubernetes API access is unavailable for non-HA admin clusters for about 20 minutes, but the Kubernetes control plane remains available for HA admin clusters with F5. During migrations, the Kubernetes data plane continues to work in a stable state.

**Note:** User workloads should only run in user clusters, which are not affected when migrating the admin clusters.From | To | Kubernetes API Access | User workloads  
---|---|---|---  
HA admin clusters with F5 BIG-IP | HA admin clusters with `ManualLB` | Not affected | Not affected  
non-HA admin clusters with `MetalLB` or `ManualLB` | HA admin clusters with the same kind of load balancer | Affected | Not affected  
non-HA admin clusters with F5 BIG-IP | HA admin clusters with `ManualLB` | Affected | Not affected  
non-HA admin clusters with Seesaw | HA admin clusters with MetalLB | Affected | Not affected  
  
  * **Affected** : There is a noticeable service disruption during the migration.
  * **Not affected** : There is either no service disruption or it is almost unnoticeable.



## Prepare for the migration

If your admin cluster is non-HA, prepare to migrate to an HA admin cluster by following the steps in this section. If your admin cluster is already HA, skip to the next section, Prepare for the load balancer migration.

### Allocate additional IP addresses

When migrating the admin cluster from non-HA to HA, allocate four additional IP addresses. Ensure these IP addresses are in the same VLAN as the existing admin cluster nodes and aren't already used by any existing nodes:

  * Allocate one IP address for the new control plane VIP, for the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field in the admin cluster configuration file.
  * Allocate a new IP addresses for each of the three control-plane nodes, for the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) section in the admin cluster configuration file.



## Update firewall rules

When migrating the admin cluster from non-HA to HA, update the firewall rules on your admin cluster. This ensures that the newly allocated IP addresses for the control-plane nodes can reach all required APIs and other destinations, as described in [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters).

## Prepare for the load balancer migration

If your admin cluster is using the integrated F5 BIG-IP configuration or the bundled Seesaw load balancer, follow the steps in this section to make the to make the necessary changes to the admin cluster configuration file. Otherwise, skip to the next section, Prepare to migrate from non-HA to HA.

### F5 BIG-IP

If your admin cluster is using the integrated F5 BIG-IP configuration, make the following changes to the admin cluster configuration file:

  1. Set the [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-kind-field) field to `"ManualLB"`.
  2. Set or keep the value of the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field. If your admin cluster is already HA, keep the same value. If you are migrating from a non-HA admin cluster to an HA admin cluster, change the value of the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field to the IP address that you allocated.
  3. Delete the entire [`loadBalancer.f5BigIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-f5bigip-section) section.



The following example admin cluster configuration file shows these changes:
    
    
    loadBalancer:
    vips:
      controlPlaneVIP: 192.0.2.6
    kind: ~~"F5BigIP"~~ "ManualLB"
    ~~f5BigIP:
        address: "203.0.113.20"
      credentials:
        fileRef:
          path: ""my-config-folder/user-creds.yaml"
          entry: "f5-creds"
      partition: "my-f5-user-partition"~~
      

### Seesaw

If your admin cluster uses the Seesaw load balancer, make the following changes to the admin cluster configuration file:

  1. Set the [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#loadbalancer-kind-field) field to "MetalLB".
  2. Keep the [`network.hostConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-hostconfig-section) section.
  3. Set or keep the value of the `loadBalancer.vips.controlPlaneVIP`][5](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field. If your admin cluster is already HA, you can keep the same value. If migrating from a non-HA admin cluster to an HA admin cluster, change the value of the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field to the IP address that you allocated.
  4. Remove the [`loadBalancer.seesaw`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#loadbalancer-seesaw-section) section.



The following example admin cluster configuration file shows these changes:
    
    
    network:
    hostConfig:
      dnsServers:
      - "203.0.113.1"
      - "203.0.113.2"
      ntpServers:
      - "203.0.113.3"
    loadBalancer:
    vips:
      controlPlaneVIP: 192.0.2.6
    kind: "MetalLB" ~~"Seesaw"~~
    ~~seesaw:
      ipBlockFilePath: "user-cluster-1-ipblock.yaml"
      vrid: 1
      masterIP: ""
      cpus: 4
      memoryMB: 3072~~
    

## Prepare to migrate from non-HA to HA

If your admin cluster is non-HA, prepare to migrate to HA by following the steps in this section.

If your admin cluster is already HA, skip to the next section, Migrate the admin cluster.

If your admin cluster version is 1.29.0-1.29.600 or 1.30.0-1.30.100, and if [always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) was enabled in the admin cluster at version 1.14 or earlier, you must [rotate the encryption key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#key_rotation) before starting the migration. Otherwise, the new HA admin cluster will be unable to decrypt secrets.

To check whether the cluster could be using an old encryption key:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secret -n kube-system admin-master-component-options -o jsonpath='{.data.data}' | base64 -d | grep -oP '"GeneratedKeys":\[.*?\]'
    

If the output shows an empty key, such as in the following example, you must rotate the encryption key using the steps in this [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#migrating-an-admin-cluster-from-non-ha-to-ha-fails-if-secrets-encryption-is-enabled).
    
    
    "GeneratedKeys":[{"KeyVersion":"1","Key":""}]
    

**Warning:** If you started the migration without rotating the encryption key, contact Google Support.

### Update the admin cluster configuration file

Make these changes to the admin cluster configuration file:

  1. Fill in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section) with the three IP addresses that you allocated for the control-plane nodes.
  2. Ensure that you have filled the [`network.hostConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-hostconfig-section) section. This section holds information about NTP servers, DNS servers, and DNS search domains used by the VMs that are your cluster nodes.
  3. Ensure that you have replaced the value of [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) with the IP address that you allocated.
  4. Set [`adminMaster.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-replicas-field) to 3.
  5. Remove the [`vCenter.dataDisk`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-datadisk-field) field. For an HA admin cluster, the paths for the three data disks used by control-plane nodes are automatically generated under the root directory `anthos` in the datastore.
  6. If `loadBalancer.kind` is set to `"ManualLB"`, set `loadBalancer.manualLB.controlPlaneNodePort` to 0.



The following example admin cluster configuration file shows these changes:
    
    
    vCenter:
      address: "my-vcenter-server.my-domain.example"
      datacenter: "my-data-center"
      ~~dataDisk: "xxxx.vmdk"~~
    ...
    network:
      hostConfig:
        dnsServers:
        - 203.0.113.1
        - 203.0.113.2
        ntpServers:
        - 203.0.113.3
      ...
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
        gateway: "198.51.100.1"
        ips:
        - ip: "192.0.2.1"
          hostname: "admin-cp-hostname-1"
        - ip: "192.0.2.2"
          hostname: "admin-cp-hostname-2"
        - ip: "192.0.2.3"
          hostname: "admin-cp-hostname-3"
    ...
    
    ...
    loadBalancer:
      vips:
        controlPlaneVIP: ~~192.0.2.6~~ 192.0.2.50
      kind: ManualLB
      manualLB:
        ~~controlPlaneNodePort: 30003~~ 0
    
    ...
    adminMaster:
      replicas: 3
      cpus: 4
      memoryMB: 8192
    ...
    

### Adjust mappings in your load balancer if needed

If your admin cluster has been using manual load balancing, complete the step in this section.

If you are migrating from integrated F5 BIG-IP to manual load balancing, or if you are migrating to MetalLB, skip to the next section, Migrate the admin cluster.

For each of the three new control-plane node IP addresses that you specified in the `network.controlPlaneIPBlock` section, configure this mapping in your external load balancer (such as F5 BIG-IP or Citrix):
    
    
    (old controlPlaneVIP:443) -> (NEW_NODE_IP_ADDRESS:old controlPlaneNodePort)
    

This ensures that the old control-plane VIP continues working during the migration.

## Migrate the admin cluster

Carefully review all the changes that you made to the admin cluster configuration file. All the settings are immutable except when updating the cluster for the migration.

Update the cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config ADMIN_CLUSTER_CONFIG
    

`Replace the following`:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
  * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.



The command displays the progress of the migration.

When prompted, enter `Y` to continue.

During the migration from non-HA to HA, the older control-plane VIP continues to function and can be used to access the new HA admin cluster. When the migration completes, the admin cluster kubeconfig file is automatically updated to use the new control-plane VIP.

## After the migration

After the update completes, verify that the admin cluster is running:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

### Load balancer migration

If you migrated the load balancer, verify that the load balancer components are running successfully.

### MetalLB

If you migrated to MetalLB, verify that the MetalLB components are running successfully using the following command:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods \
        --namespace kube-system --selector app=metallb
    

The output shows Pods for the MetalLB controller and speaker. For example:
    
    
    metallb-controller-744884bf7b-rznr9 1/1 Running
    metallb-speaker-6n8ws 1/1 Running
    metallb-speaker-nb52z 1/1 Running
    metallb-speaker-rq4pp 1/1 Running
    

After a successful migration, delete the powered-off Seesaw VMs for the admin cluster. You can find the Seesaw VM names in the `vmnames` section of the `seesaw-for-gke-admin.yaml` file in your configuration directory.

### `ManualLB`

After you update your clusters to use manual load balancing, traffic to your clusters isn't interrupted. This is because the existing F5 resources still exist, as you can see by running the following command:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
    

The expected output is similar to the following:
    
    
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
