---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha/
title: Migrate an admin cluster to HA \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:15.937877+00:00
---

# Migrate an admin cluster to HA  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate an admin cluster to HA Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows how to migrate to a high availability (HA) admin cluster from a non-HA admin cluster at version 1.29.

**Note:** If your clusters are at version 1.30 or higher, we recommend that instead you use a streamlined approach described in [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

1.29: Preview  
1.28: Not available  


Before and after the migration, the admin cluster has three nodes:

  * A non-HA admin cluster has one control-plane node and two add-on nodes.
  * An HA admin cluster has three control-plane nodes and no add-on nodes, and availability is significantly improved.



## Prepare for the migration

If your admin cluster version is 1.29.0-1.29.600 or 1.30.0-1.30.100, and if [always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) was enabled in the admin cluster at version 1.14 or earlier, you must rotate the encryption key before starting the migration. Otherwise, the new HA admin cluster will be unable to decrypt secrets.

To check whether the cluster could be using an old encryption key:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secret -n kube-system admin-master-component-options -o jsonpath='{.data.data}' | base64 -d | grep -oP '"GeneratedKeys":\[.*?\]'
    

If the output shows an empty key, such as in the following example, you must rotate the encryption key.
    
    
    "GeneratedKeys":[{"KeyVersion":"1","Key":""}]
    

### Rotate the encryption key if needed

If the steps in the preceding section showed that you need to rotate the encryptions key, perform the following steps:

  1. Increment the `keyVersion` in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#secretsencryption-generatedkey-version-field).

  2. Update the admin cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config ADMIN_CLUSTER_CONFIG
         

This creates a new key matching the new version number, re-encrypts each secret, and securely erases the old secrets. All subsequent new secrets are encrypted using the new encryption key.


**Warning:** If you started the migration without rotating the encryption key, contact Google Support.

## Procedure overview

The migration involves these primary steps:

  1. Edit the admin cluster configuration file.

  2. Run `gkectl update admin`. This command performs the following:

     * Brings up an external cluster (Kind) and ensures the current non-HA admin cluster is in a healthy state.

     * Creates a new admin cluster control plane using HA spec and a new control plane VIP.

     * Turns off the existing admin cluster control plane.

     * Takes an etcd snapshot of the existing admin cluster.

     * Restores the old admin cluster data in the new HA control plane.

     * Reconciles the restored admin cluster to meet the end state of HA admin cluster.




## Notes

  * During the migration, there's no downtime for user cluster workload.

  * During the migration, there is some downtime for the admin cluster control plane. (Downtime is less than 18 minutes, based on our tests, but the actual length depends on individual infrastructure environments).

  * Requirements for HA admin clusters still hold for non-HA to HA migration. For example, HA admin clusters don't support Seesaw so if you are using the Seesaw load balancer for a non-HA admin cluster, you must first [migrate to MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb), before migrating to an HA admin cluster.

  * After the migration completes successfully, left-over resources such as the non-HA admin master VM, are intentionally kept for failure recovery.




## Before and after migration

The following table shows the primary differences in the cluster before and after migration:

| Before migration| After migration  
---|---|---  
Control-plane node replicas| 1| 3  
Add-on nodes| 2| 0  
Control-plane Pod replicas  
(kube-apiserver, kube-etcd, etc.)| 1| 3  
Data disk size| 100GB * 1| 25GB * 3  
Data disks path | Set by [vCenter.dataDisk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-datadisk-field) in the admin cluster configuration file | Auto generated under the directory: `/anthos/[ADMIN_CLUSTER_NAME]/default/[MACHINE_NAME]-data.vmdk`  
Load balancer for the control-plane VIP | Set by [loadBalancer.kind](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancerkind) in the admin cluster configuration file | `keepalived` \+ `haproxy`  
Allocation of IP addresses for admin cluster control-plane nodes | DHCP or static, depending on [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode-type-field) | 3 static IP addresses  
Allocation of IP addresses for [kubeception](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses-kubeception) user cluster control-plane nodes | DHCP or static, depending on [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field) | DHCP or static, depending on [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field)  
Checkpoint file| Enabled by default| Not used  
  
## Edit the admin cluster configuration file

You must specify four additional IP addresses:

  * Three IP addresses for the admin cluster's control-plane nodes
  * A new control-plane VIP for the admin cluster load balancer



You must also change a few other fields in your admin cluster configuration file, as described in the following sections.

### Specify IP addresses

  1. In the admin cluster configuration file, fill in the [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section) section. Hostnames are required for HA admin clusters. For example:
         
         controlPlaneIPBlock:
           netmask: "255.255.255.0"
           gateway: "172.16.20.1"
           ips:
           - ip: "172.16.20.50"
             hostname: "admin-cp-node-1"
           - ip: "172.16.20.51"
             hostname: "admin-cp-node-2"
           - ip: "172.16.20.52"
             hostname: "admin-cp-node-3"
         

  2. Fill in the [hostconfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-hostconfig-section) section. If your admin cluster uses static IP addresses, this section is already filled in. For example:
         
         hostConfig:
           dnsServers:
           - 203.0.113.1
           - 198.51.100.1
           ntpServers:
           - 216.239.35.12
         

  3. Replace the value of [loadBalancer.vips.controlPlaneVIP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) with a new VIP. For example:
         
         loadBalancer:
          vips:
            controlPlaneVIP: "172.16.20.59"
         




### Update additional configuration fields

  1. Set [adminMaster.replicas](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#adminmaster-replicas-field) to `3`:
         
         adminMaster:
          replicas: 3
          cpus: 4
          memoryMB: 8192
         

  2. Remove the [vCenter.dataDisk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-datadisk-field) field. For an HA admin cluster, the paths for the three data disks used by control-plane nodes are automatically generated under the root directory `anthos` in the datastore.

  3. If [loadBalancer.manualLB.controlPlaneNodePort](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/admin-cluster-configuration-file#loadbalancer-manuallb-controlplanenodeport-field) has a non-zero value, set it to `0`.




## Adjust manual load balancer configuration

If your admin cluster uses manual load balancing, complete this section. Otherwise, skip this section.

For each of the three new control-plane node IP addresses that you specified in the [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section) section, configure the following mapping in your load balancer:

(old controlPlaneVIP:443) -> (NEW_NODE_IP_ADDRESS:old controlPlaneNodePort)

This mapping ensures that the old control-plane VIP works during the migration.

## Update the admin cluster

Review the configuration changes that you made because the fields are immutable. When you have confirmed the changes are correct, update the cluster.

  1. Start the migration:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file.

     * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file

  2. The command displays the migration's progress.

When prompted, enter `Y` to continue.

  3. When the migration completes, the admin cluster kubeconfig file is automatically updated to use the new control-plane VIP. The older control-plane VIP continues to function and can also be used to access the new HA admin cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
