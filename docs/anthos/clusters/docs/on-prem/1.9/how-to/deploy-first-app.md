---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/deploy-first-app/
title: Deploying an application \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:53.226215+00:00
---

# Deploying an application  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/deploy-first-app/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Deploying an application Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/deploy-first-app)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/deploy-first-app)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to deploy an application in your user cluster for Google Distributed Cloud.

## Before you begin

Create a user cluster ([quickstart](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-quickstart) | [full instructions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-user-cluster)).

## SSH into your admin workstation

SSH into your admin workstation:
    
    
    ssh -i ~/.ssh/vsphere_workstation ubuntu@[IP_ADDRESS]
    

where [IP_ADDRESS] is the IP address of your admin workstation.

Do all of the remaining steps in this topic on your admin workstation.

## Creating a Deployment

Here is a manifest for a Deployment:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
    spec:
      selector:
        matchLabels:
          app: metrics
          department: sales
      replicas: 3
      template:
        metadata:
          labels:
            app: metrics
            department: sales
        spec:
          containers:
          - name: hello
            image: "us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0"
    

Copy the manifest to a file named `my-deployment.yaml`, and create the Deployment:
    
    
    kubectl apply --kubeconfig [USER_CLUSTER_KUBECONFIG] -f my-deployment.yaml

where [USER_CLUSTER_KUBECONFIG] is the path of the [kubeconfig file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

Get basic information about your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get deployment my-deployment

The output shows that the Deployment has three Pods that are all available:
    
    
    NAME            READY   UP-TO-DATE   AVAILABLE   AGE
    my-deployment   3/3     3            3           27s
    

List the Pods in your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get pods

The output shows that your Deployment has three running Pods:
    
    
    NAME                             READY   STATUS    RESTARTS   AGE
    my-deployment-54944c8d55-4srm2   1/1     Running   0          6s
    my-deployment-54944c8d55-7z5nn   1/1     Running   0          6s
    my-deployment-54944c8d55-j62n9   1/1     Running   0          6s

Get detailed information about your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get deployment my-deployment --output yaml

The output shows details about the Deployment spec and status:
    
    
    kind: Deployment
    metadata:
      ...
      generation: 1
      name: my-deployment
      namespace: default
      ...
    spec:
      ...
      replicas: 3
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app: metrics
          department: sales
      ...
        spec:
          containers:
          - image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0
            imagePullPolicy: IfNotPresent
            name: hello
            resources: {}
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
          dnsPolicy: ClusterFirst
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext: {}
          terminationGracePeriodSeconds: 30
    status:
      availableReplicas: 3
      conditions:
      - lastTransitionTime: "2019-11-11T18:44:02Z"
        lastUpdateTime: "2019-11-11T18:44:02Z"
        message: Deployment has minimum availability.
        reason: MinimumReplicasAvailable
        status: "True"
        type: Available
      - lastTransitionTime: "2019-11-11T18:43:58Z"
        lastUpdateTime: "2019-11-11T18:44:02Z"
        message: ReplicaSet "my-deployment-54944c8d55" has successfully progressed.
        reason: NewReplicaSetAvailable
        status: "True"
        type: Progressing
      observedGeneration: 1
      readyReplicas: 3
      replicas: 3
      updatedReplicas: 3
    

Describe your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] describe deployment my-deployment

The output shows nicely formatted details about the Deployment, including the associated [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/):
    
    
    Name:                   my-deployment
    Namespace:              default
    CreationTimestamp:      Mon, 11 Nov 2019 10:43:58 -0800
    Labels:                 
    ...
    Selector:               app=metrics,department=sales
    Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
    StrategyType:           RollingUpdate
    MinReadySeconds:        0
    RollingUpdateStrategy:  25% max unavailable, 25% max surge
    Pod Template:
      Labels:  app=metrics
               department=sales
      Containers:
       hello:
        Image:        us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0
        Port:         
        Host Port:    
        Environment:  
        Mounts:       
      Volumes:        
    Conditions:
      Type           Status  Reason
      ----           ------  ------
      Available      True    MinimumReplicasAvailable
      Progressing    True    NewReplicaSetAvailable
    OldReplicaSets:  
    NewReplicaSet:   my-deployment-54944c8d55 (3/3 replicas created)
    

## Creating a Service of type LoadBalancer

One way to expose your Deployment to clients outside your cluster is to create a Kubernetes [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) of type `LoadBalancer`.

Here's a manifest for a Service of type `LoadBalancer`:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      selector:
        app: metrics
        department: sales
      type: LoadBalancer
      loadBalancerIP: [SERVICE_IP_ADDRESS]
      ports:
      - port: 80
        targetPort: 8080
    

For the purpose of this exercise, these are the important things to understand about the Service:

  * Any Pod that has the label `app: metrics` and the label `department: sales` is a member of the Service. Note that the Pods in `my-deployment` have these labels.

  * When a client sends a request to the Service on TCP port 80, the request is forwarded to a member Pod on TCP port 8080.

  * Every member Pod must have a container that is listening on TCP port 8080.




It happens that by default, the `hello-app` container listens on TCP port 8080\. You can see this by looking at the [Dockerfile and the source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/hello-app) for the app.

Replace [SERVICE_IP_ADDRESS] with an address that you own that is not already in use. For example, you could set this to a public IP address that your company owns. Or you could set it to a private address in your company network.

The address you choose must be routable from the location of any client that sends requests to the Service. For example, if you choose a private address, then external clients will not be able to send requests to the Service.

Save the manifest to a file named `my-service.yaml`, and create the Service:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] apply -f my-service.yaml

where [USER_CLUSTER_KUBECONFIG] is the path of the [kubeconfig file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

When you create the Service, Google Distributed Cloud automatically configures the `loadBalancerIP` address on your F5 BIG-IP load balancer.

View your Service:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get service my-service --output yaml

The output is similar to this:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      ...
      name: my-service
      namespace: default
      ...
    spec:
      clusterIP: 10.107.84.202
      externalTrafficPolicy: Cluster
      loadBalancerIP: 203.0.113.1
      ports:
      - nodePort: 31919
        port: 80
        protocol: TCP
        targetPort: 8080
      selector:
        app: metrics
        department: sales
      sessionAffinity: None
      type: LoadBalancer
    status:
      loadBalancer:
        ingress:
        - ip: 203.0.113.1
    

In the preceding output, you can see that your Service has a `clusterIP`, and a `loadBalancerIP`. It also has a `nodePort`, a `port`, and a `targetPort`.

The `clusterIP` is not relevant to this exercise. The `loadBalancerIP` is the IP address that you provided in `my-service.yaml`.

As an example, take the values shown in the preceding output. That is, suppose your Service has `loadBalancerIP` = 203.0.113.1, `port` = 80, `nodePort` = 31919, and `targetPort` = 8080.

A client sends a request to 203.0.113.1 on TCP port 80. The request gets routed to your F5 BIG-IP load balancer. The load balancer chooses one of your user cluster nodes, and forwards the request to [NODE_ADDRESS] on TCP port 31919. The iptables rules on the node forward the request to a member Pod on TCP port 8080.

Call your Service:
    
    
    curl [SERVICE_IP_ADDRESS]

where [SERVICE_IP_ADDRESS] is the address that you specified for `loadBalancerIP`.

The output shows a `Hello, world!` message:
    
    
    curl 21.0.133.48
    Hello, world!
    Version: 2.0.0
    Hostname: my-deployment-dbd86c8c4-9wpbv
    

## Deleting your Service

Delete your Service:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] delete service my-service

Verify that your Service has been deleted:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get services

The output no longer shows `my-service`.

## Deleting your Deployment

Delete your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] delete deployment my-deployment

Verify that your Deployment has been deleted:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get deployments

The output no longer shows `my-deployment`.

## What's next

[Create a Service and an Ingress](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-service-ingress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
