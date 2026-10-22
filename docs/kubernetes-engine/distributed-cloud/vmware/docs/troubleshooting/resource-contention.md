---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/resource-contention/
title: Troubleshooting resource contention issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:24.482139+00:00
---

# Troubleshooting resource contention issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/resource-contention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshooting resource contention issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to identify and troubleshoot resource contention issues in your Google Distributed Cloud environment.

## Overview

Sometimes your Google Distributed Cloud might experience resource contention, causing your containers to slow down, underperform, or get terminated. This can happen due to high CPU or memory consumption by the containers.

### How CPU and memory management works

  * CPU:

    * A Pod is scheduled to a node based on the CPU requests specified by the containers in the Pod.
    * A container in a Pod can't use more CPUs than the limit specified by the container
    * The CPU usage of the container is throttled at the CPU limit.
    * If the CPU usage is throttled at the node level, the containers are automatically assigned the CPU cycles proportional to the requests.

Learn more about [how Pods with resource requests are scheduled](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#how-pods-with-resource-requests-are-scheduled).

  * Memory:

    * A Pod is scheduled to a node based on the memory requests specified by the containers in the Pod.
    * A container can't use more memory than the limit specified by the container.
    * If there is no memory limit specified, a container might consume all the available memory on a node. Then the system might trigger the OOM-Killer (Out Of Memory Killer) and evict the low priority Pods.



For more information, see the following:

  * [Assign CPU resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
  * [Assign memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
  * [Google Distributed Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos)



## Issues

### Container becomes slow

CPU contention issues can cause the containers to become slow. Following are some of the potential reasons:

#### High CPU utilization on the container:

A container can become slow if it doesn't get CPU cycles proportional to the CPU requests, or the CPU requests have been set to lower than what the container needs. So check the ratio of CPU limit to CPU utilization for the container.

In **the Google Cloud console > Monitoring > Metrics explorer**, in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
    
    
      avg_over_time({
        "__name__"="kubernetes.io/anthos/container/cpu/limit_utilization",
        "monitored_resource"="k8s_container",
        "cluster_name"="CLUSTER_NAME",
        "container_name"="CONTAINER_NAME",
        "pod_name"="POD_NAME",
        "namespace_name"="NAMESPACE_NAME"
      }[${__interval}])
    

Then do one of the following:

  * If this ratio is high (>=0.8), then it means that the CPU limit on the container is low, and Kubernetes is throttling the container's CPU cycles to keep CPU usage within limit. To resolve this issue, [increase the CPU limit on the container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#specify-a-cpu-request-and-a-cpu-limit).
  * If this ratio is not high (<0.8), check if the CPU utilization is high on the node.



#### High CPU utilization on the node

If the ratio of CPU limit to utilization is not high for any individual container of the Pod, then it might be that the node doesn't have enough CPU cycles to allocate to the set of containers running on the node. So follow these steps to check the ratio of actual CPU usage to the allocatable CPUs on the node:

  1. Get the node for the Pod that is working slow:
         
         kubectl get pod –kubeconfig CLUSTER_KUBECONFIG --namespace NAMESPACE POD --output wide
         

  2. In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
         
         avg_over_time({
           "__name__"="kubernetes.io/anthos/node/cpu/allocatable_utilization",
           "monitored_resource"="k8s_node",
           "cluster_name"="CLUSTER_NAME",
           "node_name"="NODE_NAME"
         }[${__interval}])
         

If this ratio is high (>=0.8), then it means that the node doesn't have enough CPU cycles, and is oversubscribed. So follow these steps to check the CPU usage for all the other Pods on that node, and investigate if there is another container using more CPUs.

     1. Get all Pods on the node:
    
    kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=NODE_NAME
    

     1. Check the CPU utilization on each container:
    
    avg_over_time({
      "__name__"="kubernetes.io/anthos/container/cpu/limit_utilization",
      "monitored_resource"="k8s_container",
      "cluster_name"="CLUSTER_NAME",
      "container_name"="CONTAINER_NAME",
      "pod_name"="POD_NAME",
      "namespace_name"="NAMESPACE_NAME"
    }[${__interval}])
    

If there is another container using high CPU on the node, [increase the CPU requests and limits on the container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#specify-a-cpu-request-and-a-cpu-limit) that's working slow. This will recreate the Pod on another node to get the required CPU cycles.




In case it's a system Pod that's working slow, contact [Google support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).

#### CPU oversubscription at the vSphere level

If the CPU consumption is not high on either the node or the Pod, and the container is still slow, then the VM might be oversubscribed at the vSphere level. Hence, the node is unable to get the expected CPU cycles from the underlying virtualization.

Follow [these steps](https://kb.vmware.com/s/article/2001003#CPU%20constraints) to check if the VM is oversubscribed. If oversubscription is detected, try the following:

  * Move some VMs to other hosts.
  * Evaluate, and decrease the number of vCPUs per VM, for the host.
  * Allocate more resources to the cluster VMs.
  * [Increase the CPU requests and limits on the container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#specify-a-cpu-request-and-a-cpu-limit). This will recreate the Pod on another node to get the required CPU cycles.



### Pod gets OOMkilled (Out of Memory-Killed)

The Pods can get OOMKilled due to the memory leaks or poor configuration of memory requests and limits on the containers. Following are some of the potential reasons:

#### High memory usage on the container

A Pod can get OOMkilled if any container in a Pod over consumes the total allocated memory. So check the ratio of memory requests to memory limits on the container.

In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
    
    
    avg_over_time({
      "__name__"="kubernetes.io/anthos/container/memory/limit_utilization",
      "monitored_resource"="k8s_container",
      "memory_type"="non-evictable",
      "cluster_name"="CLUSTER_NAME",
      "container_name"="CONTAINER_NAME",
      "pod_name"="POD_NAME",
      "namespace_name"="NAMESPACE_NAME"
    }[${__interval}])
    

Then do one of the following:

  * If this ratio is high (>= 0.8), then [increase the memory limit on the container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/#specify-a-memory-request-and-a-memory-limit).
  * If this ratio is not high (<0.8), check if the memory usage on the node is high.



#### High memory usage on the node

A Pod can get OOMkilled if the memory usage of all the Pods running on the node exceeds the available memory. So check if the `MemoryPressure` condition on the node is `True`.

  1. Run the following command and inspect the `Conditions` section:
         
         kubectl describe nodes --kubeconfig CLUSTER_KUBECONFIG NODE-NAME
         

  2. If the `MemoryPressure` condition is `True`, then check memory utilization on the node:
         
         avg_over_time({
           "__name__"="kubernetes.io/anthos/node/memory/allocatable_utilization",
           "monitored_resource"="k8s_node",
           "memory_type"="non-evictable",
           "cluster_name"="CLUSTER_NAME",
           "node_name"="NODE_NAME",
         }[${__interval}])
         

If this ratio is high (>= 0.8), then it means that the node doesn't have enough memory to allocate to the Pod, possibly due to some processes or other Pods consuming high memory.

  3. In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query to check memory usage for the containers on the node:
         
         avg_over_time({
           "__name__"="kubernetes.io/anthos/container_memory_usage_bytes",
           "monitored_resource"="k8s_node",
           "cluster_name"="CLUSTER_NAME",
           "node_name"="NODE_NAME",
         }[${__interval}])
         

If there is a container using high memory, investigate the functioning of the container or [increase the memory request for the container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/#specify-a-memory-request-and-a-memory-limit), if needed.




In case it's a system Pod that's consuming high memory, contact [Google support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).

Additionally, you can enable the [autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-autoscaler) feature in Google Distributed Cloud to automatically scale-up and scale-down the node pools based on the demands of your workloads.

Learn how to [enable the autoscaler](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-autoscaler).

### Etcd issues

Sometimes your Anthos clusters on VMware might experience container failures due to the etcd server issues, and you might observe the following:

  * Repeated API server logs of the form:

`etcdserver: request timed out` and `etcdserver: leader changed`

  * Repeated etcd logs of the form:

`W | wal: sync duration of 2.466870869s, expected less than 1s` and `W | etcdserver: read-only range request * took too long`




Following are some of the potential reasons:

#### CPU throttling

The etcd server might be slow due to the CPU throttling on the etcd server Pod and/or the node on which the etcd server is running. Refer to the steps in Container becomes slow section to check for any CPU contention issues.

If you detect CPU contention on the ectd server Pod or on the node, add CPUs to the control plane node of the user cluster. Use [`gkectl update`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-the-control-plane-node-for-user-cluster#command-line) to edit the `cpus` field in the user cluster configuration file.

#### Etcd Pod OOMkilled

The etcd Pod might get OOMkilled due to resource contention issues. Refer to the steps in Pod gets OOMkilled (Out of Memory-Killed) section to check for any memory contention issues with the etcd server Pod and/or the node on which the etcd server is running.

If you detect OOMkills for the etcd Pod, increase the memory available to the control plane node of the user cluster. Use [`gkectl update`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-the-control-plane-node-for-user-cluster#command-line) to edit the `memoryMB` field in the user cluster configuration file.

#### Disk slowness

If there are no issues with the CPU or memory consumption on the etcd server Pod or the node, the etcd might be slow if the underlying datastore is slow or throttled.

Check for the following problems:

  * To check if the etcd server is taking too long to read/write to the underlying disk:

    1. Fetch the etcd logs:
           
           kubectl –kubeconfig ADMIN_CLUSTER_KUBECONFIG logs -n ETCD_POD_NAMESPACE ETCD_POD
           

    2. Look for the entries of the following pattern to detect if etcd is taking too long to read from the disk:

`W | etcdserver: read-only range request "key:\"/registry/configmaps/default/clusterapi-vsphere-controller-manager-leader-election\" " with result "range_response_count:1 size:685" took too long (6.893127339s) to execute`

    3. Look for the entries of the following pattern to detect if etcd is taking too long to write to the disk:

`W | wal: sync duration of 2.466870869s, expected less than 1s`

If any or both of the above log patterns show frequently in the etcd logs, it indicates disk slowness. Then check the performance of the datastore and disks.

  * To check the etcd metrics:

    1. Fetch the etcd wal sync latencies:

In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
           
           histogram_quantile(0.99,
             sum by ("le") (
               increase({
                 "__name__"="kubernetes.io/anthos/etcd_disk_wal_fsync_duration_seconds_bucket",
                 "monitored_resource"="k8s_container",
                 "cluster_name"="CLUSTER_NAME",
                 "pod_name"="POD_NAME",
                 "namespace_name"="NAMESPACE_NAME"
               }[${__interval}])
             )
           )
           

    2. Fetch the etcd write latencies:

In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
           
           histogram_quantile(0.99,
             sum by ("le") (
               increase({
                 "__name__"="kubernetes.io/anthos/etcd_disk_backend_commit_duration_seconds",
                 "monitored_resource"="k8s_container",
                 "cluster_name"="CLUSTER_NAME",
                 "pod_name"="POD_NAME",
                 "namespace_name"="NAMESPACE_NAME"
               }[${__interval}])
             )
           )
           

If `p99` for `etcd_disk_wal_fsync_duration_seconds` is continuously over 10ms, and/or `p99` for `etcd_disk_backend_commit_duration_seconds` is continuously over 25ms, it indicates disk slowness. Then check the performance of the datastore and disks.




##### Read/write latencies on the VM disk

Follow these steps to check for the read/write latencies on the VM virtual disk

  1. Identify the node for the slow etcd Pod:
         
         kubectl –kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods -n ETCD_POD_NAMESPACE ETCD_POD -owide
         

  2. Sign in to vSphere and select the VM identified in the previous step: In vSphere, go to **Monitor** > **Performance** > **Advanced** , and select **Virtual Disk** from the **View** section to identify the read and write latencies for the virtual disks.

If the virtual disk read/write latency is high:

     * Examine other VMs running on the datastore to check for the high input/output operations per second (IOPS) usage. If any VM shows spikes in the IOPS, assess the functioning of that VM.
     * Consult your lab/infra team to make sure that the read and write bandwidth is not throttled or limited at any point.
     * Consult your lab/infra team to identify the [disk performance](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.monitoring.doc/GUID-E813116C-9D72-4464-BF3E-1B19F70F45BE.html) and [storage performance](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.monitoring.doc/GUID-AFC878A9-D61A-416C-BAFE-C700AA892C02.html) issues, if any.



For more information, see the [best practices for scaling your resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability#optimize_etcd_disk_io_performance).

### API server issues

If the containers in your Google Distributed Cloud experience latency while communicating with the API server, or the Kubectl commands fail or take too long to respond, this might indicate issues with the API server.

Following are some of the potential reasons:

#### High volume of API requests

The API server might be slow to respond if the frequency and volume of the requests on it is too high. The slow response time might persist even after the API server starts throttling the requests. So check the rate of API requests on the API server.

In **Google Cloud console** > **Monitoring** > **Metrics explorer** , in the [PromQL editor](https://cloud.google.com/monitoring/promql/promql-in-monitoring), run the following query:
    
    
    sum by (verb) (
      rate({
        "__name__"="kubernetes.io/anthos/apiserver_request_total",
        "monitored_resource"="k8s_container",
        "cluster_name"="CLUSTER_NAME",
        "pod_name"="APISERVER_POD_NAME",
        "namespace_name"="NAMESPACE_NAME"
       }[${__interval}])
    )
    

If there's an unexpected increase in the API requests, use [Cloud audit logging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/audit-logging) to identify the Pod that might be querying the API server too often.

  * If it's a system Pod, contact [Google support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).
  * If it's a user Pod, investigate further to determine if the API requests are expected.



#### CPU throttling

High request rate on the API server can lead to CPU throttling. Then the API server might become slow due to CPU contention on the API server Pod and/or the node.

Refer to the Container becomes slow section to check for any CPU contention issues with the Pod and/or the node.

#### API server Pod OOMkilled

The API server Pod might get OOMkilled due to resource contention issues. Refer to the steps in Pod gets OOMkilled (Out of Memory-Killed) section to check for any memory contention issues with the Pod and/or the node.

#### Slow etcd responses

The API server relies on communication with the etcd cluster to serve read / write requests to the clients. If the etcd is slow or unresponsive, the API server also becomes slow.

Fetch the logs of the API server to check if the API server is slow because of the etcd issues:
    
    
    kubectl –kubeconfig ADMIN_CLUSTER_KUBECONFIG logs -n APISERVER_NAMESPACE APISERVER_POD_NAME
    

If you observe the recurring logs like, `etcdserver: request timedout` or `etcdserver: leader changed`, follow the steps in Etcd issues to resolve any disk related issues.

## If your cluster doesn't export metrics

The techniques shown previously in this document rely on metrics being exported from your cluster to a Google Cloud project.

If your cluster doesn't export metrics, you can use the command line to investigate resource contention. Here are some commands you can run on your admin workstation to view metrics.

View metrics for a node:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get --raw \
        /apis/metrics.k8s.io/v1beta1/nodes/NODE_NAME | jq
    

Replace the following:

  * CLUSTER_KUBECONFIG: the path of the cluster kubeconfig file
  * NODE_NAME: the name of the node



View metrics for a Pod:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get --raw \
        /apis/metrics.k8s.io/v1beta1/namespaces/NAMESPACE/pods/POD_NAME | jq
    

Replace the following:

  * NAMESPACE: the namespace of the Pod
  * POD_NAME: the name of the Pod



View metrics for all nodes:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG top node
    

View metrics for all Pods in a namespace:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG top pod --namespace NAMESPACE
    

View metrics for the containers in all the Pods in a namespace:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG top pod --containers --namespace NAMESPACE
    

For more information, see [kubectl top pod](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/) and [kubectl top node](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/).

You can also run the [top](https://man7.org/linux/man-pages/man1/top.1.html) command from inside a container running on a node.

Here are two ways to run a command inside a container:

  * On your admin workstation, run [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/) to get a shell into the container. Run the command in the shell.

  * [Get an SSH connection to a node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node). Then use [docker exec](https://docs.docker.com/reference/cli/docker/container/exec/) to get a shell into the container. Run the command in the shell.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
