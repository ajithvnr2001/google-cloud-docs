---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/route-to-gce-vms/
title: Route traffic from Cloud Service Mesh workloads to Compute Engine VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:47.763311+00:00
---

# Route traffic from Cloud Service Mesh workloads to Compute Engine VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/route-to-gce-vms/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Route traffic from Cloud Service Mesh workloads to Compute Engine VM

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview).

This page shows you how to securely route network traffic from Cloud Service Mesh workloads on GKE to Compute Engine VM fronted by a BackendService.

Note that when routing traffic from GKE to a Compute Engine VM, it is not required to have the Compute Engine VM or BackendService join the Cloud Service Mesh. However, the Compute Engine VM and BackendService must be in the same project as the Cloud Service Mesh GKE cluster. This limitation exists while this feature is available in public preview. MTLS isn't supported for Compute Engine VMs

## Before you begin

The following sections assume that you have:

  1. [A GKE cluster with Cloud Service Mesh enabled](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/provision-control-plane).
  2. [Deployed a Compute Engine VM that is fronted by a BackendService](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/set-up-envoy-http-mesh#config-server).



Alternatively, you can run the following commands to deploy a sample Compute Engine VM fronted by a BackendService.

  1. Deploy a sample Compute Engine VM and BackendService:
         
         gcloud compute instance-templates create td-httpd-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=http-td-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script="#! /bin/bash
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         sudo service apache2 restart
         echo '<!doctype <html><body><h1>'\`$(/bin/hostname)\`'</h1></body></html>' | sudo tee /var/www/html/index.html"
         
         gcloud compute instance-groups managed create http-td-mig-us-east1 \
           --zone=VM_ZONE   \
           --size=2 \
           --template=td-httpd-vm-template
         
         gcloud compute health-checks create http http-helloworld-health-check
         
         gcloud compute firewall-rules create http-vm-allow-health-checks \
           --network=default \
           --action=ALLOW \
           --direction=INGRESS \
           --source-ranges=0.0.0.0/0 \
           --target-tags=http-td-server \
           --rules=tcp:80
         
         gcloud compute backend-services create helloworld \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --protocol=HTTP \
           --health-checks http-helloworld-health-check
         
         gcloud compute backend-services add-backend helloworld \
           --instance-group=http-td-mig-us-east1 \
           --instance-group-zone=VM_ZONE  \
           --global
         

Where:

     * VM_ZONE is the zone where you want your Compute Engine VM to be deployed.



## Configure a Compute Engine VM as a GCPBackend

In this section, you expose the Compute Engine VM to the GKE workloads using GCPBackend. The GCPBackend consists of:

  1. Frontend information - specifically, the hostname and port that GKE Workloads would use to call this GCPBackend.
  2. Backend information - the BackendService details such as service name, location, and project number.



The GCPBackend contains the hostname and port details as well as the BackendService details (service name, location, and project number). The GKE workloads should use the GCPBackend hostname and port in their HTTP requests to access the Compute Engine VM.

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
           name: vm-gcp-backend
           namespace: NAMESPACE
         spec:
           type: "BackendService"
           hostname: hello-world.gcpbackend
           backendservice:
             name: helloworld
             location: global
         EOF
         kubectl apply -f gcp-backend.yaml
         

In this example GCP_BACKEND_NAME is `vm-gcp-backend`.

  4. Create a testing Pod to verify GKE to Compute Engine VM connectivity:
         
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
         
         kubectl exec testcurl -c curl -- curl http://hello-world.gcpbackend:80
         

Now, your GKE workloads may access the Compute Engine VM by sending HTTP requests to **hello-world.gcpbackend:80**.




You should use distinct names for GCPBackend to avoid conflicting with existing Kubernetes services or Istio Service Entries. If it does conflict, the precedence order (high to low) is Kubernetes Service, istio ServiceEntry, and GCPBackend.

Note that the Virtual Service and the GCPBackend must be in the same namespace and the Compute Engine VM must be in the same project as the Cloud Service Mesh GKE cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
