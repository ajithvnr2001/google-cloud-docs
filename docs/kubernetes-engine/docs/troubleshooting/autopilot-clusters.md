---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters/
title: Troubleshooting Autopilot clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:05.726695+00:00
---

# Troubleshooting Autopilot clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting Autopilot clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

Problems with your Google Kubernetes Engine (GKE) [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) can affect your application's availability and operational efficiency. These issues can disrupt the entire lifecycle of your applications, from initial deployment to scaling under load.

Use this page to diagnose and resolve common issues specific to Autopilot clusters. Find guidance on troubleshooting cluster creation issues that prevent your cluster from provisioning, scaling issues such as `out of resources` errors, and workload-specific issues such as ephemeral storage errors or Pods stuck in the `Pending` state.

This information is important for Application developers who need to ensure their applications deploy and run smoothly, and for Platform admins and operators who are responsible for the overall health and resource management of Autopilot clusters. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Cluster issues

### Cannot create a cluster: 0 nodes registered

The following issue occurs when you try to create an Autopilot cluster with an IAM service account that's disabled or doesn't have the required permissions. Cluster creation fails with the following error message:
    
    
    All cluster resources were brought up, but: only 0 nodes out of 2 have registered.
    

To resolve the issue, do the following:

  1. Check whether the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or the custom IAM service account that you want to use is disabled:
         
         gcloud iam service-accounts describe SERVICE_ACCOUNT
         

Replace `SERVICE_ACCOUNT` with service account email address, such as `my-iam-account@my-first-project.iam.gserviceaccount.com`.

If the service account is disabled, the output is similar to the following:
         
         **disabled: true**
         displayName: my-service-account
         email: my-service-account@my-project.iam.gserviceaccount.com
         ...
         

  2. If the service account is disabled, enable it:
         
         gcloud iam service-accounts enable SERVICE_ACCOUNT
         




If the service account is enabled and the error persists, grant the service account the minimum permissions required for GKE:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT" \
        --role roles/container.defaultNodeServiceAccount
    

### Namespace stuck in the Terminating state when cluster has 0 nodes

The following issue occurs when you delete a namespace in a cluster after the cluster scales down to zero nodes. The `metrics-server` component can't accept the namespace deletion request because the component has zero replicas.

To diagnose this issue, run the following command:
    
    
    kubectl describe ns/NAMESPACE_NAME
    

Replace `NAMESPACE_NAME` with the name of the namespace.

The output is the following:
    
    
    Discovery failed for some groups, 1 failing: unable to retrieve the complete
    list of server APIs: metrics.k8s.io/v1beta1: the server is currently unable to
    handle the request
    

To resolve this issue, scale any workload up to trigger GKE to create a new node. When the node is ready, the namespace deletion request automatically completes. After GKE deletes the namespace, scale the workload back down.

## Scaling issues

### Node scale up failed: Pod is at risk of not being scheduled

The following issue occurs when serial port logging is disabled in your Google Cloud project. GKE Autopilot clusters require serial port logging to effectively debug node issues. If serial port logging is disabled, Autopilot can't provision nodes to run your workloads.

The error message in your Kubernetes event log is similar to the following:
    
    
    LAST SEEN   TYPE      REASON          OBJECT                          MESSAGE
    12s         Warning   FailedScaleUp   pod/pod-test-5b97f7c978-h9lvl   Node scale up in zones associated with this pod failed: Internal error. Pod is at risk of not being scheduled
    

Serial port logging might be disabled at the organization level through an organization policy that enforces the `compute.disableSerialPortLogging` constraint. Serial port logging could also be disabled at the project or virtual machine (VM) instance level.

To resolve this issue, do the following:

  1. Ask your Google Cloud organization policy administrator to [remove the `compute.disableSerialPortLogging` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) in the project with your Autopilot cluster.
  2. If you don't have an organization policy that enforces this constraint, try to [enable serial port logging in your project metadata](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#setting_project_and_instance_metadata). This action requires the [`compute.projects.setCommonInstanceMetadata` IAM permission](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/setCommonInstanceMetadata#iam-permissions).



### Node scale up failed: Compute Engine out of resources

The following issue occurs when your workloads request more resources than are available to use in that Compute Engine region or zone. Your Pods might remain in the `Pending` state.

  * Check your Pod events:
        
        kubectl events --for='pod/POD_NAME' --types=Warning
        

Replace `RESOURCE_NAME` with the name of the pending Kubernetes resource. For example `pod/example-pod`.

The output is similar to the following:
        
        LAST SEEN         TYPE            REASON                  OBJECT                   Message
        19m               Warning         FailedScheduling        pod/example-pod          gke.io/optimize-utilization-scheduler  0/2 nodes are available: 2 node(s) didn't match Pod's node affinity/selector. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
        14m               Warning         FailedScheduling        pod/example-pod          gke.io/optimize-utilization-scheduler  0/2 nodes are available: 2 node(s) didn't match Pod's node affinity/selector. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
        **12m (x2 over 18m) Warning         FailedScaleUp           cluster-autoscaler       Node scale up in zones us-central1-f associated with this pod failed: GCE out of resources. Pod is at risk of not being scheduled.**
        **34s (x3 over 17m) Warning         FailedScaleUp           cluster-autoscaler       Node scale up in zones us-central1-b associated with this pod failed: GCE out of resources. Pod is at risk of not being scheduled.**
        




To resolve this issue, try the following:

  * Deploy the Pod in a different region or zone. If your Pod has a zonal restriction such as a topology selector, remove the restriction if you can. For instructions, see [Place GKE Pods in specific zones](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology).
  * Create a cluster in a different region and retry the deployment.
  * Try using a different compute class. Compute classes that are backed by smaller Compute Engine machine types are more likely to have available resources. For example, the default machine type for Autopilot has the highest availability. For a list of compute classes and the corresponding machine types, see [When to use specific compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).
  * If you run GPU workloads, the requested GPU might not be available in your node location. Try deploying your workload in a different location or requesting a different type of GPU.



To avoid scale-up issues caused by resource availability in the future, consider the following approaches:

  * Define a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) with a prioritized list of fallback machine series and enable [active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) (`optimizeRulePriority: true`). This configuration lets GKE automatically provision alternative hardware when there is insufficient compute capacity in the zone and migrates Pods back when preferred capacity recovers.
  * Use Kubernetes PriorityClasses to consistently provision extra compute capacity in your cluster. For details, see [Provision extra compute capacity for rapid Pod scaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning).
  * Use Compute Engine capacity reservations with the `Performance` ComputeClass or accelerated Pods. For details, see [Consume reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).



### Nodes fail to scale up: Pod zonal resources exceeded

The following issue occurs when Autopilot doesn't provision new nodes for a Pod in a specific zone because a new node would violate resource limits.

The error message in your logs is similar to the following:
    
    
        "napFailureReasons": [
                {
                  "messageId": "no.scale.up.nap.pod.zonal.resources.exceeded",
                  ...
    

This error refers to a [`noScaleUp`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#noscaleup-event) event, where [node auto-provisioning did not provision any node group for the Pod in the zone](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#noscaleup-pod-group-level-nap-reasons).

If you encounter this error, confirm the following:

  * Your Pods have [sufficient memory and CPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).
  * The [Pod IP address CIDR range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#cidr_settings_for_clusters) is large enough to support your anticipated maximum cluster size.



### Workload scheduled on older machine series or stuck in `Pending` state due to storage incompatibility

This issue occurs when a stateful workload uses an earlier Persistent Disk volume type, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes. These volume types are incompatible with newer machine series like C3 or E4.

This issue manifests in one of two ways:

  * **Symptom 1** : a workload that you expect to run on a newer general-purpose machine series (such as C3) is automatically scheduled on an E2 node instead.
  * **Symptom 2** : a Pod that explicitly requests a newer machine series (for example, using `nodeSelector` fields or a custom ComputeClass) remains stuck in the `Pending` state.



#### Root cause

GKE Autopilot enforces compatibility between the requested storage types and the node machine series. Newer machine series like C3 and E4 require Google Cloud Hyperdisk storage (such as the `hyperdisk-balanced` disk type). These machine series don't support earlier Persistent Disk volume types, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes.

  * If you don't specify a machine series, GKE Autopilot automatically schedules the workload on an E2 node because E2 nodes support these Persistent Disk volume types. The workload silently falls back from the default newer hardware.
  * If you explicitly request a newer machine series (like C3 or E4) but attach an earlier Persistent Disk volume type, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes, GKE Autopilot can't satisfy both requirements. The Pod remains stuck in the `Pending` state.



#### Verification

To verify if your workload is affected by this compatibility constraint, perform the following steps:

  1. Check the Pod's volume configuration to see if it uses an earlier Persistent Disk volume type, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes.
  2. If the Pod is stuck in the `Pending` state, check the Cluster Autoscaler visibility logs. Look for Node Auto-Provisioning (NAP) evaluation logs similar to the following:
         
         NAP: injected node groups for requirements...
         

  3. Examine the log message for the `families="..."` list. Check if newer machine families (such as `e4` or `c3` identifiers) are missing from the list. Missing identifiers indicate that GKE filtered these families out during scheduling due to the storage requirement. The `e4` identifier is used in internal logs for E4 machine series.




#### Resolution

To resolve this issue, perform one of the following actions:

  * **Use Hyperdisk storage** : update your `StorageClass` or volume definition to use Google Cloud Hyperdisk storage (such as the `hyperdisk-balanced` disk type), which is compatible with newer machine series.
  * **Allow scheduling on older series** : if you must use earlier Persistent Disk volume types (such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes), remove any explicit requests for newer machine series (such as `nodeSelector` fields or custom ComputeClasses). Removing these requests allows GKE Autopilot to schedule the Pod on compatible nodes like E2.



## Workload issues

### Workloads stuck with ephemeral storage error

GKE won't create Pods if your Pod ephemeral storage requests exceed the Autopilot maximum of 10GiB in GKE version 1.28.6-gke.1317000 and later.

To diagnose this issue, describe the workload controller, like the Deployment or the Job:
    
    
    kubectl describe CONTROLLER_TYPE/CONTROLLER_NAME
    

Replace the following:

  * `CONTROLLER_TYPE`: the type of workload controller, like `replicaset` or `daemonset`. For a list of controller types, see [Workload management](https://kubernetes.io/docs/concepts/workloads/controllers/).
  * `CONTROLLER_NAME`: the name of the stuck workload.



If the Pod is not created because of the ephemeral storage request exceeding the maximum, the output is similar to the following:
    
    
    # lines omitted for clarity
    
    Events:
    
    {"[denied by autogke-pod-limit-constraints]":["Max ephemeral-storage requested by init containers for workload '' is higher than the Autopilot maximum of '10Gi'.","Total ephemeral-storage requested by containers for workload '' is higher than the Autopilot maximum of '10Gi'."]}
    

To resolve this issue, update your ephemeral storage requests so that the total ephemeral storage requested by workload containers and by containers that webhooks inject is at less than or equal to the allowed maximum. For more information about the maximum, see [Resource requests in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#min-max-requests). for the workload configuration.

### Pods stuck in Pending state

A Pod might get stuck in the `Pending` status if you select a specific node for your Pod to use, but the sum of resource requests in the Pod and in DaemonSets that must run on the node exceeds the maximum allocatable capacity of the node. This might cause your Pod to get a `Pending` status and remain unscheduled.

To avoid this issue, evaluate the sizes of your deployed workloads to ensure that they're within the supported [maximum resource requests for Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).

You can also try scheduling your DaemonSets before you schedule your regular workload Pods.

### Consistently unreliable workload performance on a specific node

In GKE version 1.24 and later, if your workloads on a specific node consistently experience disruptions, crashes, or similar unreliable behavior, you can tell GKE about the problematic node by cordoning it using the following command:
    
    
    kubectl drain NODE_NAME --ignore-daemonsets
    

Replace `NODE_NAME` with the name of the problematic node. You can find the node name by running `kubectl get nodes`.

GKE does the following:

  * Evicts existing workloads from the node and stops scheduling workloads on that node.
  * Automatically recreates any evicted workloads that are managed by a controller, such as a Deployment or a StatefulSet, on other nodes.
  * Terminates any workloads that remain on the node and repairs or recreates the node over time.
  * **If you use Autopilot, GKE shuts down and replaces the node immediately and ignores any configured PodDisruptionBudgets.**

**Note:** GKE manages all workloads in the `kube-system` namespace. You can safely ignore draining errors in this namespace. GKE might also rate-limit your use of this command.

### Pods take longer than expected to schedule on empty clusters

This event occurs when you deploy a workload to an Autopilot cluster that has no other workloads. Autopilot clusters start with zero usable nodes and scale to zero nodes if the cluster is empty to avoid having unutilized compute resources in the cluster. Deploying a workload in a cluster that has zero nodes triggers a scale-up event.

If you experience this, Autopilot is functioning as intended, and no action is necessary. Your workload will deploy as expected after the new nodes boot up.

Check whether your Pods are waiting for new nodes:

  1. Describe your pending Pod:
         
         kubectl describe pod POD_NAME
         

Replace `POD_NAME` with the name of your pending Pod.

  2. Check the `Events` section of the output. If the Pod is waiting for new nodes, the output is similar to the following:
         
         Events:
           Type     Reason            Age   From                                   Message
           ----     ------            ----  ----                                   -------
           Warning  FailedScheduling  11s   gke.io/optimize-utilization-scheduler  no nodes available to schedule pods
           Normal   TriggeredScaleUp  4s    cluster-autoscaler                     pod triggered scale-up: [{https://www.googleapis.com/compute/v1/projects/example-project/zones/example-zone/instanceGroups/gk3-example-cluster-pool-2-9293c6db-grp 0->1 (max: 1000)} {https://www.googleapis.com/compute/v1/projects/example-project/zones/example-zone/instanceGroups/gk3-example-cluster-pool-2-d99371e7-grp 0->1 (max: 1000)}]
         

The `TriggeredScaleUp` event shows that your cluster is scaling up from zero nodes to as many nodes are required to run your deployed workload.




### System Pods fail to schedule on empty clusters

This event occurs when none of your own workloads are running in a cluster, which results in the cluster scaling down to zero nodes. Autopilot clusters start with zero usable nodes and scale down to zero nodes if you aren't running any of your workloads in the cluster. This behavior minimizes wasted compute resources in the cluster.

When a cluster scales down to zero nodes, GKE system workloads won't schedule and stay in the `Pending` state. _This is intended behavior and no action is necessary_. The next time that you deploy a workload to the cluster, GKE will scale the cluster up and the pending system Pods will run on those nodes.

To check whether system Pods are pending because of an empty cluster, do the following:

  1. Check whether your cluster has any nodes:
         
         kubectl get nodes
         

The output is the following, which indicates that the cluster has zero nodes:
         
         No resources found
         

  2. Check the status of system Pods:
         
         kubectl get pods --namespace=kube-system
         

The output is similar to the following:
         
         NAME                                                       READY   STATUS    RESTARTS   AGE
         antrea-controller-horizontal-autoscaler-6d97f7cf7c-ngfd2   0/1     Pending   0          9d
         egress-nat-controller-84bc985778-6jcwl                     0/1     Pending   0          9d
         event-exporter-gke-5c5b457d58-7njv7                        0/2     Pending   0          3d5h
         event-exporter-gke-6cd5c599c6-bn665                        0/2     Pending   0          9d
         konnectivity-agent-694b68fb7f-gws8j                        0/2     Pending   0          3d5h
         konnectivity-agent-7d659bf64d-lp4kt                        0/2     Pending   0          9d
         konnectivity-agent-7d659bf64d-rkrw2                        0/2     Pending   0          9d
         konnectivity-agent-autoscaler-5b6ff64fcd-wn7fw             0/1     Pending   0          9d
         konnectivity-agent-autoscaler-cc5bd5684-tgtwp              0/1     Pending   0          3d5h
         kube-dns-65ccc769cc-5q5q7                                  0/5     Pending   0          3d5h
         kube-dns-7f7cdb9b75-qkq4l                                  0/5     Pending   0          9d
         kube-dns-7f7cdb9b75-skrx4                                  0/5     Pending   0          9d
         kube-dns-autoscaler-6ffdbff798-vhvkg                       0/1     Pending   0          9d
         kube-dns-autoscaler-8b7698c76-mgcx8                        0/1     Pending   0          3d5h
         l7-default-backend-87b58b54c-x5q7f                         0/1     Pending   0          9d
         metrics-server-v1.31.0-769c5b4896-t5jjr                    0/1     Pending   0          9d
         

  3. Check the reason why the system Pods have the `Pending` status:
         
         kubectl describe pod --namespace=kube-system SYSTEM_POD_NAME
         

Replace `SYSTEM_POD_NAME` with the name of any system Pod from the output of the preceding command.

The output is similar to the following:
         
         ...
         Events:
         Type     Reason            Age                       From               Message
         ----     ------            ----                      ----               -------
         Warning  FailedScheduling  4m35s (x27935 over 3d5h)  default-scheduler  no nodes available to schedule pods
         ...
         

In the output, the `no nodes available to schedule pods` value in the `Message` field for the `FailedScheduling` event indicates that the system Pod didn't schedule because the cluster is empty.




### Error related to permission when trying to run tcpdump from a Pod in GKE Autopilot

Access to underlying nodes is prohibited in a GKE Autopilot cluster. Thus, it is required to run `tcpdump` utility from within a Pod and then copy it using kubectl cp command. If you generally run tcpdump utility from within a Pod in a GKE Autopilot cluster, you might see the following error:
    
    
        tcpdump: eth0: You don't have permission to perform this capture on that device
        (socket: Operation not permitted)
    

This happens because GKE Autopilot, by default, applies a security context to all Pods that _drops_ the `NET_RAW` capability to mitigate potential vulnerabilities. For example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: tcpdump
      name: tcpdump
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 500m
            ephemeral-storage: 1Gi
            memory: 2Gi
          requests:
            cpu: 500m
            ephemeral-storage: 1Gi
            memory: 2Gi
        securityContext:
          capabilities:
            # This section drops NET_RAW to mitigate security vulnerabilities
            drop:
            - NET_RAW
    

As a solution, if your workload requires the `NET_RAW` capability, you can re-enable it:

  1. _Add_ the `NET_RAW` capability to the `securityContext` section of your Pod's YAML specification:
         
         securityContext:
           capabilities:
             add:
             - NET_RAW
         

  2. Run `tcpdump` from within a Pod:
         
         tcpdump port 53 -w packetcap.pcap
         tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
         

  3. Use `kubectl cp` command to copy it to your local machine for further analysis:
         
         kubectl cp POD_NAME:/PATH_TO_FILE/FILE_NAME/PATH_TO_FILE/FILE_NAME
         

  4. Use `kubectl exec` to run the `tcpdump` command to perform network packet capture and redirect the output:
         
         kubectl exec -it POD_NAME -- bash -c "tcpdump port 53 -w -" > packet-new.pcap
         




### Pods unable to run on a Node due to NRI RunPodSandbox failed

In rare cases, an Autopilot node in default, Balanced, Scale-Out, `autopilot`, and `autopilot-spot` compute classes can enter into a state in which system Pods, such as `anetd`, and potentially user Pods assigned to the node, are unable to transition into a running state. When `anetd` can't transition into a running state, then Pod networking is partially or completely broken on the node. This error state is triggered during certain cluster control plane upgrades only.

If you notice the issue, you can mitigate it on a given node by following the procedure for mitigating unreliable workload performance on a specific node.

**To prevent the issue from recurring, manually upgrade your cluster to one of the following GKE patch versions:**

  * **1.35** : all patch versions
  * **1.34** : 1.34.1-gke.3899000 or later
  * **1.33** : 1.33.5-gke.2392000 or later



If you suspect a node is in this error state, you can confirm this state by doing the following:

  1. Find the `efficiency-daemon` Pod running on the suspected node:
         
         DAEMON_POD_NAME=$(kubectl get pods \
           --namespace kube-system \
           --selector k8s-app=efficiency-daemon \
           --field-selector spec.nodeName=NODE_NAME \
           --output custom-columns=":metadata.name" \
           --no-headers)
         echo $DAEMON_POD_NAME
         

If there is no `efficiency-daemon` pod on the node, your node is unaffected by this particular issue.

  2. Check for specific errors from the `efficiency-daemon` Pod:
         
         kubectl logs -n kube-system $DAEMON_POD_NAME | grep "connect: operation not permitted" | wc -l
         

If the output is greater than `10`, the node is highly likely to be affected by this issue.




If you continuously observe the following error message in Pod events for a Pod assigned to the node, it is a sign that the node is affected by this issue: `Failed to create pod sandbox: rpc error: code = Unknown desc = NRI RunPodSandbox failed: rpc error: code = Unknown desc = internal error: reconciliation failed`.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
