---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning/
title: Provision extra compute capacity for rapid Pod scaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:36.528791+00:00
---

# Provision extra compute capacity for rapid Pod scaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provision extra compute capacity for rapid Pod scaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to reserve extra compute capacity in your Google Kubernetes Engine (GKE) clusters so that your workloads can rapidly scale up during high traffic events without waiting for new nodes to start. You can use these instructions to reserve compute overhead on a consistently available basis, or in advance of specific events.

**Note:** GKE also features **capacity buffers** ([Preview](https://cloud.google.com/products?e=0#preview)), which provides an automated way to manage spare capacity. For more information, see [About capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).

## Why spare capacity provisioning is useful

GKE Autopilot clusters and Standard clusters with node auto-provisioning create new nodes when there are no existing nodes with the capacity to run new Pods. Each new node takes approximately 80 to 120 seconds to boot. GKE waits until the node has started before placing pending Pods on the new node, after which the Pods can boot. In Standard clusters, you can alternatively create a new node pool manually that has the extra capacity that you need to run new Pods. This page applies to clusters that use a node autoscaling mechanism such as Autopilot or node auto-provisioning.

In some cases, you might want your Pods to boot faster during scale-up events. For example, if you're launching a new expansion for your popular live-service multiplayer game, the faster boot times for your game server Pods might reduce queue times for players logging in on launch day. As another example, if you run an ecommerce platform and you're planning on a flash sale for a limited time, you expect bursts of traffic for the duration of the sale.

Spare capacity provisioning is compatible with _Pod bursting_ , which lets Pods temporarily use resources that were requested by other Pods on the node, if that capacity is available and unused by other Pods. To use bursting, set your resource limits higher than your resource requests or don't set resource limits. For details, see [Configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).

## How spare capacity provisioning works in GKE

To provision spare capacity, you can use [Kubernetes _PriorityClasses_](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) and placeholder Pods. A PriorityClass lets you tell GKE that some workloads are a lower priority than other workloads. You can deploy placeholder Pods that use a low priority PriorityClass and request the compute capacity that you need to reserve. GKE adds capacity to the cluster by creating new nodes to accommodate the placeholder Pods.

When your production workloads scale up, GKE evicts the lower-priority placeholder Pods and schedules the new replicas of your production Pods (which use a higher priority PriorityClass) in their place. If you have multiple low-priority Pods that have different priority levels, GKE evicts the lowest priority Pods first.

When a placeholder Pod is evicted, it returns to the _Pending_ state. If you're using a Deployment for consistent provisioning, the Deployment controller immediately attempts to re-create the Pod. If a placeholder Pod has a priority of -10, it will trigger cluster autoscaling to create a new node (if necessary) to replace the reserved capacity that you just used. This cycle helps to ensure that your cluster always maintains the specified amount of spare capacity.

### Capacity provisioning methods

Depending on your use case, you can provision extra capacity in your GKE clusters in one of the following ways:

  * **Consistent capacity provisioning** : Use a Deployment to create a specific number of low priority placeholder Pods that constantly run in the cluster. When GKE evicts these Pods to run your production workloads, the Deployment controller helps ensure that GKE provisions more capacity to recreate the evicted low priority Pods. This method provides consistent capacity overhead across multiple scale-up and scale-down events, until you delete the Deployment.
  * **Single use capacity provisioning** : Use a Job to run a specific number of low priority parallel placeholder Pods for a specific period of time. When that time has passed or when GKE evicts all the Job replicas, the reserved capacity stops being available. This method provides a specific amount of available capacity for a specific period.



## Pricing

In GKE Autopilot, you're charged for the resource requests of your running Pods, including the low priority workloads that you deploy. For details, see [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

In GKE Standard, you're charged for the underlying Compute Engine VMs that GKE provisions, regardless of whether Pods use that capacity. For details, see [Standard pricing](https://cloud.google.com/kubernetes-engine/pricing#standard_mode)

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a [GKE Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#create_an_autopilot_cluster), or a GKE Standard cluster with node auto-provisioning enabled.
  * Read the Considerations for capacity provisioning to ensure that you choose appropriate values in your capacity requests.



## Create a PriorityClass

To use either of the methods described in Capacity provisioning methods, you first need to create the following PriorityClasses:

  * **Default PriorityClass** : A global default PriorityClass that's assigned to any Pod that doesn't explicitly set a different PriorityClass in the Pod specification. Pods with this default PriorityClass can evict Pods that use a lower PriorityClass.
  * **Low PriorityClass** : A non-default PriorityClass set to the lowest priority possible in GKE. Pods with this PriorityClass can be evicted to run Pods with higher PriorityClasses.


  1. Save the following manifest as `priorityclasses.yaml`:
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: low-priority
         value: -10
         preemptionPolicy: Never
         globalDefault: false
         description: "Low priority workloads"
         ---
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: default-priority
         value: 0
         preemptionPolicy: PreemptLowerPriority
         globalDefault: true
         description: "The global default priority."
         

This manifest includes the following fields:

     * `preemptionPolicy`: Specifies whether or not Pods using a PriorityClass can evict lower priority Pods. The `low-priority` PriorityClass uses `Never`, and the `default` PriorityClass uses `PreemptLowerPriority`.
     * `value`: The priority for Pods that use the PriorityClass. In GKE clusters, cluster autoscaling uses a default expendable priority cutoff of -10. With a priority of -10 or higher, Pods can trigger the creation of new nodes if no capacity is available. With a priority less than -10, Pods don't trigger cluster autoscaling and therefore new nodes aren't provisioned. If no capacity exists, Pods remain in a Pending state.

For help deciding on appropriate values for priority, see Choose a priority.

     * `globalDefault`: Specifies whether or not GKE assigns the PriorityClass to Pods that don't explicitly set a PriorityClass in the Pod specification. The `low-priority` PriorityClass uses `false`, and the `default` PriorityClass uses `true`.

  2. Apply the manifest:
         
         kubectl apply -f priorityclasses.yaml
         




## Provision extra compute capacity

The following sections show an example in which you provision capacity for a single event or consistently over time.

### Use a Deployment for consistent capacity provisioning

  1. Save the following manifest as `capacity-res-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: capacity-res-deploy
         spec:
           replicas: 10
           selector:
             matchLabels:
               app: reservation
           template:
             metadata:
               labels:
                 app: reservation
             spec:
               priorityClassName: low-priority
               terminationGracePeriodSeconds: 0
               containers:
               - name: ubuntu
                 image: ubuntu
                 command: ["sleep"]
                 args: ["infinity"]
                 resources:
                   requests:
                     cpu: 500m
                     memory: 500Mi
         

This manifest includes the following fields:

     * `spec.replicas`: Change this value to meet your requirements.
     * `spec.resources.requests`: Change the CPU and memory requests to meet your requirements. Use the guidance in Choose capacity sizing to help you decide on appropriate request values.
     * `spec.containers.command` and `spec.containers.args`: Tell the Pods to remain active until evicted by GKE.
  2. Apply the manifest:
         
         kubectl apply -f capacity-res-deployment.yaml
         

  3. Get the Pod status:
         
         kubectl get pods -l app=reservation
         

Wait until all the replicas have a status of `Running`.




### Use a Job for single event capacity provisioning

  1. Save the following manifest as `capacity-res-job.yaml`:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: capacity-res-job
         spec:
           parallelism: 4
           backoffLimit: 0
           template:
             spec:
               priorityClassName: low-priority
               terminationGracePeriodSeconds: 0
               containers:
               - name: ubuntu-container
                 image: ubuntu
                 **command : ["sleep"]
                 args: ["36000"]
                 resources:
                   requests:
                     cpu: "16"**
               restartPolicy: Never
         

This manifest includes the following fields:

     * `spec.parallelism`: Change to the number of Jobs you want to run in parallel to reserve capacity.
     * `spec.backoffLimit: 0`: Prevent the Job controller from recreating evicted Jobs.
     * `template.spec.resources.requests`: Change the CPU and memory requests to meet your requirements. Use the guidance in Considerations to help you decide on appropriate values.
     * `template.spec.containers.command` and `template.spec.containers.args`: Tell the Jobs to remain active for the period of time, in seconds, during which you need the extra capacity.
  2. Apply the manifest:
         
         kubectl apply -f capacity-res-job.yaml
         

  3. Get the Job status:
         
         kubectl get jobs
         

Wait until all the Jobs have a status of `Running`.




## Test the capacity provisioning and eviction

To verify that capacity provisioning works as expected, do the following:

  1. In your terminal, watch the status of the capacity provisioning workloads:

     1. For Deployments, run the following command:
            
            kubectl get pods --label=app=reservation -w
            

     2. For Jobs, run the following command:
            
            kubectl get Jobs -w
            

  2. Open a new terminal window and do the following:

     1. Save the following manifest as `test-deployment.yaml`:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: helloweb
              labels:
                app: hello
            spec:
              replicas: 5
              selector:
                matchLabels:
                  app: hello
                  tier: web
              template:
                metadata:
                  labels:
                    app: hello
                    tier: web
                spec:
                  containers:
                  - name: hello-app
                    image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                    ports:
                    - containerPort: 8080
                    resources:
                      requests:
                        cpu: 400m
                        memory: 400Mi
            

     2. Apply the manifest:
            
            kubectl apply -f test-deployment.yaml
            

  3. In the original terminal window, note that GKE terminates some of the capacity provisioning workloads to schedule your new replicas, similar to the following example:
         
         NAME                                         READY   STATUS    RESTARTS   AGE
         capacity-res-deploy-6bd9b54ffc-5p6wc         1/1     Running   0          7m25s
         capacity-res-deploy-6bd9b54ffc-9tjbt         1/1     Running   0          7m26s
         capacity-res-deploy-6bd9b54ffc-kvqr8         1/1     Running   0          2m32s
         capacity-res-deploy-6bd9b54ffc-n7zn4         1/1     Running   0          2m33s
         capacity-res-deploy-6bd9b54ffc-pgw2n         1/1     Running   0          2m32s
         capacity-res-deploy-6bd9b54ffc-t5t57         1/1     Running   0          2m32s
         capacity-res-deploy-6bd9b54ffc-v4f5f         1/1     Running   0          7m24s
         helloweb-85df88c986-zmk4f                    0/1     Pending   0          0s
         helloweb-85df88c986-lllbd                    0/1     Pending   0          0s
         helloweb-85df88c986-bw7x4                    0/1     Pending   0          0s
         helloweb-85df88c986-gh8q8                    0/1     Pending   0          0s
         helloweb-85df88c986-74jrl                    0/1     Pending   0          0s
         capacity-res-deploy-6bd9b54ffc-v6dtk   1/1     Terminating   0          2m47s
         capacity-res-deploy-6bd9b54ffc-kvqr8   1/1     Terminating   0          2m47s
         capacity-res-deploy-6bd9b54ffc-pgw2n   1/1     Terminating   0          2m47s
         capacity-res-deploy-6bd9b54ffc-n7zn4   1/1     Terminating   0          2m48s
         capacity-res-deploy-6bd9b54ffc-2f8kx   1/1     Terminating   0          2m48s
         ...
         helloweb-85df88c986-lllbd              0/1     Pending       0          1s
         helloweb-85df88c986-gh8q8              0/1     Pending       0          1s
         helloweb-85df88c986-74jrl              0/1     Pending       0          1s
         helloweb-85df88c986-zmk4f              0/1     Pending       0          1s
         helloweb-85df88c986-bw7x4              0/1     Pending       0          1s
         helloweb-85df88c986-gh8q8              0/1     ContainerCreating   0          1s
         helloweb-85df88c986-zmk4f              0/1     ContainerCreating   0          1s
         helloweb-85df88c986-bw7x4              0/1     ContainerCreating   0          1s
         helloweb-85df88c986-lllbd              0/1     ContainerCreating   0          1s
         helloweb-85df88c986-74jrl              0/1     ContainerCreating   0          1s
         helloweb-85df88c986-zmk4f              1/1     Running             0          4s
         helloweb-85df88c986-lllbd              1/1     Running             0          4s
         helloweb-85df88c986-74jrl              1/1     Running             0          5s
         helloweb-85df88c986-gh8q8              1/1     Running             0          5s
         helloweb-85df88c986-bw7x4              1/1     Running             0          5s
         

This output shows that your new Deployment took five seconds to change from Pending to Running.




## Considerations for capacity provisioning

The following sections provide recommendations that might help you to improve the reliability of capacity that you provision.

### Consistent capacity provisioning

  * Evaluate how many placeholder Pod replicas you need and the size of the requests in each replica. The low priority replicas should request _at least_ the same capacity as your largest production workload, so that those workloads can fit in the capacity reserved by your low priority workload.
  * If you operate large numbers of production workloads at scale, consider setting the resource requests of your placeholder Pods to values that provision enough capacity to run multiple production workloads instead of just one.



### Single use capacity provisioning

  * Set the length of time for the placeholder Jobs to persist to the time during which you need additional capacity. For example, if you want the additional capacity for a 24 hour game launch day, set the length of time to 86400 seconds. This helps ensure that the provisioned capacity doesn't last longer than you need it.
  * Set a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window) for the same period of time that you're reserving the capacity. This prevents your low priority Jobs from being evicted during a node upgrade. Setting a maintenance window is also a good practice when you're anticipating high demand for your workload.
  * If you operate large numbers of production workloads at scale, consider setting the resource requests of your placeholder Jobs to values that provision enough capacity to run multiple production workloads instead of just one.



Capacity is only provisioned for a single scaling event. If you scale up and use the capacity, then scale down, that capacity is no longer available for another scale-up event. If you anticipate multiple scale-up and scale-down events, use the consistent capacity reservation method and adjust the size of the reservation as needed. For example, making the Pod requests larger ahead of an event, and lower or zero after.

### Choose a priority

You can define multiple PriorityClasses in your cluster to use with workloads that have different requirements. For example, you could create a PriorityClass with a -10 priority for single-use capacity provisioning and a PriorityClass with a -9 priority for consistent capacity provisioning. You could then provision consistent capacity using the PriorityClass with -9 priority and, when you want more capacity for a special event, you could deploy new Jobs that use the PriorityClass with -10 priority. GKE evicts the lowest priority workloads first.

**Caution:** In Standard clusters with node auto-provisioning, if you deploy workloads with a priority less than -10, GKE won't create new nodes to run the workloads.

You can also use other PriorityClasses to run low priority non-production workloads that perform actual tasks, such as fault-tolerant batch workloads, at a priority that's lower than your production workloads but higher than your placeholder Pods. For example, -5.

### Choose capacity sizing

Set replica counts and resource requests of your placeholder workload to greater than or equal to the capacity that your production workloads might need when scaling up.

The total capacity provisioned is based on the number of placeholder Pods that you deploy and the resource requests of each replica. If your scale-up requires more capacity than GKE provisioned for your placeholder Pods, some of your production workloads remain in `Pending` until GKE can provision more capacity.

## What's next

  * [Learn how to separate your workloads from each other](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation)
  * [Learn how to optimize autoscaling your workloads based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
