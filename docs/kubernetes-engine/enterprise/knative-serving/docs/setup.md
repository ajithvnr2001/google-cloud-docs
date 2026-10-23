---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup/
title: Setting up Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:20.442415+00:00
---

# Setting up Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Setting up Knative serving Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to setup and configure your installation of Knative serving.

## Before you begin

You must have Knative serving installed on your GKE cluster. See the [installation guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install) for details about GKE cluster prerequisites and how to install Knative serving.

## Setting up authentication with Workload Identity Federation for GKE

You can use Workload Identity Federation for GKE to authenticate your Knative serving services to Google Cloud APIs and services. You must set up Workload Identity Federation for GKE before you deploy services to your cluster, otherwise each service that exists on your cluster prior to enabling Workload Identity Federation for GKE needs to be migrated. [Learn more about using Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity).

### Enabling metrics with Workload Identity Federation for GKE

To enable metrics, like reporting request count or request latency to Google Cloud Observability, you need to manually set write permissions for Cloud Monitoring. For details, see [Enabling metrics with Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity#enabling_all_metrics_with_workload_identity).

## Configuring HTTPS and custom domains

To enable HTTPS and set a custom domain, see the following pages:

  * [Using managed TLS certificates and HTTPS](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls)
  * [Mapping custom domains](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains)



## Setting up Cloud Service Mesh

To configure Cloud Service Mesh options for Knative serving, see the [In-cluster control plane options](https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-in-cluster), including how to [set up a private, internal network](https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-in-cluster#enable_an_internal_load_balancer).

**Note:** The [Google-managed control plane](https://docs.cloud.google.com/service-mesh/docs/supported-features-mcp) is currently not fully supported by Knative serving.

### Setting up a private, internal network

Deploying services on an internal network is useful for enterprises that provide internal apps to their staff, and for services that are used by clients that run outside the Knative serving cluster. This configuration allows other resources in your network to communicate with the service using a private, internal ([RFC 1918](https://tools.ietf.org/html/rfc1918)) IP address that can't be accessed by the public.

To create your internal network, you configure Cloud Service Mesh to use [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing) instead of a public, external network load balancer. You can then deploy your Knative serving services on an internal IP address within your [VPC network](https://docs.cloud.google.com/vpc/docs/vpc).

**Before you begin**

  * You must have `admin` permissions on your cluster.
  * If you configured a custom domain, you must [disable the managed TLS feature](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls#disable-for-domain) because Managed TLS on Knative serving is currently unsupported by the internal load balancer.
  * Only Google Cloud CLI versions 310.0 or above are supported. For details about setting up your command-line tools, see 
    * [GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools)
    * [GKE clusters outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools)



To set up the internal load balancer:

  1. Enable the internal load balancer feature in Cloud Service Mesh.

The internal load balancer is an optional feature that you can configure during the installation of Cloud Service Mesh, or by updating your existing installation.

Follow the steps in [Enabling optional features on the in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/enable-optional-features) and make sure to include the `--option internal-load-balancer` script option.

When you specify the `--option internal-load-balancer` option, the script automatically fetches the [Enable an internal load balancer](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/enable-optional-features#enable_an_internal_load_balancer) custom resource from GitHub. If you need to modify the custom resource, follow the instructions for using the `--custom_overlay` option instead.

  2. Run the following command to watch updates to your GKE cluster:
         
         kubectl -n INGRESS_NAMESPACE get svc istio-ingressgateway --watch

Replace INGRESS_NAMESPACE with the namespace of your Cloud Service Mesh ingress service. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

     1. Note the annotation `cloud.google.com/load-balancer-type: Internal`.
     2. Look for the value of `IP` in the Ingress load balancer to change to a [private IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses).
     3. Press `Ctrl+C` to stop the updates once you see a private IP address in the `IP` field.
  3. For [private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) on Google Cloud, you must open ports. For details, see [opening ports on your private cluster](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/private-cluster-open-port) in the Cloud Service Mesh documentation.




To verify internal connectivity after your changes:

  1. Deploy a service called `sample` to Knative serving in the `default` namespace:
         
         gcloud run deploy sample \
         --image gcr.io/knative-samples/helloworld \
         --namespace default
         --platform gke
         

  2. Create a Compute Engine virtual machine (VM) in the same zone as the GKE cluster:
         
         VM=cloudrun-gke-ilb-tutorial-vm
         
         gcloud compute instances create $VM
         

  3. Store the private IP address of the Istio Ingress Gateway in an environment variable called `EXTERNAL_IP` and a file called `external-ip.txt`:
         
         export EXTERNAL_IP=$(kubectl -n INGRESS_NAMESPACE get svc istio-ingressgateway \
             -o jsonpath='{.status.loadBalancer.ingress[0].ip}' | tee external-ip.txt)

Replace INGRESS_NAMESPACE with the namespace of your Cloud Service Mesh ingress service. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

  4. Copy the file containing the IP address to the VM:
         
         gcloud compute scp external-ip.txt $VM:~
         

  5. Connect to the VM using SSH:
         
         gcloud compute ssh $VM
         

  6. While in the SSH session, test the sample service:
         
         curl -s -w'\n' -H Host:sample.default.nip.io $(cat external-ip.txt)
         

The output is as follows:
         
         Hello World!
         

  7. Leave the SSH session:
         
         exit
         




## Setting up a multi-tenant environment

In multi-tenant use cases, you'll need to manage and deploy Knative serving services to a Google Kubernetes Engine cluster that is outside your current project. For more information about GKE multi-tenancy, see [Cluster multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview).

To learn how to configure multi-tenancy for Knative serving, see [Cross-project multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/multi-tenancy).

## What's next

  * [Building containers](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/building/containers)
  * [Deploying containers](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying)
  * [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
