---
url: https://docs.cloud.google.com/endpoints/docs/grpc/get-started-mig-lb-espv2/
title: Getting started with Cloud Endpoints gRPC for Managed Instance Group with ESPv2 \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:14.222402+00:00
---

# Getting started with Cloud Endpoints gRPC for Managed Instance Group with ESPv2  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/get-started-mig-lb-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Getting started with Cloud Endpoints gRPC for Managed Instance Group with ESPv2 Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-mig-lb-espv2 "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This tutorial shows you how to deploy a simple example [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#grpc) service with the [Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) (ESPv2) in a [Managed Instance Group](https://docs.cloud.google.com/compute/docs/instance-groups).

This tutorial uses the Python version of the [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample. See the What's next section for gRPC samples in other languages.

For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/grpc/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project, and download required software. See Before you begin.
  2. Copy and configure files from the [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample. See Configuring Endpoints.
  3. Deploy the Endpoints configuration to create an Endpoints service. See Deploying the Endpoints configuration.
  4. Deploy the API and ESPv2 on the Managed Instance Group backend. See Deploying the API backend.
  5. Send a request to the API. See Sending a request to the API.
  6. Avoid incurring charges to your Google Cloud account. See Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
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

  6. Make a note of the project ID because it's needed later.
  7. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts). 
  8. Update the gcloud CLI and install the Endpoints components: 
         
         gcloud components update

  9. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud: 
         
         gcloud auth login

In the new browser tab that opens, select an account. 
  10. Set the default project to your project ID. 
         
         gcloud config set project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI Configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  11. Follow the steps in the [ gRPC Python quickstart](https://grpc.io/docs/languages/python/quickstart/) to install gRPC and the gRPC tools.



When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Configuring Endpoints

Clone the [`bookstore-grpc` sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) repository from GitHub.

To configure Endpoints:

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

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-config-deployment). See [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) for additional information.

## Deploying the API backend

So far you have deployed the API configuration to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through getting Docker set up on your Managed Instance Group and running the API backend code and the ESPv2 in a Docker container.

### Create an instance template

Create a template that you will use to create a group of VM instances. Each instance created from the template launches an ESPv2 and a backend application server.

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. Under **Name** , enter `load-balancing-espv2-template`.

  4. Under **Machine configuration** , set the **Machine type** to `e2-micro`.

  5. Under **Boot disk** , set the **Image** to `Container Optimized OS stable version`.

  6. Under **Firewall** , select **Allow HTTP traffic**.

  7. Click **Management, security, disks, networking, sole tenancy** to reveal the advanced settings.

  8. Click the **Management** tab. Under **Automation** , enter the following **Startup script**. Remember to update ENDPOINTS_SERVICE_NAME.
         
         sudo docker network create --driver bridge esp_net
         sudo docker run \
           --detach \
           --name=bookstore \
           --net=esp_net \
           gcr.io/endpointsv2/python-grpc-bookstore-server:1
         sudo docker run \
           --detach \
           --name=esp \
           --publish=80:9000 \
           --net=esp_net \
           gcr.io/endpoints-release/endpoints-runtime:2 \
           --service=ENDPOINTS_SERVICE_NAME \
           --rollout_strategy=managed \
           --listener_port=9000 \
           --healthz=/healthz \
           --backend=grpc://bookstore:8000
         

The script gets, installs, and launches the echo application server and the ESPv2 proxy server at instance startup.

  9. Click **Create**.




Wait until the template has been created before continuing.

### Create a regional managed instance group

To run the application, use the instance template to create a regional managed instance group:

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/)

  2. Click **Create instance group**.

  3. Under **Name** , enter `load-balancing-espv2-group`.

  4. Under **Location** , select **Multiple zones**.

**Pro Tip:** To ensure your application is available during extreme events, like zonal outages, Compute Engine recommends that you [distribute your application across multiple zones](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups). 

  5. Under **Region** , select **us-central1**.

  6. Click the **Configure zones** drop-down menu to reveal **Zones**. Select the following zones:

     * **us-central1-b**
     * **us-central1-c**
     * **us-central1-f**
  7. Under **Instance template** , select `load-balancing-espv2-template`.

  8. Under **Autoscaling** , select **Don't autoscale**.

  9. Set **Number of instances** to `3`.

**Pro Tip:** When creating a regional managed instance group, Compute Engine recommends that you provision enough instances so that, if all of the instances in any one zone are unavailable, the remaining instances still meet the minimum number of instances that you require. However, provisioning more instances than you need might incur additional costs. For more information, see [ Selecting instance group size to ensure availability](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision). 

  10. Under **Instance redistribution** , select **On**.

  11. Under **Autohealing** and **Health check** , select **No health check**.

  12. Click **Create**. This redirects you back to the **Instance groups** page.

**Note:** You might need to wait a few minutes until all of the instances in the group are running and ready to display the web application.



### Create a load balancer

This section explains the steps required to create a regional load balancer that directs TCP traffic to your instance group.

  1. In the Google Cloud console, go to the **Create a load balancer** page.

[Go to Create a load balancer](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Under **TCP Load Balancing** , click **Start configuration**.

  3. Under **Internet facing or internal only** , select **From Internet to my VMs**.

  4. Under **Multiple regions or single region** , select **Single region only**.

  5. Under **Backend type** , select **Backend Service**.

  6. Click **Continue**.

  7. Under **Name** , enter `espv2-load-balancer`.

  8. Under **Backend configuration** , select region **us-central1**.

  9. Select instance group `load-balancing-espv2-group`.

  10. Under **Health check** , create a new health check.

     * Under name, enter `espv2-load-balancer-check`.
     * Confirm **Protocol** is **TCP** , **Port** is **80**.
  11. Under **Frontend configuration** , enter port number **80**.

  12. Under **Review and finalize** , verify

     * The **Instance group** is `load-balancing-espv2-group`.
     * The **Region** is `us-central1`.
     * The **Protocol** is `TCP`.
     * The **IP:Port** is `EPHEMERAL:80`.
  13. After the load balancer is created, find the IP address from the **Load Balancer** page.

[Go to Load Balancer](https://console.cloud.google.com/networking/loadbalancing/add)




## Sending a request to the API

If you are sending the request from the same instance in which the Docker containers are running, you can replace SERVER_IP with `localhost`. Otherwise replace SERVER_IP with the external IP of the instance.

You can find the external IP address by running:
    
    
    gcloud compute instances list
    

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

  4. Send a request to the sample API:
         
         python bookstore_client.py --host SERVER_IP --port 80
         

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

  1. Make sure that the gcloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

  2. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list
         

  3. Using the applicable project ID from the previous step, set the default Google Cloud project to the one that your application is in:
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  4. Obtain the name of all managed services in your Google Cloud project:
         
         gcloud endpoints services list
         

  5. Delete the service from Service Management. Replace `SERVICE_NAME` with the name of the service you want to remove.
         
         gcloud endpoints services delete SERVICE_NAME
         

Running `gcloud endpoints services delete` doesn't immediately delete the managed service. Service Management disables the managed service for 30 days, which allows you time to restore it if you need to. After 30 days, Service Management permanently deletes the managed service.

  6. Go to the **Load Balancer** page.

[Go to Load Balancer](https://console.cloud.google.com/networking/loadbalancing/add)

Delete load balancer `espv2-load-balancer` with health check `espv2-load-balancer-check`.

  7. Go to the **Instance Groups** page.

[Go to Instance Groups](https://console.cloud.google.com/compute/instanceGroups)

Delete `load-balancing-espv2-group`

  8. Go to the **Instance Template** page.

[Go to Instance Templates](https://console.cloud.google.com/compute/instanceTemplates)

Delete `load-balancing-espv2-template`.




## What's next

  * Find out how to [configure your own gRPC API](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) for Endpoints.
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
