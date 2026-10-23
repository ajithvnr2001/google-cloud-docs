---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/secrets/
title: Configure secrets for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:09.271500+00:00
---

# Configure secrets for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure secrets for jobs Stay organized with collections  Save and categorize content based on your preferences. 

Your job might require API keys, passwords, certificates, or other sensitive information for its dependencies. For Cloud Run, Google recommends storing this sensitive information in a secret you create in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs#docs).

Make a secret available to your containers in one of the following ways:

  * When you mount each secret as a volume, Cloud Run makes the secret available to the container as files. When reading a volume, Cloud Run always fetches the secret value from the Secret Manager to use the value with the latest version. This method also works well with secret rotation.
  * Pass a secret using [environment variables](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables). Environment variables are resolved at instance startup time, so if you use this method, Google recommends that you pin the secret to a particular version instead of using `latest` as the version.



For more information, see Secret Manager [best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

## How secrets are checked at deployment and runtime

During job creation, Cloud Run checks all the secrets you use. The check ensures that the service account that runs the container has permission to access these secrets.

During runtime, when instances start up:

  * If the secret is an environment variable, Cloud Run retrieves the value of the secret prior to starting the instance. If the secret retrieval process fails, the instance doesn't start.
  * If you mount the secret as a volume, Cloud Run doesn't perform any checks during instance startup. However, during runtime, if a secret is inaccessible, attempts to read the mounted volume fail.



## Volume ownership

The ownership of a Cloud Run secret volume differs by the execution environment and deployment type.

When you mount a secret volume using the second generation execution environment, which is always the case for job, root owns the volume.

## Before you begin

  1. Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

  2. Use an existing secret or, create a secret in Secret Manager, as described in [ Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).



### Required roles

To get the permissions that you need to configure secrets, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



To allow Cloud Run to access the secret, the [service identity](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity) must have the following role:

  * [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`)



For instructions on how to add the service identity principal to the Secret Manager Secret Accessor role, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Make a secret accessible to Cloud Run

You can make a secret accessible to your job using the Google Cloud console, the Google Cloud CLI, or YAML:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Click **Deploy container** to configure a new job. Fill out the initial job settings page, then click **Containers, Networking, Security** to expand the configuration page.

  3. If you are configuring an existing job, click the job, and click **View and edit job configuration**.

  4. Follow the steps to mount the secret as a volume, or expose the secret as an environment variable.



  * To expose the secret as an environment variable:

    1. Click the **Container(s)** tab.
    2. In the **Variables and Secrets** tab, click **Reference a secret**.
    3. In the **Name 1** field, enter the name of the environment variable.
    4. From the **Secret** list, select the secret you want to use.
    5. From the **Version 1** list, select the version of the secret to reference.
    6. Click **Done**.
    7. Click **Create** or **Deploy**.
  * To mount the secret as a volume:

    1. Click the **Volumes** tab.
    2. Click **Mount volume**.
    3. Click **Secret**.
    4. In the **Mount path** field, enter the mount path for this secret. This is the directory where all versions of your secret are placed.
    5. From the **Secret** list, select the secret you want to use.
    6. In the **Path 1** field, enter the name of the file to mount.
    7. In the **Version 1** list, select the version of the secret to reference. By default, the latest version is selected. You can select a specific version if you want.
    8. Click **Save**.
    9. Click **Create** or **Deploy**.



###  gcloud 

**Note:** You can update multiple secrets at the same time. To do this, separate the configuration options for each secret with a comma.

  * To specify the secret in an environment variable when creating a new job:
        
        gcloud run jobs create JOB_NAME \
        --image IMAGE_URL \
        --set-secrets ENV_VAR_NAME=SECRET_NAME:VERSION

Replace the following:

    * JOB_NAME: the name of your job.
    * ENV_VAR_NAME: the name of the environment variable to use for the secret.
    * SECRET_NAME: the secret name in the same project—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.

You can specify several environment variable/secret pairs, using a comma delimited list.

  * To specify the secret in an environment variable when updating a job:
        
        gcloud run jobs update JOB_NAME \
        --set-secrets ENV_VAR_NAME=SECRET_NAME:VERSION

  * To mount the secret as a volume when creating a job:
        
        gcloud run jobs create JOB_NAME \
        --image IMAGE_URL \
        --set-secrets=PATH=SECRET_NAME:VERSION

Replace the following:

    * JOB_NAME: the name of your job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
    * SECRET_NAME: the secret name in the same project—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  * To update a secret in an existing job:
        
        gcloud run jobs update JOB_NAME \
        --update-secrets=PATH=SECRET_NAME:VERSION




### YAML

Due to constraints around API compatibility, the secret locations must be stored in an annotation.

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. For secrets exposed as environment variables:
         
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
                   - env:
                     - name: SECRET_NAME
                       valueFrom:
                         secretKeyRef:
                           key: VERSION
                           name: SECRET_LOOKUP_NAME
                     image: IMAGE_URL 

Replace the following:

     * JOB: the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`. It can be the same as SECRET_NAME.
  3. For secrets mounted as file paths:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB_NAME
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     volumeMounts:
                     - mountPath: MOUNT_PATH
                       name: VOLUME_NAME
                   volumes:
                   - name: VOLUME_NAME
                     secret:
                       items:
                       - key: VERSION
                         path: FILENAME
                       secretName: SECRET_LOOKUP_NAME

Replace the following:

     * JOB_NAME: the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`. It can be the same as SECRET_NAME.
     * VOLUME_NAME: any name—for example, `my-volume`. It can be the same as SECRET_NAME.



### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  


**For secrets exposed as environment variables:**
    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "IMAGE_URL"
    
            env {
              name = "SECRET_NAME"
    
              value_source {
                secret_key_ref {
                  secret = "SECRET_NAME"
                  version = "VERSION"
                }
              }
            }
          }
        }
      }
    }
    
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * SECRET_NAME: the secret name—for example, `mysecret`.
  * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



**For secrets mounted as file paths:**
    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "IMAGE_URL"
    
            volume_mounts {
              name       = "VOLUME_NAME"
              mount_path = "MOUNT_PATH"
            }
          }
    
          volumes {
            name = "VOLUME_NAME"
            secret {
              secret = "SECRET_NAME"
            }
          }
        }
      }
    }
    
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * VOLUME_NAME: any name—for example, `my-volume`. It can be the same as `SECRET_NAME`.
  * MOUNT_PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
  * SECRET_NAME: the secret name—for example, `mysecret`.



#### Reference secrets from other projects

You can reference a secret from another project, if your project's service account has been allowed to access the secret.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Click **Deploy container** to configure a new job. Fill out the initial job settings page, then click **Containers, Networking, Security** to expand the configuration page.

  3. If you are configuring an existing job, click the job, and click **View and edit job configuration**.

  4. Follow the steps to mount the secret as a volume, or expose the secret as an environment variable.



  * To expose the secret as an environment variable:

    1. Click the **Container(s)** tab.
    2. In the **Variables and Secrets** tab, click **Reference a secret**.
    3. In the **Name 1** field, enter the name of the environment variable.
    4. From the **Secret** list, click **Enter secret manually**.
    5. Enter the secret's resource ID in the following format:
           
           projects/PROJECT_NUMBER/secrets/SECRET_NAME
           

Replace the following:

       * PROJECT_NUMBER with your Google Cloud project number. For detailed instructions on how to find your project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

       * SECRET_NAME: The name of the secret in Secret Manager.

    6. From the **Version 1** list, select the version of the secret to reference.

    7. Click **Done**.

    8. Click **Create** or **Deploy**.

  * To mount the secret as a volume:

    1. Click the **Volumes** tab.
    2. Click **Mount volume**.
    3. Click **Secret**.
    4. In the **Mount path** field, enter the mount path for this secret. This is the directory where all versions of your secret are placed.
    5. From the **Secret** list, click **Enter secret manually**.
    6. Enter the secret's resource ID in the following format:
           
           projects/PROJECT_NUMBER/secrets/SECRET_NAME
           

Replace the following:

       * PROJECT_NUMBER with your Google Cloud project number. For detailed instructions on how to find your project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

       * SECRET_NAME: The name of the secret in Secret Manager.

    7. In the **Path 1** field, enter the name of the file to mount.

    8. In the **Version 1** list, select the version of the secret to reference. By default, the latest version is selected. You can select a specific version if you want.

    9. Click **Save**.

    10. Click **Create** or **Deploy**.




###  gcloud 

  * To mount a secret as a volume when updating a job:
        
        gcloud run jobs update JOB_NAME \
        --image IMAGE_URL \
        --update-secrets=PATH=projects/PROJECT_NUMBER/secrets/SECRET_NAME:VERSION

    * JOB_NAME: the name of your job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
    * PROJECT_NUMBER: the project number for the project the secret was created in.
    * SECRET_NAME: the secret name—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml




Due to constraints around API compatibility, the secret locations must be stored in an annotation.

  1. For secrets exposed as environment variables:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/secrets: SECRET_LOOKUP_NAME:projects/PROJECT_NUMBER/secrets/SECRET_NAME
             spec:
               template:
                 spec:
                   containers:
                   - env:
                     - name: SECRET_NAME
                       valueFrom:
                         secretKeyRef:
                           key: VERSION
                           name: SECRET_LOOKUP_NAME
                     image: IMAGE_URL 

Replace the following:

     * JOB: the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`. It can be the same as SECRET_NAME.
  2. For secrets mounted as file paths:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB_NAME
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/secrets: SECRET_LOOKUP_NAME:projects/PROJECT_NUMBER/secrets/SECRET_NAME
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     volumeMounts:
                     - mountPath: MOUNT_PATH
                       name: VOLUME_NAME
                   volumes:
                   - name: VOLUME_NAME
                     secret:
                       items:
                       - key: VERSION
                         path: FILENAME
                       secretName: SECRET_LOOKUP_NAME

Replace the following:

     * JOB_NAME: the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`, it can be the same as SECRET_NAME.
     * VOLUME_NAME: any name—for example, `my-volume`, it can be the same as SECRET_NAME.



### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  


**For secrets exposed as environment variables:**
    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "IMAGE_URL"
            env {
              name = "SECRET_NAME"
              value_source {
                secret_key_ref {
                  secret = "projects/PROJECT_ID/secrets/SECRET_NAME"
                  version = "VERSION"
                }
              }
            }
          }
        }
      }
    }
    
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * SECRET_NAME: the secret name—for example, `mysecret`.
  * PROJECT_ID: the project ID the secret was created in.
  * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



**For secrets mounted as file paths:**
    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "IMAGE_URL"
    
            volume_mounts {
              name       = "VOLUME_NAME"
              mount_path = "MOUNT_PATH"
            }
          }
    
          volumes {
            name = "VOLUME_NAME"
            secret {
              secret = "projects/PROJECT_ID/secrets/SECRET_NAME"
            }
          }
        }
      }
    }
    
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * VOLUME_NAME: any name—for example, `my-volume`, it can be the same as `SECRET_NAME`.
  * MOUNT_PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example, `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
  * PROJECT_ID: the project ID the secret was created in.
  * SECRET_NAME: the secret name—for example, `mysecret`.



## View secrets settings

To view the current secrets settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the secrets setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the secrets setting in the returned configuration.




## Limitations

The following sections describe the limitations that apply to mounting secrets.

### Disallowed paths

  * Cloud Run doesn't allow you to mount secrets at `/dev`, `/proc` and `/sys`, or on their subdirectories. 
  * Cloud Run doesn't allow you to mount multiple secrets at the same path because two volume mounts can't be mounted at the same location.



### Regional secrets

Cloud Run does not support [regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret).

### Overriding a directory

If the secret is mounted as a volume in Cloud Run, and the last directory in the volume mount path already exists, then any files or folders in the existing directory become inaccessible.

For example, if a secret called `my-secret` is mounted to path `/etc/app_data`, all the contents inside the `app_data` directory will be overwritten, and the only visible file is `/etc/app_data/my-secret`.

To avoid overwriting files in an existing directory, create a new directory for mounting the secret, for example, `/etc/app_data/secrets`, so that the mount path for the secret is `/etc/app_data/secrets/my-secret`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
