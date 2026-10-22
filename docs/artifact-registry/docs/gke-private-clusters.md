---
url: https://docs.cloud.google.com/artifact-registry/docs/gke-private-clusters/
title: Configure restricted access for GKE private clusters \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:21.485502+00:00
---

# Configure restricted access for GKE private clusters  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/gke-private-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure restricted access for GKE private clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure DNS entries to route requests to the `pkg.dev` and `gcr.io` domains using a restricted virtual IP (VIP) when you use [Google Kubernetes Engine private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) in a VPC Service Controls service perimeter. 

Registry domains normally resolve to a public IP address on the internet. In GKE private clusters, nodes are isolated from the internet by default. This means that requests to registry domains will fail when you have not configured DNS routing to the restricted VIP.

Your private clusters should always access Artifact Registry or Container Registry with the restricted VIP to prevent data exfiltration from a supported service to an unsupported one. 

Configure restricted access for GKE private clusters when all of the following are true:

  * You're using GKE private clusters.
  * You haven't already configured routing of the `pkg.dev` or `gcr.io` registry domains to `restricted.googleapis.com`.



## Before you begin

Before you create a service perimeter, [set up a new private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) or identify the existing private clusters that you want to protect.

Also, you must permit egress to 199.36.153.4/30 on port 443. Normally, a VPC network has an implied rule that allows all egress traffic to any destination. However, if you have a rule denying such traffic, you must create an egress firewall rule to allow TCP traffic on port 443 to 199.36.153.4/30.

## Configuring DNS

Configure your DNS server so that requests to registry addresses resolve to `restricted.googleapis.com`, the restricted VIP. You can do so using Cloud DNS private DNS zones.

  1. Create a managed private zone.
         
         gcloud dns managed-zones create ZONE_NAME \
             --visibility=private \
             --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK \
             --description=DESCRIPTION \
             --dns-name=REGISTRY_DOMAIN \
             --project=PROJECT_ID
         

Where:

     * `ZONE_NAME` is a name for the zone you are creating. For example, `registry`. This name will be used in each of the following steps.
     * `PROJECT_ID` is the ID of the project that hosts your GKE private cluster.
     * `NETWORK` is an optional list of names of the cluster network that you want to redirect requests from.
     * `DESCRIPTION` is a human-readable description of the managed zone.
     * `REGISTRY_DOMAIN` is the domain for your registry: 
       * `pkg.dev` for Artifact Registry
       * `gcr.io` for Container Registry or `gcr.io` repositories hosted in Artifact Registry
  2. Start a transaction.
         
         gcloud dns record-sets transaction start \
           --zone=ZONE_NAME \
           --project=PROJECT_ID
         

Where:

     * ZONE_NAME is the name of the zone you created in the first step.

     * PROJECT_ID is the ID of the project that hosts your GKE private cluster.

  3. Add a CNAME record for your registry.
         
         gcloud dns record-sets transaction add \
           --name=*.REGISTRY_DOMAIN. \
           --type=CNAME REGISTRY_DOMAIN. \
           --zone=ZONE_NAME \
           --ttl=300 \
           --project=PROJECT_ID
         

Where:

     * `ZONE_NAME` is the name of the zone you created in the first step.
     * `PROJECT_ID` is the ID of the project that hosts your GKE private cluster.
     * `REGISTRY_DOMAIN` is the domain for your registry: 
       * `pkg.dev` for Artifact Registry
       * `gcr.io` for Container Registry or `gcr.io` repositories hosted in Artifact Registry
  4. Add an A record for the restricted VIP.
         
         gcloud dns record-sets transaction add \
           --name=REGISTRY_DOMAIN. \
           --type=A 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
           --zone=ZONE_NAME \
           --ttl=300 \
           --project=PROJECT_ID
         

Where:

     * `ZONE_NAME` is the name of the zone you created in the first step.
     * `PROJECT_ID` is the ID of the project that hosts your GKE private cluster.
     * `REGISTRY_DOMAIN` is the domain for your registry: 
       * `pkg.dev` for Artifact Registry
       * `gcr.io` for Container Registry or `gcr.io` repositories hosted in Artifact Registry
  5. Execute the transaction.
         
         gcloud dns record-sets transaction execute \
           --zone=ZONE_NAME \
           --project=PROJECT_ID
         

Where:

     * ZONE_NAME is the name of the zone you created in the first step.

     * PROJECT_ID is the ID of the project that hosts your GKE private cluster.




After you have configured DNS routing, ensure that your GKE, the registry, and other required services are inside your VPC Service Controls service perimeter. To configure your service perimeter, see the following section.

## Configuring the service perimeter

After configuring the DNS records, do the following:

  1. [Create a new service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) or [update an existing perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters). 
  2. Add the Container Registry or Artifact Registry service to the list of services you want to protect using the service perimeter.
  3. Add other [supported services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) that you use with the registry to the service perimeter, such as Cloud Build, Artifact Analysis, and Binary Authorization.
  4. If you need to access Container Registry, then you must also add Cloud Storage to the service perimeter.



## Verifying the perimeter works

After configuring the service perimeter, your nodes in GKE private clusters can access container images in Artifact Registry and Container Registry if the images are stored in projects that are in your service perimeter. 

Container images in projects outside the perimeter remain inaccessible, except for some [specific read-only public repositories](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_artifacts).

For example, if the `google-samples` project is not in your service perimeter, running the command to create a deployment from the `hello-app` container will fail:

###  pkg.dev domain 
    
    
    kubectl create deployment hello-server --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

###  gcr.io domain 
    
    
    kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
    

Check the status of the pod with the command:
    
    
    kubectl get pods
    

The command returns a table similar to the following example. The pod status `ErrImagePull` indicates that the pull failed.
    
    
    NAME                            READY   STATUS         RESTARTS   AGE
    hello-server-dbd86c8c4-h5wsf    1/1     ErrImagePull   0          45s
    

You can use the `kubectl describe pod` command to see more details about the deployment. For the pod in the previous example, the command is:
    
    
    kubectl describe pod hello-server-dbd86c8c4-h5wsf
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
