---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/secure-services-istio/
title: Secure Kubernetes Services with Istio \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:02.168915+00:00
---

# Secure Kubernetes Services with Istio  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/secure-services-istio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Secure Kubernetes Services with Istio Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot 

This tutorial is intended for Kubernetes users and administrators who are interested in using [Istio service mesh](https://istio.io/latest/about/service-mesh/) to securely deploy Kubernetes Services and enable mutual TLS (mTLS) communication.

### Istio and Cloud Service Mesh

Istio is not a supported Google product. We recommend running managed Cloud Service Mesh instead. For more information, see [Provision a managed Cloud Service Mesh control plane on GKE](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane).

To run Istio on a GKE Autopilot cluster, you must enable the `NET_ADMIN` and `NET_RAW` Linux capabilities in your containers. These are privileged linux capabilities. The `NET_ADMIN` capability grants broad access to network operations, such as write access to routing tables and firewalls. An attacker could potentially use this access to perform privilege escalation attacks in your cluster. For details, see [the `CAP_NET_ADMIN` manpage](https://man7.org/linux/man-pages/man7/capabilities.7.html). 

Cloud Service Mesh provides the following benefits:

  * You can provision managed Cloud Service Mesh using the [Fleet API](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) without client-side tools like `istioctl`.
  * Cloud Service Mesh automatically injects sidecar proxies into workloads without granting elevated privileges to your containers.
  * You can view rich dashboards for your mesh and services without any extra configuration and then use these metrics to configure service level objectives (SLOs) and alerts to monitor the health of your applications.
  * The managed Cloud Service Mesh control plane is upgraded automatically to ensure that you get the latest security patches and features.
  * The Cloud Service Mesh managed data plane automatically upgrades the sidecar proxies in your workloads so that you don't need to restart services yourself when proxy upgrades and security patches are available.
  * Cloud Service Mesh is a supported product and can be configured using standard open source Istio APIs. For more information, see [supported features](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp).



## Objectives

This tutorial includes the following steps:

  * Create a GKE Autopilot cluster.
  * Install Istio using the `istioctl` command line tool.
  * Deploy a sample application to test mutual TLS (mTLS) authentication.
  * Configure Istio to use mTLS authentication for service-to-service communication using a `PeerAuthentication` custom resource.
  * Verify mTLS authentication using the Kiali dashboard.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

[Cloud Shell](https://docs.cloud.google.com/shell) is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), and [Terraform](https://docs.cloud.google.com/docs/terraform). If you don't use Cloud Shell, you must install the gcloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.clusterAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Prepare the environment

To set up your environment, follow these steps:

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         gcloud config set project $PROJECT_ID
         gcloud config set compute/region us-central1
         

Replace `PROJECT_ID` with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  2. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  3. Change to the working directory:
         
         cd kubernetes-engine-samples/service-mesh/istio-tutorial
         




## Create a GKE cluster

Enable the Linux capabilities that Istio requires: `NET_RAW` and `NET_ADMIN`. GKE Autopilot does not allow `NET_ADMIN` by default, but you can enable `NET_ADMIN` using the `--workload-policies=allow-net-admin` command in GKE versions 1.27 and later:
    
    
    gcloud container clusters create-auto istio-cluster \
        --location="us-central1" \
        --workload-policies="allow-net-admin"
    

To learn more about GKE Autopilot security, see [Built-in security configurations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#built-in-security).

## Install Istio

You can install Istio on a GKE cluster using [Istioctl](https://istio.io/latest/docs/setup/install/istioctl/).

In this tutorial, you install Istio with the default [configuration profile](https://istio.io/latest/docs/setup/additional-setup/config-profiles/) recommended for production deployments.

  1. Install Istio:

     * To install the latest version of Istio:
           
           curl -L https://istio.io/downloadIstio | sh -
           

     * To install a specific version of Istio:
           
           export ISTIO_VERSION=VERSION_NUMBER
           curl -L https://istio.io/downloadIstio | TARGET_ARCH=$(uname -m) sh -
           

Replace VERSION_NUMBER with the version of Istio you want to install. For information about Istio releases, see [Release announcements](https://istio.io/latest/news/releases/).

  2. Add the `istioctl` command line tool to the PATH:
         
         cd istio-*
         export PATH=$PWD/bin:$PATH
         

  3. Install Istio on the cluster:
         
         istioctl install --set profile="default" -y
         

This step might take several minutes.

  4. Wait for the Istio Pods to be ready:
         
         watch kubectl get pods -n istio-system
         

The output is similar to the following:
         
         NAME                                    READY   STATUS        RESTARTS   AGE
         istio-ingressgateway-5c47bff876-wjm96   1/1     Running       0          2m54s
         istiod-5fc7cb65cd-k8cp4                 1/1     Running       0          2m57s
         

When the Istio Pods are `Running`, return to the command line by pressing `Ctrl+C`.




## Deploy the sample application

In this section, you use the [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos) sample application to create a service mesh with mTLS authentication.

  1. Add a namespace label that instructs Istio to enable automatic injection of Envoy sidecar proxies:
         
         kubectl label namespace default istio-injection=enabled
         

  2. Deploy the sample application:
         
         cd ..
         git clone https://github.com/GoogleCloudPlatform/bank-of-anthos.git
         kubectl apply -f bank-of-anthos/extras/jwt/jwt-secret.yaml
         kubectl apply -f bank-of-anthos/kubernetes-manifests/
         

  3. Wait for the application to be ready:
         
         watch kubectl get pods
         

The output is similar to the following:
         
         NAME                                 READY   STATUS    RESTARTS   AGE
         accounts-db-0                        2/2     Running   0          2m16s
         balancereader-5c695f78f5-x4wlz       2/2     Running   0          3m8s
         contacts-557fc79c5-5d7fg             2/2     Running   0          3m7s
         frontend-7dd589c5d7-b4cgq            2/2     Running   0          3m7s
         ledger-db-0                          2/2     Running   0          3m6s
         ledgerwriter-6497f5cf9b-25c6x        2/2     Running   0          3m5s
         loadgenerator-57f6896fd6-lx5df       2/2     Running   0          3m5s
         transactionhistory-6c498965f-tl2sk   2/2     Running   0          3m4s
         userservice-95f44b65b-mlk2p          2/2     Running   0          3m4s
         

When the Pods are `Running`, return to the command line by pressing `Ctrl+C`.

  4. Review the following manifest:
         
         # Copyright 2020 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: networking.istio.io/v1alpha3
         kind: Gateway
         metadata:
           name: frontend-gateway
         spec:
           selector:
             istio: ingressgateway # use Istio default gateway implementation
           servers:
           - port:
               number: 80
               name: http
               protocol: HTTP
             hosts:
             - "*"
         ---
         apiVersion: networking.istio.io/v1alpha3
         kind: VirtualService
         metadata:
           name: frontend-ingress
         spec:
           hosts:
           - "*"
           gateways:
           - frontend-gateway
           http:
           - route:
             - destination:
                 host: frontend
                 port:
                   number: 80

This manifest describes Istio [Gateway and VirtualService](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/) resources that expose the application and use Istio as the Ingress controller.

  5. Apply the manifest to your cluster:
         
         kubectl apply -f bank-of-anthos/extras/istio/frontend-ingress.yaml
         




## Configure mTLS

Mutual TLS (mTLS) authentication is enabled by default in Istio. That means that Istio monitors server workloads that have been migrated to Istio proxies and automatically configures client proxies to establish mTLS connections with these workloads. Istio also configures client proxies not to use mTLS when connecting to workloads without sidecar proxies.

Istio can configure mTLS to work in three modes:

  * `PERMISSIVE`: Workloads accept both mTLS and plain text traffic.
  * `STRICT`: Workloads only accept mTLS traffic.
  * `DISABLE`: mTLS is disabled. Use this mode if you want to use your own security solution.



You can apply mTLS configuration globally, per namespace, or per workload. In this tutorial, you apply configuration per namespace using the `STRICT` mTLS mode.

  1. Review the following manifest:
         
         apiVersion: security.istio.io/v1beta1
         kind: PeerAuthentication
         metadata:
           name: default
         spec:
           mtls:
               mode: STRICT

This manifest describes a Peer Authentication Istio Custom Resource.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f peer-authentication.yaml
         




For more information about mTLS in Istio, see [mutual TLS authentication](https://istio.io/latest/docs/concepts/security/#mutual-tls-authentication).

## Verify mTLS is enabled

[Kiali](https://kiali.io/) is a web-based observability dashboard for Istio service mesh that provides a graphical view of your microservices environment, allowing you to monitor and troubleshoot your applications. You can use Kiali to verify that mTLS authentication is enabled and functioning correctly in the Istio service mesh. Kiali requires Prometheus as a telemetry data source. This tutorial uses [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

### Install a query interface

  1. Create a Kubernetes namespace for the monitoring query interface:
         
         kubectl create namespace monitoring
         

  2. Grant the `roles/monitoring.viewer` role to the `default` Kubernetes ServiceAccount in the `monitoring` namespace so that the query interface can read metrics by using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity):
         
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/monitoring/sa/default" \
             --role=roles/monitoring.viewer \
             --condition=None
         

  3. Deploy the query interface workload:
         
         kubectl -n monitoring apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.7.1/examples/frontend.yaml
         

  4. Review the following manifest:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: istiod
           namespace: istio-system
         spec:
           selector:
             matchLabels:
               app: istiod
           endpoints:
           - port: 15014
             path: /metrics
             timeout: 30s
             interval: 60s

This manifest describes a `PodMonitoring` resource that collects Istio and Envoy Proxy metrics.

  5. Apply the manifest to your cluster:
         
         kubectl apply -f pod-monitorings.yaml
         

  6. Get a link to the sample application:
         
         INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
         echo "http://$INGRESS_HOST"
         

  7. Open the link to view the sample application. Sign in with the default username and password to generate traffic between the microservices.




### Install Kiali

We recommend that you install Kiali using the Kiali Operator.

  1. Install the Kiali Operator:
         
         helm repo add kiali https://kiali.org/helm-charts
         helm repo update
         helm install \
             --namespace kiali-operator \
             --create-namespace \
             kiali-operator \
             kiali/kiali-operator
         

  2. Review the following manifest:
         
         apiVersion: kiali.io/v1alpha1
         kind: Kiali
         metadata:
           name: kiali
           namespace: istio-system
         spec:
           deployment:
             namespace: istio-system
           auth:
             strategy: anonymous
           external_services:
             custom_dashboards:
               prometheus:
                 url: "http://frontend.monitoring:9090/"
                 auth:
                   type: none
             prometheus:
               url: "http://frontend.monitoring:9090/"
               auth:
                 type: none
             tracing:
               enabled: false
             grafana:
               enabled: false

This manifest describes an Operator custom resource that defines the Kiali server.

  3. Apply the manifest to your cluster:
         
         kubectl apply -f kiali.yaml
         

  4. Wait for the Kiali server to be ready:
         
         watch kubectl get pods -n istio-system
         

The output is similar to the following:
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         istio-ingressgateway-6845466857-92zp8   1/1     Running   0          9m11s
         istiod-6b47d84cf-4cqlt                  1/1     Running   0          12m
         kiali-5f6b7c8d9-abcde                   1/1     Running   0          1m
         

When the Pods are `Running`, return to the command line by pressing `Ctrl+C`.

  5. Set up port forwarding on the Kiali server Service to access the dashboard:
         
         kubectl -n istio-system port-forward svc/kiali 8080:20001
         

  6. Open Web Preview. In Kiali, go to the **Graph** section and select the **Security** option in the **Display** drop-down. This view displays the security state of each node in the graph. Nodes with an **mTLS enabled** badge indicate that mTLS is enabled for that service, and nodes without the badge indicate that mTLS is not enabled.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the individual resources

If you used an existing project and you don't want to delete it, delete the individual resources.

  1. Delete Kiali:
         
         kubectl -n istio-system delete kiali kiali
         helm uninstall --namespace kiali-operator kiali-operator
         

  2. Delete the monitoring resources:
         
         kubectl -n monitoring delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.7.1/examples/frontend.yaml
         

  3. Delete the sample application:
         
         kubectl delete -f bank-of-anthos/extras/istio/frontend-ingress.yaml
         kubectl delete -f bank-of-anthos/kubernetes-manifests
         

  4. Uninstall Istio:
         
         istioctl uninstall --purge -y
         

  5. Delete the GKE cluster:
         
         gcloud container clusters delete --location us-central1 istio-cluster --quiet
         




## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
