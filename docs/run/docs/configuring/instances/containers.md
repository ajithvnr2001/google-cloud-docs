---
url: https://docs.cloud.google.com/run/docs/configuring/instances/containers/
title: Configure containers for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:56.821268+00:00
---

# Configure containers for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure containers for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure the entrypoint command, and arguments for a Cloud Run instance.

When Cloud Run starts a container, it runs the image's default entrypoint command and default command arguments. If you want to override the image's default entrypoint and command arguments, you can use the `command` and `args` fields in the container configuration. The `command` field specifies the actual command run by the container. The `args` field specifies the arguments passed to that command.

Note that you can have a maximum of 1000 arguments per container for each instance.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure entrypoint and arguments

To override the default image `ENTRYPOINT` and `CMD` settings, you can set the entrypoint command and arguments for a Cloud Run instance using the Google Cloud CLI or YAML:

###  gcloud 

To [update the start command and arguments](https://docs.cloud.google.com/sdk/gcloud/reference/run/instances/update) for an existing instance:
    
    
    gcloud beta run instances update INSTANCE --command COMMAND --args ARG1,ARG-N

Replace the following:

  * INSTANCE: the name of the instance.
  * COMMAND: the command that the container starts with, if you are not using the default command.
  * ARG1: the argument you are sending to the container command. Use a comma-delimited list for more than one argument.



To specify entrypoint and arguments during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/instances/deploy) of a new or existing instance:
    
    
    gcloud beta run instances deploy INSTANCE --image IMAGE_URL --command COMMAND --args ARG1,ARG-N

Replace `IMAGE_URL` with a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..

If you want to restore the container defaults for the entrypoint commands and arguments, supply empty strings as follows:
    
    
    gcloud beta run instances update INSTANCE --command "" --args ""

### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_URL
             command:
             - COMMAND
             args:
             - ARG1
             - ARG-N

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * CONTAINER_NAME: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * COMMAND: the command that the container is to start up with if you are not using the default command.
     * ARG1: the argument you are sending to the container command. If you use multiple arguments, specify each on its own line—for example, as shown, ARG-N.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




## Configure container start order for sidecar deployments

**Preview — Cloud Run instances**

For Cloud Run instances preview, request concurrency has a maximum limit of 80 (`max_concurrency = 80`), and Dynamical Maximum Concurrent Requests (DMCR) is disabled. 

To specify the container startup order in a [sidecar deployment](https://docs.cloud.google.com/run/docs/deploy-instances#sidecars), use the container dependencies feature. Specify any containers that have dependencies and list the containers they depend on, so those containers are started first. The containers that don't have any dependencies are always started first and concurrently.

To use this feature successfully, you must use [startup health check probes](https://docs.cloud.google.com/run/docs/configuring/instances/healthchecks). The startup probe enables Cloud Run to inspect the health of a dependent container, making sure it passes successfully before it starts up the next container. If you don't use health checks, containers are started in the specified order even if containers they depend on fail to start.

Note that there is no default startup health check probe for instances.

Use the Google Cloud CLI or YAML to specify the startup order:

###  gcloud 

Before using the Google Cloud CLI to specify startup order, [configure a startup health check](https://docs.cloud.google.com/run/docs/configuring/instances/healthchecks) for any sidecar container that another container depends on. The ingress container (the container with an exposed port) has a default TCP startup health check.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy multiple containers to an instance with a specified startup order, run the command:



    
    
    gcloud beta run instances deploy INSTANCE \
         --container CONTAINER_1_NAME --image='IMAGE_URL' --port='CONTAINER_PORT' \
         --container CONTAINER_2_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME \
         --startup-probe=tcpSocket.port=SIDECAR_PORT \
         --container CONTAINER_3_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME,CONTAINER_2_NAME

Replace the following:

  * INSTANCE: the name of the instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * CONTAINER_PORT: the port where the ingress container listens for incoming requests. For an instance with multiple containers, you must explicitly configure the container port for the ingress container.
  * `SIDECAR_IMAGE`: a reference to the sidecar container image.
  * SIDECAR_PORT: the port on the sidecar container checked by its TCP startup probe. Every sidecar container that another container depends on must configure a startup probe.

If you want to configure each container in the deploy command, supply each container's configuration after the `container` parameters.




### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/container-dependencies: '{"CONTAINER1":["CONTAINER2"], "CONTAINER3":["CONTAINER1","CONTAINER2"]}'

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * CONTAINER1: the name of the first container that depends on one or more container. You can set the container name in the YAML; Cloud Run automatically generates a name if one isn't specified.
     * CONTAINER2: the name of the container that must start before CONTAINER1.
     * CONTAINER3: the name of the second container that depends on one or more containers.

In the example shown in the YAML snippet, CONTAINER2 starts first, CONTAINER1 starts second, and CONTAINER3 starts last.

  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
