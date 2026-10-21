---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/healthchecks/
title: Health checks \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:54.807475+00:00
---

# Health checks  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/healthchecks/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Health checks Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/healthchecks)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/healthchecks)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Health checks are a way to test and monitor the operation of your existing clusters. Health checks run on their own, periodically. You can also use `bmctl` to run health checks on demand. This document describes each check, in what circumstances it runs automatically, how and when to run it manually, and how to interpret results.

## What's checked?

There are two categories of Distributed Cloud health checks:

  * Node machine checks

  * Cluster-wide checks




The following sections outline what gets checked for each category. These checks are used for both periodic and on-demand health checks.

### Node machine checks

This section describes what's evaluated by health checks for node machines. These checks confirm that node machines are configured properly and that they have sufficient resources and connectivity for cluster creation, cluster upgrades, and cluster operation.

These checks correspond to the Bare Metal `HealthCheck` custom resources named `bm-system-NODE_IP_ADDRESS-machine` (for example, `bm-system-192.0.2.54-machine`) that run in the admin cluster in the cluster namespace. For more information about health check resources, see `HealthCheck` custom resources.

**Note:** The common machine checks and machine Google Cloud checks are used in [preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight) too.

Common machine checks consist of the following:

  * Cluster machines are using a supported operating system (OS).

  * OS version is supported.

  * OS is using a supported kernel version.

  * Kernel has the BPF Just In Time (JIT) compiler option enabled (`CONFIG_BPF_JIT=y`).

  * For Ubuntu, Uncomplicated Firewall (UFW) is disabled.

  * Node machines meet the minimum CPU requirements.

  * Node machines have more than 20% of CPU resources available.

  * Node machines meet the minimum memory requirements.

  * Node machines meet the minimum disk storage requirements.

  * Time synchronization is configured on node machines.

  * Default route for routing packets to the default gateway is present in nodes.

  * Domain Name System (DNS) is functional (this check is skipped if the cluster is configured to run behind a proxy).

  * If the cluster is configured to use a registry mirror, the registry mirror is reachable.




Machine Google Cloud checks consist of the following:

  * Container Registry, `gcr.io` is reachable (this check is skipped if the cluster is configured to use a registry mirror).

  * Google APIs are reachable.




Machine health checks consist of the following:

  * `kubelet` is active and running on node machines.

  * `containerd` is active and running on node machines.

  * Container Network Interface (CNI) health endpoint status is healthy.

  * Pod CIDRs don't overlap with node machine IP addresses.




For more information about the node machine requirements, see [Cluster node machine prerequisites](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/node-machine-prerequisites).

### Cluster-wide checks

This section describes what's evaluated by health checks for a cluster.

#### Network checks

The following client-side cluster node network checks run automatically as part of periodic health checks. Network checks can't be run on-demand. These checks correspond to the Bare Metal `HealthCheck` custom resources named `bm-system-network` that run in the admin cluster in the cluster namespace. For more information about health check resources, see `HealthCheck` custom resources.

  * If the cluster uses bundled load balancing, nodes in the load balancing node pool must have Layer 2 address resolution protocol (ARP) connectivity. ARP is required for VIP discovery.

  * Control plane nodes have ports 2382 and 2383 open for use by the `etcd-events` instance.




For information about protocols and port usage for your Google Distributed Cloud clusters, see [Network requirements](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs).

The network checks for a preflight check differ from the network health checks. For a list of the network checks for a preflight check, see either [Preflight checks for cluster creation](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#pre_create) or [Preflight checks for cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#pre_upgrade).

#### Kubernetes

Kubernetes checks, which run automatically as part of preflight and periodic health checks, can also be run on-demand. These health checks don't return an error if any of the listed control plane components are missing. The check only returns errors if the components exist and have errors at command-execution time.

These checks correspond to the Bare Metal `HealthCheck` custom resources named `bm-system-kubernetes`resources running in the admin cluster in the cluster namespace. For more information about health check resources, see `HealthCheck` custom resources.

  * API server is functioning.

  * The `anetd` operator is configured correctly.

  * All control plane nodes are operable.

  * The following control plane components are functioning properly:

    * `anthos-cluster-operator`

    * `controller-manager`

    * `cluster-api-provider`

    * `ais`

    * `capi-kubeadm-bootstrap-system`

    * `cert-manager`

    * `kube-dns`




#### Add-ons

Add-ons checks run automatically as part of preflight checks and periodic health checks and can be run on-demand. This health check doesn't return an error if any of the listed add-ons are missing. The check only returns errors if the add-ons exist and have errors at command-execution time.

These checks correspond to Bare Metal `HealthCheck` custom resources named `bm-system-add-ons*`resources running in the admin cluster in the cluster namespace. For more information about health check resources, see `HealthCheck` custom resources.

  * Cloud Logging Stackdriver components and Connect Agent are operable:

    * `stackdriver-log-aggregator`

    * `stackdriver-log-forwarder`

    * `stackdriver-metadata-agent`

    * `stackdriver-prometheus-k8`

    * `gke-connect-agent`

  * Distributed Cloud-managed resources show no manual changes (config drift):

    * Field values haven't been updated

    * Optional fields haven't been added or removed

    * Resources haven't been deleted




If the health check detects config drift, the `bm-system-add-ons` Bare Metal `HealthCheck` custom resource `Status.Pass` value is set to `false`. The `Description` field in the `Failures` section contains details about any resources that have changed, including the following information:

  * `Version`: the API version for the resource.
  * `Kind`: the object schema, such as `Deployment`, for the resource.
  * `Namespace`: the namespace that the resource is in.
  * `Name`: the name of the resource.
  * `Diff`: a string format comparison of differences between the resource manifest on record and the manifest for the changed resource.



## `HealthCheck` custom resources

When a health check runs, Distributed Cloud creates a `HealthCheck` custom resource. `HealthCheck` custom resources are persistent and provide a structured record of the health check activities and outcomes. There are two categories of `HeathCheck` custom resources:

  * Bare Metal `HealthCheck` custom resources (`API Version: baremetal.cluster.gke.io/v1`): these resources provide details about periodic health checks. These resources are on the admin cluster in cluster namespaces. Bare Metal `HealthCheck` resources are responsible for creating health check cron jobs and jobs. These resources are consistently updated with the most recent results.

  * Anthos `HealthCheck` custom resources (`API Version: anthos.gke.io/v1`): these resources are used to report health check metrics. These resources are in the `kube-system` namespace of each cluster. Updates of these resources are _best effort_. If an update fails to an issue, such as a transient network error, the failure is ignored.




The following table lists the types of resources that are created for either `HealthCheck` category:

Bare Metal HealthChecks | GKE Enterprise HealthChecks | Severity  
---|---|---  
Type: machine  Name: `bm-system-NODE_IP_ADDRESS-machine` |  Type: machine  Name: `bm-system-NODE_IP_ADDRESS-machine` | Critical  
Type: network  Name: `bm-system-network` |  Type: network  Name: `bm-system-network` | Critical  
Type: kubernetes  Name: `bm-system-kubernetes` |  Type: kubernetes  Name: `bm-system-kubernetes` | Critical  
Type: add-ons  Name: `bm-system-add-ons` |  Type: add-ons  Name: `bm-system-add-ons-add-ons` Name: `bm-system-add-ons-configdrift` | Optional  
  
To retrieve `HealthCheck` status:

  1. To read the results of periodic health checks, you can get the associated custom resources:
         
         kubectl get healthchecks.baremetal.cluster.gke.io --kubeconfig ADMIN_KUBECONFIG --all-namespaces
         

Replace `ADMIN_KUBECONFIG` with the path of the admin cluster kubeconfig file.

The following sample shows the health checks that run periodically and whether the checks passed when they last ran:
         
         NAMESPACE               NAME                               PASS    AGE
         cluster-test-admin001   bm-system-192.0.2.52-machine       true    11d
         cluster-test-admin001   bm-system-add-ons                  true    11d
         cluster-test-admin001   bm-system-kubernetes               true    11d
         cluster-test-admin001   bm-system-network                  true    11d
         cluster-test-user001    bm-system-192.0.2.53-machine       true    56d
         cluster-test-user001    bm-system-192.0.2.54-machine       true    56d
         cluster-test-user001    bm-system-add-ons                  true    56d
         cluster-test-user001    bm-system-kubernetes               true    56d
         cluster-test-user001    bm-system-network                  true    56d
         

**Note:** All periodic health check resources have the label `baremetal.cluster.gke.io/periodic-health-check=true`.
  2. To read details for a specific health check, use `kubectl describe`:
         
         kubectl describe healthchecks.baremetal.cluster.gke.io HEALTHCHECK_NAME --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `HEALTHCHECK_NAME`: the name of the health check.
     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

When you review the resource, the `Status:` section contains the following important fields:

     * `Pass`: indicates whether or not the last health check job passed.
     * `Checks`: contains information about the most recent health check job.
     * `Failures`: contains information about the most recent failed job.
     * `Periodic`: contains information such as when was the last time a health check job was scheduled and instrumented.

The following `HealthCheck` sample is for a successful machine check:
    
    Name:         bm-system-192.0.2.54-machine
    Namespace:    cluster-test-user001
    Labels:       baremetal.cluster.gke.io/periodic-health-check=true
                  machine=192.0.2.54
                  type=machine
    Annotations:  <none>
    API Version:  baremetal.cluster.gke.io/v1
    Kind:         HealthCheck
    Metadata:
      Creation Timestamp:  2023-09-22T18:03:27Z
      ...
    Spec:
      Anthos Bare Metal Version:  1.16.0
      Cluster Name:               nuc-user001
      Interval In Seconds:        3600
      Node Addresses:
        192.168.1.54
      Type:  machine
    Status:
      Check Image Version:  1.16.0-gke.26
      Checks:
        192.168.1.54:
          Job UID:  345b74a6-ce8c-4300-a2ab-30769ea7f855
          Message:  
          Pass:     true
      ...
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
      Conditions:
        Last Transition Time:  2023-11-22T17:53:18Z
        Observed Generation:   1
        Reason:                LastPeriodicHealthCheckFinished
        Status:                False
        Type:                  Reconciling
      Node Pool Specs:
        node-pool-1:
          Cluster Name:  nuc-user001
        ...
      Pass:                  true
      Periodic:
        Last Schedule Time:                    2023-11-22T17:53:18Z
        Last Successful Instrumentation Time:  2023-11-22T17:53:18Z
      Start Time:                              2023-09-22T18:03:28Z
    Events:
      Type    Reason                  Age                  From                    Message
      ----    ------                  ----                 ----                    -------
      Normal  HealthCheckJobFinished  6m4s (x2 over 6m4s)  healthcheck-controller  health check job bm-system-192.0.2.54-machine-28344593 finished
    

The following `HealthCheck` sample is for a failed machine check:
    
    Name:         bm-system-192.0.2.57-machine
    Namespace:    cluster-user-cluster1
    ...
    API Version:  baremetal.cluster.gke.io/v1
    Kind:         HealthCheck
    ...
    Status:
      Checks:
        192.0.2.57:
          Job UID:  492af995-3bd5-4441-a950-f4272cb84c83
          Message:  following checks failed, ['check_kubelet_pass']
          Pass:     false
      Failures:
        Category:     AnsibleJobFailed
        Description:  Job: machine-health-check.
        Details:       Target: 1192.0.2.57. View logs with: [kubectl logs -n cluster-user-test bm-system-192.0.2.57-machine-28303170-qgmhn].
        Reason:       following checks failed, ['check_kubelet_pass']
      Pass:                  false
      Periodic:
        Last Schedule Time:                    2023-10-24T23:04:21Z
        Last Successful Instrumentation Time:  2023-10-24T23:31:30Z
      ...
    

  3. To get a list of health checks for metrics, use the following command:
         
         kubectl get healthchecks.anthos.gke.io --kubeconfig CLUSTER_KUBECONFIG --namespace kube-system
         

Replace `CLUSTER_KUBECONFIG` with the path of the target cluster kubeconfig file.

The following sample shows the response format:
         
         NAMESPACE     NAME                                            COMPONENT   NAMESPACE   STATUS    LAST_COMPLETED
         kube-system   bm-system-10.200.0.3-machine                                            Healthy   56m
         kube-system   bm-system-add-ons-add-ons                                               Healthy   48m
         kube-system   bm-system-add-ons-configdrift                                           Healthy   48m
         kube-system   bm-system-kubernetes                                                    Healthy   57m
         kube-system   bm-system-kubernetes-1.16.1-non-periodic                                Healthy   25d
         kube-system   bm-system-network                                                       Healthy   32m
         kube-system   check-kubernetes-20231114-190445-non-periodic                           Healthy   3h6m
         kube-system   component-status-controller-manager                                     Healthy   5s
         kube-system   component-status-etcd-0                                                 Healthy   5s
         kube-system   component-status-etcd-1                                                 Healthy   5s
         kube-system   component-status-scheduler                                              Healthy   5s
         




## Health check cron jobs

For periodic health checks, each bare metal `HealthCheck` custom resource has a corresponding [`CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) with the same name. This `CronJob` is responsible for scheduling the corresponding health check to run at set intervals.

To retrieve information about cron jobs:

  1. Get a list of cron jobs that have run for a given cluster:
         
         kubectl get cronjobs --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The following sample shows a typical response:
    
    NAMESPACE           NAME                           SCHEDULE       SUSPEND   ACTIVE   LAST SCHEDULE   AGE
    cluster-test-admin   bm-system-10.200.0.3-machine   17 */1 * * *   False     0        11m             25d
    cluster-test-admin   bm-system-add-ons              25 */1 * * *   False     0        3m16s           25d
    cluster-test-admin   bm-system-kubernetes           16 */1 * * *   False     0        12m             25d
    cluster-test-admin   bm-system-network              41 */1 * * *   False     0        47m             25d
    

The values in the `SCHEDULE` column indicate the schedule for each health check job run in [schedule syntax](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#schedule-syntax). For example, the `bm-system-kubernetes` job runs at 17 minutes past the hour (`17`) every hour (`*/1`) of every day (`* * *`). The time intervals for periodic health checks aren't editable, but it's useful for troubleshooting to know when they're supposed to run.

  2. Retrieve details for a specific `CronJob` custom resource:
         
         kubectl describe cronjob CRONJOB_NAME --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The following sample shows a successful `CronJob`:
    
    Name:                          bm-system-network
    Namespace:                     cluster-test-admin
    Labels:                        AnthosBareMetalVersion=1.16.1
                                  baremetal.cluster.gke.io/check-name=bm-system-network
                                  baremetal.cluster.gke.io/periodic-health-check=true
                                  controller-uid=2247b728-f3f5-49c2-86df-9e5ae9505613
                                  type=network
    Annotations:                   target: node-network** Schedule:                      41 */1 * * ***
    Concurrency Policy:            Forbid
    Suspend:                       False
    Successful Job History Limit:  1
    Failed Job History Limit:      1
    Starting Deadline Seconds:     <unset>
    Selector:                      <unset>
    Parallelism:                   <unset>
    Completions:                   1
    Active Deadline Seconds:       3600s
    Pod Template:
      Labels:           baremetal.cluster.gke.io/check-name=bm-system-network
      Annotations:      target: node-network
      Service Account:  ansible-runner
      Containers:
      ansible-runner:
        Image:      gcr.io/anthos-baremetal-release/ansible-runner:1.16.1-gke.5
        Port:       <none>
        Host Port:  <none>
        Command:
          cluster
        Args:
          -execute-command=network-health-check
          -login-user=root
          -controlPlaneLBPort=443
        Environment:  <none>
        Mounts:
          /data/configs from inventory-config-volume (ro)
          /etc/ssh-key from ssh-key-volume (ro)
      Volumes:
      inventory-config-volume:
        Type:      ConfigMap (a volume populated by a ConfigMap)
        Name:      bm-system-network-inventory-bm-system-ne724a7cc3584de0635099
        Optional:  false
      ssh-key-volume:
        Type:            Secret (a volume populated by a Secret)
        SecretName:      ssh-key
        Optional:        false
    Last Schedule Time:  Tue, 14 Nov 2023 18:41:00 +0000
    Active Jobs:         <none>
    Events:
      Type    Reason            Age   From                Message
      ----    ------            ----  ----                -------
      Normal  SuccessfulCreate  48m   cronjob-controller  Created job bm-system-network-28333121
      Normal  SawCompletedJob   47m   cronjob-controller  Saw completed job: bm-system-network-28333121, status: Complete
      Normal  SuccessfulDelete  47m   cronjob-controller  Deleted job bm-system-network-28333061
    




## Health check logs

When health checks run, they generate logs. Whether you run health checks with `bmctl` or they run automatically as part of periodic health checks, logs are sent to Cloud Logging. When run health checks on demand, log files are created in a time-stamped folder in the `log/` directory of your cluster folder on your admin workstation. For example, if you run the `bmctl check kubernetes` command for a cluster named `test-cluster`, you find logs in a directory like `bmctl-workspace/test-cluster/log/check-kubernetes-20231103-165923`.

### View logs locally

You can use `kubectl` to view logs for periodic health checks:

  1. Get pods and find the specific health check pod you're interested in:
         
         kubectl get pods --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The following sample response shows some health check pods:
    
    NAME                                                              READY   STATUS      RESTARTS   AGE
    bm-system-10.200.0.4-machine-28353626-lzx46                       0/1     Completed   0          12m
    bm-system-10.200.0.5-machine-28353611-8vjw2                       0/1     Completed   0          27m
    bm-system-add-ons-28353614-gxt8f                                  0/1     Completed   0          24m
    bm-system-check-kernel-gce-user001-02fd2ac273bc18f008192e177x2c   0/1     Completed   0          75m
    bm-system-cplb-init-10.200.0.4-822aa080-7a2cdd71a351c780bf8chxk   0/1     Completed   0          74m
    bm-system-cplb-update-10.200.0.4-822aa082147dbd5220b0326905lbtj   0/1     Completed   0          67m
    bm-system-gcp-check-create-cluster-202311025828f3c13d12f65k2xfj   0/1     Completed   0          77m
    bm-system-kubernetes-28353604-4tc54                               0/1     Completed   0          34m
    bm-system-kubernetes-check-bm-system-kub140f257ddccb73e32c2mjzn   0/1     Completed   0          63m
    bm-system-machine-gcp-check-10.200.0.4-6629a970165889accb45mq9z   0/1     Completed   0          77m
    ...
    bm-system-network-28353597-cbwk7                                  0/1     Completed   0          41m
    bm-system-network-health-check-gce-user05e0d78097af3003dc8xzlbd   0/1     Completed   0          76m
    bm-system-network-preflight-check-create275a0fdda700cb2b44b264c   0/1     Completed   0          77m
    

  2. Retrieve pod logs:
         
         kubectl logs POD_NAME  --kubeconfig ADMIN_KUBECONFIG --namespace CLUSTER_NAMESPACE
         

Replace the following:

     * `POD_NAME`: the name of the health check pod.
     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `CLUSTER_NAMESPACE`: the namespace of the cluster.

The following sample shows part of a pod log for a successful node machine health check:
    
    ...
    TASK [Summarize health check] **************************************************
    Wednesday 29 November 2023  00:26:22 +0000 (0:00:00.419)       0:00:19.780 ****
    ok: [10.200.0.4] => {
        "results": {
            "check_cgroup_pass": "passed",
            "check_cni_pass": "passed",
            "check_containerd_pass": "passed",
            "check_cpu_pass": "passed",
            "check_default_route": "passed",
            "check_disks_pass": "passed",
            "check_dns_pass": "passed",
            "check_docker_pass": "passed",
            "check_gcr_pass": "passed",
            "check_googleapis_pass": "passed",
            "check_kernel_version_pass": "passed",
            "check_kubelet_pass": "passed",
            "check_memory_pass": "passed",
            "check_pod_cidr_intersect_pass": "passed",
            "check_registry_mirror_reachability_pass": "passed",
            "check_time_sync_pass": "passed",
            "check_ubuntu_1804_kernel_version": "passed",
            "check_ufw_pass": "passed",
            "check_vcpu_pass": "passed"
        }
    }
    ...
    

The following sample shows part of a failed node machine health check pod log. The sample shows that the `kubelet` check (`check_kubelet_pass`) failed, indicating that the `kubelet` isn't running on this node.
    
    ...
    TASK [Reach a final verdict] ***************************************************
    Thursday 02 November 2023  17:30:19 +0000 (0:00:00.172)       0:00:17.218 *****
    fatal: [10.200.0.17]: FAILED! => {"changed": false, "msg": "following checks failed, ['check_kubelet_pass']"}
    ...
    




### View logs in Cloud Logging

Health check logs are streamed to Cloud Logging and can be viewed in Logs Explorer. Periodic health checks are classed as Pods in the console logs.

  1. In the Google Cloud console, go to the **Logs Explorer** page in the **Logging** menu.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, enter the following basic query:
         
         resource.type="k8s_container"
         resource.labels.pod_name=~"bm-system.*-machine.*"
         

  3. The **Query results** window shows the logs for node machine health checks.




Here's a list of queries for periodic health checks:

  * Node machine
        
        resource.type="k8s_container"
        resource.labels.pod_name=~"bm-system.*-machine.*"
        

  * Network
        
        resource.type="k8s_container"
        resource.labels.pod_name=~"bm-system-network.*"
        

  * Kubernetes
        
        resource.type="k8s_container"
        resource.labels.pod_name=~"bm-system-kubernetes.*"
        

  * Add-ons
        
        resource.type="k8s_container"
        resource.labels.pod_name=~"bm-system-add-ons.*"
        




## Periodic health checks

By default, the periodic health checks run hourly and check the following cluster components:

  * Machine
  * Network
  * Kubernetes
  * Add-ons



You can check the cluster health by looking at the Bare Metal `HealthCheck` (`healthchecks.baremetal.cluster.gke.io`) custom resources on the admin cluster. The Network, Kubernetes, and Add-ons checks are cluster-level checks, so there is a single resource for each check. A Machine check is run for each node in the target cluster, so there is a resource for each node.

  * To list Bare Metal `HealthCheck` resources for a given cluster, run the following command:
        
        kubectl get healthchecks.baremetal.cluster.gke.io --kubeconfig=ADMIN_KUBECONFIG \
            --namespace=CLUSTER_NAMESPACE
        

Replace the following:

    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

    * `CLUSTER_NAMESPACE`: the namespace of the target cluster of the health check.

The following sample response shows the format:
    
    NAMESPACE               NAME                               PASS    AGE
    cluster-test-user001    bm-system-192.0.2.53-machine       true    56d
    cluster-test-user001    bm-system-192.0.2.54-machine       true    56d
    cluster-test-user001    bm-system-add-ons                  true    56d
    cluster-test-user001    bm-system-kubernetes               true    56d
    cluster-test-user001    bm-system-network                  true    56d
    

The `Pass` field for `healthchecks.baremetal.cluster.gke.io` indicates whether the last health check passed (`true`) or failed (`false`). 




For more information about checking the status for periodic health checks, see `HealthCheck` custom resources and Health check logs.

### Disable periodic health checks

Periodic health checks are enabled by default on all clusters. You can disable periodic health checks for a cluster by setting the `periodicHealthCheck.enable` field to `false` in Cluster resource.

To disable periodic health checks:

  1. Edit the cluster configuration file and add the `periodicHealthCheck.enable` field to the Cluster spec and set its value to `false`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-user-basic
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: user-basic
           namespace: cluster-user-basic
         spec:
           type: user
           profile: default
           ...**  periodicHealthCheck:
             enable: false**
           ...
         

  2. Update the cluster by running the `bmctl update` command:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  3. To verify that periodic health checks have been disabled, run the following command to confirm that the corresponding `healthchecks.baremetal.cluster.gke.io` resources have been deleted:
         
         kubectl get healthchecks.baremetal.cluster.gke.io --kubeconfig=ADMIN_KUBECONFIG \
             --namespace=CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `CLUSTER_NAMESPACE`: the namespace of the target cluster of the health check.




### Re-enable periodic health checks

Periodic health checks are enabled by default on all clusters. If you've disabled periodic health checks, you can re-enable them by setting the `periodicHealthCheck.enable` field to `true` in Cluster resource.

To re-enable periodic health checks:

  1. Edit the cluster configuration file and add the `periodicHealthCheck.enable` field to the Cluster spec and set its value to `true`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-user-basic
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: user-basic
           namespace: cluster-user-basic
         spec:
           type: user
           profile: default
           ...**  periodicHealthCheck:
             enable: true**
           ...
         

  2. Update the cluster by running the `bmctl update` command:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  3. To verify that periodic health checks are enabled, run the following command to confirm that the corresponding `healthchecks.baremetal.cluster.gke.io` resources are present:
         
         kubectl get healthchecks.baremetal.cluster.gke.io --kubeconfig=ADMIN_KUBECONFIG \
             --namespace=CLUSTER_NAMESPACE
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `CLUSTER_NAMESPACE`: the namespace of the target cluster of the health check.

It may take a couple of minutes for the resources to appear.




## On-demand health checks

The following sections describe the health checks that you can run on demand with `bmctl check`. When you use `bmctl check` to run health checks, the following rules apply:

  * When you check a user cluster with a `bmctl check` command, specify the path of the kubeconfig file for the admin cluster with the `--kubeconfig` flag.

  * Logs are generated in a time-stamped directory in the cluster log folder on your admin workstation (by default, `bmctl-workspace/CLUSTER_NAME/log`).

  * Health check logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.




For more information about options for `bmctl` commands, see [bmctl command reference](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/bmctl).

### Add-ons

Check that the specified Kubernetes add-ons for the specified cluster are operable.

  * To check add-ons for a cluster:
        
        bmctl check add-ons --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you're checking.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



For a list of what's checked, see Add-ons in the What's checked section of this document.

This check generates log files in a `check-addons-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### Cluster

Check all cluster nodes, node networking, Kubernetes, and add-ons for the specified cluster. You provide the cluster name, and `bmctl` looks for the cluster configuration file at `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME.yaml`, by default.

  * To check the health of a cluster:
        
        bmctl check cluster --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you're checking.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



For a list of what's checked, see the following sections in the What's checked section of this document:

  * Node machine-level checks
  * Network checks
  * Kubernetes
  * Add-ons



This check generates log files in a `check-cluster-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### Config

Check the cluster configuration file. This check expects that you have generated the configuration file and edited it to specify the cluster configuration details for your cluster. The purpose of this command is to determine whether any configuration setting is wrong, missing, or has any syntax errors. You provide the cluster name, and `bmctl` looks for the cluster configuration file at `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME.yaml`, by default.

  * To check a cluster configuration file:
        
        bmctl check config --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you're checking.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



This command checks the YAML syntax of the cluster configuration file, Google Cloud access, and permissions for the service account specified in the cluster configuration file.

This check generates log files in a `check-config-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### GCP

Check that all cluster node machines can access Container Registry (`gcr.io`) and the Google APIs endpoint (`googleapis.com`).

  * To check the cluster access to required Google Cloud resources:
        
        bmctl check gcp --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you're checking.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



This check generates log files in a `check-gcp-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### Kubernetes

Check the health of critical Kubernetes operators running in the control plane. This check verifies that critical operators are working properly and that their pods aren't crashing. This health check doesn't return an error if any of the control plane components are missing: it only returns errors if the components exist and have errors at command-execution time.

  * To check the health of Kubernetes components in your cluster:
        
        bmctl check kubernetes --cluster CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that contains the nodes you're checking.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



For a list of what's checked, see Kubernetes in the What's checked section of this document.

This check generates log files in a `check-kubernetes-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### Nodes

Check cluster node machines to confirm that they're configured properly and that they have sufficient resources and connectivity for cluster upgrades and cluster operation.

  * To check the health of node machines in your cluster:
        
        bmctl check nodes --cluster CLUSTER_NAME --addresses NODE_IP_ADDRESSES --kubeconfig ADMIN_KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that contains the nodes you're checking.
    * `NODE_IP_ADDRESSES`: a comma-separated list of IP addresses for node machines.
    * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.



For a list of what's checked, see Node machine checks in the What's checked section of this document.

This check generates log files for each cluster node machine in a `check-nodes-TIMESTAMP` directory in the cluster log folder on your admin workstation. Logs are also sent to Cloud Logging. For more information about the logs, see Health check logs.

### Preflight

For information about using `bmctl` to run preflight checks, see [Run on-demand preflight checks for cluster creation](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#pre_create_bmctl) and [Run on-demand preflight checks for cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#pre_upgrade_bmctl).

### VM Runtime preflight check

The VM Runtime on Google Distributed Cloud preflight check validates a set of node machine prerequisites before using VM Runtime on Google Distributed Cloud and VMs. If VM Runtime on Google Distributed Cloud preflight check fails, VM creation is blocked. When `spec.enabled` is set to `true` in the `VMRuntime` custom resource, the VM Runtime on Google Distributed Cloud preflight check runs automatically.
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VMRuntime
    metadata:
      name: vmruntime
    spec:**  enabled: true**
    ...
    

For more information, see [VM Runtime on Google Distributed Cloud preflight check](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/enable-disable#preflight_check).

## What's next

  * [Node Problem Detector](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/node-problem-detector)

  * [Check cluster connectivity with nettest](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/nettest)

  * [Create snapshots to help diagnose cluster problems](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/bmctl-snapshot)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
