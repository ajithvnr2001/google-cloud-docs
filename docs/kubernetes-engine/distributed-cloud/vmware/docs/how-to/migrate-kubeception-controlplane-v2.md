---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2/
title: Migrate a user cluster to Controlplane V2 \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:42.144728+00:00
---

# Migrate a user cluster to Controlplane V2  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate a user cluster to Controlplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to migrate a version 1.29 user cluster using kubeception to Controlplane V2. If your clusters are at version 1.30 or higher, we recommend that you follow the instructions in [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

1.29: Preview  
1.28: Not available  


## About user cluster control planes

Prior to Google Distributed Cloud version 1.13, the control plane for a user cluster ran on one or more nodes in an admin cluster. This kind of control plane is referred to as kubeception. In version 1.13, Controlplane V2 was introduced for new user clusters. When Controlplane V2 is enabled, the control plane for the user cluster runs in the user cluster itself.

The benefits of Controlplane V2 include the following:

  * **Failure isolation**. An admin cluster failure does not affect user clusters.

  * **Operational separation**. An admin cluster upgrade does not cause downtime for user clusters.

  * **Deployment separation**. You can place the admin and user clusters in different failure domains or geographical sites. For example, a user cluster in an edge location can be in a different geographical site from the admin cluster.




## Requirements

To migrate a user cluster to Controlplane V2, the user cluster must meet the following requirements:

  * The user cluster must be version 1.29 or higher. The admin cluster and node pools can be one or two minor versions lower than the user cluster. If needed, [upgrade the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

  * The user cluster must have [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) enabled. This field is immutable, so if Dataplane V2 isn't enable on the cluster, you can't migrate it to Controlplane V2.

  * The user cluster must be configured to use either the MetalLB or a manual load balancer. If the user cluster is using the SeeSaw load balancer, you can [migrate it to MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb). 

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses#example_ip_addresses_user_cluster_1_nodes), and ensure that you have enough IP addresses available for the user cluster's control plane nodes. The control plane nodes require static IP addresses, and you will need an additional IP address for a new control plane virtual IP (VIP).




## Prepare for the migration

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

### Disable always-on secrets encryption and decrypt secrets if needed

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




### Fix misconfigured workload webhooks

If you have webhooks that includes system pods in the `kube-system` namespace, add [namespaceSelector](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector) to filter out `kube-system` namespace.

For example, 
    
    
      namespaceSelector:
        matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values:
          - kube-system
    

## Update the user cluster configuration file

Make the following changes to the existing user cluster configuration file:

  1. Set [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) to true.

  2. Optionally, make the control plane for the Controlplane V2 user cluster highly available (HA). To change from a non-HA to to an HA cluster, change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.

  3. Add the static IP address (or addresses) for the user cluster control plane node(s) to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section. The IP address (or addresses) for the control-plane nodes must be in the same VLAN as the worker nodes. The hostnames are required.

  4. Fill in the netmask and gateway in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section.

  5. If the [`network.hostConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-hostconfig-section) section is empty, fill it in.

  6. If the user cluster uses [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance), configure your load balancer as described in the [next section](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2#adjust_manual_load_balancer_configuration).

  7. If the user cluster uses manual load balancing, set [`loadBalancer.manualLB.controlPlaneNodePort`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb.controlplanenodeport-field) and [`loadBalancer.manualLB.konnectivityServerNodePort`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb.konnectivityservernodeport-field) to 0 as they are not required when Controlplane V2 is enabled.

  8. Update the [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) field with the new IP address for the control plane VIP. Note that it has to be in the same VLAN as the [control plane node IPs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section).

  9. All of the previous fields are immutable except when updating the cluster for the migration. Be sure to double check all settings.

  10. Run [`gkectl diagnose cluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster), and fix any issues that the command finds.
         
         gkectl diagnose cluster --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
               --cluster-name=USER_CLUSTER_NAME

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `USER_CLUSTER_NAME`: the name of the user cluster.




## Adjust manual load balancer configuration

If your user cluster uses manual load balancing, do the step in this section. Otherwise skip this section.

Similarly to [configure your load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#config_lb) for a CPv2 user cluster, for each of the three new control-plane node IP addresses that you specified in the [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section, configure the mappings in your load balancer:

  * (ingressVIP:80) -> (NEW_NODE_IP_ADDRESS:ingressHTTPNodePort)
  * (ingressVIP:443) -> (NEW_NODE_IP_ADDRESS:ingressHTTPNodePort)



## Update the cluster

Run the following command to migrate the cluster to Controlplane V2:
    
    
    gkectl update cluster \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.




The command does the following:

  1. Create the control plane of a new cluster with ControlPlane V2 enabled.

  2. Stop the Kubernetes control plane of the kubeception cluster.

  3. Take an etcd snapshot of the kubeception cluster.

  4. Power off the user cluster control plane nodes of the kubeception cluster. Note that for the sake of failure recovery, that is, falling back to the kubeception cluster, the nodes are not deleted until the completion of the migration.

  5. Restore the cluster data in the new control plane with the aforementioned etcd snapshot.

  6. Connect the nodepool nodes of the kubeception cluster to the new control-plane, which is accessible with the new `controlPlaneVIP`.

  7. Reconcile the restored user cluster to meet the end state of the cluster with ControlPlane V2 enabled.




## Notes

  * During the migration, there's no downtime for user cluster workloads.

  * During the migration, there is some downtime for the user cluster control plane. More specifically, the control plane is unavailable between step 2 and the completion of step 6. (The downtime is less than 7 minutes based on our tests, but the actual length depends on your infrastructure).

  * At the end of the migration, the user cluster control plane nodes of the kubeception clusters are deleted. If the admin cluster has [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode-type-field) set to "static", you can recycle some of the unused static IPs by removing them from the admin cluster configuration file and run `gkectl update admin`. You can list the admin cluster node objects with `kubectl get nodes -o wide` to see what IPs are in use.

  * After migration, the old control plane VIP address still functions, but it is unstable. Don't rely on it. Update any dependencies on the old VIP address to use the new VIP address as soon as possible.




## After the migration

If you disabled always-on secrets encryption before the migration, do the following steps to re-enable the feature:

  1. In the user cluster configuration file, set `secretsEncryption.generatedKey.disabled` to false. For example:
         
         secretsEncryption:
             mode: GeneratedKey
             generatedKey:
                 keyVersion: KEY_VERSION
                 disabled: false
         

  2. Update the user cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
