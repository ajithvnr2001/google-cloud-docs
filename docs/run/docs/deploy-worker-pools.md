---
url: https://docs.cloud.google.com/run/docs/deploy-worker-pools/
title: Deploy worker pools to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:48.502021+00:00
---

# Deploy worker pools to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deploy-worker-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy worker pools to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to deploy container images to a new Cloud Run worker pool or to a new revision of an existing Cloud Run worker pool.

Worker pools are a Cloud Run resource specifically designed for performing continuous background work. In contrast to Cloud Run services, worker pools do not have a load balanced endpoint/URL and do not support autoscaling.

For an example walkthrough of deploying a new worker pool, see [Deploy a sample worker pool quickstart](https://docs.cloud.google.com/run/docs/quickstarts/workerpools/deploy-workerpool).

### Required roles

To get the permissions that you need to deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the identity that your worker pools uses to interact with other Google Cloud services
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the Artifact Registry repository of the deployed container image



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Supported container registries and images

You can directly use container images stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview), or public images from [Docker Hub](https://hub.docker.com/) or [GitHub Container Registry](https://ghcr.io/). Google recommends the use of Artifact Registry. Public images from GitHub Container Registry and [Docker Hub images](https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images) are cached for up to one hour.

You can use container images from other public or private registries (like JFrog Artifactory or Nexus), or private images from GitHub Container Registry, by setting up an [Artifact Registry remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).

You should only consider [Docker Hub](https://hub.docker.com/) for deploying popular container images such as [Docker Official Images](https://docs.docker.com/docker-hub/official_images/) or [Docker Sponsored OSS images](https://docs.docker.com/docker-hub/dsos-program/). For higher availability, Google recommends deploying these Docker Hub or GitHub Container Registry images using an [Artifact Registry remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).

Cloud Run does not support container image layers larger than 9.9 GB when deploying from Docker Hub or an Artifact Registry remote repository with an external registry.

## Deploy worker pools

You can deploy worker pools in the following ways:

  * Deploy a new worker pool
  * Update an existing worker pool
  * Deploy images from other Google Cloud projects
  * Deploy multiple containers (sidecars) to a worker pool



### Deploy a new worker pool

You can specify a container image with a tag (for example, `us-docker.pkg.dev/my-project/container/my-image:latest`) or with an exact digest (for example, `us-docker.pkg.dev/my-project/container/my-image@sha256:41f34ab970ee...`).

Deploying a worker pool for the first time creates its first revision. Note that revisions are immutable. If you deploy from a container image tag, it will be resolved to a digest and the revision will always serve this particular digest.

Follow the instructions, using the Google Cloud console, the Google Cloud CLI, Terraform or REST API:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, and click **Deploy container** to display the **Create worker pool** form.

     1. In the form, specify the container image.

     2. Enter the worker pool name. Worker pool names must be 49 characters or less and must be unique per region and project. You can't share the same name as an _existing service name_ from your project. A worker pool name cannot be changed later and is publicly visible.

     3. Select the region where you want your worker located. The region selector indicates [price tier](https://cloud.google.com/run/pricing) and highlights regions with the [lowest carbon impact](https://cloud.google.com/sustainability/region-carbon#region-picker).

     4. Under **Scaling** , specify the number of instances for the worker pool.

  3. Click **Containers, Networking, Security** to set other optional settings in the appropriate tabs:

     * [Container configuration](https://docs.cloud.google.com/run/docs/configuring/workerpools/containers)
     * [CPU limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/cpu)
     * [Memory limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits)
     * [Environment variables](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables)
     * [Service accounts](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity)
     * Connect to a VPC network for [egress and ingress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-workerpool).
  4. When you are finished configuring your worker pool, click **Create** to deploy the image to Cloud Run and wait for the deployment to finish.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy a worker pool container image:

     1. Run the following command: 
            
            gcloud run worker-pools deploy WORKER_POOL --image IMAGE_URL 

Replace the following:

        * WORKER_POOL: the name of the worker pool you want to deploy to. If the worker pool does not exist yet, this command creates the worker pool during the deployment. You can omit this parameter entirely, but you will be prompted for the worker pool name if you omit it. Worker pool names must be 49 characters or fewer, use a unique name per region and project, and must not share the same name as an _existing service name_ from your project.
        * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`. Note that if you don't supply the `--image` flag, the deploy command attempts to [deploy from source code](https://docs.cloud.google.com/run/docs/workerpools/deploy-source-code).
     2. Wait for the deployment to finish. Upon successful completion, Cloud Run displays a success message along with the revision information about the deployed worker pool.

To deploy to a different location from the one you set using the `run/region` `gcloud` properties, use:
            
            gcloud run worker-pools deploy WORKER_POOL --region REGION




### YAML

You can store your worker pool specification in a `YAML` file and deploy it using the gcloud CLI.

  1. Create a new `worker-pool.yaml` file with the following content:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - image: IMAGE

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.

You can also specify more configuration such as environment variables or memory limits.

  2. Deploy the new worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.



###  REST API 

To deploy a new worker pool, send a `POST` HTTP request to the Cloud Run Admin API worker pools [`create` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/create).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X POST \
      -d '{template: {containers: [{image: "IMAGE_URL"}]}}' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools?workerPoolId=WORKER_POOL

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to deploy services](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * PROJECT_ID: the Google Cloud project ID. 
    * WORKER_POOL: the name of the worker pool.



### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

**Note:** A successful worker pools deployment doesn't indicate a deployment health check was performed or that the runtime container health was validated. To verify that the worker pool container was started and healthy, configure [startup probes and liveness checks](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks), and monitor these checks directly within the [logs](https://docs.cloud.google.com/run/docs/logging#workerpool-logs).

### Deploy a new revision of an existing worker pool

Note that changing configuration settings for a worker pool results in the creation of a new revision, even if there is no change to the container image. Each revision created is immutable.

The container image is imported by Cloud Run when deployed. Cloud Run keeps this copy of the container image as long as it is used by a revision.

Follow these instructions, using Google Cloud console, the Google Cloud CLI, Terraform, or REST API:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, select the worker pool to update, then click **Edit and deploy new revision** to display the **Deploy worker pool revision** form.

     1. If needed, specify the URL to the new container image to be deployed.

     2. [Configure the container](https://docs.cloud.google.com/run/docs/configuring/services/containers) as needed.

     3. If needed, update the number of instances for the worker pool.

  3. If needed, click **Containers, Networking, Security** to set other optional settings in the appropriate tabs:

     * [Container configuration](https://docs.cloud.google.com/run/docs/configuring/workerpools/containers)
     * [CPU limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/cpu)
     * [Memory limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits)
     * [Environment variables](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables)
     * [Service accounts](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity)
     * Connect to a VPC network for [egress and ingress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-workerpool).
  4. When you finish updating your worker pool, click **Deploy**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy a container image:

     1. Run the command: 
            
            gcloud run worker-pools deploy WORKER_POOL --image IMAGE_URL 

Replace the following:

        * WORKER_POOL: the name of the worker pool you want to deploy to. If the worker pool does not exist yet, this command creates the worker pool during the deployment. You can omit this parameter entirely, but you will be prompted for the worker pool name if you omit it. Worker pool names must be 49 characters or fewer, use a unique name per region and project, and must not share the same name as an _existing service name_ from your project.
        * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`. Note that if you don't supply the `--image` flag, the deploy command attempts to [deploy from source code](https://docs.cloud.google.com/run/docs/workerpools/deploy-source-code).

The revision suffix is assigned automatically for new revisions. If you want to supply your own revision suffix, use the gcloud CLI parameter [`--revision-suffix`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--revision-suffix).

     2. Wait for the deployment to finish. Upon successful completion, Cloud Run displays a success message along with the revision information about the deployed worker pool.




### YAML

  1. Download the worker pool [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Make a change to the configuration file.

  3. Update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

Make sure you have set up Terraform as described in the Deploying a new worker pool example.

  1. Make a change to the configuration file.

  2. Apply the Terraform configuration:
         
         terraform apply

Confirm you want to apply the actions described by entering `yes`.




###  REST API 

To deploy a new worker pool, send a `PATCH` HTTP request to the Cloud Run Admin API [worker pools endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/patch).

To create a new revision from the template even if the system doesn't detect any changes from the previously deployed revision, set the query parameter `forceNewRevision` to `true`.

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X PATCH \
      -d '{template: {containers: [{image: "IMAGE_URL"}]}}' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL>?forceNewRevision=true

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to deploy services](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * PROJECT_ID: the Google Cloud project ID.
  * WORKER_POOL: the name of the worker pool you are deploying to.



### Validate configuration with dry run

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can validate your worker pool configuration without deploying it or persisting changes by using the `--dry-run` flag.

When you specify the `--dry-run` flag, the command performs the following actions:

  * Validates the configuration.
  * Bypasses the build process if you are deploying from source.
  * Prints a validation success message.



To validate a deployment of a worker pool:
    
    
    gcloud beta run worker-pools deploy WORKER_POOL \
        --image IMAGE_URL \
        --dry-run

Replace the following:

  * WORKER_POOL: the name of the worker pool you are deploying to.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .



### Deploy images from other Google Cloud projects

To deploy images from other Google Cloud projects, you or your administrator must grant the required IAM roles to the deployer account and the Cloud Run service agent.

For the required roles for the deployer account, see required roles.

To grant the Cloud Run service agent the required roles, see the following instructions:

  1. In the Google Cloud console, open the project for your Cloud Run worker pool.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Copy the email of the Cloud Run [service agent](https://docs.cloud.google.com/iam/docs/service-agents). It has the suffix **@serverless-robot-prod.iam.gserviceaccount.com**

  4. Open the project that owns the container registry you want to use.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  5. Click **Add** to add a new principal.

  6. In the **New principals** field, paste in the email of the service account that you copied earlier.

  7. In the _Select a role_ drop-down menu, if you are using Container Registry, select the role **Storage - > Storage Object Viewer**. If you are using Artifact Registry, select the role **Artifact Registry - > Artifact Registry Reader**.

  8. Deploy the container image to the project that contains your Cloud Run worker pool.

**Note:** For stronger security, [grant access to only the Cloud Storage bucket or Artifact Registry repository that contains your container images](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).



### Deploying images from other registries

To deploy public or private container images that are not stored in Artifact Registry or Docker Hub, or are not public images in GitHub Container Registry, [set up](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) an Artifact Registry [remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview).

Artifact Registry remote repositories allow you to:

  * Deploy any public container image.
  * Deploy container images from private repositories that require authentication, for example, JFrog Artifactory or Nexus.



If using an [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) remote repository is not an option, you can temporarily pull and push container images to Artifact Registry by deploying them to Cloud Run using `docker push`. Cloud Run imports the container image during deployment, and afterwards, you can [delete the image from Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

### Deploy multiple containers (sidecars) to a worker pool

In a Cloud Run deployment with sidecars, there is one main worker pool container and one or more _sidecar_ containers. The sidecars can communicate with each other and with the worker pool container using a localhost port. The localhost port varies depending on the containers you are using.

You can deploy up to 10 containers per instance including the worker pool container. All containers within an instance share the same network namespace and can also share files using an in-memory shared volume.

You can require all deployments to use a specific sidecar by creating [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#require-prefix).

#### Deploy a worker pool with sidecar containers

Follow these instructions, using the Google Cloud CLI, YAML, or Terraform to deploy multiple containers to a Cloud Run worker pool:

###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy multiple containers to a worker pool, run the following command:
         
         gcloud run worker-pools deploy WORKER_POOL \
          --container WORKER_POOL_CONTAINER_NAME \
          --image='WORKER_POOL_IMAGE' \
          --container SIDECAR_CONTAINER_NAME \
          --image='SIDECAR_IMAGE'

Replace the following:

     * WORKER_POOL: the name of the worker pool you are deploying to. If you omit this parameter, you will be prompted for the worker pool name.
     * WORKER_POOL_CONTAINER_NAME: a name for the worker pool container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
     * SIDECAR_CONTAINER_NAME: a name for the sidecar container—for example `sidecar`.
     * `SIDECAR_IMAGE`: a reference to the sidecar container image.

To configure each container in the deploy command, supply each container's configuration after the `container` parameters, for example:
    
    gcloud run worker-pools deploy WORKER_POOL \
      --container CONTAINER_1_NAME \
      --image='WORKER_POOL_IMAGE' \
      --set-env-vars=KEY=VALUE \
      --container SIDECAR_CONTAINER_NAME \
      --image='SIDECAR_IMAGE' \
      --set-env-vars=KEY_N=VALUE_N

**Important:** When you use the `--container` flag, you must specify all non-container-level flags before the container-level flags, otherwise the deploy command fails with an error message to that effect.
  3. Wait for the deployment to finish. Upon successful completion, Cloud Run displays a success message.




### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - name: CONTAINER_NAME
                 image: IMAGE_URL
               containers:
               - name: SIDECAR_CONTAINER_NAME
                 image: SIDECAR_IMAGE_URL

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER_NAME: a name for the worker pool container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * SIDECAR_CONTAINER_NAME: a name for the sidecar container—for example, `sidecar`.
     * SIDECAR_CONTAINER_IMAGE: a reference to the sidecar container image.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          name = "CONTAINER_NAME"
          image = "IMAGE_URL"
        }
        containers {
          name = "SIDECAR_CONTAINER_NAME"
          image = "SIDECAR_IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * CONTAINER_NAME: the name of the container.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * SIDECAR_CONTAINER_NAME: the name of the sidecar container.
  * SIDECAR_IMAGE_URL: a reference to the sidecar container image.



#### Notable features available to deployments with sidecars

You can specify the [container start up order](https://docs.cloud.google.com/run/docs/configuring/workerpools/containers#container-ordering) within a deployment with multiple containers, if you have dependencies that require some containers to start up before other containers in the deployment.

If you have containers that depend on other containers, you must use [healthchecks](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks) in your deployment. When you use healthchecks, Cloud Run follows the container startup order, verifying the health of each container before starting the next container. Without healthchecks, Cloud Run tries to start all containers, even if the containers they depend on are not running yet or failed to start.

Multiple containers within a single instance can access a shared [in-memory volume](https://docs.cloud.google.com/run/docs/configuring/workerpools/in-memory-volume-mounts), which is accessible to each container using mount points that you create.

## What's next

After you deploy a new worker pool, you can do the following:

  * [View worker pool logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitor worker pool performance](https://docs.cloud.google.com/run/docs/monitoring)
  * [Set memory limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits)
  * [Set environment variables](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables)
  * [Manage the worker pool](https://docs.cloud.google.com/run/docs/managing/workerpools)
  * [Manage worker pool revisions](https://docs.cloud.google.com/run/docs/managing/workerpool-revisions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
