---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots/
title: Create diagnostic snapshots when advanced cluster isn't enabled \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:59.661104+00:00
---

# Create diagnostic snapshots when advanced cluster isn't enabled  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create diagnostic snapshots when advanced cluster isn't enabled Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to use the `gkectl diagnose` command to create diagnostic snapshots for troubleshooting issues in your clusters created using Google Distributed Cloud (software only) for VMware when advanced cluster isn't enabled. Advanced cluster isn't enabled when `enableAdvancedClusters` is set to `false` in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) and the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field). If advanced cluster is enabled, see [Create snapshots when advanced cluster is enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots-advanced-cluster).

The `gkectl` tool has two commands for troubleshooting issues with clusters: `gkectl diagnose snapshot` and `gkectl diagnose cluster`. The commands work with both admin and user clusters.

For more information how to use the `gkectl diagnose cluster` command to diagnose cluster issues, see [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose).

## `gkectl diagnose snapshot`

This command compresses a cluster's status, configurations, and logs into a tar file. When you run `gkectl diagnose snapshot`, the command automatically runs `gkectl diagnose cluster` as part of the process, and output files are placed in a new folder in the snapshot called `/diagnose-report`.

### Default snapshot

The default configuration of the `gkectl diagnose snapshot` command captures the following information about your cluster:

  * Kubernetes version.

  * Status of Kubernetes resources in the kube-system and gke-system namespaces: cluster, machine, nodes, Services, Endpoints, ConfigMaps, ReplicaSets, CronJobs, Pods, and the owners of those Pods, including Deployments, DaemonSets, and StatefulSets.

  * Status of the control plane.

  * Details about each node configuration including IP addresses, iptables rules, mount points, file system, network connections, and running processes.

  * Container logs from the admin cluster's control-plane node, when Kubernetes API server is not available.

  * vSphere information including VM objects and their Events based on Resource Pool. Also collects information on the Datacenter, Cluster, Network, and Datastore objects associated with VMs.

  * F5 BIG-IP load balancer information including virtual server, virtual address, pool, node, and monitor.

  * Logs from the `gkectl diagnose snapshot` command.

  * Logs of preflight jobs.

  * Logs of containers in namespaces based on the scenarios.

  * Information about admin cluster Kubernetes certificate expiration in the snapshot file `/nodes/<admin_master_node_name>/sudo_kubeadm_certs_check-expiration`.

  * An HTML index file for all of the files in the snapshot.

  * Optionally, the admin cluster configuration file used to install and upgrade the cluster with the `--config` flag.




Credentials, including for vSphere and F5, are removed before the tar file is created.

### Lightweight snapshot

In Google Distributed Cloud version 1.29 and higher, a lightweight version of `gkectl diagnose snapshot` is available for both admin and user clusters. The lightweight snapshot speeds up the snapshot process because it captures less information about the cluster. When you add `--scenario=lite` to the command, only the following information is included in the snapshot:

  * Status of Kubernetes resources in the kube-system and gke-system namespaces: cluster, machine, nodes, Services, Endpoints, ConfigMaps, ReplicaSets, CronJobs, Pods, and the owners of those Pods, including Deployments, DaemonSets, and StatefulSets

  * Logs from the `gkectl diagnose snapshot` command




## Capture cluster state

If the `gkectl diagnose cluster` commands finds errors, you should capture the cluster's state and provide the information to Cloud Customer Care. You can capture this information using the `gkectl diagnose snapshot` command.

`gkectl diagnose snapshot` has an optional flag for `--config`. In addition to collecting information about the cluster, this flag collects the configuration file that was used to create or upgrade the cluster.

**Note:** The `--kubeconfig` flag should always point to the admin cluster's kubeconfig file. `gkectl diagnose` returns an error if you provide the user cluster's kubeconfig.

## Capture admin cluster state

To capture an admin cluster's state, run the following command:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG --config
    

The `--config` parameter is optional:

If there's an issue with a virtual IP address (VIP) in the target cluster, use the `--config` flag to provide the admin cluster configuration file to provide more debugging information.

In version 1.29 and higher, you can include `--scenario=lite` if you don't need all the information in the default snapshot.

The output includes a list of files and the name of a tar file, as shown in the following example output:
    
    
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
       Snapshot succeeded. Output saved in [TAR_FILE_NAME].tar.gz.
    

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
    

## Snapshot scenarios

Snapshot scenarios let you control the information that is included in a snapshot. To specify a scenario, use the `--scenario` flag. The following list shows the possible values:

  * `system` (default): Collect snapshot with logs in supported system namespaces.

  * `all`: Collect snapshot with logs in all of namespaces, including user defined namespaces.

  * `lite` (1.29 and higher): Collect snapshot with only Kubernetes resources and `gkectl` logs. All other logs, such as container logs and node kernel logs are excluded.




The available snapshot scenarios vary depending on the Google Distributed Cloud version.

  * Versions lower than 1.13: `system`, `system-with-logs`, `all`, and `all-with-logs`.

  * Versions 1.13 - 1.28: `system` and `all`. The `system` scenario is the same as the old `system-with-logs` scenario. The `all` scenario is the same as the old `all-with-logs` scenario.

  * Versions 1.29 and higher: `system`, `all`, and `lite`.




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
    

To create a snapshot of a user cluster using the `lite` scenario:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=lite
    

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
    

**Note:** The meaning of the snapshot scenarios has been changed since version 1.13. There is no longer `system-with-logs` nor `all-with-logs` scenario options. In version 1.13 and later, `system` and `all` scenarios options capture the logs.

### Generate a snapshot configuration

You can generate a snapshot configuration for a given scenario by passing in the `--scenario` and `--dry-run` flags. For example, to see the snapshot configuration for the default scenario (`system`) of a user cluster, enter the following command:
    
    
    gkectl diagnose snapshot \
        --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME \
        --scenario=system
        --dry-run
    

The output is similar to the following example:
    
    
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
    

The following information is displayed in the output:

  * `numOfParallelThreads`: Number of parallel threads used to take snapshots.

  * `excludeWords`: List of words to be excluded from the snapshot (case insensitive). Lines containing these words are removed from snapshot results. "password" is always excluded, whether or not you specify it.

  * `kubectlCommands`: List of kubectl commands to run. The results are saved. The commands run against the corresponding namespaces. For `kubectl logs` commands, all Pods and containers in the corresponding namespaces are added automatically. Regular expressions are supported for specifying namespaces. If you don't specify a namespace, the `default` namespace is assumed.

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

Before you upload snapshots to a Cloud Storage bucket, review and complete the following initial requirements:

  * Enable `storage.googleapis.com` in the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). Although you can use a different project, the fleet host project is recommended.
        
        gcloud services enable --project=FLEET_HOST_PROJECT_ID storage.googleapis.com
        

  * Grant the `roles/storage.admin` to the service account on its parent project, and pass in the service account JSON key file using the `--service-account-key-file` parameter. You can use any service account, but the [connect register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account) is recommended. See [Service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts) for more information.

**Note:** If you use the `--share-with` flag in the `gkectl diagnose snapshot` command, this setup requirement is unneeded. If you want to share access to your snapshot with Cloud Customer Care manually, use the following command and don't use the `--share-with` flag when you create the snapshot.
        
        gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
          --member "serviceAccount:CONNECT_REGISTER_SERVICE_ACCOUNT" \
          --role "roles/storage.admin"
        

Replace `CONNECT_REGISTER_SERVICE_ACCOUNT` with the connect register service account.




With these requirements fulfilled, you can now upload the snapshot to the Cloud Storage bucket:
    
    
    gkectl diagnose snapshot --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name CLUSTER_NAME \
        --upload \
        --share-with GOOGLE_SUPPORT_SERVICE_ACCOUNT
    

The `--share-with` flag can accept a list of service account names. Replace `GOOGLE_SUPPORT_SERVICE_ACCOUNT` with the Cloud Customer Care service account provided by Cloud Customer Care, along with any other service accounts provided by Cloud Customer Care.

When you use the `--upload` flag, the command searches your project for a storage bucket that has a name that starts with "`anthos-snapshot-`" If such a bucket exists, the command uploads the snapshot to that bucket. If the command doesn't find a bucket with a matching name, it creates a new bucket with the name `anthos-snapshot-UUID`, where `UUID` is a 32-digit universally unique identifier.

When you use the `--share-with` flag, you don't need to manually [share access to the bucket with Cloud Customer Care](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access#share_access_with_support).

**Note:** You can use the `--upload-to` flag to provide a specific bucket name into which the snapshot will be uploaded.

The following example output is displayed when you upload a snapshot to a Cloud Storage bucket:
    
    
    Using "system" snapshot configuration...
    Taking snapshot of user cluster <var>CLUSTER_NAME</var>...
    Setting up <var>CLUSTER_NAME</var> ssh key...DONE
    Using the gke-connect register service account key...
    Setting up Google Cloud Storage bucket for uploading the snapshot...DONE
    Taking snapshots in 10 thread(s)...
       ...
    Snapshot succeeded.
    Snapshots saved in "<var>SNAPSHOT_FILE_PATH</var>".
    Uploading snapshot to Google Cloud Storage......  DONE
    Uploaded the snapshot successfully to gs://anthos-snapshot-a4b17874-7979-4b6a-a76d-e49446290282/<var>xSNAPSHOT_FILE_NAME</var>.
    Shared successfully with service accounts:
    <var>GOOGLE_SUPPORT_SERVICE_ACCOUNT</var>
    

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
