---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass/
title: Troubleshoot custom ComputeClass issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:12:46.873008+00:00
---

# Troubleshoot custom ComputeClass issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot custom ComputeClass issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document helps you troubleshoot issues where GKE workloads fail to schedule on nodes defined by a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes), or when the cluster autoscaler does not provision the expected machine types.

This document is for Application developers and Platform admins and operators who use custom ComputeClasses to manage workload scheduling and node pool auto-creation in GKE. For more information about the common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Note:** This document applies to both Standard and Autopilot clusters. Because direct node access such as SSH is not supported in Autopilot clusters, you must adjust your troubleshooting steps for those environments.

## Key concepts

To help you troubleshoot, make sure you're familiar with the following GKE components and mechanisms:

  * **Custom ComputeClass** : a GKE-specific resource that lets you define a prioritized list of node configurations for autoscaling. For more information, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

  * **Cluster autoscaler** : the component that automatically adds or removes nodes in your cluster based on workload demand. For more information, see [ About GKE Cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

  * **Node pool auto-creation** : GKE cluster autoscaler automatically creates and manages node pools based on workload requirements. For more information, see [About node poo- auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).

  * **Fallback logic** : the mechanism where the cluster autoscaler attempts to provision nodes matching your highest priority rule first. For more information, see [Choose your fallback compute priorities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#choose-priorities).




## Troubleshoot by symptoms

This document organizes troubleshooting steps in sequence, from fundamental checks to more advanced configurations. For a more comprehensive diagnosis, we recommend performing these steps in order. Alternatively, if you are experiencing specific issues, refer to the relevant links in the following table:

Symptom | Troubleshooting steps  
---|---  
Pod requesting a custom ComputeClass is stuck in the `Pending` state | 

  * Perform basic diagnostic checks
  * Check Pod scheduling constraints
  * Node pool configuration (for Standard clusters)
  * Analyze cluster autoscaler pending Pods metric

  
Cluster autoscaler is not creating new nodes that match the custom ComputeClass | 

  * Verify custom ComputeClass configurations
  * Verify node pool auto-creation configuration
  * Analyze cluster autoscaler pending Pods metric
  * Analyze node provisioning failures

  
Cluster autoscaler creates default machine types instead of specialized types |  Analyze autoscaler fallback behavior  
Output from the `kubectl describe computeclass` command shows an unhealthy status |  Verify custom ComputeClass configurations  
Workloads are not migrating to higher-priority nodes |  Verify general cluster autoscaler health  
GPU or Spot VMs workloads have scheduling issues | 

  * Check Pod scheduling constraints
  * Verify GPU or Spot VMs configuration
  * Analyze autoscaler fallback behavior

  
  
## Out-of-scope issues

This document doesn't address the following issues:

  * General GKE networking issues, such as Pod-to-Pod connectivity or service load balancing.
  * Issues related to Horizontal Pod Autoscaler (HPA) or Vertical Pod Autoscaler (VPA).
  * Issues unrelated to the custom ComputeClass mechanism, such as application-level errors or PersistentVolume problems that aren't related to scheduling constraints.
  * Quota or [resource unavailability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) issues that aren't directly related to the ComputeClass fallback logic.



## Identify placeholder variables

To customize the commands in this document, enter your specific values into the `Variable` column. Edited values are automatically synchronized across all code blocks and commands.

Variable | Description  
---|---  
PROJECT_ID | Your Google Cloud project ID.  
LOCATION | The Compute Engine region or zone where the cluster is located.  
CLUSTER_NAME | The name of your cluster.  
NODE_POOL_NAME | The name of the node pool to inspect (if applicable for Standard clusters).  
CUSTOM_COMPUTECLASS_NAME | The name of the custom ComputeClass requested by the Pod.  
NAMESPACE | The namespace of the Pod that is failing to schedule.  
POD_NAME | The name of the Pod that is failing to schedule.  
  
## Before you begin

To get the permissions that you need to perform the tasks in this document, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

  * To access GKE clusters: Kubernetes Engine Cluster Viewer (`roles/container.viewer`). 
  * To view logs: Logs Viewer (`roles/logging.viewer`). 
  * To manage GKE clusters: Kubernetes Engine Admin (`roles/container.admin`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To configure `kubectl` to communicate with the cluster, run the following command:
    
    
      gcloud container clusters get-credentials CLUSTER_NAME
          --location LOCATION
          --project PROJECT_ID
    

## Perform basic diagnostic checks

Verify that the core components are correctly configured and that the cluster supports custom ComputeClasses.

### Verify Pod status and selector

Confirm that the Pod is in the `Pending` state and correctly requests the custom ComputeClass.

  1. List Pods in the `Pending` state:
         
         kubectl get pods --all-namespaces -o wide | grep Pending
         

  2. Inspect the Pod's specification for the `nodeSelector` field:
         
         kubectl get pod POD_NAME
             -n NAMESPACE
             -o jsonpath='{.spec.nodeSelector}'
         




#### Evaluate the result

  * **Output shows the label:** the `nodeSelector` field is correctly configured with the `cloud.google.com/compute-class` label.
  * **Output doesn't show the label:**
    * **Interpretation:** there might be an incorrect or missing `nodeSelector` field for the `cloud.google.com/compute-class` label in your workload's deployment configuration.
    * **Resolution:** modify your workload's YAML file, such as a Deployment or Job, to include the `nodeSelector` field in the `spec.template.spec` section.



### Verify cluster version compatibility

Custom ComputeClasses require GKE version 1.30.3-gke.1451000 or later. Verify that your cluster is running a version that supports custom ComputeClasses.

Check your cluster version:
    
    
    gcloud container clusters describe CLUSTER_NAME
        --location LOCATION
        --format="value(currentMasterVersion)"
    

#### Evaluate the result

  * **Version`1.30.3-gke.1451000` or later:** your cluster version supports custom ComputeClasses.
  * **Version earlier than`1.30.3-gke.1451000`:**
    * **Interpretation:** your cluster has not been upgraded to a version that supports custom ComputeClasses.
    * **Resolution:** you must [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to use custom ComputeClasses.



### Verify provisioned nodes for the custom ComputeClass

To check whether there are nodes in the cluster that are associated with your ComputeClass, list the nodes matching the ComputeClass label:
    
    
    kubectl get nodes -l cloud.google.com/compute-class=CUSTOM_COMPUTECLASS_NAME
    

If the output is `No resources found`, then there are no nodes that are associated with the ComputeClass. Verify that your workloads actually selected that ComputeClass and check your autoscaling events for scale-up errors.

## Verify custom ComputeClass configurations

Misconfigurations in the custom `ComputeClass` resource can prevent Pods from scheduling or prevent GKE from provisioning nodes correctly.

### Check ComputeClass health and status

Verify that GKE reports the custom ComputeClass as healthy.

  1. List all `ComputeClass` resources:
         
         kubectl get computeclass
         

  2. Describe the specific `ComputeClass` resource:
         
         kubectl describe computeclass CUSTOM_COMPUTECLASS_NAME
         




#### Evaluate the result

  * **Health status shows`True`:** the custom ComputeClass is healthy. The following is an example of a healthy custom ComputeClass:
        
        Status:
          Conditions:
            Last Transition Time:  2024-01-19T17:18:48Z
            Message:               CCC is healthy.
            Reason:                Health
            **Status:                True**
            Type:                  Health
        

  * **Health status shows`False`:**

    * **Interpretation:** the custom ComputeClass is unhealthy. Review the `Message` and `Reason` fields in the output to identify the issue.
    * **Resolution:** perform the action that corresponds to the `Reason` field in the output: 
      * `NodePoolNotExist`: ensure the referenced node pool exists or update the ComputeClass to reference an existing node pool.
      * `ReservationUnusable`: check the configuration and usage of the referenced reservation.
      * `Invalid machine type`: update the ComputeClass to use a machine type that is supported in the cluster's region or zone.



### Validate the `unsatisfiable` policy

The `whenUnsatisfiable` field determines behavior when no priority rules can be met.

Check the policy:
    
    
    kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
    

Inspect the `spec.whenUnsatisfiable` field in the output. This field can have one of the following values:

  * `DoNotScaleUp`: Pods remain in the `Pending` state if no preferred nodes can be created.
  * `ScaleUpAnyway`: Pods might run on default node types (like E2-series) if preferred nodes are unavailable.



#### Evaluate the result

The effect of the `whenUnsatisfiable` policy depends on its value:

  * **If the value is`DoNotScaleUp`:**
    * **Interpretation:** this is expected behavior when no priority rules can be satisfied, possibly due to resource unavailability or quota limits. If Pods must wait for specific hardware, this value is correct.
    * **Resolution:** if running the workload is more critical than running on specific hardware, change the policy to `ScaleUpAnyway`.
  * **If the value is`ScaleUpAnyway`:**
    * **Interpretation:** this is expected behavior. GKE is falling back to default node types because preferred nodes are unavailable.
    * **Resolution:** if Pods must not run on default node types, change the policy to `DoNotScaleUp`.
  * **Default behavior:** if you haven't specified a value for the `whenUnsatisfiable` field and are using a GKE version earlier than 1.33, the policy defaults to `ScaleUpAnyway`.



The following example shows how to update the policy by editing the `whenUnsatisfiable` field in your ComputeClass manifest:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: CUSTOM_COMPUTECLASS_NAME
    spec:
      # ... other fields
      **whenUnsatisfiable : DoNotScaleUp** # or ScaleUpAnyway
    

## Check Pod scheduling constraints

Ensure that your Pod specification is compatible with the attributes of nodes provisioned by the custom ComputeClass.

### Verify Pod resource requests

Check if the Pod's CPU, memory, and GPU requests can be satisfied by at least one of the machine types defined in the custom ComputeClass's `priorities` field.

  1. Get Pod resource requests:
         
         kubectl get pod POD_NAME
             -n NAMESPACE
             -o jsonpath='{.spec.containers[*].resources.requests}'
         

Inspect the output for `cpu`, `memory`, and GPU requests, such as `nvidia.com/gpu`.

  2. Compare these requests with the machine types defined in the `priorities` field of the custom ComputeClass:
         
         kubectl get computeclass CUSTOM_COMPUTECLASS_NAME
             -o jsonpath='{.spec.priorities}'
         

Inspect the output for the `machineType` or `machineFamily` fields. For each machine type in the custom ComputeClass, check its specifications in the [machine types documentation](https://docs.cloud.google.com/compute/docs/machine-types) and verify if its allocatable resources are greater than the Pod's requests.




#### Evaluate the result

  * **Resources compatible:** Pod's resource requests are less than or equal to the allocatable resources of at least one machine type in the ComputeClass.
  * **Resources exceed capacity:**

    * **Interpretation:** the Pod cannot be scheduled because no machine type in the ComputeClass provides sufficient CPU, memory, or GPU. This can also happen if `nodePoolAutoCreation` field is set to `true` and the Pod's memory request exceeds the limits of auto-created node pools.
    * **Resolution:** adjust either the Pod's resource requests or the custom ComputeClass's machine types: 
      * Reduce Pod resource requests: if the resource requests are high, lower the `cpu`, `memory`, or `gpu` values in the workload's YAML file.
      * Change to larger machine types: if the Pod's requests are justified, modify the `spec.priorities` field in your custom ComputeClass manifest to include larger `machineType` or `machineFamily` options that can fulfill the Pod demands. For example:
    
    spec:
      priorities:
      **- machineType: n2d-highmem-96** # A larger machine type
        spot: true
      # ... other priorities
    




### Check for conflicting taints and tolerations

Nodes created for a custom ComputeClass have the `cloud.google.com/compute-class=CUSTOM_COMPUTECLASS_NAME:NoSchedule` taint. GKE adds this toleration to Pods automatically.

However, specialized hardware like GPUs have additional taints such as the `nvidia.com/gpu=present:NoSchedule` taint. If your ComputeClass uses nodes with specialized hardware, Pods _must_ have a toleration for these taints to schedule on those nodes.

Check the `tolerations` field for the Pod:
    
    
    kubectl get pod POD_NAME
        -n NAMESPACE
        -o jsonpath='{.spec.tolerations}'
    

#### Evaluate the result

  * **Correct tolerations:** taints and tolerations are correctly configured.
  * **Missing tolerations:**

    * **Interpretation:** missing tolerations prevent the Pod from scheduling on nodes with specialized hardware taints. For example, if the ComputeClass uses GPU nodes, the Pod might be missing the `nvidia.com/gpu=present:NoSchedule` toleration. For GPU-specific requirements, see Verify GPU configuration.
    * **Resolution:** in the `tolerations` field in your Pod specification, add the necessary tolerations to match the taints on the nodes defined by the ComputeClass. For example, for GPU nodes, add a toleration for the `nvidia.com/gpu=present:NoSchedule` taint as follows:
          
          spec:
          template:
          spec:
          **tolerations :
          - key: "nvidia.com/gpu"
          operator: "Exists"
          effect: "NoSchedule"**
          # ... other tolerations and Pod spec
          




## Analyze the cluster autoscaler pending Pods metric

_Applicable GKE versions: 1.37 and later_

To understand why Pods requesting a specific ComputeClass are pending, use the `kubernetes.io/autoscaler/cluster_pending_pods_per_ccc` metric in Cloud Monitoring. This metric helps you pinpoint whether the issue is a lack of suitable nodes for the ComputeClass, a problem with provisioning, or something inherent to the Pod's configuration. This metric shows the number of Pods the cluster autoscaler is processing, broken down by the ComputeClass, the reason for being pending, and whether it's a system or user Pod.

### Steps to query

To query the metric in the Google Cloud console, perform the following steps:

  1. In the Google Cloud console, go to the Metrics explorer page.
  2. Select the **Resource type:** `k8s_entity`.
  3. Select the **Metric:** `kubernetes.io/autoscaler/cluster_pending_pods_per_ccc`.
  4. Add a **Filter:** `entity_type = ComputeClass`.
  5. Add a **Filter** for your specific ComputeClass: `entity_name = "COMPUTECLASS_NAME"`. 
     * To see Pods that are not using any ComputeClass, filter with `entity_name = ""`.
  6. **Group by** `metric.labels.reason` to see the autoscaler states for these Pods. You can also group Pods by using the `metric.labels.type` key label.



### Example PromQL query

To find the status of pending user Pods requesting the "COMPUTECLASS_NAME" ComputeClass, use the following PromQL query:
    
    
    sum by (reason) (
      kubernetes_io:autoscaler_cluster_pending_pods_per_ccc{
        monitored_resource="k8s_entity",
        entity_type="ComputeClass",
        entity_name="COMPUTECLASS_NAME",
        type="user_pod"
      }
    )
    

### Metric reasons

The output of the `metric.labels.reason` key label might include the following:

  * **`unable_to_provision`** : The cluster autoscaler is blocked. Pods in this state for a ComputeClass can't be scheduled because new nodes can't be created. Check cluster autoscaler logs in the control plane for details about stockouts, quotas, or misconfigurations within the ComputeClass definition. Also review cluster autoscaler visibility events.

  * **`provisioning_in_progress`** : A scale-up has been triggered for nodes that should match the ComputeClass requirements. If Pods remain here, there might be delays in node creation or readiness.

  * **`unprocessed`** : The cluster autoscaler hasn't yet evaluated these Pods. A persistent high number might indicate autoscaler lag.

  * **`no_action_taken`** : The cluster autoscaler has decided not to scale for these Pods. This behavior might result from Pod constraints that can't be satisfied by the ComputeClass's node types, or other cluster-level limits. Examine the Pod specification (`kubectl describe pod`) and cluster autoscaler logs.




## Analyze node provisioning failures

_Applicable GKE versions: 1.37 and later_

To check the current health status of a ComputeClass, see Verify ComputeClass health. If you observe that Pods associated with a ComputeClass are in an `unable_to_provision` state, the cluster autoscaler is not provisioning new nodes that match the requirements of the ComputeClass. You can use the `kubernetes.io/autoscaler/cluster_node_provisioning_failed_attempts_count_per_ccc` Cloud Monitoring metric to diagnose the root cause.

  1. In the Google Cloud console, go to **Monitoring** , then **Metrics Explorer**.
  2. Select the **Resource type** as `k8s_entity`.
  3. Select the **Metric** as `kubernetes.io/autoscaler/cluster_node_provisioning_failed_attempts_count_per_ccc`.
  4. Add a **Filter** : `resource.labels.entity_type = ComputeClass`.
  5. Add a **Filter** for your specific ComputeClass: `entity_name = "CUSTOM_COMPUTECLASS_NAME"`. 
     * To see Pods _not_ using any ComputeClass, filter with `entity_name = ""`.
  6. In the **Group By** section, select `metric.labels.reason` and `resource.labels.entity_name`.
  7. Choose an **Aggregator** , such as `rate` or `delta`.



The rate or change in failures is displayed, broken down by the reason.

### Interpret failure reasons

The `metric.labels.reason` field provides insight into why node creation is failing. By identifying the primary reasons for failure, you can take corrective actions.

The possible reasons include the following:

Reason | Explanation | Potential corrective actions  
---|---|---  
`QUOTA_EXCEEDED` | A Google Cloud quota limit was reached (for example, CPUs, disks, or IP addresses). Review your project quotas. | [Request a quota increase](https://docs.cloud.google.com/docs/quota_detail/view_manage#requesting_higher_quota).  
`RESOURCE_POOL_EXHAUSTED` | Compute Engine unavailability; insufficient capacity for the requested resources in the zone. | Try different machine types or zones. Modify the ComputeClass to include [fallback machine types or zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#choose-priorities). Use [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).  
`IP_SPACE_EXHAUSTED` | The node subnet has run out of available IP addresses. | [Expand the subnet's primary IP address range](https://docs.cloud.google.com/vpc/docs/using-vpc#expand-subnet).  
`PERMISSIONS_ERROR` | The GKE service account lacks necessary IAM permissions to create resources (for example, instances, disks). | Grant required roles to the [GKE service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege).  
`VM_EXTERNAL_IP_ACCESS_POLICY_CONSTRAINT` | An organization policy (`constraints/compute.vmExternalIpAccess`) prevents creating nodes with external IPs as configured. | Review and modify the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) or ComputeClass node configuration.  
`INVALID_RESERVATION` | The configured Compute Engine reservation is invalid, misconfigured, or doesn't match the node request. | Check the [reservation settings](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) and ComputeClass definition.  
`RESERVATION_NOT_FOUND` | The specified Compute Engine reservation name does not exist. | Verify the reservation name in the ComputeClass.  
`RESERVATION_NOT_READY` | The targeted reservation is not yet active or is still being provisioned. | Wait for the reservation to become active.  
`RESERVATION_CAPACITY_EXCEEDED` | The reservation is full and cannot accommodate the request. | Increase reservation size or use other machine types.  
`RESERVATION_INCOMPATIBLE` | The node configuration (for example, machine type or zone) does not match the reservation's properties. | Align the ComputeClass node spec with the reservation's properties.  
`AUTOMATIC_RESERVATIONS_NOT_AVAILABLE` | An issue occurred while trying to use automatic reservations. | Check the logs; you might need to contact [Cloud Customer Care](https://cloud.google.com/support).  
`AUTOMATIC_RESERVATIONS_NO_CAPACITY` | Automatic reservations lack sufficient capacity. | Might need to switch to manual reservations or different machine types.  
`UNSUPPORTED_TPU_CONFIGURATION` | The requested TPU configuration is invalid or not supported in the selected zone or project. | Check the [TPU documentation](https://docs.cloud.google.com/tpu/docs/types-zones) and the ComputeClass.  
`GkePersistentOperationError` | A persistent error occurred within the GKE control plane during the node creation process. | [Contact Cloud Customer Care](https://cloud.google.com/support).  
`OTHER` | A catch-all explanation for failures that don't fit into other categories. | For more details, review the cluster autoscaler logs on the control plane.  
  
## Node pool configuration (Standard clusters)

In GKE Standard clusters, manually created node pools must be labeled and tainted to work with a custom ComputeClass.

### Verify node pool labels and taints

  1. Identify node pools in your custom ComputeClass. If the custom ComputeClass uses the `nodePools` field, note the names of the listed node pools:
         
         kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
         

  2. For each node pool that you identified, verify its configuration:
         
         gcloud container node-pools describe NODE_POOL_NAME
             --cluster CLUSTER_NAME
             --location LOCATION
             --format="yaml(config.labels, config.taints)"
         




#### Evaluate the result

  * **Node pool correctly configured:** the node pool has the label `cloud.google.com/compute-class: CUSTOM_COMPUTECLASS_NAME` and the taint `cloud.google.com/compute-class=CUSTOM_COMPUTECLASS_NAME:NoSchedule`.
  * **Node pool misconfigured:**

    * **Interpretation:** the node pool was not configured with the label and taint required to associate it with the custom ComputeClass.
    * **Resolution:** [update the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) to add the label and taint:

      1. Add or update node label:
             
             gcloud container node-pools update NODE_POOL_NAME \
                 --cluster=CLUSTER_NAME --location=LOCATION \
                 --node-labels=cloud.google.com/compute-class=CUSTOM_COMPUTECLASS_NAME
             

      2. Add or update node taint:
             
             gcloud container node-pools update NODE_POOL_NAME \
                 --cluster=CLUSTER_NAME --location=LOCATION \
                 --node-taints=cloud.google.com/compute-class=CUSTOM_COMPUTECLASS_NAME:NoSchedule
             




## Verify node pool auto-creation configuration

For both Autopilot and Standard clusters with `nodePoolAutoCreation` set to `true`, node pool auto-creation must be correctly configured.

### Verify node pool auto-creation is enabled

  1. Check if the `nodePoolAutoCreation.enabled` field in the custom ComputeClass is set to `true`:
         
         kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
         

  2. Check if node pool auto creation is enabled on the cluster:
         
         gcloud container clusters describe CLUSTER_NAME
             --location LOCATION
             --format="value(autoscaling.enableNodeAutoprovisioning)"
         




If either is disabled, node pool auto-creation won't create new node pools for your custom ComputeClass.

#### Evaluate the result

  * **Node pool auto-creation enabled:** in the ComputeClass, the `nodePoolAutoCreation.enabled` field is set to `true`, and node auto-provisioning is enabled at the cluster-level.
  * **Node pool auto-creation disabled:**

    * **Interpretation:** node pool auto-creation is disabled if the value of `nodePoolAutoCreation.enabled` field is `false` or missing in the ComputeClass, or if cluster-level node auto-provisioning is disabled.
    * **Resolution:** enable node pool auto-creation:

      1. Edit the custom ComputeClass YAML file to include `nodePoolAutoCreation: enabled: true`:
             
             spec:
               # ... priorities
               nodePoolAutoCreation:
                 **enabled : true**
             

      2. [Enable node pool auto-creation at cluster level and configure resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable):
             
             gcloud container clusters update CLUSTER_NAME --location LOCATION \
               --enable-autoprovisioning \
               --autoprovisioning-min-cpu=MIN_CPU \
               --autoprovisioning-max-cpu=MAX_CPU \
               --autoprovisioning-min-memory=MIN_MEMORY \
               --autoprovisioning-max-memory=MAX_MEMORY
             




### Check resource limits for node pool auto-creation

Node pool auto-creation has cluster-wide limits for CPU and memory. If the cluster's current usage plus the resources of a new node exceeds these limits, node pool auto-creation won't provision new nodes.

  1. View the resource limits:
         
         gcloud container clusters describe CLUSTER_NAME
             --location LOCATION
         --format="value(autoscaling.resourceLimits)"
         

The output lists the `resourceType`, `minimum`, and `maximum` fields for CPU and memory (in GB).

  2. Review the machine types in your custom ComputeClass's priorities. Check their CPU and memory specifications in the [machine types documentation](https://docs.cloud.google.com/compute/docs/machine-types).

  3. Determine the current total CPU and memory capacity of all nodes in the cluster. The sum of current capacity plus the resources of a potential new node must not exceed the maximum limit for node pool auto-creation.




#### Evaluate the result

  * **Sufficient capacity:** the cluster has sufficient CPU and memory capacity within resource limits for node pool auto-creation to provision a new node.
  * **Limits exceeded:**

    * **Interpretation:** node pool auto-creation can't provision new nodes because the cluster has reached CPU or memory limits, or limits were set too low for the machine types in the ComputeClass.
    * **Resolution:** increase the resource limits for node pool auto-creation:

      1. Determine new maximum limits that account for current usage and future growth, including the largest machine types in the custom ComputeClass.

      2. [Update resource limits for node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#set_limits). You can set multiple resources in one command:
             
             gcloud container clusters update CLUSTER_NAME --location LOCATION \
               --set-nap-resource-limits resourceType=cpu,maximum=NEW_MAX_CPU \
               --set-nap-resource-limits resourceType=memory,maximum=NEW_MAX_GB
             




## Analyze autoscaler fallback behavior

This section helps you investigate external factors to understand why the cluster autoscaler might be skipping preferred options and using fallbacks, or failing to scale up.

Custom ComputeClasses use prioritized fallback logic. If a Pod isn't scheduling on nodes matching the highest-priority rule, it's often due to constraints like resource unavailability or project quotas. When GKE can't provision nodes matching a specific priority rule, for example, due to a `ZONE_RESOURCE_POOL_EXHAUSTED` or `QUOTA_EXCEEDED` error from Compute Engine, the cluster autoscaler immediately tries the next rule in the `priorities` list. There is no waiting period before GKE falls back to the next priority, except when using TPUs or the Flex Start provisioning model, which support a configurable delay.

### Check for resource unavailability

Verify if resources are unavailable in the specified zone by checking cluster autoscaler logs or Compute Engine Managed instance group (MIG) errors.

**Option 1: Check cluster autoscaler visibility events**

In the Google Cloud console, go to **Cloud Logging > Logs Explorer** and run the following query to find autoscaler events that might indicate resource unavailability:
    
    
    resource.type="k8s_cluster"
    resource.labels.location="LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
    log_id("container.googleapis.com/cluster-autoscaler-visibility")
    jsonPayload.noScaleUpReason.messageId="no.scale.up.nap.resource.exhausted"
    

**Option 2: Check MIG errors**

You can check for MIG errors in the Google Cloud console or by using a Cloud Logging query.

  * **Using Google Cloud console** :

    1. In the Google Cloud console, go to **Compute Engine** > **Instance groups**.
    2. Find the MIG corresponding to the node pool that is failing to scale up.
    3. Click the MIG name and go to the **Errors** tab. Look for messages indicating resource exhaustion.
  * **Using Cloud Logging query** :

    1. In the Google Cloud console, go to **Cloud Logging > Logs explorer**.
    2. Run the following query to check for resource exhaustion errors from the MIG:
    
    resource.type="gce_instance"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.status.message:("ZONE_RESOURCE_POOL_EXHAUSTED" OR "does not have enough resources available to fulfill the request" OR "resource pool exhausted" OR "does not exist in zone")
    




#### Evaluate the result

  * **Resources are available:** if logs don't show the `ZONE_RESOURCE_POOL_EXHAUSTED` messages, resource unavailability is unlikely to be the cause of scale-up failure.
  * **Resources are not available:**

    * **Interpretation:** node provisioning fails due to a temporary high demand for a specific machine type (especially Spot VMs or GPUs) in that zone, or because a Pod is constrained by PersistentVolume affinity to a zone that's experiencing resource unavailability.
    * **Resolution:** Resource unavailability is transient, but you can improve resilience by adding flexibility to your configuration:

      * **Diversify machine types** : ensure the `spec.priorities` field in the custom ComputeClass contains multiple machine types or families as fallbacks:
            
            spec:
              priorities:
              - machineFamily: c3  # Highest priority
              - machineFamily: n2d # Fallback option
              - machineFamily: e2  # Lowest priority
            

      * **Use regional clusters** : if the cluster is zonal, it is vulnerable to resource unavailability in that single zone. Using regional clusters lets the cluster autoscaler attempt to provision nodes in other zones within the region where capacity might be available.

      * **Use Compute Engine reservations** : for critical workloads that cannot tolerate delays, [create Compute Engine reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to help ensure capacity for specific machine types.




### Verify project quotas

Confirm that your project has sufficient quota for the resources, such as CPUs, GPUs, and IP addresses required by the new nodes.

  1. Check autoscaler logs for quota errors. Use Cloud Logging to search for quota-related error messages in the autoscaler visibility events:
         
         resource.type="k8s_cluster"
         resource.labels.location="LOCATION"
         resource.labels.cluster_name="CLUSTER_NAME"
         log_id("container.googleapis.com/cluster-autoscaler-visibility")
         jsonPayload.noScaleUpReason.messageId="no.scale.up.nap.quota.exceeded"
         

Alternatively, use the following Cloud Logging query to check logs for quota-related errors from the MIG:
         
         resource.type="gce_instance"
         protoPayload.methodName:"compute.instances.insert"
         protoPayload.status.message:"QUOTA_EXCEEDED"
         severity=ERROR
         

  2. Review quotas in Google Cloud console:

     1. In the Google Cloud console, go to **IAM & Admin > Quotas**.
     2. Filter for the **Compute Engine API** service.
     3. Check the usage for relevant metrics like CPUs, GPUs (all types), and in-use IP addresses for the region your GKE cluster is in. Verify that current usage is not at the limit.



#### Evaluate the result

  * **Quota below limits:** if quota usage is below the quota limits and no `QUOTA_EXCEEDED` errors are found in the logs, quota limits won't block scale-up.
  * **Quota exceeded:**
    * **Interpretation:** node provisioning fails due to insufficient quota for resources like CPUs, GPUs, IP addresses, or MIGs.
    * **Resolution:** if your project has reached a quota limit, [request a quota increase](https://docs.cloud.google.com/docs/quota_detail/view_manage#requesting_higher_quota).



## Advanced configurations

Configurations such as GPUs, Spot VMs, and Compute Engine reservations have their own specific requirements and potential points of failure that need to be checked.

### Verify GPU configuration

For custom ComputeClasses that provision GPU nodes, validate the GPU configuration in the custom ComputeClass and ensure the Pod has the mandatory `nvidia.com/gpu` toleration.

  1. Check the custom ComputeClass's YAML for a `gpu` block within a priority rule:
         
         kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
         

The `gpu` block should specify a `type` field and `count` field, for example:
         
         priorities:
         - machineType: a2-highgpu-1g
           **gpu :
             type: nvidia-tesla-a100
             count: 1**
         

  2. Inspect the Pod for GPU toleration. Any Pod that needs to be scheduled on a GPU node _must_ have the `nvidia.com/gpu` toleration, even if the Pod doesn't request a GPU itself.
         
         kubectl get pod POD_NAME -n NAMESPACE -o jsonpath='{.spec.tolerations}'
         

Check for the toleration under `spec.tolerations` field.




#### Evaluate the result

  * **GPU configured correctly:** if the ComputeClass defines GPU `type` and `count`, and Pods include the `nvidia.com/gpu` toleration, the GPU configuration is correct. Following shows the required toleration:
        
        tolerations:
        **- key: "nvidia.com/gpu"
          operator: "Exists"
          effect: "NoSchedule"**
        

  * **GPU misconfigured:**

    * **Interpretation:** the Pod might be missing the required `nvidia.com/gpu` toleration, the ComputeClass might be unhealthy due to GPU field mismatches, or the GKE version might not handle GPU configuration correctly.
    * **Resolution:** perform one of the following actions: 
      * Modify the workload's YAML file to include the mandatory GPU toleration and re-apply the YAML file.
      * Upgrade the GKE cluster. If the custom ComputeClass is unhealthy and the issue is related to GPU fields, check for known issues and upgrade to a patched GKE version, for example, 1.31.8-gke.1045000 or later.



### Verify Spot VMs configuration

If you use Spot VMs, ensure that `spot: true` setting is in the correct priority rules in your ComputeClass manifest. Also, ensure that you understand the cluster autoscaler's pricing logic.

Inspect the ComputeClass manifest:
    
    
    kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
    

In the output, look for `spot: true` in `spec.priorities` field, for example:
    
    
    priorities:
    - machineFamily: n2d
      **spot : true**
    

The cluster autoscaler might use pricing data from `us-central1` as a baseline when comparing the cost of different Spot VMs types, which can lead to seemingly non-optimal choices in other regions. This is a known behavior.

#### Evaluate the result

  * **Spot VMs configured correctly:** if the `spot: true` field is specified and cluster autoscaler provisions Spot VMs, the configuration works as expected.
  * **Spot VMs failing to schedule:**

    * **Interpretation:** Pods requiring Spot VMs might be failing to schedule on Spot VMs due to resource unavailability in the target zone, or because the cluster autoscaler might be choosing a different VM type based on its `us-central1` pricing model.
    * **Resolution:**

      * If you suspect resource unavailability, see Check for resource unavailability.
      * To control the selection of Spot VMs, explicitly list `machineType` entries in your `priorities` field from cheapest to most expensive for your region. This approach gives you direct control over the fallback order. For example:
            
            spec:
              priorities:
              - machineType: t2d-standard-48 # Cheapest in this region
                spot: true
              - machineType: n2d-standard-48 # Fallback Spot option
                spot: true
              - machineType: n2d-standard-48 # On-demand fallback
                spot: false
            




## General cluster autoscaler health

This section helps you check for issues that might not be directly related to the custom ComputeClass configuration but might be affecting its operation.

### Check for concurrent operations

Verify that no other cluster or node pool operations are in progress concurrently. GKE has limits on concurrent operations, which can block autoscaling.

List ongoing operations that are not in a `DONE` state:
    
    
    gcloud container operations list \
        --location=LOCATION \
        --filter='targetLink~"/clusters/CLUSTER_NAME" AND status!=DONE'
    

If the command returns any operations, an action like a cluster upgrade, node pool creation, or another modification might be in progress. Autoscaling events might be blocked until this operation completes.

#### Evaluate the result

  * **No concurrent operations:** if the `list` command returns an empty list, cluster autoscaler is not blocked by any operations.
  * **Concurrent operations found:**

    * **Interpretation:** if the command lists operations with status `RUNNING` or `PENDING`, a concurrent operation, such as a cluster upgrade or node pool modification, might be in progress and blocking autoscaling.
    * **Resolution:** wait for the ongoing operation to complete. You can monitor the status using an operation ID by using:
          
          gcloud container operations wait OPERATION_ID --location LOCATION
          

Replace `OPERATION_ID` with the ID from the `list` command's output. After the blocking operation completes, cluster autoscaler should resume normal function.




### Review active migration

If you observe workloads staying on lower-priority nodes when higher-priority nodes are available, verify whether active migration is enabled. If the `activeMigration.optimizeRulePriority` field is set to `false` or omitted in your ComputeClass, GKE won't automatically move workloads to higher-priority nodes when they become available.

  1. To check Pod tolerations, review `spec.tolerations` field. If the Pod has tolerations that match taints on multiple node pools of different priorities, the scheduler might place it on a lower-priority node if it's available first.
         
         kubectl get pod POD_NAME -n NAMESPACE -o jsonpath='{.spec.tolerations[*]}{"\n"}'
         

  2. To check if active migration is enabled, inspect the ComputeClass manifest for the `spec.activeMigration.optimizeRulePriority` field.
         
         kubectl get computeclass CUSTOM_COMPUTECLASS_NAME -o yaml
         




#### Evaluate the result

  * **Active migration enabled:** if the `activeMigration.optimizeRulePriority` field is `true`, GKE attempts to move workloads to higher-priority nodes when they become available.
  * **Active migration disabled or ineffective:**

    * **Interpretation:** if `activeMigration.optimizeRulePriority` field is `false` or omitted, or if Pod tolerations are too broad, workloads stay on lower-priority nodes when higher-priority nodes are available. This approach allows workloads to be scheduled on lower-priority nodes that become available first.
    * **Resolution:** if you want workloads to move to higher-priority nodes, perform one of the following actions:

      * Use more specific scheduling constraints like `nodeAffinity` to prefer higher-priority node pools.
      * Edit the ComputeClass manifest to set `activeMigration.optimizeRulePriority: true` and apply the YAML file:
            
            spec:
              activeMigration:
                **optimizeRulePriority : true**
            




## Get support

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



## What's next

  * [Read best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses)
  * [Apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes)
  * [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints)
  * [Troubleshoot cluster autoscaler scale-up issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
