---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting/
title: Troubleshoot Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:46.150604+00:00
---

# Troubleshoot Distributed Cloud connected  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Troubleshoot Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

Google remotely monitors and maintains the Google Distributed Cloud connected deployments. For this purpose, Google engineers have Secure Shell (SSH) access to the Distributed Cloud connected hardware. If Google detects an issue, a Google engineer contacts you to troubleshoot and resolve it. If you have identified an issue yourself, contact Google Support immediately to diagnose and resolve it.

## Distributed Cloud connected software upgrades

This section describes how to use Metrics Explorer to check whether a Distributed Cloud connected cluster is undergoing a software upgrade.

This procedure uses the following Monitoring metrics:

  * **Current Cluster Version** (`/edge_cluster/current_cluster_version`): indicates the current version of the Distributed Cloud connected software running on the cluster.

  * **Target Cluster Version** (`/edge_cluster/target_cluster_version`): indicates the target version of the Distributed Cloud connected to which the cluster is upgrading.




To complete the steps in this section, you must satisfy the following prerequisites:

  1. Access to the Google Cloud console and your Distributed Cloud connected Google Cloud project.
  2. The **Monitoring Viewer** IAM role, which lets you view Monitoring metrics.
  3. (Optional) the `machine_id` value of the target Distributed Cloud connected machine for filtering the returned results.



### Use Metrics Explorer to check the cluster's current and target software versions

  1. Navigate to Metrics Explorer:

     1. In the Google Cloud console, navigate to the **Monitoring** section.

     2. In the left-hand navigation tree, click **Metrics Explorer**.

  2. Select the target resource type:

     1. In the Metrics Explorer page, navigate to the **Configuration** page.

     2. Click **Select a metric**.

     3. Use the search bar to search for the **Cluster** resource type. You can also use the full resource identifier `edgecontainer.googleapis.com/Cluster`.

     4. In the returned results, click the **Cluster** resource type.

  3. Obtain the cluster's current software version:

     1. In the **Metric** section, search for the `current_cluster_version` value.

     2. Select the **Machine Uptime** metric. Its full path is `edgecontainer.googleapis.com/edge_cluster/current_cluster_version`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

  4. Obtain the cluster's target software version:

     1. Click **Add Query**.

     2. In the **Metric** section, search for the `target_cluster_version` value.

     3. Select the **Target Cluster Version** metric. Its full path is `edgecontainer.googleapis.com/edge_cluster/target_cluster_version`.

     4. (Optional) Filter by the target `machine_id` value using the **Filter** section.

  5. Check the cluster's software upgrade status in the chart that appears.

     * If the **Current Cluster Version** and **Target Cluster Version** lines each indicate different values, the cluster is undergoing a software upgrade.

     * If the **Current Cluster Version** and **Target Cluster Version** lines indicate the same value, the cluster is not undergoing a software upgrade.

  6. Verify the result from the previous step using the following command:
         
         gcloud edge-cloud container clusters describe CLUSTER_ID --location=REGION
         

Replace the following:

     * `CLUSTER_ID`: the ID of the target cluster.
     * `REGION`: the Google Cloud region in which the cluster has been created.

In the command's output, note the values of the following fields:

     * If the value of the `status` field is `UPDATING`, the cluster is undergoing a software upgrade.
     * If the values of the `clusterVersion` and `targetVersion` fields are different, check them against the values returned by Metrics Explorer. 



### Understand the results

The following table explains the results returned by Metrics Explorer and the `gcloud` command.

Cluster state | Diagnosis | Resolution  
---|---|---  
**Healthy**  
`currentVersion` and `targetVersion` values match  
`status` value is `RUNNING`  
| Cluster is running the target version of the Distributed Cloud connected software. | None.  
**Upgrading**  
`currentVersion` value is lower than `targetVersion`  
`status` value is `UPDATING`  
| Cluster is upgrading to the target version of the Distributed Cloud connected software. | Monitor the cluster in Metrics Explorer until the current and target cluster version values match.  
**Stuck**  
`currentVersion` value is lower than `targetVersion` indefinitely  
`status` value is `UPDATING` indefinitely  
| Upgrade to the target version of the Distributed Cloud connected software has failed on at least one node in the cluster. | Check machine connectivity and system logs; contact Google for assistance.  
**Rolling back**  
`currentVersion` value is higher than `targetVersion`  
`status` value is `UPDATING`  
| luster is rolling back to a previous version of the Distributed Cloud connected software. | Contact Google to identify the reason for the rollback.  
  
If the software upgrade on the cluster has failed or the cluster has rolled back to a previous software version, check the following:

  * **Node health**. Verify that each physical Distributed Cloud connected machine has network connectivity and reporting uptime as described in the next section.
  * **Maintenance windows**. Verify whether the software upgrade has been paused due to a maintenance exclusion window.
  * **System logs**. Examine your system logs to identify possible reasons for the software upgrade failure, such as Pod eviction timeouts.



If the resolution steps listed in the table don't resolve the issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/docs/latest/getting-support) with the affected machine's `machine_id` value and the timestamp of the outage.

## Distributed Cloud connected machine restarts

This section describes how to use Metrics Explorer to check whether a Distributed Cloud connected physical machine has restarted, and determine the reason for the restart. Monitoring restarts helps determine whether they were part of planned maintenance or the result of a hardware failure or power disruption.

This procedure uses the following Monitoring metrics:

  * **Machine Uptime** (`/machine/uptime`): indicates the time, in seconds, since the last restart.

  * **Machine Restarts** (`/machine/restart_count`): indicates the total number of restarts for the target machine since its deployment.




To complete the steps in this section, you must satisfy the following prerequisites:

  1. Access to the Google Cloud console and your Distributed Cloud connected Google Cloud project.
  2. The **Monitoring Viewer** IAM role, which lets you view Monitoring metrics.
  3. (Optional) the `machine_id` value of the target Distributed Cloud connected machine for filtering the returned results.



### Use Metrics Explorer to check machine uptime and restart count

  1. Navigate to Metrics Explorer:

     1. In the Google Cloud console, navigate to the **Monitoring** section.

     2. In the left-hand navigation tree, click **Metrics Explorer**.

  2. Select the target resource type:

     1. In the Metrics Explorer page, navigate to the **Configuration** page.

     2. Click **Select a metric**.

     3. Use the search bar to search for the **Machine** resource type. You can also use the full resource identifier `edgecontainer.googleapis.com/Machine`.

     4. In the returned results, click the **Machine** resource type.

  3. Check the machine's uptime:

     1. In the **Metric** section, search for the `uptime` value.

     2. Select the **Machine Uptime** metric. Its full path is `edgecontainer.googleapis.com/machine/uptime`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the uptime graph is continuously rising. If at any point the uptime value drops to zero and restarts, this indicates the machine has restarted.

  4. Check the machine's restart count:

     1. In the **Metric** section, search for the `restart_count` value.

     2. Select the **Machine Restarts** metric. Its full path is `edgecontainer.googleapis.com/machine/restart_count`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the graph line remains at `0`, which indicates no restarts have occurred. If at any point the line spikes to `1` this indicates the machine has restarted; note the exact timestamp of the restart for further troubleshooting.

     5. (Optional) To view individual events instead of a graph, navigate to the **Aggregation** section of the page, set the **Alignment period** field to `1 minute` and the **Per-series aligner** field to **Delta**.




### Understand the results

The following table explains the results returned by Metrics Explorer.

Machine state | Diagnosis | Resolution  
---|---|---  
**Stable**  
"Machine Uptime" metric rises steadily  
"Machine Restarts" metric delta is `0`  
| Machine has not restarted. | None.  
**Clean restart**  
"Machine Uptime" metric drops to `0`  
"Machine Restarts" metric spikes to `1`  
| Machine has successfully restarted and reconnected to Google Cloud. | Check system logs to determine the reason for the restart.  
**Power failure**  
"Machine Uptime" metric graph has a break with no data  
"Machine Restarts" metric has not changed during the break in machine uptime  
| Machine lost power or network connectivity before it could restart. | Check power and network cabling, local network configuration, LED indicator status.  
**Intermittent**  
"Machine Connected" metric value alternates between `0` and `1`  
"Network Connectivity" metric value alternates between `0` and `1`  
| Unstable network connection, packet loss, or excessive latency. | Check your local network for congestion and faulty hardware.  
  
If the resolution steps listed in the table don't resolve the issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/docs/latest/getting-support) with the affected machine's `machine_id` value and the timestamp of the outage.

## Distributed Cloud connected machine connectivity

This section describes how to check the internet and Google Cloud connectivity for your Distributed Cloud connected machines using the Metrics Explorer feature of Cloud Monitoring.

This procedure uses the following Monitoring metrics:

  * **Machine Connected** (`/machine/connected`): indicates whether the machine is connected to Google Cloud.

  * **Network Connectivity** (`/machine/network/connectivity`): indicates whether the machine's primary network interface has internet connectivity.




To complete the steps in this section, you must satisfy the following prerequisites:

  1. Access to the Google Cloud console and your Distributed Cloud connected Google Cloud project.
  2. The **Monitoring Viewer** IAM role, which lets you view Monitoring metrics.
  3. (Optional) the `machine_id` value of the target Distributed Cloud connected machine for filtering the returned results.



### Use Metrics Explorer to check machine connectivity

  1. Navigate to Metrics Explorer:

     1. In the Google Cloud console, navigate to the **Monitoring** section.

     2. In the left-hand navigation tree, click **Metrics Explorer**.

  2. Select the target resource type:

     1. In the Metrics Explorer page, navigate to the **Queries** page.

     2. Use the search bar to search for the **Machine** resource type. You can also use the full resource identifier `edgecontainer.googleapis.com/Machine`.

     3. In the returned results, click the **Machine** resource type.

  3. Check the machine's connection to Google Cloud:

     1. In the **Metric** section, search for the `connected` value.

     2. Select the **Machine Connected** metric. Its full path is `edgecontainer.googleapis.com/machine/connected`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the **Healthy** line remains at 100% contiguously. If at any point this value is 0% or **Unhealthy** , the machine had lost connectivity with Google Cloud at the indicated time.

  4. Check the machine's internet connectivity:

     1. In the **Metric** section, search for the `connectivity` value.

     2. Select the **Network Connectivity** metric. Its full path is `edgecontainer.googleapis.com/machine/network/connectivity`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the **Healthy** line remains at 100% contiguously. If at any point this value is 0% **Unhealthy** , the machine had lost internet connectivity at the indicated time.




### Understand the results

The following table explains the results returned by Metrics Explorer.

Machine state | Diagnosis | Resolution  
---|---|---  
**Healthy**  
"Machine Connected" metric value is `1`  
"Network Connectivity" metric value is `1`  
| Normal operation. | None.  
**Disconnected**  
"Machine Connected" metric value is `0`  
"Network Connectivity" metric value is `1`  
| Machine has internet connectivity but can't connect to Google Cloud. | Check your [firewall rules](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/requirements#management-monitoring-traffic) for Google services and API endpoints. Verify that Distributed Cloud connected agents are running on the machine.  
**Isolated**  
"Machine Connected" metric value is `0`  
"Network Connectivity" metric value is `0`  
| Machine has no internet connectivity. | Check power and network cabling, local network configuration, LED indicator status. Verify your VLAN and routing configuration.  
**Intermittent**  
"Machine Connected" metric value alternates between `0` and `1`  
"Network Connectivity" metric value alternates between `0` and `1`  
| Unstable network connection, packet loss, or excessive latency. | Check your local network for congestion and faulty hardware.  
  
If you notice sustained values of `0` for either metric, follow the troubleshooting steps described in the table to resolve them. If the problem persists, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/docs/latest/getting-support) with the affected machine's `machine_id` value and the timestamp of the outage.

## Virtual machines stuck in `Pending` state

A virtual machine workload can get stuck in the `Pending` state and fail to schedule on a node if one of the following happens:

  * Distributed Cloud connected cannot allocate the requested resources, such as CPU time, memory, or disk space, to the virtual machine.
  * There is a fault in the virtual machine's configuration.
  * There is a fault with the virtual machine's storage.
  * The target node is tainted.



To resolve this issue, do the following:

  1. Obtain cluster credentials as described in [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#credentials).

  2. Get information about the affected virtual machine:
         
         kubectl describe virtualmachine VM_NAME -n NAMESPACE
         

Replace the following:

     * `VM_NAME`: The name of the target virtual machine.
     * `NAMESPACE`: The namespace of the target virtual machine.

The command returns output similar to the following:
    
    Status:
    ...
    State:                    Pending
    ...
    Events:
    Type     Reason                  Age   From                       Message
    ----     ------                  ----  ----                       -------
    Normal   SuccessfulCreate        15m   virtualmachine-controller  Created virtual machine my-stuck-vm
    Warning  DiskProvisioningFailed  14m   virtualmachine-controller  Failed to provision disk: DataVolume my-stuck-vm-data-disk not ready
    Warning  PVCNotBound             14m   virtualmachine-controller  PersistentVolumeClaim my-stuck-vm-data-disk is in phase Pending
    Warning  VMINotCreated           10m   virtualmachine-controller  VirtualMachineInstance cannot be created: dependencies not ready
    

The output of the command contains messages that might indicate resource constraints, scheduling failures, storage faults, and other problems.

  3. Examine the output to determine the causes of the scheduling failure as explained in the next sections.




### Insufficient resources

You might see a message indicating insufficient resources, such as CPU, memory, or disk space. For example:
    
    
    5/8 nodes are available: 3 Insufficient memory, 3 Insufficient CPU.
    

To remedy this problem, check the resources allocated to the affected virtual machines and other workloads scheduled on the node, then do the following depending on your business needs:

  * Scale down other workloads scheduled on the node,
  * Reduce the amount of resources allocated to the affected virtual machine,
  * Add more machines to the affected cluster.



### Tainted nodes

You might see a message indicating the target node is tainted. For example:
    
    
    5/8 nodes are available: 3 node(s) had taint {<taint-key>:<taint-value>}, that the pod didn't tolerate.
    

To remedy this problem, do the following:

  1. Use the following command to check for taints on the node:
         
         kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
         

The command returns output similar to the following:
         
         NAME                           TAINTS
         node-name-1   [map[effect:PreferNoSchedule key:node-role.kubernetes.io/master] map[effect:PreferNoSchedule key:node-role.kubernetes.io/control-plane]]
         node-name-2   <none>
         

  2. Do one of the following:

     * For unexpected taints, remove them as described in [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).
     * For expected taints, add corresponding tolerations to the virtual machine's configuration, as described in [Taints and Tolerations](https://kubevirt.io/user-guide/compute/node_assignment/#taints-and-tolerations).



### Storage faults

You might see a message indicating a fault with the virtual machine's storage. For example:
    
    
    5/8 nodes are available: 3 node(s) had volume node affinity conflict, 3 node(s) had unbound immediate PersistentVolumeClaims.
    

This message might indicate that the corresponding persistent volume fails to mount on the target node.

To remedy this problem, do the following:

  1. Use the following command to obtain the status of the persistent volume claims (PVCs) in the affected virtual machine's namespace:
         
         kubectl get pvc -n NAMESPACE
         

Replace `NAMESPACE` with the name of the target namespace.

The command returns output similar to the following:
         
         NAME                                               STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS            AGE
         windows-robin-disk-0                               Bound     pvc-b1a1d264-84bf-4e58-857d-f37f629d5082   25Gi       RWX            robin-block-immediate   30h
         windows-robin-disk-1                               Bound     pvc-0130b9a8-7fed-4df0-8226-d79273792a16   25Gi       RWX            robin-block-immediate   30h
         windows-robin-vm-0-restored-windows-robin-disk-0   Pending                                                                        gce-pd-gkebackup-in     26m
         

  2. Verify that the corresponding PVC has a `Bound` status; if the status is `Pending`, the storage subsystem has failed to provision the volume. In such cases, you must troubleshoot the storage subsystem configuration and ensure that the appropriate `StorageClass` is available.




## Scheduling lock-ups caused by failed admission webhooks

Admission webhooks let you intercept requests to the Kubernetes API server before the object becomes persistent. While useful for enforcing custom security policies, misconfigured webhooks can cause cluster-wide outages, especially during critical operations such as software upgrades and certificate refreshes. Specifically, a blocked or unavailable admission webhook can stall the Kubernetes control plane, preventing any further workload scheduling on the cluster.

### Control plane deadlocking

A circular dependency deadlock can occur when an admission webhook is responsible for validating resources that are required for the webhook's own recovery. For example, if an admission webhook is configured to validate Pods and that webhook Pod needs to be rescheduled during a node software upgrade, the Kubernetes API server may attempt to contact the webhook to authorize the creation of the new Pod. If the webhook is not reachable, the request fails, the Pod is not created, and the cluster enters a deadlock state where no new workloads can be scheduled.

When a webhook is configured with `failurePolicy: Fail`, any communication error or timeout between the API server and the webhook results in the rejection of the API request. This causes the following problems:

  * **Software upgrades fail** : System components and VMs can't be scheduled during and after a node software upgrade.
  * **System services can't start** : Infrastructure Pods, such as Symcloud Storage and VM Runtime on GDC, can't start.
  * **Nodes stuck in maintenance mode** : Nodes in maintenance mode can't be reconciled or exited because the controller is blocked by the admission logic.



### Webhook configuration best practices

Follow the best practices described in this section to prevent the control plane deadlocking described earlier. These best practices apply to all `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` objects.

#### Use `failurePolicy: Ignore`

Unless your business requirements dictate that an API request **must** fail if it can't be validated, always set the `failurePolicy` field to `Ignore`. This ensures that the Kubernetes API server continues to function even when the affected webhook service is down, allowing system-critical Pods to schedule and recover.

#### Exclude reserved namespaces

Your webhooks must never intercept requests for resources in reserved namespaces. You must exclude those namespaces from your webhook configuration using the `namespaceSelector` field. See [Management namespace restrictions](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy#namespace-restrictions) for a complete list of reserved namespaces. For example:
    
    
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingWebhookConfiguration
    metadata:
      name: "customer-policy-webhook"
    webhooks:
    - name: "validate-labels.example.com"
      failurePolicy: Ignore
      sideEffects: None
      admissionReviewVersions: ["v1"]
      namespaceSelector:
        matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values:
          - kube-system
          - kube-node-lease
          - kube-public
          - capi-system
          - capi-kubeadm-bootstrap-system
          - gke-system
          - gke-connect
          - gke-operators
          - gke-managed-metrics-server
          - anthos-identity-service
          - anthos-creds
          - robinio
          - robin-admin
          - vm-system
          - cert-manager
          - cert-manager-cluster-resources
          - dns-system
          - g-istio-system
          - nf-operator
          - prom-monitoring
          - gpu-system
          - oclcm-system
          - saas-system
      rules:
      - operations: ["CREATE", "UPDATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["pods", "deployments"]
    

### Recover a cluster deadlocked by failed webhooks

If your cluster has been deadlocked by failed webhooks, and your `kubectl` commands for creating resources time out or return errors, it's typically because the webhook has its `failurePolicy` set to `Fail`. Follow the steps in this section to recover the cluster from the deadlock. If the failing webhook is a mutating webhook, use `mutatingwebhookconfiguration` instead of `validatingwebhookconfiguration`.

  1. Identify the failed webhooks:

     1. List the validating webhooks deployed on the cluster:
            
            kubectl get validatingwebhookconfigurations
            

     2. List the mutating webhooks deployed on the cluster:
            
            kubectl get mutatingwebhookconfigurations
            

  2. Verify whether the Pods backing those webhooks are running:
         
         kubectl get pods -A | grep WEBHOOK_SERVICE
         

Replace `WEBHOOK_SERVICE` with the name of the target webhook's service.

  3. Set the failed webhook's `failurePolicy` to `Ignore`:
         
         kubectl patch validatingwebhookconfiguration WEBHOOK_CONFIG \
           --type='json' \
           -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value":"Ignore"}]'
         

Replace `WEBHOOK_SERVICE` with the name of the target webhook's service.

  4. (Optional) If the previous step failed, force-delete the affected webhook's configuration:
         
         kubectl delete validatingwebhookconfiguration WEBHOOK_CONFIG --timeout=10s
         

Replace `WEBHOOK_CONFIG` with the name of the target webhook's configuration.




After modifying or force-deleting the webhook's configuration, the Kubernetes API server resumes processing requests, resolving the deadlock and letting blocked processes complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
