---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features/
title: Migrate a user cluster to recommended features \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:29.408899+00:00
---

# Migrate a user cluster to recommended features  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate a user cluster to recommended features Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This page shows you how to migrate version 1.30 or higher user clusters to the following recommended features:

  * Migrate to Dataplane V2 as the container network interface (CNI).
  * Migrate user clusters using kubeception to Controlplane V2.
  * Migrate the load balancer configuration:

    * From the integrated F5 BIG-IP load balancer configuration to `ManualLB`

or

    * From the bundled Seesaw load balancer to MetalLB.




This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. For information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

### Best practices

recommend that you first migrate the least critical environment, such as test. After you verify that the migration was successful, repeat this process for each environment, migrating your production environment last. This lets you validate each migration's success and ensure that your workloads are running properly, before moving to the next more critical environment.

We recommend that you [create a new user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) with Controlplane V2 enabled to learn about the architectural differences with kubeception clusters. The new cluster doesn't affect your workloads. However, in a worst-case scenario, if the migration fails, you have a cluster ready for your workloads.

For more information about migration planning, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

## Requirements

For this migration:

  * The user cluster must be at version 1.30 or higher.
  * All node pools must be the same version as the user cluster.
  * If the cluster is using the Seesaw load balancer, make sure you aren't relying on Seesaw for client IP preservation as described in the next section.



### Seesaw client IP preservation

**Warning:** Don't migrate to MetalLB if you are relying on Seesaw for client IP address preservation. Specifically, don't migrate to MetalLB if there are Services in the cluster with `spec.externalTrafficPolicy` set to `Local`.

To check the `externalTrafficPolicy`, run the following command:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get svc -A -o yaml | grep "externalTrafficPolicy: Local"
    

If you have this issue, contact Google Support.

## Estimate the time commitment and plan a maintenance window

When you update the cluster, by default, all node pools are updated in parallel. However, within each node pool, the nodes are updated sequentially. Therefore, the total update time depends on the number of nodes in the largest node pool. To calculate a rough estimate for each update:

  * If migrating from Seesaw to MetalLB, then estimate 15 minutes for the update to choose a node pool for the MetalLB load balancer. For this update, only the selected node pool is updated.
  * For any other update in the migration process, multiply 15 minutes by the number of nodes in the node pool.



To estimate the time commitment, count the number of times you need to update the cluster. The following high-level steps show when you need to run `gkectl update cluster` to update the cluster:

  1. If the user cluster uses [always-on secret encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#enable_always-on_secrets_encryption), disable the feature and run `gkectl update cluster`.
  2. If the user cluster has `enableDataplaneV2` unset or set to `false`, make the configuration changes, and then run `gkectl update cluster` to migrate to Dataplane V2.
  3. Prepare for load balancer and control plane migration:

     1. If the admin cluster has [auto-repair enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#enabling_node_repair_and_health_checking_for_an_existing_admin_cluster), disable it. Then run `gkectl update admin`. This update finishes quickly because it does not recreate the admin cluster nodes.
     2. If the user cluster uses Seesaw, choose a node pool for the MetalLB load balancer to use, then run `gkectl update cluster`. This update only updates the nodes in the selected node pool.
  4. Make all the needed configuration changes to update your load balancer and to migrate to Controlplane V2. Then run `gkectl update cluster`.

  5. After the migration, if you disabled always-on secret encryption, re-enable the feature and run `gkectl update cluster`.




The total time for the migration depends on how many times you must run `gkectl cluster update`, which depends on your configuration. For example, suppose that you are migrating to Dataplane V2, ControlPlane V2, and to MetalLB. Also assume that there are 10 nodes in the largest node pool and 3 nodes in the node pool that MetalLB will use. To calculate an estimate for the migration time, add the following:

  * 150 minutes for the migration to Dataplane V2 because 15 minutes * 10 nodes in the biggest pool = 150 minutes.
  * 45 minutes for the node pool used by MetalLB because 15 minutes * 3 nodes in that node pool = 45 minutes.
  * 150 minutes for the Controlplane V2 and MetalLB update because 15 minutes * 10 nodes in the biggest pool = 150 minutes.



The total time for the migration is approximately 345 minutes, which is equal to 5 hours and 45 minutes.

If needed, you can do the migration in stages. Using the previous example, you can do the migration to Dataplane V2 in one maintenance window, and do the rest of the migration in one or two maintenance windows.

### Plan for downtime during migration

When planning your migration, plan for these types of downtime:

  * **Control-plane downtime** : Access to the Kubernetes API server is affected during the migration. If you are migrating to Controlplane V2, there is control-plane downtime for kubeception user clusters as the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) is migrated. The downtime is typically be less than 10 minutes, but the length of the downtime depends on your infrastructure.
  * **Workload downtime** : The virtual IPs (VIPs) used by [Services of type: LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) are unavailable. This only occurs during a migration from Seesaw to MetalLB. The MetalLB migration process will stop network connections to all VIPs in the user cluster for Kubernetes Services of type LoadBalancer for about two to ten minutes. After the migration is complete, the connections work again.



The following table describes the migration's impact:

From | To | Kubernetes API Access | User workloads  
---|---|---|---  
Kubeception cluster using Calico, which has `enableDataplaneV2` unset or set to `false` | Kubeception cluster with Dataplane V2 | Not affected | Not affected  
Kubeception cluster, which has `enableControlplaneV2` unset or set to `false` with `MetalLB` or `ManualLB` | Controlplane V2 cluster with the same kind of load balancer | Affected | Not affected  
Kubeception cluster with `loadBalancer.kind: "F5BigIP"` | Controlplane V2 cluster with manual load balancer configuration | Affected | Not affected  
Kubeception cluster with `loadBalancer.kind: "Seesaw"` | Controlplane V2 cluster with MetalLB | Affected | Affected  
  
  * **Affected** : There is a noticeable service disruption during the migration.
  * **Not affected** : There is either no service disruption or it is almost unnoticeable.



## Prepare for the migration

To ensure a successful migration, perform the steps in the following sections.

### Allocate new IP addresses

If you are migrating to Controlplane V2, allocate new static IP addresses in the same VLAN as the worker nodes (the nodes in node pools).

  * You need one IP address for the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field).

  * Allocate one IP address for each control-plane node. The number of IP addresses that you need to allocate depends on whether the user cluster will be highly available (HA) or non-HA.

    * Non-HA: one IP address
    * HA: three IP addresses



### Update firewall rules

If you are migrating to Controlplane V2, update the firewall rules on your user clusters. Ensure that the newly allocated IP addresses for the control-plane nodes on the user cluster can reach all required APIs and other destinations, as described in [Firewall rules user cluster nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_user_cluster_nodes).

### Check the cluster and node pool versions

Verify that all node pools use the same version as the user cluster, which must be at version 1.30 or higher. If not, [upgrade the node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading) to the [gkeOnPremVersion](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) in the user cluster configuration file before continuing with the migration. To check the versions, run the following command:
    
    
    gkectl version --kubeconfig ADMIN_CLUSTER_KUBECONFIG --details
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path to your admin cluster kubeconfig file.

### Check the cluster health

Check the cluster health and fix any issues that the [gkectl diagnose cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) command reports:
    
    
    gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name USER_CLUSTER_NAME
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
  * `USER_CLUSTER_NAME`: the name of the user cluster.



### Disable auto-repair in the admin cluster

If you are migrating the user cluster to use Controlplane V2 and [auto-repair is enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#enabling_node_repair_and_health_checking_for_an_existing_admin_cluster) in the admin cluster, disable auto-repair. Check the admin cluster configuration file's `autoRepair.enabled` field. If that field is unset or set to `true`, perform the following steps:

  1. In the admin cluster configuration file, set `autoRepair.enabled` to `false` . For example:
         
         autoRepair:
           enabled: false
         

  2. Update the admin cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         




Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster's kubeconfig file.
  * `ADMIN_CLUSTER_CONFIG`: the path to the admin cluster configuration file.



After the migration completes, be sure to [re-enable auto-repair in the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#enabling_node_repair_and_health_checking_for_an_existing_admin_cluster).

### Check for an issue with always-on secret encryption

If you are migrating the user cluster to use Controlplane V2, check for an issue with always-on secret encryption.

If [always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) has ever been enabled on the user cluster, you must do the steps in Disable always-on secrets encryption and decrypt secrets before starting the migration. Otherwise, the new Controlplane V2 cluster is unable to decrypt secrets.

Before startng the migration, run the following command to see if always-on secrets encryption has ever been enabled at some point:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
      get onpremusercluster USER_CLUSTER_NAME \
      -n USER_CLUSTER_NAME-gke-onprem-mgmt \
      -o jsonpath={.spec.secretsEncryption}

If the output of the preceding command is empty, then always-on secrets encryption has never been enabled. You can start the migration.

If the output of the preceding command isn't empty, then always-on secrets encryption previously had been enabled. Before migrating, you must do the steps in the next section to ensure that the new Controlplane V2 cluster can decrypt secrets.

The following example shows non-empty output:
    
    
    {"generatedKeyVersions":{"keyVersions":[1]}}
    

**Warning:** If you started the migration without first doing the steps in the next section, contact Google for support.

#### Disable always-on secrets encryption and decrypt secrets if needed

To disable always-on secrets encryption and decrypt secrets, perform the following steps:

  1. In the user cluster configuration file, to disable always-on secrets encryption add a `disabled: true` field to the `secretsEncryption` section:
         
         secretsEncryption:
             mode: GeneratedKey
             generatedKey:
                 keyVersion: KEY_VERSION
                 disabled: true
         

  2. Update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file
  3. Do a rolling update on a specific DaemonSet, as follows:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           rollout restart statefulsets kube-apiserver \
           -n USER_CLUSTER_NAME

  4. Get the manifests of all the secrets in the user cluster, in YAML format:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           get secrets -A -o yaml > SECRETS_MANIFEST.yaml

  5. So that all secrets are stored in etcd as plaintext, reapply all the secrets in the user cluster:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           apply -f SECRETS_MANIFEST.yaml

You can now start the migration to Controlplane V2. After the migration completes, you can [re-enable always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#enable_always-on_secrets_encryption) on the cluster.




### Check for an issue with misconfigured workload webhooks

If you are migrating the user cluster to use Controlplane V2, check for an issue with misconfigured workload webhooks.

If you have webhooks that includes system pods in the `kube-system` namespace, add [namespaceSelector](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector) to filter out `kube-system` namespace.

For example, 
    
    
      namespaceSelector:
        matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values:
          - kube-system
    

### Enable a node pool for use by MetalLB

If you are migrating from the bundled Seesaw load balancer to MetalLB, perform the steps in this section. The cluster is using Seesaw if `loadBalancer.kind: Seesaw` is in the user cluster configuration file. If you are migrating the integrated F5 BIG-IP configuration, skip to the next section, Migrate to Dataplane V2.

Choose a node pool and enable it for use with MetalLB. The migration deploys MetalLB on the nodes in that node pool.

**Warning:** Ensure that the node pool that you enable for use by MetalLB doesn't include the IP address of a Service with a high network address translation (NAT) ingress volume. That can cause your workloads to run out of memory. Instead, use another existing node pool or create a new node pool for MetalLB to use.

  1. In the [nodePools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepools-section) section in your user cluster configuration file, choose a node pool or [add a new node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools#add_a_node_pool), and set `enableLoadBalancer` to `true`. For example:
         
         nodePools:
           - name: pool-1
             replicas: 3
             enableLoadBalancer: true
         

  2. Update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         




For more information about MetalLB, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

## Migrate to Dataplane V2

Before migrating, check whether DataPlane V2 is enabled on the cluster by running the following command:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get onpremusercluster USER_CLUSTER_NAME -n USER_CLUSTER_NAME-gke-onprem-mgmt -o yaml | grep enableDataplaneV2
    

If Dataplane V2 is already enabled:

  * If the cluster was originally created with Dataplane V2 enabled, skip to Prepare for the load balancer migration.
  * If the cluster was previously migrated from Calico to Dataplane V2 (for example, during an upgrade to version 1.31), skip to Remove dormant Calico DaemonSets.



To migrate to Dataplane V2, you have the following options:

  * Upgrade the cluster to 1.31. For detailed steps, see [Enable Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#enable-dataplane-v2).

  * Update the 1.30 cluster.




In both cases you need to temporarily remove the `NetworkPolicy` specification as described in the following steps.

To migrate to Dataplane V2, perform the following steps. If you have concerns about temporarily removing the `NetworkPolicy` specification, contact Google Support.

If your cluster is using a `NetworkPolicy`, temporarily remove the its specification from the cluster, as follows:

  1. Check whether there's any non-system `NetworkPolicy` applied to your cluster:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get networkpolicy -A -o wide | grep -v kube-system
         

  2. If the output of the prior step was not empty, save each `NetworkPolicy` specification to a file so that you can reapply the specification after updating the cluster.
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get networkpolicy NETWORK_POLICY_NAME -n NETWORK_POLICY_NAMESPACE -o yaml > NETWORK_POLICY_NAME.yaml
         

Replace the following:

     * `NETWORK_POLICY_NAME`: the name of the `NetworkPolicy` that you are saving.
     * `NETWORK_POLICY_NAMESPACE`: the namespace of the `NetworkPolicy`.
  3. Delete the `NetworkPolicy`, using the following command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete networkpolicy NETWORK_POLICY_NAME -n NETWORK_POLICY_NAMESPACE
         




Migrate to Dataplane V2 using these steps:

  1. Set [`enableDataplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) to `true` in your user cluster configuration file.

  2. To enable DataPlane V2, update your cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
         --config USER_CLUSTER_CONFIG
         

  3. If you removed any non-system `NetworkPolicy` specifications in a prior step, then after the update completes, reapply them with this command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f NETWORK_POLICY_NAME.yaml
         




You enabled Dataplane V2.

### Remove dormant Calico DaemonSets

After you migrate an admin cluster or user cluster from Calico to Dataplane V2, the `calico-node` and `calico-route-daemon` DaemonSets remain dormant in the `kube-system` namespace to preserve rollback capability. Before you scale or upgrade the cluster, remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation once per migrated cluster so the cluster controller permanently deletes the dormant Calico DaemonSets and prevents them from initializing on new nodes (see the [Intermittent connection timeouts after upgrading or scaling a cluster migrated from Calico to Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#connection-timeouts-after-dpv2-migration-upgrade) known issue). You don't need to perform these steps on clusters that were created with Dataplane V2 enabled.

**Caution:** Only remove this annotation after the migration to Dataplane V2 is complete on all nodes. Removing it on a cluster that is still using Calico or is in the middle of migrating evicts Calico from existing nodes and disrupts Pod networking.

  1. Verify that the Dataplane V2 migration is complete and that all nodes in the cluster have the `networking.gke.io/cni-type: cilium` label:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get nodes -L networking.gke.io/cni-type
         

Replace `CLUSTER_KUBECONFIG` with the path to the user cluster or admin cluster kubeconfig file.

  2. After you confirm that Dataplane V2 is running on all nodes and you no longer need to roll back to Calico, remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation from the `OnPremUserCluster` custom resource (and from `OnPremAdminCluster` if your admin cluster was migrated from Calico during the upgrade from version 1.29 to 1.30):
         
         # For a user cluster:
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG annotate onpremusercluster USER_CLUSTER_NAME \
             -n USER_CLUSTER_NAME-gke-onprem-mgmt \
             features.onprem.cluster.gke.io/dpv2-migration-
         
         # For an admin cluster:
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG annotate onpremadmincluster ADMIN_CLUSTER_NAME \
             -n kube-system \
             features.onprem.cluster.gke.io/dpv2-migration-
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster kubeconfig file.
     * `USER_CLUSTER_NAME`: the name of the user cluster.
     * `ADMIN_CLUSTER_NAME`: the name of the admin cluster (you can find this by running `kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get onpremadmincluster -n kube-system`).
**Note:** Don't use `kubectl delete daemonset` to manually delete the DaemonSets, because the cluster controller reconciles the add-on bundle during updates and upgrades and recreates them unless you remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation.
  3. Verify that the controller deleted the `calico-node` and `calico-route-daemon` DaemonSets (both return `NotFound`):
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-system get daemonset calico-node calico-route-daemon
         




Next, prepare to migrate your cluster to the recommended load balancer and Controlplane V2.

## Prepare for the load balancer migration

If your user clusters are using the Seesaw load balancer or integrated F5 BIG-IP, follow the steps in this section to make the needed user cluster configuration file changes. Otherwise, skip to the next section, Prepare for the migration to Controlplane V2.

### F5 BIG-IP

If your clusters use the integrated F5 BIG-IP configuration, prepare for the migration to `ManualLB` by making the following changes to the user cluster configuration file:

  1. Change [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-kind-field) to `"ManualLB"`.
  2. Keep the same value for the [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field) field.
  3. If you are migrating to Controlplane V2, change the value of the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field to the IP address that you allocated. Otherwise, you can keep the same value.
  4. Delete the entire [`loadBalancer.f5BigIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-f5bigip-section) section.



The following example user cluster configuration file shows these changes:
    
    
    loadBalancer:
    vips:
      controlPlaneVIP: 192.0.2.5
      ingressVIP: 198.51.100.20
    kind: ~~"f5BigIP"~~ "ManualLB"
    ~~f5BigIP:
      address: "203.0.113.2"
      credentials:
      fileRef:
        path: "my-config-folder/user-creds.yaml"
        entry: "f5-creds"
      partition: "my-f5-user-partition"~~
    

### Seesaw

If your user clusters use the Seesaw load balancer, prepare for the migration to MetalLB by performing the steps in the following sections.

#### Specify address pools

The MetalLB controller assigns IP addresses for Services. When an application developer creates a Service of type LoadBalancer in a user cluster, the MetalLB controller automatically assigns an IP address for the Service. The MetalLB controller selects an IP address from an address pool that you specify.

To ensure your user cluster has enough IP addresses, consider the maximum number of LoadBalancer Services likely to be active. Then, specify enough IP addresses in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-metallb-section) section of your user cluster's configuration file.

**Key Point:** Because a Service of type LoadBalancer exposes the [ingress proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-service-ingress), you must include the [ingress VIP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field) for your user cluster in one of the address pools.

Addresses in the pool must be in CIDR format or range format. To specify an individual address, use a `/32` CIDR. For example:
    
    
    addresses:
      -   "192.0.2.0/26"
      -   "192.0.2.64-192.0.2.72"
      -   "192.0.2.75/32"
    

#### Exclude IP addresses used for other purposes

Don't include the following IP addresses in any address pool:

  * Control plane VIPs:

    * [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field)
    * [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field)
  * Control plane node IP addresses:

    * [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-ips-section)
    * [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section)
  * Gateway IP addresses:

    * [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-gateway-field)
    * [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-gateway-field)
  * IP addresses for Services:

    * [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-servicecidr-field)
    * [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-servicecidr-field)
  * IP addresses for Pods:

    * [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-podcidr-field)
    * [user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-podcidr-field)
  * User cluster [worker node IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file)

  * IP addresses of [vCenter servers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address), [DNS servers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-hostconfig-dnsservers-field), [NTP servers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-hostconfig-ntpservers-field), and the [admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation)




#### Update the cluster configuration file

Update the cluster configuration file to remove the Seesaw section and add a MetalLB section, as follows:

  1. Set `loadBalancer.kind` to `"MetalLB"`.
  2. You can keep the same value for the [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field) field.
  3. Add the ingress VIP to a [MetalLB address pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-metallb-addresspool-addresses-field).
  4. If you are migrating to Controlplane V2, change the value of the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field to the IP address that you allocated. Otherwise, you can keep the same value.
  5. Remove the `loadBalancer.seesaw` section.
  6. Add a [`loadBalancer.metalLB`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-metallb-section) section.



The following portion of a user cluster configuration file shows these changes and the MetalLB configuration of:

  * An address pool for the MetalLB controller to choose from and assign to Services of type LoadBalancer. The ingress VIP, which in this example is `198.51.100.10`, is in this pool in range format notation, `198.51.100.10/32`.
  * The VIP designated for the Kubernetes API server of the user cluster.
  * The ingress VIP you have configured for the ingress proxy.
  * A node pool enabled to use MetalLB. The migration deploys MetalLB on the nodes in this node pool.


    
    
    loadBalancer:
      vips:
        controlPlaneVIP: "198.51.100.50"
        ingressVIP: "198.51.100.10"
      kind: "MetalLB" ~~"Seesaw"
      seesaw:
        ipBlockFilePath: "user-cluster-2-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      metalLB:
        addressPools:
          - name: "address-pool-1"
            addresses:
            - "198.51.100.10/32"
            - "198.51.100.80 - 198.51.100.89"
    

## Prepare for the migration to Controlplane V2

If the cluster doesn't have Controlplane V2 enabled:

  * Update the user cluster configuration file.
  * If the cluster is using manual load balancing (`loadBalancer.kind: "ManualLB"`), also update the configuration on your load balancer.



These steps are described in the following sections.

If the cluster already has Controlplane V2 enabled, skip to the Migrate the user cluster section.

### Update the user cluster configuration file

Make the following changes to the existing user cluster configuration file:

  1. Set [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) to true.
  2. Optionally, make the control plane for the Controlplane V2 user cluster highly available (HA). To change from a non-HA to an HA cluster, change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.
  3. Add the static IP address (or addresses) for the user cluster control-plane node(s) to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section. The IP address (or addresses) for the control-plane nodes must be in the same VLAN as the worker nodes. The hostnames are required.
  4. Fill in the `netmask` and `gateway` in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section.
  5. If the [`network.hostConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-hostconfig-section) section is empty, fill it in.
  6. Make sure that the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field has the new IP address for the control plane VIP. The IP address has to be in the same VLAN as the control plane node IPs.
  7. If the user cluster uses manual load balancing, set [`loadBalancer.manualLB.controlPlaneNodePort`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb.controlplanenodeport-field) and [`loadBalancer.manualLB.konnectivityServerNodePort`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb.konnectivityservernodeport-field) to 0. They are not required when Controlplane V2 is enabled but they must have 0 as a value.
  8. If the user cluster uses manual load balancing, configure your load balancer as described in the next section.

**Note:** Be sure to double check all settings. All of the previous fields are immutable except when updating the cluster for the migration.

### Adjust mappings in your load balancer if needed

If your user cluster is already using manual load balancing, you need to configure some mappings on your load balancer. If you are migrating from the integrated F5 BIG-IP configuration to manual load balancing, you don't need to make any configuration changes on your load balancer and can skip to the next section, Migrate the user cluster.

For each IP address that you specified in the `network.controlPlaneIPBlock` section, configure the following mappings in your load balancer for the control-plane nodes:
    
    
    (ingressVIP:80) -> (NEW_NODE_IP_ADDRESS:ingressHTTPNodePort)
    (ingressVIP:443) -> (NEW_NODE_IP_ADDRESS:ingressHTTPSNodePort)
    

These mappings are needed for all nodes in the user cluster, both control plane nodes and worker nodes. Because NodePorts are configured on the cluster, Kubernetes opens the NodePorts on all cluster nodes so any node in the cluster can handle data plane traffic.

After you configure the mappings, the load balancer listens for traffic on the IP address that you configured for the user cluster's ingress VIP on standard HTTP and HTTPS ports. The load balancer routes requests to any node in the cluster. After a request is routed to one of the cluster nodes, internal Kubernetes networking routes the request to the destination Pod.

## Migrate the user cluster

First, carefully review all changes that you made to the user cluster configuration file. All the load balancer and Controlplane V2 settings are immutable except when you are updating the cluster for the migration.

To update the cluster, run this command:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG
    

### Controlplane V2 migration

During the Controlplane V2 migration, the update performs the following actions:

  1. Creates the control plane of a new cluster with ControlPlane V2 enabled.
  2. Stops the kubeception cluster's Kubernetes control plane.
  3. Takes an etcd snapshot of the kubeception cluster.
  4. Powers off the kubeception cluster's user cluster control plane nodes. Until the migration completes, the nodes are not deleted because that permits failure recovery by falling back to that kubeception cluster.
  5. Restores the cluster data in the new control plane, using the etcd snapshot created in an earlier step.
  6. Connects the nodepool nodes of the kubeception cluster to the new control-plane, which is accessible with the new `controlPlaneVIP`.
  7. Reconciles the restored user cluster to meet the end state of the cluster with ControlPlane V2 enabled.



Note the following:

  * There's no downtime for user cluster workloads during migration.
  * There is some downtime for the user cluster control plane during migration. Specifically, the control plane is unavailable between stopping the kubeception cluster's Kubernetes control plane and the completion of connecting the nodepool nodes of the kubeception cluster to the new control-plane. (In tests, this downtime was less than 7 minutes, but the actual length depends on your infrastructure).
  * At the end of the migration, the user cluster control plane nodes of the kubeception clusters are deleted. If the admin cluster has [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode-type-field) set to `"static"`, you can recycle some of the unused static IP addresses. You can list the admin cluster node objects with `kubectl get nodes -o wide` to see what IP addresses are in use. To recycle those IP addresses, remove them from the admin cluster configuration file and run `gkectl update admin`.
  * At the end of the migration, the worker nodes go through a rolling update. Wait for all nodes to become ready before continuing to the post-migration steps in the following section.
  * After migration, the old control plane VIP address still functions, but it is unstable. Don't rely on it. Update any dependencies on the old VIP address to use the new VIP address as soon as possible.



## After the migration

After the update completes, perform the following steps:

  1. Verify that your user cluster is running:
         
         kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
         

The output is similar to the following:
         
         cp-vm-1       Ready    control-plane,master   18m
         cp-vm-2       Ready    control-plane,master   18m
         cp-vm-3       Ready    control-plane,master   18m
         worker-vm-1   Ready                           6m7s
         worker-vm-2   Ready                           6m6s
         worker-vm-3   Ready                           6m14s
         

  2. If you migrated to Controlplane V2, update the [firewall rules on your admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters) to remove the kubeception user cluster's control-plane nodes.

  3. If you disabled always-on secret encryption, re-enable the feature.

     1. In the user cluster configuration file, remove the `disabled: true` field.
     2. Update the user cluster:
            
            gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config USER_CLUSTER_CONFIG
            

  4. If you disabled auto-repair in the admin cluster, re-enable the feature.

     1. In your admin cluster configuration file, set `autoRepair.enabled` to `true`.

     2. Update the cluster:
            
            gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config ADMIN_CLUSTER_CONFIG
            




### Load balancer migration

If you migrated the load balancer, verify that the load balancer components are running successfully.

### MetalLB migration

If you migrated to MetalLB, verify that the MetalLB components are running successfully:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pods \
        --namespace kube-system --selector app=metallb
    

The output shows Pods for the MetalLB controller and speaker. For example:
    
    
    metallb-controller-744884bf7b-rznr9   1/1     Running
    metallb-speaker-6n8ws                 1/1     Running
    metallb-speaker-nb52z                 1/1     Running
    metallb-speaker-rq4pp                 1/1     Running
    

After a successful migration, delete the powered-off Seesaw VMs for the user cluster. You can find the Seesaw VM names in the `vmnames` section of the `seesaw-for-[USERCLUSTERNAME].yaml` file in your configuration directory.

### F5 BIG-IP migration

After the migration to manual load balancing, traffic to your clusters isn't interrupted. This is because the existing F5 resources still exist, as you can see by running the following command:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
    api-resources --verbs=list -o name | xargs -n 1 kubectl --kubeconfig
    CLUSTER_KUBECONFIG get --show-kind --ignore-not-found
    --selector=onprem.cluster.gke.io/legacy-f5-resource=true -A
    

The expected output is similar to the following:
    
    
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
