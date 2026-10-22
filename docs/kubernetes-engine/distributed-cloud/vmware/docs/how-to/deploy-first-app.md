---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app/
title: Deploy an application \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:56.954104+00:00
---

# Deploy an application  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Deploy an application Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an example of how to deploy an application in a user cluster created with Google Distributed Cloud (software only) for VMware.

## Before you begin

For the example given here, you need a user cluster that uses [bundled MetalLB load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb). For instructions on creating a minimal user cluster that uses MetalLB, see [Create basic clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-create-clusters#create_a_user_cluster).

You can use either the Google Cloud console or the command-line tool `kubectl` on your admin workstation to deploy the application.

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the list of clusters, click your user cluster, and verify that you are logged in to the cluster.

If you aren't already logged in to your user cluster, log in by following the instructions in [Manage clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console).




**Containers**

  1. Under **New container** , select **Existing container image**.

  2. For **Image path** , enter `us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0`.

  3. Click **Continue**.




**Configuration**

  1. For **Deployment name** , enter `my-deployment`.

  2. For **Namespace** , enter `default`.

  3. Enter these two labels:

     * **Key 1** : `app`, **Value 1** : `metrics`
     * **Key 2** : `department`, **Value 2** `sales`
  4. In the **Kubernetes cluster** drop-down, select your cluster.

  5. Click **Continue**.




**Expose**

  1. Check **Expose deployment as a new service**.

  2. For **Port 1** , enter `80`.

  3. For **Target port 1** , enter `8080`. This is the appropriate value because the `hello-app` container listens on TCP port 8080 by default. You can see this by looking at the [Dockerfile and the source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app) for the app.

  4. For **Protocol 1** , select `TCP`.

  5. For **Service type** , select `LoadBalancer`.




At the bottom of the page, click the **Deploy** button.

**View Deployment and Service details**

  1. When your Deployment is ready, the **Deployment details** page opens in the [Kubernetes workloads](https://console.cloud.google.com/kubernetes/workload) section of the Google Cloud console. On this page, you can see details about the Deployment and its three Pods.

  2. Under **Exposing services** , click the name of the Service that exposes your Deployment. For this exercise, the name is `my-deployment-service`.

  3. The **Service details** page opens. On this page, you can see details about Service. For example, you can see that any Pod that has the labels `app: metrics` and `department: sales` is a member of the Service. Recall that the Pods in `my-deployment` have these labels.




You can also see a value for **Load balancer IP**. The load balancer IP has been automatically configured on the cluster load balancer.

**Forwarding for the Service**

Suppose a client outside the cluster sends a request to the load balancer IP on TCP port 80. The request gets routed to the cluster load balancer. The load balancer forwards the request to a member Pod on TCP port 8080. Recall that every Pod in `my-deployment` has a container listening on TCP port 8080.

**Test your Service**

Go to a machine where the load balancer IP is routable.

To call your Service, enter the load balancer IP in a browser, or use a command like `curl`. For example:
    
    
    curl [LOAD_BALANCER_IP]:80
    

The output shows a `Hello, world!` message. For example:
    
    
    curl 203.0.113.1:80
    Hello, world!
    Version: 2.0.0
    Hostname: my-deployment-dbd86c8c4-9wpbv
    

**Delete the Deployment**

Go to the **Workloads** page in the **Kubernetes Engine** section of the console.

[Go to the Workloads page](https://console.cloud.google.com/kubernetes/workload)

In the list of Deployments, select `my-deployment`.

At the top of the page, click delete **Delete**. This deletes both the Deployment and the exposing Service.

### Command line

## Connect to your admin workstation

Get an SSH connection to your admin workstation. Do the following steps on your admin workstation.

## Create a Deployment

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
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f my-deployment.yaml
    

where USER_CLUSTER_KUBECONFIG is the path of the [kubeconfig file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

Get basic information about your Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get deployment my-deployment
    

The output shows that the Deployment has three Pods that are all available:
    
    
    NAME            READY   UP-TO-DATE   AVAILABLE   AGE
    my-deployment   3/3     3            3           27s
    

List the Pods in your Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pods
    

The output shows that your Deployment has three running Pods:
    
    
    NAME                             READY   STATUS    RESTARTS   AGE
    my-deployment-54944c8d55-4srm2   1/1     Running   0          6s
    my-deployment-54944c8d55-7z5nn   1/1     Running   0          6s
    my-deployment-54944c8d55-j62n9   1/1     Running   0          6s
    

Get detailed information about your Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get deployment my-deployment --output yaml
    

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
      ‑ lastTransitionTime: "2019-11-11T18:44:02Z"
        lastUpdateTime: "2019-11-11T18:44:02Z"
        message: Deployment has minimum availability.
        reason: MinimumReplicasAvailable
        status: "True"
        type: Available
      ‑ lastTransitionTime: "2019-11-11T18:43:58Z"
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
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe deployment my-deployment
    

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
    

## Create a Service of type LoadBalancer

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
      ports:
      ‑ port: 80
        targetPort: 8080
    

For the purpose of this exercise, these are the important things to understand about the Service:

  * Any Pod that has the label `app: metrics` and the label `department: sales` is a member of the Service. Note that the Pods in `my-deployment` have these labels.

  * When a client sends a request to the Service on TCP port 80, the request is forwarded to a member Pod on TCP port 8080.

  * Every member Pod must have a container that is listening on TCP port 8080.




It happens that by default, the `hello-app` container listens on TCP port 8080\. You can see this by looking at the [Dockerfile and the source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app) for the app.

Save the manifest to a file named `my-service.yaml`, and create the Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f my-service.yaml
    

where USER_CLUSTER_KUBECONFIG is the path of the [kubeconfig file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

When you create the Service, Google Distributed Cloud automatically configures the `loadBalancerIP` address on the cluster load balancer.

View your Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get service my-service --output yaml
    

The output is similar to this:
    
    
    kind: Service
    metadata:
      ...
      name: my-service
      namespace: default
      ...
    spec:
      allocateLoadBalancerNodePorts: true
      clusterIP: 10.96.1.39
      clusterIPs:
      - 10.96.1.39
      externalTrafficPolicy: Cluster
      internalTrafficPolicy: Cluster
      ipFamilies:
      - IPv4
      ipFamilyPolicy: SingleStack
      ports:
      - nodePort: 31184
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
    

In the preceding output, you can see that your Service has a `clusterIP`, and a `loadBalancerIP`. It also has a `port`, and a `targetPort`.

The `clusterIP` is not relevant to this exercise. The `loadBalancerIP` is the IP address that clients outside the cluster can use to call the Service.

As an example, take the values shown in the preceding output. That is, suppose your Service has `loadBalancerIP` = 203.0.113.1, `port` = 80, and `targetPort` = 8080.

A client sends a request to 203.0.113.1 on TCP port 80. The request gets routed to the cluster load balancer. The load balancer forwards the request to a member Pod on TCP port 8080.

Call your Service:
    
    
    curl LOAD_BALANCER_IP
    

The output shows a `Hello, world!` message:
    
    
    curl 203.0.113.1
    Hello, world!
    Version: 2.0.0
    Hostname: my-deployment-dbd86c8c4-9wpbv
    

## Delete your Service

Delete your Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete service my-service
    

Verify that your Service has been deleted:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get services
    

The output no longer shows `my-service`.

## Delete your Deployment

Delete your Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete deployment my-deployment
    

Verify that your Deployment has been deleted:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get deployments
    

The output no longer shows `my-deployment`.

## What's next

[Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-service-ingress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
