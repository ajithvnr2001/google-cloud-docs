---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/kube-scheduler/
title: Troubleshoot the Kubernetes scheduler \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:04.811426+00:00
---

# Troubleshoot the Kubernetes scheduler  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/kube-scheduler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot the Kubernetes scheduler Stay organized with collections  Save and categorize content based on your preferences. 

This pages shows you how to resolve issues with the Kubernetes scheduler (`kube-scheduler`) for Google Distributed Cloud.

## Kubernetes always schedules Pods to the same set of nodes

This error might be observed in a few different ways:

  * **Unbalanced cluster utilization.** You can inspect cluster utilization for each Node with the `kubectl top nodes` command. The following exaggerated example output shows pronounced utilization on certain Nodes:
        
        NAME                   CPU(cores)   CPU%      MEMORY(bytes)   MEMORY%
        XXX.gke.internal       222m         101%       3237Mi          61%
        YYY.gke.internal       91m          0%         2217Mi          0%
        ZZZ.gke.internal       512m         0%         8214Mi          0%
        

  * **Too many requests.** If you schedule a lot of Pods at once onto the same Node and those Pods make HTTP requests, it's possible for the Node to be rate limited. The common error returned by the server in this scenario is `429 Too Many Requests`.

  * **Service unavailable.** A webserver, for example, hosted on a Node under high load might respond to all requests with `503 Service Unavailable` errors until it's under lighter load.




To check if you have Pods that are always scheduled to the same nodes, use the following steps:

  1. Run the following `kubectl` command to view the status of the Pods:
         
         kubectl get pods -o wide -n default
         

To see the distribution of Pods across Nodes, check the `NODE` column in the output. In the following example output, all of the Pods are scheduled on the same Node:
         
         NAME                               READY  STATUS   RESTARTS  AGE  IP             NODE
         nginx-deployment-84c6674589-cxp55  1/1    Running  0         55s  10.20.152.138  10.128.224.44
         nginx-deployment-84c6674589-hzmnn  1/1    Running  0         55s  10.20.155.70   10.128.226.44
         nginx-deployment-84c6674589-vq4l2  1/1    Running  0         55s  10.20.225.7    10.128.226.44
         




Pods have a number of features that allow you to fine tune their scheduling behavior. These features include topology spread constraints and anti-affinity rules. You can use one, or a combination, of these features. The requirements you define are ANDed together by `kube-scheduler`.

The scheduler logs aren't captured at the default logging verbosity level. If you need the scheduler logs for troubleshooting, do the following steps to capture the scheduler logs:

  1. Increase the logging verbosity level:

     1. Edit the `kube-scheduler` Deployment:
            
            kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG edit deployment kube-scheduler \
              -n USER_CLUSTER_NAMESPACE
            

     2. Add the flag `--v=5` under the `spec.containers.command` section:
            
            containers:
            - command:
            - kube-scheduler
            - --profiling=false
            - --kubeconfig=/etc/kubernetes/scheduler.conf
            - --leader-elect=true
            - --v=5
            

  2. When you are finished troubleshooting, reset the verbosity level back to the default level:

     1. Edit the `kube-scheduler` Deployment:
            
            kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG edit deployment kube-scheduler \
              -n USER_CLUSTER_NAMESPACE
            

     2. Set the verbosity level back to the default value:
            
            containers:
            - command:
            - kube-scheduler
            - --profiling=false
            - --kubeconfig=/etc/kubernetes/scheduler.conf
            - --leader-elect=true
            




### Topology spread constraints

[Topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) can be used to evenly distribute Pods among Nodes according to their `zones`, `regions`, `node`, or other custom-defined topology.

The following example manifest shows a Deployment that spreads replicas evenly among all schedulable Nodes using topology spread constraints:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: topology-spread-deployment
      labels:
        app: myapp
    spec:
      replicas: 30
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          topologySpreadConstraints:
          - maxSkew: 1 # Default. Spreads evenly. Maximum difference in scheduled Pods per Node.
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule # Default. Alternatively can be ScheduleAnyway
            labelSelector:
              matchLabels:
                app: myapp
            matchLabelKeys: # beta in 1.27
            - pod-template-hash
          containers:
          # pause is a lightweight container that simply sleeps
          - name: pause
            image: registry.k8s.io/pause:3.2
    

The following considerations apply when using topology spread constraints:

  * A Pod's `labels.app: myapp` is matched by the constraint's `labelSelector`.
  * The `topologyKey` specifies `kubernetes.io/hostname`. This label is automatically attached to all Nodes and is populated with the Node's hostname.
  * The `matchLabelKeys` prevents rollouts of new Deployments from considering Pods of old revisions when calculating where to schedule a Pod. The `pod-template-hash` label is automatically populated by a Deployment.



### Pod anti-affinity

[Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) lets you define constraints for which Pods can be co-located on the same Node.

The following example manifest shows a Deployment that uses anti-affinity to limit replicas to one Pod per Node:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: pod-affinity-deployment
      labels:
        app: myapp
    spec:
      replicas: 30
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          name: with-pod-affinity
          labels:
            app: myapp
        spec:
          affinity:
            podAntiAffinity:
              # requiredDuringSchedulingIgnoredDuringExecution
              # prevents Pod from being scheduled on a Node if it
              # does not meet criteria.
              # Alternatively can use 'preferred' with a weight
              # rather than 'required'.
              requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                  - key: app
                    operator: In
                    values:
                    - myapp
                # Your nodes might be configured with other keys
                # to use as `topologyKey`. `kubernetes.io/region`
                # and `kubernetes.io/zone` are common.
                topologyKey: kubernetes.io/hostname
          containers:
          # pause is a lightweight container that simply sleeps
          - name: pause
            image: registry.k8s.io/pause:3.2
    

This example Deployment specifies `30` replicas, but only expands to as many Nodes are available in your cluster.

The following considerations apply when using Pod anti-affinity:

  * A Pod's `labels.app: myapp` is matched by the constraint's `labelSelector`.
  * The `topologyKey` specifies `kubernetes.io/hostname`. This label is automatically attached to all Nodes and is populated with the Node's hostname. You can choose to use other labels if your cluster supports them, such as `region` or `zone`.



### Pre-pull container images

In the absence of any other constraints, by default `kube-scheduler` prefers to schedule Pods on Nodes that already have the container image downloaded onto them. This behavior might be of interest in smaller clusters without other scheduling configurations where it would be possible to download the images on every Node. However, relying on this concept should be seen as a last resort. A better solution is to use `nodeSelector`, topology spread constraints, or affinity / anti-affinity. For more information, see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node).

If you want to make sure container images are pre-pulled onto all Nodes, you can use a `DaemonSet` like the following example:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: prepulled-images
    spec:
      selector:
        matchLabels:
          name: prepulled-images
      template:
        metadata:
          labels:
            name: prepulled-images
        spec:
          initContainers:
            - name: prepulled-image
              image: IMAGE
              # Use a command the terminates immediately
              command: ["sh", "-c", "'true'"]
          containers:
          # pause is a lightweight container that simply sleeps
          - name: pause
            image: registry.k8s.io/pause:3.2
    

After the Pod is `Running` on all Nodes, redeploy your Pods again to see if the containers are now evenly distributed across Nodes.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
