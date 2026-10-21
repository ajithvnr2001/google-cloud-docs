---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/configure-cloud-service-mesh-for-cloud-run/
title: Configure Cloud Service Mesh for Cloud Run \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:27.595791+00:00
---

# Configure Cloud Service Mesh for Cloud Run  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/configure-cloud-service-mesh-for-cloud-run/

You are viewing archived v1.25 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Cloud Service Mesh for Cloud Run

**Preview — Cloud Service Mesh for Cloud Run**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows how to configure Cloud Service Mesh to run on a range of computing infrastructures for Cloud Run services.

Cloud Service Mesh lets you enable mesh [advanced traffic management capabilities](https://docs.cloud.google.com/service-mesh/docs/advanced-traffic-management), such as weighted traffic splitting and global load balancing, as well as observability and security policies for traffic from one Cloud Run service to another. It also gives you a fully managed data plane solution that removes the operational burden of maintaining your own service mesh sidecars.

## Before you begin

  1. Have familiarity with [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

  2. Set your project:
         
         gcloud config set core/project PROJECT_ID

  3. In the Google Cloud console, enable the following APIs for your project:

     * [Cloud DNS API](https://console.cloud.google.com/apis/library/dns.googleapis.com)

     * [Network Services API](https://console.cloud.google.com/apis/library/networkservices.googleapis.com)

     * [Network Security API](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com)

     * [Traffic Director API](https://console.cloud.google.com/apis/library/trafficdirector.googleapis.com)

     * [Serverless VPC Access API](https://console.cloud.google.com/apis/library/vpcaccess.googleapis.com)

If you're using a Serverless VPC Access connector and not Direct VPC for network egress.

  4. Update `gcloud` components to the latest version (488.0.0 or above):
         
         gcloud components update




### Limitations

Cloud Run services using Cloud Service Mesh may experience increased cold start latency. Refer to the [General development tips](https://docs.cloud.google.com/run/docs/tips/general#optimize_performance) section in the Cloud Run documentation for advice on improving startup times.

### Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



The Cloud Run client's service account must also have the following roles:

  * [Traffic Director Client](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.client) (`roles/trafficdirector.client`) to access the [service routing APIs](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview)
  * [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) to enable tracing



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Call between Cloud Run services using Cloud Service Mesh

Cloud Run uses the Cloud Service Mesh [service routing APIs](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview). These APIs let a Cloud Run service call other Cloud Run services using a customized URL rather than the provided `run.app` URL. In addition, Cloud Run automatically authenticates to the destination Cloud Run service so that you don't have to configure your own authentication to attach request credentials to other Cloud Run services.

To call from one Cloud Run service to another using Cloud Service Mesh, follow these steps:

  1. Set up a Cloud Service Mesh
  2. Set up Cloud DNS
  3. Create the destination Cloud Run service
  4. Create the serverless NEG
  5. Create the client Cloud Run service
  6. Call the service from the mesh client



### Set up a Cloud Service Mesh

  1. To create a service route using the default URL, save the `Mesh` specification in a file called `mesh.yaml`:
         
         name: MESH_NAME

Replace `MESH_NAME` with the [mesh resource](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview#mesh-resource) name.

  2. Import the `Mesh` resource from the specification by running the following command:
         
         gcloud network-services meshes import MESH_NAME \
           --source=mesh.yaml \
           --location=global

Replace `MESH_NAME` with the [mesh resource](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview#mesh-resource) name.




### Set up Cloud DNS

**Note:** Cloud DNS is a paid service. See [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

You can skip Cloud DNS setup and go to the [next section](https://docs.cloud.google.com/service-mesh/v1.25/docs/configure-cloud-service-mesh-for-cloud-run#internal) if you use a [Private Service Connect endpoint](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc) with the full `run.app` URL address as the hostname because only private IP addresses are captured.

When a mesh client calls the destination service, the hostname used in the request must be resolvable through DNS. Any valid [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3) IP address is acceptable because the sidecar captures all IP traffic to these IP address ranges and redirects it appropriately.

The following example shows how to create a wildcard `*` entry in the Cloud DNS zone that resolves to a single IP address. If you don't want to use an exclusive Cloud DNS zone, [create a Cloud DNS entry](https://docs.cloud.google.com/dns/docs/records#add_a_record) for every hostname corresponding to the Cloud Run services that you want to be addressable from the mesh.

  * To create a Cloud DNS record in an exclusive zone, run the following commands:

    1. Create a private managed DNS zone in Cloud DNS for a service mesh.
           
           gcloud dns managed-zones create MESH_NAME \
           --description="Domain for DOMAIN_NAME service mesh routes" \
           --dns-name=DOMAIN_NAME. \
           --networks=VPC_NETWORK_NAME \
           --visibility=private

    2. Create a DNS record within the newly created private managed zone. Make sure that the IP address `10.0.0.1` is unused.
           
           gcloud dns record-sets create "*.DOMAIN_NAME." \
           --type=A \
           --zone="MESH_NAME" \
           --rrdatas=10.0.0.1 \
           --ttl=3600

Replace the following:

       * `DOMAIN_NAME`: the name of the DNS domain.
       * `MESH_NAME`: the mesh resource name.
       * `VPC_NETWORK_NAME`: the name of your VPC network; for example, "default".



### Access internal services with Cloud Service Mesh

Cloud Run lets you restrict incoming network traffic to "internal." If your service has this ingress restriction enabled, traffic that travels from your mesh through the Virtual Private Cloud network can be set as "internal" when you enable an access path to Cloud Run.

To access internal services with Cloud Service Mesh, use one of the following methods:

  * [Configure Private Google Access for your VPC network](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). You don't need to set up a custom DNS record.
  * [Attach a Private Service Connect endpoint to Cloud Service Mesh](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc). This requires custom DNS record setup for the default `*.run.app` URL to use the Private Service Connect endpoint address.



### Create the destination Cloud Run service

Note that the Cloud Run destination cannot have the [default URL disabled](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url).

  1. Deploy a new or existing Cloud Run service:
         
         gcloud run deploy DESTINATION_SERVICE_NAME \
         --no-allow-unauthenticated \
         --region=REGION \
         --image=IMAGE_URL 

Replace the following:

     * `DESTINATION_SERVICE_NAME`: the name of the destination Cloud Run service.
     * `REGION`: the name of the region.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.



### Create the serverless network endpoint group (NEG)

  1. Create the destination NEG by running the following command:
         
         gcloud compute network-endpoint-groups create DESTINATION_SERVICE_NAME-neg \
         --region=REGION \
         --network-endpoint-type=serverless \
         --cloud-run-service=DESTINATION_SERVICE_NAME

Replace the following:

     * `REGION`: the name of the region.
     * `DESTINATION_SERVICE_NAME`: the name of the destination Cloud Run service.
  2. Create an internal self-managed backend service that references the serverless NEG.

     1. Create the backend service:
            
            gcloud compute backend-services create DESTINATION_SERVICE_NAME-REGION \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED

Replace `DESTINATION_SERVICE_NAME` with the name of the destination service and `REGION` with the name of the region.

     2. Add the serverless backend to the backend service:
            
            gcloud compute backend-services add-backend DESTINATION_SERVICE_NAME-REGION \
            --global \
            --network-endpoint-group=DESTINATION_SERVICE_NAME-neg \
            --network-endpoint-group-region=REGION

Replace `DESTINATION_SERVICE_NAME` with the name of the destination service and `REGION` with the name of the region.

  3. Create an HTTP route that references the backend service.

The `Mesh` resource and services are configured. Connect them with an `HTTPRoute` resource that associates a hostname with a backend service.

     1. Create the `HTTPRoute` specification and save it to a file called `http_route.yaml`:
            
            name: "DESTINATION_SERVICE_NAME-route"
            hostnames:
            - "DESTINATION_SERVICE_NAME.DOMAIN_NAME"
            meshes:
            - "projects/PROJECT_ID/locations/global/meshes/MESH_NAME"
            rules:
            - action:
               destinations:
               - serviceName: "projects/PROJECT_ID/locations/global/backendServices/DESTINATION_SERVICE_NAME-REGION"
            

Set the hostnames to the names that you'd like to use to address the service. All clients within the same service mesh can call this service using the `http://<HOSTNAME>` URL, regardless of the region and project of the caller. If you've set up Cloud DNS to use a private IP address, the route hostname can also be the full `run.app` URL address—in which case, you can skip the Cloud DNS setup step.

Replace the following:

        * `DESTINATION_SERVICE_NAME`: the name of the destination Cloud Run service.
        * `DOMAIN_NAME`: the name of the DNS domain.
        * `PROJECT_ID`: the ID of the project.
        * `MESH_NAME`: the name of the mesh.
        * `REGION`: the name of the region.
     2. Create the `HTTPRoute` resource by using the specification in the `http_route.yaml` file:
            
            gcloud network-services http-routes import DESTINATION_SERVICE_NAME-route \
            --source=http_route.yaml \
            --location=global
            

     3. Grant the [Cloud Run Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/iam.invoker`) on the Cloud Run destination service by running the following command:
            
            gcloud run services add-iam-policy-binding DESTINATION_SERVICE_NAME \
            --region REGION \
            --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
            --role=roles/run.invoker

Replace the following:

        * `DESTINATION_SERVICE_NAME`: the name of the destination Cloud Run service.
        * `REGION`: the name of the region.
        * `PROJECT_NUMBER`: the number of the project.



### Create the client Cloud Run service

Creating a client Cloud Run service creates an [Envoy sidecar](https://www.envoyproxy.io/) whose resources relate to your QPS and total configuration size. Most of the time, CPU usage is less than 1 percent of a vCPU and memory usage is less than 50 MB.

You must have [network egress](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) access to a Virtual Private Cloud network.

  * To create the client service for testing, deploy the fortio app in Cloud Run to allow forwarding traffic to HTTP routes:
        
        gcloud beta run deploy CLIENT_SERVICE_NAME \
        --region=REGION \
        --image=fortio/fortio \
        --network=VPC_NETWORK_NAME \
        --subnet=SUBNET_NAME \
        --mesh="projects/PROJECT_ID/locations/global/meshes/MESH_NAME"

Replace the following:

    * `CLIENT_SERVICE_NAME`: the name of the client Cloud Run service.
    * `REGION`: the name of your region.
    * `VPC_NETWORK_NAME`: the name of your VPC network; for example, "default".
    * `SUBNET_NAME`: the name of your subnet; for example, "default".
    * `PROJECT_ID`: the ID of your project.
    * `MESH_NAME`: the [mesh resource](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview#mesh-resource) name.
**Note:** If your container fails to start, make sure that you've enabled all APIs. You might also need to give your service account access to Traffic Director by running the following command: 
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com --role=roles/trafficdirector.client




### Call service from a mesh client

To forward a request to the destination route by using the fortio test app from the previous Create client service section:

  1. Fetch the URL of the Cloud Run client service that you created by running the following command:
         
         TEST_SERVICE_URL=$(gcloud run services describe CLIENT_SERVICE_NAME \
         --region=REGION --format="value(status.url)" \
         --project=PROJECT_ID)

Replace the following:

     * `CLIENT_SERVICE_NAME`: the name of the client Cloud Run service.
     * `REGION`: the name of your region.
     * `PROJECT_ID`: the ID of your project.
  2. Use the `curl` command to send a request to the destination route of the fortio endpoint from the previous step:
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" "$TEST_SERVICE_URL/fortio/fetch/DESTINATION_SERVICE_NAME.DOMAIN_NAME"

Replace the following:

     * `DESTINATION_SERVICE_NAME`: the name of the destination Cloud Run service.
     * `DOMAIN_NAME`: the name of the DNS domain.



## Call Compute Engine backend from Cloud Run

To deploy a Compute Engine and Cloud Service Mesh service route using managed instance groups as backends, [configure the Compute Engine-based HTTP server in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-envoy-http-mesh#config-server). This lets Cloud Run clients use this backend service route to send requests directly to Compute Engine instances.

## Next steps

  * [Explore common Cloud Run networking configurations](https://services.google.com/fh/files/misc/serverless_networking_guide.pdf) for public and private networking
  * [Configure private networking for Cloud Run ](https://docs.cloud.google.com/run/docs/securing/private-networking)
  * [Set up Envoy proxies with HTTP services](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-envoy-http-mesh)
  * [Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE](https://docs.cloud.google.com/service-mesh/v1.25/docs/route-from-cloud-run)
  * [Route traffic from Cloud Service Mesh workloads to Cloud Run Services](https://docs.cloud.google.com/service-mesh/v1.25/docs/route-to-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
