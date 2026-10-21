---
url: https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine-espv2/
title: Getting started with Endpoints for GKE with ESPv2 \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:14.610531+00:00
---

# Getting started with Endpoints for GKE with ESPv2  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Getting started with Endpoints for GKE with ESPv2 Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine-espv2 "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This tutorial shows you how to deploy a simple example [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#grpc) service with the [Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) (ESPv2) on [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/clusters) (GKE). This tutorial uses the Python version of the [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample. See the What's next section for gRPC samples in other languages.

The tutorial uses prebuilt container images of the sample code and ESPv2, which are stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry). If you are unfamiliar with containers, see the following for more information:

  * [Deploying a containerized web application](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)
  * [Kubernetes container images](https://kubernetes.io/docs/concepts/containers/images/)



For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/grpc/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project, and download the required software. See Before you begin.
  2. Copy and configure files from the [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample. See Configuring Endpoints.
  3. Deploy the Endpoints configuration to create a Endpoints service. See Deploying the Endpoints configuration.
  4. Create a backend to serve the API and deploy the API. See Deploying the API backend.
  5. Get the service's external IP address. See Getting the service's external IP address.
  6. Send a request to the API. See Sending a request to the API.
  7. Avoid incurring charges to your Google Cloud account. See Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
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

  6. Make a note of the Google Cloud project ID because it is needed later.
  7. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts). 
  8. Update the gcloud CLI and install the Endpoints components. 
         
         gcloud components update

  9. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud: 
         
         gcloud auth login

A new browser tab opens and you are prompted to choose an account. 
  10. Set the default project to your project ID. 
         
         gcloud config set project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your project ID.

If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  11. Install `kubectl`: 
         
         gcloud components install kubectl

  12. Acquire new user credentials to use as the application's default credentials. The user credentials are needed to authorize `kubectl`. 
         
         gcloud auth application-default login

In the new browser tab that opens, choose an account. 
  13. Follow the steps in the [ gRPC Python quickstart](https://grpc.io/docs/languages/python/quickstart/) to install gRPC and the gRPC tools.



## Configuring Endpoints

The [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample contains the files that you need to copy locally and configure.

  1. Create a self-contained protobuf descriptor file from your service `.proto` file: 
     1. Save a copy of [ `bookstore.proto`](https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/endpoints/bookstore-grpc/bookstore.proto) from the example repository. This file defines the Bookstore service's API. 
     2. Create the following directory: `mkdir generated_pb2`
     3. Create the descriptor file, `api_descriptor.pb`, by using the `protoc` protocol buffers compiler. Run the following command in the directory where you saved `bookstore.proto`: 
            
            python -m grpc_tools.protoc \
                --include_imports \
                --include_source_info \
                --proto_path=. \
                --descriptor_set_out=api_descriptor.pb \
                --python_out=generated_pb2 \
                --grpc_python_out=generated_pb2 \
                bookstore.proto

In the preceding command, `--proto_path` is set to the current working directory. In your gRPC build environment, if you use a different directory for `.proto` input files, change `--proto_path` so the compiler searches the directory where you saved `bookstore.proto`. 

  2. Create a gRPC API configuration YAML file: 
     1. Save a copy of the [ `api_config.yaml`file](https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/endpoints/bookstore-grpc/api_config.yaml). This file defines the [gRPC API configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) for the Bookstore service.
     2. Replace MY_PROJECT_ID in your `api_config.yaml` file with your Google Cloud project ID. For example: 
            
            #
            # Name of the service configuration.
            #
            name: bookstore.endpoints.**example-project-12345**.cloud.goog
            

Note that the `apis.name` field value in this file exactly matches the fully-qualified API name from the `.proto` file; otherwise deployment won't work. The Bookstore service is defined in `bookstore.proto` inside package `endpoints.examples.bookstore`. Its fully-qualified API name is `endpoints.examples.bookstore.Bookstore`, just as it appears in the `api_config.yaml` file.
            
            apis:
              - name: endpoints.examples.bookstore.Bookstore




See [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints) for more information.

## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

  1. Make sure you are in the directory where the `api_descriptor.pb` and `api_config.yaml` files are located. 
  2. Confirm that the default project that the `gcloud` command-line tool is currently using is the Google Cloud project that you want to deploy the Endpoints configuration to. Validate the project ID returned from the following command to make sure that the service doesn't get created in the wrong project. 
         
         gcloud config list project
         

If you need to change the default project, run the following command:
         
         gcloud config set project YOUR_PROJECT_ID
         

  3. Deploy the `proto descriptor` file and the configuration file by using the Google Cloud CLI: 
         
         gcloud endpoints services deploy api_descriptor.pb api_config.yaml
         

As it is creating and configuring the service, Service Management outputs information to the terminal. When the deployment completes, a message similar to the following is displayed:
         
         Service Configuration [CONFIG_ID] uploaded for service [bookstore.endpoints.example-project.cloud.goog]

CONFIG_ID is the unique Endpoints service configuration ID created by the deployment. For example:
         
         Service Configuration [2017-02-13r0] uploaded for service [bookstore.endpoints.example-project.cloud.goog]
         

In the previous example, `2017-02-13r0` is the service configuration ID and `bookstore.endpoints.example-project.cloud.goog` is the service name. The service configuration ID consists of a date stamp followed by a revision number. If you deploy the Endpoints configuration again on the same day, the revision number is incremented in the service configuration ID.




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

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-config-deployment).

See [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) for additional information.

## Deploying the API backend

So far you have deployed the service configuration to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through creating a [GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/clusters) to host the API backend and deploying the API.

### Creating a container cluster

The cluster needs an [IP alias](https://docs.cloud.google.com/vpc/docs/alias-ip) to use [container native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing). To create a container cluster with an IP alias for our example:
    
    
    gcloud container clusters create espv2-demo-cluster \
        --enable-ip-alias \
        --create-subnetwork="" \
        --network=default \
        --zone=us-central1-a
    

The above command creates a cluster, `espv2-demo-cluster`, with an auto-provisioned subnetwork in zone `us-central1-a`.

### Authenticating `kubectl` to the container cluster

To use `kubectl` to create and manager cluster resources, you need to get cluster credentials and make them available to `kubectl`. To do this, run the following command, replacing NAME with your new cluster name and ZONE with its cluster zone. 
    
    
    gcloud container clusters get-credentials NAME --zone ZONE
    

### Checking required permissions

ESP and ESPv2 calls Google services which use IAM to verify if the calling identity has enough permissions to access the used IAM resources. The calling identity is the attached service account deploying ESP and ESPv2.

When deployed in GKE pod, the attached service account is the node service account. Usually it is the Compute Engine default service account. Please follow this permission [recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#permissions) to choose a proper node service account.

If [ Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is used, a separate service account other than the node service account can be used to talk to Google services. You can create a Kubernetes service account for the pod to run ESP and ESPv2, create a Google service account and associate the Kubernetes service account to the Google service account.

Follow these [ steps](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to associate a Kubernetes service account with a Google service account. This Google service account is the attached service account.

If the attached service account is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) of the project and the endpoint service configuration is deployed in the **same project** , the service account should have enough permissions to access the IAM resources, following IAM roles setup step can be skipped. Otherwise following IAM roles should be added to the attached service account.

#### Add required IAM roles:

This section describes the IAM resources used by ESP and ESPv2 and the IAM roles required for the attached service account to access these resources.

##### Endpoint Service Configuration

ESP and ESPv2 call Service Control which uses the endpoint service configuration. The endpoint service configuration is an IAM resource and ESP and ESPv2 need the [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) role to access it.

The IAM role is on the endpoint service configuration, not on the project. A project may have multiple endpoint service configurations.

Use the following gcloud command to add the role to the attached service account for the endpoint service configuration.
    
    
    gcloud endpoints services add-iam-policy-binding SERVICE_NAME \
      --member serviceAccount:SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com \
      --role roles/servicemanagement.serviceController

Where  
* `SERVICE_NAME` is the endpoint service name  
* `SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com` is the attached service account.

##### Cloud Trace

ESP and ESPv2 call [ Cloud Trace](https://cloud.google.com/trace) service to export Trace to a project. This project is called the tracing project. In ESP, the tracing project and the project that owns the endpoint service configuration are the same. In ESPv2, the tracing project can be specified by the flag `--tracing_project_id`, and defaults to the deploying project.

ESP and ESPv2 require the [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace) role to enable Cloud Trace.

Use the following gcloud command to add the role to the attached service account:
    
    
    gcloud projects add-iam-policy-binding TRACING_PROJECT_ID \
      --member serviceAccount:SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com \
      --role roles/cloudtrace.agent

Where  
* TRACING_PROJECT_ID is the tracing project ID  
* SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com is the attached service account. For more information, see [ What are roles and permissions?](https://cloud.google.com/iam/docs/understanding-roles)

### Configuring your SSL keys and certificates

[Container native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing) uses HTTP2 LB which must be TLS encrypted. This required deploying a TLS certificate to the GKE ingress and ESPv2. You can bring your own certificate or use a self-signed certificate. 

  1. Create a self-signed certificate and key using [openssl](https://www.openssl.org/). Make sure you entered the same FQDN `bookstore.endpoints.MY_PROJECT_ID.cloud.goog` when asked for **"Common Name(CN)"**. This name is used by the clients to verify the server certificate.
         
         openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
         -keyout ./server.key -out ./server.crt

  2. Create a Kubernetes secret with your SSL key and certificate. Note that the certificate is copied to two places, `server.crt` and `tls.crt`, as the secret is supplied to both GKE ingress and ESPv2. GKE ingress looks for certificate path `tls.crt` and ESPv2 looks for certificate path `server.crt`.
         
         kubectl create secret generic esp-ssl \
         --from-file=server.crt=./server.crt --from-file=server.key=./server.key \
         --from-file=tls.crt=./server.crt --from-file=tls.key=./server.key




### Deploying the sample API and ESPv2 to the cluster

**Note:** For singular/smaller endpoint fleets, use `--rollout_strategy=managed` with `SERVICE_NAME`. For large endpoint fleets, mount the service configuration as shown in the following section. 

To deploy the sample gRPC service to the cluster so that clients can use it:

  1. `git clone` this [repo](https://github.com/GoogleCloudPlatform/endpoints-samples) and open to edit the [ grpc-bookstore.yaml](https://github.com/GoogleCloudPlatform/endpoints-samples/blob/master/gke/grpc-bookstore.yaml) deployment manifest file. 
  2. Replace SERVICE_NAME with the name of your Endpoints service for ingress and ESPv2 container. This is the same name that you configured in the `name` field in the `api_config.yaml` file. 
         
         # Copyright 2016 Google Inc.
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License
         
         # Use this file to deploy the container for the grpc-bookstore sample
         # and the container for the Extensible Service Proxy (ESP) to
         # Google Kubernetes Engine (GKE).
         
         apiVersion: networking.k8s.io/v1beta1
         kind: Ingress
         metadata:
           name: esp-grpc-bookstore
           annotations:
             kubernetes.io/ingress.class: "gce"
             kubernetes.io/ingress.allow-http: "false"
         spec:
           tls:
           - hosts:
             - SERVICE_NAME
             secretName: esp-ssl
           backend:
             serviceName: esp-grpc-bookstore
             servicePort: 443
         ---
         apiVersion: cloud.google.com/v1
         kind: BackendConfig
         metadata:
           name: esp-grpc-bookstore
         spec:
           healthCheck:
             type: HTTP2
             requestPath: /healthz
             port: 9000
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: esp-grpc-bookstore
           annotations:
             service.alpha.kubernetes.io/app-protocols: '{"esp-grpc-bookstore":"HTTP2"}'
             cloud.google.com/neg: '{"ingress": true, "exposed_ports": {"443":{}}}'
             cloud.google.com/backend-config: '{"default": "esp-grpc-bookstore"}'
         spec:
           ports:
           # Port that accepts gRPC and JSON/HTTP2 requests over TLS.
           - port: 443
             targetPort: 9000
             protocol: TCP
             name: esp-grpc-bookstore
           selector:
             app: esp-grpc-bookstore
           type: ClusterIP
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: esp-grpc-bookstore
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: esp-grpc-bookstore
           template:
             metadata:
               labels:
                 app: esp-grpc-bookstore
             spec:
               volumes:
               - name: esp-ssl
                 secret:
                   secretName: esp-ssl
               containers:
               - name: esp
                 image: gcr.io/endpoints-release/endpoints-runtime:2
                 args: [
                   "--listener_port=9000",
                   "--service=SERVICE_NAME",
                   "--rollout_strategy=managed",
                   "--backend=grpc://127.0.0.1:8000",
                   "--healthz=/healthz",
                   "--ssl_server_cert_path=/etc/esp/ssl",
                 ]
                 ports:
                   - containerPort: 9000
                 volumeMounts:
                 - mountPath: /etc/esp/ssl
                   name:  esp-ssl
                   readOnly: true
               - name: bookstore
                 image: gcr.io/endpointsv2/python-grpc-bookstore-server:1
                 ports:
                   - containerPort: 8000
         

The `--rollout_strategy=managed` option configures ESPv2 to use the latest deployed service configuration. When you specify this option, within a minute after you deploy a new service configuration, ESPv2 detects the change and automatically begins using it. We recommend that you specify this option instead of providing a specific configuration ID for ESPv2 to use. For more details on the ESPv2 arguments, see [ESPv2 startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options). 

For example:
         
         spec:
               containers:
               - name: esp
                 image: gcr.io/endpoints-release/endpoints-runtime:2
                 args: [
                   "--listener_port=9000",
                   "--service=bookstore.endpoints.example-project-12345.cloud.goog",
                   "--rollout_strategy=managed",
                   "--backend=grpc://127.0.0.1:8000"
                 ]

We recommend that you set the `imagePullPolicy` in the container spec above to `Always`. This will allow newly created pods to always pull the latest version of ESPv2. Read about [ configuration best practices](https://kubernetes.io/docs/concepts/configuration/overview/#container-images) for more details. When a new version of ESPv2 is released, you can perform a rolling restart of all pods to ensure the newest version is used. 

#### Deploying service configurations to Endpoints 

If you run a large fleet of Endpoints (more than 100) in the same Google Cloud project, we recommend that you mount the service config for the container instead of using the `--rollout_strategy=managed` flag to pull the service config from the Service Management API.

The Service Management API has a default [quota](https://docs.cloud.google.com/service-infrastructure/docs/quotas#management). If a large fleet of ESPv2 proxies uses `--rollout_strategy=managed`, they will all poll for the latest service config. The fleet may exceed the quota and thus cause service config update failures.

Follow the steps below to mount the service config: 
     1. Download the service config JSON config. 
    
    curl -o "/tmp/service_config.json" -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://servicemanagement.googleapis.com/v1/services/SERVICE/configs/CONFIG_ID?view=FULL"
    

     2. Create a kubernetes config map resource from the JSON config. 
    
    kubectl create configmap service-config-configmap \
      --from-file=service_config.json:/tmp/service_config.json
    

     3. Mount the config map resource to the container and use flag `--service_config_path` to specify the path of the config file. 

For example:
    
    containers:
      - args:
        - --listener_port=8081
        - --backend=http://127.0.0.1:8080
        - --service_json_path=/etc/espv2_config/service_config.json
        - --healthz=/healthz
        image: gcr.io/endpoints-release/endpoints-runtime:2
        name: esp
        ports:
        - containerPort: 8081
          protocol: TCP
        volumeMounts:
        - mountPath: /etc/espv2_config
          name: service-config-volume
      volumes:
      - configMap:
          defaultMode: 420
          name: service-config-configmap
        name: service-config-volume
    

  3. Start the service: 
         
         kubectl create -f grpc-bookstore.yaml
         




If you get an error message, see [Troubleshooting Endpoints in GKE](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment).

## Getting the service's external IP address

You need the service's external IP address to send requests to the sample API. It can take a few minutes after you start your service in the container before the external IP address is ready.

  1. View the external IP address: 
         
         kubectl get ingress

  2. Make a note of the value for `EXTERNAL-IP` and save it in a SERVER_IP environment variable. The external IP address is used to send requests to the sample API. 
         
         export SERVER_IP=YOUR_EXTERNAL_IP
         




## Sending a request to the API

To send requests to the sample API, you can use a sample gRPC client written in Python.

  1. Clone the git repo where the gRPC client code is hosted:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
            

  2. Change your working directory:
         
         cd python-docs-samples/endpoints/bookstore-grpc/
           

  3. Install dependencies: 
         
         pip install virtualenv
         virtualenv env
         source env/bin/activate
         python -m pip install -r requirements.txt

  4. Create a root CA for the self-signed certificate
         
         openssl x509 -in server.crt -out client.pem -outform PEM
           

  5. Send a request to the sample API:
         
         python bookstore_client.py --host SERVER_IP --port 443 \
         --servername bookstore.endpoints.MY_PROJECT_ID.cloud.goog --use_tls true --ca_path=client.pem
         

     * Look at the activity graphs for your API in the **Endpoints** > **Services** page.   


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It may take a few moments for the request to be reflected in the graphs.

     * Look at the request logs for your API in the Logs Explorer page.   


[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




If you don't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors).

You just deployed and tested an API in Endpoints!

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Delete the API:
         
         gcloud endpoints services delete SERVICE_NAME
         

Replace SERVICE_NAME with the name of your API.

  2. Delete the GKE cluster:
         
         gcloud container clusters delete NAME --zone ZONE
         




## What's next

  * Find out how to [configure your own gRPC API](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) for Cloud Endpoints.
  * Look through the Bookstore sample on GitHub in more detail. Both the client and server are available in [Python](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) and [Java](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints).
  * The `getting-started-grpc` sample is available on GitHub in the following languages: 
    * [Java](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Python](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Ruby](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Go](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/endpoints/getting-started-grpc)
    * [Node.js](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/endpoints/getting-started-grpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
