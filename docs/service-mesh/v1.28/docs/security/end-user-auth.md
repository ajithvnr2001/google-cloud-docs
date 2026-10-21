---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/security/end-user-auth/
title: Configuring Cloud Service Mesh user authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:02.680490+00:00
---

# Configuring Cloud Service Mesh user authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/security/end-user-auth/

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

# Configuring Cloud Service Mesh user authentication

**Caution:** There is a known issue with the TRAFFIC_DIRECTOR control plane implementation. If you are using that implementation, then you must make changes in the `istio-asm-managed-rapid` configmap, even if you are using a channel other than rapid.

Cloud Service Mesh user authentication is an integrated solution for browser-based end-user authentication and access control to your deployed workloads. It lets you integrate with existing Identity Providers (IDP) for user authentication and uses Istio APIs and authorization policies for access management. It is a user-friendly alternative to Istio JSON Web Token (JWT) authentication.

A typical use-case is when an organization uses Cloud Service Mesh to host a web application for its workforce to access via a web browser. In addition, the organization needs to use their existing identity provider to manage user identities. Cloud Service Mesh user authentication makes it easy for users to authenticate using a standard web-based OpenID Connect (OIDC) login and consent flow. When the user authenticates, Cloud Service Mesh enforces Istio authorization policies, and on successful authorization, it transmits the identity to workloads in a secure credential format.

## How it works

Cloud Service Mesh user authentication introduces a new component, `authservice`. This component integrates with the Envoy-based ingress as an external authorization service that intercepts all the incoming requests for authentication. `authservice` implements the client-side of the OIDC protocol and enables user access to applications via a browser, where users complete an interactive authentication and consent flow to establish a short-lived session. `authservice` implements industry standard protocols to integrate with any identity provider that can act as a OIDC authorization server. When the user is authenticated, the principal information is encapsulated in an `RCToken` in JWT format, signed by `authservice` which it forwards to the Istio authorization layer in the ingress. This model provides perimeter access control for traffic into the mesh. If the user is authorized to access a resource, this RCToken is also forwarded to the microservices to obtain principal information and enforce fine-grained access control.

The following diagram shows the location of `authservice` in the mesh and how it relates to the other parts of the mesh, such as the ingress, workloads, user's browser, and any existing IDP.

![end user authentication](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/user-auth.svg)

Administrators can install `authservice` as an add-on over a Cloud Service Mesh installation. When installed, `authservice` reads the OIDC endpoint configuration and other associated settings defined in the `UserAuth` custom resource. The administrator can use Cloud Service Mesh `ExternalAuthorization` APIs to configure `auth_server` as a filter on the ingress.

## Install the user authentication service

The following steps explain how to configure the `authservice`.

### Prerequisites

Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools) to: 

  * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster)


  * If you are using managed Cloud Service Mesh on a private cluster, then ensure the cluster is capable of sending egress traffic to the IDP.



Additionally, ensure that you meet the prerequisites by using the following steps.

#### Customize the installation user authentication overlay

To install the user authentication service, you must customize the Cloud Service Mesh installation to add a mesh-level external authorization provider. The steps required depend on whether you are using managed or in-cluster Cloud Service Mesh.

**Important:** Make sure you have kpt v1.0 or later.

### Managed

  1. Update the [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) to include the user authentication MeshConfig. In the following command, use the same `REVISION_LABEL` you used when [provisioning managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/managed/provision-managed-anthos-service-mesh) (such as, `asm-managed`, `asm-managed-rapid`, or `asm-managed-stable`):
         
         kubectl edit configmap istio-REVISION_LABEL -n istio-system
         

  2. Add the following text under `mesh` field in the MeshConfig:
         
         mesh: |-
         ...
           extensionProviders:
           - name: "asm-userauth-grpc"
             envoyExtAuthzGrpc:
               service: "authservice.asm-user-auth.svc.cluster.local"
               port: "10003"
         

  3. Create `asm-user-auth` namespace.
         
         kubectl create namespace asm-user-auth
         

  4. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.28/docs/check-control-plane-implementation).

### Managed (TD)

Apply the default injection label to the namespace:
         
         kubectl label namespace asm-user-auth \
             istio.io/rev- istio-injection=enabled --overwrite
         

### Managed (Istiod)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

**Recommended:** Run the following command to apply the default injection label to the namespace:
         
         ```sh
         kubectl label namespace asm-user-auth \
             istio.io/rev- istio-injection=enabled --overwrite
         ```
         

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
    
    kubectl -n istio-system get controlplanerevision
    

The output is similar to the following:
    
    NAME                AGE
    asm-managed-rapid   6d7h
    

**Note:** If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/v1.28/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     1. Apply the revision label to the namespace:
            
            kubectl label namespace asm-user-auth \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  5. [Install the Istio gateway](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh#install_gateways) in the `asm-user-auth` namespace.
         
         kubectl apply -n asm-user-auth -f DIR_PATH/samples/gateways/istio-ingressgateway
         

**Note:** `DIR_PATH` refers to the location of the [`anthos-service-mesh-packages` repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages) on your machine. If you do not have this repository on your machine, clone it: `git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages.git`



### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

  1. Get the example [user auth overlay](https://github.com/GoogleCloudPlatform/asm-user-auth/blob/v1.2.5/overlay/user-auth-overlay.yaml) and update it if there are any customizations in your mesh. It is a recommended best practice to maintain this overlay file in your source control.
         
         curl https://raw.githubusercontent.com/GoogleCloudPlatform/asm-user-auth/v1.2.5/overlay/user-auth-overlay.yaml > user-auth-overlay.yaml
         

  2. Follow the [install Cloud Service Mesh with overlay](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh#install_with_optional_features) to use a Google-provided script to install Cloud Service Mesh with the user authentication overlay. For example:
         
         ./asmcli install \
           --project_id PROJECT_ID \
           --cluster_name CLUSTER_NAME \
           --cluster_location CLUSTER_LOCATION \
           --fleet_id FLEET_PROJECT_ID \
           --output_dir DIR_PATH \
           --enable_all \
           --custom_overlay user-auth-overlay.yaml
         

**Important:** If you customize the installation with multiple overlays, ensure the `--custom_overlay` option includes all your overlay files.

The user authentication `kpt` packages creates an `AuthorizationPolicy` to reference the external authorization provider specified by `pkg/ext-authz.yaml`.

  3. Create `asm-user-auth` namespace.
         
         kubectl create namespace asm-user-auth
         

  4. Enable the namespace for injection.

**Recommended:** Run the following command to apply the default injection label to the namespace:
         
         kubectl label namespace asm-user-auth \
               istio.io/rev- istio-injection=enabled --overwrite
         

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
              jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace asm-user-auth \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  5. [Install the Istio gateway](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh#install_gateways) in the `asm-user-auth` namespace.
         
         kubectl apply -n asm-user-auth -f DIR_PATH/samples/gateways/istio-ingressgateway
         

**Note:** `DIR_PATH` refers to the location of the [`anthos-service-mesh-packages` repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages) on your machine. If you do not have this repository on your machine, clone it: `git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages.git`



#### Prepare the OIDC client configuration

Set your OIDC client configuration by using the following steps. This guide uses Google as an IDP, but you can use any IDP that supports OIDC authentication.

  1. In the Google Cloud console, go to **API & Services** > **Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Go to **Create Credentials** , then choose **OAuth client ID**. If required, set your **OAuth consent screen** options, then configure the following options:

     * Set **Application type** to **Web application**.
     * Set **Authorized redirect URI** to `https://REDIRECT_HOST/REDIRECT_PATH`. For example, for localhost you could set to `https://localhost:8443/_gcp_asm_authenticate`.

Then, click **Save**.

  3. In addition, save your OIDC client configuration to use later.
         
         export OIDC_CLIENT_ID=CLIENT_ID
         export OIDC_CLIENT_SECRET=CLIENT_SECRET
         export OIDC_ISSUER_URI=ISSUER_URI
         export OIDC_REDIRECT_HOST=REDIRECT_HOST
         export OIDC_REDIRECT_PATH=REDIRECT_PATH
         




#### Get the `kpt` packages

Use the following steps to install the recommended `authservice` configuration from the [public repository](https://github.com/GoogleCloudPlatform/asm-user-auth). These commands retrieve the latest `authservice` container and start it as a Pod in the `asm-user-auth` namespace. It also configures the ingress to intercept all requests.

Get the kpt package:
    
    
    kpt pkg get https://github.com/GoogleCloudPlatform/asm-user-auth.git/@v1.2.5 .
    cd asm-user-auth/
    

### Set the redirection URL and secret for ingress gateway

`OAuth2` requires a redirection URL hosted on an HTTPS-protected endpoint. These commands are for example purposes and simplify setup by generating a self-signed certificate for the Istio ingress gateway.

**Important:** A production deployment should not use self-signed certificates.

  1. Generate a self-signed certificate:
         
         openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
          -days 365 -nodes -subj '/CN=localhost'
         

  2. Create a secret for the ingress gateway to host HTTPS traffic:
         
         kubectl create -n asm-user-auth secret tls userauth-tls-cert --key=key.pem \
         --cert=cert.pem
         




### Apply the encryption and signing keys

The `authservice` needs two sets of keys to operate successfully. The first is a symmetric key for encryption and decryption. This key is used for encrypting the session state before setting that as a cookie.

The second set of keys are a public/private key pair. This key is used to sign the authenticated user information in JWT format as an RCToken. The public key from this pair is published at a predefined endpoint that the sidecars can use to validate the JWT.

The user authentication `kpt` package contains two sample keys for quick setup. However, you can use your preferred key management system to generate these keys instead.

  1. Prepare the session encryption key with following format or use the sample from the pkg, which you can view by `cat ./samples/cookie_encryption_key.json`.
         
         {
           "keys":[
              {
                 "kty":"oct",
                 "kid":"key-0",
                 "K":"YOUR_KEY",
                 "useAfter": 1612813735
              }
           ]
         }
         

You can generate a test AES key with following command:
         
         openssl enc -aes-256-cbc -k mycustomkey -P -md sha1 | grep key
         

  2. Prepare the RCToken signing key with following format or use the sample from the pkg, which you can view by `cat ./samples/rctoken_signing_key.json`.
         
         {
           "keys":[
              {
                 "kty":"RSA",
                 "kid":"rsa-signing-key",
                 "K":"YOUR_KEY",  # k contains a Base64 encoded PEM format RSA signing key.
                 "useAfter": 1612813735  # unix timestamp
              }
           ]
         }
         

You can generate a test 512-bit RSA private key with following command:
         
         openssl genpkey -algorithm RSA -out rsa_private.pem -pkeyopt rsa_keygen_bits:512
         

  3. Create the kubernetes secret, which `authservice` will mount into its own file system.

**Important:** In a production environment, generate your own keys to populate the JSON file instead.
         
         kubectl create secret generic secret-key  \
             --from-file="session_cookie.key"="./samples/cookie_encryption_key.json" \
             --from-file="rctoken.key"="./samples/rctoken_signing_key.json"  \
             --namespace=asm-user-auth
         




### Deploy the user authentication service

The following commands create the user authentication service and deployment in the `asm-user-auth` namespace.

Set the necessary values for User Auth configuration. The client ID and secret are stored as Kubernetes secrets, so we use Base64 to encode them. Please visit [public repository](https://github.com/GoogleCloudPlatform/asm-user-auth/tree/v1.2.5/pkg) to view all available setters.
    
    
    kpt fn eval pkg --image gcr.io/kpt-fn/apply-setters:v0.2 --truncate-output=false -- \
      client-id="$(echo -n ${OIDC_CLIENT_ID} | base64 -w0)" \
      client-secret="$(echo -n ${OIDC_CLIENT_SECRET} | base64 -w0)" \
      issuer-uri="${OIDC_ISSUER_URI}" \
      redirect-host="${OIDC_REDIRECT_HOST}" \
      redirect-path="${OIDC_REDIRECT_PATH}"
    

Apply the `kpt` package:
    
    
    # Remove the potential alpha version CRD if exists.
    kubectl delete crd userauthconfigs.security.anthos.io
    kubectl apply -f ./pkg/asm_user_auth_config_v1beta1.yaml
    kubectl apply -f ./pkg
    

The `authservice` consumes the `UserAuthConfig` CRD to provide end user authentication. `UserAuthConfig` is configurable in the run time, and you can update it to change the `authservice` behavior and configure it with endpoints for any OIDC authorization server.

You can view the file by `cat pkg/user_auth_config.yaml`, it contains these fields:
    
    
    apiVersion: security.anthos.io/v1beta1
    kind: UserAuthConfig
    metadata:
      name: user-auth-config
      namespace: asm-user-auth
    spec:
      authentication:
        oidc:
          certificateAuthorityData: ""  # kpt-set: ${ca-cert}
          issuerURI: "<your issuer uri>"  # kpt-set: ${issuer-uri}
          proxy: ""  # kpt-set: ${proxy}
          oauthCredentialsSecret:
            name: "oauth-secret"  # kpt-set: ${secret-name}
            namespace: "asm-user-auth"  # kpt-set: ${secret-namespace}
          redirectURIHost: ""  # kpt-set: ${redirect-host}
          redirectURIPath: "/_gcp_asm_authenticate"  # kpt-set: ${redirect-path}
          scopes: ""  # kpt-set: ${scopes}
          groupsClaim: ""  # kpt-set: ${groups}
      outputJWTAudience: "test_audience"  # kpt-set: ${jwt-audience}
    

See user authentication configuration details for detailed descriptions of the `user_auth_config.yaml` fields.

### Configure API Request Identifiers

**Note:** API request identifiers are only supported on Cloud Service Mesh user authentication versions 1.2.5 and higher.

API request identifiers are a set of [Common Expression Language (CEL)](https://github.com/google/cel-spec) expressions used by Cloud Service Mesh user authentication to identify API requests. By defining these identifiers, you enable Cloud Service Mesh user authentication to handle API request authentication failures semantically.

Specifically, when you provide CEL expressions that identify your API requests, you allow Cloud Service Mesh user authentication to fail unauthenticated API requests with a 401-Unauthorized status code. This is crucial for clients like CLIs and service accounts, which expect this status code for unauthenticated API requests.

Without API request identifiers, Cloud Service Mesh user authentication will redirect all unauthenticated requests to the configured OpenID Connect (OIDC) provider, returning a 302-Found status code. This redirect behavior is generally undesirable for API requests, which expect a 401-Unauthorized on failure.

To define your API request identifiers, add an `apiRequestIdentifier` section to your `UserAuthConfig CR`. This allows adding multiple CEL expressions. If multiple CEL expressions are provided, a request is considered an API request if it matches at least one of them.

The following example shows how to designate as an API request: any request containing the header `example-api-header`, any request directed to the host `api.example.com`, or any request targeting a path under `/v1/api/`.

**Note:** Fields relevant to `apiRequestIdentifier` are highlighted.
    
    
    apiVersion: security.anthos.io/v1beta1
    kind: UserAuthConfig
    metadata:
      name: user-auth-config
      namespace: asm-user-auth
    spec:
      authentication:
        oidc:
          certificateAuthorityData: ""  # kpt-set: ${ca-cert}
          issuerURI: "<your issuer uri>"  # kpt-set: ${issuer-uri}
          proxy: ""  # kpt-set: ${proxy}
          oauthCredentialsSecret:
            name: "oauth-secret"  # kpt-set: ${secret-name}
            namespace: "asm-user-auth"  # kpt-set: ${secret-namespace}
          redirectURIHost: ""  # kpt-set: ${redirect-host}
          redirectURIPath: "/_gcp_asm_authenticate"  # kpt-set: ${redirect-path}
          scopes: ""  # kpt-set: ${scopes}
          groupsClaim: ""  # kpt-set: ${groups}
      outputJWTAudience: "test_audience"  # kpt-set: ${jwt-audience}
      **apiRequestIdentifier : **    **name : "api-request-identifiers"**    **expressions : **    **- "'example-api-header' in http_request.headers"**    **- "http_request.host == 'api.example.com'"**    **- "matches(http_request.path, '/v1/api/(.*)')"**    # other expressions go here
    

Cloud Service Mesh user authentication CEL expressions can be constructed from the following fields:

**Note:** Cloud Service Mesh user authentication CEL expressions must evaluate to a boolean value (True or False).

  1. `http_request.headers`: A map of the HTTP request headers, where the keys are lowercase strings and the values are vectors of strings.

Use this field in your CEL expression to designate requests with specific headers as API requests.

  2. `http_request.host`: The requested HTTP URL host (e.g. `api.example.com`).

Use this field in your CEL expression to designate requests to specific hosts as API requests.

  3. `http_request.path`: The requested HTTP URL path (e.g. `/example-api-path`). This always starts with '/' and does not contain the query component of the request URL.

Use this field in your CEL expression to designate requests with specific paths as API requests.




The next section shows sample CEL expressions that check and match parts of these fields to inform Cloud Service Mesh user authentication on how to determine which requests are API requests.

#### Sample Expressions

Match all requests that contain the header `X-API-Key`:

**Note:** the header must be specified in lowercase.
    
    
    "'x-api-key' in http_request.headers"
    

Match all requests with the header `X-API-Key` set to a particular value:

**Note:** the header must be specified in lowercase.
    
    
    "'x-api-key' in http_request.headers && http_request.headers['x-api-key'].values == ['example-value ']"
    

Match all requests to the host `api.example.com`:
    
    
    "http_request.host == api.example.com"
    

Match all requests to the path `/api/query`:

**Note:** paths must start with a `/`.
    
    
    "http_request.path == /api/query"
    

Match all requests to any path under `/api/`:
    
    
    "matches(http_request.path, '/api/(.*)')"
    

## Perform post-install tasks

The following tasks are required after you finish the previous installation steps.

### Enable user authentication for your applications

This section demonstrates how to enable user authentication, by using the `httpbin` as an example.

Cloud Service Mesh user authentication uses a [`CUSTOM`](https://istio.io/v1.28/docs/tasks/security/authorization/authz-custom/) typed authorization policy to trigger the OIDC flow.

After you have [installed the Istio gateway](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh#install_gateways), configure it to serve HTTPS traffic using the TLS certificate `userauth-tls-cert` you created above. Below is the `pkg/gateway.yaml` configuration that you just installed.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: userauth
      namespace: asm-user-auth
    spec:
      selector:
        istio: ingressgateway
      servers:
      - hosts:
        - '*'
        port:
          name: https
          number: 443
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: userauth-tls-cert
    ---
    # This ensures the OIDC endpoint has at least some route defined.
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: userauth-oidc
      namespace: asm-user-auth
    spec:
      gateways:
      - userauth
      hosts:
      - '*'
      http:
      - match:
        - uri:
            prefix: /status
        - uri:
            prefix: "your-oidc-redirect-path"
        name: user-auth-route
        route:
        - destination:
            host: authservice
            port:
              number: 10004
    

  1. Label `default` namespace to enable `istio-proxy` auto injection for deployments.
         
         kubectl label namespace default istio.io/rev=REVISION --overwrite
         

  2. Deploy `httpbin` to `default` namespace.
         
         kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/httpbin/httpbin.yaml -n default
         

  3. Update `httpbin` to use this gateway to serve HTTPS traffic, and use port forwarding to access the application locally:
         
         kubectl apply -f./samples/httpbin-route.yaml -n default
         kubectl port-forward service/istio-ingressgateway 8443:443 -n asm-user-auth
         
         
         apiVersion: networking.istio.io/v1alpha3
         kind: VirtualService
         metadata:
           name: httpbin
           namespace: default
         spec:
           gateways:
           - asm-user-auth/userauth
           hosts:
           - '*'
           http:
           - match:
             - uri:
                 prefix: /ip
             - uri:
                 prefix: /headers
             name: httpbin-routes
             route:
             - destination:
                 host: httpbin.default.svc.cluster.local
                 port:
                   number: 8000
         

The ingress gateway on port 8443 will be forwarded to `localhost` to make the application accessible locally.

  4. Deploy the `samples/rctoken-authz.yaml` to enable RequestAuthentication and AuthorizationPolicy to verify the RCToken for the requests.
         
         kubectl apply -f ./samples/rctoken-authz.yaml -n asm-user-auth
         

Example `samples/rctoken-authz.yaml`:
         
         apiVersion: security.istio.io/v1beta1
         kind: RequestAuthentication
         metadata:
           name: require-rc-token
         spec:
           selector:
             matchLabels:
               istio: ingressgateway
           jwtRules:
           - issuer: "authservice.asm-user-auth.svc.cluster.local"
             audiences:
             - "test_audience"
             jwksUri: "http://authservice.asm-user-auth.svc.cluster.local:10004/_gcp_user_auth/jwks"
             fromHeaders:
             - name: X-ASM-RCTOKEN
             forwardOriginalToken: true
         ---
         apiVersion: security.istio.io/v1beta1
         kind: AuthorizationPolicy
         metadata:
           name: require-rc-token
         spec:
           selector:
             matchLabels:
               istio: ingressgateway
           action: ALLOW
           rules:
           - when:
             - key: request.auth.claims[iss]
               values:
               - authservice.asm-user-auth.svc.cluster.local
             - key: request.auth.claims[aud]
               values:
               - test_audience
         




### Verify user authentication

The `httpbin` serves two paths, `/ip` is publicly accessible and `/headers` requires the end user to login via their configured IDP.

**Important:** User would need to trust the self-signed certificate in this case.

  1. Verify that you are able to access `/ip` directly by visiting `https://localhost:8443/ip`.

  2. Verify that you see the OIDC login page by visiting `https://localhost:8443/headers`.

  3. After you login, click **Next** and verify that it redirects you to the `/headers` page.




### Configure authorization policies

After you finish the configuration in the previous steps, each user will be redirected through a web-based authentication flow. When the flow completes, the `authservice` will generate an `RCToken` in JWT format, which it uses to transmit the authenticated user information.

  1. Add Istio authorization policies at the ingress to ensure that an authorization check occurs for each authenticated user:
         
         kubectl apply -f ./samples/httpbin-authz.yaml -n asm-user-auth
         

  2. The `httpbin-authz.yaml` file configures the ingress gateway to validate the RC token issued by authservice, and only authorize when the JWT contains the desired fields, such as audiences and issuers.

See the following example authorization policy:
         
         apiVersion: security.istio.io/v1beta1
         kind: AuthorizationPolicy
         metadata:
           name: require-rc-token
         spec:
           selector:
             matchLabels:
               istio: ingressgateway
           action: ALLOW
           rules:
           - to:
             - operation:
                 paths: ["/ip"]
           - to:
             when:
             - key: request.auth.claims[iss]
               values:
               - authservice.asm-user-auth.svc.cluster.local
             - key: request.auth.claims[aud]
               values:
               - test_audience
             - key: request.auth.claims[sub]
               values:
               - allowed_user_sub_1  # Change this with the "sub" claim in the RC token. Wildcard '*' will match everything.
         




### Configure environment-specific settings

The previous steps use `localhost` and a self-signed HTTPS certificate for quick setup. For real production use, use your own domain, such as `example.com`.

In addition, ensure the `certificateAuthorityData` has the intended root cert content. For example, if the IDP is trusted with system's root certs, you can leave it empty. If there is a HTTPS proxy terminating the HTTPS connection, it should be set to the proxy's root cert.

### Manage and rotate keys

There are two sets of keys used by `authservice`. You can rotate each key independently. However, before you rotate the keys, it is important to understand how the rotation works.

Both keys are in JSON format. The `useAfter` field specifies the timestamp since when the key will be considered to use. During a key rotation, you should include both old and new keys in the JSON. For example, in the following example, `new-key` will only be used after timestamp `1712813735`.
    
    
    {
       "keys":[
          {
             "kty":"RSA",
             "kid":"old-key",
             "K":"...", # k contains a Base64 encoded PEM format RSA signing key.
             "useAfter": 1612813735, # unix timestamp
          }
          {
          "kty":"RSA",
             "kid":"new-key",
             "K":"...", # k contains a Base64 encoded PEM format RSA signing key.
             "useAfter": 1712813735, # unix timestamp
          }
       ]
    }
    

Cloud Service Mesh uses the symmetric key for encrypting session data that is stored in browser cookies. To ensure validity of existing sessions, `authservice` attempts decryption with all keys in the key set. On rotation, the `authservice` will use the new key for encrypting new sessions, and will continue to attempt decryption with the old keys.

The public/private key pair is used to sign `RCToken`. The public key is transmitted to the sidecars by `istiod` for JWT verification. It is crucial for sidecars to receive the new public key before `authservice` starts using the new private key to sign the `RCToken`. To that end, `authservice` starts publishing the public key immediately after the key is added, but waits a significant amount of time before starting to use that to sign `RCToken`.

To summarize, when performing key rotations we recommend:

  1. Perform regular key rotations or on demand as you need.
  2. In the JSON format, include both the current and the new keys. The new keys should be associated with a timestamp in the future. We recommend that you specify a timestamp at least a couple of hours ahead of the current time.
  3. Monitor and confirm that the services are still healthy after the new key is in use. Wait at least one day after the new key is being used before moving to next step.
  4. Remove the old keys from the JSON entries. They are no longer needed.



## Multi Cluster Deployment

Cloud Service Mesh user authentication supports multi cluster deployment. You need to deploy user auth in each cluster as described above. The user auth configuration such as UserAuth custom resource, OIDC client secret, encryption keys, all need to be replicated in each clusters.

By default ingress gateway will load balance the authentication requests to any one of `authservice` instances. You can use destination rule to configure the ingress gateway to send requests to the `authservice` in the same cluster, and only fail over to other clusters' `authservice`.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: DestinationRule
    metadata:
      name: authservice-fail-over
      namespace: asm-user-auth
    spec:
      host: authservice.asm-user-auth.svc.cluster.local
      trafficPolicy:
        loadBalancer:
          localityLbSetting:
            enabled: true
            failover:
            - from:  us-east
              to: us-west
            - from: us-west
              to: us-east
    

Same as other configuration, this needs to be configured in each cluster.

## Custom claims mapping

To configure custom claims mapping, configure `spec.authentication.oidc.attributeMapping` to define any mappings from original identity provider's IDToken. The key will be the claim name in the RCToken and value is a CEL expression on how to parse the claim from IDToken, use `assertion` to reference the IDToken.

Example:
    
    
    spec:
      authentication:
        oidc:
          attributeMapping:
            aud_copy: assertion.aud
            decision: 'assertion.sub.startsWith("123") ? "success" : "fail"'
    

In the RCToken, a nested claim `attributes` contains the claims that been configured:
    
    
    "attributes": {
        "aud_copy": "foo.googleusercontent.com",
        "decision": "success"
    }
    

If the CEL expression fails to parse the value from IDToken, it will ignore the claim without failing the authentication flow.

## User Auth upgrades

  1. Install the user-auth packages again as it contains the updated binary for new user-auth version:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/asm-user-auth.git/@v1.2.5 .
         cd asm-user-auth/
         

  2. Save your OIDC client configuration:
         
         export OIDC_CLIENT_ID=CLIENT_ID
         export OIDC_CLIENT_SECRET=CLIENT_SECRET
         export OIDC_ISSUER_URI=ISSUER_URI
         export OIDC_REDIRECT_HOST=REDIRECT_HOST
         export OIDC_REDIRECT_PATH=REDIRECT_PATH
         

  3. Deploy the user authentication service to upgrade to a new version.




## User authentication configuration details

The following table describes each field in the CRD:

Field name | Description  
---|---  
`authentication.oidc` | This section holds the OIDC endpoint configuration and the parameters used in OIDC flow.  
`authentication.oidc.certificateAuthorityData` | This is the SSL root certificate of the domain of the OIDC authorization server or HTTPS proxy if there is any.   
`authentication.oidc.oauthCredentialsSecret` | Secret references to the Kubernetes Opaque type secret which contains OAuth2 OIDC client_id and client_secret in JSON payload.  
`authentication.oidc.issuerURI` | The URI to use as the issuer in the output RCToken.  
`authentication.oidc.proxy` | Proxy server to the OIDC IDP, if applicable. With format http://user:password@10.10.10.10:8888.  
`authentication.oidc.redirectURIHost` |  The host to be used for OAuth termination URI. If you leave this empty, the host from the target URL will be used and the redirect URI will be assembled dynamically.  
This value can be used when a user auth SSO session is desired at a higher level domain. For example, to enable SSO between profile.example.com/ and admin.example.com/, this value can be set to example.com. It will enable a user auth session to be established at example.com that'll be shared amongst all subdomains. Note: If multiple domains are served from the same mesh, example1.com and example2.com, the feature cannot be used, and is recommended to be left empty.   
`authentication.oidc.redirectURIPath` | The endpoint path where `authservice` will terminate the OAuth flow. You should register this URI path plus the host as an authorized redirect URI in the authorization server for the `authentication.oidc.clientID`.  
In addition, this URI should be served from the same service mesh and ingress where `authservice` is enabled.  
`authentication.oidc.scopes` | The OAuth scope that should be requested in the authentication request. Comma-separated list of identifiers used to specify what access privileges are being requested in addition to "openid" scope, eg. "groups,allatclaim".  
`authentication.oidc.groupsClaim` | If the `idtoken` contains a groups claim, use this field to indicate its name. If specified, the service will pass on the data in this claim into the `groups` claim in the output RCToken. This claim should contain a comma-separated list of strings, eg. ["group1", "group2"].  
`authentication.oidc.attributeMapping` | Contains one or more claim mappings from `idtoken` followed CEL expressions. All claims should be referenced by `assertion.X`, `assertion` is referenced to the original IDToken, for example `aud_copy: assertion.aud`.``  
`authentication.outputJWTAudience` | The audience of the RCToken generated by `authservice`. The sidecars can validate the incoming RCToken against this audience value.  
  
## Troubleshoot

  1. Network accessibility to IDP.

Possible log: `error: TLS handshake failed.`.

Verify by executing `curl` from the ephemeral container attached to the `istio-proxy` to call IDP issuer URI. For example, see [Collecting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-collect-logs#configure_envoy_proxy).

If you're unable to connect, check the firewall rules or other network configurations for the cluster.

  2. Root CA certificate.

Possible log: `error: The server's TLS certificate did not match expectations.` or `error: TLS handshake failed.`.

Make sure the `certificateAuthorityData` holds the correct root CA certificate. When there is no HTTPS proxy terminating HTTPS traffic, this should hold the root CA certificate for the IDP. If there is one, this should hold the proxy's instead.

  3. Redirect path configuration.

Possible observation: receive 404 error page during OIDC authentication flow.

User Auth returns the "Set-Cookie" header without using the path attribute, which by default the browser uses the directory of the request url as the cookie path (scope of the cookie related to path). So we recommend to not include "/" in the redirect path unless you are intended.

  4. The sidecar is not able to fetch jwksUri.

In some scenarios, a [sidecar](https://istio.io/latest/docs/reference/config/networking/sidecar/) restriction could lead to failure of fetching jwksUri. If the namespace is not present using a wildcard (for example, `./*` or `istio-system/*`) then this will not work. You must manually add their namespace in the egress sidecar.




## FAQs

  1. How do I upgrade Cloud Service Mesh with User Auth enabled?

Follow the [Cloud Service Mesh upgrade](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade) process and specify the overlay file by adding `--custom_overlay user-auth-overlay.yaml` on the command line to `asmcli install`.

  2. How much resources should we provision for the `authservice`? And how many requests per second can it handle?

By default, `authservice` is configured with 2.0 vCPU, 256Mi memory. Under such configuration, `authservice` is able to handle 500 requests per second. To handle larger amounts of requests, you should provision [more CPU](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), which is roughly proportionally to its requests handling capacity. You can also configure multiple replicas of the authservice to increase the horizontal scalability.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
