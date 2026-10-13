---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/tutorials/authz/
title: Cloud Service Mesh by example: Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:40.499748+00:00
---

# Cloud Service Mesh by example: Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/tutorials/authz/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback 

#  Cloud Service Mesh by example: Authorization Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

In this tutorial, you will learn what authorization is, and how to enable it with Cloud Service Mesh on a sample application to learn how to enable authorization policies to your microservices. You will create an `AuthorizationPolicy` to `DENY` access to a microservice, then create an `AuthorizationPolicy` to `ALLOW` specific access to a microservice.

### What is authorization?

Authentication verifies an identity -- is this service who they say they are? Authorization verifies the permission - is this service allowed to do that? Identity is fundamental to this idea. With Cloud Service Mesh, `AuthorizationPolicies` allow for workload-to-workload communication in your mesh to be controlled for improved security and access.

In a microservice architecture, where calls are made across network boundaries, IP-based firewall rules are often not adequate to secure access between workloads. With Cloud Service Mesh, you can set authorization rules to:

  * Control access to workloads within your mesh, either workload-to-workload or end-user-to-workload
  * Broadly or granularly define policies depending on your needs.



To see an in-depth explanation on configuring policies and best practices, see [Authorization with Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/security/authorization-policy-overview).

## Costs

This tutorial uses the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/pricing)



When you finish this tutorial, you can avoid ongoing costs by deleting the resources you created. For more information, see Clean up.

## Before you begin

  * Ensure [billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project).

  * Provision Cloud Service Mesh on a GKE cluster. There are various supported setup methods:

    * [Fleet API and a managed control plane on Google Cloud](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane)

    * [`asmcli` and an unmanaged, in-cluster control plane off Google Cloud](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh)

  * Clone the repo:
        
        git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples
        cd anthos-service-mesh-samples
        




## Deploy an ingress gateway

  1. Set the current context for `kubectl` to the cluster:

**Note:** Use `--region` instead of `--zone`, if the cluster is a regional cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME  \
         --project=PROJECT_ID \
         --zone=CLUSTER_LOCATION 
         

  2. Create a namespace for your ingress gateway:
         
         kubectl create namespace asm-ingress
         

  3. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation).

### Managed (TD)

Apply the default injection label to the namespace:
         
         kubectl label namespace asm-ingress \
             istio.io/rev- istio-injection=enabled --overwrite
         

### Managed (Istiod)

**Recommended:** Run the following command to apply the default injection label to the namespace:
         
         kubectl label namespace asm-ingress \
               istio.io/rev- istio-injection=enabled --overwrite
         

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

**Note:** If two control plane revisions appear in the earlier list, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            kubectl label namespace asm-ingress \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

### In-cluster

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace asm-ingress \
          istio.io/rev- istio-injection=enabled --overwrite
    

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
               jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace asm-ingress \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  4. Deploy the example gateway in the `anthos-service-mesh-samples` repo:
         
         kubectl apply -n asm-ingress \
         -f docs/shared/asm-ingress-gateway
         

Expected output:
         
         serviceaccount/asm-ingressgateway configured
         service/asm-ingressgateway configured
         deployment.apps/asm-ingressgateway configured
         gateway.networking.istio.io/asm-ingressgateway configured
         




## Deploy the Online Boutique sample application

  1. If you haven't, set the current context for `kubectl` to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME  \
         --project=PROJECT_ID \
         --zone=CLUSTER_LOCATION 
         

  2. Create the namespace for the sample application:
         
         kubectl create namespace onlineboutique
         

  3. Label the `onlineboutique` namespace to automatically inject Envoy proxies. Follow the steps [to enable automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/anthos-service-mesh-proxy-injection).

  4. Deploy the sample app, the `VirtualService` for the frontend, and service accounts for the workloads. For this tutorial, you will deploy [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo), a microservice demo app.
         
         kubectl apply \
         -n onlineboutique \
         -f docs/shared/online-boutique/virtual-service.yaml
         kubectl apply \
         -n onlineboutique \
         -f docs/shared/online-boutique/service-accounts
         




### View your services

  1. View the pods in the `onlineboutique` namespace:
         
         kubectl get pods -n onlineboutique
         

Expected output:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         adservice-85598d856b-m84m6               2/2     Running   0          2m7s
         cartservice-c77f6b866-m67vd              2/2     Running   0          2m8s
         checkoutservice-654c47f4b6-hqtqr         2/2     Running   0          2m10s
         currencyservice-59bc889674-jhk8z         2/2     Running   0          2m8s
         emailservice-5b9fff7cb8-8nqwz            2/2     Running   0          2m10s
         frontend-77b88cc7cb-mr4rp                2/2     Running   0          2m9s
         loadgenerator-6958f5bc8b-55q7w           2/2     Running   0          2m8s
         paymentservice-68dd9755bb-2jmb7          2/2     Running   0          2m9s
         productcatalogservice-84f95c95ff-c5kl6   2/2     Running   0          114s
         recommendationservice-64dc9dfbc8-xfs2t   2/2     Running   0          2m9s
         redis-cart-5b569cd47-cc2qd               2/2     Running   0          2m7s
         shippingservice-5488d5b6cb-lfhtt         2/2     Running   0          2m7s
         

All of the pods for your application should be up and running, with a `2/2` in the `READY` column. This indicates that the pods have an Envoy sidecar proxy injected successfully. If it does not show `2/2` after a couple of minutes, visit the [Troubleshooting guide](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-resources).

  2. Get the external IP, and set it to a variable:
         
         kubectl get services -n asm-ingress
         export FRONTEND_IP=$(kubectl --namespace asm-ingress \
         get service --output jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}' \
         )
         

You see output similar to the following:
         
         NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                      AGE
         asm-ingressgateway   LoadBalancer   10.19.247.233   35.239.7.64   80:31380/TCP,443:31390/TCP,31400:31400/TCP   27m
         
         

  3. Visit the `EXTERNAL-IP` address in your web browser. You should expect to see the Online Boutique shop in your browser.

![online boutique frontend](https://docs.cloud.google.com/static/service-mesh/docs/images/online-boutique.jpeg)




## DenyAll Authorization for a workload

This section adds an `AuthorizationPolicy` to deny all incoming traffic to the currency service. `AuthorizationPolicies` work by transforming `AuthorizationPolicies` into Envoy-readable configs, and applying the configs to your sidecar proxies. This enables the Envoy proxy to authorize or deny incoming requests to a service.

  1. Apply an `AuthorizationPolicy` to the `currencyservice`. Notice the match on the label `currencyservice` in the YAML file.
         
         kubectl apply -f docs/authorization/currency-deny-all.yaml -n onlineboutique
         
         
         apiVersion: security.istio.io/v1beta1
         kind: AuthorizationPolicy
         metadata:
           name: currency-policy
         spec:
           selector:
             matchLabels:
               app: currencyservice

  2. Try accessing your gateway's `EXTERNAL-IP` to view Online Boutique in the web browser. You should see an authorization error (500 Internal Service Error) from `currency service`.

![authz rbac 500 error](https://docs.cloud.google.com/static/service-mesh/docs/images/authz-rbac-currencyservice-error-500.png)




### Observe your sidecar proxy logs

To see what is occurring in the sidecar proxy, you can review the logs in the pod.

  1. Get the name of your `currencyservice` pod:
         
         CURRENCY_POD=$(kubectl get pod -n onlineboutique |grep currency|awk '{print $1}')
         

  2. Set the Envoy proxy to allow for trace level logs. By default, blocked authorization calls are not logged:
         
         kubectl debug --image istio/base --target istio-proxy -it $CURRENCY_POD -n onlineboutique -- curl -X POST "http://localhost:15000/logging?level=trace"
         

Expected output: `none {:.devsite-disable-click-to-copy} active loggers: admin: trace alternate_protocols_cache: trace ... tracing: trace upstream: trace udp: trace wasm: trace`

  3. Use `curl` to send traffic to your `EXTERNAL_IP` to generate logs:
         
         for i in {0..10}; do
         curl -s -I $FRONTEND_IP ; done
         

  4. View the role-based access control (RBAC) related logs in your istio-proxy:
         
         kubectl logs -n onlineboutique $CURRENCY_POD -c istio-proxy | grep -m5 rbac
         

Expected output:
         
         2022-07-08T14:19:20.442920Z     debug   envoy rbac      checking request: requestedServerName: outbound_.7000_._.currencyservice.onlineboutique.svc.cluster.local, sourceIP: 10.8.8.5:34080, directRemoteIP: 10.8.8.5:34080, remoteIP: 10.8.8.5:34080,localAddress: 10.8.0.6:7000, ssl: uriSanPeerCertificate: spiffe://christineskim-tf-asm.svc.id.goog/ns/onlineboutique/sa/default, dnsSanPeerCertificate: , subjectPeerCertificate: OU=istio_v1_cloud_workload,O=Google LLC,L=Mountain View,ST=California,C=US, headers: ':method', 'POST'
         2022-07-08T14:19:20.442944Z     debug   envoy rbac      enforced denied, matched policy none
         2022-07-08T14:19:20.442965Z     debug   envoy http      [C73987][S13078781800499437460] Sending local reply with details rbac_access_denied_matched_policy[none]
           ```
         




You should see an `enforced denied` message in the logs, showing that `currencyservice` is set to block inbound requests.

## Allow Restricted Access

Instead of a `DENYALL` policy, you can set access to be allowed for certain workloads. This will be relevant in a microservice architecture where you want to ensure that only authorized services can communicate with each other.

In this section, you will enable the `frontend` and `checkout` service the ability to communicate with the `currency` service.

  1. In the following file, see that a specific `source.principal`(client) is allowed to access `currencyservice`:


    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: currency-policy
    spec:
      selector:
        matchLabels:
          app: currencyservice
      rules:
      - from:
        - source:
            principals: ["cluster.local/ns/onlineboutique/sa/frontend"]
      - from:
        - source:
            principals: ["cluster.local/ns/onlineboutique/sa/checkoutservice"]

  1. Apply the policy:
         
         kubectl apply -f docs/authorization/currency-allow-frontend-checkout.yaml -n onlineboutique
         

  2. Visit the `EXTERNAL-IP` in your web browser, you should now be able to access Online Boutique.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To avoid incurring continuing charges to your Google Cloud account for the resources used in this tutorial, you can either delete the project or delete the individual resources.

### Delete the project

**Caution:** Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an appspot.com URL, delete selected resources inside the project instead of deleting the whole project.



In Cloud Shell, delete the project:
    
    
    gcloud projects delete PROJECT_ID
    

### Delete the resources

  * If you want to keep your cluster and remove the Online Boutique sample:

    1. Delete the application namespaces:
           
           kubectl delete namespace onlineboutique
           

Expected output:
           
           namespace "onlineboutique" deleted
           

    2. Delete the Ingress Gateway namespace:
           
           kubectl delete namespace asm-ingress
           

Expected output:
           
           amespace "asm-ingress" deleted
           

  * If you want to prevent additional charges, delete the cluster:
        
        gcloud container clusters delete  CLUSTER_NAME  \
        --project=PROJECT_ID \
        --zone=CLUSTER_LOCATION 
        




## What's next

  * For a general guide on configuring `PeerAuthentication` policies, see [Configuring transport security](https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls).
  * Explore your mesh's security dashboard with [Monitor mesh security](https://docs.cloud.google.com/service-mesh/docs/observability/monitor-mesh-security).
  * Deep dive with authorization policies with [Configure authorization policy advanced features](https://docs.cloud.google.com/service-mesh/docs/security/authorization-advanced-features).
  * Familiarize yourself with [Cloud Service Mesh security best practices](https://docs.cloud.google.com/service-mesh/docs/security/cloud-service-mesh-security-best-practices). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
