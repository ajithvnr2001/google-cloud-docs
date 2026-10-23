---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking/
title: Prepare GKE ambient networking \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:13.661313+00:00
---

# Prepare GKE ambient networking  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Prepare GKE ambient networking Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

This page shows you how to enable ambient networking on a new or existing cluster, enroll namespaces and workloads to enable ambient traffic redirection, and configure mTLS and authorization policies.

For more information about ambient networking architecture, benefits, and capabilities, see the [Ambient networking overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ambient-overview).

## Prerequisites and limitations

Before setting up ambient networking, review the following feature limitations, version requirements, and scope restrictions:

  * **GKE Version:** Requires GKE version `1.36.4-gke.1391000` or higher.
  * **Regional Support:** Clusters must be created in a region supported by [Regional Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/regional-cloud-service-mesh).
  * **Workload Interoperability:** Workloads enrolled in ambient networking cannot interoperate with sidecar-injected workloads or proxyless gRPC in preview.
  * **Unsupported Features:**
    * Kubernetes Service `trafficDistribution` field.
    * Headless Services.
    * GKE Sandbox (gVisor).
  * **Security Notice:** If the `gke-ambient-nriplugin` component becomes unavailable on a node, inbound traffic authentication and authorization enforcement might be bypassed.



## Before you begin

Complete the following prerequisite setup steps in Google Cloud:

  1. Create or select a project.
  2. Enable the required APIs:
         
         gcloud services enable \
             privateca.googleapis.com \
             gkehub.googleapis.com \
             compute.googleapis.com \
             container.googleapis.com \
             trafficdirector.googleapis.com \
             networkservices.googleapis.com \
             networksecurity.googleapis.com \
             telemetry.googleapis.com \
             monitoring.googleapis.com \
             logging.googleapis.com
         

  3. [Configure managed workload identity authentication for GKE](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke).




## Enable ambient networking on a new cluster

Run the following command to create a new GKE cluster with ambient networking enabled:

  1. Create a GKE cluster with ambient networking enabled
         
         gcloud beta container clusters create CLUSTER_NAME \
             --machine-type=e2-standard-4 \
             --enable-ambient-networking \
             --enable-dataplane-v2 \
             --enable-fleet \
             --gateway-api=standard \
             --location=CLUSTER_LOCATION \
             --release-channel=rapid \
             --workload-pool=PROJECT_ID.svc.id.goog
         

Two DaemonSets now run in the `gke-managed-ambient` namespace.




## Enable ambient networking on an existing cluster

Follow these steps to enable ambient mesh on an existing GKE cluster:

  1. Verify that your cluster meets the following requirements:

     * Version `1.36.4-gke.1391000` or higher.
     * [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) enabled.
     * Machine type must be e2-standard-4 or larger.
     * The cluster must be added to a fleet.
     * The cluster must have the Gateway API and Workload Identity enabled.
  2. Enable ambient networking on an existing cluster:
         
         gcloud beta container clusters update CLUSTER_NAME \
             --enable-ambient-networking \
             --location=CLUSTER_LOCATION \
             --enable-fleet
         

Two DaemonSets now run in the `gke-managed-ambient` namespace.

  3. To verify, point your CLI to the cluster:
         
         gcloud beta container clusters get-credentials CLUSTER_NAME \
             --location=CLUSTER_LOCATION
         

  4. Get the daemonsets in the `gke-managed-ambient` namespace:
         
         kubectl get daemonset -n gke-managed-ambient
         

The output is similar to:
         
         NAME                    DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   AGE
         gke-ambient-nriplugin   9         9         9       9            9           4d1h
         gke-ambient-proxy       9         9         9       9            9           4d1h
         




## Enroll a namespace for ambient networking

Follow these steps to deploy a sample application and enable ambient traffic redirection on its namespace:

  1. Deploy a sample application:
         
         kubectl apply -f - <<EOF
         apiVersion: v1
         kind: Namespace
         metadata:
           name: ambient-test
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: client
           namespace: ambient-test
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: server
           namespace: ambient-test
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: server
           namespace: ambient-test
           labels:
             app: server
         spec:
           ports:
           - port: 80
             protocol: TCP
           selector:
             app: server
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: client
           namespace: ambient-test
           labels:
             app: client
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: client
           template:
             metadata:
               labels:
                 app: client
             spec:
               serviceAccountName: client
               containers:
               - name: nginx
                 image: nginx:1.29.6
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: server
           namespace: ambient-test
           labels:
             app: server
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: server
           template:
             metadata:
               labels:
                 app: server
             spec:
               serviceAccountName: server
               containers:
               - name: nginx
                 image: nginx:1.29.6
                 readinessProbe:
                   httpGet:
                     path: /
                     port: 80
         EOF
         

  2. Label the `ambient-test` namespace to enable traffic redirection through the GKE ambient proxy:
         
         kubectl label namespace ambient-test networking.gke.io/dataplane-mode=ambient
         

  3. Verify that individual Pods in the namespace have been configured for traffic redirection:
         
         kubectl get pods -n ambient-test -o yaml | grep redirection
         

The output is similar to:
         
         ambient.networking.gke.io/redirection: enabled
         ambient.networking.gke.io/redirection: enabled
         

  4. Test the client-to-server traffic:
         
         kubectl exec -it deploy/client -n ambient-test -- \
             /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

  5. To verify that plaintext traffic is flowing through `gke-ambient-proxy`, check the access logs in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and search for the `gke-ambient-node-proxy-accesslog` log name:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  6. Optionally, enable Layer 4 metrics generation for workloads in the namespace:
         
         kubectl label namespace ambient-test networking.gke.io/ambient-network-metrics=enabled
         

Once enabled, workload metrics are available in Cloud Monitoring through [Network Services Monitoring](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview).




## Enable mTLS for a service

After enabling traffic redirection for workloads in a namespace, apply policies to enforce encryption, authentication, and authorization.

  1. Configure a permissive mTLS policy on the server-side workloads:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPServerTLSPolicy
         metadata:
           name: server
           namespace: ambient-test
         spec:
           mtlsMode: Permissive
           targetRefs:
           - group: ""
             kind: Pod
             selector:
               matchLabels:
                 app: server
         EOF
         

This policy makes the Pods accept both mTLS and plaintext traffic. Note that permissive mTLS uses traffic sniffing to detect whether traffic is mTLS or plain text. This will break application traffic that uses its own TLS or a "server speaks first" protocol such as MySQL.

  2. Verify the policy has been accepted by the controller:
         
         kubectl describe gcpservertlspolicies -n ambient-test server | grep -A50 Status
         

The output is similar to:
         
         [...]
         
             Conditions:
             Last Transition Time:  2026-03-25T17:47:30Z
             Message:
             Reason:                Accepted
             Status:                True
             Type:                  Accepted
             Controller Name:         networking.gke.io/dpv2-1n
         Events:
         Type    Reason  Age                   From                   Message
         ----    ------  ----                  ----                   -------
         Normal  Sync    108s (x2 over 2m20s)  sc-dpv2-1n-controller  Sync on Mesh dpv2-1n-fqtx-mesh succeeded
         

Policy propagation can take up to three minutes after controller acceptance. Wait three minutes before proceeding.

  3. Configure a client side mTLS policy that targets the service:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPClientTLSPolicy
         metadata:
           name: server-mtls
           namespace: ambient-test
         spec:
           targetRefs:
           - group: ""
             kind: Service
             name: server
           subjectAltNames:
           - uri: spiffe://PROJECT_ID.svc.id.goog/ns/ambient-test/sa/server
         EOF
         

This policy configures enrolled clients to originate mTLS traffic to the server Service. You might need to wait at least two minutes before proceeding to the next step.

  4. Verify the policy has been accepted by the controller:
         
         kubectl describe gcpclienttlspolicies -n ambient-test server-mtls | grep -A50 Status
         

The output is similar to:
         
         [...]
         Status:
         Conditions:
             Last Transition Time:  2024-10-13T01:15:03Z
             Message:
             Observed Generation:   1
             Reason:                Accepted
             Status:                True
             Type:                  Accepted
         

  5. Test the client-to-server traffic:
         
         kubectl exec -it deploy/client -n ambient-test -- \
             /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

Traffic from Pods enrolled in ambient networking to the server service in the ambient-test namespace should now be using mTLS.

  6. To verify that connections are using mTLS, check the access logs in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and search for the `gke-ambient-node-proxy-accesslog` log name:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  7. Update the existing GCPServerTLSPolicy to change the `mode` from **Permissive** to **Strict** on the server service so that the workload Pods no longer accept plaintext traffic:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPServerTLSPolicy
         metadata:
           name: server
           namespace: ambient-test
         spec:
           mtlsMode: Strict
           targetRefs:
           - group: ""
             kind: Pod
             selector:
               matchLabels:
                 app: server
         EOF
         

  8. Verify the policy has been accepted:
         
         kubectl describe gcpservertlspolicies -n ambient-test server | grep -A50 Status
         

The output is similar to:
         
         Name:         server
         
         <...>
         
         UID:                 e4f2a7a3-69aa-4528-8ea6-6f1bf2142011
         Spec:
         Mtls Mode:  Strict
         Target Refs:
         Group:
         Kind:   Pod
         Selector:
           Match Labels:
             App:  server
         Status:
         Ancestors:
             Ancestor Ref:
             Group:
             Kind:   Pod
             Name:   app=server
             Conditions:
             Last Transition Time:  2026-03-25T22:33:54Z
             Message:
             Reason:                Accepted
             Status:                True
             Type:                  Accepted
             Controller Name:         networking.gke.io/dpv2-1n
         Events:
         Type    Reason  Age                  From                   Message
         ----    ------  ----                 ----                   -------
         Normal  Sync    43s (x5 over 4m57s)  sc-dpv2-1n-controller  Sync on Mesh dpv2-1n-2cdi-mesh succeeded
         

Any plaintext traffic to your server Service will now be rejected.

  9. To verify that plaintext traffic is now being rejected, send traffic to the server service from a client that is NOT enrolled into ambient networking:
         
         kubectl create namespace noambient-test && \
         kubectl run -it -n noambient-test --rm curl --image=nginx -- \
             /bin/curl -fsLSv http://server.ambient-test.svc.cluster.local
         

This connection should fail with a message similar to the following:
         
         * Request completely sent off
         * Empty reply from server
         * shutting down connection #0
         curl: (52) Empty reply from server
         




## Set Layer 4 authorization policy

To enforce identity-based authorization, workload owners specify Pod labels in the policy selector. Namespace owners apply policies namespace-wide without selectors.

  1. Apply the following policy to enforce that only the client is allowed to talk to the server:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: allow-client
           namespace: ambient-test
         spec:
           action: ALLOW
           enforcementLevel: L4
           targetRefs:
           - group: ""
             kind: Pod
             selector:
               matchLabels:
                 app: server
           rules:
           - from:
               sources:
               - principals:
                 - principalSelector: CLIENT_CERT_URI_SAN
                   principal:
                     type: Exact
                     value: spiffe://PROJECT_ID.svc.id.goog/ns/ambient-test/sa/client
         EOF
         

This policy is enforced on traffic to server Pods in the `ambient-test` namespace. It ensures that traffic is only allowed from sources with SPIFFE identity spiffe://PROJECT_ID.svc.id.goog/ns/ambient-test/sa/client.

  2. Verify policy enforcement is **allowed** by sending a sample request from the **client** service account.
         
         kubectl exec -it deploy/client -n ambient-test -- \
             /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

  3. Verify policy enforcement is **not allowed** by sending a sample request from the **server** service account.
         
         kubectl exec -it deploy/server -n ambient-test -- \
             /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

The output is similar to:
         
         curl: (52) Empty reply from server
         command terminated with exit code 52
         

  4. You can use Logs Explorer to see the authorization enforcement logging. In the Google Cloud console, go to the **Logs Explorer** page and search for denied requests using the `gke-ambient-node-proxy-accesslog` log name:
         
         resource.type="k8s_container"
         logName="projects/PROJECT_ID/logs/gke-ambient-node-proxy-accesslog"
         jsonPayload.error_details=~"rbac_access_denied"
         

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
