---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-hostport/
title: Allow direct connections to Autopilot Pods using hostPort \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:17.939987+00:00
---

# Allow direct connections to Autopilot Pods using hostPort  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-hostport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Allow direct connections to Autopilot Pods using hostPort Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page shows you how to expose a random port in a Pod running in a Google Kubernetes Engine (GKE) Autopilot cluster.

Exposing a port in a Pod lets the Pod accept incoming connections directly, without a load balancer. GKE chooses a random port to open from a range that you specify in the Pod specification. This type of random port exposure is useful when your workload requires direct incoming connections but doesn't rely on a persistent port number. An example of this type of workload is an [Agones GameServer resource](https://agones.dev/site/docs/reference/gameserver/) with the default `Dynamic` port policy.

When you request a random port, GKE overrides the value in the `hostPort` field in the container specification to the port that GKE selected for you.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a [GKE Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) running version 1.24.7-gke.1200 and later or 1.25.3-gke.1100 and later.



### Limitations

You can only assign random hostPorts for static Pods or for Pods that are managed by a custom controller, such as Agones. This functionality isn't supported on [Kubernetes managed controllers](https://kubernetes.io/docs/concepts/workloads/controllers/) such as Deployments.

## Request a random port

  1. Save the following manifest as `host-port-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: game-pod
           **annotations :
             autopilot.gke.io/host-port-assignment: '{"min":MIN_PORT,"max":MAX_PORT}'**
         spec:
           containers:
           - name: local-chat
             image: ubuntu
             **command : ["sleep", "infinity"]**
             **ports :
             - containerPort: 80
               hostPort: HOST_PORT1**
               protocol: TCP
           - name: game-server
             image: ubuntu
             **command : ["sleep", "infinity"]**
             **ports :
             - containerPort: 80
               hostPort: HOST_PORT2**
               protocol: UDP
         

Replace the following:

     * `MIN_PORT`: the minimum port number for the range from which GKE chooses a random port.
     * `MAX_PORT`: the maximum port number for the range from which GKE chooses a random port.
     * `HOST_PORT1, HOST_PORT2`: any valid port number. When the Pod is scheduled, GKE updates this field with the randomly assigned port. If you have multiple containers, use different port numbers for each container.

The port range (the difference between `MAX_PORT` and `MIN_PORT`) must be at least 1000 ports.

  2. Apply the manifest:
         
         kubectl apply -f host-port-pod.yaml
         




When you apply the manifest, GKE selects a random port from your range and assigns the port to your container. If GKE assigns the same port value to two Pods, GKE automatically places the Pods on separate nodes to avoid port conflict.

## Check the assigned port

To find the port number that GKE assigned to your containers, inspect the Pod:
    
    
    kubectl get pod game-pod --output=yaml
    

The output is similar to the following:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        **autopilot.gke.io/host-port-assignment: '{"min": MIN_PORT,"max":MAX_PORT,"portsAssigned":{"HOST_PORT1":7300,"HOST_PORT2":7450}}'**
      name: game-pod
      namespace: default
    spec:
      containers:
      - name: local-chat
        image: ubuntu
        **command:
        - sleep
        - infinity**
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          **hostPort: 7300**
          protocol: **TCP**
      - name: game-server
        image: ubuntu
        **command:
        - sleep
        - infinity**
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          **hostPort: 7450**
          protocol: **UDP**
    

In this output:

  * `metadata.annotations.autopilot.gke.io/host-port-assignment`: the port assignments, showing the original value for `hostPort` that you set for each container and the updated value for `hostPort` that GKE assigned. This field is useful if you requested multiple ports in your Pod specification.
  * `spec.containers.ports.hostPort`: the opened port that GKE assigned to each container.



## What's next

[Track Agones support on Autopilot on GitHub](https://github.com/googleforgames/agones/issues/2777).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
