---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy/
title: Configure network policies for applications \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:14.394741+00:00
---

# Configure network policies for applications  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure network policies for applications Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to use cluster network policies to control which Pods receive incoming network traffic, and which Pods can send outgoing traffic. For more information, see [Creating a cluster network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).

Network policies allow you to limit connections between Pods. Therefore, using network policies provide better security by reducing the compromise radius.

Note that the network policies determine whether a connection is allowed, and they do not offer higher level features like authorization or secure transport (like SSL/TLS).

## Objectives

In this tutorial, you will learn: 

  * How to create clusters with Network Policy enforcement
  * How to restrict incoming traffic to Pods using labels
  * How to restrict outgoing traffic from Pods using labels



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Take the following steps to enable the Kubernetes Engine API: 

  1. Visit the [ Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes) in the Google Cloud console. 
  2. Create or select a project. 
  3. Wait for the API and related services to be enabled. This can take several minutes. 
  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




Install the following command-line tools used in this tutorial: 

  * `gcloud` is used to create and delete Kubernetes Engine clusters. `gcloud` is included in the [`gcloud` CLI](https://docs.cloud.google.com/sdk/docs/install). 
  * `kubectl` is used to manage Kubernetes, the cluster orchestration system used by Kubernetes Engine. You can install `kubectl` using `gcloud`: 
        
        gcloud components install kubectl




Clone the sample code from GitHub:
    
    
    git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
    cd kubernetes-engine-samples/networking/network-policies
    

### Set defaults for the `gcloud` command-line tool

To save time typing your [project ID](https://support.google.com/cloud/answer/6158840) and [Compute Engine zone](https://docs.cloud.google.com/compute/docs/zones#available) options in the `gcloud` command-line tool, you can set the defaults: 
    
    
    gcloud config set project project-id
    gcloud config set compute/zone compute-zone

## Creating a GKE cluster with network policy enforcement

To create a [container cluster](https://docs.cloud.google.com/kubernetes-engine/docs/clusters) with network policy enforcement, run the following command:
    
    
    gcloud container clusters create test --enable-network-policy
    

**Warning:** If you omit the `--enable-network-policy` flag, any NetworkPolicy resources you create are silently ignored.

## Restricting incoming traffic to Pods

Kubernetes `NetworkPolicy` resources let you configure network access policies for the Pods. `NetworkPolicy` objects contain the following information:

  * Pods the network policies apply to, usually designated by a label selector

  * Type of traffic the network policy affects: Ingress for incoming traffic, Egress for outgoing traffic, or both

  * For Ingress policies, which Pods can connect to the specified Pods

  * For Egress policies, the Pods to which the specified Pods can connect




First, run a web server application with label `app=hello` and expose it internally in the cluster:
    
    
    kubectl run hello-web --labels app=hello \
      --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080 --expose
    

Next, configure a `NetworkPolicy` to allow traffic to the `hello-web` Pods from only the `app=foo` Pods. Other incoming traffic from Pods that do not have this label, external traffic, and traffic from Pods in other namespaces are blocked.

The following manifest selects Pods with label `app=hello` and specifies an Ingress policy to allow traffic only from Pods with the label `app=foo`:
    
    
    kind: NetworkPolicy
    apiVersion: networking.k8s.io/v1
    metadata:
      name: hello-allow-from-foo
    spec:
      policyTypes:
      - Ingress
      podSelector:
        matchLabels:
          app: hello
      ingress:
      - from:
        - podSelector:
            matchLabels:
              app: foo

To apply this policy to the cluster, run the following command:
    
    
    kubectl apply -f hello-allow-from-foo.yaml
    

### Validate the Ingress policy

First, run a temporary Pod with the label `app=foo` and get a shell in the Pod:
    
    
    kubectl run -l app=foo --image=alpine --restart=Never --rm -i -t test-1
    

Make a request to the `hello-web:8080` endpoint to verify that the incoming traffic is allowed:
    
    
    / # wget -qO- --timeout=2 http://hello-web:8080
    
    
    Hello, world!
    Version: 1.0.0
    Hostname: hello-web-2258067535-vbx6z
    / # exit

Traffic from Pod `app=foo` to the `app=hello` Pods is enabled.

Next, run a temporary Pod with a different label (`app=other`) and get a shell inside the Pod:
    
    
    kubectl run -l app=other --image=alpine --restart=Never --rm -i -t test-1
    

Make the same request to observe that the traffic is **not allowed** and therefore the request times out, then exit from the Pod shell:
    
    
    / # wget -qO- --timeout=2 http://hello-web:8080
    
    
    wget: download timed out
    / # exit

## Restricting outgoing traffic from the Pods

You can restrict outgoing traffic as you would incoming traffic.

However, to be able to query internal hostnames such as `hello-web` or external hostnames such as `www.example.com`, you must allow DNS (domain name system) resolution in your egress network policies. DNS traffic occurs on port 53 using TCP and UDP protocols.

To enable egress network policies, deploy a `NetworkPolicy` controlling outbound traffic from Pods with the label `app=foo` while allowing traffic only to Pods with the label `app=hello`, as well as the DNS traffic.

The following manifest specifies a network policy controlling the egress traffic from Pods with label `app=foo` with two allowed destinations:

  1. Pods in the same namespace with the label `app=hello`.
  2. Cluster Pods or external endpoints on port 53 (UDP and TCP).


    
    
    kind: NetworkPolicy
    apiVersion: networking.k8s.io/v1
    metadata:
      name: foo-allow-to-hello
    spec:
      policyTypes:
      - Egress
      podSelector:
        matchLabels:
          app: foo
      egress:
      - to:
        - podSelector:
            matchLabels:
              app: hello
      - ports:
        - port: 53
          protocol: TCP
        - port: 53
          protocol: UDP

To apply this policy to the cluster, run the following command:
    
    
    kubectl apply -f foo-allow-to-hello.yaml
    

### Validate the egress policy

First, deploy a new web application called `hello-web-2` and expose it internally in the cluster:
    
    
    kubectl run hello-web-2 --labels app=hello-2 \
      --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080 --expose
    

Next, run a temporary Pod with the label `app=foo` and open a shell inside the container:
    
    
    kubectl run -l app=foo --image=alpine --rm -i -t --restart=Never test-3
    

Validate that the Pod can establish connections to `hello-web:8080`:
    
    
    / # wget -qO- --timeout=2 http://hello-web:8080
    
    
    Hello, world!
    Version: 1.0.0
    Hostname: hello-web-2258067535-vbx6z

Validate that the Pod **cannot** establish connections to `hello-web-2:8080`:
    
    
    / # wget -qO- --timeout=2 http://hello-web-2:8080
    
    
    wget: download timed out

Validate that the Pod **cannot** establish connections to external websites such as `www.example.com`, and exit from the Pod shell.
    
    
    / # wget -qO- --timeout=2 http://www.example.com
    
    
    wget: download timed out
    / # exit

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. **Delete the container cluster:** This step will delete the resources that make up the container cluster, such as the compute instances, disks and network resources.
         
         gcloud container clusters delete test




## What's next

  * [Configuring Network Policies on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * [Kubernetes Network Policies documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  * [Example Network Policies](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
