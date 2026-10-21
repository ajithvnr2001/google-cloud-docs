---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/route-to-cloud-run/
title: Route traffic from Cloud Service Mesh workloads to Cloud Run Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:02.778942+00:00
---

# Route traffic from Cloud Service Mesh workloads to Cloud Run Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/route-to-cloud-run/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Route traffic from Cloud Service Mesh workloads to Cloud Run Services

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

This page shows you how to securely route network traffic from Cloud Service Mesh workloads on GKE to Cloud Run Services.

Note that when routing traffic from GKE to Cloud Run, it is not required to have Cloud Run Service join the Cloud Service Mesh. However, the Cloud Run Service must be in the same project as the Cloud Service Mesh GKE cluster. This limitation exists while this feature is available in public preview.

## Before you begin

The following sections assume that you have:

  1. [A GKE cluster with Cloud Service Mesh enabled](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/provision-control-plane).
  2. [Deployed a Cloud Run service](https://cloud.google.com/run/docs).



Alternatively, you can run the following commands to deploy a sample Cloud Run service.

  1. Generate a kubeconfig context for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME --project=PROJECT_ID  --location=CLUSTER_LOCATION
         

Where:

     * CLUSTER_NAME is the name of the your cluster.
     * PROJECT_ID is the project ID of your project.
     * CLUSTER_LOCATION is the region or zone of your cluster.
  2. Deploy a sample Cloud Run service:
         
         gcloud run deploy hello-world \
           --image=us-docker.pkg.dev/cloudrun/container/hello \
           --no-allow-unauthenticated \
           --port=8080 \
           --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --region=us-central1 \
           --project=PROJECT_ID
         

Where:

     * PROJECT_NUMBER is the project number of the your project.
     * PROJECT_ID is the project ID of your project.



## Configure IAM

To invoke Cloud Run services, Cloud Run Identity and Access Management (IAM) checks must pass. You must grant the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) to the Google Service Account. You must also configure the GKE Kubernetes Service Account (KSA) to impersonate the Google Service Account.

Perform the following steps to allow a Kubernetes Service Account to impersonate a Google Service Account.

  1. Add an IAM policy binding to an IAM service account:
         
         gcloud iam service-accounts add-iam-policy-binding PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KSA]"
         

Where:

     * NAMESPACE is the namespace name. For the purposes of this guide, you can use the namespace `default`.
     * KSA is the name of the Kubernetes Service Account. For the purposes of this guide, you can use the KSA `default`.
  2. Annotate the service account:
         
         kubectl annotate serviceaccount KSA \
           --namespace NAMESPACE \
           iam.gke.io/gcp-service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com
         

  3. Grant the Cloud Run Invoker Role to the Google Service Account:
         
         gcloud run services add-iam-policy-binding hello-world \
           --region=us-central1 \
           --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
           --role="roles/run.invoker"
         




## Configure a Cloud Run Service as a GCPBackend

In this section, you expose the Cloud Run service to the GKE workloads using GCPBackend. The GCPBackend consists of:

  1. Frontend information - specifically, the hostname and port that GKE Workloads would use to call this GCPBackend.
  2. Backend information - the Cloud Run Service details such as service name, location, and project number.



The GCPBackend contains the hostname and port details as well as the Cloud Service details (service name, location, and project number). The GKE workloads should use the GCPBackend hostname and port in their HTTP requests to access the Cloud Run Service.

To make the hostname DNS resolvable within the cluster (by default it isn't resolvable), you must configure Google Cloud DNS to resolves all hosts under a chosen hostname to an arbitrary IP address. Until you configure this DNS entry, the request fails. The Google Cloud DNS configuration is a one-time setup per custom domain.

  1. Create a managed-zone:
         
         gcloud dns managed-zones create prod \
             --description="zone for gcpbackend" \
             --dns-name=gcpbackend \
             --visibility=private \
             --networks=default
         

In this example the DNS Name is gcpbackend and the VPC Network is default.

  2. Set up the record to make the domain resolvable:
         
         gcloud beta dns record-sets create *.gcpbackend \
           --ttl=3600 --type=A --zone=prod \
           --rrdatas=10.0.0.1
         

  3. Create the GCPBackend with a hostname under the previous domain:
         
         cat <<EOF > gcp-backend.yaml
         apiVersion: networking.gke.io/v1
         kind: GCPBackend
         metadata:
           name: cr-gcp-backend
           namespace: NAMESPACE
         spec:
           hostname: hello-world.gcpbackend
           type: CloudRun
           cloudrun:
             service: hello-world
             regions: [us-central1]
         EOF
         kubectl apply -f gcp-backend.yaml
         

In this example GCP_BACKEND_NAME is `cr-gcp-backend`.

  4. Create a testing Pod to verify GKE to Cloud Run connectivity:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: v1
         kind: Pod
         metadata:
           name: testcurl
           namespace: default
         spec:
           containers:
           - name: curl
             image: curlimages/curl
             command: ["sleep", "3000"]
         EOF
         
         kubectl exec testcurl -c curl -- curl http://hello-world.gcpbackend/hello
         

Now, your GKE workloads may access the Cloud Run Service by sending HTTP requests to **hello-world.gcpbackend/hello**.




You should use distinct names for GCPBackend to avoid conflicting with existing Kubernetes services or Istio Service Entries. If it does conflict, the precedence order (high to low) is Kubernetes Service, istio ServiceEntry, and GCPBackend.

Note that the Virtual Service and the GCPBackend must be in the same namespace and the Cloud Run Service must be in the same project as the Cloud Service Mesh GKE cluster.

## (Optional) Use Cloud Run's hostname instead of Cloud DNS

Every Cloud Run Service is assigned a hostname (for example, hello-world.us-central1.run.app) and is DNS resolvable globally. You can use this hostname directly in the GCPBackend hostname and skip the Cloud DNS configuration.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: networking.gke.io/v1
    kind: GCPBackend
    metadata:
      name: cr-gcp-backend
      namespace: NAMESPACE
    spec:
      hostname: hello-world.us-central1.run.app
      type: CloudRun
      cloudrun:
        service: hello-world
        region: [us-central1]
    EOF
    

Now, your GKE workloads may access the Cloud Run Service by sending HTTP requests to **hello-world.us-central1.run.app**.

## (Optional) Configure Istio Virtual Service and or Destination Rule

You can configure Istio Virtual Service or Istio Destination Rule for the GCPBackend Hostname to set consumer or client policies for requests to the GCPBackend.

The following example injects a delay of 5s to 50% of the requests and abort (503 http status) to 10% of the requests going to the GCPBackend.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: cr-virtual-service
      namespace: NAMESPACE
    spec:
      hosts:
      - hello-world.us-central1.run.app
      gateways:
      - mesh
      http:
      - fault:
          delay:
            percentage:
              value: 50  # Delay 50% of requests
            fixedDelay: 5s
          abort:
            percentage:
              value: 10  # Abort 10% of requests
            httpStatus: 503
      - route:
        - destination:
            host: hello-world.us-central1.run.app
    EOF
    

In this example VIRTUAL_SERVICE_NAME is `cr-virtual-service`.

## Troubleshooting

This section shows you how to troubleshoot common errors with Cloud Service Mesh and Cloud Run.

### Cloud Run Sidecar Logs

Envoy errors are logged in Cloud Logging.

For example an error such as the following will be logged if the Cloud Run service account is not given the trafficdirector client role in the mesh project:
    
    
    StreamAggregatedResources gRPC config stream to trafficdirector.googleapis.com:443 closed: 7, Permission 'trafficdirector.networks.getConfigs' denied on resource '//trafficdirector.googleapis.com/projects/525300120045/networks/mesh:test-mesh/nodes/003fb3e0c8927482de85f052444d5e1cd4b3956e82b00f255fbea1e114e1c0208dbd6a19cc41694d2a271d1ab04b63ce7439492672de4499a92bb979853935b03d0ad0' (or it may not exist).
    

### CSDS

The trafficdirector client state can be retrieved using CSDS:
    
    
    gcloud alpha container fleet mesh debug proxy-status --membership=<CLUSTER_MEMBERSHIP> --location=<CLUSTER_LOCATION>
    External Clients:
    ....
    

## What's next

  * [Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE](https://docs.cloud.google.com/service-mesh/v1.27/docs/route-from-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
