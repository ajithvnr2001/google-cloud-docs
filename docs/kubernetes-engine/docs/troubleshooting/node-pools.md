---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools/
title: Troubleshoot GKE Standard node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:06.916197+00:00
---

# Troubleshoot GKE Standard node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot GKE Standard node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When managing Google Kubernetes Engine (GKE) [Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison), issues with your [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) can disrupt critical operations. These problems can prevent you from scaling out workloads to meet demand or performing essential infrastructure upgrades, which might affect your application's reliability.

Use this page to troubleshoot these common node pool issues. Find guidance on how to confirm if you have insufficient resources, use features like best-effort provisioning to create nodes, and safely migrate your workloads without causing disruption.

This information is important for Platform admins and operators responsible for managing cluster infrastructure. It can also be useful for Application developers who need to understand how node pool limitations might affect their application deployments. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Node pool creation issues

This section lists issues that might occur when creating new node pools in Standard clusters and provides suggestions for how you might fix them.

### Issue: Node pool creation fails due to insufficient resources

The following issue occurs when you create a node pool with specific hardware in a Google Cloud zone that doesn't have enough hardware available to meet your requirements.

To validate that node pool creation failed because a zone didn't have enough resources, check your logs for relevant error messages.

  1. Go to Logs Explorer in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following query:
         
         log_id(cloudaudit.googleapis.com/activity)
         resource.labels.cluster_name="CLUSTER_NAME"
         protoPayload.status.message:("ZONE_RESOURCE_POOL_EXHAUSTED" OR "does not have enough resources available to fulfill the request" OR "resource pool exhausted" OR "does not exist in zone")
         

Replace `CLUSTER_NAME` with the name of your GKE cluster.

  3. Click **Run query**.




You might see one of the following error messages:

  * `resource pool exhausted`
  * `The zone does not have enough resources available to fulfill the request. Try a different zone, or try again later.`
  * `ZONE_RESOURCE_POOL_EXHAUSTED`
  * `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS`
  * `Machine type with name 'MACHINE_NAME' does not exist in zone 'ZONE_NAME'`



To resolve this issue, try the following suggestions:

  * Ensure that the selected Google Cloud region or zone has the specific hardware that you need. Use the [Compute Engine availability table](https://docs.cloud.google.com/compute/docs/regions-zones#available) to check whether specific zones support specific hardware. Choose a different Google Cloud region or zone for your nodes that might have better availability of the hardware that you need.
  * Create the node pool with smaller machine types. Increase the number of nodes in the node pool so that the total compute capacity remains the same.
  * Use [Compute Engine capacity reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to reserve the resources in advance.
  * Define a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) with a prioritized list of fallback machine series and enable [active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) (`optimizeRulePriority: true`). This configuration lets GKE automatically provision alternative hardware when your preferred machine series is unavailable in a zone and migrates workloads back when preferred capacity recovers.
  * Use best-effort provisioning, described in the following section, to successfully create the node pool if it can provision at least a specified minimum number of nodes out of the requested number.



**Best-effort provisioning**

For certain hardware, you can use _best-effort provisioning_ , which tells GKE to successfully create the node pool if it can provision at least a specified minimum number of nodes. GKE continues attempting to provision the remaining nodes to satisfy the original request over time. To tell GKE to use best-effort provisioning, use the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --node-locations=ZONE1,ZONE2,... \
        --machine-type=MACHINE_TYPE
        **--best-effort-provision \
        --min-provision-nodes=MINIMUM_NODES**
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `ZONE1,ZONE2,...`: the Compute Engine zones for the nodes. These zones must support the selected hardware.
  * `MACHINE_TYPE`: the Compute Engine engine machine type for the nodes. For example, `a2-highgpu-1g`.
  * `MINIMUM_NODES`: the minimum number of nodes for GKE to provision and successfully create the node pool. If omitted, the default is `1`.

**Note:** Best-effort provisioning is not available for TPUs and for Standard nodes that use a [compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement#compact-placement-standard).

For example, consider a scenario in which you need 10 nodes with attached NVIDIA A100 40GB GPUs in `us-central1-c`. According to [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones), this zone supports A100 GPUs. To avoid node pool creation failure if 10 GPU machines aren't available, you use best-effort provisioning.
    
    
    gcloud container node-pools create a100-nodes \
        --cluster=ml-cluster \
        --location=us-central1 \
        --node-locations=us-central1-c \
        --num-nodes=10 \
        --machine-type=a2-highgpu-1g \
        --accelerator=type=nvidia-tesla-a100,count=1 \
        **--best-effort-provision \
        --min-provision-nodes=5**
    

GKE creates the node pool even if only five GPUs are available in `us-central1-c`. Over time, GKE attempts to provision more nodes until there are 10 nodes in the node pool.

## Error: Instance does not contain 'instance-template' metadata

You might see the following error as a status of a node pool that fails to upgrade, scale, or perform automatic node repair:
    
    
    Instance INSTANCE_NAME does not contain 'instance-template' metadata
    

This error indicates that the metadata of VM instances, allocated by GKE, was corrupted. This typically happens when custom-authored automation or scripts attempt to add new instance metadata (like [`block-project-ssh-keys`](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys)), and instead of just adding or updating values, it also deletes existing metadata. You can read about VM instance metadata in [Setting custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#custom).

In case any of the critical metadata values (among others: `instance-template`, `kube-labels`, `kubelet-config`, `kubeconfig`, `cluster-name`, `configure-sh`, `cluster-uid`) were deleted, the node or entire node pool might render itself into an unstable state as these values are crucial for GKE operations.

If the instance metadata was corrupted, we recommend that you recover the metadata by re-creating the node pool that contains the corrupted VM instances. You will need to [add a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add) to your cluster and increase the node count on the new node pool, while cordoning and removing nodes on another. See the instructions to migrate workloads between node pools.

To find who and when instance metadata was edited, you can review [Compute Engine audit logging information](https://docs.cloud.google.com/compute/docs/logging/audit-logging) or find logs using [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) with a search query similar to the following:
    
    
    resource.type="gce_instance_group_manager"
    protoPayload.methodName="v1.compute.instanceGroupManagers.setInstanceTemplate"
    

In the logs you can find the request originator IP address and user agent. For example:
    
    
    requestMetadata: {
      callerIp: "REDACTED"
      callerSuppliedUserAgent: "google-api-go-client/0.5 GoogleContainerEngine/v1"
    }
    

## Migrate workloads between node pools

Use the following instructions to migrate workloads from one node pool to another node pool. If you want to change the machine attributes of the nodes in your node pool, see [Vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).

### Understand how to migrate Pods to a new node pool

To migrate Pods to a new node pool, you must do the following:

  1. **Cordon the nodes in the existing node pool:** This operation marks the nodes in the existing node pool as _unschedulable_. Kubernetes stops scheduling new Pods to these nodes once you mark them as _unschedulable_.

  2. **Drain the nodes in the existing node pool:** This operation evicts the workloads running on the nodes of the existing node pool gracefully.




These steps, done individually for each node, cause Pods running in your existing node pool to gracefully terminate. Kubernetes reschedules them onto other available nodes.

**Note:** If your workload has a LoadBalancer service with `externalTrafficPolicy` set to `Local`, then cordoning the existing node pool might cause the workload to become unreachable. Either change the `externalTrafficPolicy` to `Cluster` or ensure the workload is re-deployed into the new node pool before cordoning the existing pool.

To make sure Kubernetes terminates your applications gracefully, your containers should handle the [SIGTERM](http://man7.org/linux/man-pages/man7/signal.7.html) signal. Use this approach to close active connections to clients and commit or rollback database transactions in a clean way. In your Pod manifest, you can use the `spec.terminationGracePeriodSeconds` field to specify how long Kubernetes must wait before stopping containers in the Pod. This defaults to 30 seconds. You can read more about [Pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) in the Kubernetes documentation.

You can cordon and drain nodes using the `kubectl cordon` and `kubectl drain` commands.

**Note:** Kubernetes does not reschedule Pods that are not managed by a controller such as Deployment, ReplicationController, ReplicaSet, Job, DaemonSet or StatefulSet. Such Pods prevent `kubectl drain` commands from running, therefore you must deploy your Pods using these controllers. Run `kubectl drain` with `--force` option to clean up some GKE system Pods, such as kube-proxy and fluend-cloud-logging.

### Create node pool and migrate workloads

To migrate your workloads to a new node pool, create the new node pool, then cordon and drain the nodes in the existing node pool:

  1. [Add a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add) to your cluster.

Verify that the new node pool is created by running the following command:
         
         gcloud container node-pools list --cluster CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
**Note:** If you create a node pool with cluster autoscaler enabled and you wait more than 10 minutes to drain the existing node pool after creating the new node pool, cluster autoscaler might scale down the nodes in the new node pool because they are underutilized. In this scenario, if the Pods can only run on the new node pool, there would be a delay in rescheduling the Pods as the new node pool scales back up. To learn more, see [how cluster autoscaler works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#how_cluster_autoscaler_works).
  2. To disable autoscaling on the existing node pool, if it's enabled, run the following command:
         
         gcloud container clusters update CLUSTER_NAME
             --location=CONTROL_PLANE_LOCATION \
             --no-enable-autoscaling \
             --node-pool=EXISTING_NODE_POOL_NAME
         

  3. Run the following command to see which node the Pods are running on (see the `NODE` column):
         
         kubectl get pods -o=wide
         

  4. Get a list of nodes in the existing node pool, replacing `EXISTING_NODE_POOL_NAME` with the name:
         
         kubectl get nodes -l cloud.google.com/gke-nodepool=EXISTING_NODE_POOL_NAME
         

  5. Run the `kubectl cordon NODE` command (substitute `NODE` with the names from the previous command). The following shell command iterates each node in the existing node pool and marks them as unschedulable:
         
         for node in $(kubectl get nodes -l cloud.google.com/gke-nodepool=EXISTING_NODE_POOL_NAME -o=name); do
           kubectl cordon "$node";
         done
         

  6. Optionally, update your workloads running on the existing node pool to add a nodeSelector for the label `cloud.google.com/gke-nodepool:NEW_NODE_POOL_NAME`, where `NEW_NODE_POOL_NAME` is the name of the new node pool. This helps ensure that GKE places those workloads on nodes in the new node pool.

  7. Drain each node by evicting all Pods with an allotted graceful termination period of 10 seconds:
         
         for node in $(kubectl get nodes -l cloud.google.com/gke-nodepool=EXISTING_NODE_POOL_NAME -o=name); do
           kubectl drain --force --ignore-daemonsets --delete-emptydir-data --grace-period=GRACEFUL_TERMINATION_SECONDS  "$node";
         done
         

Replace `GRACEFUL_TERMINATION_PERIOD_SECONDS` with the required amount of time for graceful termination.

  8. Confirm that the nodes in the existing node pool have the `SchedulingDisabled` status in the node list by running the following command:
         
         kubectl get nodes
         

Additionally, you should see that the Pods now run on the nodes in the new node pool:
         
         kubectl get pods -o=wide
         

  9. Delete the existing node pool if you don't need it:
         
         gcloud container node-pools delete default-pool --cluster CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
