---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb/
title: Migrate from the Seesaw load balancer to MetalLB \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:44.135370+00:00
---

# Migrate from the Seesaw load balancer to MetalLB  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate from the Seesaw load balancer to MetalLB Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to migrate from the Seesaw load balancer to the [MetalLB load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) for versions 1.16 to 1.29. If your clusters are at version 1.30 or higher, we recommend that you follow the instructions in [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

Using MetalLB has several [benefits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb#benefits_of_using_metallb) compared to other [load balancing options](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance).

1.28 and 1.29: GA  
1.16: Preview

**Warning:** Don't migrate to MetalLB if you are relying on Seesaw for client IP address preservation. More specifically, don't migrate to MetalLB if there are Services in the cluster with `spec.externalTrafficPolicy` set to `Local`.

To check the `externalTrafficPolicy`, run the following command:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get svc -A -o yaml | grep "externalTrafficPolicy: Local"
    

Contact Google Support for help with this issue.

## Notes on downtime

There is workload downtime during the migration. The following notes apply only to non-high availability (non-HA) admin clusters because the SeeSaw load balancer doesn't support HA admin clusters.

  * When migrating an admin cluster:

    * There is control-plane downtime for kubeception user clusters as the [`controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-1.29#loadbalancer-vips-controlplanevip-field) is migrated. The downtime should be less than 10 minutes, but the length of the downtime depends on your infrastructure.

    * There is downtime for the admin cluster control plane as the admin master node needs to be recreated with the `controlPlaneVIP` directly attached to the VM. The downtime should be less than 20 minutes, but the length of downtime depends on your infrastructure.

  * When migrating a user cluster, there is an outage for the VIPs after the Seesaw load balancer is powered off and before the MetalLB Pods come up. This process generally takes about one minute.




## User cluster migration

You must choose a node pool and enable it for use with MetalLB. MetalLB will be deployed on the nodes in this node pool.

**Warning:** Make sure that the node pool that you enable for use by MetalLB doesn't include the IP address of a Service with a high network address translation (NAT) ingress volume. Doing so could cause your workloads to run out of memory. Instead, use another existing node pool or create a new node pool for MetalLB to use.

In your user cluster configuration file, choose a node pool, and set `enableLoadBalancer` to `true`:
    
    
    nodePools:
    - name: pool-1
      replicas: 3
      enableLoadBalancer: true
    

Update the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of the user cluster configuration file




Next, remove the Seesaw sections from the file, and add a MetalLB section.

Then update the cluster again:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Verify that the MetalLB components are running successfully:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pods \
        --namespace kube-system --selector app=metallb
    

The output shows Pods for the MetalLB controller and speaker. For example:
    
    
    metallb-controller-744884bf7b-rznr9   1/1     Running
    metallb-speaker-6n8ws                 1/1     Running
    metallb-speaker-nb52z                 1/1     Running
    metallb-speaker-rq4pp                 1/1     Running
    

**Important:** The migration process will stop network connections to all VIPs in the user cluster for Kubernetes Services of type LoadBalancer for two to ten minutes. After the migration is complete, the connections will work again.

After a successful migration, manually delete the Seesaw VMs, which are already powered off, for the user cluster. You can find the Seesaw VM names in the `vmnames` section of the `seesaw-for-[USERCLUSTERNAME].yaml` file in your configuration directory.

### Example: User cluster, static IP addresses

Suppose you have a user cluster that uses static IP addresses for its cluster nodes. Also suppose that the cluster has two Services of type `LoadBalancer`, and the external addresses for those Services are 172.16.21.41 and 172.16.21.45.

Adjust the user cluster configuration file as follows:

  * Keep the `network.hostConfig` section.
  * Set `loadBalancer.kind` to `MetalLB`.
  * Remove the `loadBalancer.seesaw` section.
  * Add a `loadBalancer.metalLB` section.



Example:
    
    
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
        ntpServers:
        - "216.239.35.0"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.30"
        ingressVIP: "172.16.20.31"
      kind: MetalLB ~~Seesaw~~
      ~~seesaw:
        ipBlockFilePath: "user-cluster-1-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
          - "172.16.20.31/32"
          - "172.16.20.40 - 172.16.21.49"
      

Key points from the preceding example:

  * Even though the cluster will no longer use the Seesaw load balancer, the `network.hostConfig` section is needed, because the cluster nodes use static IP addresses.

  * The value of `ingressVIP` appears in the MetalLB address pool.

  * The external IP addresses, 172.16.21.41 and 172.16.21.45, for the existing Services of type `LoadBalancer` are included in the MetalLB address pool.




### Example: kubeception user cluster, DHCP

Suppose you have a user cluster that uses DHCP for its cluster nodes. Also suppose that the cluster has two Services of type `LoadBalancer`, and the external addresses for those Services are 172.16.21.61 and 172.16.21.65.

Adjust the user cluster configuration file as follows:

  * Remove the `network.hostConfig` section.
  * Set `loadBalancer.kind` to `MetalLB`.
  * Remove the `loadBalancer.seesaw` section.
  * Add a `loadBalancer.metalLB` section.



Example:
    
    
    enableControlplaneV2: false
    network:
    ~~hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
        ntpServers:
        - "216.239.35.0"~~
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.50"
        ingressVIP: "172.16.20.51"
      kind: MetalLB ~~Seesaw~~
      ~~seesaw:
        ipBlockFilePath: "user-cluster-2-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
          - "172.16.20.51/32"
          - "172.16.20.60 - 172.16.21.69"
      

Key points from the preceding example:

  * The cluster will no longer use the Seesaw load balancer, and the cluster does not use static IP addresses for its cluster nodes. So the `network.hostConfig` section is not needed.

  * The value of `ingressVIP` appears in the MetalLB address pool.

  * The external IP addresses, 172.16.21.61 and 172.16.21.65, for the existing Services of type `LoadBalancer` are included in the MetalLB address pool.




### Example: Controlplane V2 user cluster, DHCP

Suppose you have a user cluster that has Controlplane V2 enabled, and uses DHCP for its worker nodes. Also suppose that the cluster has two Services of type `LoadBalancer`, and the external addresses for those Services are 172.16.21.81 and 172.16.21.85.

Adjust the user cluster configuration file as follows:

  * Keep the `network.hostconfig` section.
  * Set `loadBalancer.kind` to `MetalLB`.
  * Remove the `loadBalancer.seesaw` section.
  * Add a `loadBalancer.metalLB` section.



Example:
    
    
    enableControlplaneV2: true
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
        ntpServers:
        - "216.239.35.0"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.70"
        ingressVIP: "172.16.20.71"
      kind: MetalLB ~~Seesaw~~
      ~~seesaw:
        ipBlockFilePath: "user-cluster-2-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
          - "172.16.20.71/32"
          - "172.16.20.80 - 172.16.21.89"
      

Key points from the preceding example:

  * The cluster will no longer use static IP addresses for the worker nodes, but it will use static IP addresses for the control-plane nodes. So the `network.hostConfig` section is needed.

  * The value of `ingressVIP` appears in the MetalLB address pool.

  * The external IP addresses, 172.16.21.81 and 172.16.21.85, for the existing Services of type `LoadBalancer` are included in the MetalLB address pool.




## Admin cluster migration

In your admin cluster configuration file, set `loadBalancer.kind` to `MetalLB`, and remove the `loadBalancer.seesaw` section.

Update the cluster:
    
    
    gkectl update admin --kubeconfig  ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file




Verify that the MetalLB components are running successfully: 
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods \
        --namespace kube-system --selector app=metallb
    

The output shows Pods for the MetalLB controller and speaker. For example:
    
    
    metallb-controller-744884bf7b-rznr9   1/1     Running
    metallb-speaker-6n8ws                 1/1     Running
    metallb-speaker-nb52z                 1/1     Running
    metallb-speaker-rq4pp                 1/1     Running
    

**Important:** The migration process will stop network connections to all VIPs in the admin cluster for Kubernetes Services of type LoadBalancer for two to ten minutes. After the migration is complete, the connections will work again.

After a successful migration, manually delete the Seesaw VMs, which are already powered off, for the admin cluster. You can find the Seesaw VM names in the `vmnames` section of the `seesaw-for-gke-admin.yaml` file in your configuration directory.

### Example: Admin cluster, static IP addresses

Suppose you have an admin cluster that uses static IP addresses for its cluster nodes.

Adjust the admin cluster configuration file as follows:

  * Keep the `network.hostConfig` section.
  * Set `loadBalancer.kind` to `MetalLB`.
  * Remove the `loadBalancer.seesaw` section.



Example:
    
    
    network:
      hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
        ntpServers:
        - "216.239.35.0"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.30"
      kind: MetalLB ~~Seesaw~~
      ~~seesaw:
        ipBlockFilePath: "user-cluster-1-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      

Key point from the preceding example:

  * Even though the cluster will no longer use the Seesaw load balancer, the `network.hostConfig` section is needed, because the cluster nodes use static IP addresses.



### Example: Admin cluster, DHCP

Suppose you have an admin cluster that uses DHCP for its cluster nodes.

Adjust the admin cluster configuration file as follows:

  * Remove the `network.hostConfig` section.
  * Set `loadBalancer.kind` to `MetalLB`.
  * Remove the `loadBalancer.seesaw` section.



Example:
    
    
    network:
    ~~hostConfig:
        dnsServers:
        - "172.16.255.1"
        - "172.16.255.2"
        ntpServers:
        - "216.239.35.0"~~
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.30"
      kind: MetalLB ~~Seesaw~~
      ~~seesaw:
        ipBlockFilePath: "user-cluster-1-ipblock.yaml"
        vrid: 1
        masterIP: ""
        cpus: 4
        memoryMB: 3072~~
      

Key point from the preceding example:

  * The cluster will no longer use the Seesaw load balancer, and the cluster does not use static IP addresses for its cluster nodes. So the `network.hostConfig` section is not needed.



## Troubleshooting

If `gkectl update` fails during user cluster migration, and the MetalLB Pods are not running in the user cluster, manually power on the user cluster Seesaw VMs. This will re-establish traffic to currently used VIPs. But newly created VIPs might not be served by the Seesaw VMs if the `load-balancer-seesaw` Pod is not running. If that is the case, create a support ticket.

If `gkectl update` fails during admin cluster migration, and the MetalLB Pods are not running in the admin cluster, manually power on the admin cluster Seesaw VMs. This might allow traffic to currently used control plane VIPs for user clusters to work again. But the VIP for the control plane of the admin cluster itself might not work. In that case, edit the kubeconfig file of the admin cluster to directly use the IP address of the admin cluster control-plane node.

Also, in the `kube-system` namespace, change the `kube-apiserver` Service type from `ClusterIP` to `LoadBalancer`. If necessary, create a support ticket.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
