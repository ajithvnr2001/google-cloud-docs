---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway/
title: Secure a Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:31.984324+00:00
---

# Secure a Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Secure a Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how you can secure a Gateway using various security features:

  * SSL Policies to help ensure the Gateway is using the required secure protocols and algorithms

  * Certificates to secure Client-to-Gateway and Gateway-to-Backends traffic with TLS

  * Google Cloud Armor security policy to protect Services from DDoS attacks

  * Identity-Aware Proxy (IAP) to provide a layer of authentication and authorization before allowing access to a Service

  * Authorization policies to enforce identity-based access control and zero-trust architecture at the Gateway layer




To learn more about Gateway security, see [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### GKE Gateway controller requirements

  * Gateway API is supported on [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) clusters only.
  * If you are using the regional or cross-region GatewayClasses, you must enable a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * Your cluster must have the `HttpLoadBalancing` add-on enabled.
  * If you are using Istio, you must upgrade Istio to one of the following versions: 
    * 1.15.2 or later
    * 1.14.5 or later
    * 1.13.9 or later.
  * If you are using Shared VPC, then in the host project, you need to assign the `Compute Network User` role to the GKE Service account for the service project. 

  * Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).




### Restrictions and limitations

In addition to the GKE Gateway controller [restrictions and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#limitations), the following limitations apply specifically to Gateway security:

  * TLS configurations using either an [SSL Certificate](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-ssl-certificate) or [Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager) on Gateways are not supported with GKE version 1.28.4-gke.1083000. Use a [Kubernetes secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret) as a workaround for this GKE version.

  * You cannot use the `networking.gke.io/certmap` annotation with a `tls.certificateRefs` on the same Gateway resource. If you reference a CertificateMap in a Gateway, GKE will treat this as an error.

  * Certificate Manager supports both self-managed and Google-managed certificates. Google-managed certificates are compatible with regional Gateways and global Gateways.

  * When using Google-managed SSL certificates, you must create the SSL certificates outside of GKE before you attach them to your Gateway.

  * You cannot use the same service as a backend to a regional and a global Gateway if you are referencing a Google Cloud Armor backend security policy in your GCPBackendPolicy. You must create two separate services and policies for this use case.

  * The Gateway controller does not support the ManagedCertificate resource.

  * The Gateway controller does not support the `networking.gke.io/managed-certificates` annotation.

  * If you [configure Cloud CDN with GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cdn-for-gateway), you can't enable both IAP and Cloud CDN with the same Gateway, including individual routes with Cloud CDN. If you need to enable Cloud CDN for a route that uses a GCPHTTPFilter resource, you must first remove any existing GCPBackendPolicy that configures IAP for that Gateway.

  * **TrustConfig quota.** For information about the total size of all TrustConfig resources in each location, see [Resource quotas and limits](https://docs.cloud.google.com/certificate-manager/docs/quotas#resource_quotas_and_limits).

  * **Location alignment.** The referenced TrustConfig resource must exist in the same location (global or specific region) as the Gateway that uses the Service.

  * **Namespace constraint.** The BackendTLSPolicy resource and its target resource must be in the same namespace.




For a list of supported Gateway API fields and capabilities of the GatewayClass resources available on GKE, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

## Secure a Gateway using a Kubernetes Secret

In this example, you configure a Gateway using a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/).

### Store a certificate in a Kubernetes Secret

You can use a certificate issued and validated by your certificate authority (CA) or create a self-signed certificate. The following steps use a self-signed certificate.

  1. Create a private key:
         
         openssl genrsa -out PRIVATE_KEY_FILE 2048
         

Replace `PRIVATE_KEY_FILE` with the name of your private key file, such as `private-key.pem`. For more information, see [Select or create a private key](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#private-key).

  2. Create an [Open SSL configuration file](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf):
         
         cat <<EOF >CONFIG_FILE
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
         commonName                = store.example.com
         
         [sans_list]
         DNS.1                     = store.example.com
         EOF
         

Replace `CONFIG_FILE` with the name for the new config file, such as `config-file.cnf`.

  3. Create a certificate signing request (CSR) file:
         
         openssl req -new -key PRIVATE_KEY_FILE \
             -out CSR_FILE \
             -config CONFIG_FILE
         

Replace `CSR_FILE` with the name of the new CSR file, such as `cert.pem`. For more information, see [Create a CSR](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-csr).

  4. Sign the CSR:
         
         openssl x509 -req \
             -signkey PRIVATE_KEY_FILE \
             -in CSR_FILE \
             -out CERTIFICATE_FILE \
             -extfile CONFIG_FILE \
             -extensions extension_requirements \
             -days 30
         

Replace `CERTIFICATE_FILE` with the path and name of the file that the command generates, such as `cert-file.pem`. For more information, see [Sign the CSR](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-cert).

  5. Create a Kubernetes TLS Secret using the key and the certificate file that you created:
         
         kubectl create secret tls store-example-com \
             --cert=CERTIFICATE_FILE \
             --key=PRIVATE_KEY_FILE
         

GKE saves the certificate and key as a Kubernetes resource that you can attach to your Gateway.




### Create a Gateway and HTTPRoute

  1. Save the following manifest as `external-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
         spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
             tls:
               mode: Terminate
               certificateRefs: # Directly reference the Kubernetes Secret containing the TLS certificate and private key.
               - name: store-example-com # The name of the TLS secret.
         

This manifest describes a Gateway with the following properties:

     * `gatewayClassName: gke-l7-global-external-managed`: deploys a global external Application Load Balancer.
     * `protocol: HTTPS` and `port: 443`: required for enabling TLS.
     * `tls`: references the Kubernetes Secret created in the previous step.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f external-gateway.yaml
         

  3. Save the following manifest as `store-external-route.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-external
           labels:
             gateway: external-http
         spec:
           parentRefs:
           - name: external-http # Link this route to the 'external-http' Gateway.
           hostnames:
           - "store.example.com" # Match traffic for this hostname.
           rules:
           - backendRefs: # Define where to forward the traffic.
             - name: store-v1
               port: 8080
         

This manifest describes an HTTPRoute that matches traffic to `store.example.com` and sends it to the `store-v1` Service.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f store-external-route.yaml
         




### Verify the Gateway

Verify that the Gateway works by sending a request over the internet.

  1. Get the IP address of the Gateway:
         
         kubectl get gateway external-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is similar to the following:
         
         203.0.113.12
         

This output is a public IP address, which means any client with internet access can connect to it.

  2. Access the domain of the Gateway using `curl`:
         
         curl https://store.example.com --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert CERTIFICATE_FILE -v
         

Replace the following:

     * `GATEWAY_IP_ADDRESS`: the IP address of the Gateway load balancer.
     * `CERTIFICATE_FILE`: the certificate file that you generated. You must save this file on the machine that you are using to connect to the Gateway. The certificate is required to authenticate the Gateway because the Gateway uses a self-signed certificate.

The `--resolve` option resolves the domain name to the IP address of the Gateway, which is required because DNS is not configured for this domain.

The output is similar to the following:
    
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
    # This block shows the certificate details presented by the Gateway.
    # The value of the 'common name' field matches the requested hostname.
    * Server certificate:
    *  subject: O=example; CN=store.example.com
    *  start date: Apr 19 15:54:50 2021 GMT
    *  expire date: Apr 19 15:54:50 2022 GMT
    *  common name: store.example.com (matched)
    *  issuer: O=example; CN=store.example.com
    *  SSL certificate verify ok.
    ...
    {
      "cluster_name": "gw",
      "host_header": "store.example.com",
      "metadata": "store-v1",
      "node_name": "gke-gw-default-pool-51ccbf30-yya8.c.agmsb-k8s.internal",
      "pod_name": "store-v1-84b47c7f58-tj5mn",
      "pod_name_emoji": "😍",
      "project_id": "agmsb-k8s",
      "timestamp": "2021-04-19T16:30:08"
      # Several lines of output omitted here.
    }
    

This output includes a successful TLS handshake followed by a response from the application. The TLS connection is terminated at the Gateway and the application responds to the client securely.




## Secure a Gateway using an SSL certificate

In this example, you configure a Gateway with a [Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

**Note:** Configuring an SSL Certificate and the `networking.gke.io/certmap` annotation on the same Gateway is not a valid configuration and the controller will treat this as an error.

### Create an SSL certificate

  1. Create a Google-managed global SslCertificate resource:
         
         gcloud compute ssl-certificates create store-example-com \
             --domains=store.example.com \
             --global
         




### Create a Gateway and HTTPRoute

  1. Save the following manifest as `external-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
         spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
             tls:
               mode: Terminate # Terminate TLS using your SSL certificate.
               options:
                 networking.gke.io/pre-shared-certs: store-example-com # Specify the Google Cloud SSL certificate resource name.
         

This manifest describes a Gateway with the following properties:

     * `gatewayClassName: gke-l7-global-external-managed`: deploys a global external Application Load Balancer.
     * `protocol:HTTPS` and `port:443`: required for enabling TLS.
     * `tls.mode:Terminate`: terminates TLS using your SSL certificate.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f external-gateway.yaml
         

  3. Save the following HTTPRoute manifest as `store-external-route.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-external
           labels:
             gateway: external-http
         spec:
           parentRefs:
           - name: external-http
           hostnames:
           - "store.example.com"
           rules:
           - backendRefs:
             - name: store-v1
               port: 8080
         

  4. Deploy the HTTPRoute in your cluster:
         
         kubectl apply -f store-external-route.yaml
         

It might take several minutes for GKE to deploy the Gateway.




### Verify the Gateway

  1. Get the IP address of the Gateway:
         
         kubectl get gateway external-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is similar to the following:
         
         203.0.113.12
         

This output is a public IP address, which means any client with internet access can connect to it.

  2. [Update an A or AAAA record](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns) to direct your domain to the IP address of the Gateway.

This step is only necessary if you are configuring a Google-managed SSL certificate. If you are configuring a self-managed certificate, you can skip this step.

After the DNS records are updated, it can take up to 10 minutes for your load balancer to begin using the Google-managed certificate.

  3. Verify that the Gateway is working by sending a request over the internet using `curl`:
         
         curl https://store.example.com -v
         

The output is similar to the following:
         
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
         *  subject: O=example; CN=store.example.com
         *  start date: Apr 19 15:54:50 2021 GMT
         *  expire date: Apr 19 15:54:50 2022 GMT
         *  common name: store.example.com (matched)
         *  issuer: O=example; CN=store.example.com
         *  SSL certificate verify ok.
         ...
         {
           "cluster_name": "gw",
           "host_header": "store.example.com",
           "metadata": "store-v1",
           "node_name": "gke-gw-default-pool-51ccbf30-yya8.c.agmsb-k8s.internal",
           "pod_name": "store-v1-84b47c7f58-tj5mn",
           "pod_name_emoji": "😍",
           "project_id": "agmsb-k8s",
           "timestamp": "2021-04-19T16:30:08",
           "zone": "us-west1-a"
         }
         

This output includes a successful TLS handshake and a response from the application. TLS is terminated at the Gateway correctly and the application responds to the client securely.




## Secure a Gateway using Certificate Manager

In this example, you configure a Gateway using [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs).

**Note:** Configuring an SSL Certificate and the `networking.gke.io/certmap` annotation on the same Gateway is not a valid configuration and the controller will treat this as an error.

### Create a Certificate

### Global Gateway

To create a global Gateway, you reference a [certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps) resource that contains one or more certificates. You must create at least one certificate and add it as an entry to your certificate map.

  1. To create a certificate, first create a [private key and certificate file](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

  2. Create a Certificate resource by loading your self-managed certificate and key:
         
         gcloud certificate-manager certificates create store-example-com-cert \
             --certificate-file="cert.pem" \
             --private-key-file="PRIVATE_KEY_FILE"
         

  3. Create a CertificateMap:
         
         gcloud certificate-manager maps create store-example-com-map
         

  4. Create a CertificateMapEntry which assigns the certificate to the CertificateMap:
         
         gcloud certificate-manager maps entries create store-example-com-map-entry \
             --map=store-example-com-map \
             --hostname=store.example.com \
             --certificates=store-example-com-cert
         




### Regional Gateway

For a regional Gateway, you create a Certificate which will be specified directly when creating the Gateway. Unlike a global Gateway, you don't need to create a CertificateMap to which certificates are assigned.

  1. Create a [private key and certificate file](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

  2. Create a Certificate resource by uploading your certificate file and key:



    
    
    gcloud certificate-manager certificates create "CERTIFICATE_NAME" \
        --certificate-file="CERTIFICATE_FILE" \
        --private-key-file="PRIVATE_KEY_FILE" \
        --location="REGION"
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of your certificate, for example `store-example-com-cert`.
  * `CERTIFICATE_FILE`: the name of the certificate file, for example, `cert.pem`.
  * `PRIVATE_KEY_FILE`: the name of your private key file, such as `private-key.pem`. For more information, see [Select or create a private key](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#private-key).
  * `REGION`: the name of the region in which you are configuring the Gateway, for example `us-central1`.

**Note:** If you use a cross-region Gateway, replace the `--location` flag with a `--scope=all-regions` flag. Failing to use `--scope=all-regions` will result in the certificate not being found when creating the gateway. For example, `'Certificate' was not found`.

### Create a Gateway and HTTPRoute

### Global Gateway

To create a global Gateway, complete the following steps:

  1. Save the following manifest as `cert-map-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
           annotations:
             networking.gke.io/certmap: store-example-com-map
         spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
           # No TLS section is included here because TLS is handled by the certmap annotation.
         

This manifest describes a Gateway with the following properties:

     * `gatewayClassName: gke-l7-global-external-managed`: deploys a global external Application Load Balancer.
     * `protocol: HTTPS` and `port: 443`: required for enabling TLS.

There is no TLS section because TLS is configured with Certificate Manager using the annotation `networking.gke.io/certmap`.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f cert-map-gateway.yaml
         

It might take several minutes for GKE to deploy the Gateway.

  3. To create an HTTPRoute, save the following manifest as `cert-map-http-route.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: foo
           namespace: default
         spec:
           parentRefs:
           - name: external-http
           hostnames:
           - foo.example.com
           rules:
           - matches:
             - path:
                 value: /
             backendRefs:
             - name: foo-v1
               port: 8080
         

  4. Apply the manifest to the cluster:
         
         kubectl apply -f cert-map-http-route.yaml
         




### Regional Gateway

When creating a regional Gateway, you can specify certificates managed by Certificate Manager and certificates managed by Compute Engine.

  1. To create a regional external Gateway, save the following manifest as `external-gateway.yaml`:
         
         kind: Gateway
            apiVersion: gateway.networking.k8s.io/v1
            metadata:
              name: gateway
              namespace: corp
            spec:
              gatewayClassName: gke-l7-regional-external-managed
              listeners:
              - name: gateway-pre-shared-certmap
                protocol: HTTPS
                port: 443
                tls:
                  mode: Terminate # TLS is terminated at the Gateway.
                  options: # Specifies a comma-separated list of Certificate Manager certificates to use for TLS termination.
                    networking.gke.io/cert-manager-certs: store-example-com-cert1, store-example-com-cert2 # These certificates are directly managed by Certificate Manager.
                allowedRoutes:
                  kinds:
                  - kind: HTTPRoute
                  namespaces:
                    from: All
         

This manifest describes a Gateway with the following properties:

     * `gatewayClassName`: `gke-l7-regional-external-managed`: deploys a regional external Application Load Balancer.
     * `protocol: HTTPS` and `port: 443`: required for enabling TLS.
     * `options`: 
       * `networking.gke.io/cert-manager-certs` : certificates managed by Certificate Manager.

To create a regional internal Gateway, in the preceding example, change the value of `gatewayClassName` to `gke-l7-rilb`. This deploys an internal Application Load Balancer.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f external-gateway.yaml
         

  3. To create an HTTPRoute, save the following manifest as `store-external-route.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: store-external
           labels:
             gateway: external-http
         spec:
           parentRefs:
           - name: external-http
           hostnames:
           - "store.example.com"
           rules:
           - backendRefs:
             - name: store-v1
               port: 8080
         

This manifest describes an HTTPRoute that matches traffic for `store.example.com` and forwards the traffic to the `store-v1` Service.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f store-external-route.yaml
         




### Verify the Gateway

  1. Get the IP address of the Gateway:
         
         kubectl get gateway external-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is similar to the following:
         
         203.0.113.12
         

This output is a public IP address, which means any client with internet access can connect to it.

  2. [Update an A or AAAA record](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns) to direct your domain to the IP address of the Gateway.

This step is only necessary if you are configuring a Google-managed SSL Certificate. If you are configuring a self-managed certificate, you can skip this step.

After the DNS records are updated, it can take up to 10 minutes for your load balancer to begin using the Google-managed certificate.

  3. Access the domain of the Gateway using `curl`:
         
         curl https://store.example.com --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert CERTIFICATE_FILE -v
         

Replace the following:

     * `GATEWAY_IP_ADDRESS`: the IP address of the Gateway load balancer.
     * `CERTIFICATE_FILE`: the certificate file that you generated. You must save this file on the machine that you are using to connect to the Gateway. The certificate is required to authenticate the Gateway because the Gateway uses a self-signed certificate.

The output is similar to the following:
    
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
    *  subject: O=example; CN=store.example.com
    *  start date: Apr 19 15:54:50 2021 GMT
    *  expire date: Apr 19 15:54:50 2022 GMT
    *  common name: store.example.com (matched)
    *  issuer: O=example; CN=store.example.com
    *  SSL certificate verify ok.
    ...
    {
      "cluster_name": "gw",
      "host_header": "store.example.com",
      "metadata": "store-v1",
      "node_name": "gke-gw-default-pool-51ccbf30-yya8.c.agmsb-k8s.internal",
      "pod_name": "store-v1-84b47c7f58-tj5mn",
      "pod_name_emoji": "😍",
      "project_id": "agmsb-k8s",
      "timestamp": "2021-04-19T16:30:08",
      "zone": "us-west1-a"
    }
    

This output includes a successful TLS handshake and a response from the application. TLS is terminated at the Gateway correctly and the application responds to the client securely.




## Configure frontend mTLS for a Gateway

You can configure client certificate validation, also known as frontend mTLS, for your GKE Gateway.

Frontend mTLS is supported for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-regional-external-managed`
  * `gke-l7-rilb`
  * `gke-l7-global-external-managed-mc`
  * `gke-l7-regional-external-managed-mc`
  * `gke-l7-cross-regional-internal-managed-mc`
  * `gke-l7-rilb-mc`



Frontend mTLS lets the Gateway authenticate the certificates presented by clients, and is valid for HTTPS listeners that use `Terminate` mode.

**Note:** An HTTPS Gateway requires a server certificate. For information about how to configure server certificates, see the earlier sections of this document.

You can configure frontend mTLS in one of the following ways:

  * Use Gateway API configuration (recommended).
  * Use a self-managed `TrustConfig` annotation on the Gateway (advanced).



### Configure frontend mTLS using Gateway API configuration (recommended)

**Note:** Configuring frontend mTLS by using the `tls.frontendValidation` field requires Gateway API version 1.5 or later.

Using Gateway API is the recommended way to configure client certificate validation. This method involves storing trust sources in a Kubernetes ConfigMap and referencing this ConfigMap in the Gateway specification.

  1. Create trust sources.

Trust sources establish and validate the root of trust for client certificates that are presented to the load balancer. GKE Gateway supports trust sources based on root certificates.

To create certificates, see [Create the root and intermediate certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm#create_the_root_and_intermediate_certificates).

  2. Create a ConfigMap.

Store your trust sources in a Kubernetes ConfigMap. Each key in the ConfigMap must contain exactly one PEM-encoded CA certificate in a valid x509 format. You must create this ConfigMap in the same namespace as your Gateway resource unless you use a ReferenceGrant. To reference a ConfigMap in a different namespace, see [ReferenceGrant](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#referencegrant).

Place the certificate data under the `ca.crt` key:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: my-cert
         data:
           ca.crt: |
             -----BEGIN CERTIFICATE-----
             <PEM_DATA>
             -----END CERTIFICATE-----
         

**Note:** You can reference up to eight ConfigMap resources per configuration (either in the default or per-port configuration). Only root certificates are supported when using a ConfigMap. To use intermediate or allowed certificates, you must use a self-managed TrustConfig resource.

To create a ConfigMap with your certificates, run the following command:
         
         kubectl create configmap my-config \
             --from-file=ca.crt=ROOT_CERT_PATH
         

Replace `ROOT_CERT_PATH` with the path to your certificate file. A ConfigMap can contain only one certificate.

  3. Configure the Gateway.

Attach the ConfigMap to your Gateway by adding a `tls` section that contains the `frontendValidation` field to your Gateway specification. The `default` configuration is required and applies to all HTTPS listeners that use `Terminate` mode unless you specify a per-port configuration. The following example shows an end-to-end Gateway configuration that includes both a server certificate (by using the `certmap` annotation) and client certificate validation (by using the `tls.frontendValidation` field):
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: mtls-example
           annotations:
             networking.gke.io/certmap: store-example-com-map
         spec:
           gatewayClassName: gke-l7-global-external-managed
           tls:
             frontend:
               default:
                 validation:
                   caCertificateRefs:
                   - kind: ConfigMap
                     group: ""
                     name: my-config
           listeners:
           - name: foo-https
             protocol: HTTPS
             port: 443
             hostname: foo.example.com
             tls:
               mode: Terminate
               # No certificateRefs needed when using the certmap annotation
         

  4. Override configuration per port.

You can also specify unique trust sources for individual ports. A per-port configuration overrides the default configuration for all listeners configured for that port.
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: mtls-port-override
           annotations:
             networking.gke.io/certmap: store-example-com-map
         spec:
           gatewayClassName: gke-l7-global-external-managed
           tls:
             frontend:
               default:
                 validation:
                   caCertificateRefs:
                   - kind: ConfigMap
                     group: ""
                     name: global-ca-config
               perPort:
               - port: 8443
                 tls:
                   validation:
                     caCertificateRefs:
                     - kind: ConfigMap
                       group: ""
                       name: port-specific-ca-config
           listeners:
           - name: https-default
             protocol: HTTPS
             port: 443
             tls:
               mode: Terminate
           - name: https-override
             protocol: HTTPS
             port: 8443
             tls:
               mode: Terminate
         

  5. Optional: configure the client validation mode.

By default, GKE Gateways enforce strict client certificate validation (`AllowValidOnly`). To allow invalid or missing client certificates, in the `frontendValidation.default` configuration, set the value of the `mode` key to `AllowInsecureFallback`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: mtls-example
           annotations:
             networking.gke.io/certmap: store-example-com-map # Add this annotation
         spec:
           gatewayClassName: gke-l7-global-external-managed
           tls:
             frontendValidation:
               default:
                 caCertificateRefs:
                 - kind: ConfigMap
                   group: ""
                   name: my-config
                 mode: AllowInsecureFallback
           listeners:
           - name: foo-https
             protocol: HTTPS
             port: 443
             hostname: foo.example.com
             tls:
               mode: Terminate
               # No certificateRefs needed when using the certmap annotation
         




### Use a self-managed TrustConfig (advanced)

Alternatively, configure client certificate validation by annotating your Gateway with a TrustConfig resource. Use this self-managed method if you need additional flexibility or if your configuration exceeds standard Gateway API limitations. This method is mutually exclusive with the Gateway API configuration method and applies to all HTTPS listeners on the Gateway (per-port overrides are not supported).

  1. Create a TrustConfig resource. For instructions, see [Create a trust config resource](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm#trustconfig).

When you create the TrustConfig resource, specify `global` for global Gateways (`gke-l7-global-external-managed`) and all multi-cluster Gateways (`gke-l7-global-external-managed-mc`, `gke-l7-regional-external-managed-mc`, `gke-l7-cross-regional-internal-managed-mc`, and `gke-l7-rilb-mc`), or the appropriate region (for example, `us-central1`) for regional Gateways (`gke-l7-regional-external-managed` and `gke-l7-rilb`).

  2. Attach the TrustConfig to your Gateway by using the `networking.gke.io/frontend-trust-config` annotation.

The following example shows an end-to-end Gateway configuration that includes both a server certificate (using the `certmap` annotation) and client certificate validation (using the `TrustConfig` annotation):
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: mtls-example
           annotations:
             networking.gke.io/frontend-trust-config: my-trust-config
             networking.gke.io/certmap: store-example-com-map # Add this annotation
         spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: foo-https
             protocol: HTTPS
             port: 443
             hostname: foo.example.com
             tls:
               mode: Terminate
               # Remove certificateRefs and replace with the comment
               # No certificateRefs needed when using the certmap annotation
         

  3. Optional: configure the client validation mode.

By default, GKE Gateways enforce strict client certificate validation (`REJECT_INVALID`). To allow invalid or missing client certificates, set the `networking.gke.io/allow-invalid-or-missing-client-cert` annotation to `true`.




## Configure backend TLS for a Gateway

Backend TLS enables the GKE Gateway load balancer to verify the identity of the backends it connects to. Backend TLS adds an explicit verification step during the TLS handshake between the Gateway and the backend Pod. The Gateway acts as the TLS client, validating the backend server's certificate against a set of trusted Certificate Authorities (CAs) that you configure. This verification occurs when a new connection is established, ensuring the Gateway communicates only with trusted backends and enhancing overall security.

**Note:** Ensure that your application Pods are running an HTTPS server on the port targeted by your Service or InferencePool.

You can configure _backend authenticated TLS_ using a BackendTLSPolicy resource attached to a Service, InferencePool, ServiceImport, or GCPInferencePoolImport. The BackendTLSPolicy must reside in the same namespace as the target resource.

Backend TLS is supported for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-global-external-managed-mc`
  * `gke-l7-regional-external-managed`
  * `gke-l7-regional-external-managed-mc`
  * `gke-l7-cross-regional-internal-managed-mc`
  * `gke-l7-rilb`
  * `gke-l7-rilb-mc`



## Configure backend mTLS for a Gateway

**Note:** Configuring backend mTLS by using the `spec.tls.backend.clientCertificateRef` field requires Gateway API version 1.5 or later.

Backend mutual TLS (mTLS) is a feature built on top of backend authenticated TLS. Although backend authenticated TLS verifies the identity of backend Pods to the load balancer, backend mTLS enables the GKE Gateway load balancer to also authenticate its own identity to backend Pods by presenting a client certificate. You must configure backend authenticated TLS as part of setting up backend mTLS.

GKE Gateway configures backend mTLS by using the standard Gateway API `spec.tls.backend.clientCertificateRef` field.

Backend mTLS is supported for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-regional-external-managed`
  * `gke-l7-rilb`
  * `gke-l7-global-external-managed-mc`
  * `gke-l7-regional-external-managed-mc`
  * `gke-l7-cross-regional-internal-managed-mc`
  * `gke-l7-rilb-mc`



To configure backend mTLS, complete the following steps:

  1. Store the client certificate and private key in a standard Kubernetes Secret.
  2. Reference the client certificate Secret in your Gateway resource specification.
  3. Configure backend authenticated TLS by using a BackendTLSPolicy that targets your Service.



### Step 1: Store client credentials

Before storing your client credentials, ensure that your certificate complies with the [certificate requirements](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls#certificate-requirements).

To store the client certificate and private key in a standard Kubernetes TLS Secret in the same namespace as your Gateway resource, run the following command:
    
    
    kubectl create secret tls gateway-client-identity \
        --cert=PATH_TO_CERT_FILE \
        --key=PATH_TO_KEY_FILE \
        --namespace=default
    

Replace the following values:

  * `PATH_TO_CERT_FILE`: the path to your PEM-formatted client certificate file.
  * `PATH_TO_KEY_FILE`: the path to your PEM-formatted private key file.



### Step 2: Reference client credentials in the Gateway

  1. To reference the client certificate Secret under the `spec.tls.backend` block of your Gateway resource, save the following manifest as `my-gateway.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: my-gateway
           namespace: default
         spec:
           gatewayClassName: gke-l7-global-external-managed
           tls:
             backend:
               clientCertificateRef:
                 group: "" # empty group resolves to Core API
                 kind: Secret
                 name: gateway-client-identity
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
             tls:
               mode: Terminate
         

  2. Apply the manifest to the cluster:
         
         kubectl apply -f my-gateway.yaml
         




### Step 3: Apply the BackendTLSPolicy

To validate the backend server's identity, you must apply a BackendTLSPolicy targeting the Service that is referenced by your HTTPRoute.

For detailed instructions and manifests on how to set up backend authenticated TLS, see Configure backend TLS for a Gateway.

### Use a Kubernetes ConfigMap (Standard)

**Best practice:** We recommend this method for configuring backend TLS because it uses standard Kubernetes built-in objects and is fully conformant with Gateway API. 

In this method, you provide the CA certificate directly in a Kubernetes ConfigMap.

  1. Create a ConfigMap resource containing your PEM-encoded CA certificates. For more information, see [certificate requirements](https://docs.cloud.google.com/load-balancing/docs/mtls#certificate-requirements). Each ConfigMap must contain only one CA certificate. You must create this ConfigMap in the same namespace as your BackendTLSPolicy resource. BackendTLSPolicy doesn't support cross-namespace references to ConfigMap resources.

**Note:** A single BackendTLSPolicy supports referencing up to eight ConfigMap resources in the `caCertificateRefs` field.

The certificate data must be placed under the `ca.crt` key:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: my-backend-ca
         data:
           ca.crt: |
             -----BEGIN CERTIFICATE-----
             PEM_DATA
             -----END CERTIFICATE-----
         

Replace `PEM_DATA` with the Base64-encoded, PEM-formatted content of your CA certificate.

  2. Target a Service, InferencePool, ServiceImport, or GCPInferencePoolImport with a BackendTLSPolicy that references the ConfigMap:

### Service

The following manifest shows a BackendTLSPolicy targeting a Service:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: BackendTLSPolicy
         metadata:
           name: secure-backend-policy
         spec:
           targetRefs:
           - group: "" # empty group means Core API.
             kind: Service
             name: my-service-name
           validation:
             hostname: "backend.example.com"
             caCertificateRefs:
             - group: "" # empty group means Core API.
               kind: ConfigMap
               name: my-backend-ca
         

### InferencePool

The following manifest shows a BackendTLSPolicy targeting an InferencePool:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: BackendTLSPolicy
         metadata:
           name: secure-backend-policy-inferencepool
         spec:
           targetRefs:
           - group: "inference.networking.k8s.io" # For InferencePool
             kind: InferencePool
             name: my-inference-pool
           validation:
             hostname: "backend.example.com"
             caCertificateRefs:
             - group: "" # empty group means Core API.
               kind: ConfigMap
               name: my-backend-ca
         

### ServiceImport

The following manifest shows a BackendTLSPolicy targeting a ServiceImport:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: BackendTLSPolicy
         metadata:
           name: secure-backend-policy-serviceimport
         spec:
           targetRefs:
           - group: "net.gke.io" # For ServiceImport
             kind: ServiceImport
             name: my-service-import
           validation:
             hostname: "backend.example.com"
             caCertificateRefs:
             - group: "" # empty group means Core API.
               kind: ConfigMap
               name: my-backend-ca
         

### GCPInferencePoolImport

The following manifest shows a BackendTLSPolicy targeting a GCPInferencePoolImport:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: BackendTLSPolicy
         metadata:
           name: secure-backend-policy-gcpinferencepoolimport
         spec:
           targetRefs:
           - group: "networking.gke.io" # For GCPInferencePoolImport
             kind: GCPInferencePoolImport
             name: my-gcp-inference-pool-import
           validation:
             hostname: "backend.example.com"
             caCertificateRefs:
             - group: "" # empty group means Core API.
               kind: ConfigMap
               name: my-backend-ca
         




### Use a self-managed TrustConfig (Advanced)

**Note:** Use this method if your configuration requires advanced features like certificate allowlisting, or if it exceeds standard Gateway API limitations, such as the maximum number of supported intermediate or trust anchor certificates.

This method lets you reference a TrustConfig resource that you manage independently in Google Cloud Certificate Manager.

  1. Create a TrustConfig resource in Certificate Manager. The TrustConfig must be created in the same project and location as the Gateway.

     * For _global_ or _multi-cluster_ Gateways (including regional multi-cluster) and _cross-regional_ Gateways, use the `global` location.
     * For _regional single-cluster_ Gateways, use the same region as the Gateway.
     * If your Service is used by multiple Gateways in different locations, you must create a TrustConfig resource with the same name in each of those locations.
  2. Target a Service with a BackendTLSPolicy that references the external TrustConfig resource through the `options` field:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: BackendTLSPolicy
         metadata:
           name: secure-backend-policy
         spec:
           targetRefs:
           - group: "" # empty group means Core API.
             kind: Service
             name: my-service-name
           validation:
             wellKnownCACertificates: "System"
             hostname: "backend.example.com"
             options:
               networking.gke.io/backend-trust-config: "my-trust-config-name"
         

**Note:** You cannot use both the `wellKnownCACertificates: "System"` and `caCertificateRefs` settings on the same object; doing so invalidates the policy.



### BackendTLSPolicy field reference

The following table describes the key fields in a BackendTLSPolicy resource:

Field | Description  
---|---  
**`targetRefs`** | The backend resources to which this policy applies. Supports Service (`group: ""`), InferencePool (`group: "inference.networking.k8s.io"`), ServiceImport (`group: "net.gke.io"`), or GCPInferencePoolImport (`group: "networking.gke.io"`). **Note:** For `gke-l7-global-external-managed` and `gke-l7-global-external-managed-mc` GatewayClasses, only Service and ServiceImport backends are supported.  
**`validation.hostname`** | The hostname (SNI) used by the Gateway during the TLS handshake with the backend pods.  
**`validation.subjectAltNames`** | Optional. Defines one or more Subject Alternative Names (SANs) to validate against the backend's certificate. Supports `Hostname` and `URI` (such as SPIFFE IDs).  
**`validation.caCertificateRefs`** | Standard method. References a list of ConfigMap resources (up to eight) in the same namespace. Each ConfigMap must contain a single PEM-encoded CA certificate under the `ca.crt` key. Cross-namespace references are not supported.  
**`validation.wellKnownCACertificates`** | Advanced method. Set the value to `System` when using a self-managed TrustConfig.  
**`options`** | A map for GKE-specific options. Use the `networking.gke.io/backend-trust-config` setting to reference an external TrustConfig resource.  
  
### Verify the Backend TLS configuration

After applying the BackendTLSPolicy, verify that the Gateway controller has accepted the configuration by checking the policy status:
    
    
    kubectl describe backendtlspolicy POLICY_NAME
    

Replace `POLICY_NAME` with the name of your policy.

A policy is successfully applied if it contains `Accepted` and `ResolvedRefs` conditions with `Status: "True"` in the `Status.Ancestors` section:
    
    
    Status:
      Ancestors:
      - Ancestor Ref:
          Group: gateway.networking.k8s.io
          Kind: Gateway
          Name: my-gateway-name
          Namespace: default
        Conditions:
        - Last Transition Time: "2026-02-17T15:19:26Z"
          Message: ""
          Reason: Accepted
          Status: "True"
          Type: Accepted
        - Last Transition Time: "2026-02-17T15:19:26Z"
          Message: ""
          Reason: ResolvedRefs
          Status: "True"
          Type: ResolvedRefs
        Controller Name: networking.gke.io/gateway
    

If `Status` is `False` for any of these conditions, it indicates the policy has not been applied. Check the `Reason` and `Message` fields for more details. Common errors include referencing a ConfigMap in `caCertificateRefs` that does not exist or is missing the `ca.crt` key.

This status confirms that the Gateway has successfully validated the policy and applied the TLS settings to the backends of the target Service or InferencePool. The BackendTLSPolicy resource must reside in the same namespace as the target resource.

## Secure load balancer to application traffic using TLS

You can encrypt traffic from the load balancer to backend Pods using the `ports[].appProtocol` field. The supported fields for `appProtocol` are: `HTTP`, `HTTPS`, `HTTP2`, and `kubernetes.io/h2c`.

The following manifest describes a Service that specifies the load balancer must use HTTPS traffic to communication with the backend Pods:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: store-v2
    spec:
      selector:
        app: store
        version: v2
      ports:
      - port: 8080
        targetPort: 8080
        appProtocol: HTTPS
    

The GKE Gateway controller doesn't manage the certificate used by backend Pods. It is your responsibility to ensure the certificate used on the backend Pods is valid.

**Note:** The previously supported `networking.gke.io/app-protocol` is deprecated. This annotation is not supported by the GKE Gateway controller.

## Secure client to load balancer traffic using SSL policies

When your applications are exposed through an external gateway that uses HTTPS, it is important to use the latest protocols or specify the minimum [SSL or TLS](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) version. You can secure the client to load balancer traffic by using SSL policies.

To know more about SSL policies that can be attached to your Gateway and how to create them, see [Configure SSL Policies to secure client to load balancer traffic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_ssl_policies).

## Protect your backends using Google Cloud Armor

[Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) help you protect your load-balanced applications from web-based attacks. Once you have [configured a Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies), you can reference it in a GCPBackendPolicy applied to your Kubernetes Services.

To configure Google Cloud Armor policies with Gateway, see [Configure Google Cloud Armor security policy to secure your backend Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor).

## Authenticate requests to your backends using Identity-Aware Proxy

[Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview) helps you protect your backends from unwanted traffic by authenticating clients sending requests to your applications and enforcing role-based traffic authorization. After you enable [Identity-Aware Proxy for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto), you can reference your OAuth credentials in a GCPBackendPolicy applied to your Kubernetes Services.

To configure Identity-Aware Proxy with Gateway, see [Configure Identity-Aware Proxy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_iap).

**Note:** IAP is incompatible with Cloud CDN. If your application requires edge caching by using the GCPHTTPFilter resource, ensure that IAP is not enabled for the same Gateway or its routes. For more information about configuring caching, see [Configure Cloud CDN for Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cdn-for-gateway).

## Configure Cross-Origin Resource Sharing (CORS)

Cross-Origin Resource Sharing (CORS) is a security mechanism that helps web applications running at one origin (domain) securely access resources hosted on a different origin. You can configure CORS policies directly in your HTTPRoute resources by using the `CORS` filter. When you configure the CORS filter, GKE Gateway offloads responding to preflight (`OPTIONS`) requests and injecting CORS response headers from your application code.

For more information about how to configure the CORS filter and the supported fields, see [Configure Cross-Origin Resource Sharing (CORS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors).

## Enforce access control using authorization policies

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce granular, identity-based access control on traffic that enters your Gateway by using authorization policies (GCPAuthzPolicy). This policy lets you define rules that `ALLOW` or `DENY` requests based on the source identity (such as a client certificate's Subject Alternative Name or common name), the target path, or specific HTTP headers.

For advanced security scenarios, you can delegate authorization decisions to external services or third-party engines (such as a custom web application firewall) by using an authorization extension (GCPAuthzExtension).

### Set up an `ALLOW` authorization policy

The following example describes an authorization policy that applies to a Gateway in the `default` namespace. The policy restricts access by only allowing requests to the `/home` and `/public` paths, which implicitly denies access to all other paths.

  1. Save the following manifest to `allow-policy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: allow-paths
           namespace: default
         spec:
           enforcementLevel: L7
           targetRefs:
           - group: gateway.networking.k8s.io
             kind: Gateway
             name: "GATEWAY_NAME"
           action: ALLOW
           rules:
           - to:
               operations:
               - paths:
                 - type: Exact
                   value: "/home"
                 - type: Exact
                   value: "/public"
         

Replace `GATEWAY_NAME` with the name of your Gateway.

  2. Apply the manifest:
         
         kubectl apply -f allow-policy.yaml
         




### Set up a `DENY` authorization policy

The following example describes an authorization policy that applies to a Gateway in the `default` namespace. The policy explicitly denies all requests to the `/private` path while permitting access to all other paths by default.

  1. Save the following manifest to `deny-policy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: deny-path
           namespace: default
         spec:
           enforcementLevel: L7
           targetRefs:
           - group: gateway.networking.k8s.io
             kind: Gateway
             name: "GATEWAY_NAME"
           action: DENY
           rules:
           - to:
               operations:
               - paths:
                 - type: Exact
                   value: "/private"
         

Replace `GATEWAY_NAME` with the name of your Gateway.

  2. Apply the manifest:
         
         kubectl apply -f deny-policy.yaml
         




## What's next

  * Learn more about [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).
  * Learn how to [configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).
  * Learn how to [deploy Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Learn more about [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
