---
url: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment/
title: From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service Mesh \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:55.964672+00:00
---

# From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service Mesh  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-06-04 UTC

This document shows you how accomplish the following tasks:

  * Deploy [globally distributed applications exposed through GKE Gateway and Cloud Service Mesh](https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service).
  * Expose an application to multiple clients by combining Cloud Load Balancing with Cloud Service Mesh.
  * Integrate load balancers with a service mesh deployed across multiple [Google Cloud regions](https://cloud.google.com/about/locations).



This deployment guide is intended for platform administrators. It's also intended for advanced practitioners who run Cloud Service Mesh. The instructions also work for Istio on GKE.

## Architecture

The following diagram shows the default ingress topology of a service mesh—an external TCP/UDP load balancer that exposes the ingress gateway proxies on a single cluster:

![An external load balancer routes external clients to the mesh through ingress gateway proxies.](https://docs.cloud.google.com/static/architecture/images/build-apps-using-gateway-and-cloud-service-networking.svg)

This deployment guide uses Google Kubernetes Engine (GKE) Gateway resources. Specifically, it uses a [multi-cluster gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#multi-cluster-gateway) to configure multi-region load balancing in front of multiple [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters that are distributed across two regions.

![TLS encryption from the client, a load balancer, and from the mesh.](https://docs.cloud.google.com/static/architecture/images/build-apps-using-gateway-and-cloud-service-ad.svg)

The preceding diagram shows how data flows through cloud ingress and mesh ingress scenarios. For more information, see the explanation of the [architecture diagram](https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service#architecture) in the associated reference architecture document.

## Objectives

  * Deploy a pair of [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters on Google Cloud to the same [fleet](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview).
  * Deploy an Istio-based [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) to the same fleet.
  * Configure a load balancer using [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) to terminate public HTTPS traffic.
  * Direct public HTTPS traffic to applications hosted by Cloud Service Mesh that are deployed across multiple clusters and regions.
  * Deploy the [whereami](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/whereami) sample application to both Autopilot clusters. 



## Cost optimization

In this document, you use the following billable components of Google Cloud: 

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Cloud Service Mesh](https://cloud.google.com/service-mesh/pricing)
  * [Multi Cluster Ingress](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-ingress)
  * [Google Cloud Armor](https://cloud.google.com/armor/pricing)
  * [Certificate Manager](https://cloud.google.com/certificate-manager/pricing)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

You run all of the terminal commands for this deployment from Cloud Shell.

  4. Set your default Google Cloud project:
         
         export PROJECT=PROJECT_ID
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project that you want to use for this deployment.

  5. Create a working directory:
         
         mkdir -p ${HOME}/edge-to-mesh-multi-region
         cd ${HOME}/edge-to-mesh-multi-region
         export WORKDIR=`pwd`
         




## Create GKE clusters

In this section, you create GKE clusters to host the applications and supporting infrastructure, which you create later in this deployment guide.

  1. In Cloud Shell, create a new `kubeconfig` file. This step ensures that you don't create a conflict with your existing (default) `kubeconfig` file.
         
         touch edge2mesh_mr_kubeconfig
         export KUBECONFIG=${WORKDIR}/edge2mesh_mr_kubeconfig
         

  2. Define the environment variables that are used when creating the GKE clusters and the resources within them. Modify the default region choices to suit your purposes.
         
         export CLUSTER_1_NAME=edge-to-mesh-01
         export CLUSTER_2_NAME=edge-to-mesh-02
         export CLUSTER_1_REGION=us-central1
         export CLUSTER_2_REGION=us-east4
         export PUBLIC_ENDPOINT=frontend.endpoints.PROJECT_ID.cloud.goog
         

  3. Enable the Google Cloud APIs that are used throughout this guide:
         
         gcloud services enable \
           container.googleapis.com \
           mesh.googleapis.com \
           gkehub.googleapis.com \
           multiclusterservicediscovery.googleapis.com \
           multiclusteringress.googleapis.com \
           trafficdirector.googleapis.com \
           certificatemanager.googleapis.com
         

  4. Create a GKE Autopilot cluster [with private nodes](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-private-nodes) in `CLUSTER_1_REGION`. Use the `--async` flag to avoid waiting for the first cluster to provision and register to the fleet:
         
         gcloud container clusters create-auto --async \
         ${CLUSTER_1_NAME} --region ${CLUSTER_1_REGION} \
         --release-channel rapid \
         --enable-private-nodes --enable-fleet
         

  5. Create and register a second Autopilot cluster in `CLUSTER_2_REGION`:
         
         gcloud container clusters create-auto \
         ${CLUSTER_2_NAME} --region ${CLUSTER_2_REGION} \
         --release-channel rapid \
         --enable-private-nodes --enable-fleet
         

  6. Ensure that the clusters are running. It might take up to 20 minutes until all clusters are running:
         
         gcloud container clusters list
         

The output is similar to the following:
         
         NAME             LOCATION     MASTER_VERSION      MASTER_IP      MACHINE_TYPE   NODE_VERSION        NUM_NODES  STATUS   STACK_TYPE
         edge-to-mesh-01  us-central1  1.35.5-gke.1000000  34.31.166.104  ek-standard-8  1.35.5-gke.1000000  1          RUNNING  IPV4
         edge-to-mesh-02  us-east4     1.35.5-gke.1000000  35.245.233.88  ek-standard-8  1.35.5-gke.1000000  1          RUNNING  IPV4
         

  7. Gather the credentials for `CLUSTER_1_NAME`.You created `CLUSTER_1_NAME`asynchronously so you could run additional commands while the cluster provisioned.
         
         gcloud container clusters get-credentials ${CLUSTER_1_NAME} \
             --region ${CLUSTER_1_REGION}
         

  8. To clarify the names of the Kubernetes contexts, rename them to the names of the clusters:
         
         kubectl config rename-context gke_PROJECT_ID_${CLUSTER_1_REGION}_${CLUSTER_1_NAME} ${CLUSTER_1_NAME}
         kubectl config rename-context gke_PROJECT_ID_${CLUSTER_2_REGION}_${CLUSTER_2_NAME} ${CLUSTER_2_NAME}
         




## Install a service mesh

In this section, you configure the [managed Cloud Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet). Using the fleet API to enable Cloud Service Mesh provides a declarative approach to provision a service mesh.

  1. In Cloud Shell, enable Cloud Service Mesh on the fleet:
         
         gcloud container fleet mesh enable
         

  2. Enable automatic control plane and data plane management:
         
         gcloud container fleet mesh update \
           --management automatic \
           --memberships ${CLUSTER_1_NAME},${CLUSTER_2_NAME}
         

  3. Wait about 20 minutes. Then verify that the control plane status is `ACTIVE`:
         
         gcloud container fleet mesh describe
         

The output is similar to the following:
         
         createTime: '2026-06-04T23:40:02.666228685Z'
         membershipSpecs:
           projects/497535075790/locations/us-central1/memberships/edge-to-mesh-01:
             mesh:
               management: MANAGEMENT_AUTOMATIC
           projects/497535075790/locations/us-east4/memberships/edge-to-mesh-02:
             mesh:
               management: MANAGEMENT_AUTOMATIC
         membershipStates:
           projects/497535075790/locations/us-central1/memberships/edge-to-mesh-01:
             servicemesh:
               conditions:
               - code: VPCSC_GA_SUPPORTED
                 details: This control plane supports VPC-SC GA.
                 documentationLink: http://cloud.google.com/service-mesh/docs/managed/vpc-sc
                 severity: INFO
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed-rapid'
                 implementation: TRAFFIC_DIRECTOR
                 state: ACTIVE
               dataPlaneManagement:
                 details:
                 - code: OK
                   details: Service is running.
                 state: ACTIVE
             state:
               code: OK
               description: 'Revision ready for use: asm-managed-rapid.'
               updateTime: '2026-06-04T23:45:52.958139396Z'
           projects/497535075790/locations/us-east4/memberships/edge-to-mesh-02:
             servicemesh:
               conditions:
               - code: VPCSC_GA_SUPPORTED
                 details: This control plane supports VPC-SC GA.
                 documentationLink: http://cloud.google.com/service-mesh/docs/managed/vpc-sc
                 severity: INFO
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed-rapid'
                 implementation: TRAFFIC_DIRECTOR
                 state: ACTIVE
               dataPlaneManagement:
                 details:
                 - code: OK
                   details: Service is running.
                 state: ACTIVE
             state:
               code: OK
               description: 'Revision ready for use: asm-managed-rapid.'
               updateTime: '2026-06-04T23:45:54.621862416Z'
         name: projects/e2m-mc-h2c/locations/global/features/servicemesh
         resourceState:
           state: ACTIVE
         spec: {}
         updateTime: '2026-06-04T23:40:55.123874541Z'
         




## Deploy an external Application Load Balancer and create ingress gateways

In this section, you deploy an external Application Load Balancer through the GKE Gateway controller and create ingress gateways for both clusters. The `gateway` and `gatewayClass` resources automate the provisioning of the load balancer and backend health checking. To provide TLS termination on the load balancer, you create [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) resources and attach them to the load balancer. Additionally, you use [Endpoints](https://docs.cloud.google.com/endpoints/docs/choose-endpoints-option) to automatically provision a public DNS name for the application.

### Install an ingress gateway on both clusters

As a security best practice, we recommend that you deploy the ingress gateway in a different namespace from the mesh control plane.

  1. In Cloud Shell, create a dedicated `ingress-gateway` namespace on each cluster:
         
         kubectl --context=${CLUSTER_1_NAME} create namespace ingress-gateway
         kubectl --context=${CLUSTER_2_NAME} create namespace ingress-gateway
         

  2. Add a namespace label to the `ingress-gateway` namespaces:
         
         kubectl --context=${CLUSTER_1_NAME} label namespace ingress-gateway istio-injection=enabled
         kubectl --context=${CLUSTER_2_NAME} label namespace ingress-gateway istio-injection=enabled
         

The output is similar to the following:
         
         namespace/ingress-gateway labeled
         

Labeling the `ingress-gateway` namespaces with `istio-injection=enabled` instructs Cloud Service Mesh to automatically inject Envoy sidecar proxies when a pod is deployed.

  3. Generate a self-signed certificate for future use:
         
         openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
          -subj "/CN=frontend.endpoints.PROJECT_ID.cloud.goog/O=Edge2Mesh Inc" \
          -keyout ${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.key \
          -out ${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.crt
         

The certificate provides an additional layer of encryption between the load balancer and the service mesh ingress gateways. It also enables support for HTTP/2-based protocols like gRPC. Instructions about how to attach the self-signed certificate to the ingress gateways are provided later in Create external IP address, DNS record, and TLS certificate resources.

If you want to use HTTP/2 for the GFE-to-mesh connection but you don't need your own encryption, then you can use [H2C](https://docs.cloud.google.com/load-balancing/docs/https#protocol-to-backends).

For more information about the requirements of the ingress gateway certificate, see [Encryption from the load balancer to the backends](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends#secure_backend_protocol_considerations).

  4. Create a Kubernetes secret on each cluster to store the self-signed certificate:
         
         kubectl --context ${CLUSTER_1_NAME} -n ingress-gateway create secret tls \
          edge2mesh-credential \
          --key=${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.key \
          --cert=${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.crt
         kubectl --context ${CLUSTER_2_NAME} -n ingress-gateway create secret tls \
          edge2mesh-credential \
          --key=${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.key \
          --cert=${WORKDIR}/frontend.endpoints.PROJECT_ID.cloud.goog.crt
         

  5. To integrate with external Application Load Balancer, create a [kustomize](https://github.com/kubernetes-sigs/kustomize) variant to configure the [ingress gateway resources](https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples/tree/main/docs/ingress-gateway-asm-manifests):
         
         mkdir -p ${WORKDIR}/asm-ig/base
         
         cat <<EOF > ${WORKDIR}/asm-ig/base/kustomization.yaml
         resources:
           - github.com/GoogleCloudPlatform/anthos-service-mesh-samples/docs/ingress-gateway-asm-manifests/base
         EOF
         
         mkdir ${WORKDIR}/asm-ig/variant
         
         cat <<EOF > ${WORKDIR}/asm-ig/variant/role.yaml
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: asm-ingressgateway
           namespace: ingress-gateway
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "watch", "list"]
         EOF
         
         cat <<EOF > ${WORKDIR}/asm-ig/variant/rolebinding.yaml
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: asm-ingressgateway
           namespace: ingress-gateway
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: Role
           name: asm-ingressgateway
         subjects:
           - kind: ServiceAccount
             name: asm-ingressgateway
         EOF
         
         cat <<EOF > ${WORKDIR}/asm-ig/variant/service-proto-type.yaml
         apiVersion: v1
         kind: Service
         metadata:
           name: asm-ingressgateway
           namespace: ingress-gateway
         spec:
           ports:
           - name: status-port
             port: 15021
             protocol: TCP
             targetPort: 15021
           - name: http
             port: 80
             targetPort: 8080
             appProtocol: HTTP
           - name: https
             port: 443
             targetPort: 8443
             appProtocol: HTTP2
           type: ClusterIP
         EOF
         
         cat <<EOF > ${WORKDIR}/asm-ig/variant/gateway.yaml
         apiVersion: networking.istio.io/v1beta1
         kind: Gateway
         metadata:
           name: asm-ingressgateway
           namespace: ingress-gateway
         spec:
          servers:
           - port:
               number: 443
               name: https
               protocol: HTTPS
             hosts:
             - "*" # IMPORTANT: Must use wildcard here when using SSL, as SNI isn't passed from GFE
             tls:
               mode: SIMPLE
               credentialName: edge2mesh-credential
         EOF
         
         cat <<EOF > ${WORKDIR}/asm-ig/variant/kustomization.yaml
         namespace: ingress-gateway
         resources:
         - ../base
         - role.yaml
         - rolebinding.yaml
         patches:
         - path: service-proto-type.yaml
           target:
             kind: Service
         - path: gateway.yaml
           target:
             kind: Gateway
         EOF
         

  6. Apply the ingress gateway configuration to both clusters:
         
         kubectl --context ${CLUSTER_1_NAME} apply -k ${WORKDIR}/asm-ig/variant
         kubectl --context ${CLUSTER_2_NAME} apply -k ${WORKDIR}/asm-ig/variant
         




## Expose ingress gateway pods to the load balancer using a multi-cluster service

In this section, you export the ingress gateway pods through a `ServiceExport` custom resource. You must export the ingress gateway pods through a `ServiceExport` custom resource for the following reasons:

  * Allows the load balancer to [address the ingress gateway pods across multiple clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs).
  * Allows the ingress gateway pods to proxy requests to services running within the service mesh.


  1. In Cloud Shell, enable multi-cluster Services (MCS) for the fleet:
         
         gcloud container fleet multi-cluster-services enable
         

  2. Grant MCS the required IAM permissions to the project or fleet:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member "serviceAccount:PROJECT_ID.svc.id.goog[gke-mcs/gke-mcs-importer]" \
          --role "roles/compute.networkViewer"
         

  3. Create the `ServiceExport` YAML file:
         
         cat <<EOF > ${WORKDIR}/svc_export.yaml
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
           name: asm-ingressgateway
           namespace: ingress-gateway
         EOF
         

  4. Apply the `ServiceExport` YAML file to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/svc_export.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/svc_export.yaml
         

If you receive the following error message, wait a few moments for the MCS custom resource definitions (CRDs) to install. Then re-run the commands to apply the `ServiceExport` YAML file to both clusters.
         
         error: resource mapping not found for name: "asm-ingressgateway" namespace: "ingress-gateway" from "svc_export.yaml": no matches for kind "ServiceExport" in version "net.gke.io/v1"
         ensure CRDs are installed first
         




## Create external IP address, DNS record, and TLS certificate resources

In this section, you create networking resources that support the load-balancing resources that you create later in this deployment.

  1. In Cloud Shell, reserve a static external IP address:
         
         gcloud compute addresses create mcg-ip --global
         

A static IP address is used by the GKE Gateway resource. It lets the IP address remain the same, even if the external load balancer is recreated.

  2. Get the static IP address and store it as an environment variable:
         
         export MCG_IP=$(gcloud compute addresses describe mcg-ip --global --format "value(address)")
         echo ${MCG_IP}
         

To create a stable, human-friendly mapping to your Gateway IP address, you must have a public DNS record.

You can use any DNS provider and automation scheme that you want. This deployment uses Endpoints instead of creating a managed DNS zone. Endpoints provides a free [Google-managed DNS](https://docs.cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure) record for an external IP address.

  3. Run the following command to create a YAML file named `dns-spec.yaml`:
         
         cat <<EOF > ${WORKDIR}/dns-spec.yaml
         swagger: "2.0"
         info:
           description: "Cloud Endpoints DNS"
           title: "Cloud Endpoints DNS"
           version: "1.0.0"
         paths: {}
         host: "frontend.endpoints.PROJECT_ID.cloud.goog"
         x-google-endpoints:
         - name: "frontend.endpoints.PROJECT_ID.cloud.goog"
           target: "${MCG_IP}"
         EOF
         

The `dns-spec.yaml` file defines the public DNS record in the form of `frontend.endpoints.PROJECT_ID.cloud.goog`, where `PROJECT_ID` is your unique project identifier.

  4. Deploy the `dns-spec.yaml` file to create the DNS entry. This process takes a few minutes.
         
         gcloud endpoints services deploy ${WORKDIR}/dns-spec.yaml
         

  5. Create a [certificate using Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/certificates) for the DNS entry name you created in the previous step:
         
         gcloud certificate-manager certificates create mcg-cert \
             --domains="frontend.endpoints.PROJECT_ID.cloud.goog"
         

A Google-managed TLS certificate is used to terminate inbound client requests at the load balancer.

  6. Create a [certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps):
         
         gcloud certificate-manager maps create mcg-cert-map
         

The load balancer references the certificate through the certificate map entry you create in the next step.

  7. Create a [certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries) for the certificate you created earlier in this section:
         
         gcloud certificate-manager maps entries create mcg-cert-map-entry \
             --map="mcg-cert-map" \
             --certificates="mcg-cert" \
             --hostname="frontend.endpoints.PROJECT_ID.cloud.goog"
         




## Create backend service policies and load balancer resources

In this section you accomplish the following tasks;

  * Create a Cloud Armor security policy with rules.
  * Create a policy that lets the load balancer check the responsiveness of the ingress gateway pods through the `ServiceExport` YAML file you created earlier.
  * Use the GKE Gateway API to create a load balancer resource.
  * Use the `GatewayClass` custom resource to set the specific load balancer type.
  * Enable multi-cluster load balancing for the fleet and designate one of the clusters as the [configuration cluster for the fleet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways#enable_multi-cluster_gateway_in_the_fleet).


  1. In Cloud Shell, create a Cloud Armor security policy:
         
         gcloud compute security-policies create edge-fw-policy \
             --description "Block XSS attacks"
         

  2. Create a rule for the security policy:
         
         gcloud compute security-policies rules create 1000 \
             --security-policy edge-fw-policy \
             --expression "evaluatePreconfiguredExpr('xss-stable')" \
             --action "deny-403" \
             --description "XSS attack filtering"
         

  3. Create a YAML file for the security policy, and reference the `ServiceExport` YAML file through a corresponding `ServiceImport` YAML file:
         
         cat <<EOF > ${WORKDIR}/cloud-armor-backendpolicy.yaml
         apiVersion: networking.gke.io/v1
         kind: GCPBackendPolicy
         metadata:
           name: cloud-armor-backendpolicy
           namespace: ingress-gateway
         spec:
           default:
             securityPolicy: edge-fw-policy
           targetRef:
             group: net.gke.io
             kind: ServiceImport
             name: asm-ingressgateway
         EOF
         

  4. Apply the Cloud Armor policy to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/cloud-armor-backendpolicy.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/cloud-armor-backendpolicy.yaml
         

  5. Create a custom YAML file that lets the load balancer perform health checks against the Envoy health endpoint (port `15021` on path `/healthz/ready`) of the ingress gateway pods in both clusters:
         
         cat <<EOF > ${WORKDIR}/ingress-gateway-healthcheck.yaml
         apiVersion: networking.gke.io/v1
         kind: HealthCheckPolicy
         metadata:
           name: ingress-gateway-healthcheck
           namespace: ingress-gateway
         spec:
           default:
             config:
               httpHealthCheck:
                 port: 15021
                 portSpecification: USE_FIXED_PORT
                 requestPath: /healthz/ready
               type: HTTP
           targetRef:
             group: net.gke.io
             kind: ServiceImport
             name: asm-ingressgateway
         EOF
         

  6. Apply the custom YAML file you created in the previous step to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/ingress-gateway-healthcheck.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/ingress-gateway-healthcheck.yaml
         

  7. Enable multi-cluster load balancing for the fleet, and designate `CLUSTER_1_NAME` as the configuration cluster:
         
         gcloud container fleet ingress enable \
           --config-membership=${CLUSTER_1_NAME} \
           --location=${CLUSTER_1_REGION}
         

  8. Grant IAM permissions for the Gateway controller in the fleet:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "serviceAccount:service-${PROJECT_NUMBER}@gcp-sa-multiclusteringress.iam.gserviceaccount.com" \
             --role "roles/container.admin"
         

  9. Create the load balancer YAML file through a Gateway custom resource that references the `gke-l7-global-external-managed-mc` [`gatewayClass`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities) and the static IP address you created earlier:
         
         cat <<EOF > ${WORKDIR}/frontend-gateway.yaml
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
           namespace: ingress-gateway
           annotations:
             networking.gke.io/certmap: mcg-cert-map
         spec:
           gatewayClassName: gke-l7-global-external-managed-mc
           listeners:
           - name: http # list the port only so we can redirect any incoming http requests to https
             protocol: HTTP
             port: 80
           - name: https
             protocol: HTTPS
             port: 443
             allowedRoutes:
               kinds:
               - kind: HTTPRoute
           addresses:
           - type: NamedAddress
             value: mcg-ip
         EOF
         

  10. Apply the `frontend-gateway` YAML file to both clusters. Only `CLUSTER_1_NAME` is authoritative unless you designate a different configuration cluster as authoritative:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/frontend-gateway.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/frontend-gateway.yaml
         

  11. Create an `HTTPRoute` YAML file called `default-httproute.yaml` that instructs the Gateway resource to send requests to the ingress gateways:
         
         cat << EOF > ${WORKDIR}/default-httproute.yaml
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: default-httproute
           namespace: ingress-gateway
         spec:
           parentRefs:
           - name: external-http
             namespace: ingress-gateway
             sectionName: https
           rules:
           - backendRefs:
             - group: net.gke.io
               kind: ServiceImport
               name: asm-ingressgateway
               port: 443
         EOF
         

  12. Apply the `HTTPRoute` YAML file you created in the previous step to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/default-httproute.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/default-httproute.yaml
         

  13. To perform HTTP to HTTP(S) redirects, create an additional `HTTPRoute` YAML file called `default-httproute-redirect.yaml`:
         
         cat << EOF > ${WORKDIR}/default-httproute-redirect.yaml
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: http-to-https-redirect-httproute
           namespace: ingress-gateway
         spec:
           parentRefs:
           - name: external-http
             namespace: ingress-gateway
             sectionName: http
           rules:
           - filters:
             - type: RequestRedirect
               requestRedirect:
                 scheme: https
                 statusCode: 301
         EOF
         

  14. Apply the redirect `HTTPRoute` YAML file to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/default-httproute-redirect.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/default-httproute-redirect.yaml
         

  15. Inspect the Gateway resource to check the progress of the load balancer deployment:
         
         kubectl --context=${CLUSTER_1_NAME} describe gateway external-http -n ingress-gateway
         

The output shows the information you entered in this section.




## Deploy the whereami sample application

This guide uses [whereami](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/whereami) as a sample application to provide direct feedback about which clusters are replying to requests. The following section sets up two separate deployments of whereami across both clusters: a `frontend` deployment and a `backend` deployment.

The `frontend` deployment is the first workload to receive the request. It then calls the `backend` deployment.

This model is used to demonstrate a multi-service application architecture. Both `frontend` and `backend` services are deployed to both clusters.

  1. In Cloud Shell, create the namespaces for a whereami `frontend` and a whereami `backend` across both clusters and enable namespace injection:
         
         kubectl --context=${CLUSTER_1_NAME} create ns frontend
         kubectl --context=${CLUSTER_1_NAME} label namespace frontend istio-injection=enabled
         kubectl --context=${CLUSTER_1_NAME} create ns backend
         kubectl --context=${CLUSTER_1_NAME} label namespace backend istio-injection=enabled
         kubectl --context=${CLUSTER_2_NAME} create ns frontend
         kubectl --context=${CLUSTER_2_NAME} label namespace frontend istio-injection=enabled
         kubectl --context=${CLUSTER_2_NAME} create ns backend
         kubectl --context=${CLUSTER_2_NAME} label namespace backend istio-injection=enabled
         

  2. Create a kustomize variant for the whereami `backend`:
         
         mkdir -p ${WORKDIR}/whereami-backend/base
         
         cat <<EOF > ${WORKDIR}/whereami-backend/base/kustomization.yaml
         resources:
           - github.com/GoogleCloudPlatform/kubernetes-engine-samples/quickstarts/whereami/k8s
         EOF
         
         mkdir ${WORKDIR}/whereami-backend/variant
         
         cat <<EOF > ${WORKDIR}/whereami-backend/variant/cm-flag.yaml
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: whereami
         data:
           BACKEND_ENABLED: "False" # assuming you don't want a chain of backend calls
           METADATA:        "backend"
         EOF
         
         cat <<EOF > ${WORKDIR}/whereami-backend/variant/service-type.yaml
         apiVersion: "v1"
         kind: "Service"
         metadata:
           name: "whereami"
         spec:
           type: ClusterIP
         EOF
         
         cat <<EOF > ${WORKDIR}/whereami-backend/variant/kustomization.yaml
         nameSuffix: "-backend"
         namespace: backend
         labels:
         - includeSelectors: true
           includeTemplates: true
           pairs:
             app: whereami-backend
         resources:
         - ../base
         patches:
         - path: cm-flag.yaml
           target:
             kind: ConfigMap
         - path: service-type.yaml
           target:
             kind: Service
         EOF
         

  3. Apply the whereami `backend` variant to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -k ${WORKDIR}/whereami-backend/variant
         kubectl --context=${CLUSTER_2_NAME} apply -k ${WORKDIR}/whereami-backend/variant
         

  4. Create a kustomize variant for the whereami `frontend`:
         
         mkdir -p ${WORKDIR}/whereami-frontend/base
         
         cat <<EOF > ${WORKDIR}/whereami-frontend/base/kustomization.yaml
         resources:
           - github.com/GoogleCloudPlatform/kubernetes-engine-samples/quickstarts/whereami/k8s
         EOF
         
         mkdir whereami-frontend/variant
         
         cat <<EOF > ${WORKDIR}/whereami-frontend/variant/cm-flag.yaml
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: whereami
         data:
           BACKEND_ENABLED: "True"
           BACKEND_SERVICE: "http://whereami-backend.backend.svc.cluster.local"
         EOF
         
         cat <<EOF > ${WORKDIR}/whereami-frontend/variant/service-type.yaml
         apiVersion: "v1"
         kind: "Service"
         metadata:
           name: "whereami"
         spec:
           type: ClusterIP
         EOF
         
         cat <<EOF > ${WORKDIR}/whereami-frontend/variant/kustomization.yaml
         nameSuffix: "-frontend"
         namespace: frontend
         labels:
         - includeSelectors: true
           includeTemplates: true
           pairs:
             app: whereami-frontend
         resources:
         - ../base
         patches:
         - path: cm-flag.yaml
           target:
             kind: ConfigMap
         - path: service-type.yaml
           target:
             kind: Service
         EOF
         

  5. Apply the whereami `frontend` variant to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -k ${WORKDIR}/whereami-frontend/variant
         kubectl --context=${CLUSTER_2_NAME} apply -k ${WORKDIR}/whereami-frontend/variant
         

  6. Create a [`VirtualService`](https://istio.io/latest/docs/reference/config/networking/virtual-service/) YAML file to route requests to the whereami `frontend`:
         
         cat << EOF > ${WORKDIR}/frontend-vs.yaml
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: whereami-vs
           namespace: frontend
         spec:
           gateways:
           - ingress-gateway/asm-ingressgateway
           hosts:
           - 'frontend.endpoints.PROJECT_ID.cloud.goog'
           http:
           - route:
             - destination:
                 host: whereami-frontend
                 port:
                   number: 80
         EOF
         

  7. Apply the `frontend-vs` YAML file to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/frontend-vs.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/frontend-vs.yaml
         

  8. Now that you have deployed `frontend-vs.yaml` to both clusters, attempt to call the public endpoint for your clusters:
         
         curl -s https://frontend.endpoints.PROJECT_ID.cloud.goog | jq
         

The output is similar to the following:
         
         {
           "backend_result": {
             "cluster_name": "edge-to-mesh-02",
             "gce_instance_id": "8396338201253702608",
             "gce_service_account": "e2m-mcg-01.svc.id.goog",
             "host_header": "whereami-backend.backend.svc.cluster.local",
             "metadata": "backend",
             "node_name": "gk3-edge-to-mesh-02-pool-2-675f6abf-645h",
             "pod_ip": "10.124.0.199",
             "pod_name": "whereami-backend-7cbdfd788-8mmnq",
             "pod_name_emoji": "📸",
             "pod_namespace": "backend",
             "pod_service_account": "whereami-backend",
             "project_id": "e2m-mcg-01",
             "timestamp": "2023-12-01T03:46:24",
             "zone": "us-east4-b"
           },
           "cluster_name": "edge-to-mesh-01",
           "gce_instance_id": "1047264075324910451",
           "gce_service_account": "e2m-mcg-01.svc.id.goog",
           "host_header": "frontend.endpoints.e2m-mcg-01.cloud.goog",
           "metadata": "frontend",
           "node_name": "gk3-edge-to-mesh-01-pool-2-d687e3c0-5kf2",
           "pod_ip": "10.54.1.71",
           "pod_name": "whereami-frontend-69c4c867cb-dgg8t",
           "pod_name_emoji": "🪴",
           "pod_namespace": "frontend",
           "pod_service_account": "whereami-frontend",
           "project_id": "e2m-mcg-01",
           "timestamp": "2023-12-01T03:46:24",
           "zone": "us-central1-c"
         }
         


**Note:** It takes around 20 minutes for the certificate to be provisioned. If you don't receive a response, use the `-v` flag in the `curl` command in this step to verify whether the error is related to TLS errors.

If you run the `curl` command a few times, you'll see that the responses (both from `frontend` and `backend`) come from different regions. In its response, the load balancer is providing geo-routing. That means the load balancer is routing requests from the client to the nearest active cluster, but the requests are still landing randomly. When requests occasionally go from one region to another, it increases latency and cost.

In the next section, you implement locality load balancing in the service mesh to keep requests local.

## Enable and test locality load balancing for whereami

In this section, you implement [locality load balancing](https://istio.io/latest/docs/tasks/traffic-management/locality-load-balancing/) in the service mesh to keep requests local. You also perform some tests to see how whereami handles various failure scenarios.

When you make a request to the whereami `frontend` service, the load balancer sends the request to the cluster with the lowest latency relative to the client. That means the ingress gateway pods within the mesh load balance requests to whereami `frontend` pods across both clusters. This section will address that issue by enabling locality load balancing within the mesh.

**Note:** The `DestinationRule` examples in the following section set an artificially low value for regional failover. When adapting these samples for your own purposes, test extensively to verify that you've found the appropriate value for your needs.

  1. In Cloud Shell, create a [`DestinationRule`](https://istio.io/latest/docs/reference/config/networking/destination-rule/) YAML file that enables locality load balancing regional failover to the `frontend` service:
         
         cat << EOF > ${WORKDIR}/frontend-dr.yaml
         apiVersion: networking.istio.io/v1beta1
         kind: DestinationRule
         metadata:
           name: frontend
           namespace: frontend
         spec:
           host: whereami-frontend.frontend.svc.cluster.local
           trafficPolicy:
             connectionPool:
               http:
                 maxRequestsPerConnection: 0
             loadBalancer:
               simple: LEAST_REQUEST
               localityLbSetting:
                 enabled: true
             outlierDetection:
               consecutive5xxErrors: 1
               interval: 1s
               baseEjectionTime: 1m
         EOF
         

The preceding code sample only enables local routing for the `frontend` service. You also need an additional configuration that handles the backend.

  2. Apply the `frontend-dr` YAML file to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/frontend-dr.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/frontend-dr.yaml
         

  3. Create a `DestinationRule` YAML file that enables locality load balancing regional failover to the `backend` service:
         
         cat << EOF > ${WORKDIR}/backend-dr.yaml
         apiVersion: networking.istio.io/v1beta1
         kind: DestinationRule
         metadata:
           name: backend
           namespace: backend
         spec:
           host: whereami-backend.backend.svc.cluster.local
           trafficPolicy:
             connectionPool:
               http:
                 maxRequestsPerConnection: 0
             loadBalancer:
               simple: LEAST_REQUEST
               localityLbSetting:
                 enabled: true
             outlierDetection:
               consecutive5xxErrors: 1
               interval: 1s
               baseEjectionTime: 1m
         EOF
         

  4. Apply the `backend-dr` YAML file to both clusters:
         
         kubectl --context=${CLUSTER_1_NAME} apply -f ${WORKDIR}/backend-dr.yaml
         kubectl --context=${CLUSTER_2_NAME} apply -f ${WORKDIR}/backend-dr.yaml
         

With both sets of `DestinationRule` YAML files applied to both clusters, requests remain local to the cluster that the request is routed to.

To test failover for the `frontend` service, reduce the number of replicas for the ingress gateway in your primary cluster.

From the perspective of the multi-regional load balancer, this action simulates a cluster failure. It causes that cluster to fail its load balancer health checks. This example uses the cluster in `CLUSTER_1_REGION`. You should only see responses from the cluster in `CLUSTER_2_REGION`.

  5. Reduce the number of replicas for the ingress gateway in your primary cluster to zero and call the public endpoint to verify that requests have failed over to the other cluster:
         
         kubectl --context=${CLUSTER_1_NAME} -n ingress-gateway scale --replicas=0 deployment/asm-ingressgateway
         

**Note:** While there is a [HorizontalPodAutoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) configured with `minReplicas:3` for the `asm-ingressgateway` deployment, scaling is temporarily deactivated when the deployment's replica count is set to 0. For more information, see [Horizontal Pod Autoscaling - Implicit maintenance-mode deactivation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#implicit-maintenance-mode-deactivation).

The output should resemble the following:
         
         $ curl -s https://frontend.endpoints.PROJECT_ID.cloud.goog | jq
         {
           "backend_result": {
             "cluster_name": "edge-to-mesh-02",
             "gce_instance_id": "2717459599837162415",
             "gce_service_account": "e2m-mcg-01.svc.id.goog",
             "host_header": "whereami-backend.backend.svc.cluster.local",
             "metadata": "backend",
             "node_name": "gk3-edge-to-mesh-02-pool-2-675f6abf-dxs2",
             "pod_ip": "10.124.1.7",
             "pod_name": "whereami-backend-7cbdfd788-mp8zv",
             "pod_name_emoji": "🏌🏽‍♀",
             "pod_namespace": "backend",
             "pod_service_account": "whereami-backend",
             "project_id": "e2m-mcg-01",
             "timestamp": "2023-12-01T05:41:18",
             "zone": "us-east4-b"
           },
           "cluster_name": "edge-to-mesh-02",
           "gce_instance_id": "6983018919754001204",
           "gce_service_account": "e2m-mcg-01.svc.id.goog",
           "host_header": "frontend.endpoints.e2m-mcg-01.cloud.goog",
           "metadata": "frontend",
           "node_name": "gk3-edge-to-mesh-02-pool-3-d42ddfbf-qmkn",
           "pod_ip": "10.124.1.142",
           "pod_name": "whereami-frontend-69c4c867cb-xf8db",
           "pod_name_emoji": "🏴",
           "pod_namespace": "frontend",
           "pod_service_account": "whereami-frontend",
           "project_id": "e2m-mcg-01",
           "timestamp": "2023-12-01T05:41:18",
           "zone": "us-east4-b"
         }
         

  6. To resume typical traffic routing, restore the ingress gateway replicas to the original value in the cluster:
         
         kubectl --context=${CLUSTER_1_NAME} -n ingress-gateway scale --replicas=3 deployment/asm-ingressgateway
         

  7. Simulate a failure for the `backend` service, by reducing the number of replicas in the primary region to 0:
         
         kubectl --context=${CLUSTER_1_NAME} -n backend scale --replicas=0 deployment/whereami-backend
         

Verify that the responses from the `frontend` service come from the `us-central1` primary region through the load balancer, and the responses from the `backend` service come from the `us-east4` secondary region.

The output should also include a response for the `frontend` service from the primary region (`us-central1`), and a response for the `backend` service from the secondary region (`us-east4`), as expected.

  8. Restore the backend service replicas to the original value to resume typical traffic routing:
         
         kubectl --context=${CLUSTER_1_NAME} -n backend scale --replicas=3 deployment/whereami-backend
         




You now have a global HTTP(S) load balancer serving as a frontend to your service-mesh-hosted, multi-region application.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this deployment, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to keep the Google Cloud project you used in this deployment, delete the individual resources:

  1. In Cloud Shell, delete the `HTTPRoute` resources:
         
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/default-httproute-redirect.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/default-httproute-redirect.yaml
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/default-httproute.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/default-httproute.yaml
         

  2. Delete the GKE Gateway resources:
         
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/frontend-gateway.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/frontend-gateway.yaml
         

  3. Delete the policies:
         
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/ingress-gateway-healthcheck.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/ingress-gateway-healthcheck.yaml
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/cloud-armor-backendpolicy.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/cloud-armor-backendpolicy.yaml
         

  4. Delete the service exports:
         
         kubectl --context=${CLUSTER_1_NAME} delete -f ${WORKDIR}/svc_export.yaml
         kubectl --context=${CLUSTER_2_NAME} delete -f ${WORKDIR}/svc_export.yaml
         

  5. Delete the Cloud Armor resources:
         
         gcloud --project=PROJECT_ID compute security-policies rules delete 1000 --security-policy edge-fw-policy --quiet
         gcloud --project=PROJECT_ID compute security-policies delete edge-fw-policy --quiet
         

  6. Delete the Certificate Manager resources:
         
         gcloud --project=PROJECT_ID certificate-manager maps entries delete mcg-cert-map-entry --map="mcg-cert-map" --quiet
         gcloud --project=PROJECT_ID certificate-manager maps delete mcg-cert-map --quiet
         gcloud --project=PROJECT_ID certificate-manager certificates delete mcg-cert --quiet
         

  7. Delete the Endpoints DNS entry:
         
         gcloud --project=PROJECT_ID endpoints services delete "frontend.endpoints.PROJECT_ID.cloud.goog" --quiet
         

  8. Delete the static IP address:
         
         gcloud --project=PROJECT_ID compute addresses delete mcg-ip --global --quiet
         

  9. Delete the GKE Autopilot clusters. This step takes several minutes.
         
         gcloud --project=PROJECT_ID container clusters delete ${CLUSTER_1_NAME} --region ${CLUSTER_1_REGION} --quiet
         gcloud --project=PROJECT_ID container clusters delete ${CLUSTER_2_NAME} --region ${CLUSTER_2_REGION} --quiet
         




## What's next

  * Learn about [more features offered by GKE Gateway that you can use with your service mesh](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).
  * Learn about [the different types of Cloud Load Balancing available for GKE](https://cloud.google.com/blog/products/containers-kubernetes/exposing-services-on-gke).
  * Learn about [the features and functions offered by Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Alex Mattson](https://www.linkedin.com/in/alex-m-b505564) | Application Specialist Engineer
  * [Mark Chilvers](https://www.linkedin.com/in/mark-c-77b3a03a) | Application Specialist Engineer



Other contributors: 

  * [Abdelfettah Sghiouar](https://www.linkedin.com/in/sabdelfettah) | Cloud Developer Advocate
  * [Greg Bray](https://www.linkedin.com/in/gregorysbray) | Customer Engineer
  * [Paul Revello](https://www.linkedin.com/in/paul-revello) | Cloud Solutions Architect
  * [Valavan Rajakumar](https://www.linkedin.com/in/valavanr) | Key Enterprise Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-04 UTC."],[],[]] 
