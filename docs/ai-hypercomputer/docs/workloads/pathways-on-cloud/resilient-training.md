---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training/
title: Resilient training with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:05.040155+00:00
---

# Resilient training with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Resilient training with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Pathways provides resiliency benefits in the following ways:

  * **Suspend-Resume** : tolerance in face of planned interruptions like preemption notices without needing the user to write any custom preemption handling code.
  * **Elastic Training** : tolerance in face of unplanned hardware failures without causing the client to crash but requiring users to write model specific recovery code.



## Before you begin

Make sure you have:

  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Installed the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Enabled the GKE API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Suspend-resume

Typically, GKE sends a preemption notice to an accelerator pod, before the pod is preempted. Pathways preemption tolerance is enabled by default on all cloud deployments and Pathways accelerator jobs listen for these notices.

When a preemption notice arrives, Pathways first determines whether the current workload is restorable - whether Pathways can transparently save and restore the workload. If so, then it attempts to transparently suspend your ML workload by writing out its current state to persistent storage such as Cloud Storage before GKE evicts your accelerator jobs. When GKE reschedules your jobs later, Pathways resumes your ML workload by reading back its persisted state.

If the workload is not restorable, Pathways shuts down the accelerator job and forwards the failure to your job if Elastic training is configured. If Elastic training is not configured, GKE restarts the entire workload based on the JobSet restart policy.

Typical ML workloads defined using JAX rely on stateless Pathways XLA components which are restorable using a high bandwidth memory (HBM) snapshot. Certain ML workloads such as those defined using the [JAX colocated python API](https://github.com/jax-ml/jax/blob/main/jax/experimental/colocated_python/api.py) rely on stateful Pathways components; these are not restorable.

## Elastic training

Elastic training allows your training job to continue even when hardware failures occur. This is achieved through a combination of Pathways system capabilities and user-defined model recovery logic:

  * **Detection of failure** : When a hardware failure happens (for example, a TPU worker crashes), the Pathways system detects this and notifies the user's training job through an exception the next time data that was located on that hardware is accessed. This notification doesn't crash your workload; it allows your code to handle the notification and reconfigure your resources to either continue processing or exit gracefully.
  * **User-defined elasticity handler** : User's model code needs to be able to handle this exception. This is what makes it "model-specific recovery". 
    * **Snapshotting** : The most common approach is to periodically save snapshots of your model's state. When a failure occurs, you can load from the most recent snapshot to resume training.
    * **Reconfiguration** : You will likely need to reconfigure your training job to adjust for the number of available slices. For example, if one slice stops working, you might reduce the number of active slices by one until a replacement is available. For more information, see Elastic Handler.
    * **Data/Computation graph updates** : Your code needs to handle any changes in the number of devices available to your computation by re-creating the computation graph as needed. This might involve re-partitioning data or re-compiling your model.
  * **Pathways' role in recovery** : Pathways provides the primitives to support user defined reconfiguration: 
    * **Slice replacement** : If a failed slice is replaced, the client can be informed once the new slice is available. Your code can then reconfigure to use this new slice.
    * **Transparent recovery** : Pathways handles the lower-level details of the recovery, like re-establishing connections to the healthy portions of the cluster.
  * **Utilities in pathwaysutils** : A set of Pathways utilities defined in [pathways-utils](https://github.com/AI-Hypercomputer/pathways-utils).



### Implement an elastic handler

Most of the code you will have to write will be in a user-defined elastic handler. This handler reacts to elastic events (such as a TPU slice becoming unavailable) by re-creating the mesh and reinitializing the training loop.

Each workload is unique. The complexity of the elastic handler may scale with the complexity of the workload. The inputs and outputs of the handler should be the minimum arguments and return values needed to reinitialize the train loop.
    
    
    def elastic_handler(elastic_utils, *args, **kwargs):
      mesh = initialize_mesh(**kwargs["mesh_kwargs"])
      initial_state, initial_step, jitted_train_step, other_variables =
          initialize_training_loop(mesh, **kwargs["initialize_training_loop_kwargs"])
    
      step, snapshot = elastic_utils.get_next_snapshot()
      state = initial_state.replace(**snapshot)
    
      return state, step, mesh, jitted_train_step, other_variables
    

### Update your training loop

You need to make the following changes to your training loop:

  1. Create an elastic manager
  2. Wrap your training loop inside a try-except blocks that handles `jax.errors.JaxRuntimeError`s
  3. Within your `jax.errors.JaxRuntimeError` handler, call `maybe_reshard_down`. The elastic manager will reshard down if the error is related to an elastic event or otherwise reraise it.
  4. Call `maybe_snapshot` and `maybe_reshard_up` at the end of the training loop


    
    
    import pathwaysutils
    from pathwaysutils.elastic import manager
    
    pathwaysutils.initialize()
    
    def initialize_mesh(**kwargs):
      ...
    
    
    def initialize_training_loop(**kwargs):
      ...
    
    
    def train_loop(
        final_step,
        elastic_manager,
        mesh_kwargs,
        initialize_training_loop_kwargs,
    ):
      mesh = initialize_mesh(**mesh_kwargs)
      initial_state, initial_step, jitted_train_step, other_variables =
          initialize_training_loop(mesh, **initialize_training_loop_kwargs)
    
      step = initial_step
      while step < final_step:
        try:
          state = jitted_train_step(state)
    
          elastic_manager.maybe_snapshot(step=step, snapshot=state)
          handler_returns = elastic_manager.maybe_reshard_up(
              step=step,
              snapshot=state,
              elastic_handler=elastic_handler,
              handler_args=(),
              handler_kwargs=dict(
                  mesh_kwargs=mesh_kwargs,
                  initialize_training_loop_kwargs=initialize_training_loop_kwargs,
              ),
          )
          if handler_returns:
            state, step, mesh, jitted_train_step, other_variables = handler_returns
          step += 1
        except jax.errors.JaxRuntimeError as error:
          handler_returns = elastic_manager.maybe_reshard_down(
              error=error,
              elastic_handler=elastic_handler,
              handler_args=(),
              handler_kwargs=dict(
                  mesh_kwargs=mesh_kwargs,
                  initialize_training_loop_kwargs=initialize_training_loop_kwargs,
              ),
          )
          if handler_returns:
            state, step, mesh, jitted_train_step, other_variables = handler_returns
    
      return state
    
    
    def main():
      elastic_manager = manager.Manager(
          devices=jax.devices(),
          snapshot_period=10,
          snapshot_buffer_size=1,
          reshard_check_period=5,
          max_elastic_down_event_count=10,
          max_reshard_retry_count=3,
      )
    
      train_loop(100, elastic_manager, {}, {})
    

### Configure the elastic manager

The elastic manager can be configured in a few different ways. The frequency of snapshotting is determined by the snapshot period. The snapshot period effects the average number of steps lost due to an elastic event. The reshard check period determines how often your training loop will poll for slice availability. The `max_elastic_down_event_count` lets you set the number of elastic events due to slice loss your training loop will support. The `max_reshard_retry_count` specifies the number of times the elastic manager should retry resharding. The manager is a singleton object and should be created only once.

### Snapshots

Based on the elastic manager configuration, the function may snapshot data onto host memory that will be available to use by your elastic handler during an elastic event.

### Reduce sharding

After catching a `jax.errors.JaxRuntimeError`, Pathways will check if the error is due to an elastic event due to a lost slice. If so, it will call the elastic handler in a loop until success or the maximum retry attempts. If the error is not due to an elastic event, the error will be raised again. The return values of the elastic handler are passed through to the caller.

### Increase sharding

Based on the elastic manager configuration and if there are unavailable slices, Pathways will check if additional slices have become available. If so, it will immediately save a snapshot (if a pre-existing snapshot for the current step was not already taken) and call the elastic handler in a loop until success or the maximum number of retry attempts is reached. If re-sharding occurs, the return values of the elastic handler are passed through to the caller. Otherwise, `None` is returned.

## Hot-swap

Hot-Swap refers to a feature of the GKE JobSet API where a higher-priority job can quickly take over resources from a lower-priority job, minimizing downtime and ensuring faster recovery.

When a JobSet is created, GKE schedules the workload across multiple slices, as specified in the JobSet configuration. If a hardware failure occurs on one or more slices, the affected Pods are marked as failed. When rescheduling this Jobset, if you have elected to keep a spare slice in your GKE cluster which could be utilized for a lower priority Job, the JobSet system will remap the workload of the failed slice of the higher-priority job onto the spare slice being utilized by the lower priority job within the same GKE cluster. This remapping typically takes less than a minute.

Upon JobSet restart, hot-swap can occur in the following situations:

  1. **Default Mode** : If spare, idle TPU slices are available within the same cluster, the Kubernetes scheduler will prioritize scheduling the restarted jobs onto these slices rather than waiting for the failed slices to be repaired. This provides faster recovery.
  2. **Heterogeneous Workloads** : In clusters running multiple workloads with a configured Kubernetes PriorityClass, a restarted JobSet can trigger a hot swap. If the restarted job's affinity matches a lower-priority job's resources, Kubernetes preempts the lower-priority job, allowing the higher-priority job to start immediately. For example, you can configure your Pathways worker pods with different priorities using `PriorityClass`.



To use priorities in your cluster, define a priority class, for example:
    
    
    kind: PriorityClass
    metadata:
      name: high-prior-job
    value: 2000
    globalDefault: false
    description: "This priority class should be used for high priority job."
    

Apply this YAML to your GKE cluster:
    
    
    kubectl apply -f high-prior-job.yaml
    

Next, attach the new priority class to your Pathways worker job by adding the following text to the podspec of your `pathways-worker` Pod.
    
    
    priorityClassName: high-prior-job
    

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
