---
url: https://docs.cloud.google.com/endpoints/docs/grpc/set-up-cloud-run-anthos-espv2/
title: Quickstart: Set up Cloud Endpoints gRPC for Knative serving with ESPv2 \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:06.836772+00:00
---

# Quickstart: Set up Cloud Endpoints gRPC for Knative serving with ESPv2  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/set-up-cloud-run-anthos-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Cloud Endpoints gRPC for Knative serving with ESPv2

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-cloud-run-anthos "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page shows you how to set up Cloud Endpoints for [Knative serving](https://docs.cloud.google.com/run/docs/gke/setup). Endpoints uses the [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) as an [API gateway](https://wikipedia.org/wiki/API_management). To provide API management for Knative serving, you deploy the prebuilt ESPv2 container to [Knative serving](https://docs.cloud.google.com/run/docs) running on a GKE cluster.

With this set up, ESPv2 intercepts all requests to your services and performs any necessary checks (such as authentication) before invoking the service. When the service responds, ESPv2 gathers and reports telemetry.

For an overview of Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview).

## Task List

Use the following task list as you work through the tutorial. **All tasks are required to complete this tutorial.**

  1. Create a Google Cloud project, and if you haven't deployed your own Knative serving, deploy a sample service. See Before you begin.

  2. Create a GKE cluster with Knative serving enabled.

  3. Deploy a gRPC sample Knative serving service.

  4. Create an [gRPC API configuration document](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#grpc) that describes your Endpoints API, and configure the routes to your Knative serving service. See Configuring Endpoints.

  5. Deploy the gRPC API configuration document to create a managed service. See Deploying the Endpoints configuration.

  6. Build a new ESPv2 Docker image with your Endpoints service configuration. See Building a new ESPv2 image.

  7. Deploy the new ESPv2 Knative serving image. See Deploying the ESPv2 Cloud Run image.

  8. Create a domain mapping to the ESPv2 Knative serving service.

  9. Test your configuration by Sending a request to the API.

  10. Track activity to your services. See Tracking API activity.

  11. Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Knative serving](https://docs.cloud.google.com/anthos/run/pricing)
  * [Endpoints](https://docs.cloud.google.com/endpoints/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the project ID because it is needed later. On the rest of this page, this project ID is referred to as ESPv2_PROJECT_ID.
  7. [Download and install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts).



### Setting up the gcloud command line

To set up the gcloud CLI for Knative serving for Anthos:

  1. Make sure that gcloud CLI is authorized to access your data and services.

     1. Log in. 
            
            gcloud auth login

     2. On the new browser tab that opens, choose an account that has the **Editor** or **Owner** role in the Google Cloud project that you created for deploying ESPv2 to Knative serving.

  2. Update installed `gcloud` components: 
         
         gcloud components update

  3. Set the platform to `gke` and set your default project setting for `gcloud` to the one you just created: 
         
         gcloud config set run/platform gke 
         gcloud config set project ESPv2_PROJECT_ID

Replace ESPv2_PROJECT_ID with the project ID of the project you created.

  4. Set the desired [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the new cluster. You can use any zone where GKE is supported, for example: 
         
         gcloud config set compute/zone ZONE

Replace ZONE with your zone. For example, use `us-central1-a`. You can use any zone supported by GKE. 

  5. Enable the following APIs for the project, which are needed to create a cluster, build and publish a container into the Artifact Registry: 
         
         gcloud services enable container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com




## Creating a GKE cluster with Knative serving enabled

To create a cluster and enable it for Knative serving on Google Cloud:

  1. Create a new cluster using the command: 
         
         gcloud container clusters create CLUSTER_NAME \ 
           --addons=HttpLoadBalancing,CloudRun \ 
           --machine-type=n1-standard-4 \ 
           --num-nodes=3

Replace CLUSTER_NAME with the name you want for your cluster. 

**Note:** The minimum cluster size is three nodes and the minimum machine type is `n1-standard-4` for this example. 

Although these instructions don't enable [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to resize clusters for demand, Knative serving on Google Cloud automatically scales instances within the cluster. 

  2. Wait for the cluster creation to complete. During the creation process, you should see messages similar to the following: 
         
         Creating cluster CLUSTER_NAME...done. 
         Created [https://container.googleapis.com/v1/projects/ESPv2_PROJECT_ID/zones/ZONE/clusters/CLUSTER_NAME].

The output also shows the cluster version under the `NODE_VERSION` column of the output. For example, `1.15.11-gke.1` or `1.14.10-gke.27`. Make note of the cluster version for use later in this document.

  3. Set `gcloud` defaults to use your new cluster and cluster location, to avoid having to specify these when you use the gcloud CLI: 
         
         gcloud config set run/cluster CLUSTER_NAME
         gcloud config set run/cluster_location ZONE

  4. Use the following command to view details about the new cluster: 
         
         gcloud container clusters describe CLUSTER_NAME

  5. Use the following command to fetch credentials for your cluster: 
         
         gcloud container clusters get-credentials CLUSTER_NAME




## Deploying a sample gRPC Cloud Run service

To deploy the "grpc-bookstore" Cloud Run for Anthos [sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) container to the cluster you just created:

  1. Follow the steps in the [gRPC Python quickstart](https://grpc.io/docs/languages/python/quickstart/) to install gRPC and the gRPC tools.

  2. This gRPC server [sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) contains a pre-build Docker image for the Python "grpc-bookstore service": `gcr.io/endpointsv2/python-grpc-bookstore-server:2`. Use the following command to deploy "grpc-bookstore" to your cluster:
         
         gcloud run deploy GRPC_SERVICE \
           --image=gcr.io/endpointsv2/python-grpc-bookstore-server:2 \
           --platform=gke \
          **--connectivity=internal** \
           --use-http2

Note that you specify this as an internal service so that the service is not externally accessible. 

Replace GRPC_SERVICE with the name you want for your service. For example:
         
         gcloud run deploy **grpc-bookstore** \
           --image=gcr.io/endpointsv2/python-grpc-bookstore-server:2 \
           --platform=gke \
           **--connectivity=internal** \
           --use-http2

When you are done, the following message appears:
         
         Service [**grpc-bookstore**] revision [**grpc-bookstore-00001-nuk**] has been deployed and is serving 100 percent of traffic at **http://grpc-bookstore.default.svc.cluster.local**

When you create an internal service, GKE creates a DNS name (`grpc-bookstore.default.svc.cluster.local` in this example) that can only be resolved for requests originating from within the cluster itself, not for external requests. You cannot access this DNS externally from the cluster. See [Cloud Run services](https://cloud.google.com/run/docs/resource-model#services) for more.

  3. To verify that your service is working correctly, deploy a pod with the same Docker image to your cluster. The image contains the gRPC client code for "grpc-bookstore" that you can use to test the internal service.

     1. Use the following `kubectl` command to deploy a pod to the same cluster as you deployed earlier:
            
            kubectl run grpc --generator=run-pod/v1 \
              --image=gcr.io/endpointsv2/python-grpc-bookstore-server:2

This image contains the `bookstore_client.py` script that you can use to make client requests from within the cluster. 

**Note** : For newer versions of `kubectl`, the command might issue the following warning:

`Flag --generator has been deprecated, has no effect and will be removed in the future".`

You can ignore that warning.

     2. Get the name of the "grpc-bookstore" pod created on your cluster when you deployed the Docker image in the previous step:
            
            kubectl get pods

You should see output in the form:
            
            NAME   READY    STATUS    RESTARTS   AGE
            grpc   1/1      Running   0          23h

Where `grp` the name of the "grpc-bookstore" pod. Ensure that the **Status** of the pod is **Running** before continuing.

     3. Use the following command to make a client request to the "grpc-bookstore" service:
            
            kubectl exec grpc -ti -- python3 bookstore_client.py \
              --host grpc-bookstore.default.svc.cluster.local --port=80

This command runs the `bookstore_client.py` script internally on the cluster to make a gRPC request to the "grpc-bookstore" service on the hostname `grpc-bookstore.default.svc.cluster.local`. 

If everything is working correctly, you should see a response in the form:
            
            ListShelves: shelves {
              id: 1
              theme: "Fiction"
            }
            shelves {
              id: 2
              theme: "Fantasy"
            }




## Configuring Endpoints

You must have a gRPC API spec that describes the [surface](https://cloud.google.com/endpoints/docs/openapi/glossary#surface) of your backend service and any authentication requirements. 

### About setting the name field of the gRPC API spec

In the `name` field of the gRPC API spec, you specify the Endpoints service name used to access your Knative serving service. The Endpoints service name is in the form of a domain name:
    
    
    API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog

Because the Endpoints service name corresponds to a domain name, the name must follow these rules:

  * Must contain only lowercase letters, numbers, periods, or dashes.
  * Must not start with a dash.
  * Must not contain an underscore.



For example:
    
    
    grpc-boostore-api.endpoints.ESPv2_PROJECT_ID.cloud.goog

### Creating the gRPC API spec

The [bookstore-grpc](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample contains the files that you need to copy locally and configure.

  1. Create a new directory for the gRPC API spec, such as `my-anthos-grpc`. Then cd to that directory.

  2. Clone the git repo where the gRPC client code is hosted to your new directory:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

  3. Change your working directory:
         
         cd python-docs-samples/endpoints/bookstore-grpc/

Note that this directory contains the [bookstore.proto](https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/endpoints/bookstore-grpc/bookstore.proto) file. This file defines the Bookstore service's API.

  4. Create a self-contained protobuf descriptor file from your service `.proto` file: 

     1. Create the `generated_pb2` directory under your working directory.

     2. Create the descriptor file, `api_descriptor.pb`, by using the `protoc` protocol buffers compiler. Run the following command in the directory containing `bookstore.proto`:
            
            python3 -m grpc_tools.protoc \
            --include_imports \
            --include_source_info \
            --proto_path=. \
            --descriptor_set_out=api_descriptor.pb \
            --python_out=generated_pb2 \
            --grpc_python_out=generated_pb2 \
            bookstore.proto

In the preceding command, `--proto_path` is set to the current working directory. In your gRPC build environment, if you use a different directory for `.proto` input files, change `--proto_path` so the compiler searches the directory where you saved `bookstore.proto`.

  5. Modify the `api_config_anthos.yaml` file in your current working directory (the same directory that contains `bookstore.proto`) to add the following contents to the file: 
         
         type: google.api.Service
         config_version: 3
         #
         # Name of the service configuration.
         #
         name: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
         #
         # API title to appear in the user interface (Google Cloud console).
         #
         title: Bookstore gRPC API In Cloud Run Anthors
         apis:
         - name: endpoints.examples.bookstore.Bookstore
         #
         # Create a DNS record to map your service name to IP address
         #
         endpoints:
           - name: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
             target: IP_ADDRESS
         #
         # Specify the backend address to route to
         #
         backend:
           rules:
             - selector: "*"
               address: grpc://GRPC_SERVICE.default.svc.cluster.local
               disable_auth: true
         #
         # API usage restrictions.
         #
         usage:
           rules:
           # ListShelves methods can be called without an API Key.
           - selector: endpoints.examples.bookstore.Bookstore.ListShelves
             allow_unregistered_calls: true

Indentation is important for yaml format.

  6. In the `name` field, specify the domain name of the Cloud Endpoints API used to access your Knative serving service, in the form:

`API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog`

For example:

`grpc-bookstore-api.endpoints.ESPv2_PROJECT_ID.cloud.goog`

  7. The `endpoints` section registers a DNS entry for your Endpoints service on the `cloud.goog` domain, in the form:
         
         endpoints:
           - name: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
             target: IP_ADDRESS

**Note:** If you have your own domain mapping defined for your cluster, you can omit this step. See [Configuring DNS on the cloud.goog domain](https://cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure) for more.

The IP_ADDRESS is the IP of the `istio-ingress` service for your cluster. To determine this IP address:

     1. Go to the Google Kubernetes Engine page in thethe Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes)

     2. Click **Services & Ingress** in the left navigation panel to display a list of services.

     3. If your cluster version is `1.15.3-gke.19` or greater, `1.14.3-gke.12` or greater, or `1.13.10-gke.8` or greater, scroll down to the `istio-ingress` service. For all other cluster versions, scroll down to the `istio-ingressgateway` service.

     4. Copy the external IP address shown next to the Load Balancer, without the port setting, if there is one. For example, if the IP is `XX.XXX.XX.XXX:15020`, omit the `:15020`. Ignore the other IP addresses listed.

  8. The `address` field in the `backend` section specifies the internal DNS name of the Cloud Run "grpc-bookstore" service with proto scheme `grpc://`, and disables authentication to this service:
         
         address: grpc://GRPC_SERVICE.default.svc.cluster.local
         disable_auth: true

For example:
         
         address: grpc://grpc-bookstore.default.svc.cluster.local
         disable_auth: true

This is necessary because the call from ESPv2 to the Knative serving service is made as an internal call from within the cluster and therefore authentication is not necessary.

  9. Note the value of the `title` property in the `api_config_authos.yaml` file:

`title: Bookstore gRPC API In Cloud Run Anthos`

The value of the `title` property becomes the name of the Endpoints service after you deploy the configuration.

  10. Save your gRPC API document.




For information about the fields in the OpenAPI document that Endpoints requires, see [Configuring Endpoints](https://cloud.google.com/endpoints/docs/openapi/configure-endpoints).

## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use the [gcloud endpoints services deploy](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

To deploy the Endpoints configuration:

  1. Make sure you are in the directory that contains your gRPC document.

  2. Upload the configuration and create a managed service. 
         
         gcloud endpoints services deploy api_descriptor.pb api_config_anthos.yaml \ 
           --project ESPv2_PROJECT_ID

This creates a new Endpoints service with the name that you specified in the `name` field of the `api_config_anthos.yaml` file. The Endpoints service is configured according to your OpenAPI document.

As it is creating and configuring the Endpoints service, Service Management outputs information to the terminal. When the deployment completes, a message similar to the following is displayed: 
         
         Service Configuration [CONFIG_ID] uploaded for service [API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog]

CONFIG_ID is the unique Endpoints service configuration ID created by the deployment. For example: 
         
         Service Configuration [2019-02-01r0] uploaded for service [grpc-bookstore-api.endpoints.ESPv2_PROJECT_ID.cloud.goog] 

The service configuration ID consists of a date stamp followed by a revision number. If you deploy `api_config_anthos.yaml` again on the same day, the revision number is incremented in the service configuration ID. You can view the service configuration and the [deployment history](https://docs.cloud.google.com/endpoints/docs/openapi/config-file-compare) on the **Endpoints > Services** page in the Google Cloud console.

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment). 




### Checking required services

At a minimum, Endpoints and ESP require the following Google services to be enabled: Name | Title  
---|---  
`servicemanagement.googleapis.com` | Service Management API  
`servicecontrol.googleapis.com` | Service Control API  
  
In most cases, the `gcloud endpoints services deploy` command enables these required services. However, the `gcloud` command completes successfully but doesn't enable the required services in the following circumstances:

  * If you used a third-party application such as Terraform, and you don't include these services.

  * You deployed the Endpoints configuration to an existing Google Cloud project in which these services were explicitly disabled.




Use the following command to confirm that the required services are enabled:
    
    
    gcloud services list

If you do not see the required services listed, enable them:
    
    
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

Also enable your Endpoints service:
    
    
    gcloud services enable ENDPOINTS_SERVICE_NAME

To determine the ENDPOINTS_SERVICE_NAME you can either:

  * After deploying the Endpoints configuration, go to the **Endpoints** page in the Cloud console. The list of possible ENDPOINTS_SERVICE_NAME are shown under the **Service name** column.

  * For OpenAPI, the ENDPOINTS_SERVICE_NAME is what you specified in the `host` field of your OpenAPI spec. For gRPC, the ENDPOINTS_SERVICE_NAME is what you specified in the `name` field of your gRPC Endpoints configuration.




For more information about the `gcloud` commands, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Building a new ESPv2 Knative serving image

Build the Endpoints service config into a new ESPv2 docker image. After creating this image, you can deploy it to your cluster.

**Note:**

This step is required.

The service config must be built into a new docker image because Cloud Run is a _scale-to-zero_ service. That means when there is no traffic, all instances are deleted. When traffic increases, new instances are created on-demand. This type of service instance creation is also called _cold start_. See the Cloud Run [Concurrency](https://docs.cloud.google.com/run/docs/about-concurrency) documentation for more. 

If the docker image did not have the service config built into it, Cloud Run would have to make two API calls to Google ServiceManagement at cold start. These calls count against your Google ServiceManagement API quota.

By building the service config into the ESPv2 docker image, you remove the two API calls and avoid impacting the quota count for the Google ServiceManagement service. This step also speeds up the new service instance creation and reduces the latency for the requests waiting for the new instance.

You must re-run this entire step and redeploy the new container:

  * Every time you modify and redeploy the Endpoints service configuration. Otherwise, changes to the service configuration will not be propagated to ESPv2.
  * When a new version of ESPv2 is released. Otherwise, the older version of ESPv2 will remain deployed.



To build the service config into a new ESPv2 docker image:

  1. Download this [script](https://github.com/GoogleCloudPlatform/esp-v2/tree/master/docker/serverless/gcloud_build_image) to your local machine where the gcloud CLI is installed and run it as:
         
         chmod +x gcloud_build_image 
         ./gcloud_build_image -s API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog \ 
         -c CONFIG_ID -p ESPv2_PROJECT_ID

**Note:** This script requires bash. If you are not using macOS/Linux, you can run it on [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), [Compute Engine](https://docs.cloud.google.com/compute), or Windows Subsystem for Linux.

The script uses the `gcloud` command to download the service config, build the service config into a new ESPv2 image, and upload the new image to your project container registry. The script automatically uses the latest release of ESPv2, denoted by the ESPv2_VERSION in the output image name. The output image is uploaded to:
         
         gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:ESPv2_VERSION-API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID




## Deploying the ESPv2 Knative serving image

Deploy the ESPv2 Knative serving service image to your cluster:

  1. Deploy the ESPv2 Knative serving service with the new image: 
         
         gcloud run deploy ESPv2_SERVICE_NAME \ 
           --image="gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID" \ 
           --platform gke \
           --use-http2 \
           --project=ESPv2_PROJECT_ID

For ESPv2_PROJECT_ID specify the name that you want to use for the ESPv2 service. In this example, set ESPv2_SERVICE_NAME to `ESPv2`. 

  2. If you want to configure Endpoints to use additional ESPv2 startup options, such as [enabling CORS](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options#adding_cors_support_to_esp), you can pass the arguments in the `ESPv2_ARGS` environment variable: 
         
         gcloud run deploy ESPv2_SERVICE_NAME \
           --image="gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID" \ 
           --set-env-vars=ESPv2_ARGS=--cors_preset=basic \ 
           --platform gke --use-http2 \
           --project ESPv2_PROJECT_ID

For more information and examples on setting the ESPv2_ARGS environment variable, including the list of available options and information on how to specify multiple options, see [Extensible Service Proxy V2 flags](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options).




## Creating a domain mapping to the ESPv2 Knative serving service

To be able to omit the `host` header when you make a request, add a domain mapping for the ESPv2 service: 

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Manage Custom Domains**. 

  3. Select **Add Mapping**. 

  4. From the dropdown, select **Add service domain mapping**. 

  5. In the **Select a service to map to** field of the **Add mapping** popup, select your ESPv2 service. 

  6. In the **Enter domain name** field, specify the domain name you want to use to access your Knative serving service through Endpoints. For example, specify: 
         
         API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog

Where API_NAME is the name of your Endpoints API. For this example, you can use "hello-api": 
         
         grpc-bookstore-api.endpoints.ESPv2_PROJECT_ID.cloud.goog

  7. Click **Continue**. A summary of the mapping appears. 

  8. Select **Done** to save the mapping.




## Sending requests to the API

To send requests to the sample API, you can use a sample gRPC client written in Python.

  1. Make sure you are in the directory that contains your gRPC documents, such as `api_config_anthos.yaml`.

  2. Install dependencies:
         
         pip3 install virtualenv
         virtualenv env
         source env/bin/activate
         pip3 install -r requirements.txt

  3. Send a request to the sample API:
         
         python3 bookstore_client.py --host API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog --port 80

For example:
         
         python3 bookstore_client.py --host grpc-bookstore-api.endpoints.ESPv2_PROJECT_ID.cloud.goog --port 80

If everything is working correctly, you should see a response in the form:
         
         ListShelves: shelves {
           id: 1
           theme: "Fiction"
         }
         shelves {
           id: 2
           theme: "Fantasy"
         }

     * Look at the activity graphs for your API in the **Endpoints** > **Services** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It may take a few moments for the request to be reflected in the graphs.

     * Look at the request logs for your API in the Logs Explorer page. 

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




If you don't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors).

You just deployed and tested an API in Endpoints!

### Configuring Endpoints API to use HTTPS

Automatic TLS support is disabled by default for Knative serving on Google Cloud. Therefore, in this example when you access your Endpoints API through ESPv2, you make the call using HTTP.

You can configure ESPv2 to support requests using HTTPS. Note that you configure HTTPS support on ESPv2, the external service, not on "hello", the internal backend service. 

To support HTTPS with ESPv2, you must: 

  1. Own a domain. If you don't have a domain, you can obtain one from [Google](https://domains.google/) or from another domain vendor. 

  2. Create a domain mapping for your ESPv2 service and have updated your DNS record accordingly following the instructions at the [domains mapping page](https://docs.cloud.google.com/run/docs/mapping-custom-domains). 

If you obtained your domain from Google Domains, use that as your DNS server. Otherwise use [Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name), or a DNS server of your choice. Using a domain from Google Domains is the easiest option. 

  3. In the Endpoints OpenAPI spec: 

     1. Set the `name` field to refer to your domain instead of to `*.cloud.goog`. 

     2. Remove the `endpoints` tag and its two child properties.




For complete instructions and tutorial, see [Enabling HTTPS and automatic TLS certificates](https://docs.cloud.google.com/run/docs/gke/auto-tls).

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

  1. View the activity graphs for your API on the **Endpoints** > **Service** page in the Google Cloud console.

[View Endpoints activity graphs](https://console.cloud.google.com/endpoints)

It may take a few moments for the request to be reflected in the graphs.

  2. Look at the request logs for your API on the Logs Explorer page.

[View Endpoints request logs](https://console.cloud.google.com/logs/query)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

See [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances) for information on stopping the services used by this tutorial.

## What's next

  * [Learn more about Cloud Run](https://docs.cloud.google.com/run/docs/deploying)
  * [Learn more about deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config)
  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key)
  * [Learn about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method)
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
