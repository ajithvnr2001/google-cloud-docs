---
url: https://docs.cloud.google.com/compute/docs/containers/deploying-containers/
title: Deploying containers on instances and MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:57.259959+00:00
---

# Deploying containers on instances and MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/deploying-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deploying containers on instances and MIGs Stay organized with collections  Save and categorize content based on your preferences. 

You can configure a Compute Engine instance or an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to deploy and launch a Docker container. Compute Engine supplies an up-to-date [Container-Optimized OS (COS)](https://docs.cloud.google.com/container-optimized-os/docs) image with Docker installed and launches your container when your instance starts.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

## Before you begin

  * If you aren't familiar with containers, read [What are containers and their benefits](https://docs.cloud.google.com/containers).
  * If you aren't familiar with Docker, read the [Docker documentation](https://docs.docker.com/).
  * Read about [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs).
  * Read about [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




## Choosing to deploy containers on instances and MIGs

By deploying containers on Compute Engine, you can simplify app deployment while controlling your instance infrastructure.

  * Manage instances that are running containers in the same way you would treat any other instance when configuring and managing your Compute Engine infrastructure.
  * Use familiar processes and tools such as the Google Cloud CLI or the Compute Engine API to manage your instances with containers.
  * Create scalable services using managed instance groups (MIGs) running containers, which offer features like autoscaling, autohealing, rolling updates, multi-zone deployments, and load balancing.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

Alternatively, you might consider deploying to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) to:

  * Run a large number of microservices
  * Have faster container startup time
  * Take advantage of [Kubernetes](https://kubernetes.io/) automated orchestration, including auto upgrades, node auto repair, and autoscaling



Running each microservice on a separate instance on Compute Engine could make the operating system overhead a significant part of your cost. Google Kubernetes Engine lets you deploy multiple containers and groups of containers for each instance, which can allocate host instance resources more efficiently to microservices with a smaller footprint.

## How deploying containers on Compute Engine works

The common methods of deploying software onto a Compute Engine instance include:

  * Deploying software on instance boot using a [startup script](https://docs.cloud.google.com/compute/docs/startupscript) or [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html).
  * Creating a custom boot disk image with software pre-installed.



Both of the methods in the previous list combine the tasks of configuring the app and setting up the operating system environment. As the developer, you must carefully track and resolve any runtime dependencies. For example, if two apps running on a VM use different versions of the same library, you must install both versions and point to them through system variables.

[ ![Apps running on different versions of the same library.](https://docs.cloud.google.com/static/compute/images/container-without-container-image.png)](https://docs.cloud.google.com/static/compute/images/container-without-container-image.png) **An instance with apps deployed directly to the operating system**

Alternatively, you can deploy software in a container onto an instance or to a MIG. A container carries both application software and the required libraries and is isolated from OS apps and libraries. A container can be moved between deployment environments without dealing with conflicting library versions in the container and its OS.

[ ![An example of apps deployed in containers.](https://docs.cloud.google.com/static/compute/images/container-image-cos.png)](https://docs.cloud.google.com/static/compute/images/container-image-cos.png) **An instance with apps deployed in a container**

The following process describes how you deploy a container on Compute Engine:

  1. You bundle your app and required libraries into a Docker image and publish the image to [Artifact Registry](https://docs.cloud.google.com/artifact-registry), or a third-party registry such as Docker Hub.
  2. You specify a Docker image name and the `docker run` configuration when creating an instance or an instance template for a MIG.



**Note:** As of November 1, 2020, Docker Hub [ rate limits](https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/) apply to unauthenticated or authenticated pull requests on the Docker Free plan. To avoid disruptions and have greater control over your software supply chain, you can migrate your dependencies to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).

Compute Engine executes the following tasks after you make a request to create an instance:

  1. Compute Engine creates a VM instance that uses a Google-provided [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) image. This image includes a Docker runtime and additional software that is responsible for starting your container.
  2. Compute Engine stores your container settings in [instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) under the `gce-container-declaration` metadata key.
  3. When the VM starts, the Container-Optimized OS image uses the `docker run` command configuration that is stored in the instance's metadata, pulls the container image from the repository, and starts the container.

[ ![Using the container image and docker run command.](https://docs.cloud.google.com/static/compute/images/containers-gce-process.png)](https://docs.cloud.google.com/static/compute/images/containers-gce-process.png) **Steps to create an instance or a managed instance group running a container**

## Limitations

  * You can only deploy one container for each instance. Consider [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) if you need to deploy multiple containers per instance.
  * You can only deploy containers from a public repository or from a private Artifact Registry or Container Registry repository that you can access. Other private repositories are not supported.

See the access control documentation for [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control) or [Container Registry](https://docs.cloud.google.com/container-registry/docs/access-control) for information about private registry permissions.

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

  * You can't map an instance's ports to the container's ports (Docker's `-p` option). To enable access to your containers, see [Publishing container ports](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers#publishing_container_ports).

  * You can only use [Container-Optimized OS images](https://docs.cloud.google.com/container-optimized-os/docs) with this deployment method.

  * You can only use this feature through the Google Cloud console or the Google Cloud CLI, not the API.




## Preparing a container for deployment

Choose one of the following approaches to make your container image accessible to Compute Engine:

  * [Upload](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) your Docker image to Artifact Registry.
  * Use any publicly available container images from [Docker Hub](https://hub.docker.com) or other registries.

**Note:** Consider running your container image builds on [Cloud Build](https://docs.cloud.google.com/build), with none of the overhead of managing your own build servers.

## Deploying a container on a new instance

You can deploy a container on a new VM instance by using the Google Cloud console or the Google Cloud CLI.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

The following example deploys a container from a Google-provided Nginx Docker image, `https://gcr.io/cloud-marketplace/google/nginx1:latest`, to a VM instance. To use a different Docker image, replace the Nginx Docker image with the one you want in the following steps.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  1. In the **Machine configuration** pane, go to **Name** and specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  2. In the navigation menu, click **OS and storage**. The **Operating system and storage** pane appears.

  3. Go to the **Container** section and then click **Deploy container**. In the **Configure container** pane that appears, do the following:

     1. Specify the **Container image** to use. Consider the following examples: 
        * To select an NGINX 1.12 container image from Cloud Launcher, specify `gcr.io/cloud-marketplace/google/nginx1:1.12`.
        * To deploy an Apache container image from Docker Hub, always specify the full Docker image name, such as `docker.io/httpd:2.4`.
     2. Optional. Specify any other configuration parameters of your choice. For more information about container configuration options, see [Configuring options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).
     3. To finish configuring the container and return to the **Operating system and storage** pane, click **Select**.
  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  5. To finish creating the instance, click **Create**.

After creating your instance, Compute Engine starts the instance and launches the container.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud compute instances create-with-container` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container):
         
         gcloud compute instances create-with-container INSTANCE_NAME \
             --container-image=CONTAINER_IMAGE
         

Replace the following:

     * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
     * `CONTAINER_IMAGE`: name of the container image.

For example, the following command creates an instance named `nginx-vm`, which launches and runs the container image:

`gcr.io/cloud-marketplace/google/nginx1:1.12`
    
    gcloud compute instances create-with-container nginx-vm \
        --container-image=gcr.io/cloud-marketplace/google/nginx1:1.12
    

To deploy an Apache container image from Docker Hub, always specify the full Docker image name:

`docker.io/httpd:2.4`.




## Updating a container on an instance

You can update a Docker image and configuration options to run the container on an instance using Google Cloud console or the Google Cloud CLI.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

When you update an running a container, Compute Engine performs two steps:

  * Updates container declaration on the instance. Compute Engine stores the updated container declaration in [instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) under the `gce-container-declaration` metadata key.
  * [Stops and restarts](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) the instance to actuate the updated configuration, if the instance is running. If the instance is stopped, updates the container declaration and keeps the instance stopped. The instance downloads the new image and launches the container at startup.

**Note:** If you specify a Docker image labeled with `latest`, the instance downloads the latest image and launches a container from the new image each time the instance starts. Don't use the `latest` label in production if you depend on a specific image version.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance to update.

  3. On the instance details page, click **Edit**.

  4. Specify the new container image and update the [options to run the container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers) as needed.

  5. To save your changes, click **Save and restart**. Compute Engine saves the changes and restarts the instance automatically to make the update. After the instance restarts, it downloads the new image and starts the container with the updated configuration.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Update the container declaration by using the `gcloud compute instances update-container` command. For example:
    
    
    gcloud compute instances update-container nginx-vm \
        --container-image gcr.io/cloud-marketplace/google/nginx1:latest
    

This command sets the container image to `gcr.io/cloud-marketplace/google/nginx1:latest` and restarts the instance to actuate the changes. You can also update any of the properties described in [Configuring options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers) by adding corresponding flags.

After the instance restarts, it downloads the new container image and starts the container with the new configuration.

## Deploying a container on a managed instance group

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

You can deploy a container to a new managed instance group (MIG) using Google Cloud console or the Google Cloud CLI by following these steps:

  1. Create an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) that is based on a Docker image.

**Note:** To maintain identical instances in your group, include a specific Docker image version in your instance template, such as `nginx1:15`. For more information, see [Deterministic instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates).
  2. Create a [MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) from the new instance template.




###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

The following example creates an instance template that deploys a container from a Google-provided Nginx (`gcr.io/cloud-marketplace/google/nginx1:15`) Docker image to a MIG. To use other Docker images, replace `gcr.io/cloud-marketplace/google/nginx1:15` in the following example with the image you want to use.

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. To create an instance template, click **Create instance template**.

  3. Under **Container** , select **Deploy container image**.

  4. Under **Container image** , specify the Docker image name and configure [options to run the container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers). For example, you can specify `gcr.io/cloud-marketplace/google/nginx1:15` for the container image.

  5. Click **Create**.




Next, create a MIG that uses the new instance template.

###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Create an instance template for running Docker images using the `gcloud compute instance-templates create-with-container` command:
    
    
    gcloud compute instance-templates create-with-container TEMPLATE_NAME \
      --container-image DOCKER_IMAGE
    

You can also configure [options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).

For example, the following command creates a new instance template with name `nginx-template`, which includes information about the Docker image. An instance created from this template launches and runs the Docker image `gcr.io/cloud-marketplace/google/nginx1:15` when the instance starts.
    
    
    gcloud compute instance-templates create-with-container nginx-template \
        --container-image gcr.io/cloud-marketplace/google/nginx1:15
    

Next, create a MIG using the new instance template.

Now that you have an instance template, you can [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) that uses the instance template. For example, to create a MIG by using the gcloud CLI and the `nginx-template` that you just created, run the following command:
    
    
    gcloud compute instance-groups managed create example-group \
        --base-instance-name nginx-vm \
        --size 3 \
        --template nginx-template
    

## Updating a managed instance group running a container

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can update a managed instance group (MIG) to deploy a new version of a Docker image or a new version of the Container-Optimized OS image.

### Updating a MIG to a new version of a container image

You can deploy a new version of a Docker image to a MIG by using the Managed Instance Group Updater, in three steps:

  1. Prepare a new Docker image for deployment.
  2. Create an instance template based on the new Docker image in the same way you create a container-based template.
  3. Update a MIG to the new instance template by using the [Managed Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups).



### Updating a managed instance group to a new version of Container-Optimized OS image

Google updates Container-Optimized OS images [regularly](https://docs.cloud.google.com/container-optimized-os/docs/resources/support-policy#release_quality), and you might want to apply those updates to your containerized MIGs without changing your Docker image. You can update a MIG to a new version of a Container-Optimized OS image by using Google Cloud console or the Google Cloud CLI in two steps:

  1. Create an instance template based on the current version of your Docker image, the same way you create a container-based template for a new MIG. The latest supported version of a Container-Optimized OS image is used by default.
  2. Update a MIG with the new instance template by using [Managed Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups).



## Connecting to a container using SSH

You can connect to a container on an instance by using SSH. Use the gcloud CLI to run `gcloud compute ssh` with the `--container` flag:
    
    
    gcloud compute ssh INSTANCE_NAME --container CONTAINER_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance
  * `CONTAINER_NAME`: the name of the container



Learn more about the [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) command and its arguments.

## Monitoring containers on Compute Engine

To monitor your instances running a Container-Optimized OS image, use the [Node Problem Detector](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring) agent, which communicates with Cloud Monitoring and reports health-related metrics. The agent is built into Container-Optimized OS images starting with Milestone 77.

To enable the agent, in containers using images with Milestone 88 or later, edit the [custom metadata section](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring#metadata) and set `google-monitoring-enabled` to `true`.

**Note:** For more information about setting custom metadata for an instance, refer to the [VM metadata documentation](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata).

To find other ways of enabling the Node Problem Detector, visit [Enabling health monitoring](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring#enabling_health_monitoring).

The Node Problem Detector agent supports the metrics in the [metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) that begin with `guest/`.

To interact with the metrics collected by the agent, visit the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Viewing logs

You can view three types of logs related to containers:

  1. **Startup agent logs** , also known as [konlet](https://github.com/GoogleCloudPlatform/konlet) logs. The container startup agent parses the container's configuration and runs tasks to start the container on a Compute Engine instance.

  2. **Docker event logs** report container events, including container start and stop events.

  3. **Logs from your container** include the `STDOUT` from apps that run in your container.


**Note:** Depending on the container that you're using, you might need to allow incoming traffic to the container before you see any log entries. To enable access to your containers, see [Publishing container ports](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers#publishing_container_ports).".

### Viewing container startup agent logs

Container startup agent logs are available in the serial console, through the `journald` system service included in the OS image, and through [Cloud Logging](https://docs.cloud.google.com/logging/docs).

#### Viewing container startup agent logs in the serial console

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instance for which you want to view container startup agent logs.

  3. Under **Logs** , click **Serial port 1 (console)** to view serial console logs.




###  gcloud 

Use the [`get-serial-port-output`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output) command to view logs on the instance's serial port.
    
    
    gcloud compute instances get-serial-port-output INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the instance.

For example, use the following command to view the serial port output of a instance named `nginx-vm`:
    
    
    gcloud compute instances get-serial-port-output nginx-vm
    

#### Viewing container startup agent logs in `journald`

  1. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) with a container by using SSH.
  2. Execute the `sudo journalctl` command to see the instance startup and container startup logs. Use the following command to filter for container startup agent logs (`konlet`).
         
         sudo journalctl -u konlet*
         




#### Viewing container startup agent logs in Logging

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instance for which you want to view container startup agent logs.

  3. Under **Logs** , click **Cloud Logging** to view Cloud Logging logs.

  4. Enter a search filter to retrieve container startup agent logs.
         
         resource.type="gce_instance"
         logName="projects/PROJECT_ID/logs/cos_system"
         jsonPayload.SYSLOG_IDENTIFIER="konlet-startup"
         jsonPayload._HOSTNAME="INSTANCE_NAME"
         

Replace the following:

     * `PROJECT_ID`: the project ID that contains the instance
     * `INSTANCE_NAME`: the name of the instance you want to get logs for



###  gcloud 

Use the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) with an appropriate filter to view container startup agent logs.
    
    
    gcloud logging read "resource.type=gce_instance AND \
        logName=projects/PROJECT_ID/logs/cos_system AND \
        jsonPayload.SYSLOG_IDENTIFIER=konlet-startup AND \
        jsonPayload._HOSTNAME=INSTANCE_NAME"
    

Replace the following:

  * `PROJECT_ID`: the project ID that contains the instance
  * `INSTANCE_NAME`: the name of the instance that you want to get logs for



For example, use the following command to view the last 10 container startup agent logs in Logging for an instance named `nginx-vm` that's running COS 70 and that exists in `my-project`.
    
    
    gcloud logging read "resource.type=gce_instance AND \
        logName=projects/my-project/logs/cos_system AND \
        jsonPayload.SYSLOG_IDENTIFIER=konlet-startup AND \
        jsonPayload._HOSTNAME=nginx-vm" \
        --limit 10
    

### Viewing Docker event logs

You can view Docker event logs in `journald` and in Cloud Logging.

#### Viewing Docker event logs in `journald`

  1. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) with a container using SSH.
  2. Execute the `sudo journalctl` command with the following filter to see Docker event logs.
         
         sudo journalctl -u docker-events-collector
         




#### Viewing Docker event logs in Logging

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instance for which you want to view startup agent logs.

  3. Under **Logs** , click **Cloud Logging** to view Cloud Logging logs.

  4. Enter the following search filter to retrieve Docker event logs.
         
         resource.type="gce_instance"
         logName="projects/PROJECT_ID/logs/cos_system"
         jsonPayload._HOSTNAME="INSTANCE_NAME"
         jsonPayload.SYSLOG_IDENTIFIER="docker"
         

Replace the following:

     * `PROJECT_ID`: the project ID that contains the instance
     * `INSTANCE_NAME`: the name of the instance you want to get logs for



###  gcloud 

Use the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) with an appropriate filter to view Docker event logs.
    
    
    gcloud logging read "resource.type=gce_instance AND \
        logName=projects/PROJECT_ID/logs/cos_system AND \
        jsonPayload._HOSTNAME=INSTANCE_NAME AND \
        jsonPayload.SYSLOG_IDENTIFIER=docker"
    

Replace the following:

  * `PROJECT_ID`: the project ID that contains the instance
  * `INSTANCE_NAME`: the name of the instance you want to get logs for



For example, use the following command to view the last 10 Docker event logs in Logging for an instance named `nginx-vm` that's running COS 70 and that exists in `my-project`.
    
    
    gcloud logging read "resource.type=gce_instance AND \
        logName=projects/my-project/logs/cos_system AND \
        jsonPayload._HOSTNAME=nginx-vm AND \
        jsonPayload.SYSLOG_IDENTIFIER=docker" \
        --limit 10
    

### Viewing container logs

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instance for which you want to view startup agent logs.

  3. Under **Logs** , click **Cloud Logging** to view Cloud Logging logs.

![Logs serial port 1.](https://docs.cloud.google.com/static/compute/images/containers-serial-console-logs.png)

  4. The Cloud Logging page loads with a default search filter. Copy the value for `resource.labels.instance_id`. You will use it later.

  5. Update the search filter to retrieve container logs.
         
         resource.type="gce_instance"
         logName="projects/PROJECT_ID/logs/cos_containers"
         resource.labels.instance_id="INSTANCE_ID"
         

Replace the following:

     * `PROJECT_ID`: the project ID that contains the instance
     * `INSTANCE_ID`: the ID of the instance that you want to get logs for



###  gcloud 

Use the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view container logs.

  1. Determine the ID for the instance that you want to get logs for:
         
         gcloud compute instances describe INSTANCE_NAME \
            --zone ZONE \
            --format="value(id)"
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance that you want to get logs for
     * `ZONE`: the zone where the instance is located
  2. Use the following command and filter to view the instance's container logs.
         
         gcloud logging read "resource.type=gce_instance AND \
             logName=projects/PROJECT_ID/logs/cos_containers AND \
             resource.labels.instance_id=INSTANCE_ID"
         

Replace the following:

     * `PROJECT_ID`: the project ID that contains the instance.
     * `INSTANCE_ID`: the ID of the instance.

For example, use the following command to view the last 10 container logs in Cloud Logging for an instance that is running COS 70, that exists in `my-project`, and that has an instance ID of `555123456789012345`.
    
    gcloud logging read "resource.type=gce_instance AND \
        logName=projects/my-project/logs/cos_containers AND \
        resource.labels.instance_id=555123456789012345" \
        --limit 10
    




## Specifying container-optimized images or image families

Containerized instances or instance templates are created to use the latest supported [container-optimized image](https://docs.cloud.google.com/container-optimized-os/docs) by default. The image belongs to the `cos-cloud` project.

You can override this default with another image from the `cos-cloud` project. For information about available image families and their attributes, see [Choosing the right Container-Optimized OS version](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#choosing_the_right_version).

For example, after you know which image you want to use, in the gcloud CLI, either provide the `--image` flag to override the default container-optimized image or provide the `--image-family` flag to pick the latest image from the specified family at instance creation time.

The following example creates a containerized instance that uses the latest image from the `cos-dev` image family:
    
    
    gcloud compute instances create-with-container nginx-vm \
        --image-family cos-dev \
        --image-project cos-cloud \
        --container-image gcr.io/cloud-marketplace/google/nginx1:1.15
    

## Configuring firewall rules

Containerized instances launch containers whose network is set to host mode. A container shares the host network stack, and all interfaces from the host are available to the container.

**Note:** An instance starts a container with the `--network="host"` flag of the `docker run` command. Learn about [container network settings and host mode](https://docs.docker.com/engine/reference/run#network-settings).

By [default](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules), Google Cloud [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) block all incoming connections to an instance and allow all outgoing connections from an instance.

[Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to allow incoming connections to your instance and therefore to the container.

**Note:** This method of instance creation overrides the [default host firewall configuration](https://docs.cloud.google.com/container-optimized-os/docs/how-to/firewall) of container-optimized images and opens all ports for incoming TCP connections. The ports are still not accessible from outside the instance because of the [default firewall settings](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) of the [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs) (VPC) network.

## Configuring options to run a container

You can configure the following options to run your container:

  * Specify a container restart policy.
  * Override container `ENTRYPOINT` (default command to be executed on container start).
  * Pass arguments to container `ENTRYPOINT` command.
  * Run a container in a privileged mode.
  * Mount a host directory or `tmpfs` as a data volume inside the container.
  * Set environment variables.
  * Allocate a buffer for `STDIN` in the container runtime.
  * Allocate a pseudo-TTY.



Learn more about [configuring options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).

## What's next

  * Learn about [configuring options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).
  * Learn more about [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * Learn about [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
