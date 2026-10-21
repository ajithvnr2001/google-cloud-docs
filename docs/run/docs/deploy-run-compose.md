---
url: https://docs.cloud.google.com/run/docs/deploy-run-compose/
title: Deploy services using Compose \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:54.546002+00:00
---

# Deploy services using Compose  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deploy-run-compose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy services using Compose Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy services to Cloud Run using a file based on the [Compose specification](https://compose-spec.io/).

You can deploy to Cloud Run with a Compose file in the following ways:

  * From a prebuilt container image
  * From source code



Using Compose to deploy to Cloud Run is ideal for development and simplifies the transition from your local environment to a cloud environment. It lets you maintain a consistent configuration format for both your local and deployed applications.

For managing production environments in an infrastructure-as-code (IaC) environment, we recommend using [Terraform](https://docs.cloud.google.com/docs/terraform).

## Limitations

  * Compose deployment deploys a single Cloud Run service with multiple containers.
  * Compose deployment translates only a subset of supported Cloud Run features.
  * Services created using Compose are set by default to [1 maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances).
  * While it simplifies deployment, Cloud Run Compose deploy isn't a replacement for a comprehensive infrastructure-as-code strategy for production environments.



## Deploy services from container images with Compose

Define your services in a `compose.yaml` file and deploy them from existing container images. For more information, see [Deploy container images](https://docs.cloud.google.com/run/docs/deploying).

### Example: Single-service application

The following example shows a `compose.yaml` file for a web service that uses a prebuilt container image.
    
    
    services:
      web:
        image: us-docker.pkg.dev/cloudrun/container/hello
        ports:
          - "8080:8080"
    

### Example: Multi-container application with Nginx, Flask, and MongoDB

The following example shows a `compose.yaml` file for an application with an Nginx proxy, a Flask backend, and a MongoDB database.

Deploying this example requires the following project structure:

  * `compose.yaml`: The Compose file defining the services.
  * [`nginx/nginx.conf`](https://github.com/docker/awesome-compose/blob/master/nginx-flask-mongo/nginx/nginx.conf): Configuration for the Nginx proxy.
  * [`flask/`](https://github.com/docker/awesome-compose/tree/master/nginx-flask-mongo/flask): Directory containing the Flask application code (`server.py`, `Dockerfile`, and `requirements.txt`).


    
    
    services:
      web:
        image: nginx
        volumes:
          - ./nginx/nginx.conf:/tmp/nginx.conf
        environment:
          - FLASK_SERVER_ADDR=backend:9091
        command: /bin/bash -c "envsubst < /tmp/nginx.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
          - 80:80
        x-google-cloudrun:
          ingress-container: true
        depends_on:
          - backend
    
      backend:
        build:
          context: flask
          target: builder
        stop_signal: SIGINT
        environment:
          - FLASK_SERVER_PORT=9091
        volumes:
          - ./flask:/src
        depends_on:
          -  mongo
        ports:
          - 9091:9091
    
      mongo:
        image: mongo
        ports:
          - 27017:27017
    

### Deploy the services

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.

After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.




## Deploy from source with Compose

Define your services in a `compose.yaml` file and deploy them by building from source code. For more information, see [Deploy services from source code](https://docs.cloud.google.com/run/docs/deploying-source-code).

### Example: Single-service application

The following example shows a `compose.yaml` file for a web service that builds from source in the current directory.
    
    
    services:
      web:
        build: .
        ports:
          - "8080:8080"
    

### Deploy the services

  * In your project directory, create a `compose.yaml` file with your service definitions.

    1. To deploy the services, run the `gcloud run compose up` command:
           
           gcloud run compose up compose.yaml

    2. Respond `y` to any prompts to install required components or to enable APIs.

    3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.

After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.




### Force a rebuild

By default, Cloud Run Compose deploy skips the build process if your source code has not changed since the last build. To force a rebuild of any services defined with a `build` configuration, use the `--build` flag as follows:
    
    
    gcloud run compose up compose.yaml --build
    

This is particularly useful if a remote repository, image, or digest was deleted but your local source code remains the same. The `--build` and `--no-build` flags are mutually exclusive.

## Supported features

When you deploy using a `compose.yaml` file, Cloud Run can automatically provision other Google Cloud resources as defined in your Compose file. If resources are required, Cloud Run prompts you for consent before creating them.

Cloud Run supports the following subset of Compose features:

Compose field | Cloud Run mapping & description  
---|---  
`services` |  Services map to individual containers in the deployed Cloud Run service.  
`volumes` |  Partially supported. Translates `bind`, `volume`, and `tmpfs` mounts into Cloud Run equivalents.  
`secrets` |  Supported. Using Secret Manager.  
`configs` |  Supported. Using Cloud Storage.  
`build` |  Supported. Builds the container using the build context, tagging and pushing to the `cloud-run-source-deploy` repository in Artifact Registry. Use the `--build` flag to force a rebuild even if the source code hasn't changed since the last build.  
`image` |  Deploys a prebuilt container image from a supported registry. Use if you have a prebuilt image. Only supports Docker Hub and Artifact Registry images. For custom images, you can push images to Artifact Registry and use them.  
`ports` |  A list of port mappings, such as `8080:8080`, that determine the ingress container.  
`expose` |  A list of ports to expose but not publish, such as `3000`, to ensure that dependent services have a port available for communication.  
`depends_on` |  Defines the container startup order. This ensures that any `run-compose`-listed service has a port defined by `ports` or `expose` so that other containers can communicate with it.  
`cpus` |  A hint used to set Cloud Run CPU and memory limits, automatically allocating resources according to the following logic:

  * `<= 2 CPU: 1Gi Memory`
  * `<= 4 CPU: 2Gi Memory`
  * `> 4 CPU: 4Gi Memory`

  
`container_name` |  Sets the container's name for dependency resolution, defaulting to the service name if not specified.  
`environment` |  Passes environment variables to the corresponding container in Cloud Run.  
`command` |  Overrides the container's default command, declared by the container, by mapping to the `args` attribute in Cloud Run; for example, a Dockerfile's `CMD` instruction.  
`entrypoint` |  Supported.  
`env_file` |  Supported.  
`x-google-cloudrun:ingress-container` |  (Extension) Add this Google-specific extension to a service and set to `true` to mark as the ingress container that receives all external traffic.  
`x-google-cloudrun:volume-type: in-memory` |  (Extension) Add this Google-specific extension to a volume and set to `in-memory` instead of the default volume backed by Cloud Storage.  
  
### Secrets mapped to Secret Manager

If your `compose.yaml` file defines `secrets`, the gcloud CLI provisions Secret Manager secrets to store this data.

The following example shows a `compose.yaml` file for a gcloud CLI service that uses a secret stored in Secret Manager:
    
    
    services:
      web:
        image: us-docker.pkg.dev/cloudrun/container/hello
        ports:
          - "8080:8080"
        secrets:
          - my_app_password
    secrets:
      my_app_password:
        file: my_app_password.txt
    

The secret name in Secret Manager follows this pattern: `SERVICE_NAME-REGION-SECRET_NAME`.

For more information, see [Secret mounting limitations](https://docs.cloud.google.com/run/docs/configuring/services/secrets#limitations).

### Volumes and configs mapped to Cloud Storage

If your `compose.yaml` file defines top-level `volumes` or `configs`, the gcloud CLI provisions a Cloud Storage bucket to manage this data. A single bucket is created per deployment, using folders to separate volumes and configs.

  * **Named volumes** : An empty folder corresponding to the volume name is created in the bucket.
  * **Bind mounts** : For bind mounts, Cloud Run uploads the contents of the local source directory to a folder in the bucket prior to deployment.
  * **Configs** : For each config defined with a `file:` source, Cloud Run uploads the contents of the local file to a folder in the bucket.



## Required roles

During deployment, Cloud Run automatically grants the service identity of the deployed service the necessary roles to access provisioned resources:

  * **Cloud Storage Bucket** : `roles/storage.objectUser`
  * **Secret Manager Secrets** : `roles/secretmanager.secretAccessor`



## Communication between containers of the same instance

Cloud Run adds an entry to the `/etc/hosts` file in each container. This entry maps the service names from your `compose.yaml` file to their internal IP addresses, which lets services communicate with each other using their service names.

## What's next

  * Learn more about [managing services](https://docs.cloud.google.com/run/docs/managing/services).
  * Learn about [setting up authentication](https://docs.cloud.google.com/run/docs/authenticating/public).
  * Learn how to [manage secrets](https://docs.cloud.google.com/run/docs/configuring/secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
