---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose/
title: Diagnosing cluster issues \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:11.100054+00:00
---

# Diagnosing cluster issues  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Diagnosing cluster issues Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/diagnose)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/diagnose)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to use `gkectl diagnose` to diagnose issues in your clusters.

## Overview

The `gkectl` tool has two commands for troubleshooting issues with clusters: `gkectl diagnose cluster` and `gkectl diagnose snapshot`. The commands work with both admin and user clusters.

### `gkectl diagnose cluster`

Performs health checks on your cluster and reports errors. Runs health checks on the following components:

  * VCenter 
    * Credential
    * DRS
    * Anti Affinity Groups
    * Network
    * Version
    * Datacenter
    * Datastore
    * ResourcePool
    * Folder
    * Network
  * Loadbalancer (F5, Seesaw, Manual)
  * User cluster and node pools
  * Cluster objects
  * Konnectivity server readiness of the user cluster
  * Machine objects and the corresponding cluster nodes
  * Pods in the kube-system and gke-system namespaces
  * Control plane
  * vSphere persistent volumes in the cluster
  * User and admin cluster vCPU (virtual CPU) and memory contention signals
  * User and admin cluster ESXi [preconfigured Host CPU Usage and Memory Usage alarms](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.monitoring.doc/GUID-82933270-1D72-4CF3-A1AF-E5A1343F62DE.html).
  * Time of day (TOD)
  * Node network policy for a cluster with Dataplane V2 enabled
  * Overall healthiness of the Dataplane V2 node agent



### `gkectl diagnose snapshot`

This command compresses a cluster's status, configurations, and logs into a tarball file. If you run `gkectl diagnose snapshot`, that command automatically runs `gkectl diagnose cluster` as part of the process, and output files are placed in a new folder in the snapshot called `/diagnose-report`.

The default configuration of the `gkectl diagnose snapshot` command also captures the following information about your cluster:

  * Kubernetes version

  * Status of Kubernetes resources in the kube-system and gke-system namespaces: cluster, machine, nodes, Services, Endpoints, ConfigMaps, ReplicaSets, CronJobs, Pods, and the owners of those Pods, including Deployments, DaemonSets, and StatefulSets

  * Status of the control plane

  * Details about each node configuration including IP addresses, iptables rules, mount points, file system, network connections, and running processes

  * Container logs from the admin cluster's control-plane node, when Kubernetes API server is not available

  * vSphere information including VM objects and their Events based on Resource Pool. Also Datacenter, Cluster, Network, and Datastore objects associated with VMs

  * F5 BIG-IP load balancer information including virtual server, virtual address, pool, node, and monitor

  * Logs from the `gkectl diagnose snapshot` command

  * Logs of preflight jobs

  * Logs of containers in namespaces based on the scenarios

  * Information about admin cluster Kubernetes certificate expiration in the snapshot file `/nodes/<admin_master_node_name>/sudo_kubeadm_certs_check-expiration`

  * An HTML index file for all of the files in the snapshot

  * Optionally, the admin cluster configuration file used to install and upgrade the cluster with the `--config` flag.




Credentials, including vSphere and F5 credentials, are removed before the tarball is created.

## Get help

To get help about the commands available:
    
    
    gkectl diagnose --help
    

### Diagnose an admin cluster

To diagnose an admin cluster:
    
    
    gkectl diagnose cluster --kubeconfig=ADMIN_CLUSTER_KUBECONFIG
    

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.

Examle output:
    
    
    Preparing for the diagnose tool...
    Diagnosing the cluster......DONE
    
    - Validation Category: Admin Cluster Connectivity
    Checking VMs TOD (availability)...SUCCESS
    Checking Konnectivity Server (readiness)...SUCCESS
    
    - Validation Category: Admin Cluster F5 BIG-IP
    Checking f5 (credentials, partition)...SUCCESS
    
    - Validation Category: Admin Cluster VCenter
    Checking Credentials...SUCCESS
    Checking DRS enabled...SUCCESS
    Checking Hosts for AntiAffinityGroups...SUCCESS
    Checking Version...SUCCESS
    Checking Datacenter...SUCCESS
    Checking Datastore...SUCCESS
    Checking Resource pool...SUCCESS
    Checking Folder...SUCCESS
    Checking Network...SUCCESS
    
    - Validation Category: Admin Cluster
    Checking cluster object...SUCCESS
    Checking machine deployment...SUCCESS
    Checking machineset...SUCCESS
    Checking machine objects...SUCCESS
    Checking kube-system pods...SUCCESS
    Checking anthos-identity-service pods...SUCCESS
    Checking storage...SUCCESS
    Checking resource...SUCCESS
    Checking virtual machine resource contention...SUCCESS
    Checking host resource contention...SUCCESS
    All validation results were SUCCESS.
    Cluster is healthy!
    

If there is an issue with a virtual IP address (VIP) in the target cluster, use the `--config` flag to provide the admin cluster configuration file. That gives you more debugging information.
    
    
    gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config CLUSTER_CONFIG
    

Replace CLUSTER_CONFIG with the path of the admin or user cluster configuration file.

**Note:** Always set `--kubeconfig` to the path of the admin cluster kubeconfig file, regardless of whether you are diagnosing an admin or user cluster.

Example output:
    
    
    Failed to access the api server via LB VIP "...": ...
    Try to use the admin master IP instead of problematic VIP...
    Reading config with version "[CONFIG_VERSION]"
    Finding the admin master VM...
    Fetching the VMs in the resource pool "[RESOURCE_POOL_NAME]"...
    Found the "[ADMIN_MASTER_VM_NAME]" is the admin master VM.
    Diagnosing admin|user cluster "[TARGET_CLUSTER_NAME]"...
    ...
    

### Diagnose a user cluster

To get the name of a user cluster:
    
    
    kubectl get cluster --kubeconfig=USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of the user cluster kubeconfig file.

To diagnose a user cluster:
    
    
    gkectl diagnose cluster --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME
    

Replace USER_CLUSTER_NAME with the name of the user cluster.

Example output:
    
    
    Preparing for the diagnose tool...
    Diagnosing the cluster......DONE
    
    Diagnose result is saved successfully in 
    
    - Validation Category: User Cluster Connectivity
    Checking Node Network Policy...SUCCESS
    Checking VMs TOD (availability)...SUCCESS
    Checking Dataplane-V2...Success
    
    - Validation Category: User Cluster F5 BIG-IP
    Checking f5 (credentials, partition)...SUCCESS
    
    - Validation Category: User Cluster VCenter
    Checking Credentials...SUCCESS
    Checking DRS enabled...SUCCESS
    Checking Hosts for AntiAffinityGroups...SUCCESS
    Checking VSphere CSI Driver...SUCCESS
    Checking Version...SUCCESS
    Checking Datacenter...SUCCESS
    Checking Datastore...SUCCESS
    Checking Resource pool...SUCCESS
    Checking Folder...SUCCESS
    Checking Network...SUCCESS
    
    - Validation Category: User Cluster
    Checking user cluster and node pools...SUCCESS
    Checking cluster object...SUCCESS
    Checking machine deployment...SUCCESS
    Checking machineset...SUCCESS
    Checking machine objects...SUCCESS
    Checking control plane pods...SUCCESS
    Checking kube-system pods...SUCCESS
    Checking gke-system pods...SUCCESS
    Checking gke-connect pods...SUCCESS
    Checeking anthos-identity-service pods...SUCCESS
    Checking storage...SUCCESS
    Checking resource...SUCCESS
    Checking virtual machine resource contention...SUCCESS
    Checking host resource contention...SUCCESS
    All validation results were SUCCESS.
    Cluster is healthy!
    

### Troubleshooting diagnosed cluster issues

If you have the following issues when running the `gkectl diagnose cluster`, here are some possible resolutions.

Issue| Possible causes| Resolution  
---|---|---  
Kubernetes API server is not reachable, either for the admin cluster, or for user clusters. | Check the virtual machine health OOB (out-of-box) memory latency graphs, which ideally should have a memory latency around zero. Memory contention can also increase CPU contention, and the CPU readiness graphs might have a spike as there will be swapping involved.  | Increase physical memory. For other options, see [VMware troubleshooting suggestions](https://kb.vmware.com/s/article/2001003).  
Nodepool creation times out. | VMDK high read/write latency. Check VM health OOB for virtual disk read and write latency. According to VMware, a total latency greater than 20ms indicates a problem. | See [VMware solutions for disk performance problems](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.monitoring.doc/GUID-E813116C-9D72-4464-BF3E-1B19F70F45BE.html)..   
  
## Capturing cluster state

If `gkectl diagnose cluster` finds errors, you should capture the cluster's state and provide the information to Google. You can do so using the `gkectl diagnose snapshot` command.

`gkectl diagnose snapshot` has an optional flag, `--config`. In addition to collecting information about the cluster, this flag collects the Google Distributed Cloud configuration file that was used to create or upgrade the cluster.

**Note:** The `--kubeconfig` flag should always point to the admin cluster's kubeconfig file. `gkectl diagnose` returns an error if you provide the user cluster's kubeconfig.

### Capturing admin cluster state

To capture an admin cluster's state, run the following command, where `--config` is optional:
    
    
    gkectl diagnose snapshot --kubeconfig=[ADMIN_CLUSTER_KUBECONFIG] --config
    

**Note:** When there is a VIP issue with the target cluster, use `--config` to provide the admin cluster configuration file. That gives you more debugging information.

The output includes a list of files and the name of a tarball file:
    
    
    Taking snapshot of admin cluster "[ADMIN_CLUSTER_NAME]"...
       Using default snapshot configuration...
       Setting up "[ADMIN_CLUSTER_NAME]" ssh key file...DONE
       Taking snapshots...
           commands/kubectl_get_pods_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_kube-system
           commands/kubectl_get_deployments_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_kube-system
           commands/kubectl_get_daemonsets_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_kube-system
           ...
           nodes/[ADMIN_CLUSTER_NODE]/commands/journalctl_-u_kubelet
           nodes/[ADMIN_CLUSTER_NODE]/files/var/log/startup.log
           ...
       Snapshot succeeded. Output saved in [TARBALL_FILE_NAME].tar.gz.

To extract the tarball file to a directory, run the following command: 
    
    
    tar -zxf TARBALL_FILE_NAME --directory EXTRACTION_DIRECTORY_NAME
    

To look at the list of files produced by the snapshot, run the following commands:
    
    
    cd EXTRACTION_DIRECTORY_NAME/EXTRACTED_SNAPSHOT_DIRECTORY
    ls kubectlCommands
    ls nodes/NODE_NAME/commands
    ls nodes/NODE_NAME/files
    

To see the details of a particular operation, open one of the files.

#### Specifying the SSH key for the admin cluster

When you get a snapshot of the admin cluster, `gkectl` finds the private SSH key for the admin cluster automatically. You can also specify the key explicitly by using the `--admin-ssh-key-path` parameter.

Follow the instructions for [Using SSH to connect to a cluster node](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ssh-cluster-node) to download the SSH keys.

Then in your `gkectl diagnose snapshot` command, set `--admin-ssh-key-path` to your decoded key file path:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --admin-ssh-key-path=PATH_TO_DECODED_KEY
    

### Capturing user cluster state

To capture a user cluster's state, run the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME
    

The output includes a list of files and the name of a tarball file:
    
    
    Taking snapshot of user cluster "[USER_CLUSTER_NAME]"...
    Using default snapshot configuration...
    Setting up "[USER_CLUSTER_NAME]" ssh key file...DONE
        commands/kubectl_get_pods_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_user
        commands/kubectl_get_deployments_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_user
        commands/kubectl_get_daemonsets_-o_yaml_--kubeconfig_...env.default.kubeconfig_--namespace_user
        ...
        commands/kubectl_get_pods_-o_yaml_--kubeconfig_.tmp.user-kubeconfig-851213064_--namespace_kube-system
        commands/kubectl_get_deployments_-o_yaml_--kubeconfig_.tmp.user-kubeconfig-851213064_--namespace_kube-system
        commands/kubectl_get_daemonsets_-o_yaml_--kubeconfig_.tmp.user-kubeconfig-851213064_--namespace_kube-system
        ...
        nodes/[USER_CLUSTER_NODE]/commands/journalctl_-u_kubelet
        nodes/[USER_CLUSTER_NODE]/files/var/log/startup.log
        ...
    Snapshot succeeded. Output saved in [FILENAME].tar.gz.
    

### Snapshot scenarios

**Warning:** The snapshot scenarios have changed. In versions earlier than 1.13, there were four scenarios: `system`, `system-with-logs`, `all`, and `all-with-logs`. Now there are only two scenarios: `system`, and `all`. The new `system` scenario is the same as the old `system-with-logs` scenario. The new `all` scenario is the same as the old `all-with-logs` scenario.

The `gkectl diagnose snapshot` command supports two scenarios for the user cluster. To specify a scenario, use the `--scenario` flag. The following list shows the possible values:

  * System(default): Collect snapshot with logs in supported system namespaces.

  * All: Collect snapshot with logs in all of namespaces, including user defined namespaces




The following examples show some of the possibilities.

To create a snapshot of the admin cluster, you do not need to specify a scenario:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG
    

To create a snapshot of a user cluster using the `system` scenario:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=system
    

To create a snapshot of a user cluster using the `all` scenario:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=all
    

### Using `--log-since` to limit a snapshot

You can use the `--log-since` flag to limit log collection to a recent time period. For example, you could collect only the logs from the last two days or the last three hours. By default, `diagnose snapshot` collects all logs.

To limit the time period for log collection:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=CLUSTER_NAME \
        --scenario=system \
        --log-since=DURATION
    

Replace DURATION with a time value like `120m` or `48h`.

Notes:

  * The `--log-since` flag is supported only for `kubectl` and `journalctl` logs.
  * Command flags like `--log-since` are not allowed in the customized snapshot configuration.



### Performing a dry run for a snapshot

You can use the `--dry-run` flag to show the actions to be taken and the snapshot configuration.

To perform a dry run on your admin cluster, enter the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=ADMIN_CLUSTER_NAME \
        --dry-run
    

To perform a dry run on a user cluster, enter the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --dry-run
    

### Using a snapshot configuration

If these two scenarios (`--scenario system` or `all`) don't meet your needs, you can create a customized snapshot by passing in a snapshot configuration file using the `--snapshot-config` flag:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --snapshot-config=SNAPSHOT_CONFIG_FILE
    

**Note:** The meaning of the snapshot scenarios has been changed since 1.13. Now there is no `system-with-logs` nor `all-with-logs` scenario options. Since 1.13+ `system` and `all` scenarios options capture the logs.

#### Generating a snapshot configuration

You can generate a snapshot configuration for a given scenario by passing in the `--scenario` and `--dry-run` flags. For example, to see the snapshot configuration for the default scenario (`system`) of a user cluster, enter the following command:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=system
        --dry-run
    

The output is similar to the following:
    
    
    numOfParallelThreads: 10
    excludeWords:
    - password
    kubectlCommands:
    - commands:
      - kubectl get clusters -o wide
      - kubectl get machines -o wide
      - kubectl get clusters -o yaml
      - kubectl get machines -o yaml
      - kubectl describe clusters
      - kubectl describe machines
      namespaces:
      - default
    - commands:
      - kubectl version
      - kubectl cluster-info
      - kubectl get nodes -o wide
      - kubectl get nodes -o yaml
      - kubectl describe nodes
      namespaces: []
    - commands:
      - kubectl get pods -o wide
      - kubectl get deployments -o wide
      - kubectl get daemonsets -o wide
      - kubectl get statefulsets -o wide
      - kubectl get replicasets -o wide
      - kubectl get services -o wide
      - kubectl get jobs -o wide
      - kubectl get cronjobs -o wide
      - kubectl get endpoints -o wide
      - kubectl get configmaps -o wide
      - kubectl get pods -o yaml
      - kubectl get deployments -o yaml
      - kubectl get daemonsets -o yaml
      - kubectl get statefulsets -o yaml
      - kubectl get replicasets -o yaml
      - kubectl get services -o yaml
      - kubectl get jobs -o yaml
      - kubectl get cronjobs -o yaml
      - kubectl get endpoints -o yaml
      - kubectl get configmaps -o yaml
      - kubectl describe pods
      - kubectl describe deployments
      - kubectl describe daemonsets
      - kubectl describe statefulsets
      - kubectl describe replicasets
      - kubectl describe services
      - kubectl describe jobs
      - kubectl describe cronjobs
      - kubectl describe endpoints
      - kubectl describe configmaps
      namespaces:
      - kube-system
      - gke-system
      - gke-connect.*
    prometheusRequests: []
    nodeCommands:
    - nodes: []
      commands:
      - uptime
      - df --all --inodes
      - ip addr
      - sudo iptables-save --counters
      - mount
      - ip route list table all
      - top -bn1
      - sudo docker ps -a
      - ps -edF
      - ps -eo pid,tid,ppid,class,rtprio,ni,pri,psr,pcpu,stat,wchan:14,comm,args,cgroup
      - sudo conntrack --count
    nodeFiles:
    - nodes: []
      files:
      - /proc/sys/fs/file-nr
      - /proc/sys/net/nf_conntrack_max
    seesawCommands: []
    seesawFiles: []
    nodeCollectors:
    - nodes: []
    f5:
      enabled: true
    vCenter:
      enabled: true
    

  * `numOfParallelThreads`: Number of parallel threads used to take snapshots.

  * `excludeWords`: List of words to be excluded from the snapshot (case insensitive). Lines containing these words are removed from snapshot results. "password" is always excluded, whether or not you specify it.

  * `kubectlCommands`: List of kubectl commands to run. The results are saved. The commands run against the corresponding namespaces. For `kubectl logs` commands, all Pods and containers in the corresponding namespaces are added automatically. Regular expressions are supported for specifying namespaces. If you do not specify a namespace, the `default` namespace is assumed.

  * `nodeCommands`: List of commands to run on the corresponding nodes. The results are saved. When nodes are not specified, all nodes in the target cluster are considered.

  * `nodeFiles`: List of files to be collected from the corresponding nodes. The files are saved. When nodes are not specified, all nodes in the target cluster are considered.

  * `seesawCommands`: List of commands to run to collect Seesaw load balancer information. The results are saved if the cluster is using the Seesaw load balancer.

  * `seesawFiles`: List of files to be collected for the Seesaw load balancer.

  * `nodeCollectors`: A collector running for Cilium nodes to collect eBPF information.

  * `f5`: A flag to enable the collecting of information related to the F5 BIG-IP load balancer.

  * `vCenter`: A flag to enable the collecting of information related to vCenter.

  * `prometheusRequests`: List of Prometheus requests. The results are saved.




## Upload snapshots to a Cloud Storage bucket

To make record-keeping, analysis, and storage easier, you can upload all of the snapshots of a specific cluster to a Cloud Storage bucket. This is particularly helpful if you need assistance from Cloud Customer Care.

Before you run that command, make sure you have fulfilled these setup requirements.

  * Enable `storage.googleapis.com` in the [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#fleet_host_project). Although you can use a different project, the fleet host project is recommended.
        
        gcloud services enable --project=FLEET_HOST_PROJECT_ID storage.googleapis.com
        

  * Grant the `roles/storage.admin` to the service account on its parent project, and pass in the service account JSON key file using the `--service-account-key-file` parameter. You can use any service account, but the [connect register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#connect_register_service_account) is recommended. See [Service accounts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts) for more information.

**Note:** If you use the `--share-with` flag in the `gkectl diagnose snapshot` command, this setup requirement is unneeded. If you want to share access to your snapshot with Google Support manually, use the following command and don't use the `--share-with` flag when you create the snapshot.
        
        gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
          --member "serviceAccount:CONNECT_REGISTER_SERVICE_ACCOUNT" \
          --role "roles/storage.admin"
        

Replace CONNECT_REGISTER_SERVICE_ACCOUNT with the connect register service account.




With these requirements fulfilled, you can now upload the snapshot with this command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name CLUSTER_NAME \
        --upload \
        --share-with GOOGLE_SUPPORT_SERVICE_ACCOUNT
    

The `--share-with` flag can accept a list of service account names. Replace GOOGLE_SUPPORT_SERVICE_ACCOUNT with the Google support service account provided by Google support, along with any other service accounts provided by Google support. When you use the `--upload` flag, the command searches your project for a storage bucket that has a name that starts with "`anthos-snapshot-`" If such a bucket exits, the command uploads the snapshot to that bucket. If the command doesn't find a bucket with a matching name, it creates a new bucket wth the name `anthos-snapshot-UUID`, where `UUID` is a 32-digit universally unique identifier.

When you use the `--share-with` flag, you don't need to manually [share access to the bucket with Google Cloud support](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access#share_access_with_support).

**Note:** You can use the `--upload-to` flag to provide a specific bucket name into which the snapshot will be uploaded. 

Example output:
    
    
    Using "system" snapshot configuration...
    Taking snapshot of user cluster CLUSTER_NAME...
    Setting up CLUSTER_NAME ssh key...DONE
    Using the gke-connect register service account key...
    Setting up Google Cloud Storage bucket for uploading the snapshot...DONE
    Taking snapshots in 10 thread(s)...
       ...
    Snapshot succeeded.
    Snapshots saved in "SNAPSHOT_FILE_PATH".
    Uploading snapshot to Google Cloud Storage......  DONE
    Uploaded the snapshot successfully to gs://anthos-snapshot-a4b17874-7979-4b6a-a76d-e49446290282/xSNAPSHOT_FILE_NAME.
    Shared successfully with service accounts:
    GOOGLE_SUPPORT_SERVICE_ACCOUNT
    

## Known issues

### `BundleUnexpectedDiff` error

The Kubernetes Cluster API resource managed by a Google Distributed Cloud bundle might be accidentally modified which can cause failure of system components, or cluster upgrade or update failure.

From Google Distributed Cloud version 1.13, the `onprem-user-cluster-controller` will periodically check the status of objects, and report any unexpected differences from the desired state through logs and events. These objects include the user cluster control plane and add-ons such as Services and DaemonSets.

Here is an example of an event:
    
    
     Type     Reason                 Age    From                              Message
     ----     ------                 ----   ----                              -------
     Warning  BundleUnexpectedDiff   13m    onpremusercluster/ci-bundle-diff  Detected unexpected difference of user control plane objects: [ConfigMap/istio], please check onprem-user-cluster-controller logs for more details.
    

Here is an example of logs generated by the `onprem-user-cluster-controller`:
    
    
    2022-08-06T02:54:42.701352295Z W0806 02:54:42.701252       1 update.go:206] Detected unexpected difference of user addon object(ConfigMap/istio), Diff:   map[string]string{
    2022-08-06T02:54:42.701376406Z -    "mesh": (
    2022-08-06T02:54:42.701381190Z -        """
    2022-08-06T02:54:42.701385438Z -        defaultConfig:
    2022-08-06T02:54:42.701389350Z -          discoveryAddress: istiod.gke-system.svc:15012
    ...
    2022-08-06T02:54:42.701449954Z -        """
    2022-08-06T02:54:42.701453099Z -    ),
    2022-08-06T02:54:42.701456286Z -    "meshNetworks": "networks: {}",
    2022-08-06T02:54:42.701459304Z +    "test-key":     "test-data",
    2022-08-06T02:54:42.701462434Z   }
    

The events and logs will not block cluster operation. Objects that have unexpected differences from their desired state will be overwritten in the next cluster upgrade.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
