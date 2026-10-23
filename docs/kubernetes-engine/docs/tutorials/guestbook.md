---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/guestbook/
title: Create a multi-tier web application with Redis and PHP \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:34.464330+00:00
---

# Create a multi-tier web application with Redis and PHP  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/guestbook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create a multi-tier web application with Redis and PHP Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to build a multi-tier web application using Google Kubernetes Engine (GKE).

In this tutorial, you do the following:

  * Set up a web application with an external IP address and a load balancer.
  * Create a [Redis](http://redis.io/) cluster with a single master (leader) and multiple [replicas (followers)](https://redis.io/topics/replication).



The example describes the following Kubernetes concepts:

  * [Declarative configuration](https://kubernetes.io/docs/tutorials/object-management-kubectl/declarative-object-management-configuration/) using YAML manifest files
  * [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), which are Kubernetes resources that determine the configuration for a set of replicated [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
  * [Services](https://kubernetes.io/docs/concepts/services-networking/service/) to create internal and external load balancers for a set of Pods



## Objectives

To deploy and run the application on GKE: 

  1. Set up the Redis leader
  2. Set up two Redis followers
  3. Set up the web frontend
  4. Visit the website
  5. Scale up the web frontend



The following diagram shows you an overview of the cluster architecture you create by completing these objectives:

![GKE cluster architecture](https://docs.cloud.google.com/static/kubernetes-engine/images/guestbook_diagram.svg)

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Cloud Shell is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). If you don't use Cloud Shell, you must install the gcloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com




## Prepare the environment

To set up your environment, follow these steps:

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export COMPUTE_LOCATION=COMPUTE_LOCATION
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
     * `COMPUTE_LOCATION`: a [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available), such as `us-central1`.
  2. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  3. Change to the working directory:
         
         cd kubernetes-engine-samples/quickstarts/guestbook/
         




### Create a GKE cluster

Create an Autopilot or Standard GKE cluster:

**Autopilot**
    
    
    gcloud container clusters create-auto guestbook \
        --location=${COMPUTE_LOCATION} \
    

**Standard**
    
    
    gcloud container clusters create guestbook \
        --location=${COMPUTE_LOCATION} \
        --num-nodes=4
    

### Connect to the cluster

Configure `kubectl` to communicate with the cluster:
    
    
    gcloud container clusters get-credentials guestbook \
        --location=${COMPUTE_LOCATION}
    

## Set up the Redis leader

The application uses Redis to store its data. The application writes its data to a Redis leader instance and reads data from multiple Redis follower instances.

  1. The following manifest describes a Kubernetes Deployment that runs a single replica Redis leader Pod:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: redis-leader
           labels:
             app: redis
             role: leader
             tier: backend
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: redis
           template:
             metadata:
               labels:
                 app: redis
                 role: leader
                 tier: backend
             spec:
               containers:
               - name: leader
                 image: "docker.io/redis:6.0.5"
                 resources:
                   requests:
                     cpu: 100m
                     memory: 100Mi
                 ports:
                 - containerPort: 6379

Apply the manifest to your cluster:
         
         kubectl apply -f redis-leader-deployment.yaml
         

  2. Verify that the Redis leader Pod is running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                           READY     STATUS    RESTARTS   AGE
         redis-leader-343230949-qfvrq   1/1       Running   0          43s
         

It might take several minutes for `STATUS` to change from `Pending` to `Running`.




## Create the Redis leader Service

The web application needs to communicate with the Redis leader to write its data. You can create a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/services) to proxy the traffic to the Redis leader Pod.

A Service is a Kubernetes abstraction that defines a logical set of Pods and a policy to enable access to the Pods. When you create a Service, you describe which Pods to proxy based on Pod labels.

  1. The following manifest describes a Service for the Redis leader:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: redis-leader
           labels:
             app: redis
             role: leader
             tier: backend
         spec:
           ports:
           - port: 6379
             targetPort: 6379
           selector:
             app: redis
             role: leader
             tier: backend

This manifest includes a set of label selectors. These labels match the set of labels that are deployed in the previous step. Therefore, this Service routes the network traffic to the Redis leader Pod created in a previous step.

The `ports` section of the manifest declares a single port mapping. The Service routes the traffic on `port: 6379` to the `targetPort: 6379` of the containers that match the specified `selector` labels. The `containerPort` used in the Deployment must match the `targetPort` to route traffic to the Deployment.

Apply the manifest to your cluster:
         
         kubectl apply -f redis-leader-service.yaml
         

  2. Verify that GKE created the Service:
         
         kubectl get service
         

The output is similar to the following:
         
         NAME           CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
         kubernetes     10.51.240.1     <none>        443/TCP    42s
         redis-leader   10.51.242.233   <none>        6379/TCP   12s
         




## Set up Redis followers

Although the Redis leader is a single Pod, you can make it highly available and meet traffic demands by adding a few Redis followers, or replicas.

  1. The following manifest describes a Deployment for the Redis follower Pods:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: redis-follower
           labels:
             app: redis
             role: follower
             tier: backend
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: redis
           template:
             metadata:
               labels:
                 app: redis
                 role: follower
                 tier: backend
             spec:
               containers:
               - name: follower
                 image: us-docker.pkg.dev/google-samples/containers/gke/gb-redis-follower:v2
                 resources:
                   requests:
                     cpu: 100m
                     memory: 100Mi
                 ports:
                 - containerPort: 6379

  2. Apply the manifest to your cluster:
         
         kubectl apply -f redis-follower-deployment.yaml
         

  3. Verify that the two Redis follower replicas are running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                              READY   STATUS    RESTARTS   AGE
         redis-follower-76588f55b7-bnsq6   1/1     Running   0          27s
         redis-follower-76588f55b7-qvtws   1/1     Running   0          27s
         redis-leader-dd446dc55-kl7nl      1/1     Running   0          119s
         

It might take several minutes for `STATUS` to change from `Pending` to `Running`.




## Create the Redis follower Service

The web application must communicate with the Redis followers to read data. To make the Redis followers discoverable, you must set up a Service.

  1. The following manifest describes a Service for the Redis followers:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: redis-follower
           labels:
             app: redis
             role: follower
             tier: backend
         spec:
           ports:
             # the port that this service should serve on
           - port: 6379
           selector:
             app: redis
             role: follower
             tier: backend

This manifest specifies the Service runs on port 6379. The `selector` field of the Service matches the Redis follower Pods created in the previous step.

Apply the manifest to your cluster:
         
         kubectl apply -f redis-follower-service.yaml
         

  2. Verify GKE created the Service:
         
         kubectl get service
         

The output is similar to the following:
         
         NAME           CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
         kubernetes     10.51.240.1     <none>        443/TCP    1m
         redis-leader   10.51.242.233   <none>        6379/TCP   49s
         redis-follower 10.51.247.238   <none>        6379/TCP   3s
         




## Set up the application web frontend

Now that you have Redis storage for your application, start the web servers. Like the Redis followers, the frontend is deployed using a Kubernetes Deployment.

The web application uses a [PHP](https://www.php.net/) frontend, which is configured to communicate with either the Redis follower or leader Services, depending on whether the request is a read or a write. The frontend exposes a JSON interface, and serves a [jQuery Ajax-based](https://learn.jquery.com/ajax/) UI.

  1. The following manifest describes a Deployment for the web server:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontend
         spec:
           replicas: 3
           selector:
             matchLabels:
                 app: guestbook
                 tier: frontend
           template:
             metadata:
               labels:
                 app: guestbook
                 tier: frontend
             spec:
               containers:
               - name: php-redis
                 image: us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
                 env:
                 - name: GET_HOSTS_FROM
                   value: "dns"
                 resources:
                   requests:
                     cpu: 100m
                     memory: 100Mi
                 ports:
                 - containerPort: 80

The manifest file specifies the environment variable `GET_HOSTS_FROM=dns`. When you provide the configuration to the web frontend application, the frontend application uses the hostnames `redis-follower` and `redis-leader` to performs a DNS lookup. The DNS lookup finds the IP addresses of the Services you created in the previous steps. This concept is called DNS service discovery.

Apply the manifest to your cluster:
         
         kubectl apply -f frontend-deployment.yaml
         

  2. Verify that the replicas are running:
         
         kubectl get pods -l app=guestbook -l tier=frontend
         

The output is similar to the following:
         
         NAME                        READY   STATUS    RESTARTS   AGE
         frontend-7b78458576-8kp8s   1/1     Running   0          37s
         frontend-7b78458576-gg86q   1/1     Running   0          37s
         frontend-7b78458576-hz87g   1/1     Running   0          37s
         




## Expose the frontend on an external IP address

With the current configuration, the `redis-follower` and `redis-leader` Services that you created in the previous steps are only accessible within the GKE cluster because the default type for a Service is [`ClusterIP`](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types).

A `ClusterIP` Service provides a single IP address for the set of Pods where the Service is pointing. This IP address is accessible only within the cluster.

To make the web frontend Service externally accessible, you can [specify `type: LoadBalancer` or `type: NodePort`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer) in the Service configuration depending on your requirements.

The following manifest describes a Service of type LoadBalancer:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: frontend
      labels:
        app: guestbook
        tier: frontend
    spec:
      type: LoadBalancer
      ports:
        # the port that this service should serve on
      - port: 80
      selector:
        app: guestbook
        tier: frontend

The port declaration under the `ports` section specifies `port: 80` and the `targetPort` is not specified. When you omit the `targetPort` property, it defaults to the value of the `port` field. In this case, this Service routes external traffic on port 80 to the port 80 of the containers in the `frontend` Deployment.

Apply the manifest to your cluster:
    
    
    kubectl apply -f frontend-service.yaml
    

When the `frontend` Service is created, GKE creates a [load balancer](https://docs.cloud.google.com/load-balancing) and an external IP address. These resources are [subject to billing](https://cloud.google.com/compute/pricing#lb).

## Visit the application website

To access the application website, get the external IP address of the `frontend` Service:
    
    
    kubectl get service frontend
    

The output is similar to the following:
    
    
    NAME       CLUSTER-IP      EXTERNAL-IP        PORT(S)        AGE
    frontend   10.51.242.136   109.197.92.229     80:32372/TCP   1m
    

The `EXTERNAL-IP` column might show `<pending>` while the load balancer is being created. This might take several minutes. If you see errors such as `Does not have minimum availability`, wait a few minutes. This temporary error occurs because GKE re-creates the nodes to make the changes.

Copy the IP address and open the page in your browser:

![Web application running on GKE](https://docs.cloud.google.com/static/kubernetes-engine/images/guestbook.png)

Try adding some entries by typing in a message, and clicking **Submit**. The message you typed appears in the frontend. This message indicates that data is successfully added to Redis through the Services that you created.

## Scale up the web frontend

Suppose your application has been running for a while, and it gets a sudden burst of publicity. You decide it would be a good idea to add more web servers to your frontend. You can do this by increasing the number of Pods.

  1. Scale up the number of `frontend` Pods:
         
         kubectl scale deployment frontend --replicas=5
         

The output is similar to the following:
         
         deployment.extensions/frontend scaled
         

  2. Verify the number of replicas that are running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                             READY     STATUS    RESTARTS   AGE
         frontend-88237173-3s3sc          1/1       Running   0          1s
         frontend-88237173-twgvn          1/1       Running   0          1s
         frontend-88237173-5p257          1/1       Running   0          23m
         frontend-88237173-84036          1/1       Running   0          23m
         frontend-88237173-j3rvr          1/1       Running   0          23m
         redis-leader-343230949-qfvrq     1/1       Running   0          54m
         redis-follower-132015689-dp23k   1/1       Running   0          37m
         redis-follower-132015689-xq9v0   1/1       Running   0          37m
         

You can scale down the number of `frontend` Pods by using the same command, replacing `5` with `1`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the individual resources

If you used an existing project and you don't want to delete it, delete the individual resources.

  1. Delete the `frontend` Service:
         
         kubectl delete service frontend
         

  2. Delete the GKE cluster:
         
         gcloud container clusters delete guestbook
         




## What's next

  * Learn how to [configure horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * Learn how to [deploy WordPress on GKE with Persistent Disk and Cloud SQL](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/persistent-disk).
  * Learn how to [Configure domain names with static IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip).
  * Explore other [Kubernetes Engine tutorials](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
