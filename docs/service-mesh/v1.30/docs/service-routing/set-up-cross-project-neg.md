---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/set-up-cross-project-neg/
title: Set up cross-project network endpoint group \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:13.275719+00:00
---

# Set up cross-project network endpoint group  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/set-up-cross-project-neg/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up cross-project network endpoint group

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview).

The cross-project network endpoint group (NEG) feature allows customers to attach NEGs from a different project to a Traffic Director/Cloud Service Mesh `BackendService`, enabling the following use cases:

  * In a multi-project deployment, `BackendServices` along with their associated routing and traffic policies in a centralized project. with backend endpoints from different projects.

  * In a multi-project deployment, you can manage all your compute resources (Compute Engine VMs, GKE NEGs, etc) in a single, central Google Cloud project while Service teams own their own Google Cloud service projects where they define service policies expressed in `BackendServices` and Service routing Routes in their respective service project. This delegates managing their services while maintaining close control over the compute resources which may be shared between different service teams.




This page shows you how to create a baseline 2-project setup where the NEG in project B (referred to as the workload project) is attached to the `BackendService` in project A (referred to as the policy project). The following example sets up workload VMs in the default VPC network in the workload project and demonstrates that the client can route to in the workload project based on the configurations in the policy project.

![Baseline cross-project NEG example](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/baseline-backendservice-neg-example.png)

In a more sophisticated setup, a solution such as Shared VPC is required for an interconnected dataplane across multiple projects. This also implies that NEG endpoints have unique IPs. This example setup can be extended to more complicated scenarios where workloads are in a Shared VPC network spanning multiple projects.

## Limitations

The general [Traffic Director limitations](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/service-routing-overview#considerations_and_limitations) and [BackendService/NetworkEndpointGroup limitations](https://docs.cloud.google.com/load-balancing/docs/quotas) apply.

The following limitations also apply but may not be specific to a multi-project setup:

  * A single BackendService can only support up to 50 backends(including NEGs, MIGs).
  * Only zonal NEGs of type GCP_VM_IP_PORT are supported.
  * Cross project BackendServices to instance groups (managed or unmanaged) reference is not supported.
  * Listing cross-project NEGs that can be attached to a given BackendService is not supported.
  * Listing cross-project BackendServices that are using a specific NEG is not supported.



## Before you begin

You must complete the following prerequisites before you can set up cross-project NEGs.

### Enable the required APIs

The following APIs are required to complete this guide:

  * osconfig.googleapis.com
  * trafficdirector.googleapis.com
  * compute.googleapis.com
  * networkservices.googleapis.com



Run the following command to enable the required APIs in both the workload project and the policy project:
    
    
    gcloud services enable --project PROJECT_ID \
        osconfig.googleapis.com \
        trafficdirector.googleapis.com \
        compute.googleapis.com \
        networkservices.googleapis.com
    

### Grant the required IAM permissions

You must have sufficient Identity and Access Management (IAM) permissions to complete this guide. If you have the role of project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`) in the project where you are enabling Cloud Service Mesh, you automatically have the correct permissions.

Otherwise, you must grant all of the following IAM roles. If you have these roles, you also have their associated permissions, as described in the [Compute Engine IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).

The following roles are required in **both** workload and policy projects:

  * roles/iam.serviceAccountAdmin
  * roles/serviceusage.serviceUsageAdmin
  * roles/compute.networkAdmin



The following roles are required in the workload project only:

  * roles/compute.securityAdmin
  * roles/container.admin
  * Any role that includes the following permissions. The most granular predefined role that include all the required permission for attaching a NEG to a BackendService is roles/compute.loadBalancerServiceUser 
    * compute.networkEndpointGroups.get
    * compute.networkEndpointGroups.use



Additionally, Traffic Director managed xDS clients (like Envoy proxy) must have the permissions under `roles/trafficdirector.client`. For demonstration purposes, you can use the following command to grant this permission in the policy project to the default compute service account of the workload project:
    
    
    gcloud projects add-iam-policy-binding POLICY_PROJECT_ID \
        --member "serviceAccount:WORKLOAD_PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
        --role "roles/trafficdirector.client"
    

where

  * POLICY_PROJECT_ID is the ID of the policy project.
  * WORKLOAD_PROJECT_NUMBER is the project number of the workload project.



## Configure a service backend in the workload project

  1. Run the following command to point your Google Cloud CLI to the workload project and set the preferred Google Cloud compute zone:
         
         gcloud config set project WORKLOAD_PROJECT_ID
         gcloud config set compute/zone ZONE
         

where

     * WORKLOAD_PROJECT_ID is the ID of the workload project.
     * ZONE is the zone of the GKE cluster, for example `us-central1`.
  2. Create a GKE cluster. For demonstration purposes, the following command creates a zonal GKE cluster. However, this feature also works on regional GKE clusters.
         
         gcloud container clusters create test-cluster \
             --scopes=https://www.googleapis.com/auth/cloud-platform
             --zone=ZONE
         

  3. Create a firewall rule:
         
         gcloud compute firewall-rules create http-allow-health-checks \
             --network=default \
             --action=ALLOW \
             --direction=INGRESS \
             --source-ranges=35.191.0.0/16,130.211.0.0/22 \
             --rules=tcp:80
         

A firewall rule allows the Google Cloud control plane to send health check probes to backends in the default VPC network.

  4. Change the current context for kubectl to the newly created cluster:
         
         gcloud container clusters get-credentials test-cluster \
             --zone=ZONE
         

  5. Create and deploy the whereami sample app:
         
         kubectl apply -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: whereami
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: whereami
           template:
             metadata:
               labels:
                 app: whereami
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                 - containerPort: 8080
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: whereami
           annotations:
             cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-neg"}}}'
         spec:
           selector:
             app: whereami
           ports:
           - port: 8080
             targetPort: 8080
         EOF
         

  6. Run the following command to store the reference to the NEG in a variable:
         
         NEG_LINK=$(gcloud compute network-endpoint-groups describe example-neg --format="value(selfLink)")
         

The NEG controller automatically creates a zonal NetworkEndpointGroup for the service backends in each zone. In this example, the NEG name is hardcoded to example-neg. Storing it as a variable will be useful in the next session when attaching this NEG to a BackendService in the policy project.

If you example $NEG_LINK, it should look similar to the following:
         
         $ echo ${NEG_LINK}
         https://www.googleapis.com/compute/v1/projects/WORKLOAD_PROJECT/zones/ZONE/networkEndpointGroups/example-neg
         

Alternatively, you can retrieve the NEG URL by reading the neg-status annotation on the service:
         
         kubectl get service whereami -o jsonpath="{.metadata.annotations['cloud\.google\.com/neg-status']}"
         NEG_LINK="https://www.googleapis.com/compute/v1/projects/WORKLOAD_PROJECT_ID/zones/ZONE/networkEndpointGroups/example-neg"
         




## Configure Google Cloud networking resources in the policy project

  1. Point your Google Cloud CLI to the policy project:
         
         gcloud config set project POLICY_PROJECT_ID
         

  2. Configures a mesh resource:
         
         gcloud network-services meshes import example-mesh --source=- --location=global << EOF
         name: example-mesh
         EOF
         

The name of the mesh resource is the key that sidecar proxies use to request the configuration of the service mesh.

  3. Configure a baseline `BackendService` with a health check:
         
         gcloud compute health-checks create http http-example-health-check
         
         gcloud compute backend-services create example-service \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --protocol=HTTP \
           --health-checks http-example-health-check
         

  4. Attaches the `NetworkEndpointGroup` created in the previous section to the `BackendService`:
         
         gcloud compute backend-services add-backend example-service --global \
           --network-endpoint-group=${NEG_LINK} \
           --balancing-mode=RATE \
           --max-rate-per-endpoint=5
         

  5. Create an HTTPRoute to direct all HTTP requests with host header `example-service` to the server in the workload project:
         
         gcloud network-services http-routes import example-route --source=- --location=global << EOF
         name: example-route
         hostnames:
         - example-service
         meshes:
         - projects/POLICY_PROJECT_NUMBER/locations/global/meshes/example-mesh
         rules:
         - action:
             destinations:
             - serviceName: "projects/POLICY_PROJECT_NUMBER/locations/global/backendServices/example-service"
         EOF
         

where POLICY_PROJECT_NUMBER is the project number of the policy project.




## Verify the setup

You can verify the setup by sending an HTTP request with HOST header set to `example-service` to a VIP behind a Traffic Director managed sidecar proxy:
    
    
    curl -H "Host: example-service" http://10.0.0.1/
    

The output is similar to:
    
    
    {"cluster_name":"test-cluster","gce_instance_id":"4879146330986909656","gce_service_account":"...","host_header":"example-service","pod_name":"whereami-7fbffd489-nhkfg","pod_name_emoji":"...","project_id":"...","timestamp":"2024-10-15T00:42:22","zone":"us-west1-a"}
    

Note that since all outbound traffic from Pods are intercepted by an Envoy sidecar in a service mesh, and the previous HTTPRoute is configured to send all traffic to the "whereami" Kubernetes Service purely based on the L7 attribute (host header). For example purposes the VIP in this command is 10.0.0.1, but the VIP can be any IP.

The sidecar proxy should request configurations associated with the mesh resource in the policy project. To do so, make sure the Node ID is set in the following format:
    
    
    projects/POLICY_PROJECT_NUMBER/networks/mesh:example-mesh/nodes/UUID"
    

## What's next

  * [Set up cross-project mesh route](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/set-up-cross-project-mesh-route)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
