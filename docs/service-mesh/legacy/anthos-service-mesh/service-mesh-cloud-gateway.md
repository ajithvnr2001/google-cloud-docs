---
url: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/service-mesh-cloud-gateway/
title: Configure classic Application Load Balancer for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:48.181704+00:00
---

# Configure classic Application Load Balancer for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/service-mesh-cloud-gateway/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure classic Application Load Balancer for Cloud Service Mesh

**Preview — service mesh cloud gateway**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

## Overview

This document is for you if you're an existing Cloud Service Mesh user who has the Istiod managed control plane and you want to configure classic Application Load Balancer as an ingress gateway. The classic Application Load Balancer is also known as the classic external Application Load Balancer.

Do not use this document if you're a new Cloud Service Mesh user. New users are automatically set up with the Traffic Director managed control plane. You cannot use the configuration described in this document with the Cloud Service Mesh managed control plane

[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) provides many cloud-managed edge capabilities including global anycast load balancing, Google-managed certificates, Identity and Access Management, Cloud Next Generation Firewall, and Cloud Intrusion Detection System. Cloud Service Mesh can seamlessly integrate these edge capabilities in the following mesh ingress model. Service mesh cloud gateway provides an unified way to configure Cloud Service Mesh ingress gateway with [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) simultaneously through [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io).

![Diagram demonstrating a load balancer with Cloud Service Mesh](https://docs.cloud.google.com/static/service-mesh/docs/images/cloud-service-mesh-ingress.svg)

Compared to our previous user guide, [From edge to mesh: Exposing service mesh applications through GKE Ingress](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress#install-service-mesh), with service mesh cloud gateway, this model can now be deployed through one Kubernetes Gateway resource which simplifies the process of deploying cloud and cluster-hosted load balancing together.

### Preview limitations

For the Preview release of this feature, the following limitations apply:

  * Multi-cluster Gateways are not supported.
  * [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters are not supported.
  * Only the classic Application Load Balancer is supported. The global external Application Load Balancer (sometimes called the Advanced Load Balancer) and internal Application Load Balancer are not supported.
  * Traffic between the classic Application Load Balancer and Cloud Service Mesh ingress gateway is encrypted using TLS. However, the classic Application Load Balancer won't verify the certificate provided by Cloud Service Mesh ingress gateway. This [limitation](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends#secure-protocol-considerations) applies to all the users of Google Cloud HTTP(S) Load Balancer.
  * If Cloud Service Mesh `GatewayClasses` are deleted from a cluster, then they won't be re-installed automatically. However, this won't impact the usability of the feature.
  * Route matching logic does not follow [Gateway API specifications](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.HTTPRoute) and matches in the order of the `HTTPRoute` instead. This will change in future versions to follow Gateway API specifications.



### Requirements

  * [Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/configure-managed-anthos-service-mesh) installed on a Google Kubernetes Engine (GKE) cluster running 1.24 or later. Other GKE Enterprise clusters are not supported.
  * Kubernetes Gateway API v1beta1 version only.



### Prerequisites

  * Enable the following APIs in your project:

    * compute.googleapis.com
    * container.googleapis.com
    * certificatemanager.googleapis.com
    * serviceusage.googleapis.com
    
    gcloud services enable \
       compute.googleapis.com \
       container.googleapis.com \
       certificatemanager.googleapis.com \
       serviceusage.googleapis.com
    




## Deploy service mesh cloud gateway for a single-cluster mesh

This sections shows you how to deploy a [Kubernetes Gateway resource](https://gateway-api.sigs.k8s.io/) which deploys a classic Application Load Balancer and a Cloud Service Mesh ingress gateway.

### Enable Gateway API with managed Cloud Service Mesh

  1. [Enable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway) the Gateway API in your cluster. The GKE cluster must be version 1.24 or later.

  2. Install [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/configure-managed-anthos-service-mesh) with `rapid` or `regular` as its release channel.




### Deploy the Gateway resource

When deploying service mesh cloud gateway, the Kubernetes Gateway resources are used to deploy both Cloud Load Balancing and Cloud Service Mesh ingress gateway as a single step. Note that [Kubernetes Gateway](https://gateway-api.sigs.k8s.io/) resources are different from [Istio Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/) resources.

For more information about the differences, see [Kubernetes Gateways and Istio Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#istio-gateways). Every Kubernetes Gateway has a GatewayClass that indicates its type and inherent capabilities. service mesh cloud gateway has a GatewayClass which have the capability to deploy both Cloud Load Balancing and Cloud Service Mesh ingress gateway.

  1. Save the following GatewayClass manifest to a file named `l7-gateway-class.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: GatewayClass
         metadata:
           name: asm-l7-gxlb
         spec:
           controllerName: mesh.cloud.google.com/gateway
         

  2. Deploy the GatewayClass in your cluster:
         
         kubectl apply -f l7-gateway-class.yaml
         

  3. Verify that the GatewayClass is present after the installation:
         
         kubectl get gatewayclasses.gateway.networking.k8s.io
         

The output is similar to:
         
         NAME          CONTROLLER
         asm-l7-gxlb   mesh.cloud.google.com/gateway
         gke-l7-rilb   networking.gke.io/gateway
         gke-l7-gxlb   networking.gke.io/gateway
         

It may take a few minutes for all of the resources to deploy. If you don't see the expected output, verify that you have correctly satisfied the prerequisites.

You will also see the following GatewayClass:
         
         gke-l7-gxlb   networking.gke.io/gateway
         

This is used to deploy the underlying Google Cloud classic Application Load Balancer.

  4. Create a dedicated Namespace for your service mesh cloud gateway:
         
         kubectl create namespace istio-ingress
         

  5. Save the following Gateway manifest to a file named `gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: servicemesh-cloud-gw
           namespace: istio-ingress
         spec:
           gatewayClassName: asm-l7-gxlb
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               namespaces:
                 from: All
         

  6. Deploy the Gateway in your cluster in the istio-ingress Namespace:
         
         kubectl apply -f gateway.yaml
         

  7. Verify that the Kubernetes Gateway API objects are created:
         
         kubectl get gateways.gateway.networking.k8s.io -n istio-ingress
         

The output is similar to:
         
         NAME                                CLASS         ADDRESS         READY   AGE
         asm-gw-gke-servicemesh-cloud-gw     gke-l7-gxlb   34.111.114.64   True    9m40s
         asm-gw-istio-servicemesh-cloud-gw   istio                                 9m44s
         servicemesh-cloud-gw                asm-l7-gxlb                           9m44s
         




The following things will happen when this Kubernetes Gateway API object is deployed:

  * An external HTTP(S) Load Balancer is deployed and configured. It may take a few minutes for it to come up but when it does, the Gateway will indicate the IP address and will be annotated with the names of the Compute Engine load balancer resources that were created.
  * A Cloud Service Mesh ingress gateway Deployment is created in the istio-ingress namespace. This creates the Envoy proxy instances that will receive traffic from the load balancer.
  * The load balancer will encrypt and route all traffic to the Cloud Service Mesh ingress gateway.

**Warning:** Currently, it's required to have at least one sidecar injected workload for the Cloud Service Mesh ingress gateway to actuate properly.

You now have the full infrastructure needed to accept internet traffic into your mesh. Note that this is the simplest possible Gateway deployment. In the following sections you add additional policies and capabilities that will make it production ready.

## App and routing deployment

To fully demonstrate the capabilities you'll deploy an application to Cloud Service Mesh and receive internet traffic through your Gateway for example purposes.

  1. Label the `default` Namespace to enable sidecar injection.
         
         kubectl label namespace default istio-injection=enabled istio.io/rev- --overwrite
         

  2. Save the following Gateway manifest to a file named `whereami.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: whereami-v1
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: whereami-v1
           template:
             metadata:
               labels:
                 app: whereami-v1
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                   - containerPort: 8080
                 env:
                 - name: METADATA
                   value: "whereami-v1"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: whereami-v1
         spec:
           selector:
             app: whereami-v1
           ports:
           - port: 8080
             targetPort: 8080
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: whereami-v2
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: whereami-v2
           template:
             metadata:
               labels:
                 app: whereami-v2
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                   - containerPort: 8080
                 env:
                 - name: METADATA
                   value: "whereami-v2"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: whereami-v2
         spec:
           selector:
             app: whereami-v2
           ports:
           - port: 8080
             targetPort: 8080
         

This manifest creates `Service/whereami-v1`, `Service/whereami-v2`, `Deployment/whereami-v1`, and `Deployment/whereami-v2` for whereami, a simple application that outputs JSON to indicate its identity and location. You will deploy two different versions of it.

  3. Create the Services and Deployments:
         
         kubectl apply -f whereami.yaml
         

Once it is up and running, you will have four whereami Pods running in your cluster.

  4. Verify that all four Pods are running:
         
         kubectl get pods
         

The output is similar to:
         
         whereami-v1-7c76d89d55-qg6vs       2/2     Running   0          28s
         whereami-v1-7c76d89d55-vx9nm       2/2     Running   0          28s
         whereami-v2-67f6b9c987-p9kqm       2/2     Running   0          27s
         whereami-v2-67f6b9c987-qhj76       2/2     Running   0          27s
         

  5. Save the following HTTPRoute manifest to a file named `http-route.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: where-route
         spec:
          parentRefs:
          - kind: Gateway
            name: servicemesh-cloud-gw
            namespace: istio-ingress
          hostnames:
          - "where.example.com"
          rules:
          - matches:
            - headers:
              - name: version
                value: v2
            backendRefs:
            - name: whereami-v2
              port: 8080
          - backendRefs:
            - name: whereami-v1
              port: 8080
         

  6. Deploy `http-route.yaml` to your cluster:
         
         kubectl apply -f http-route.yaml
         

This HTTPRoute references the `servicemesh-cloud-gw` which means that it will configure service mesh cloud gateway so that it configures the underlying Cloud Service Mesh ingress gateway with these routing rules. The HTTPRoute performs the same function as the Istio VirtualService but uses the Kubernetes Gateway API to do so. Because the Gateway API is an OSS spec with many underlying implementations, it is the best API suited to define routing across a combination of different load balancers (such as Cloud Service Mesh proxies and load balancers).

  7. Retrieve the IP address from the Gateway so that you can send traffic to your application:
         
         VIP=$(kubectl get gateways.gateway.networking.k8s.io asm-gw-gke-servicemesh-cloud-gw -o=jsonpath="{.status.addresses[0].value}" -n istio-ingress)
         

The output is an IP address.
         
         echo $VIP
         
         34.111.61.135
         

  8. Send traffic to the Gateway IP address to validate that this setup functions correctly. Send one request with the `version: v2` header and one without to determine that routing is done correctly across the two application versions.

**Note:** This can take up to 10 minutes to work, and you'll see `Empty reply from server` or `Connection reset by peer` error while waiting.
         
         curl ${VIP} -H "host: where.example.com"
         
         {
           "cluster_name": "gke1",
           "host_header": "where.example.com",
           "metadata": "whereami-v1",
           "node_name": "gke-gke1-default-pool-9b3b5b18-hw5z.c.church-243723.internal",
           "pod_name": "whereami-v1-67d9c5d48b-zhr4l",
           "pod_name_emoji": "⚒",
           "project_id": "church-243723",
           "timestamp": "2021-02-08T18:55:01",
           "zone": "us-central1-a"
         }
         
         curl ${VIP} -H "host: where.example.com" -H "version: v2"
         
         {
           "cluster_name": "gke1",
           "host_header": "where.example.com",
           "metadata": "whereami-v2",
           "node_name": "gke-gke1-default-pool-9b3b5b18-hw5z.c.church-243723.internal",
           "pod_name": "whereami-v2-67d9c5d48b-zhr4l",
           "pod_name_emoji": "⚒",
           "project_id": "church-243723",
           "timestamp": "2021-02-08T18:55:01",
           "zone": "us-central1-a"
         }
         




## Production gateway deployment

The previous section showed a very simple example of service mesh cloud gateway. The following steps build on the simple example to show a production-ready setup that demonstrates the advantages of delegating some of the ingress routing functionality to the load balancer.

In the following example, you'll take the `servicemesh-cloud-gw` from the previous section and will add the following capabilities to create a more secure and manageable Gateway:

  * Deploy the Gateway with a static IP address that will be retained even if the underlying infrastructure changes.
  * Convert the Gateway to receive HTTPS traffic with a self-signed certificate.

**Note:** This example builds on the Gateway Deployment, but because the port and protocol of the Gateway are changed, these steps will disrupt any traffic going to your Gateway on port 80. In any realistic scenario the frontend port of your Gateway would be unlikely to ever change.

  1. Create a static external IP address. A static IP is useful because the underlying infrastructure can change in the future but the IP address can be retained.
         
         gcloud compute addresses create whereami-ip \
             --global \
             --project PROJECT_ID
         

  2. Create a self-signed certificate for the `where-example-com` domain:
         
         openssl genrsa -out key.pem 2048
         cat <<EOF >ca.conf
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         [extension_requirements]
         basicConstraints          = CA:FALSE
         keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
         subjectAltName            = @sans_list
         [dn_requirements]
         0.organizationName        = example
         commonName                = where.example.com
         [sans_list]
         DNS.1                     = where.example.com
         EOF
         
         
         openssl req -new -key key.pem \
             -out csr.pem \
             -config ca.conf
         
         
         openssl x509 -req \
             -signkey key.pem \
             -in csr.pem \
             -out cert.pem \
             -extfile ca.conf \
             -extensions extension_requirements \
             -days 365
         
         
         gcloud compute ssl-certificates create where-example-com \
             --certificate=cert.pem \
             --private-key=key.pem \
             --global \
             --project PROJECT_ID
         

There are many ways to generate TLS certificates. They can be manually generated on the command line, generated using [Google-managed certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs), or may be generated internally by your company's public key infrastructure (PKI) system. In this example, you manually generate a self-signed certificate. While self-signed certificates are not typically used for public services, it demonstrates these concepts more easily.

For more information about creating a self-signed certificate through Kubernetes Secret, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret).

  3. Update `gateway.yaml` with the following manifest:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: servicemesh-cloud-gw
           namespace: istio-ingress
         spec:
           gatewayClassName: asm-l7-gxlb
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               namespaces:
                 from: All
           - name: https
             protocol: HTTPS
             port: 443
             allowedRoutes:
               namespaces:
                 from: All
             tls:
               mode: Terminate
               options:
                 networking.gke.io/pre-shared-certs: where-example-com
           addresses:
           - type: NamedAddress
             value: whereami-ip
         

  4. Redeploy the Gateway in your cluster:
         
         kubectl apply -f gateway.yaml
         

  5. Obtain the IP address of the static IP:
         
         VIP=$(gcloud compute addresses describe whereami-ip --global --format="value(address)")
         

  6. Use `curl` to access the domain of the Gateway. Because DNS is not configured for this domain, use the --resolve option to tell curl to resolve the domain name to the IP address of the Gateway:
         
         curl https://where.example.com --resolve where.example.com:443:${VIP} --cacert cert.pem -v
         

**Note:** This can take up to 10 minutes to work, and you'll see `error:0A000126:SSL routines::unexpected eof while reading` error while waiting.

Once complete, the output is similar to:
         
         ...
         * TLSv1.2 (OUT), TLS handshake, Client hello (1):
         * TLSv1.2 (IN), TLS handshake, Server hello (2):
         * TLSv1.2 (IN), TLS handshake, Certificate (11):
         * TLSv1.2 (IN), TLS handshake, Server key exchange (12):
         * TLSv1.2 (IN), TLS handshake, Server finished (14):
         * TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
         * TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
         * TLSv1.2 (OUT), TLS handshake, Finished (20):
         * TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
         * TLSv1.2 (IN), TLS handshake, Finished (20):
         * SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
         * ALPN, server accepted to use h2
         * Server certificate:
         *  subject: O=example; CN=where.example.com
         *  start date: Apr 19 15:54:50 2021 GMT
         *  expire date: Apr 19 15:54:50 2022 GMT
         *  common name: where.example.com (matched)
         *  issuer: O=example; CN=where.example.com
         *  SSL certificate verify ok.
         ...
         {
           "cluster_name": "gke1",
           "host_header": "where.example.com",
           "metadata": "where-v1",
           "node_name": "gke-gw-default-pool-51ccbf30-yya8.c.agmsb-k8s.internal",
           "pod_name": "where-v1-84b47c7f58-tj5mn",
           "pod_name_emoji": "😍",
           "project_id": "agmsb-k8s",
           "timestamp": "2021-04-19T16:30:08",
           "zone": "us-west1-a"
         }
         




The verbose output includes a successful TLS handshake followed by a response from the application like the following output. This proves that TLS is being terminated at the Gateway correctly and that the application is responding to the client securely.

You have successfully deployed the following architecture:

![ASM Architecture](https://docs.cloud.google.com/static/service-mesh/docs/images/cloud-service-mesh-production-deployment.svg)

The `servicemesh-cloud-gw` and its `asm-l7-gxlb` GatewayClass has abstracted some internal infrastructural components away to simplify the user experience. The Cloud Load Balancing is terminating TLS traffic using an internal certificate and its also health checking the Cloud Service Mesh ingress gateway proxy layer. The `whereami-route` deployed in App & Routing Deployment configures the Cloud Service Mesh ingress gateway proxies to route traffic to the correct mesh-hosted Service.

In the following example, you'll take the `servicemesh-cloud-gw` from the previous section and will add the following capabilities to create a more secure and manageable Gateway:

  * Deploy the Gateway with a static IP address that will be retained even if the underlying infrastructure changes.
  * Convert the Gateway to receive HTTPS traffic with a self-signed certificate.

**Note:** This example builds on the Gateway Deployment, but because the port and protocol of the Gateway are changed, these steps will disrupt any traffic going to your Gateway on port 80. In any realistic scenario the frontend port of your Gateway would be unlikely to ever change.

  1. Create a static external IP address. A static IP is useful because the underlying infrastructure can change in the future but the IP address can be retained.
         
         gcloud compute addresses create whereami-ip \
             --global \
             --project PROJECT_ID
         

  2. Create a self-signed certificate for the `where-example-com` domain:
         
         openssl genrsa -out key.pem 2048
         cat <<EOF >ca.conf
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         [extension_requirements]
         basicConstraints          = CA:FALSE
         keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
         subjectAltName            = @sans_list
         [dn_requirements]
         0.organizationName        = example
         commonName                = where.example.com
         [sans_list]
         DNS.1                     = where.example.com
         EOF
         
         
         openssl req -new -key key.pem \
             -out csr.pem \
             -config ca.conf
         
         
         openssl x509 -req \
             -signkey key.pem \
             -in csr.pem \
             -out cert.pem \
             -extfile ca.conf \
             -extensions extension_requirements \
             -days 365
         
         
         gcloud compute ssl-certificates create where-example-com \
             --certificate=cert.pem \
             --private-key=key.pem \
             --global \
             --project PROJECT_ID
         

There are many ways to generate TLS certificates. They can be manually generated on the command line, generated using [Google-managed certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs), or may be generated internally by your company's public key infrastructure (PKI) system. In this example, you manually generate a self-signed certificate. While self-signed certificates are not typically used for public services, it demonstrates these concepts more easily.

For more information about creating a self-signed certificate through Kubernetes Secret, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret).

  3. Update `gateway.yaml` with the following manifest:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: servicemesh-cloud-gw
           namespace: istio-ingress
         spec:
           gatewayClassName: asm-l7-gxlb
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               namespaces:
                 from: All
           - name: https
             protocol: HTTPS
             port: 443
             allowedRoutes:
               namespaces:
                 from: All
             tls:
               mode: Terminate
               options:
                 networking.gke.io/pre-shared-certs: where-example-com
           addresses:
           - type: NamedAddress
             value: whereami-ip
         

  4. Redeploy the Gateway in your cluster:
         
         kubectl apply -f gateway.yaml
         

  5. Obtain the IP address of the static IP:
         
         VIP=$(gcloud compute addresses describe whereami-ip --global --format="value(address)")
         

  6. Use `curl` to access the domain of the Gateway. Because DNS is not configured for this domain, use the --resolve option to tell curl to resolve the domain name to the IP address of the Gateway:
         
         curl https://where.example.com --resolve where.example.com:443:${VIP} --cacert cert.pem -v
         

**Note:** This can take up to 10 minutes to work, and you'll see `error:0A000126:SSL routines::unexpected eof while reading` error while waiting.

Once complete, the output is similar to:
         
         ...
         * TLSv1.2 (OUT), TLS handshake, Client hello (1):
         * TLSv1.2 (IN), TLS handshake, Server hello (2):
         * TLSv1.2 (IN), TLS handshake, Certificate (11):
         * TLSv1.2 (IN), TLS handshake, Server key exchange (12):
         * TLSv1.2 (IN), TLS handshake, Server finished (14):
         * TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
         * TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
         * TLSv1.2 (OUT), TLS handshake, Finished (20):
         * TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
         * TLSv1.2 (IN), TLS handshake, Finished (20):
         * SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
         * ALPN, server accepted to use h2
         * Server certificate:
         *  subject: O=example; CN=where.example.com
         *  start date: Apr 19 15:54:50 2021 GMT
         *  expire date: Apr 19 15:54:50 2022 GMT
         *  common name: where.example.com (matched)
         *  issuer: O=example; CN=where.example.com
         *  SSL certificate verify ok.
         ...
         {
           "cluster_name": "gke1",
           "host_header": "where.example.com",
           "metadata": "where-v1",
           "node_name": "gke-gw-default-pool-51ccbf30-yya8.c.agmsb-k8s.internal",
           "pod_name": "where-v1-84b47c7f58-tj5mn",
           "pod_name_emoji": "😍",
           "project_id": "agmsb-k8s",
           "timestamp": "2021-04-19T16:30:08",
           "zone": "us-west1-a"
         }
         




The verbose output includes a successful TLS handshake followed by a response from the application like the following output. This proves that TLS is being terminated at the Gateway correctly and that the application is responding to the client securely.

You have successfully deployed the following architecture:

![ASM Architecture](https://docs.cloud.google.com/static/service-mesh/docs/images/cloud-service-mesh-production-deployment.svg)

The `servicemesh-cloud-gw` and its `asm-l7-gxlb` GatewayClass has abstracted some internal infrastructural components away to simplify the user experience. The Cloud Load Balancing is terminating TLS traffic using an internal certificate and its also health checking the Cloud Service Mesh ingress gateway proxy layer. The `whereami-route` deployed in App & Routing Deployment configures the Cloud Service Mesh ingress gateway proxies to route traffic to the correct mesh-hosted Service.

## What's next

  * Learn more about Google Kubernetes Engine (GKE) [implementation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) of the Kubernetes Gateway API.
  * Learn how to [Enable optional managed Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/docs/managed-service-mesh-optional-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
