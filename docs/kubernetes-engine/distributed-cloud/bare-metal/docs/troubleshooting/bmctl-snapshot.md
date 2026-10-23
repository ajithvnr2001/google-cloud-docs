---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/bmctl-snapshot/
title: Create snapshots to help diagnose cluster problems \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:28.717992+00:00
---

# Create snapshots to help diagnose cluster problems  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/bmctl-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create snapshots to help diagnose cluster problems Stay organized with collections  Save and categorize content based on your preferences. 

When you experience a problem with one of your clusters, you can get help from [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support). Customer Care might ask you to take a 'snapshot' of the cluster, which they can use to diagnose the problem. A snapshot captures cluster and node configuration files, and packages that information into a single tar file.

This document describes how to create default snapshots or more customized snapshots of a cluster. It also explains how to create snapshots when a cluster is experiencing particular errors.

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



## Default snapshots

The following sections describe what's in a standard snapshot and how to create one. For information about customized snapshots, see the section on customized snapshots.

### What information does a default snapshot contain?

The snapshot of a cluster is a tar file of configuration files and logs about the cluster. Specifically, the default configuration of the command captures the following information about your cluster:

  * Kubernetes version.

  * Status of Kubernetes resources in the kube-system and gke-system namespaces: cluster, machine, nodes, Services, Endpoints, ConfigMaps, ReplicaSets, CronJobs, Pods, and the owners of those Pods, including Deployments, DaemonSets, and StatefulSets.

  * Details about each node configuration including IP addresses, iptables rules, mount points, file system, network connections, and running processes.

  * Information about VM Runtime on GDC and any VMs and VM-related resources running in your cluster. For more information about what's collected by default and how to create VM-specific snapshots, see VM information in snapshots in this document.

  * Logs from the `bmctl check cluster --snapshot` command.




A cluster's credential information is not included in the default snapshot. If Cloud Customer Care requests that information, see [Retrieving cluster information](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/get-cluster-info).

For a comprehensive list of the information collected when you run the snapshot command, see a following section about the configuration file in detail. This configuration file shows which commands are run when taking a default snapshot.

### Create a default snapshot

The `bmctl check cluster` command takes a snapshot of a cluster. You can use this command to perform either of the following actions:

  * Create a snapshot and automatically upload that snapshot to a Cloud Storage bucket.
  * Create a snapshot of a cluster and save the snapshot file on the local machine on which you are running the command.



#### Method #1: create default snapshot and automatically upload to Cloud Storage bucket

To create and upload a snapshot to a Cloud Storage bucket, do the following:

  1. Set up API and service account as described in [Configure a service account that can access a Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#bucket-sa).

This is a one-time step.

  2. Run the following `bmctl` command to create and automatically upload a snapshot to a Cloud Storage bucket:
         
         bmctl check cluster --snapshot --cluster=CLUSTER_NAME \
             --admin-kubeconfig=ADMIN_KUBECONFIG \
             --service-account-key-file SA_KEY_FILE
         

Replace the following entries with information specific to your cluster environment:

     * `CLUSTER_NAME`: the name of the cluster you want to take a snapshot of.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.
     * `SA_KEY_FILE`: the path to the downloaded JSON key file for the service account created in the preceding step. If you don't use the `--service-account-key-file` flag, the command uses the credentials associated with the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Explicitly specifying the service account credentials with the flag takes precedence.

This command generates a snapshot tar file and saves it locally. When the [service account is set up properly](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#bucket-sa), the command also uploads the snapshot tar file to a bucket in Cloud Storage. The command searches your project for a storage bucket that has a name that starts with "`anthos-snapshot-`" If such a bucket exists, the command uploads the snapshot to that bucket. If the command doesn't find a bucket with a matching name, it creates a new bucket with the name `anthos-snapshot-UUID`, where `UUID` is a 32-digit universally unique identifier.

**Note:** You can use the `--upload-to` flag to provide a specific bucket name into which the snapshot is uploaded.
  3. Share access with Cloud Customer Care as described in [Allow Cloud Customer Care to view your uploaded cluster snapshot](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-access#allow_google_cloud_support_to_view_your_uploaded_cluster_snapshot).




#### Method #2: create default snapshot on local machine only

Use the `--local` flag to ensure that your cluster snapshot is saved locally only. You can capture the state of your created clusters with the following command:
    
    
    bmctl check cluster --snapshot --cluster=CLUSTER_NAME \
        --admin-kubeconfig=ADMIN_KUBECONFIG --local
    

Replace the following:

  * `CLUSTER_NAME`: the name of the target cluster.

  * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.




This command outputs a tar file to your local machine. The name of this tar file is in the form `snapshot-CLUSTER_NAME-TIMESTAMP.tar.gz`, where `TIMESTAMP` indicates the date and time the file was created. This tar file includes relevant debug information about a cluster's system components and machines.

When you execute this command, information is gathered about Pods from the following namespaces: `gke-system`, `gke-connect`, `capi-system`, `capi-webhook-system`, `cert-manager`, and `capi-kubeadm-bootstrap-system`

However, you can widen the scope of the diagnostic information collected by using the flag `--snapshot-scenario all`. This flag increases the scope of the diagnostic snapshot to include all the Pods in a cluster:
    
    
    bmctl check cluster --snapshot --snapshot-scenario all \
        --cluster=CLUSTER_NAME \
        --kubeconfig=KUBECONFIG_PATH \
        --local
    

### Snapshot scenarios

The `bmctl check cluster --snapshot` command supports two scenarios. To specify a scenario, use the `--scenario` flag. The following list shows the possible values:

  * `system`: Collect a snapshot of system components, including their logs.

  * `all`: Collect a snapshot of all pods, including their logs.




You can use each of the two scenarios with an admin cluster or a user cluster. The following example creates a snapshot of the admin cluster using the `system` scenario:
    
    
    bmctl check cluster --snapshot --snapshot-scenario system \
        --cluster=ADMIN_CLUSTER_NAME \
        --kubeconfig=ADMIN_KUBECONFIG_PATH
    

The following example creates a snapshot of a user cluster using the `all` scenario:
    
    
    bmctl check cluster --snapshot --snapshot-scenario all \
        --cluster=USER_CLUSTER_NAME \
        --kubeconfig=USER_KUBECONFIG_PATH
    

### Perform a dry run for a snapshot

When you use the `--snapshot-dry-run` flag, the command doesn't create a snapshot. Instead, it shows what actions the snapshot command would perform and it outputs a snapshot configuration file. For information about the snapshot configuration file, see How to create a customized snapshot.

To perform a dry run snapshot on your admin cluster, enter the following command:
    
    
    bmctl check cluster --snapshot --snapshot-dry-run \
        --cluster=ADMIN_CLUSTER_NAME \
        --kubeconfig=ADMIN_KUBECONFIG_PATH
    

To perform a dry run snapshot on a user cluster, enter the following command:
    
    
    bmctl check cluster --snapshot --snapshot-dry-run \
        --cluster=USER_CLUSTER_NAME \
        --kubeconfig=USER_KUBECONFIG_PATH
    

### Get logs from a particular period

You can use the `--since` flag to retrieve logs from a period of time that you are particularly interested in. In this way, you can create smaller, and more focused snapshots of logging that has happened in the last few seconds, minutes or hours.

For example, the following `bmctl` command creates a snapshot of logging that has happened in the last three hours:
    
    
    bmctl check cluster --snapshot --since=3h \
        --cluster=CLUSTER_NAME \
        --kubeconfig=ADMIN_KUBECONFIG_PATH
    

### Specify a directory in which the snapshot is saved temporarily

You can use the `--snapshot-temp-output-dir` flag to specify a directory in which the snapshot is saved temporarily:
    
    
    bmctl check cluster --snapshot --snapshot-temp-output-dir=TEMP_OUTPUT_DIR \
        --cluster=CLUSTER_NAME \
        --kubeconfig=ADMIN_KUBECONFIG_PATH
    

If you don't specify a directory, the snapshot is saved in the `/tmp` directory temporarily. Using the `--snapshot-temp-output-dir` option is a good idea when space is limited in the default `/tmp` directory, for example.

### Suppress console logging

You can use the `--quiet` flag to suppress log messages from appearing in the console during a snapshot run. Instead, the console logs are saved in the 'bmctl_diagnose_snapshot.log' file as part of the snapshot.

Run the following command to suppress log messages from appearing in the console:
    
    
    bmctl check cluster --snapshot --quiet \
        --cluster=CLUSTER_NAME \
        --kubeconfig=ADMIN_KUBECONFIG_PATH
    

### Adjust parallel threading on the command line

The snapshot routine typically runs numerous commands. Multiple parallel threads let you run commands simultaneously, which helps the routine execute faster.

In release 1.31 and later, the `bmctl check cluster` command supports a `--num-of-parallel-threads` flag. You use this flag to set the number of parallel threads used to take snapshots.

By default, the snapshot routine uses 10 threads. If your snapshots take too long, increase this value.

The following example command sets the number of parallel threads to `30`.
    
    
    bmctl check cluster --snapshot --cluster=cluster1 \
        --admin-kubeconfig=bmctl-workspace/admin-cluster/admin-cluster-kubeconfig \**    --num-of-parallel-threads=30**
    

This capability is similar to the `numOfParallelThreads` field in the snapshot configuration file, when you create customized snapshots.

## Customized snapshots

You might want to create a customized snapshot of a cluster for the following reasons:

  * To include more information about your cluster than what's provided in the default snapshot.
  * To exclude some information that's in the default snapshot.



### Create a customized snapshot

Creating a customized snapshot requires the use of a snapshot configuration file. The following steps explain how to create the configuration file, modify it, and use it to create a customized snapshot of a cluster:

  1. Create a snapshot configuration file by running the following command on your cluster and writing the output to a file:
         
         bmctl check cluster \
             --snapshot --snapshot-dry-run --cluster CLUSTER_NAME \
             --kubeconfig KUBECONFIG_PATH
         

  2. Define what kind of information you want to appear in your customized snapshot. To do that, modify the snapshot configuration file that you created in step 1. For example, if you want the snapshot to contain additional information, such as how long a particular node has been running, add the Linux command `uptime` to the relevant section of the configuration file.

The following snippet of a configuration file shows how to make the snapshot command provide `uptime` information about node `10.200.0.3`. This information doesn't appear in a standard snapshot.
         
         ...
         nodeCommands:
         - nodes:
           - 10.200.0.3
           commands:
           - uptime
         ...
         

  3. After you have modified the configuration file to define what kind of snapshot you want, create the customized snapshot by running the following command:
         
         bmctl check cluster --snapshot --snapshot-config SNAPSHOT_CONFIG_FILE \
             --cluster CLUSTER_NAME--kubeconfig KUBECONFIG_PATH
         

The `--snapshot-config` flag directs the `bmctl` command to use the contents of the snapshot configuration file to define what information appears in the snapshot.




### The configuration file in detail

The following sample snapshot configuration file shows the standard commands and files used for creating a snapshot, but you can add more commands and files when additional diagnostic information is needed:
    
    
    numOfParallelThreads: 10
    excludeWords:
    - password
    nodeCommands:
    - nodes:
      - 10.200.0.3
      - 10.200.0.4
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
      - docker ps -a || true
      - crictl ps -a || true
      - docker ps -a | grep anthos-baremetal-haproxy | cut -d ' ' -f1 | head -n 1 | xargs
        sudo docker logs || true
      - docker ps -a | grep anthos-baremetal-keepalived | cut -d ' ' -f1 | head -n 1 |
        xargs sudo docker logs || true
      - crictl ps -a | grep anthos-baremetal-haproxy | cut -d ' ' -f1 | head -n 1 | xargs
        sudo crictl logs || true
      - crictl ps -a | grep anthos-baremetal-keepalived | cut -d ' ' -f1 | head -n 1 |
        xargs sudo crictl logs || true
      - ps -edF
      - ps -eo pid,tid,ppid,class,rtprio,ni,pri,psr,pcpu,stat,wchan:14,comm,args,cgroup
      - conntrack --count
      - dmesg
      - systemctl status -l docker || true
      - journalctl --utc -u docker
      - journalctl --utc -u docker-monitor.service
      - systemctl status -l kubelet
      - journalctl --utc -u kubelet
      - journalctl --utc -u kubelet-monitor.service
      - journalctl --utc --boot --dmesg
      - journalctl --utc -u node-problem-detector
      - systemctl status -l containerd || true
      - journalctl --utc -u containerd
      - systemctl status -l docker.haproxy || true
      - journalctl --utc -u docker.haproxy
      - systemctl status -l docker.keepalived || true
      - journalctl --utc -u docker.keepalived
      - systemctl status -l container.haproxy || true
      - journalctl --utc -u container.haproxy
      - systemctl status -l container.keepalived || true
      - journalctl --utc -u container.keepalived
    nodeFiles:
    - nodes:
      - 10.200.0.3
      - 10.200.0.4
      files:
      - /proc/sys/fs/file-nr
      - /proc/sys/net/netfilter/nf_conntrack_max
      - /proc/sys/net/ipv4/conf/all/rp_filter
      - /lib/systemd/system/kubelet.service
      - /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
      - /lib/systemd/system/docker.service || true
      - /etc/systemd/system/containerd.service || true
      - /etc/docker/daemon.json || true
      - /etc/containerd/config.toml || true
      - /etc/systemd/system/container.keepalived.service || true
      - /etc/systemd/system/container.haproxy.service || true
      - /etc/systemd/system/docker.keepalived.service || true
      - /etc/systemd/system/docker.haproxy.service || true
    nodeSSHKey: ~/.ssh/id_rsa # path to your ssh key file
    

The following entries in your configuration file likely differ from the ones appearing in the previous sample configuration file:

  * The IP addresses of nodes in the `nodeCommands` and `nodeFiles` sections
  * The path to your cluster's `nodeSSHKey`



### Fields in the configuration file

A snapshot configuration file is in YAML format. The configuration file includes the following fields:

  * `numOfParallelThreads`: the snapshot routine typically runs numerous commands. Multiple parallel threads help the routine execute faster. We recommend that you set `numOfParallelThreads` to `10` as shown in the preceding sample configuration file. If your snapshots take too long, increase this value.

  * `excludeWords`: the snapshot contains a large quantity of data for your cluster nodes. Use `excludeWords` to reduce security risks when you share your snapshot. For example, exclude `password` so that corresponding password strings can't be identified.

  * `nodeCommands`: this section specifies the following information:

    * `nodes`: a list of IP addresses for the cluster nodes from which you want to collect information. To create a snapshot when the admin cluster is not reachable, specify at least one node IP address.

    * `commands`: a list of commands (and arguments) to run on each node. The output of each command is included in the snapshot.

  * `nodeFiles`: this section specifies the following information:

    * `nodes`: a list of IP addresses of cluster nodes from which you want to collect files. To create a snapshot when the admin cluster is not reachable, specify at least one node IP address.

    * `files`: a list of files to retrieve from each node. When the specified files are found on a node, they are included in the snapshot.

  * `nodeSSHKey`: path to your SSH key file. When the admin cluster is unreachable, this field is required.




## Create snapshots when you experience particular errors

Additional steps or command parameters might be needed to successfully create a snapshot when certain events occur, like a stalled upgrade.

### Create a default snapshot during stalled installs or upgrades

When installing or upgrading admin, hybrid, or standalone clusters, `bmctl` can sometimes stall at points in which the following outputs can be seen:

  * Waiting for cluster kubeconfig to become ready.
  * Waiting for cluster to become ready.
  * Waiting for node pools to become ready.
  * Waiting for upgrade to complete.



If you experience a stalled install or upgrade, you can take a snapshot of a cluster using the [bootstrap cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade), as shown in the following example:
    
    
    bmctl check cluster --snapshot --cluster=CLUSTER_NAME \
        --kubeconfig=WORKSPACE_DIR/.kindkubeconfig
    

### Create a customized snapshot during stalled installs or upgrades

The following steps show how to create a customized snapshot of a cluster when an install or upgrade is stalled:

  1. Retrieve a snapshot configuration file of the cluster from your archives.

  2. Modify the snapshot configuration file so that the snapshot contains the information you want.

  3. Create the customized snapshot by running the following command:
         
         bmctl check cluster --snapshot
             --snapshot-config=SNAPSHOT_CONFIG_FILE \
             --cluster=CLUSTER_NAME
             --kubeconfig=WORKSPACE_DIR/.kindkubeconfig
         




### Create a customized snapshot when the admin cluster is unreachable

When the admin cluster is unreachable, you can take a customized snapshot of the cluster by running the following command:
    
    
    bmctl check cluster --snapshot --cluster CLUSTER_NAME
        --node-ssh-key SSH_KEY_FILE
        --nodes NODE_1_IP_ADDRESS, NODE_2_IP_ADDRESS, ...
    

In the command, replace the following entries with information specific to your cluster environment:

  * `CLUSTER_NAME`: the name of the cluster you want to take a snapshot of.
  * `SSH_KEY_FILE`: the path to the node SSH key file.
  * `NODE_x_IP_ADDRESS`: the IP address of a cluster node you want information about.



Alternatively, you can list node IP addresses on separate lines:
    
    
    bmctl check cluster
        --snapshot --cluster CLUSTER_NAME \
        --node-ssh-key SSH_KEY_FILE \
        --nodes NODE_1_IP_ADDRESS \
        --nodes NODE_2_IP_ADDRESS
      ...
    

## VM information in snapshots

If you use VM Runtime on GDC to create and manage virtual machines (VMs) on Google Distributed Cloud, you can collect relevant diagnostic information in snapshots. Snapshots are a critical resource for diagnosing and troubleshooting issues with your VMs.

### What gets collected by default

When you create a default snapshot, it contains the information about VM Runtime on GDC and related resources. VM Runtime on GDC is bundled with Google Distributed Cloud and the `VMRuntime` custom resource is available on your clusters that run workloads. Even if you haven't [enabled VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable), the snapshot still contains the `VMRuntime` custom resource YAML description.

**Note:** Snapshots for admin clusters don't contain any information related to VM Runtime on GDC or your VMs.

If you've enabled VM Runtime on GDC, snapshots contain status and configuration information for the VM-related resources (when the objects are present) in your cluster. VM-related resources include Kubernetes objects, such as Pods, Deployments, DaemonSets, and ConfigMaps.

#### Objects in the `vm-system` namespace

Status and configuration information for the following objects is located in `kubectlCommands/vm-system` in the generated snapshot:

  * `KubeVirt`
  * `VirtualMachineType`
  * `VMHighAvailabilityPolicy`



#### Objects in other namespaces

When you create a VM (`VirtualMachine`), you can specify the namespace. If you don't specify a namespace, the VM gets the `default` namespace. The other objects in this section, such as `VirtualMachineInstance`, are all bound to the namespace for the corresponding VM.

Status and configuration information for the following objects is located in `kubectlCommands/VM_NAMESPACE` in the generated snapshot. If you didn't set a specific namespace for your VM, the information is located in `kubectlCommands/default`:

  * `VirtualMachine`
  * `VirtualMachineInstance`
  * `VirtualMachineDisk`
  * `GuestEnvironmentData`
  * `VirtualMachineAccessRequest`
  * `VirtualMachinePasswordResetRequest`



#### Objects that aren't namespaced

The following objects aren't namespaced, so their corresponding information is located directly in `kubectlCommands` in the generated snapshot:

  * `VMRuntime`
  * `DataVolume`
  * `CDI`
  * `GPUAllocation`



### Use a snapshot configuration file to capture VM details only

If you are diagnosing issues for VMs specifically, you can use a snapshot configuration file to both restrict the collected information to VM-related details only and tailor the VM information collected.

The following snapshot configuration file illustrates how you might construct a VM-specific snapshot. You can include additional commands to collect more information for your snapshot.
    
    
    ---
    kubectlCommands:
    - commands:
        - kubectl get vm -o wide
        - kubectl get vmi -o wide
        - kubectl get gvm -o wide
        - kubectl get vm -o yaml
        - kubectl get vmi -o yaml
        - kubectl get gvm -o yaml
        - kubectl describe vm
        - kubectl describe vmi
        - kubectl describe gvm
      namespaces:
        - .*
    - commands:
        - kubectl get virtualmachinetype -o wide
        - kubectl get virtualmachinedisk -o wide
        - kubectl get virtualmachinetype -o yaml
        - kubectl get virtualmachinedisk -o yaml
        - kubectl describe virtualmachinetype
        - kubectl describe virtualmachinedisk
      namespaces:
        - vm-system
    

For more information on using snapshot configuration files, see Customized snapshots in this document.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
