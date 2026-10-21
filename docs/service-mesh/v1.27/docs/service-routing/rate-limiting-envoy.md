---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/rate-limiting-envoy/
title: Configure Google Cloud Armor rate limiting with Envoy \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:50.068085+00:00
---

# Configure Google Cloud Armor rate limiting with Envoy  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/rate-limiting-envoy/

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

# Configure Google Cloud Armor rate limiting with Envoy

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to configure global server-side rate limiting for your service mesh by using Cloud Armor. You can use this feature to apply fairshare rate limiting to all traffic arriving to your service, helping you to fairly share the available capacity of your services and mitigate the risk of malicious or misbehaving clients from overloading your services. For more information about rate limiting, read the [rate limiting overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/rate-limiting-overview).

## Configure Google Kubernetes Engine (GKE) for Envoy

### Before you begin

Before you begin, you must enable the following APIs:

  * `container.googleapis.com`
  * `compute.googleapis.com`
  * `trafficdirector.googleapis.com`
  * `networkservices.googleapis.com`
  * `meshconfig.googleapis.com`
  * `monitoring.googleapis.com`



You can enable all of the APIs by using the following Google Cloud CLI command:
    
    
    gcloud services enable \
        container.googleapis.com \
        compute.googleapis.com \
        trafficdirector.googleapis.com \
        networkservices.googleapis.com \
        meshconfig.googleapis.com \
        monitoring.googleapis.com
    

Then, create the environment variables that are used in this document:
    
    
    export PROJECT_ID=PROJECT_ID
    export PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")"
    export CLUSTER=CLUSTER
    export ZONE=ZONE
    export MESH_NAME=MESH_NAME
    export MESH_URI=projects/${PROJECT_NUMBER}/locations/global/meshes/${MESH_NAME}
    

Replace the following variables with information from your project:

  * Replace `PROJECT_ID` with your project ID
  * Replace `ZONE` with the zone in which you intend to create your GKE cluster
  * Replace `CLUSTER` with the name of the cluster
  * Replace `MESH_NAME` with the name of the mesh



### Create a GKE cluster

  1. Use the following command to create a GKE cluster in the zone that you specified in the previous section:
         
         gcloud container clusters create "CLUSTER" \
              --zone="ZONE" \
              --scopes="cloud-platform" \
              --tags="allow-envoy-health-checks" \
              --enable-ip-alias
         

  2. Get the credentials of your new cluster:
         
         gcloud container clusters get-credentials "CLUSTER" \
              --zone="ZONE"
         




### Enable automatic injection

  1. Use the following command to apply the `MutatingWebhookConfiguration` resource to your cluster. When a Pod is created, the in-cluster admission controller is invoked, and it instructs the managed sidecar injector to add the Envoy container to the Pod.
         
         cat <<EOF | kubectl apply -f -
         apiVersion: admissionregistration.k8s.io/v1
         kind: MutatingWebhookConfiguration
         metadata:
          labels:
            app: sidecar-injector
          name: td-mutating-webhook
         webhooks:
         - admissionReviewVersions:
           - v1beta1
           - v1
           clientConfig:
             url: https://meshconfig.googleapis.com/v1internal/projects/PROJECT_ID/locations/ZONE/clusters/CLUSTER/channels/rapid/targets/${MESH_URI}:tdInject
           failurePolicy: Fail
           matchPolicy: Exact
           name: namespace.sidecar-injector.csm.io
           namespaceSelector:
             matchExpressions:
             - key: td-injection
               operator: Exists
           reinvocationPolicy: Never
           rules:
           - apiGroups:
             - ""
             apiVersions:
             - v1
             operations:
             - CREATE
             resources:
             - pods
             scope: '*'
           sideEffects: None
           timeoutSeconds: 30
         EOF
         

  2. Enable sidecar injection for the default namespace. The sidecar injector injects sidecar containers for pods created under the default namespace.
         
         kubectl label namespace default td-injection=enabled
         

  3. Save the following GKE config for your service as `service_sample.yaml`.

**Note:** This YAML file uses annotations. When the pod is initialized, the sidecar proxy picks up the annotations and transmits them to the Cloud Service Mesh. Cloud Service Mesh then uses this information to send back a filtered configuration. The value of `IncludeInboundPorts` is the port on which your server application listens for connection. `cloud.google.com/sidecarProxyVersion` specifies the Envoy image version. `1.34.1-gke.1` is the only Envoy version that supports rate limiting.
         
         apiVersion: v1
         kind: Service
         metadata:
          name: service-test
          annotations:
            cloud.google.com/neg: '{"exposed_ports":{"80":{"name": "rate-limit-demo-neg"}}}'
         spec:
          ports:
          - port: 80
            name: service-test
            targetPort: 8000
          selector:
            run: app1
          type: ClusterIP
         
         ---
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: app1
          labels:
            run: app1
         spec:
          replicas: 1
          selector:
            matchLabels:
              run: app1
          template:
            metadata:
              labels:
                run: app1
              annotations:
                cloud.google.com/proxyMetadata: '{"app": "rate-limit-demo"}'
                cloud.google.com/includeInboundPorts: "8000"
                cloud.google.com/sidecarProxyVersion: "1.34.1-gke.1"
            spec:
              containers:
              - image: mendhak/http-https-echo:37
                name: app1
                ports:
                - containerPort: 8000
                env:
                - name: VALIDATION_NONCE
                  value: "http"
                - name: HTTP_PORT
                  value: "8000"
              securityContext:
                fsGroup: 1337
         

  4. Apply the service sample that you created in the previous step:
         
         kubectl apply -f service_sample.yaml
         

  5. Save the following GKE config for your client as `client_sample.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          labels:
            run: client
          name: load-generator
         spec:
          replicas: 1
          selector:
            matchLabels:
              run: client
          template:
            metadata:
              labels:
                run: client
            spec:
              containers:
              - name: load-generator
                image: envoyproxy/nighthawk-dev
                command: ["/bin/sh", "-c"]
                args: ["echo 'Nighthawk client pod is running' && sleep infinity"]
                resources:
                  requests:
                    cpu: 200m
                    memory: 256Mi
                  limits:
                    cpu: 1
                    memory: 512Mi
              securityContext:
                fsGroup: 1337
         

  6. Apply the client sample that you created in the previous step:
         
         kubectl apply -f client_sample.yaml
         




## Set up Cloud Service Mesh for rate limiting

Use the steps in this section to prepare Cloud Service Mesh for rate limiting.

  1. Create the `Mesh` resource specification and save it in a file called `mesh.yaml`:
         
         name: MESH_NAME
         interceptionPort: 15001
         

  2. Create the `Mesh` resource using the mesh.yaml specification.
         
         gcloud network-services meshes import "MESH_NAME" \
               --source=mesh.yaml \
               --location=global
         

  3. Create a health check:
         
         gcloud compute health-checks create http rate-limit-demo-hc \
               --use-serving-port
         

  4. Create a firewall rule to allow incoming health check connections to instances in your network.
         
         gcloud compute firewall-rules create rate-limit-demo-fw-allow-hc \
               --action ALLOW \
               --direction INGRESS \
               --source-ranges 35.191.0.0/16,130.211.0.0/22 \
               --target-tags allow-envoy-health-checks \
               --rules tcp
         

  5. Create a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and add the health check.
         
         gcloud compute backend-services create rate-limit-demo-service \
               --global \
               --health-checks rate-limit-demo-hc \
               --load-balancing-scheme INTERNAL_SELF_MANAGED
         

  6. Add the NEG `rate-limit-demo-neg` to the backend service.
         
         gcloud compute backend-services add-backend rate-limit-demo-service \
               --global \
               --network-endpoint-group rate-limit-demo-neg \
               --network-endpoint-group-zone "ZONE" \
               --balancing-mode RATE \
               --max-rate-per-endpoint 5
         

  7. Create the `HTTPRoute` specification and save it to a file called `http_route.yaml`:
         
         name: rate-limit-demo-http-route
         hostnames:
         - service-test
         - service-test:80
         meshes:
         - projects/PROJECT_ID/locations/global/meshes/MESH_NAME
         rules:
         - action:
            destinations:
            - serviceName: "projects/PROJECT_ID/locations/global/backendServices/rate-limit-demo-service"
         

  8. Create the `HTTPRoute` resource using the specification in the `http_route.yaml` file.
         
         gcloud network-services http-routes import rate-limit-demo-http-route \
               --source=http_route.yaml \
               --location=global
         




## Configure rate limiting with Envoy

**Note:** When you configure global server-side rate limiting for your service mesh using Cloud Armor, the allowed `deny` status codes are `403`, `404`, `429`, and `502`. If you use any other status code, it defaults to `429`.

The following sections explain how to configure server-side rate limiting for your service mesh. The first section shows you how to set up one server-side global rate limit for all clients, and the second section shows you how to enforce different rate limits for different groups of clients.

### Configure server-side global rate limiting

In this example, you create one server-side rate limiting rule that enforces rate limiting on all clients.

  1. In a YAML file called `rate-limit-policy.yaml`, create a Cloud Armor security policy with the type `CLOUD_ARMOR_INTERNAL_SERVICE`.
         
         name: "rate-limit-policy"
         type: CLOUD_ARMOR_INTERNAL_SERVICE
         rules:
         - priority: 2147483647
           match:
             config:
               srcIpRanges: ["*"]
             versionedExpr: SRC_IPS_V1
           action: "fairshare"
           rateLimitOptions:
             rateLimitThreshold:
               count: 10000
               intervalSec: 60
             exceedAction: "deny(429)"
             conformAction: "allow"
             enforceOnKey: "ALL"
         

  2. Create the security policy called `rate-limit-policy`:
         
         gcloud beta compute security-policies create rate-limit-policy \
               --global \
               --file-name=rate-limit-policy.yaml
         

  3. In a YAML file, create an endpoint policy that references the security policy that you created in the previous step. In these examples, this file is called `endpoints-policies.yaml`.
         
         name: "rate-limit-ep"
         endpointMatcher:
          metadataLabelMatcher:
            metadataLabelMatchCriteria: MATCH_ALL
            metadataLabels:
            - labelName: app
              labelValue: rate-limit-demo
         type: SIDECAR_PROXY
         securityPolicy: projects/PROJECT_ID/locations/global/securityPolicies/rate-limit-policy
         

  4. Create an endpoint policy named `rate-limit-ep`:
         
         gcloud beta network-services endpoint-policies import rate-limit-ep \
               --source=endpoints-policies.yaml \
               --location=global
         




### Configure different server-side rate limits for different groups of clients

In this example, you create different server-side rate limiting rules that enforce different rate limiting thresholds for groups of clients.

  1. Create a Cloud Armor security policy with the type `CLOUD_ARMOR_INTERNAL_SERVICE` with multiple rate limiting rules, like the one defined in the following file. In these examples, this file is called `per-client-security-policy.yaml`.
         
         name: "per-client-security-policy"
         type: CLOUD_ARMOR_INTERNAL_SERVICE
         rules:
         - priority: 0
           match:
             expr:
               expression: "request.headers['user'] == 'demo'"
           action: "fairshare"
           rateLimitOptions:
             rateLimitThreshold:
               count: 1000
               intervalSec: 60
             exceedAction: "deny(429)"
             conformAction: "allow"
             enforceOnKey: "ALL"
         - priority: 2147483647
           match:
             config:
               srcIpRanges: ["*"]
             versionedExpr: SRC_IPS_V1
           action: "fairshare"
           rateLimitOptions:
             rateLimitThreshold:
               count: 10000
               intervalSec: 60
             exceedAction: "deny(429)"
             conformAction: "allow"
             enforceOnKey: "ALL"
         

This policy applies rate limiting to requests containing an HTTP header with the name `user` and value `demo` if Cloud Service Mesh receives more than 1,000 such requests within a 60 second window. Requests that don't have this HTTP header are instead rate limited if Cloud Service Mesh receives more than 10,000 such requests within a 60 second window.

  2. Use the following command to create the policy, which is called `per-client-security-policy`:
         
         gcloud beta compute security-policies create per-client-security-policy \
               --global \
               --file-name=per-client-security-policy.yaml
         

Create an endpoint policy that references the security policy that you created in the previous step, like the one defined in the following file. In this example, this file is called `per-client-endpoints-policies.yaml`.
         
         name: "rate-limit-ep"
         endpointMatcher:
          metadataLabelMatcher:
            metadataLabelMatchCriteria: MATCH_ALL
            metadataLabels:
            - labelName: app
              labelValue: rate-limit-demo
         type: SIDECAR_PROXY
         securityPolicy: projects/PROJECT_ID/locations/global/securityPolicies/per-client-security-policy
         

Use the following command to create an endpoint policy named `rate-limit-ep`:
         
         gcloud beta network-services endpoint-policies import rate-limit-ep \
               --source=per-client-endpoints-policies.yaml \
               --location=global
         




## Validate your setup

You can use the [Nighthawk](https://github.com/envoyproxy/nighthawk) load testing tool to generate traffic to test whether your rate limiting rules are performing as you expect. Use the following command to generate traffic with Nighthawk:
    
    
    kubectl exec -it deploy/load-generator -c load-generator -- \
        nighthawk_client http://service-test \
        --open-loop --no-default-failure-predicates \
        --rps 60 \
        --duration 360 \
        --connections 10 \
        --protocol http1 \
        --request-header user:demo
    

Next, use the following command to enable Envoy debug logs:
    
    
    kubectl exec -it deploy/app1 -c app1 -- wget -q -O - \
        --post-data="" 'http://localhost:15000/logging?level=debug'
    

To view the usage reports Envoy sends to the management server, see [Accessing your logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#accessing_your_logs).

You can expect to see the following from your test results:

  * It takes roughly five minutes before rate limiting takes effect.
  * After the initial warm up period, you see about 15-21 QPS from the Nighthawk client output `benchmark.http_2xx` counter. This means that Cloud Armor allows about 1,000 requests per minute.



To view the effectiveness of your Cloud Armor security policy rules, see [Viewing the monitoring dashboard](https://docs.cloud.google.com/armor/docs/monitoring#viewing_the_monitoring_dashboard).

## Disable rate limiting

You can disable rate limiting by using either of the following methods:

  * You can delete the endpoint policies and security policies that you configured with your rate limiting rules.
  * You can detach the security policy from your endpoint policy by updating your endpoint policy to remove the `securityPolicies` field.



The following sections tell you how to disable rate limiting using each method.

### Delete an endpoint policy and a security policy

First, use the following `gcloud` command to delete your endpoint policy named `rate-limit-ep`. If you used the name provided in the first or second example on this page, the endpoint policy is named `endpoints-policies` or `per-client-endpoints-policies` respectively.
    
    
    gcloud beta network-services endpoint-policies delete --location=global rate-limit-ep
    

Then, use the following `gcloud` command to delete a security policy, replacing `per-client-security-policy` with the name of your security policy. If you used the name provided in the first or second example on this page, then your security policy has the same name as your endpoint policy.
    
    
    gcloud beta compute security-policies delete --global per-client-security-policy
    

### Detach a security policy from your endpoint policy

First, update your `endpoint-policy.yaml` file to remove the `securityPolcies` field:
    
    
    name: "rate-limit-ep"
    endpointMatcher:
      metadataLabelMatcher:
        metadataLabelMatchCriteria: MATCH_ALL
        metadataLabels:
        - labelName: app
          labelValue: rate-limit-demo
    type: SIDECAR_PROXY
    

Then, use the following command to update the endpoint policy named `rate-limit-ep` with the changes to the `endpoint-policy.yaml` file:
    
    
    gcloud beta network-services endpoint-policies import rate-limit-ep \
        --source=endpoints-policies.yaml \
        --location=global
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
