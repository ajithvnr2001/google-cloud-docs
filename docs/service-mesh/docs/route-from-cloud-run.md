---
url: https://docs.cloud.google.com/service-mesh/docs/route-from-cloud-run/
title: Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:14.010123+00:00
---

# Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/route-from-cloud-run/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Connecting Cloud Run services to Cloud Service Mesh lets you securely route traffic to workloads on GKE. This configuration uses Istio APIs and a fully managed Envoy sidecar to handle service communication across environments.

## Before you begin

The following sections assume that you have a [GKE cluster with Cloud Service Mesh enabled](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane).

If you don't have a GKE Service deployed, use the following command to deploy a sample service:
    
    
    cat <<EOF > /tmp/service.yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: ads
    spec:
      ports:
      - port: 9999
        targetPort: 8000
      selector:
        run: ads
      type: ClusterIP
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ads
    spec:
      replicas: 1
      selector:
        matchLabels:
          run: ads
      template:
        metadata:
          labels:
            run: ads
        spec:
          containers:
          - image: docker.io/waip/simple-http:v1.0.1
            name: my-http2-svc
            ports:
            - protocol: TCP
              containerPort: 8000
          securityContext:
            fsGroup: 1337
    EOF
    kubectl apply -f /tmp/service.yaml
    

## Configure a Custom Domain for `VirtualService` hosts

A [virtual service](https://istio.io/latest/docs/reference/config/networking/virtual-service/) defines traffic routing rules. Any matched traffic is then sent to a named destination service 

  1. Create a new managed zone:
         
         gcloud dns managed-zones create ZONE_NAME \
           --description="zone for service mesh routes" \
           --dns-name=DNS_SUFFIX. \
           --networks=default \
           --visibility=private
         

where:

     * ZONE_NAME is a name for your zone (example: 'prod').
     * DNS_SUFFIX is any valid DNS host (example: 'mesh.private').
  2. Create a resource record set:
         
         IP=10.0.0.1
         gcloud dns record-sets create '*.'"DNS_SUFFIX." --type=A --zone="ZONE_NAME" \
           --rrdatas=10.0.0.1 --ttl 3600
         

Ensure the IP (RFC 1918 required) is unused. Alternatively, [reserve a static internal IP](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

  3. Export a `VirtualService` for External Cloud Run Clients:
         
         cat <<EOF > virtual-service.yaml
         apiVersion: networking.istio.io/v1alpha3
         kind: VirtualService
         metadata:
           name: VIRTUAL_SERVICE_NAME
           namespace: NAMESPACE
         spec:
           hosts:
           - GKE_SERVICE_NAME.DNS_SUFFIX
           gateways:
           - external-mesh
           http:
           - route:
             - destination:
                 host: GKE_SERVICE_NAME
         EOF
         kubectl apply -f virtual-service.yaml
         

where:

     * VIRTUAL_SERVICE_NAME is a name for your `VirtualService`.
     * NAMESPACE is `default` if you're using the provided example service; otherwise, replace NAMESPACE with your namespace name.
     * GKE_SERVICE_NAME is `ads` if you're using the provided example service; otherwise, replace GKE_SERVICE_NAME with a name for your GKE service.



While it is feasible to add an `external-mesh` gateway as a target to a pre-existing `VirtualService`, you should establish a distinct `VirtualService` to export a Kubernetes service to external Cloud Run clients. Having a separate `VirtualService` facilitates the management of exported services and their configurations without affecting existing GKE clients. Additionally, some fields in `VirtualServices` are disregarded for mesh external `VirtualServices` but continue to function as anticipated for GKE services. So managing and troubleshooting `VirtualServices` separately may be advantageous.

For GKE clients to also receive the `VirtualService` configuration, the `mesh` or `mesh/default` gateway must be added.

The mesh external `VirtualService` must be defined in the same namespace as the Kubernetes Service in the `VirtualService` destination.

## Configure a Cloud Run Service to join a service mesh

To join a Cloud Run Service to a service mesh, perform the following steps:

  1. Determine the mesh ID backing the Cloud Service Mesh GKE cluster:
         
         MESH=$(kubectl get controlplanerevision --namespace istio-system -o json | jq -r '.items[0].metadata.annotations["mesh.cloud.google.com/external-mesh"]')
         

  2. Deploy a Cloud Run Service using the mesh ID, making sure to also connect to the cluster's VPC network:
         
         gcloud alpha run deploy --mesh "$MESH" --network default \
           mesh-svc --image=fortio/fortio \
           --region=REGION --project=PROJECT_ID --no-allow-unauthenticated
         

  3. Verify that the Cloud Run service is able to send a request to the GKE workload:
         
         TEST_SERVICE_URL=$(gcloud run services describe mesh-svc --region REGION --format="value(status.url)" --project=PROJECT_ID)
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" "$TEST_SERVICE_URL/fortio/fetch/GKE_SERVICE_NAME.DNS_SUFFIX"
         

The output should be a valid HTTP 200 response.




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

  * [Route traffic from Cloud Service Mesh workloads to Cloud Run Services](https://docs.cloud.google.com/service-mesh/docs/route-to-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
