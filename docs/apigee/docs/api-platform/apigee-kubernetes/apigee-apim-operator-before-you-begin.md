---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-before-you-begin/
title: Apigee Operator for Kubernetes: Before you begin \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:50.860613+00:00
---

# Apigee Operator for Kubernetes: Before you begin  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Operator for Kubernetes: Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes the steps you must complete before you install and configure the Apigee Operator for Kubernetes. To learn more about the benefits of using the Apigee Operator for Kubernetes, see [ Apigee Operator for Kubernetes overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install).

## Required roles

To get the permissions that you need to set up the resources required to install and use the Apigee Operator for Kubernetes, ask your administrator to grant you the following IAM roles on the organization: 

  * Create and manage the Google Kubernetes Engine (GKE) cluster: [Container Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 
  * Create and manage service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) 
  * Create and manage service extensions: [Service Extensions Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.serviceExtensionsAdmin) (`roles/networkservices.serviceExtensionsAdmin`) 
  * Create and manage network endpoint groups (NEGs): [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) 
  * Create and manage backend services: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) 
  * Create and manage Apigee resources: [Apigee Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Required set up tasks

Before you install the Apigee Operator for Kubernetes, complete the following tasks to set up the resources you need to use the feature: 

  1. **Provision an[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) instance using version `1-15-0-apigee-4` or later.**

You can view instance versions in the **Instance details** page of the Apigee UI in Google Cloud console. Go to the **Instances** page in the Google Cloud console to select an instance and view its details: 

[Go to Instances](https://console.cloud.google.com/apigee/instances)

You can use Apigee Operator for Kubernetes with a [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) or [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-entitlements) Apigee organization. For more details about provisioning paid Apigee instances, see [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview).

  2. **Install the[Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).**

After you install the Google Cloud CLI, run the `gcloud components update` command to get the latest gcloud components.

  3. **Install and configure the[`kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl) command-line tool.**
  4. **Install[Helm](https://helm.sh/) (version v3.14.3 or later).**
  5. **Create a GKE cluster using GKE version 1.27 or later with[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) enabled.**

If you have an existing cluster that meets these requirements, you can skip this step.

Workload Identity Federation for GKE is enabled by default when you use Autopilot mode to create and manage your clusters. For more information, see [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

For the steps required to create a new cluster with Workload Identity Federation for GKE and GKE Gateway enabled using Autopilot, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).

**Note:** If you use Standard mode to create and manage your clusters, you must manually enable Workload Identity Federation for GKE and GKE Gateway. For more information, see [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  6. **Deploy a GKE Gateway to your cluster.**

You can choose to configure and deploy an [ internal Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#internal-gateway) or an [external Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#external-gateway) to use with Apigee Operator for Kubernetes. If you choose to deploy an internal Gateway, a proxy-only subnet and shared VPC are required. For testing the steps in this guide, we recommend that you deploy an external Gateway. For more information, see [GKE Gateway controller requirements](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#requirements). **Note:** If you plan to deploy more than one GKE Gateway in the same region, both Gateways must be of the same type (internal or external). You can't deploy an internal Gateway and an external Gateway in the same region. The example configurations in this guide use an external Gateway.

To deploy the GKE Gateway, use the steps outlined in [Deploy an external Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#external-gateway). When you [create the Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#external-gateway), use the following `yaml` configuration: 
         
         # gateway.yaml
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: global-ext-lb1
           namespace: default
         spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
             - name: http
               protocol: HTTP
               allowedRoutes:
                 kinds:
                   - kind: HTTPRoute
                 namespaces:
                   from: All
               port: 80

Apply the file to your cluster: 
         
         kubectl apply -f gateway.yaml

  7. **Deploy a backend application to your cluster**. 

To deploy the backend application exposed by the `global-ext-lb1` Gateway you created and deployed: 

     1. Create a new file named `target.yaml`.
     2. Copy the following content into the new file: 
            
            # target.yaml
            apiVersion: v1
            kind: Namespace
            metadata:
              name: http
            ---
            apiVersion: v1
            kind: ServiceAccount
            metadata:
              name: httpbin
              namespace: http
            ---
            apiVersion: v1
            kind: Service
            metadata:
              name: httpbin
              namespace: http
              labels:
                app: httpbin
                service: httpbin
            spec:
              type: LoadBalancer
              ports:
                - name: https
                  port: 80
                  targetPort: 80
              selector:
                app: httpbin
            ---
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: httpbin
              namespace: http
            spec:
              replicas: 1
              selector:
                matchLabels:
                  app: httpbin
                  version: v1
              template:
                metadata:
                  labels:
                    app: httpbin
                    version: v1
                spec:
                  serviceAccountName: httpbin
                  containers:
                    - image: docker.io/kennethreitz/httpbin
                      imagePullPolicy: IfNotPresent
                      name: httpbin
                      ports:
                        - containerPort: 80
                      resources:
                        requests:
                          cpu: 1
                          memory: 1024Mi
                        limits:
                          cpu: 1
                          memory: 1024Mi

     3. Apply the configuration to your cluster: 
            
            kubectl apply -f target.yaml

For more information on deploying backend applications to GKE clusters, see [Deploy the demo applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#deploy_the_demo_applications_2).

  8. **Deploy the HTTPRoute resource to your cluster to map traffic from the Gateway to your backend service.**

For more information on the HTTPRoute resource, see [Deploy the HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#store-route) (for internal Gateways) or [Create an HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#create_an_httproute) (for external Gateways).

For the purposes of this guide, we recommend that you deploy an external Gateway and HTTPRoute, following the steps in [Create an HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#create_an_httproute). When you [create the HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#create_an_httproute), use the following `yaml` configuration, substituting `HOST_NAME` with the hostname you want to use: 
         
         # httproute.yaml
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: http-bin-route
           namespace: http
         spec:
           parentRefs:
             - kind: Gateway
               name: global-ext-lb1
               namespace: default
           hostnames:
             - HOST_NAME
           rules:
             - matches:
                 - path:
                     value: /
               backendRefs:
                 - name: httpbin
                   kind: Service
                   port: 80
                   namespace: http

Apply the file to your cluster: 
         
         kubectl apply -f httproute.yaml

  9. **Verify the GKE Gateway setup to confirm that it works.** **Note:** It may take up to five minutes for the applied changes to propagate. If you do not see the expected output for the steps in this section, wait a few minutes and try again.
     1. Get the Gateway details using the following command: 
            
            kubectl get gateway global-ext-lb1

The output should appear similar to the following: 
            
            NAME             CLASS                            ADDRESS        PROGRAMMED   AGE
            global-ext-lb1   gke-l7-global-external-managed   **34.54.193.72**   **True**         11d
            

Confirm that an IP address is assigned to the Gateway and that the value of `PROGRAMMED` is `True`.

     2. Describe the Gateway to confirm the route is attached: 
            
            kubectl describe gateway global-ext-lb1

The output should look similar to the following: 
            
            ...
              Listeners:
                **Attached Routes:  1**
                Conditions:
                  Last Transition Time:  2024-10-03T03:10:17Z
            ...

Confirm that the value of `Attached Routes` is `1`, indicating that the route is attached.

     3. Send a request to the Gateway: 
            
            curl http://GATEWAY_IP_ADDRESS/get \
                -H "Host: HOST_NAME"

Where: 

        * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
              
              kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

        * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`. You can retrieve the `HOST_NAME` using the following command: 
              
              kubectl get HTTPRoute HTTPROUTE_NAME -n NAMESPACE

For example: 
    
    curl **http://34.54.193.72/get** \
    -H "Host: **apigee-apim-operator-test.apigee.net** "

The response should appear similar to the following: 
    
    {
        "args": {},
        "headers": {
          "Accept": "*/*",
          "Host": "apigee-apim-operator-test.apigee.net",
          "User-Agent": "curl/8.7.1",
          "X-Cloud-Trace-Context": "2bb8a80e29e80662ff9cb89971c447d9/13083106619927322701"
        },
        "origin": "67.164.1.10,34.54.193.72",
        "url": "http://apigee-apim-operator-test.apigee.net/get"
      }




## What's next

Learn how to [Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
