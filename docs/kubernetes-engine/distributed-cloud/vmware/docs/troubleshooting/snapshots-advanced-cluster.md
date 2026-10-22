---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots-advanced-cluster/
title: Create diagnostic snapshots when advanced cluster is enabled \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:08.703729+00:00
---

# Create diagnostic snapshots when advanced cluster is enabled  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots-advanced-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create diagnostic snapshots when advanced cluster is enabled Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to use the `gkectl diagnose` command to create diagnostic snapshots for troubleshooting issues in your clusters created using Google Distributed Cloud (software only) for VMware when advanced cluster is enabled. Advanced cluster is enabled when `enableAdvancedClusters` is set to `true` in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) and the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field). If advanced cluster isn't enabled, see [Create diagnostic snapshots when advanced cluster isn't enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots).

## `gkectl diagnose snapshot`

This command compresses a cluster's status, configurations, and logs into a tar file. The default configuration of the gkectl diagnose snapshot command captures the following information about your cluster:

  * Kubernetes version.

  * Status of Kubernetes resources in the kube-system and gke-system namespaces: cluster, machine, nodes, Services, Endpoints, ConfigMaps, ReplicaSets, CronJobs, Pods, and the owners of those Pods, including Deployments, DaemonSets, and StatefulSets.

  * Status of the control plane.

  * Details about each node configuration including IP addresses, iptables rules, mount points, file system, network connections, and running processes.

  * Container logs from the admin cluster's control-plane node, when Kubernetes API server is not available.

  * Logs from the `gkectl diagnose snapshot` command.

  * Logs of preflight jobs.

  * Logs of containers in namespaces based on the scenarios.




Credentials, including for vSphere and F5, are removed before the tar file is created.

## Capture admin cluster state

To capture an admin cluster's state, run the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path to the admin cluster kubeconfig file.

The output includes a list of files and the name of a tar file, as shown in the following example output:
    
    
    Using "system" snapshot configuration...
    Creating ssh signer for "[ADMIN_CLUSTER_NAME]"...
    Taking snapshots in 10 thread(s)...
        gkectlLogs/gkectl-xxx.log
    ...
        kubectlCommands/[NAMESPACE]/kubectl_get_pods
        kubectlCommands/[NAMESPACE]/kubectl_get_deployments
        kubectlCommands/[NAMESPACE]/kubectl_get_daemonsets
    ...
        nodes/[ADMIN_CLUSTER_NODE]/commands/journalctl_-u_kubelet
        nodes/[ADMIN_CLUSTER_NODE]/files/var/log/startup.log
    ...
    Snapshot succeeded. Output saved in [FILENAME].tar.gz.
    

To extract the tar file to a directory, run the following command:
    
    
    tar -zxf TAR_FILE_NAME --directory EXTRACTION_DIRECTORY_NAME
    

Replace the following:

  * `TAR_FILE_NAME`: the name of the tar file.

  * `EXTRACTION_DIRECTORY_NAME`: the directory into which you want to extract the tar file archive.




To look at the list of files produced by the snapshot, run the following commands:
    
    
    cd EXTRACTION_DIRECTORY_NAME/EXTRACTED_SNAPSHOT_DIRECTORY
    ls kubectlCommands
    ls nodes/NODE_NAME/commands
    ls nodes/NODE_NAME/files
    

Replace `NODE_NAME` with the name of the node that you want to view the files for.

To see the details of a particular operation, open one of the files.

### Specify the SSH key for the admin cluster

When you get a snapshot of the admin cluster, `gkectl` finds the private SSH key for the admin cluster automatically. You can also specify the key explicitly by using the `--admin-ssh-key-path` parameter.

Follow the instructions for [Using SSH to connect to a cluster node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node) to download the SSH keys.

In your `gkectl diagnose snapshot` command, set `--admin-ssh-key-path` to your decoded key path:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --admin-ssh-key-path=PATH_TO_DECODED_KEY
    

## Capture user cluster state

To capture a user cluster's state, run the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME
    

The following example output includes a list of files and the name of a tar file:
    
    
    Using "system" snapshot configuration...
    Creating ssh signer for "[USER_CLUSTER_NAME]"...
    Taking snapshots in 10 thread(s)...
        gkectlLogs/gkectl-xxx.log
    ...
        kubectlCommands/[NAMESPACE]/kubectl_get_pods
        kubectlCommands/[NAMESPACE]/kubectl_get_deployments
        kubectlCommands/[NAMESPACE]/kubectl_get_daemonsets
    ...
        nodes/[USER_CLUSTER_NODE_IP_ADDRESS]/commands/journalctl_-u_kubelet
        nodes/[USER_CLUSTER_NODE_IP_ADDRESS]/files/var/log/startup.logn
    ...
    Snapshot succeeded. Output saved in [FILENAME].tar.gz.
    

## Snapshot scenarios

Snapshot scenarios let you control the information that is included in a snapshot. To specify a scenario, use the `--scenario` flag. The following list shows the possible values:

  * `system` (default): Collect snapshot with logs in supported system namespaces.

  * `all`: Collect snapshot with logs in all of namespaces, including user defined namespaces.




To create a snapshot of the admin cluster, you don't need to specify a scenario:
    
    
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
    

## Use `--log-since` to limit a snapshot

You can use the `--log-since` flag to limit log collection to a recent time period. For example, you could collect only the logs from the last two days or the last three hours. By default, `diagnose snapshot` collects all logs.
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=CLUSTER_NAME \
        --scenario=system \
        --log-since=DURATION
    

Replace `<var>DURATION</var>` with a time value like `120m` or `48h`.

The following considerations apply:

  * The `--log-since` flag is supported only for `kubectl` and `journalctl` logs.
  * Command flags like `--log-since` are not allowed in the customized snapshot configuration.



## Perform a dry run for a snapshot

You can use the `--dry-run` flag to show the actions to be taken and the snapshot configuration.

To perform a dry run on your admin cluster, enter the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=ADMIN_CLUSTER_NAME \
        --dry-run
    

To perform a dry run on a user cluster, enter the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --dry-run
    

## Use a snapshot configuration

If these two scenarios (`--scenario system` or `all`) don't meet your needs, you can create a customized snapshot by passing in a snapshot configuration file using the `--snapshot-config` flag:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --snapshot-config=SNAPSHOT_CONFIG_FILE
    

### Generate a snapshot configuration

You can generate a snapshot configuration for a given scenario by passing in the `--scenario` and `--dry-run` flags. For example, to see the snapshot configuration for the default scenario (`system`) of a user cluster, enter the following command:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=system
        --dry-run
    

The output is similar to the following example:
    
    
    The snapshot configuration is:
    numOfParallelThreads: 10
    excludeWords:
    - password
    kubectlCommands:
    - commands:
      - kubectl version
      - kubectl cluster-info
      - kubectl top node
      - kubectl top pod -A --containers
      namespaces: []
    - commands:
      - kubectl get -o wide --ignore-not-found
      - kubectl get -o yaml --ignore-not-found
      - kubectl describe
      namespaces:
      - kube-system
    ...
      expandResources: true
    - commands:
      - kubectl logs
      namespaces:
      - kube-system
    ...
    kindNodeCommands: []
    nodeCommands:
    - nodes: []
      commands:
      - uptime
      - df --all --inodes
      - ip addr
      - ip neigh
      - iptables-save --counters
      - mount
      - ip route list table all
      - top -bn1 || true
      - docker info || true
    ...
    - nodes: []
      commands:
      - dmesg
      - systemctl status -l kubelet
      - journalctl --utc -u kubelet
      - journalctl --utc -u kubelet-monitor.service
    ...
    nodeFiles:
    - nodes: []
      files:
      - /proc/sys/fs/file-nr
      - /proc/sys/net/netfilter/nf_conntrack_max
    ...
    - nodes: []
      files:
      - /var/log/apiserver/audit-proxy-buffer/* || true
    

The following information is displayed in the output:

  * `numOfParallelThreads`: Number of parallel threads used to take snapshots.

  * `excludeWords`: List of words to be excluded from the snapshot (case insensitive). Lines containing these words are removed from snapshot results. "password" is always excluded, whether or not you specify it.

  * `kubectlCommands`: List of kubectl commands to run. The results are saved. The commands run against the corresponding namespaces. For `kubectl logs` commands, all Pods and containers in the corresponding namespaces are added automatically. Regular expressions are supported for specifying namespaces. If you don't specify a namespace, the `default` namespace is assumed.

  * `nodeCommands`: List of commands to run on the corresponding nodes. The results are saved. When nodes are not specified, all nodes in the target cluster are considered.

  * `nodeFiles`: List of files to be collected from the corresponding nodes. The files are saved. When nodes are not specified, all nodes in the target cluster are considered.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
