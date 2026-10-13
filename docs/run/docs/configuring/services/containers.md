---
url: https://docs.cloud.google.com/run/docs/configuring/services/containers/
title: Configure containers for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:27.904397+00:00
---

# Configure containers for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure containers for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the container port, entrypoint command, and arguments for a Cloud Run service.

When Cloud Run starts a container, it runs the image's default entrypoint command and default command arguments. If you want to override the image's default entrypoint and command arguments, you can use the `command` and `args` fields in the container configuration. The `command` field specifies the actual command run by the container. The `args` field specifies the arguments passed to that command.

Note that you can have a maximum of 1000 arguments per container for each service.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure the container port for a service

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

For Cloud Run services, Cloud Run injects the `PORT` environment variable into the container. If you deploy multiple containers to a service, this is the ingress container. The container listens on the port defined by the `PORT` environment variable, rather than on a specific hardcoded port. If this isn't possible, configure listening to occur on the port that sends requests to the container. Note that port settings _don't_ apply to Cloud Run jobs.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Specify the port you want requests to be sent to, if not the default value of `8080`. This also sets the `PORT` environment variable.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update a service's port configuration](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) using the following command:
    
    
    gcloud run services update SERVICE --port PORT

Replace the following:

  * SERVICE: the name of the service.
  * PORT: the port to send requests to. Note that the default port is `8080`.



You can also configure ports during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --port PORT

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `containerPort:` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               name: REVISION
             spec:
               containers:
               - image: IMAGE_URL
                 ports:
                 - containerPort: PORT
         

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * PORT: the port to send requests to.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        containers {
          name = "hello-1"
          ports {
            container_port = PORT
          }
          image = "IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

  * PORT: the port to send requests to.




### Compose

To specify the container port in your `compose.yaml` file, add the `ports` attribute to your service definition.
    
    
      services:
        web:
          image: IMAGE
          ports:
            - "PORT:PORT"

Replace the following:

  * IMAGE: the URL of your container image.
  * PORT: the port to send requests to.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

## Configure entrypoint and arguments

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

The specified container command and arguments override the default image `ENTRYPOINT` and `CMD`.

You can set entrypoint command and arguments using the Google Cloud console, the Google Cloud CLI, or using a YAML file when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Specify the command you want the container to run, if not the command defined in your container, and optionally specify the arguments to the entrypoint command.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To [update the start command and arguments](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for an existing service:
    
    
    gcloud run services update SERVICE --command COMMAND --args ARG1,ARG-N

Replace the following:

  * COMMAND: the command that the container is to start up with if you are not using the default command.
  * ARG1: the argument you are sending to the container command, use a comma delimited list for more than one argument.



To specify entrypoint and arguments during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) of a new or existing service:
    
    
    gcloud run deploy --image IMAGE_URL --command COMMAND --args ARG1,ARG-N

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

To clear any entrypoint commands and arguments you have set (restore to container defaults), supply empty strings as follows:
    
    
    gcloud run deploy --image IMAGE_URL --command "" --args ""

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `command` and `args` attributes:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
                 command:
                 - COMMAND
                 args:
                 - ARG1
                 - ARG-N

Replace the following:

     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * COMMAND: the command that the container is to start up with if you are not using the default command.
     * ARG1: the argument you are sending to the container command. If you use multiple arguments, specify each on its own line—for example, as shown, ARG-N.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-containers"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
    ** image = "us-docker.pkg.dev/cloudrun/container/hello"**
    ******# Container "entry-point" command**
    ** command = ["/server"]**
    ******# Container "entry-point" args**
          args = []
        }
      }
    }

The preceding `google_cloud_run_v2_service` resource specifies a command and args. Replace `/server` with the command used to start your container, and add any necessary arguments to the `args` array.

### Compose

To specify entrypoint and arguments in your `compose.yaml` file, add the `entrypoint` or `command` attribute to your service definition.
    
    
      services:
        web:
          image: IMAGE
          entrypoint: ["COMMAND"]
          command: ["ARG1", "ARG-N"]

Replace the following:

  * IMAGE: the URL of your container image.
  * COMMAND: the command that the container is to start up with.
  * ARG1: the argument you are sending to the container command.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

### Use equals signs or commas in arguments

If you use equal signs in your arguments, supply these using the following format:
    
    
    gcloud run deploy  \
      --args="--repo-allowlist=github.com/example/example_demo"
    

If your arguments use commas, refer to [configuring environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables#setting) for details on escaping those.

## Set a working directory

The working directory is where the container executes its commands and arguments. You can specify a custom working directory for the container process during deployment of a new or existing service. If not specified, the container image's default working directory is used. To reset this field to its default, pass an empty string or remove the field.

For example:

###  gcloud 

To [update the working directory](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for an existing service:
    
    
    gcloud run services update SERVICE --workdir WORKING_DIR

Replace the following:

  * WORKING_DIR: Container's working directory. If not specified, the container image's default is used. To reset this field to its default, pass an empty string `""`.



To specify the working directory during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) of a new or existing service:
    
    
    gcloud run deploy --image IMAGE_URL --workdir WORKING_DIR

Replace the following:

  * `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * WORKING_DIR: Container's working directory.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `workingDir:` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               name: REVISION
             spec:
               containers:
               - image: IMAGE_URL
                 workingDir: WORKING_DIR
                 ports:
                 - containerPort: PORT
         

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * WORKING_DIR: (Optional) Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.
     * PORT: the port to send requests to.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        containers {
          name = "hello-1"
          working_dir = WORKING_DIR
          ports {
            container_port = PORT
          }
          image = "IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * WORKING_DIR: (Optional) Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * PORT: the port to send requests to. Note that the default port is `8080`.



## Configure container start order for sidecar deployments

To specify container start up order in a [sidecar deployment](https://docs.cloud.google.com/run/docs/deploying#sidecars), you use the container dependencies feature. You specify any containers that have dependencies and list the containers they depend on: those containers are started first. The containers that don't have any dependencies are always started first and concurrently.

You must use [startup healthcheck probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks) if you want to use this feature successfully. The startup probe enables Cloud Run to inspect the health of a dependent container, making sure it passes successfully before it starts up the next container. If you don't use healthchecks, containers are started in the specified order even if containers they depend on fail to start.

Note that ingress containers have a default startup healthcheck probe.

You can use Google Cloud console, the Google Cloud CLI, or YAML to specify the startup order:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

     * For an existing service, click the service, then click **Containers**.
     * For a new service, click **Deploy container** to display the **Create service** form.
  2. For a new service, specify the service name, ingress container URL, CPU allocation, ingress control, and authentication. In the **Containers, Networking, Security** tab, do the following:

     1. Configure the ingress container.
     2. To add each of the other containers you are deploying, click **Add container**.
     3. For all containers except the ingress container, [configure a startup healthcheck](https://docs.cloud.google.com/run/docs/configuring/healthchecks). Ingress containers have a default startup healthcheck.
     4. If a container needs other containers to start first before it can start, use the **Container startup order** menu to select the containers that must start first.
  3. For an existing service, follow these steps:

     1. For all containers except the ingress container, [configure a startup healthcheck](https://docs.cloud.google.com/run/docs/configuring/healthchecks). Ingress containers have a default startup healthcheck.
     2. Each container is shown with its own **Container startup order** menu. If a container needs other containers to start first before it can start, use the **Container startup order** menu to select the containers that must start first.
  4. Finish any other required configurations. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service. Wait for the deployment to finish.




###  gcloud 

Before using the Google Cloud CLI to specify startup order, you must [configure a startup healthcheck](https://docs.cloud.google.com/run/docs/configuring/healthchecks) for all containers except the ingress container. Ingress containers have a default startup healthcheck. You cannot configure healthchecks using the Google Cloud CLI.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy multiple containers to a service with a specified startup order, run the command:



    
    
    gcloud run deploy SERVICE \
         --container CONTAINER_1_NAME --image='INGRESS_IMAGE' --port='CONTAINER_PORT' \
         --container CONTAINER_2_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME \
         --container CONTAINER_3_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAMECONTAINER_2_NAME

Replace the following:

  * SERVICE: the name of the service you are deploying to. You can omit this parameter entirely, but you will be prompted for the service name if you omit it.
  * CONTAINER_PORT: the port where the ingress container listens for incoming requests. Unlike a single-container service, for a service containing sidecars, there is no default port for the ingress container. You must explicitly configure the container port for the ingress container and only one container can have the port exposed.
  * `INGRESS_IMAGE`: a reference to the container image that should receive requests—for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * `SIDECAR_IMAGE`: a reference to the sidecar container image.

If you want to configure each container in the deploy command, supply each container's configuration after the `container` parameters.




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `container-dependencies` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           annotations:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/container-dependencies: '{"CONTAINER1":["CONTAINER2"], "CONTAINER3":["CONTAINER1","CONTAINER2"]}'
         

Replace the following:

     * CONTAINER1: the name of the first container that depends on one or more container. Note that you can set the container name in the YAML: Cloud Run will automatically generate a name if one isn't specified.
     * CONTAINER2: the name of the container that must be started before CONTAINER1.
     * CONTAINER3: the name of the second container that depends on one or more containers.

In the example shown in the YAML snippet, CONTAINER2 is started first, CONTAINER1 is started second, and CONTAINER3 is started last.

  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Compose

To specify container startup order in your `compose.yaml` file, define the containers as separate services and use the `depends_on` attribute for the dependent container.
    
    
    services:
      web:
        image: IMAGE
        ports:
          - "8080:8080"
        container_name: web
      sidecar:
        image: SIDECAR_IMAGE
        container_name: sidecar
        depends_on:
          - web

Replace the following:

  * IMAGE: the URL of your main container image, for example, `us-docker.pkg.dev/my-project/my-repo/hello`.
  * SIDECAR_IMAGE: the URL of your sidecar container image.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        containers {
          name = "CONTAINER1"
          ports {
            container_port = 8080
          }
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          depends_on = ["CONTAINER2"]
        }
        containers {
          name = "CONTAINER2"
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          env {
            name = "PORT"
            value = "8081"
          }
          startup_probe {
            http_get {
              port = 8081
            }
          }
        }
        containers {
          name = "CONTAINER3"
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          depends_on = ["CONTAINER1", "CONTAINER2"]
          env {
            name = "PORT"
            value = "8080"
          }
          startup_probe {
            http_get {
              port = 8080
            }
          }
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * CONTAINER1: the name of the first container that depends on one or more containers.
  * CONTAINER2: the name of the container that must be started before CONTAINER1.
  * CONTAINER3: the name of the container that depends on CONTAINER1 and CONTAINER2.



## View container settings

To view the current container settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the container setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
