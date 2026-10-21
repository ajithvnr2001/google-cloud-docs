---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/containers/
title: Configure containers for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:49.445526+00:00
---

# Configure containers for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure containers for jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the entrypoint command, and arguments for a Cloud Run job.

When Cloud Run starts a container, it runs the image's default entrypoint command and default command arguments. If you want to override the image's default entrypoint and command arguments, you can use the `command` and `args` fields in the container configuration. The `command` field specifies the actual command run by the container. The `args` field specifies the arguments passed to that command.

Note that you can have a maximum of 1000 arguments per container for each job.

This page shows you how to configure the command, arguments, and start order for containers in your Cloud Run jobs.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure entrypoint and arguments

You can configure command entrypoint and arguments for jobs using the Google Cloud console, the gcloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. Specify the command you want the container to run, if not the command defined in your container.

  5. Optional: Specify the arguments to the entrypoint command.

  6. Click **Create** or **Update**.




###  gcloud 

  * [To set the start command and arguments](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) for a new job, run the following command:
        
        gcloud run jobs create JOB --image IMAGE_URL --command COMMAND --args ARG1,ARG_N

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `COMMAND`: the command that the container is to start with if you are not using the default command.
    * `ARG1`: the argument you are sending to the container command. For more than one argument, use a comma-separated list, for example, `--args="arg1", "arg2", "arg3"`. If your arguments contain commas or special characters, see Use equals signs or commas in arguments.
  * To [update command and args](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
        
        gcloud run jobs update JOB --command COMMAND --args ARG1,ARG_N 

  * To clear any entrypoint commands and arguments, run the following command:
        
        gcloud run jobs update JOB --command "" --args "" 




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `args:` and `command` attributes:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     args:
                     - ARG1'
                     - ARG_N
                     command:
                     - COMMAND
                     

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `ARG1`: the argument you are sending to the container command. Optionally specify additional arguments each in a separate line. If your arguments contain commas or special characters, see Use equals signs or commas in arguments.
     * `COMMAND`: the command that the container is to start with if you are not using the default command.
  3. Update the existing job configuration:
         
         gcloud run jobs replace job.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
     name     = "JOB"
     location = "REGION"
    
     template {
       template {
         containers {
           image = "us-docker.pkg.dev/cloudrun/container/job"
           command = ["COMMAND"]
           args = ["ARG1", "ARG_N"]
         }
       }
     }
    }
    

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `REGION`: the Google Cloud region. For example, `europe-west1`.
  * `COMMAND`: the command that the container is to start with if you are not using the default command.
  * `ARG1`: the argument you are sending to the container command. Optionally, specify additional arguments. If your arguments contain commas or special characters, see Use equals signs or commas in arguments.



### Use equals signs or commas in arguments

If you use equal signs in your arguments, supply these using the following format:
    
    
    gcloud run deploy  \
      --args="--repo-allowlist=github.com/example/example_demo"
    

If your arguments use commas, refer to [configuring environment variables](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables#setting) for details on escaping those.

## Set a working directory

The working directory is where the container executes its commands and arguments. You can specify a custom working directory for the container process during deployment of a new or existing service. If not specified, the container image's default working directory is used. To reset this field to its default, pass an empty string or remove the field.

You can set a working directory using the gcloud CLI, YAML, or Terraform:

###  gcloud 

To [update the working directory](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
    
    
    gcloud run jobs update JOB --workdir WORKING_DIR

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `WORKING_DIR`: container's working directory. If not specified, the container image's default is used. To reset this field to its default, pass an empty string `""`.



To specify the working directory when [creating a job](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create), run the following command:
    
    
    gcloud run jobs create JOB --image IMAGE_URL --workdir WORKING_DIR

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * `WORKING_DIR`: container's working directory. If it is not specified, the container image's default is used. To reset this field to its default, pass an empty string `""`.



### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `workingDir:` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
          name: JOB
         spec:
          template:
            spec:
              template:
                spec:
                  containers:
                  - image: IMAGE_URL
                    workingDir: WORKING_DIR
                    

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `WORKING_DIR` (Optional): container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.
  3. Update the existing job configuration:
         
         gcloud run jobs replace job.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
     name     = "JOB"
     location = "REGION"
    
     template {
       template {
         containers {
           image = "us-docker.pkg.dev/cloudrun/container/job"
           working_dir = WORKING_DIR
         }
       }
     }
    }
    

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `REGION`: the Google Cloud region. For example, `europe-west1`.
  * `WORKING_DIR` (Optional): container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.



## Configure the container start order for sidecar deployments

To specify container start order in a [sidecar deployment](https://docs.cloud.google.com/run/docs/create-jobs#sidecars), you use the container dependencies feature. You specify any containers that have dependencies and list the containers they depend on. The containers that don't have any dependencies are always started first and concurrently.

You can use the Google Cloud console, the gcloud CLI, or YAML to specify the startup order:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. If you are creating a new job, follow these steps:

     1. Click **Deploy container**.
     2. Specify the job name, job container URL, region, and number of tasks.
     3. Click **Containers, Networking, Security** to expand the section.
     4. Configure the main job container.
     5. To add each sidecar container you are deploying, click **Add container**.
     6. If a container depends on other containers, use the **Container startup order** menu to select the containers that Cloud Run must start before the current container.
  3. If you are configuring an existing job, follow these steps:

     1. Select the job you want to update.
     2. Click **View and edit job configuration**.
     3. Click **Containers, Connections, Security** to expand the section.
     4. If a container depends on other containers, use the **Container startup order** menu to select the those containers.
  4. Finish any other required configurations, then click **Create** for a new job or **Update** for an existing job. Wait for the deployment to finish.




###  gcloud 

To deploy multiple containers to a job with a specified startup order, run the command:
    
    
      gcloud beta run create JOB \
          --container CONTAINER_1_NAME --image='JOB_IMAGE' \
          --container CONTAINER_2_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME \
          --container CONTAINER_3_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAMECONTAINER_2_NAME
    

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `CONTAINER_1_NAME`: a name for the main job container.
  * `JOB_IMAGE`: a reference to the main job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * `CONTAINER_2_NAME`: a name for the sidecar container, for example `sidecar`.
  * `SIDECAR_IMAGE`: a reference to the sidecar container image.

If you want to configure each container in the deploy command, supply each container's configuration after the `container` parameters.




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `container-dependencies` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           annotations:
             run.googleapis.com/launch-stage: BETA
           name: JOB
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/container-dependencies: '{"CONTAINER1":["CONTAINER2"], "CONTAINER3":["CONTAINER1","CONTAINER2"]}'
         

Replace the following:

     * `CONTAINER1`: the name of the first container that depends on one or more container. Note that you can set the container name in the YAML: Cloud Run will automatically generate a name if one isn't specified.
     * `CONTAINER2`: the name of the container that must be started before CONTAINER1.
     * `CONTAINER3`: the name of the second container that depends on one or more containers.

In the example shown in the YAML snippet, CONTAINER2 is started first, CONTAINER1 is started second, and CONTAINER3 is started last.

  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




## View container settings

To view the current container settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the container setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the container setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
