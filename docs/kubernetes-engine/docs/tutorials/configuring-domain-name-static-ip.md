---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip/
title: Configure domain names with static IP addresses \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:03.382672+00:00
---

# Configure domain names with static IP addresses  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure domain names with static IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to use Google Kubernetes Engine (GKE) to expose your web application to the internet on a [static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress) and configure a domain name to point to your application.

This tutorial assumes you own a registered domain name, such as `example.com`.

**Note:** This tutorial uses the built-in [GKE Ingress Controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) and does not apply to the [NGINX Ingress Controller](https://github.com/kubernetes/ingress-nginx).

## Objectives

This tutorial demonstrates the following steps:

  * Reserve a static external IP address for your application
  * Configure either [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) or [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) resources to use the static IP address
  * Update DNS records of your domain name to point to your application



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
    cd kubernetes-engine-samples/quickstarts/hello-app/manifests
    

### Set defaults for the `gcloud` command-line tool

To save time typing your [project ID](https://support.google.com/cloud/answer/6158840) and [Compute Engine zone](https://docs.cloud.google.com/compute/docs/zones#available) options in the `gcloud` command-line tool, you can set the defaults: 
    
    
    gcloud config set project project-id
    gcloud config set compute/zone compute-zone

### Create a cluster

Create a cluster:
    
    
    gcloud container clusters create-auto domain-test
    

## Deploy your web application

The following manifest describes a Deployment that runs a sample web application container image:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: helloweb
      labels:
        app: hello
    spec:
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
                cpu: 200m

Create the Deployment:
    
    
    kubectl apply -f helloweb-deployment.yaml
    

## Expose your application

You can expose your application on GKE using either of the following methods:

  * **Use a Service** , which creates a [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/network) that works with regional IP addresses.

  * **Use an Ingress** , which creates an [Application Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/http) and supports global IP addresses.




To learn more about the advantages and disadvantages of each method, see [Setting up an external Application Load Balancer with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer#background).

### Use a Service

To ensure that your application has a static external IP address, you must [reserve a static IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static).

**Note:** Static IP addresses have no cost when they are used by a load balancer. If you reserve a static IP address and don't use it, you are charged per [unused IP address pricing](https://cloud.google.com/compute/pricing#ipaddress).

If you choose to expose your application using a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), you must create a regional IP address. Global IP addresses only work with Ingress resource type, as explained in the next section.

To use a Service, create a static IP address named `helloweb-ip` in the region `us-central1`:

###  gcloud 
    
    
    gcloud compute addresses create helloweb-ip --region us-central1
    

Find the static IP address that you created:
    
    
    gcloud compute addresses describe helloweb-ip --region us-central1
    

The output is similar to the following:
    
    
    ...
    address: 203.0.113.32
    ...
    

### Config Connector

**Note:** This step requires [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview). Follow the [installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) to install Config Connector on your cluster.
    
    
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: helloweb-ip
    spec:
      location: us-central1

Save the manifest as `compute-address-regional.yaml`.

Apply the manifest to your cluster:
    
    
      kubectl apply -f compute-address-regional.yaml
    

Find the static IP address that you created:
    
    
      kubectl get computeaddress helloweb-ip -o jsonpath='{.spec.address}'
    

The following manifest describes a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) of type LoadBalancer, which creates a regional external passthrough Network Load Balancer to expose Pods with an external IP address.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: helloweb
      labels:
        app: hello
      annotations:
        networking.gke.io/load-balancer-ip-addresses: "helloweb-ip"
    spec:
      selector:
        app: hello
        tier: web
      ports:
      - port: 80
        targetPort: 8080
      type: LoadBalancer

Create the Service:
    
    
    kubectl apply -f helloweb-service-static-ip.yaml
    

View the reserved IP address associated with the load balancer:
    
    
    kubectl get service
    

The output is similar to the following:
    
    
    NAME               CLUSTER-IP      EXTERNAL-IP      PORT(S)          AGE
    helloweb           10.31.254.176   203.0.113.32     80:30690/TCP     54s
    

**Note:** Provisioning and configuring the load balancer might take a few minutes.

### Use an Ingress

If you choose to expose your application using an [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), you must [reserve a global static IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static). Use the annotation `kubernetes.io/ingress.global-static-ip-name` to specify a global IP address.

To expose your application to clients and services in a region, use a regional static internal IP address while deploying an internal ingress resource for GKE along with the [required annotations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#static_ip_addressing).

To learn how to use Ingress to expose your applications to the internet, see [Setting up an external Application Load Balancer with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).

**Note:** Static IP addresses have no cost when they are used by a load balancer. If you reserve a static IP address and don't use it, you are charged per [unused IP address pricing](https://cloud.google.com/compute/pricing#ipaddress).

To create a global static IP address named `helloweb-ip`:

### gcloud
    
    
    gcloud compute addresses create helloweb-ip --global
    

Find the static IP address that you created:
    
    
    gcloud compute addresses describe helloweb-ip --global
    

The output is similar to the following:
    
    
    ...
    address: 203.0.113.32
    ...
    

### Config Connector

**Note:** This step requires [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview). Follow the [installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) to install Config Connector on your cluster.
    
    
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: helloweb-ip
    spec:
      location: global

Save the manifest as `compute-address-global.yaml`.

Apply the manifest to your cluster:
    
    
      kubectl apply -f compute-address-global.yaml
    

The following manifest describes an Ingress that exposes a web application on a static IP with two resources:

  * A `Service` with `type:NodePort`
  * An `Ingress` configured with the service name and static IP annotation


    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: helloweb
      annotations:
        kubernetes.io/ingress.global-static-ip-name: helloweb-ip
      labels:
        app: hello
    spec:
      defaultBackend:
        service:
          name: helloweb-backend
          port:
            number: 8080
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloweb-backend
      labels:
        app: hello
    spec:
      type: NodePort
      selector:
        app: hello
        tier: web
      ports:
      - port: 8080
        targetPort: 8080

The `kubernetes.io/ingress.global-static-ip-name` annotation specifies the name of the global IP address resource to be associated with the load balancer.

Apply the manifest to your cluster:
    
    
    kubectl apply -f helloweb-ingress-static-ip.yaml
    

View the IP address associated with the load balancer:
    
    
    kubectl get ingress
    

The output is similar to the following
    
    
    NAME       HOSTS     ADDRESS          PORTS     AGE
    helloweb   *         203.0.113.32     80        4m
    

**Note:** Provisioning and configuring the load balancer might take a few minutes.

## View your reserved static IP address

To verify that the load balancer is configured correctly, you can either use a web browser to visit the IP address or use `curl`:
    
    
    curl http://203.0.113.32/
    

The output is similar to the following:
    
    
    Hello, world!
    Hostname: helloweb-3766687455-8lvqv
    

**Note:** You might get HTTP 404 and HTTP 500 errors for a few minutes if you used an Ingress to configure a load balancer. It takes time for configuration changes to propagate to regions across the globe.

## Configure your domain name records

To have browsers querying your domain name, such as `example.com`, or subdomain name, such as `blog.example.com`, point to the static IP address you reserved, you must update the DNS (Domain Name Server) records of your domain name.

You must create an **A** (Address) type DNS record for your domain or subdomain name and have its value configured with the reserved IP address

DNS records of your domain are managed by your name server. Your name server might be the "registrar" where you registered your domain, a DNS service such as [Cloud DNS](https://docs.cloud.google.com/dns), or another third-party provider.

  * **If your nameserver is Cloud DNS:** Follow [Cloud DNS Quickstart guide](https://docs.cloud.google.com/dns/quickstart#create_a_new_record) to configure DNS A record for your domain name with the reserved IP address of your application.

  * **If your nameserver is another provider:** Refer to your DNS providers documentation on setting DNS A records to configure your domain name. If you choose to use Cloud DNS instead, refer to [Migrating to Cloud DNS](https://docs.cloud.google.com/dns/migrating).




## Visit your domain name

To verify that your domain name's DNS A records resolve to the IP address you reserved, visit your domain name.

**Note:** It can take a few hours for DNS records to propagate. This time might depend on your name servers, local internet service provider (ISP), and many other factors.

To make a DNS query for your domain name's A record, run the `host` command:
    
    
    host example.com
    

The output is similar to the following:
    
    
    example.com has address 203.0.113.32
    

You can now point your web browser to your domain name and visit your website.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Delete the Service and Ingress:
         
         kubectl delete ingress,service -l app=hello
         

  2. Release the reserved static IP. After the load balancer is deleted, the unused but reserved IP address is billed per unused IP address pricing.

     * If you used a Service:
           
           gcloud compute addresses delete helloweb-ip --region us-central1
           

     * If you used an Ingress:
           
           gcloud compute addresses delete helloweb-ip --global
           

  3. Delete the sample application:
         
         kubectl delete -f helloweb-deployment.yaml
         

  4. Delete the cluster:
         
         gcloud container clusters delete domain-test
         




## What's next

  * Learn how to [set up an external Application Load Balancer with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).
  * Learn more about [GKE Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress).
  * Learn how to [use Google-managed SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs).
  * Explore other [Kubernetes Engine tutorials](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials). 
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
