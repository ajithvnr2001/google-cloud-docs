---
url: https://docs.cloud.google.com/endpoints/docs/grpc/running-esp-localdev/
title: Running Extensible Service Proxy locally or on another platform \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:17.632144+00:00
---

# Running Extensible Service Proxy locally or on another platform  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/running-esp-localdev/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Running Extensible Service Proxy locally or on another platform Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page explains how to configure and run an instance of the [Extensible Service Proxy](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) (ESP) on a local machine, on another cloud provider, such as Amazon Web Services (AWS), or on a Kubernetes cluster that isn't on Google Cloud.

You can run ESP on a Linux or macOS computer or virtual machine (VM). Microsoft Windows isn't supported. You can deploy your application and ESP on the same host or on different hosts. Hosting a local instance of ESP lets you:

  * Try out ESP before deploying it to a production platform.
  * Verify that security settings are configured and working properly, and that metrics and logs appear on the **Endpoints** > **Services** page as expected.

**Note:** We recommend that you use separate Google Cloud projects for development and production. This setup avoids mixing production and development logs and metrics.**Note:** [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) supports all the features described in the following section.

## Prerequisites

As a starting point, this page assumes that:

  * You have installed Docker, if you're deploying the ESP container locally or to a VM. See [Install Docker](https://docs.docker.com/engine/installation/) for more information.

  * You have deployed an API locally or on a host that is reachable to the host where you run ESP.

  * You have [configured Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints) and [deployed the configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) to create a managed service for your API.




If you need an API for testing with ESP, you can configure and deploy the sample code in the Optional: Using a sample API section. If you have already configured and deployed your API, skip to Creating a service account.

## Optional: Using a sample API

This section walks you through configuring and deploying the Python version of the [`getting-started` for Endpoints](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/getting-started) sample locally. Do the steps in this section only if you don't have an API for testing with ESP.

The Cloud Endpoints `getting-started` sample is available in other languages. See the [Samples](https://docs.cloud.google.com/endpoints/docs/samples-videos-articles) page for the GitHub location of the `getting-started` sample in your preferred language. Follow the instructions in the sample's `README.md` file for running locally, and then follow the instructions in this section to configure Endpoints and to deploy the Endpoints configuration.

### Get required software

If you don't have a Python development environment set up yet, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup) for guidance. Make sure that you have the following installed:

  * [`virtualenv`](https://virtualenv.pypa.io/en/stable/)
  * [The Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts)
  * [`curl`](https://curl.haxx.se/download.html)



### Get the sample code

  1. Clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples
         

  2. Change to the directory that contains the sample code:
         
         cd python-docs-samples/endpoints/getting-started
         




### Configure Endpoints

  1. In the sample code directory, open the `openapi.yaml` configuration file.
         
         swagger: "2.0"
         info:
           description: "A simple Google Cloud Endpoints API example."
           title: "Endpoints Example"
           version: "1.0.0"
         host: "echo-api.endpoints.YOUR-PROJECT-ID.cloud.goog"

  2. In the `host` field, replace `YOUR-PROJECT-ID` with your own Google Cloud project ID.

**Important:** This must be the same project that you select in Creating the service account.
  3. Save the `openapi.yaml` file.




### Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

  1. Update the gcloud CLI:
         
         gcloud components update

  2. Make sure that the gcloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login

In the new browser tab that opens, select an account.

  3. Set the default project to your project ID:
         
         gcloud config set project YOUR-PROJECT-ID
         

Replace `YOUR-PROJECT-ID` with the project ID of the Google Cloud project that you specified in the `openapi.yaml` file.

  4. Deploy your configuration:
         
         gcloud endpoints services deploy openapi.yaml




Service Management uses the text that you specified in the `host` field in the `openapi.yaml` file to create a new Endpoints service with the name `echo-api.endpoints.YOUR-PROJECT-ID.cloud.goog` (if it doesn't exist), and then configures the service according to your OpenAPI configuration file.

As it's creating and configuring the service, Service Management outputs information to the terminal. You can safely ignore the warnings about the paths in the `openapi.yaml` file not requiring an API key. On successful completion, a line similar to the following displays the service configuration ID and the service name within square brackets:
    
    
    Service Configuration [2017-02-13r0] uploaded for service [echo-api.endpoints.example-project-12345.cloud.goog]
    

In the preceding example, `2017-02-13r0` is the service configuration ID, and `echo-api.endpoints.example-project-12345.cloud.goog` is the service name.

### Starting your local server

  1. Create a `virtualenv`, activate it, and install the application dependencies.
         
         virtualenv env
         source env/bin/activate
         pip install -r requirements.txt

  2. Start the server:
         
         python main.py
         

  3. Open another terminal window and use `curl` to send a request:
         
         curl --request POST \
           --header "content-type:application/json" \
           --data '{"message":"hello world"}' \
           http://localhost:8080/echo
         

The API echoes back the message that you send it, and responds with the following:
         
         {
         "message": "hello world"
         }




## Creating a service account

To provide management for your API, both ESP and ESPv2 require the services in [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview). To call these services, ESP and ESPv2 must use access tokens. When you deploy ESP or ESPv2 to Google Cloud environments, such as GKE or Compute Engine, ESP and ESPv2 obtain access tokens for you through the Google Cloud metadata service. 

When you deploy ESP or ESPv2 to a non-Google Cloud environment, such as your local desktop, an on-premises Kubernetes cluster, or another cloud provider, you must provide a [service account JSON file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) that contains a private key. ESP and ESPv2 use the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to generate access tokens to call the services that it needs to manage your API.

You can use either the Google Cloud console or the Google Cloud CLI to create the service account and private key file:

### Console

  1. In the Google Cloud console, open the **Service Accounts** page . 

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Select a project**.
  3. Select the project that your API was created in and click **Open**.
  4. Click **\+ Create Service Account**.
  5. In the **Service account name** field, enter the name for your service account.
  6. Click **Create**.
  7. Click **Continue**.
  8. Click **Done**.
  9. Click the email address of the newly created service account.
  10. Click **Keys**.
  11. Click **Add key** , then click **Create new key**.
  12. Click **Create**. A JSON key file is downloaded to your computer.

Make sure to store the key file securely, because it can be used to authenticate as your service account. You can move and rename this file however you would like.

  13. Click **Close**.




### `gcloud`

  1. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list

  2. Replace PROJECT_ID in the following command to set the default project to the one that your API is in:
         
         gcloud config set project PROJECT_ID

**Important:** You must create the service account in the same project that your API is in.
  3. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login

If you have more than one account, make sure to choose the account that is in the Google Cloud project that the API is in. If you run `gcloud auth list`, the account that you selected is shown as the active account for the project.

  4. To create a service account, run the following command and replace SERVICE_ACCOUNT_NAME and `My Service Account` with the name and display name that you want to use:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
            --display-name "My Service Account"

The command assigns an email address for the service account in the following format:

`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

This email address is required in the subsequent commands.

  5. Create a service account key file:
         
         gcloud iam service-accounts keys create ~/service-account-creds.json \
            --iam-account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com




Add required IAM roles:

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

See [`gcloud iam service-accounts`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts) for more information about the commands.

## Running ESP in a container

This section describes how to deploy the ESP container. The procedure that you use depends on where you deploy the ESP container:

  * Running ESP in a Docker container locally or on another platform
  * Running ESP in a container on a Kubernetes cluster

In the following examples, the ESP option `--http_port` only works if the gRPC service has HTTP/JSON transcoding configured. For more information, see [Transcoding HTTP/JSON to gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding). 

### Running ESP in a Docker container locally or on another platform

  1. Rename the JSON file that contains the private key for the service account to `service-account-creds.json` and copy it to `$HOME/Downloads/` if it was downloaded to a different directory. This way, the full path matches the value for the `--service_account_key` in the following `docker run` command.

  2. In the following `docker run` command, replace `YOUR_SERVICE_NAME` with the [name of your service](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id).




### Linux
    
    
    sudo docker run \
        --detach \
        --name="esp" \
        --net="host" \
        --volume=$HOME/Downloads:/esp \
        --publish=8082 \
        gcr.io/endpoints-release/endpoints-runtime:1 \
        --service=YOUR_SERVICE_NAME \
        --rollout_strategy=managed \
        --http_port=8082 \
        --http2_port=8083 \
        --backend=grpc://localhost:8080 \
        --service_account_key=/esp/service-account-creds.json
      

### mac OS

The Docker `--net="host"` option doesn't work on macOS. Instead, you must do explicit port mapping from the host to container replacing `--net="host"` with `--publish 8082:8082`. You also need to replace `localhost` with the special macOS-only DNS name `docker.for.mac.localhost`. See [Use cases and workarounds](https://docs.docker.com/docker-for-mac/networking/#per-container-ip-addressing-is-not-possible) in the Docker documentation for more information.
    
    
    sudo docker run \
      --detach \
      --name="esp" \
      --publish=8082:8082 \
      --volume=$HOME/Downloads:/esp \
      gcr.io/endpoints-release/endpoints-runtime:1 \
      --service=YOUR_SERVICE_NAME \
      --rollout_strategy=managed \
      --http_port=8082 \
      --http2_port=8083 \
      --backend=grpc://docker.for.mac.localhost:8080 \
      --service_account_key=/esp/service-account-creds.json
      

### Another platform
    
    
    sudo docker run \
      --detach \
      --name="esp" \
      --net="host" \
      --volume=$HOME/Downloads:/esp \
      --publish=8082 \
      gcr.io/endpoints-release/endpoints-runtime:1 \
      --service=YOUR_SERVICE_NAME \
      --rollout_strategy=managed \
      --http_port=8082 \
      --http2_port=8083 \
      --backend=grpc://IP_Address:PORT \
      --service_account_key=/esp/service-account-creds.json
      

The following table describes the Docker options used in the preceding commands. For information about the ESP options used in the example, see [ESP startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options).

**Option** | **Description**  
---|---  
`--detach` | This Docker option starts the container in detached mode, so it runs in the background.  
`--name="esp"` | This Docker option provides an easy-to-access name for the container. For example, to see logs from the container, you could run `docker logs esp`  
`--net="host"` | This Docker option indicates that the Docker container uses the same network configuration as the host machine, allowing it to make calls to localhost on the host machine. This option doesn't work to run ESP locally on macOS.   
`--publish=8082:8082` | For macOS when you want to run ESP locally, use this Docker option instead of `--net="host"` to do explicit port mapping from the host to container.   
`--volume=`  
`$HOME/Downloads:/esp` | This Docker option maps your local `$HOME/Downloads` directory to the `/esp `directory in the container. This mapping is used by the `--service_account_key` ESP option.  
  
### Run ESP in a container on a Kubernetes cluster

This section describes how to deploy ESP to a Kubernetes cluster that isn't on Google Cloud.

To have your API managed by Endpoints, deploy the ESP container to the same [Kubernetes pod](http://kubernetes.io/docs/user-guide/pods/) as your API container. The set of pods running ESP and your API are grouped under a [Kubernetes service](http://kubernetes.io/docs/user-guide/services/) by using a label selector, such as `app: my-api`. The Kubernetes service specifies the access policy to load balance the client requests to the proxy port.

  1. Rename the JSON file that contains the private key for the service account to `service-account-creds.json` and copy it to `$HOME/Downloads/` if it was downloaded to a different directory. This way, the full path matches the command in the next step.

  2. Run the following command to create a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) and mount the secret as a [Kubernetes volume](https://kubernetes.io/docs/concepts/storage/volumes/).
         
         kubectl create secret generic service-account-creds \
           --from-file=$HOME/Downloads/service-account-creds.json
         

On success, the following message is displayed: `secret "service-account-creds" created`

  3. In your Kubernetes configuration file, add the following, replacing `YOUR_APP_NAME` with the name of your API and `YOUR_SERVICE_NAME` with the [name of your service](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id).
         
         spec:
         replicas: 1
         template:
           metadata:
             labels:
               app: "YOUR_APP_NAME"
           spec:
             volumes:
               - name: service-account-creds
                 secret:
                   secretName: service-account-creds
                   containers:
               - name: esp
                 image: gcr.io/endpoints-release/endpoints-runtime:1
                 args: [
                   "--http_port=8082",
                   "--http2_port=8083",
                   "--backend=grpc://127.0.0.1:8081",
                   "--service=YOUR_SERVICE_NAME",
                   "--rollout_strategy=managed",
                   "--service_account_key=/etc/nginx/creds/service-account-creds.json"
                 ]
                 ports:
                   - containerPort: 8080
                 volumeMounts:
                   - mountPath: /etc/nginx/creds
                     name: service-account-creds
                     readOnly: true
         

For information about the ESP options used in the example, see [ESP startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options).

  4. Deploy ESP to Kubernetes. Replace `YOUR_CONFIGURATION_FILE` with the name of your Kubernetes configuration file.
         
         kubectl apply -f YOUR_CONFIGURATION_FILE




## Sending requests

To confirm that the service account file is correct and that the ports are mapped correctly, send some requests to your API and make sure that the requests are going through ESP. You can see the ESP logs by running:
    
    
    sudo docker logs esp

The following examples send requests to the sample API. If you aren't using the sample API, we recommend that you run similar tests.

You have configured the ESP container to receive requests on port `8082`. If you send a request directly to the server at `http://localhost:8080`, the requests bypasses ESP. For example:
    
    
    curl --request POST \
      --header "content-type:application/json" \
      --data '{"message":"hello world"}' \
      http://localhost:8080/echo
    

Response: 
    
    
      {
        "message": "hello world"
      }

When you send a request to `http://localhost:8082` which passes through ESP, and you don't send an API key, ESP rejects the request. For example:
    
    
    curl --request POST \
      --header "content-type:application/json" \
      --data '{"message":"hello world"}' \
      http://localhost:8082/echo

Response: 
    
    
      {
       "code": 16,
       "message": "Method doesn't allow unregistered callers (callers without
        established identity). Please use API Key or other form of API consumer
        identity to call this API.",
       "details": [
        {
         "@type": "type.googleapis.com/google.rpc.DebugInfo",
         "stackEntries": [],
         "detail": "service_control"
        }
       ]
      }

To test the API with an API key:

  1. Create an API key on the **API credentials** page.  


[Go to the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , then select **API key**.

  3. Copy the key, then paste it into the following environment variable statement:
         
         export KEY=AIza...
         

  4. Send a request with the key:
         
         curl --request POST \
           --header "content-type:application/json" \
           --data '{"message":"hello world"}' \
           http://localhost:8082/echo?key=$KEY

You see a successful response: 
         
         {
           "message": "hello world"
         }




## Cleaning up

Shut down and remove the `esp` Docker container using the `docker` tool:
    
    
        sudo docker stop esp
        sudo docker rm esp

If you want to clean up the deployed service configuration, see [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/grpc/deleting-an-api-and-instances). 

## What's next

  * [Learn how to add SSL support to ESP](https://docs.cloud.google.com/endpoints/docs/openapi/enabling-ssl)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
