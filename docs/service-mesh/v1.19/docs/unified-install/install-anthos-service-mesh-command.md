---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh-command/
title: Quickstart: Create a GKE cluster with Cloud Service Mesh and the gcloud CLI \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:47.779761+00:00
---

# Quickstart: Create a GKE cluster with Cloud Service Mesh and the gcloud CLI  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh-command/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a GKE cluster with Cloud Service Mesh and the gcloud CLI

In this tutorial, you provision managed Cloud Service Mesh using the Google Kubernetes Engine (GKE) [Fleet](https://cloud.google.com/anthos/fleet-management/docs/fleet-concepts) API on a new GKE public cluster. This tutorial walks you through:

  1. Configuring your Google Cloud project.
  2. Creating a GKE cluster with the minimum number of vCPUs required by Cloud Service Mesh.
  3. Registering the GKE cluster to your project's [Fleet](https://cloud.google.com/anthos/fleet-management/docs/fleet-concepts).
  4. Provisioning managed Cloud Service Mesh on the cluster using the Fleet API.
  5. Deploying an ingress gateway to expose the application.
  6. Deploying a sample application so that you can view telemetry data on the Cloud Service Mesh dashboards in the Google Cloud console.
  7. Exposing and accessing the sample application.



### Fleet API

This guide assumes you are familiar with [Fleets](https://cloud.google.com/anthos/fleet-management/docs), which are logical groupings of GKE clusters and other resources that can be managed together. A Fleet is a GKE concept — not a Kubernetes concept. Registering a cluster to a Fleet allows you to provision managed Cloud Service Mesh on that cluster using the [`gcloud container fleet mesh update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update). The use of Fleets is enabled by the Fleet API (`gkehub.googleapis.com`) which you enable when you begin this tutorial.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.19/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish this quickstart, you can avoid continued billing by deleting the cluster. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE, Fleet (GKE Hub), and Cloud Service Mesh APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,mesh.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE, Fleet (GKE Hub), and Cloud Service Mesh APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,mesh.googleapis.com&redirect=https%3A//console.cloud.google.com)

  8. Make a note of your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). **Tip:** Click _edit_ and enter your project ID in the following placeholder: `PROJECT_ID`

You need the project ID for some of the `gcloud` commands used in this tutorial. As long as you don't close or browse away from this documentation page, the project ID placeholders are updated on this page in each command that requires it. Placeholders make it easier to copy and paste commands to the command line. If you decide to open a link, open a new tab to preserve the placeholder values.


**Note:** In this tutorial, you will not enable the GKE Enterprise API. There are some minor differences in the Google Cloud console when the GKE Enterprise API is enabled. To learn more about these differences, see [GKE Enterprise and Cloud Service Mesh UI differences](https://docs.cloud.google.com/service-mesh/v1.19/docs/ui-differences).

## Install required tools

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

You can run the tool on [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell) or on your local machine. Cloud Shell pre-installs all the required tools.

###  Cloud Shell 

Cloud Shell provisions a [g1-small Compute Engine virtual machine (VM)](https://docs.cloud.google.com/compute/docs/machine-types) running a Debian-based Linux operating system. The advantages to using Cloud Shell are:

  * Cloud Shell includes `gcloud`, `kubectl`, `git`, and the other command-line tools that you need.

  * Your Cloud Shell $HOME directory has 5GB persistent storage space.

  * You have your choice of [text editors](https://docs.cloud.google.com/shell/docs/features#tools):

    * [Code editor](https://docs.cloud.google.com/shell/docs/features#code_editor), which you access by clicking _edit_ at the top of the Cloud Shell window.

    * Emacs, Vim, or Nano, which you access from the command line in Cloud Shell.




In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

###  Local computer 

  1. Make sure you have the following tools installed:

     * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install)
     * [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
     * [git](https://git-scm.com/downloads)
  2. Authenticate with the Google Cloud CLI:
         
         gcloud auth login --project PROJECT_ID
         

  3. Update the components:
         
         gcloud components update
         




## Create a GKE cluster

  1. Run the following command to create the cluster with the minimum number of vCPUs required by Cloud Service Mesh. In the command, replace the placeholders with the following information:

     * CLUSTER_NAME: the name of your cluster. The name can contain only lowercase alphanumerics and `-`, must start with a letter and end with an alphanumeric, and must be no longer than 40 characters.
     * PROJECT_ID: the project ID that the cluster will be created in.
     * CLUSTER_LOCATION: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1-a`.
    
    gcloud container clusters create CLUSTER_NAME \
        --project=PROJECT_ID \
        --zone=CLUSTER_LOCATION \
        --machine-type=e2-standard-4 \
        --num-nodes=2 \
        --workload-pool=PROJECT_ID.svc.id.goog
    

It takes several minutes to create the cluster. While the cluster is being created, the `gcloud` command displays the following:
    
    Creating cluster CLUSTER_NAME in CLUSTER_LOCATION...working...
    

Expected output on successful creation is similar to the following:
    
    Creating cluster CLUSTER_NAME in CLUSTER_LOCATION...done.
    Created [https://container.googleapis.com/v1/projects/PROJECT_ID/zones/CLUSTER_LOCATION/clusters/CLUSTER_NAME].
    To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/CLUSTER_LOCATION/CLUSTER_NAME?project=PROJECT_ID
    kubeconfig entry generated for CLUSTER_NAME.
    NAME: CLUSTER_NAME
    LOCATION: CLUSTER_LOCATION
    MASTER_VERSION: 1.20.10-gke.1600
    MASTER_IP: 198.51.100.1
    MACHINE_TYPE: e2-standard-4
    NODE_VERSION: 1.20.10-gke.1600
    NUM_NODES: 2
    STATUS: RUNNING
    

  2. Get [authentication credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#default_cluster_kubectl%22) to interact with the cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --project=PROJECT_ID \
             --zone=CLUSTER_LOCATION
         

Expected output:
         
         Fetching cluster endpoint and auth data.
         kubeconfig entry generated for CLUSTER_NAME.
         

  3. Set the current context for `kubectl` to the cluster.
         
         kubectl config set-context CLUSTER_NAME
         

Expected output:
         
         Context "CLUSTER_NAME" created.
         


**Tip:** To make setting up your shell environment easier in the future, you can create environment variables for the cluster name, cluster location and project ID and add them to a simple shell script that you `source` when you start a new shell. Adding a shell script or [customizing `.bashrc`](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell) is particularly handy if you are using Cloud Shell because it [disconnects](https://docs.cloud.google.com/shell/docs/limitations) after 20 minutes of inactivity. You can also add the `gcloud container clusters get-credentials` command as well so that your `kubeconfig` file points to the correct cluster. 

## Provision Cloud Service Mesh

If you haven't closed this page since you created the cluster, the placeholders have the values that you entered for the `gcloud container clusters create` command.

**Tip:** If you need to get the cluster name and location, run `gcloud container clusters list --project PROJECT_ID`. 

  1. Enable Cloud Service Mesh on your project's Fleet.
         
         gcloud container fleet mesh enable --project PROJECT_ID
         

The output is similar to:
         
         Waiting for Feature Service Mesh to be created...done.
         

  2. Register the cluster to the project's Fleet:
         
         gcloud container fleet memberships register CLUSTER_NAME-membership \
           --gke-cluster=CLUSTER_LOCATION/CLUSTER_NAME \
           --enable-workload-identity \
           --project PROJECT_ID
         

The output is similar to:
         
         Waiting for membership to be created...done.
          Finished registering to the Fleet.
         

  3. Provision managed Cloud Service Mesh on the cluster using the Fleet API:
         
         gcloud container fleet mesh update \
           --management automatic \
           --memberships CLUSTER_NAME-membership \
           --project PROJECT_ID
         

The output is similar to:
         
         Waiting for Feature Service Mesh to be updated...done.
         

**Note:** Managed Cloud Service Mesh takes cares of a lot of the manual maintenance associated with upgrading, scaling, and securing your service mesh. Learn more about about [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp).
  4. Verify that managed Cloud Service Mesh has been enabled for the cluster and is ready to be used:
         
         gcloud container fleet mesh describe --project PROJECT_ID
         

It can take about 10 minutes for Cloud Service Mesh to provision and be ready to use on the cluster. If you see `controlPlaneManagement.state: DISABLED` or `controlPlaneManagement.state: PROVISIONING`, you will need to re-run the previous command every few minutes until you see `controlPlaneManagement.state: ACTIVE`.

The output is similar to:
         
         createTime: '2022-07-06T01:05:39.110120474Z'
         membershipSpecs:
           projects/123456789123/locations/global/memberships/your-cluster-membership:
             mesh:
               management: MANAGEMENT_AUTOMATIC
         membershipStates:
           projects/123456789123/locations/global/memberships/your-cluster-membership:
             servicemesh:
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed'
                 state: ACTIVE
               dataPlaneManagement:
                 details:
                 - code: OK
                   details: Service is running.
                 state: ACTIVE
             state:
               code: OK
               description: 'Revision(s) ready for use: asm-managed.'
               updateTime: '2022-07-06T01:19:24.243993678Z'
         name: projects/your-project-id/locations/global/features/servicemesh
         resourceState:
           state: ACTIVE
         spec: {}
         state:
           state: {}
         updateTime: '2022-07-06T01:19:27.475885687Z'
         




## Download the sample code

Clone the git repository that contains the example code used in this tutorial:
    
    
       git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages.git
    

The next sections of this tutorial use a DIR_PATH variable. Set this variable to the path of the `anthos-service-mesh-packages` repository that you cloned (for example, `./anthos-service-mesh-packages`).

## Deploy an ingress gateway

Cloud Service Mesh gives you the option to deploy and manage gateways as part of your service mesh. A gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateways are Envoy proxies that provide you with fine-grained control over traffic entering and leaving the mesh.

  1. Create a namespace for the ingress gateway if you don't already have one. Gateways are user workloads, and as a best practice, they shouldn't be deployed in the control plane namespace. Replace `GATEWAY_NAMESPACE` with the name of your namespace.
         
         kubectl create namespace GATEWAY_NAMESPACE
         

Expected output:
         
         namespace/GATEWAY_NAMESPACE created
         

  2. Enable auto-injection on the gateway. The steps required depend on whether you want to use [default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) (for example, `istio-injection=enabled`) or the [revision label](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#revision) on the gateway namespace. The default revision tag and revision label are used by the sidecar injector webhook to associate injected proxies with a particular control plane revision.

### Default injection labels

**Note:** If you used a default tag revision to enable auto-injection on the gateway then verify the default tag exists in the directory that you specified in `--output_dir` and is pointing to the newly installed revision. Run the command `istioctl tag list`.

Apply the default injection labels to the namespace.
         
         kubectl label namespace GATEWAY_NAMESPACE istio-injection=enabled istio.io/rev-
         

### Revision label

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
              "jsonpath={.items[*].metadata.labels['istio\.io/rev']}{'\n'}"
            

The command outputs the revision label that corresponds to the Cloud Service Mesh version, for example: `asm-11910-9`

     2. Apply the revision label to the namespace. In the following command, `REVISION` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace GATEWAY_NAMESPACE \
              istio.io/rev=REVISION --overwrite
            

Expected output:
            
            namespace/GATEWAY_NAMESPACE labeled
            

You can ignore the message `"istio.io/rev" not found` in the output. That means that the namespace didn't previously have the `istio.io/rev` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection fails if a namespace has both the `istio.io/rev` and the `istio-injection` label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly specify both labels. 

If the gateway namespace is not labelled, the `istio-ingressgateway` pods will fail with an `ImagePullBackOff` error when the gateway attempts to pull and the `auto` image. This image should be replaced by the webhook.

  3. Download the example ingress gateway .yaml configuration file from the [`anthos-service-mesh-packages` repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.19/samples/gateways/istio-ingressgateway).

  4. Apply the example ingress gateway .yaml configuration as is, or modify as needed.
         
         kubectl apply -n GATEWAY_NAMESPACE \
           -f CONFIG_PATH/istio-ingressgateway
         

Expected output:
         
         deployment.apps/istio-ingressgateway created
         poddisruptionbudget.policy/istio-ingressgateway created
         horizontalpodautoscaler.autoscaling/istio-ingressgateway created
         role.rbac.authorization.k8s.io/istio-ingressgateway created
         rolebinding.rbac.authorization.k8s.io/istio-ingressgateway created
         service/istio-ingressgateway created
         serviceaccount/istio-ingressgateway created
         




Learn more about [best practices for gateways](https://docs.cloud.google.com/service-mesh/v1.19/docs/gateways).

## Deploy the Online Boutique sample

The Online Boutique sample application in the [`anthos-service-mesh-packages`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages) repo is modified from the original set of manifests in the [`microservices-demo`](https://github.com/GoogleCloudPlatform/microservices-demo) repo. Following best practices, each service is deployed in a separate namespace with a unique service account.

  1. Create the namespaces for the application:
         
         kubectl apply -f \
           DIR_PATH/samples/online-boutique/kubernetes-manifests/namespaces
         

Expected output:
         
         namespace/ad created
         namespace/cart created
         namespace/checkout created
         namespace/currency created
         namespace/email created
         namespace/frontend created
         namespace/loadgenerator created
         namespace/payment created
         namespace/product-catalog created
         namespace/recommendation created
         namespace/shipping created
         

  2. Enable automatic sidecar injection (auto-injection). The command required depends on whether you want to use [default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) (for example, `istio-injection=enabled`) or the same [revision label](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#revision) that you used to annotate the ingress gateway namespace

### Default injection labels

Apply the default injection labels to the namespace. In the following command, GATEWAY_NAMESPACE is the same value that you used to annotate the ingress gateway namespace.
         
         for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
           kubectl label namespace $ns istio-injection=enabled istio.io/rev-
         done;
         

Expected output:
         
         namespace/ad labeled
         namespace/cart labeled
         namespace/checkout labeled
         namespace/currency labeled
         namespace/email labeled
         namespace/frontend labeled
         namespace/loadgenerator labeled
         namespace/payment labeled
         namespace/product-catalog labeled
         namespace/recommendation labeled
         namespace/shipping labeled
         

### Revision label

Apply the revision label to the application namespaces. In the following command, REVISION is the same value that you used to annotate the ingress gateway namespace.
         
         for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
           kubectl label namespace $ns istio.io/rev=REVISION --overwrite
         done;
         

Expected output:
         
         namespace/ad labeled
         namespace/cart labeled
         namespace/checkout labeled
         namespace/currency labeled
         namespace/email labeled
         namespace/frontend labeled
         namespace/loadgenerator labeled
         namespace/payment labeled
         namespace/product-catalog labeled
         namespace/recommendation labeled
         namespace/shipping labeled
         

  3. Deploy the sample application to the cluster.

     1. Create the service accounts and deployments:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/kubernetes-manifests/deployments
            

Expected output:
            
            serviceaccount/ad created
            deployment.apps/adservice created
            serviceaccount/cart created
            deployment.apps/cartservice created
            serviceaccount/checkout created
            deployment.apps/checkoutservice created
            serviceaccount/currency created
            deployment.apps/currencyservice created
            serviceaccount/email created
            deployment.apps/emailservice created
            serviceaccount/frontend created
            deployment.apps/frontend created
            serviceaccount/loadgenerator created
            deployment.apps/loadgenerator created
            serviceaccount/payment created
            deployment.apps/paymentservice created
            serviceaccount/product-catalog created
            deployment.apps/productcatalogservice created
            serviceaccount/recommendation created
            deployment.apps/recommendationservice created
            serviceaccount/shipping created
            deployment.apps/shippingservice created
            

     2. Create the services:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/kubernetes-manifests/services
            

Expected output:
            
            service/adservice created
            service/cartservice created
            service/checkoutservice created
            service/currencyservice created
            service/emailservice created
            service/frontend created
            service/frontend-external created
            service/paymentservice created
            service/productcatalogservice created
            service/recommendationservice created
            service/shippingservice created
            

     3. Create the service entries:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/istio-manifests/allow-egress-googleapis.yaml
            

Expected output:
            
            serviceentry.networking.istio.io/allow-egress-googleapis created
            serviceentry.networking.istio.io/allow-egress-google-metadata created
            




## Exposing and accessing the application

There are multiple ways to expose the application. In this guide, we will use the ingress gateway we deployed above to do that. For other ways to expose the Online Boutique application refer to [exposing and accessing the application](https://docs.cloud.google.com/service-mesh/v1.19/docs/onlineboutique-install-kpt#exposing_and_accessing_the_application) section in the Deploying the Online Boutique sample application guide.

  1. Deploy a `Gateway` and `VirtualService` for the frontend service
         
         kubectl apply -f \
             DIR_PATH/samples/online-boutique/istio-manifests/frontend-gateway.yaml
         

Expected output:
         
         gateway.networking.istio.io/frontend-gateway created
         virtualservice.networking.istio.io/frontend-ingress created
         

  2. Get the external IP address of the [ingress gateway](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#ingress-gateway), replace the placeholders with the following information:

     * GATEWAY_SERVICE_NAME: the name of ingress gateway service. If you deployed the sample gateway without modification that would be `istio-ingressgateway`.
     * GATEWAY_NAMESPACE: the namespace in which you deployed the ingress gateway:
    
    kubectl get service GATEWAY_SERVICE_NAME \
        -n GATEWAY_NAMESPACE
    

The output is similar to:
    
    NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                      AGE
    istio-ingressgateway   LoadBalancer   10.19.247.233   35.239.7.64   80:31380/TCP,443:31390/TCP,31400:31400/TCP   27m

In this example, the IP address of the ingress gateway is `35.239.7.64`.

  3. Visit the application on your browser to confirm installation:
         
         http://EXTERNAL_IP/
         




## View the Service Mesh dashboards

After you have workloads deployed on your cluster with the sidecar proxies injected, you can explore the Cloud Service Mesh pages in the Google Cloud console to see all of the observability features that Cloud Service Mesh offers. Note that it takes about one or two minutes for telemetry data to be displayed in the Google Cloud console after you deploy workloads.

Access to Cloud Service Mesh in the Google Cloud console is controlled by [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview). To access the Cloud Service Mesh pages, a Project Owner must grant users the Project Editor or Viewer role, or the more restrictive roles described in [Controlling access to Cloud Service Mesh in the Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.19/docs/access-dashboard).

  1. In the Google Cloud console, go to **Cloud Service Mesh**.

[Go to Cloud Service Mesh](https://console.cloud.google.com/anthos/services)

  2. Select the Google Cloud project from the drop-down list on the menu bar.

  3. If you have more than one service mesh, select the mesh from the **Service Mesh** drop-down list.




To learn more, see [Exploring Cloud Service Mesh in the Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.19/docs/observability/explore-dashboard).

## Clean up

Before cleaning up, if you are interested in learning more about [mutual TLS](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#mutual_tls), see [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/v1.19/docs/by-example/mtls).

  * If you want to keep your cluster and remove the Online Boutique sample:

    1. Delete the application namespaces:
           
           kubectl delete -f DIR_PATH/samples/online-boutique/kubernetes-manifests/namespaces
           

Expected output:
           
           namespace "ad" deleted
           namespace "cart" deleted
           namespace "checkout" deleted
           namespace "currency" deleted
           namespace "email" deleted
           namespace "frontend" deleted
           namespace "loadgenerator" deleted
           namespace "payment" deleted
           namespace "product-catalog" deleted
           namespace "recommendation" deleted
           namespace "shipping" deleted
           

    2. Delete the service entries:
           
           kubectl delete -f DIR_PATH/samples/online-boutique/istio-manifests/allow-egress-googleapis.yaml
           

Expected output:
           
           serviceentry.networking.istio.io "allow-egress-googleapis" deleted
           serviceentry.networking.istio.io "allow-egress-google-metadata" deleted
           

  * If you want to prevent additional charges, delete the cluster:

    1. Run the following command:
           
           gcloud container clusters delete CLUSTER_NAME \
               --project=PROJECT_ID \
               --zone=CLUSTER_LOCATION
           

    2. At the **Do you want to continue (Y/n)?** prompt, enter **y**.

After a few minutes, you see the following output:
           
           Deleting cluster CLUSTER_NAME...done.
           Deleted [https://container.googleapis.com/v1/projects/PROJECT_ID/zones/CLUSTER_LOCATION/clusters/CLUSTER_NAME].
           




## What's next

  * To find out more about Managed Cloud Service Mesh, see [Provisioning managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh)
  * For a quick introduction to the gcloud CLI used in this tutorial, see [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference)
  * To find out how to explore Cloud Service Mesh in the Google Cloud console, see [Exploring Cloud Service Mesh in the Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.19/docs/observability/explore-dashboard)
  * To explore Cloud Service Mesh optional features, such as Cloud Trace, distroless proxy images, and end user authentication, see [Enable optional features on managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features)
  * To learn more about Security in Cloud Service Mesh, see [Cloud Service Mesh Security Overview](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/security-overview) and [Cloud Service Mesh Security Best Practices](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/anthos-service-mesh-security-best-practices)
  * To find out more about Telemetry in Cloud Service Mesh, see [Observability Overview](https://docs.cloud.google.com/service-mesh/v1.19/docs/observability-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
