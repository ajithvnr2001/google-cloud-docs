---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/gateway/authorization-policy-sidecar/
title: Setup authorization policies on sidecars on GKE \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:46.564440+00:00
---

# Setup authorization policies on sidecars on GKE  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/gateway/authorization-policy-sidecar/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Setup authorization policies on sidecars on GKE

**Preview — Authorization Policies on Sidecars**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides instructions for setting up different kinds of authorization policies on Cloud Service Mesh sidecars on GKE.

## Before you begin

You should be familiar with [Gateway API](https://docs.cloud.google.com/service-mesh/v1.30/docs/gateway/prepare-gateway) and [Authorization Extensions](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions).

Before you create authorization policy, you must perform the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Network Security, Network Services APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=networksecurity.googleapis.com,networkservices.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Network Security, Network Services APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=networksecurity.googleapis.com,networkservices.googleapis.com)




## Namespace-wide AuthzPolicy

If you want to deny an expected traffic pattern for the whole namespace, configure an authorization policy to deny any incoming HTTP requests to all the workloads in a namespace:
    
    
    cat >ns-authz-policy-deny.yaml <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzPolicy
    metadata:
      name: ns-authz
      namespace: NAMESPACE
    spec:
      targetRefs:
      - kind: Pod
        selector: {}
      rules:
      - to:
          operations:
          - paths:
            - type: Prefix
              value: "/bad_token"
      action: DENY
    EOF
    kubectl apply -f ns-authz-policy-deny.yaml
    

Note that that the empty `selector: {}` targets all Pods in the namespace.

If you want to allow an expected traffic pattern for the whole namespace, configure an authorization policy to allow any incoming HTTP requests to all the workloads in a namespace:
    
    
    cat >ns-authz-policy-allow.yaml <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzPolicy
    metadata:
      name: ns-authz
      namespace: NAMESPACE
    spec:
      targetRefs:
      - kind: Pod
        selector: {}
      rules:
      - to:
          operations:
          - paths:
            - type: Prefix
              value: "/headers"
            methods: ["GET"]
      action: ALLOW
    EOF
    kubectl apply -f ns-authz-policy-allow.yaml
    

Note that that the empty `selector: {}` targets all Pods in the namespace.

## Deny inbound requests to a workload

If you have a workload that is supposed to make only outbound calls, like a cron job, configure an authorization policy to deny any incoming HTTP requests to the workload:
    
    
    cat >deny-path-authz-policy.yaml <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzPolicy
    metadata:
      name: my-workload-authz
      namespace: NAMESPACE
    spec:
     targetRefs:
     - kind: Pod
       selector:
    matchLabels:
          app: EXAMPLE_APP
      rules:
      - to:
          operations:
          - paths:
            - type: Prefix
              value: "/deny_path"
      action: DENY
    EOF
    kubectl apply -f deny-path-authz-policy.yaml
    

The output is similar to:
    
    
    gcpauthzpolicy.networking.gke.io/my-workload-authz created
    

After this policy is applied, any incoming HTTP request to the path /deny_path on the Pods matching app: EXAMPLE_APP will be rejected and the caller will receive an HTTP 403 Forbidden response code.

## Allow specific inbound requests to a workload

You can also configure an `ALLOW` policy that allows only requests that match a specific criteria while rejecting the rest.

The following example configures an authorization policy on the example-app Deployment to allow only mTLS requests from Pods with identity spiffe://cluster.local/namespace/pod1.
    
    
    cat >allow-authz-policy.yaml <<EOF
    apiVersion: networking.gke.io/v1
    kind: GCPAuthzPolicy
    metadata:
      name: my-workload-authz
      namespace: NAMESPACE
    spec:
     targetRefs:
     - kind: Pod
       selector:
    matchLabels:
          app: EXAMPLE_APP
      rules:
      - from:
          sources:
          - principals:
            - principal:
              exact: "spiffe://cluster.local/NAMESPACE/pod1"
      action: ALLOW
    EOF
    kubectl apply -f allow-authz-policy.yaml
    

The output is similar to:
    
    
    gcpauthzpolicy.networking.gke.io/my-workload-authz created
    

Only incoming requests authenticated using mTLS presenting the exact SPIFFE identity spiffe://cluster.local/NAMESPACE/pod1 will receive an HTTP 200 OK. Any other request will be rejected by the proxy with an HTTP 403 Forbidden.

## Delegate to an external authorization engine

You can bring your own authorization engine and configure Cloud Service Mesh to delegate all authorization decisions for a workload to the configured engine.

  1. Install the `GCPAuthzExtension` CRD if it's not already installed:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/main/config/crd/networking.gke.io_gcpauthzextensions.yaml
         

  2. Deploy a callout based authorization extension workload in Kubernetes supporting the `ext_proc gRPC` protocol and configure an authorization extension resource:
         
         cat >authz-extension.yaml <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzExtension
         metadata:
           name: my-authz-ext
           namespace: ns1
         spec:
           backendRef:
             kind: Service
             name: authz-service
           loadBalancingScheme: INTERNAL_SELF_MANAGED
           forwardHeaders:
           - Authorization
           failOpen: false
           timeout: "0.1s"
           wireFormat: EXT_PROC_GRPC
         EOF
         kubectl apply -f authz-extension.yaml
         

This command creates a callout-based authorization extension that runs as a Kubernetes service `authz-service`.

The output is similar to:
         
         gcpauthzextension.networking.gke.io/my-authz-ext created
         

  3. Set up the authorization policy to delegate authorization decisions for the workload to the authorization extension previously configured:
         
         cat >authz-policy.yaml <<EOF
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: my-workload-authz
           namespace: NAMESPACE
         spec:
           targetRefs:
           - kind: Pod
             selector:
               matchLabels:
                 app: EXAMPLE_APP
           rules:
           - from:
               sources:
               - principals:
                 - principal:
                     exact: "spiffe://cluster.local/NAMESPACE/pod1"
             to:
               operations:
               - paths:
                 - type: Exact
                   value: "/api/payments-schedule"
           action: CUSTOM
           customProvider:
             authzExtension:
               targetRefs:
               - kind: GCPAuthzExtension
                 name: my-authz-ext
         EOF
         kubectl apply -f authz-policy.yaml
         

The output is similar to:
         
         gcpauthzpolicy.networking.gke.io/my-workload-authz created
         

The proxy will wait for your custom service to return an `OK` or `DENY` response before forwarding the request to the application or returning an HTTP 403 to the caller. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
