---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying/
title: Deploying container images \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:08.901826+00:00
---

# Deploying container images  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Deploying container images Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy new services and new revisions to Knative serving.

## Before you begin

To use the Google Cloud CLI, you must first [setup and configured the command-line tools](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools).

## Connecting to GKE clusters

Before you can deploy services to Knative serving, you need to log in to connect to your GKE cluster.

For more information about connecting to your GKE clusters, including additional options, see:

  * [Logging in from the Google Cloud console](https://docs.cloud.google.com/anthos/fleet-management/docs/console).
  * [Logging in from the command line](https://docs.cloud.google.com/anthos/fleet-management/docs/command-line).



### Permissions required to deploy

You need permissions to create, update, and delete on the apiGroup `serving.knative.dev` and kind `Service`, and in addition you must have ONE of the following Identity and Access Management roles:

  * [_Owner_](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
  * [_Editor_](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
  * [_Kubernetes Engine Admin_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles)
  * [_Kubernetes Engine Developer_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles)



## Images you can deploy

There is no size limit that applies to the container image you can deploy.

You can use containers from any container registry, such as [Docker Hub](https://hub.docker.com/). For information on deploying private images from registries different from Container Registry or Artifact Registry, see Deploying private container images from other container registries.

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

## Deploying a new service

You can specify a container image with a tag (for example, `gcr.io/my-project/my-image:latest`) or with an exact digest (for example, `gcr.io/my-project/my-image@sha256:41f34ab970ee...`).

Deploying to a service for the first time creates its first revision. Note that revisions are immutable. If you deploy from a container image tag, it will be resolved to a digest and the revision will always serve this particular digest.

You can deploy a container using the Google Cloud console, the Google Cloud CLI or from a YAML configuration file.

Click the tab for instructions using the tool of your choice.

### Default `gcloud` location configuration

If you previously configured a location in the [`default` configuration](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup#configuring_default_settings_for_the) of Google Cloud CLI, your `gcloud` commands use those values by default, including:

  * `compute/region`
  * `compute/zone`
  * `run/cluster`
  * `run/cluster_location`
  * `run/platform`
  * `run/region`



Run the following [`gcloud` config](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/describe) command to view your settings for the `default` configuration:
    
    
    gcloud config configurations describe default
    

OK

### Console

To deploy a container image:

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create service** to display the _Create service_ page.

In the form:

     1. From the dropdown menu, select one of the available GKE clusters for your service.

     2. Enter the desired service name. Service names must be unique per region and project or per cluster. A service name cannot be changed later.

     3. Under _Connectivity_ :

        * Select **Internal** if you want to restrict access only to other Knative serving services or services in your cluster that use Istio.
        * Select **External** to allow external access to your service

Note that you can change the connectivity option at any time, as described in [Changing service connectivity settings](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/services#connectivity).

     4. Click **Next** to continue to the second page of the service creation form.

In the form:

        1. In the _Container image URL_ textbox, supply the URL of an image from a supported registry, for example: `us-docker.pkg.dev/cloudrun/container/hello:latest`

        2. Optionally, click **Show Advanced Settings** and the subsequent tabs to set:

           * [Container configuration](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers)
           * [Concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency)
           * [Request timeout](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/request-timeout)
           * [CPU allocation](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/cpu)
           * [Memory limits](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits)
           * [Maximum instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances)
           * [Environment variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables)
        3. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.

You have just deployed a service to a Knative serving enabled cluster.




### Command line

To deploy a container image:

  1. Run the [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) command:
         
         gcloud run deploy SERVICE --image IMAGE_URL

     * Replace SERVICE with the name of the service to which you want to deploy. If the specified service does not exist, a new service is created.

     * Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.

     * Additional deployment options:

       * To deploy to a namespace other than the [default](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-organizing-with-namespaces), you must specify that namespace using the [`--namespace`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--namespace) parameter.

       * To deploy to a location other than the default configuration, you must specify the `name` and `location` of the cluster with the `--cluster` and `--cluster-location` parameters:
             
             gcloud run deploy SERVICE --cluster CLUSTER-NAME --cluster-location CLUSTER-LOCATION

       * You can set connectivity options with the `--connectivity` flag as described in [Changing service connectivity settings](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/services#connectivity) to specify internal or external access.

       * For Knative serving on VMware, you must include the `--kubeconfig` parameter and specify your configuration file:
             
             gcloud run deploy SERVICE --image IMAGE_URL --kubeconfig KUBECONFIG-FILE

  2. Wait for the deployment to finish. Upon successful completion, a success message is displayed along with the URL of the deployed service.




### YAML

You can store your service specification in a `YAML` file and then deploy it using the Google Cloud CLI.

  1. Create a new `service.yaml` file with this content:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               containers:
               - image: IMAGE

Replace

     * SERVICE with the name of your Knative serving service
     * IMAGE with the URL of your container image.

You can also [specify more configuration](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits) such as environment variables or memory limits.

  2. Deploy the new service using the following command:
         
         gcloud run services replace service.yaml




## Deploying a new revision of an existing service

You can deploy a new revision using the Google Cloud console, the `gcloud` command line, or a YAML configuration file.

Note that changing any configuration settings results in the creation of a new revision, even if there is no change to the container image. Each revision created is immutable.

Click the tab for instructions using the tool of your choice.

### Console

To deploy a new revision of an existing service:

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service you want to update in the services list, and click on it to open the details of that service.

  3. Click **EDIT & DEPLOY NEW REVISION**. This displays the revision deployment form:

  4. If needed, supply the URL to the new container image you want to deploy.

  5. Optionally, set:

     * [Container configuration](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers)
     * [Concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency)
     * [Request timeout](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/request-timeout)
     * [CPU allocation](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/cpu)
     * [Memory limits](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits)
     * [Maximum instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances)
     * [Environment variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables)
  6. To send all traffic to the new revision, check the checkbox labelled _Serve this revision immediately_. To gradually roll out a new revision, uncheck that checkbox: this will result in a deployment where no traffic is sent to the new revision--follow the instructions for [gradual rollouts](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration#gradual) after you deploy.

  7. Click **DEPLOY** and wait for the deployment to finish.




### Command line

To deploy a container image:

  1. Run the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command:
         
         gcloud run services update SERVICE --image IMAGE_URL

     * A revision suffix is automatically assigned for each revision. If you want to specify your own revision suffix, add the [\--revision-suffix](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--revision-suffix) parameter.

     * Replace SERVICE with the name of the service to which you want to deploy. If the specified service does not exist, a new service is created.

     * Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.

     * Additional deployment options:

       * To deploy to a namespace other than the [default](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-organizing-with-namespaces), you must specify that namespace using the [`--namespace`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--namespace) parameter.

       * To deploy to a location other than the default configuration, you must specify the `name` and `location` of the cluster with the `--cluster` and `--cluster-location` parameters:
             
             gcloud run deploy SERVICE --cluster CLUSTER-NAME --cluster-location CLUSTER-LOCATION

       * You can set connectivity options with the `--connectivity` flag as described in [Changing service connectivity settings](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/services#connectivity) to specify internal or external access.

       * For Knative serving on VMware, you must include the `--kubeconfig` parameter and specify your configuration file:
             
             gcloud run deploy SERVICE --image IMAGE_URL --kubeconfig KUBECONFIG-FILE

  2. Wait for the deployment to finish. Upon successful completion, a success message is displayed along with the URL of the deployed service.




### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

     1. In your local file, update the [revision settings](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions) in any child attribute of the `spec.template`.

     2. Deploy the new revision:
            
            gcloud run services replace service.yaml




## Deploying images from other Google Cloud projects

You can deploy container images from other Google Cloud projects if you set the correct IAM permissions:

  1. In the Google Cloud console console, open the project for your Knative serving service.

  2. [Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  3. Obtain your service account info:

     * For clusters on Google Cloud, copy the email of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_default_service_account). It has the suffix **@developer.gserviceaccount.com**

     * For other clusters, create a Google Cloud service account and [download the credentials](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys). Add these credentials as the [default `imagePullSecrets` of the Kubernetes Service Account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account).

  4. Open the project that owns the container registry you want to use.

  5. [Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  6. Click **Add** to add a new principal.

  7. In the **New principals** text box, paste in the email of the service account that you copied earlier.

  8. In the _Select a role_ dropdown list, select the role to read from the registry:

     * Artifact Registry, including [gcr.io repositories in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo): **Artifact Registry - > Artifact Registry Reader**
     * Container Registry: **Storage - > Storage Object Viewer**
  9. Deploy the container image to the project that contains your Knative serving service.




For stronger security, you can limit grant access:

  * Artifact Registry: Grant the role on the [repository](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant-repo) that stores your container images.
  * Container Registry: Grant the role on the [Cloud Storage bucket](https://docs.cloud.google.com/container-registry/docs/access-control#granting_users_and_other_projects_access_to_a_registry) that stores your container images.



## Deploying private container images from other container registries

This section describes setting up correct permissions to deploy container images from an arbitrary private registry to Knative serving. A private container registry requires credentials to access the container image. Note that you do not need to follow these steps to deploy private container images from Container Registry ([Deprecated](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)) or Artifact Registry in the same project as your cluster.

To be able to deploy a private container image, you must create an `imagePullSecret` type Kubernetes secret and associate it with a service account:

  1. Create an `imagePullSecret` secret called `container-registry`:
         
         kubectl create secret docker-registry container-registry \
           --docker-server=DOCKER_REGISTRY_SERVER \
           --docker-email=REGISTRY_EMAIL \
           --docker-username=REGISTRY_USER \
           --docker-password=REGISTRY_PASSWORD

     * Replace DOCKER_REGISTRY_SERVER with your private registry FQDN (ex: <https://gcr.io/> for Container Registry or <https://hub.docker.com> for DockerHub).
     * Replace REGISTRY_EMAIL with your email.
     * Replace REGISTRY_USER with your container registry username.

If you're using Container Registry or Artifact Registry and would like to store and pull long-lived credentials instead of passing short-lived access tokens, see [Authentication methods: JSON key file](https://docs.cloud.google.com/container-registry/docs/advanced-authentication#json_key_file).

     * Replace REGISTRY_PASSWORD with your container registry password.

  2. Open your default service account:
         
         kubectl edit serviceaccount default --namespace default

Every [namespace](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-organizing-with-namespaces) in your Kubernetes cluster has a default service account called `default`. This default service account is used to pull your container image unless otherwise specified when you [deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--service-account) your Knative serving service.

  3. Add the newly created `imagePullSecret` secret to your default service account:
         
         imagePullSecrets:
         - name: container-registry
         

Your service account should now look like this:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: default
           namespace: default
           ...
         secrets:
         - name: default-token-zd84v
         # The secret we just created:
         imagePullSecrets:
         - name: container-registry
         




Now, any new pods created in the current `default` namespace will have the `imagePullSecret` secret defined.

## Deploying with automatic sidecar injection enabled

To deploy your service with Istio sidecar injection enabled, see [automatic sidecar injection enabled](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-workloads#enabling_automatic_sidecar_injection) in the Cloud Service Mesh documentation.

## Deploying services on an internal network

To deploy services on an internal network, you must [set up a private, internal network](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup#setting_up_a_private_internal_network).

## What's next

After you deploy a new service, you can do the following:

  * [Gradual rollouts, rollback revisions, traffic migration](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration)
  * [View service logs](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging)
  * [Monitor service performances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/monitoring)
  * [Configure your services](https://docs.cloud.google.com/anthos/run/docs/how-to#configure). For example, set memory limits, set environment variables, or change concurrency.
  * Manage: 
    * [Services](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/services)
    * [Revisions](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions)



You can automate the builds and deployments of your Knative serving services using Cloud Build Triggers:

  * [Set up Continuous Deployment](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/continuous-deployment-with-cloud-build)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
