---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-zero-using-keda/
title: Scale to zero using KEDA \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:50.689094+00:00
---

# Scale to zero using KEDA  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-zero-using-keda/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scale to zero using KEDA Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Recommended:** In GKE version 1.37 or later, the built-in horizontal Pod autoscaler supports scaling workloads to and from zero without third-party tools like KEDA. For simpler management and faster Pod activation, see [Scale GKE workloads to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa). 

This tutorial shows how to scale your GKE workloads down to zero Pods using [KEDA](https://keda.sh/). Scaling the deployments to zero Pods saves resources during periods of inactivity (such as weekends and non-office hours), or for intermittent workloads such as periodic jobs.

## Objectives

This tutorial describes the following use cases:

  * Scale your Pub/Sub workload to zero: Scale the number of Pods in proportion to the number of messages queued on the Pub/Sub topic. When the queue is empty, the workload automatically scales down to zero Pods.
  * Scale your LLM workload to zero. Deploy your LLM model servers on nodes with GPU. When the service is idle, the workload automatically scales down to zero Pods.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)
  * [GPU resources](https://cloud.google.com/compute/gpus-pricing) used by GKE
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), [kubectl](https://kubernetes.io/docs/reference/kubectl/), [Helm](https://helm.sh/) and [Terraform](https://docs.cloud.google.com/docs/terraform) command-line tools. If you don't use Cloud Shell, you must install the Google Cloud CLI and Helm.

  1. To run the commands on this page, set up the gcloud CLI in one of the following development environments:

### Cloud Shell

To use an online terminal with the gcloud CLI already set up, activate Cloud Shell:

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

### Local shell

To use a local development environment, follow these steps:

     1. [ Install the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/install)
     2. [ Initialize the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/initialize)
     3. [ Install Helm, a Kubernetes package management tool.](https://helm.sh/docs/intro/install/)

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Resource Manager, Compute Engine, GKE, Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,compute.googleapis.com,container.googleapis.com,pubsub.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Resource Manager, Compute Engine, GKE, Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,compute.googleapis.com,container.googleapis.com,pubsub.googleapis.com)




### Setting up your environment

**Note:** This tutorial assumes that your GKE cluster, Pub/Sub topic, and Pub/Sub subscription are all located in the same Google Cloud project.

To set up your environment with Cloud Shell, follow these steps:

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format 'get(projectNumber)')
         export LOCATION=LOCATION
         

Replace `PROJECT_ID` with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) and `LOCATION` with the [regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) where your GKE cluster should be created.

**Note:** For deploying an Ollama workload, choose a location that supports the `g2-standard-4` machine type. For more information, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

If you don't follow the entire tutorial in a single session, or if your environment variables are unset for some reason, make sure to run this command again to set the variables again.

  2. Create a Standard GKE cluster with [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) and [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enabled:
         
         gcloud container clusters create scale-to-zero \
             --project=${PROJECT_ID} --location=${LOCATION} \
             --machine-type=n1-standard-2 \
             --enable-autoscaling --min-nodes=1 --max-nodes=5 \
             --workload-pool=${PROJECT_ID}.svc.id.goog
         




## Install KEDA

[KEDA](https://keda.sh/) is a component that complements the Kubernetes horizontal Pod autoscaler. With KEDA, you can scale a Deployment to zero Pods and up from zero Pods to one Pod. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.. The standard [horizontal Pod autoscaler algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) applies after GKE creates at least one Pod.

After GKE scales the Deployment to zero Pods, because no Pods are running, autoscaling cannot rely on Pod metrics such as CPU utilization. As a consequence, KEDA allows fetching metrics originating from outside the cluster using an implementation of the Kubernetes [External Metrics API](https://kubernetes.io/docs/reference/external-api/external-metrics.v1beta1/). You can use this API to autoscale based on metrics such as the number of outstanding messages on a Pub/Sub subscription. See the [KEDA documentation](https://keda.sh/docs/2.15/scalers/) for a list of all supported metric sources.

Install KEDA on your cluster with Helm or with `kubectl`.

###  Helm 

Run the following commands to add the KEDA Helm repository, install the KEDA Helm chart, and give the KEDA service account read access to Cloud Monitoring:
    
    
    helm repo add kedacore https://kedacore.github.io/charts
    helm repo update
    helm install keda kedacore/keda --create-namespace --namespace keda
    
    gcloud projects add-iam-policy-binding projects/${PROJECT_ID} \
         --role roles/monitoring.viewer \
         --member=principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/keda/sa/keda-operator
    

Note that this command also sets up authorization rules that require the cluster to be set up with Workload Identity Federation for GKE.

###  `kubectl`

Run the following commands to install KEDA using `kubectl apply` and to give the KEDA service account read access to Cloud Monitoring:
    
    
    kubectl apply --server-side  -f https://github.com/kedacore/keda/releases/download/v2.15.1/keda-2.15.1.yaml
    
    gcloud projects add-iam-policy-binding projects/${PROJECT_ID} \
         --role roles/monitoring.viewer \
         --member=principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/keda/sa/keda-operator
    

Note that this command also sets up authorization rules that require the cluster to be set up with Workload Identity Federation for GKE.

Confirm that all KEDA resources appear under the `keda` namespace:
    
    
    kubectl get all -n keda
    

For more information about KEDA design and resources, see the [KEDA documentation](https://keda.sh/docs/2.15/).

## Scale your Pub/Sub workload to zero

This section describes a workload that processes messages from a Pub/Sub subscription, handling each message and acknowledging its completion. The workload scales dynamically: as the number of unacknowledged messages increases, autoscaling instantiates more Pods to ensure timely processing.

Scaling to zero ensures that no Pods are instantiated when no messages have been received for a while. This saves resources as no Pods stay idle for long periods of time.

### Deploy a Pub/Sub workload

Deploy a sample workload that processes messages queued on a Pub/Sub topic. To simulate a realistic workload, this sample program waits three seconds before acknowledging a message. The workload is configured to run under the `keda-pubsub-sa` service account.

Run the following commands to create the Pub/Sub topic and subscription, configure their permission, and create the Deployment starting the workload under the `keda-pubsub` namespace.
    
    
    gcloud pubsub topics create keda-echo
    gcloud pubsub subscriptions create keda-echo-read --topic=keda-echo
    gcloud projects add-iam-policy-binding projects/${PROJECT_ID}  \
        --role=roles/pubsub.subscriber \
      --member=principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/keda-pubsub/sa/keda-pubsub-sa
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/cost-optimization/gke-keda/cloud-pubsub/deployment/keda-pubsub-with-workload-identity.yaml
    

### Configure scale-to-zero

To configure your Pub/Sub workload to scale to zero, use KEDA to define a ScaledObject resource to specify how the deployment should scale. KEDA will then automatically create and manage the underlying HorizontalPodAutoscaler (HPA) object.

  1. Create the ScaledObject resource to describe the expected autoscaling behavior:
         
         curl https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/cost-optimization/gke-keda/cloud-pubsub/deployment/keda-pubsub-scaledobject.yaml | envsubst | kubectl apply -f -
         

This creates the following object:
         
         apiVersion: keda.sh/v1alpha1
         kind: ScaledObject
         metadata:
           name: keda-pubsub
           namespace: keda-pubsub
         spec:
           maxReplicaCount: 5
           scaleTargetRef:
             name: keda-pubsub
           triggers:
             - type: gcp-pubsub
               authenticationRef:
                 name: keda-auth
               metadata:
                 subscriptionName: "projects/${PROJECT_ID}/subscriptions/keda-echo-read"
         

  2. Inspect the HorizontalPodAutoscaler (HPA) object that KEDA creates based on the ScaledObject object:
         
         kubectl get hpa keda-hpa-keda-pubsub -n keda-pubsub -o yaml
         

**Note:** Even if the `minReplicas` field is not set to zero, KEDA overrides it by removing any Pods from the target Deployment when scaling to zero.

You can read more about autoscaling in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

  3. Wait until KEDA acknowledges that the Pub/Sub subscription is empty, and scales the Deployment to zero replicas.

Inspect the workload autoscaler:
         
         kubectl describe hpa keda-hpa-keda-pubsub -n keda-pubsub
         

Observe that in the command response, the `ScalingActive` condition is false. The associated message shows that the horizontal Pod autoscaler acknowledges that KEDA scaled the deployment to zero, at which point it stops operating until the Deployment scales back up to one Pod.
         
         Name:                                                  keda-hpa-keda-pubsub
         Namespace:                                             keda-pubsub
         Metrics:                                               ( current / target )
           "s0-gcp-ps-projects-[...]]" (target average value):  0 / 10
         Min replicas:                                          1
         Max replicas:                                          5
         Deployment pods:                                       5 current / 5 desired
         Conditions:
           Type            Status  Reason               Message
           ----            ------  ------               -------
           AbleToScale     True    ScaleDownStabilized  recent recommendations were higher than current one [...]
           ScalingActive   False   ScalingDisabled      scaling is disabled since the replica count of the target is zero
           ScalingLimited  True    TooManyReplicas      the desired replica count is more than the maximum replica count
         




### Trigger the scale-up

To stimulate the Deployment to scale up:

  1. Enqueue messages on the Pub/Sub topic:
         
         for num in {1..20}
         do
           gcloud pubsub topics publish keda-echo --project=${PROJECT_ID} --message="Test"
         done
         

  2. Verify that the Deployment is scaling up:
         
         kubectl get deployments -n keda-pubsub
         

In the output, observe that the 'Ready' column shows one replica:
         
         NAME          READY   UP-TO-DATE   AVAILABLE   AGE
         keda-pubsub   1/1     1            1           2d
         




KEDA scales up the Deployment after it observes that the queue is not empty.

## Scale your LLM workload to zero

This section describes a Large Language Model (LLM) workload that deploys an [Ollama server](https://ollama.com/) with attached GPU. Ollama allows running popular LLMs such as [Gemma](https://github.com/google-deepmind/gemma) and [Llama 2](https://www.llama.com/llama2/), and exposes its features primarily through HTTP.

### Install KEDA-HTTP add-on

Scaling an HTTP service down to zero Pods during periods of inactivity causes request failures, since there's no backend to handle the requests.

This section shows how to solve this problem using the [KEDA-HTTP](https://github.com/kedacore/http-add-on) add-on. KEDA-HTTP starts an HTTP proxy that receives user requests and forwards them to the Services configured to scale-to-zero. When the Service has no Pod, the proxy triggers the Service to scale up, and buffers the request until the Service has scaled up to at least one Pod.

**Caution:** KEDA-HTTP is in beta.

Install the KEDA-HTTP add-on using Helm. For more information, refer to [KEDA-HTTP documentation](https://github.com/kedacore/http-add-on/blob/main/docs/install.md).
    
    
    helm repo add ollama-helm https://otwld.github.io/ollama-helm/
    helm repo update
    
    # Set the proxy timeout to 120s, giving Ollama time to start.
    helm install http-add-on kedacore/keda-add-ons-http  \
      --create-namespace --namespace keda \
      --set interceptor.responseHeaderTimeout=120s
    

### Deploy an Ollama LLM workload

To deploy an Ollama LLM workload:

  1. Create a node pool containing `g2-standard-4` nodes with attached GPUs, and configure cluster autoscaling to provide between zero and two nodes:
         
         gcloud container node-pools create gpu --machine-type=g2-standard-4 \
             --location=${LOCATION} --cluster=scale-to-zero \
             --min-nodes 0 --max-nodes 2 --num-nodes=1 --enable-autoscaling
         

**Note:** Your location must support the `g2-standard-4` machine type. For more information, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  2. Add the official Ollama Helm chart repository, and update your local Helm client's repository:
         
         helm repo add ollama-helm https://otwld.github.io/ollama-helm/
         helm repo update
         

  3. Deploy the Ollama server using the Helm chart:
         
         helm install ollama ollama-helm/ollama --create-namespace --namespace ollama \
           -f https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/cost-optimization/gke-keda/ollama/helm-values-ollama.yaml
         

The `helm-values-ollama.yaml` configuration specifies the LLM models to load, the GPU requirements, and the TCP port for the Ollama server.




### Configure scale-to-zero

To configure your Ollama workload to scale to zero, KEDA-HTTP uses an [`HTTPScaledObject`](https://github.com/kedacore/http-add-on/blob/main/docs/ref/v0.9.0/http_scaled_object.md).

  1. Create the `HTTPScaledObject` resource to describe the expected autoscaling behavior:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/cost-optimization/gke-keda/ollama/keda-ollama-httpscaledobject.yaml
         

This creates the `HTTPScaledObject` object that defines the following fields:

     * `scaleTargetRef`: specifies the Service to which KEDA-HTTP should forward the requests. In this example, all requests with the host `ollama.ollama` are routed to the Ollama server.
     * `scaledownPeriod`: specifies (in seconds) how fast to scale down when no requests are received.
     * `replicas`: specifies the minimum and maximum number of Pods to maintain for the Ollama deployment.
     * `scalingMetric`: specifies the metrics used to drive autoscaling, such as request rate in this example. For more metric options, see the [KEDA-HTTP documentation](https://github.com/kedacore/http-add-on/blob/main/docs/ref/v0.9.0/http_scaled_object.md#scalingmetric).
    
    kind: HTTPScaledObject
    apiVersion: http.keda.sh/v1alpha1
    metadata:
        namespace: ollama
        name: ollama
    spec:
        hosts:
        - ollama.ollama
        scaleTargetRef:
            name: ollama
            kind: Deployment
            apiVersion: apps/v1
            service: ollama
            port: 11434
        replicas:
            min: 0
            max: 2
        scaledownPeriod: 3600
        scalingMetric:
            requestRate:
                targetValue: 20
    

  2. Run the following command to verify that KEDA-HTTP has successfully processed the HTTPScaledObject created in the previous step:
         
         kubectl get hpa,scaledobject -n ollama
         

The output shows the HorizontalPodAutoscaler (created by KEDA), and the ScaledObject (created by KEDA-HTTP) resources:
         
         NAME                                                  REFERENCE           TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
         horizontalpodautoscaler.autoscaling/keda-hpa-ollama   Deployment/ollama   0/100 (avg)   1         2         1          2d
         
         NAME                          SCALETARGETKIND      SCALETARGETNAME   MIN   MAX   TRIGGERS        AUTHENTICATION   READY   ACTIVE   FALLBACK   PAUSED    AGE
         scaledobject.keda.sh/ollama   apps/v1.Deployment   ollama            0     2     external-push                    True    False    False      Unknown   2d
         

  3. Verify that the Deployment scales down to zero Pods.

Wait the period of time set in the `scaledownPeriod` field and run the command:
         
         kubectl get deployments -n ollama
         

The output shows that KEDA scaled down the Ollama deployment, and that no Pods are running:
         
         NAME     READY   UP-TO-DATE   AVAILABLE   AGE
         ollama   0/0     0            0           2d
         




### Trigger the scale-up

To stimulate the Deployment to scale up, call the Ollama service using the proxy set up by the KEDA-HTTP add-on. This causes the value of the _request rate_ metric to increase, and triggers the creation of a first Pod.

Use `kubectl` port forwarding capabilities to access the proxy because the proxy is not exposed externally.
    
    
    kubectl port-forward svc/keda-add-ons-http-interceptor-proxy -n keda 8080:8080 &
    
    # Set the 'Host' HTTP header so that the proxy routes requests to the Ollama server.
    curl -H "Host: ollama.ollama" \
      http://localhost:8080/api/generate \
      -d '{ "model": "gemma:7b", "prompt": "Hello!" }'
    

The `curl` command sends the prompt "Hello!" to a Gemma model. Observe the answer tokens coming back in the response. For the specification of the API, see the [Ollama guide](https://github.com/ollama/ollama/blob/main/docs/api.md).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Clean up the Pub/Sub subscription and topic:
         
         gcloud pubsub subscriptions delete keda-echo-read
         gcloud pubsub topics delete keda-echo
         

  2. Delete your GKE cluster:
         
         gcloud container clusters delete scale-to-zero --location=${LOCATION}
         




## What's next

  * Learn more about [autoscaling LLM inference workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling).
  * Explore the KEDA [GitHub repository](https://github.com/kedacore/keda) and [documentation](https://keda.sh/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
