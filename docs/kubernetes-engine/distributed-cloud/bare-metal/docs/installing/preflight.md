---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight/
title: Preflight checks \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:19.475842+00:00
---

# Preflight checks  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Preflight checks Stay organized with collections  Save and categorize content based on your preferences. 

Preflight checks let you identify issues before you perform major cluster operations, such as creating or upgrading clusters. When checks run automatically ahead of an operation, Google Distributed Cloud blocks cluster modifications until all validations pass. You can also run checks on demand or bypass them during cluster management workflows.

Google Distributed Cloud executes these validations when you create or upgrade clusters and node pools with `bmctl`. It also runs internal checks when an admin or hybrid cluster updates resources on user clusters. If any check fails, no changes are applied to your clusters.

## `PreflightCheck` custom resources

When a preflight check runs, Google Distributed Cloud creates a `PreflightCheck` custom resource. `PreflightCheck` custom resources are persistent and provide a record of the preflight check activities and outcomes.

To retrieve `PreflightCheck` custom resources:

  1. Get a list of preflight checks that have run for a given cluster:
         
         kubectl get preflightchecks --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The response lists the resources by namespace. You can run `kubectl get preflightchecks` across all namespaces for a comprehensive list. For each resource, the response shows the age of the resource and whether or not the preflight checks passed. The following sample response shows `PreflightCheck` resources for the `cluster-test-admin001` namespace.
    
    NAMESPACE              NAME                                PASS    AGE
    cluster-test-admin001   test-admin001                      true    52d
    cluster-test-admin001   test-admin001jkm4q                 true    52d
    cluster-test-admin001   test-admin001k79t7                 true    6d20h
    cluster-test-admin001   upgrade-cluster-20231106-222746    true    6d20h
    

  2. Retrieve the details for a specific `PreflightCheck` custom resource:
         
         kubectl describe preflightchecks --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The following sample command response shows a `PreflightCheck` resource for a successful preflight check that ran as part of cluster creation:
    
    Name:         create-cluster-20230922-175006
    Namespace:    cluster-test-user001
    Labels:       <none>
    Annotations:  <none>
    API Version:  baremetal.cluster.gke.io/v1
    Kind:         PreflightCheck
    Metadata:
      Creation Timestamp:  2023-09-22T17:50:11Z
      Generation:          1
      Resource Version:    6502800
      UID:                 917daf64-963d-44b4-a1f9-c54972a39191
    Spec:
      Check Image Version:  latest
      Config YAML:          ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-test-user
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: test-user001
      namespace: cluster-test-user001
    spec:
      type: user
      profile: default
      anthosBareMetalVersion: 1.16.0
      gkeConnect:
        projectID: clusters-project
      controlPlane:
        nodePoolSpec:
          nodes:
          - address: 192.0.2.53
      ...
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-test-user001
    spec:
      clusterName: test-user001
      nodes:
      - address: 192.0.2.54
      ...
    Status:
      Checks:
        192.0.2.53:
          Job UID:  d0b5dc1f-9d39-4cc8-b3d2-0841212f7f8c
          Message:  
          Pass:     true
        192.0.2.53-gcp:
          Job UID:  b4d96ce5-0d4e-4e3c-97db-6317e0c15fc8
          Message:  
          Pass:     true
        192.0.2.54:
          Job UID:  b67cf195-3951-46ad-b91c-0d79025cfc0a
          Message:  
          Pass:     true
        192.0.2.54-gcp:
          Job UID:  aed509e2-4bf7-44c4-bfa0-8147ef8ea74e
          Message:  
          Pass:     true
        Gcp:
          Job UID:  ac479ac4-e1c4-4681-9f2b-5773069bf6ae
          Message:  
          Pass:     true
        Node - Network:
          Job UID:  8a57c4ee-ad17-4560-8809-b117c871ad5d
          Message:  
          Pass:     true
        Pod - Cidr:
          Message:  
          Pass:     true
      Cluster Spec:
        Anthos Bare Metal Version:  1.16.0
        Bypass Preflight Check:     false
        Cluster Network:
          Bundled Ingress:  true
          Pods:
            Cidr Blocks:
              10.0.0.0/16
          Services:
            Cidr Blocks:
              10.96.0.0/20
      ...
      Completion Time:                 2023-09-22T17:51:22Z
      Conditions:
        Last Transition Time:  2023-10-02T23:59:06Z
        Observed Generation:   1
        Reason:                Reconciling
        Status:                True
        Type:                  Reconciling
      Node Pool Specs:
        node-pool-1:
          Cluster Name:  test-user001
          Nodes:
            Address:         192.0.2.54
        ...
      Pass:                  true
      Start Time:            2023-09-22T17:50:32Z
    Events:                  <none>
    

In the preceding `PreflightCheck` custom resource, the `Status` section contains the following information:

     * The `Checks` section lists individual preflight checks that were run and whether or not they passed. In this example, the following checks ran: 
       * `192.0.2.53` and `192.0.2.54`: node checks (OS configuration, resources, and software settings) for machines with IP addresses `192.0.2.53` and `192.0.2.54`.
       * `192.0.2.53-gpc` and `192.0.2.54-gcp`: Google Cloud connectivity checks (Artifact Registry and Google API access) for machines with IP addresses `192.0.2.53` and `192.0.2.54`.
       * `Gcp`: Google Cloud connectivity checks for the cluster.
       * `Node - Network`: Network checks (connectivity, `etcd` operation, VIP access, and port binding) for the cluster.
       * `Pod - Cidr`: Pod IP address checks for overlapping addresses for the cluster.
     * The `Cluster Spec` section shows the cluster configuration.
     * The `Pass` field shows `true`, indicating that the preflight checks passed collectively.



## Preflight check logs

When preflight checks run as a result of a `bmctl` command, such as `bmctl check preflight`, Google Distributed Cloud creates log files. Here's what gets generated and where:

  * Preflight check logs are generated in a directory with the following naming pattern `preflight-TIMESTAMP`.

  * This preflight directory is created in the `log` directory for the cluster in the `bmctl` workspace. By default, the `log` directory path is `bmctl-workspace/CLUSTER_NAME/log`.

  * The preflight logs consist of the following files:

    * Log files for node machine checks, one for each cluster node. These log files are named using the IP address of the node. For example, a filename might be `192.0.2.53`.

    * Log files for Google Cloud access checks, one for each cluster node. These log files are named using the IP address of the node. For example, a filename might be `192.0.2.53-gcp`.

    * Log file for cluster Google Cloud access checks, which is named `gcp`.

    * Log file for node networking checks, which is named `node-network`.




If a preflight check fails, these log files can help you identify and troubleshoot the problem.

## Preflight checks for cluster creation

When you [create clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview), Google Distributed Cloud automatically runs preflight checks before any changes are made.

### What's checked?

Preflight checks for installation check the following:

  * Node machine checks:

    * Cluster machines are using a supported operating system (OS).

    * OS version is supported.

    * OS is using a supported kernel version.

    * Node machines are configured to use `cgroupsv2`. The check fails if  
`cgroupsv1` is detected.

    * For Ubuntu, Uncomplicated Firewall (UFW) is disabled.

    * For Ubuntu, package manager `apt` is operable and required packages are available.

    * For Red Hat Enterprise Linux, package manager `dnf` is operable and required packages are available.

    * For Red Hat Enterprise Linux, Podman isn't installed.

    * Node machines meet the minimum CPU requirements.

    * Node machines meet the minimum memory requirements.

    * Node machines meet the minimum disk storage requirements.

    * Time synchronization is configured on node machines.

    * `kubelet` is active and running on node machines.

    * `containerd` is active and running on node machines.

    * Default route for routing packets to the default gateway is present in nodes.

    * Domain Name System (DNS) is functioning properly. If the cluster is configured to run behind a proxy, this check is skipped.

    * Pod CIDRs don't overlap with node machine IP addresses.

    * If the cluster is configured to use a registry mirror, the registry mirror is reachable.

  * Google Cloud checks for each node and for the cluster:

    * Artifact Registry, `gcr.io`, reachability is checked. If the cluster is configured to use a registry mirror, this check is skipped.

    * Google APIs are reachable.

  * Node networking checks (varies based on load balancing configuration):

    * VIP for the Kubernetes API server is accessible.

    * Load balancer VIPs are accessible.

    * Nodes can communicate on required ports.

    * The `etcd` events instance is provisioned and port requirements are met.




When all checks pass, Google Distributed Cloud creates the cluster. For more information about the requirements for creating clusters, see [Installation prerequisites overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq).

### Run on-demand preflight checks for cluster creation

You can also run preflight checks independently, before you create a cluster. Doing so can be beneficial as major cluster operations, such as cluster creation, are time-consuming. Identifying and resolving issues separately before starting a major cluster operation may help you with scheduling.

**Note:** Preflight checks are updated as known issues are identified. To direct `bmctl` to run the checks from the latest patch image of your installed minor version, use the `--check-image-version latest` option flag. For more information, see Run the latest preflight checks.

###  Self-managed clusters 

  * The following command validates the specified cluster configuration file, but doesn't try to create the cluster itself:
        
        bmctl check config --cluster CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of the cluster that's associated with the configuration file you're checking.

  * This command checks whether the machines and network are ready for cluster creation:
        
        bmctl check preflight --cluster CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of the cluster that you're checking.




###  User clusters 

  * The following command validates the specified cluster config file, but doesn't try to create the cluster itself:
        
        bmctl check config --cluster CLUSTER_NAME --admin-kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the user cluster that you're checking.
    * `ADMIN_KUBECONFIG`: the path of the associated admin cluster kubeconfig file.
  * The following command checks whether the machines and network are ready for cluster creation:
        
        bmctl check preflight --cluster CLUSTER_NAME --admin-kubeconfig ADMIN_KUBECONFIG
        




`bmctl` supports the use of `--kubeconfig` as an alias for the`--admin-kubeconfig` flag.

## Preflight checks for cluster upgrades

When you [upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade), Google Distributed Cloud automatically runs preflight checks before any changes are made.

### What's checked?

Preflight checks for cluster upgrades check the following:

  * Node machine checks:

    * Cluster machines are using a supported operating system (OS).

    * OS version is supported.

    * OS is using a supported kernel version.

    * Node machines are configured to use `cgroupsv2`. The check fails if `cgroupsv1` is detected.

    * For Ubuntu, Uncomplicated Firewall (UFW) is disabled.

    * Node machines meet the minimum CPU requirements.

    * Node machines have more than 20% of CPU resources available.

    * Node machines meet the minimum memory requirements.

    * Node machines meet the minimum disk storage requirements.

    * Time synchronization is configured on node machines.

    * Default route for routing packets to the default gateway is present in nodes.

    * Domain Name System (DNS) is functioning properly. If the cluster is configured to run behind a proxy, this check is skipped.

    * If the cluster is configured to use a registry mirror, the registry mirror is reachable.

    * No control plane nodes or load balancer nodes are in maintenance mode.
  * Google Cloud checks for each node and for the cluster:

    * Artifact Registry, `gcr.io`, reachability is checked. If the cluster is configured to use a registry mirror, this check is skipped.

    * Google APIs are reachable.

  * Machine checks:

    * `kubelet` is active and running on node machines.

    * `containerd` is active and running on node machines.

    * Container Network Interface (CNI) health endpoint status is healthy.

    * Pod CIDRs don't overlap with node machine IP addresses.

    * `kubeadm` certificates haven't expired.
  * Node networking checks (varies based on load balancing configuration):

    * VIP for the Kubernetes API server is accessible.

    * Load balancer VIPs are accessible.

    * Nodes can communicate on required ports.

    * The `etcd` events instance is provisioned and port requirements are met.


**Note:** On cluster node machines, if the Docker executable is present in the `PATH` environment variable, but the Docker service isn't active, the preflight check fails. You can either remove Docker or enable the Docker service.

When all checks pass, Google Distributed Cloud upgrades the cluster. For more information about upgrading clusters, see [Best practices for Google Distributed Cloud cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-best-practices) and [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).

### Run on-demand preflight checks for cluster upgrades

The `bmctl check preflight` command lets you run a preflight check before upgrading your cluster. You can check if the clusters are ready for an upgrade by running the following preflight check command before starting the upgrade:

**Note:** Preflight checks are updated as known issues are identified. To direct `bmctl` to run the checks from the latest patch image of your installed minor version, use the `--check-image-version latest` option flag. For more information, see Run the latest preflight checks.

  1. Update the cluster version (`anthosBareMetalVersion`) in the cluster configuration file.

  2. Use the following command to check if the clusters are ready for an upgrade and run a preflight check:
         
         bmctl check preflight --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster to upgrade.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

When you create the preflight check with this command to test a cluster upgrade, a `PreflightCheck` custom resource is created in the admin cluster.




## Internal preflight checks on existing clusters

Google Distributed Cloud performs internal preflight checks automatically when you apply Kubernetes resources to an existing cluster. If any checks fail, Google Distributed Cloud doesn't change any of the related nodes unless you bypass the checks explicitly.

### Bypass preflight checks when applying Kubernetes resources

To ignore the internal preflight checks when applying resources to existing clusters, you need to set the `BypassPreflightCheck` field to `true` in the cluster configuration file.

Here's part of a cluster configuration file that shows the `bypassPreflightCheck` field set to `true`:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-user1
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user1
      namespace: cluster-user1
    spec:
      type: user**  bypassPreflightCheck: true**
      # Anthos cluster version.
      anthosBareMetalVersion: 1.36.200-gke.118
    ...
    

## Run the latest preflight checks

Preflight checks (and health checks) are updated as known issues are identified. To direct `bmctl` to run the checks from the latest patch image of your installed minor version, use the `--check-image-version latest` option flag:
    
    
    bmctl check preflight --cluster CLUSTER_NAME **--check-image-version latest**
    

Replace `CLUSTER_NAME` with the name of the cluster that you're checking.

This can help you catch any recently identified known issues without first creating or upgrading your cluster.

You can also perform the latest health checks of a live cluster to determine whether it's operating properly. For more information, see [Run the latest health checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/healthchecks#on_demand_latest).

## Ignore the results of automated preflight checks

If you run preflight checks on demand before you create or upgrade clusters, you can bypass the automated preflight checks. To bypass automated preflight checks, use the optional `--force` flag when you run `bmctl create cluster` or `bmctl upgrade cluster`.

## What's next

  * [Health checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/healthchecks)

  * [Node Problem Detector](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-problem-detector)

  * [Check cluster connectivity with nettest](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/nettest)

  * [Create snapshots to help diagnose cluster problems](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/bmctl-snapshot)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
