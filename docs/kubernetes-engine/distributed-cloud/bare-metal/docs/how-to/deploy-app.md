---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app/
title: Deploy an application \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:06.755112+00:00
---

# Deploy an application  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Deploy an application Stay organized with collections  Save and categorize content based on your preferences. 

Kubernetes Deployments let you run containerized workloads on Google Distributed Cloud, and Services of type `LoadBalancer` make those workloads reachable from outside your cluster. In this document, you deploy a sample application and expose it on an external IP address from your cluster's load balancer address pool.

## Before you begin

To deploy a workload, you must have a user, hybrid, or standalone cluster capable of running workloads.

## Create a Deployment

The following steps create a Deployment on your cluster:

  1. Copy the following manifest to a file named `my-deployment.yaml`:
         
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
         

  2. Use `kubectl apply` to create the Deployment:
         
         kubectl apply -f my-deployment.yaml --kubeconfig CLUSTER_KUBECONFIG
         

Replace CLUSTER_KUBECONFIG with the path of the kubeconfig file for your cluster.

  3. Get basic information about your Deployment to confirm it was created successfully:
         
         kubectl get deployment my-deployment --kubeconfig CLUSTER_KUBECONFIG
         

The output shows that the Deployment has three Pods that are all available:
         
         NAME            READY   UP-TO-DATE   AVAILABLE   AGE
         my-deployment   3/3     3            3           27s
         

  4. List the Pods in your Deployment:
         
         kubectl get pods --kubeconfig CLUSTER_KUBECONFIG
         

The output shows that your Deployment has three running Pods:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         my-deployment-869f65669b-5259x   1/1     Running   0          34s
         my-deployment-869f65669b-9xfrs   1/1     Running   0          34s
         my-deployment-869f65669b-wn4ft   1/1     Running   0          34s
         

  5. Get detailed information about your Deployment:
         
         kubectl get deployment my-deployment --output yaml --kubeconfig CLUSTER_KUBECONFIG
         

The output shows details about the Deployment spec and status:
         
         apiVersion: apps/v1
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
           - lastTransitionTime: "2023-06-29T16:17:17Z"
             lastUpdateTime: "2023-06-29T16:17:17Z"
             message: Deployment has minimum availability.
             reason: MinimumReplicasAvailable
             status: "True"
             type: Available
           - lastTransitionTime: "2023-06-29T16:17:12Z"
             lastUpdateTime: "2023-06-29T16:17:17Z"
             message: ReplicaSet "my-deployment-869f65669b" has successfully progressed.
             reason: NewReplicaSetAvailable
             status: "True"
             type: Progressing
           observedGeneration: 1
           readyReplicas: 3
           replicas: 3
           updatedReplicas: 3
         

  6. Describe your Deployment:
         
         kubectl describe deployment my-deployment --kubeconfig CLUSTER_KUBECONFIG
         

The output shows nicely formatted details about the Deployment, including the associated [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/):
         
         Name:                   my-deployment
         Namespace:              default
         CreationTimestamp:      Thu, 29 Jun 2023 16:17:12 +0000
         Labels:                 <none>
         Annotations:            deployment.kubernetes.io/revision: 1
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
             Port:         <none>
             Host Port:    <none>
             Environment:  <none>
             Mounts:       <none>
           Volumes:        <none>
         Conditions:
           Type           Status  Reason
           ----           ------  ------
           Available      True    MinimumReplicasAvailable
           Progressing    True    NewReplicaSetAvailable
         OldReplicaSets:  <none>
         NewReplicaSet:   my-deployment-869f65669b (3/3 replicas created)
         Events:
           Type    Reason             Age    From                   Message
           ----    ------             ----   ----                   -------
           Normal  ScalingReplicaSet  6m50s  deployment-controller  Scaled up replica set my-deployment-869f65669b to 3
         




## Create a Service of type `LoadBalancer`

One way to expose your Deployment to clients outside your cluster is to create a Kubernetes [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) of type `LoadBalancer`.

To create a Service of type `LoadBalancer`:

  1. Copy the following manifest to a file named `my-service.yaml`:
         
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
           - port: 80
             targetPort: 8080
         

Here are the important things to understand about the Service in this exercise:

     * Any Pod that has the label `app: metrics` and the label `department: sales` is a member of the Service. The Pods in `my-deployment` have these labels.

     * When a client sends a request to the Service on TCP port`80`, the request is forwarded to a member Pod on TCP port `8080`.

     * Every member Pod must have a container that is listening on TCP port `8080`.

By default, the `hello-app` container listens on TCP port `8080`. You can see this port setting by looking at the [Dockerfile and the source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app) for the app.

  2. Use `kubectl apply` to create the Service on your cluster:
         
         kubectl apply -f my-service.yaml --kubeconfig CLUSTER_KUBECONFIG
         

Replace CLUSTER_KUBECONFIG with the path of the kubeconfig file for your cluster.

  3. View your Service:
         
         kubectl get service my-service --output yaml --kubeconfig CLUSTER_KUBECONFIG
         

The output is similar to the following:
         
         apiVersion: v1
         kind: Service
         metadata:
           ...
           name: my-service
           namespace: default
           ...
         spec:
           allocateLoadBalancerNodePorts: true
           clusterIP: 10.96.2.165
           clusterIPs:
           - 10.96.2.165
           externalTrafficPolicy: Cluster
           internalTrafficPolicy: Cluster
           ipFamilies:
           - IPv4
           ipFamilyPolicy: SingleStack
           ports:
           - nodePort: 31565
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
             - ip: 192.168.1.13
         

In the preceding output, you can see that your Service has a `clusterIP`, and an external IP address. It also has a `nodePort`, a `port`, and a `targetPort`.

The `clusterIP` isn't relevant to this exercise. The external IP address (`status.loadBalancer.ingress.ip`) comes from the range of addresses that you specified when you defined load balancer address pools (`spec.loadBalancer.addressPools`) in the cluster configuration file.

As an example, take the values shown in the preceding output for your Service:

     * External IP address: `192.168.1.13`
     * `port`: `80`
     * `nodePort`: `31565`
     * `targetPort`: `8080`

A client sends a request to `192.168.1.13` on TCP port `80`. The request is routed to your load balancer, and from there it is forwarded to a member Pod on TCP port `8080`.

  4. Call your Service:
         
         curl INGRESS_IP_ADDRESS
         

Replace INGRESS_IP_ADDRESS with the ingress IP address in the `status` section of the Service that you retrieved in the preceding step (`status.loadBalancer.ingress`).

The output shows a `Hello, world!` message:
         
         Hello, world!
         Version: 2.0.0
         Hostname: my-deployment-869f65669b-wn4ft
         




### LoadBalancer port limits

The `LoadBalancer` type is an extension of the `NodePort` type. So a Service of type `LoadBalancer` has a cluster IP address and one or more `nodePort` values. By default, Kubernetes allocates node ports to Services of type `LoadBalancer`. These allocations can quickly exhaust available node ports from the 2,768 allotted to your cluster. To save node ports, disable load balancer node port allocation by setting the `allocateLoadBalancerNodePorts` field to `false` in the `LoadBalancer` Service spec. This setting prevents Kubernetes from allocating node ports to LoadBalancer Services. For more information, see [Disabling load balancer NodePort allocation](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) in the Kubernetes documentation.

Here's a manifest to create a Service that doesn't use any node ports:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: service-does-not-use-nodeports
    spec:
      selector:
        app: my-app
      type: LoadBalancer
      ports:
      - port: 8000
      # Set allocateLoadBalancerNodePorts to false**  allocateLoadBalancerNodePorts: false**
    

## Delete your Service

To delete your Service:

  1. Use `kubectl delete` to delete your Service from your cluster:
         
         kubectl delete service my-service --kubeconfig CLUSTER_KUBECONFIG
         

  2. Verify that your Service has been deleted:
         
         kubectl get services --kubeconfig CLUSTER_KUBECONFIG
         

The output no longer shows `my-service`.




## Delete your Deployment

To delete your Deployment:

  1. Use `kubectl delete` to delete your Deployment from your cluster:
         
         kubectl delete deployment my-deployment --kubeconfig CLUSTER_KUBECONFIG
         

Verify that your Deployment has been deleted:
         
         kubectl get deployments --kubeconfig CLUSTER_KUBECONFIG
         

The output no longer shows `my-deployment`.




## What's next

[Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
