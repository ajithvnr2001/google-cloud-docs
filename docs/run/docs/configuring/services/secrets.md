---
url: https://docs.cloud.google.com/run/docs/configuring/services/secrets/
title: Configure secrets for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:21.835165+00:00
---

# Configure secrets for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure secrets for services Stay organized with collections  Save and categorize content based on your preferences. 

Your service might require API keys, passwords, certificates, or other sensitive information for its dependencies. For Cloud Run, Google recommends storing this sensitive information in a secret you create in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs#docs).

Make a secret available to your containers in one of the following ways:

  * When you mount each secret as a volume, Cloud Run makes the secret available to the container as files. When reading a volume, Cloud Run always fetches the secret value from the Secret Manager to use the value with the latest version. This method also works well with secret rotation.
  * Pass a secret using [environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables). Environment variables are resolved at instance startup time, so if you use this method, Google recommends that you pin the secret to a particular version instead of using `latest` as the version.



For more information, see Secret Manager [best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

## How secrets are checked at deployment and runtime

During service deployment, Cloud Run checks all the secrets you use. The check ensures that the service account that runs the container has permission to access these secrets.

During runtime, when instances start up:

  * If the secret is an environment variable, Cloud Run retrieves the value of the secret prior to starting the instance. If the secret retrieval process fails, the instance doesn't start.
  * If you mount the secret as a volume, Cloud Run doesn't perform any checks during instance startup. However, during runtime, if a secret is inaccessible, attempts to read the mounted volume fail.



## Volume ownership

The ownership of a Cloud Run secret volume differs by the execution environment and deployment type.

When you mount a secret volume, the identity owning the files and directories differs depending on the workload's execution environment and on whether the deployment consists of one or multiple containers.

In the first generation execution environment where you are deploying a single container, the identity you use for the container owns the secret volume. In all other cases, root owns the volume. This includes:

  * First generation execution environment where you are deploying multiple containers
  * The second generation environment



## Before you begin

  1. Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

  2. Use an existing secret or, create a secret in Secret Manager, as described in [ Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).



### Required roles

To get the permissions that you need to configure secrets, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



To allow Cloud Run to access the secret, the [service identity](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) must have the following role:

  * [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`)



For instructions on how to add the service identity principal to the Secret Manager Secret Accessor role, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Make a secret accessible to Cloud Run

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can make a secret accessible to your service using the Google Cloud console, the Google Cloud CLI, or a YAML file when you deploy a new [service](https://docs.cloud.google.com/run/docs/deploying#service) or update an existing service, and deploy a [revision](https://docs.cloud.google.com/run/docs/deploying#revision). Click the tab of your choice:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. If you are configuring a new service, click **Deploy container**. Fill out the initial service settings page, then click **Containers, Networking, Security** to expand the service configuration page.

  3. If you are configuring an existing service, click the service.

  4. Follow the steps to mount the secret as a volume, or expose the secret as an environment variable. 

     * To expose the secret as an environment variable:

       1. Click the **Containers** tab.
       2. Under **Variables and Secrets** , click **Reference a secret**.
       3. In the **Name 1** field, enter the name of the environment variable.
       4. From the **Secret** list, select the secret you want to use.
       5. From the **Version 1** list, select the version of the secret to reference.
       6. Click **Done**.
       7. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.
     * To mount the secret as a volume:

       1. If you are configuring a new service, click the **Volumes** tab. If you are configuring an existing service, click the **Containers** tab.
       2. Click **Mount volume**.
       3. Click **Secret**.
       4. In the **Mount path** field, enter the mount path for this secret. This is the directory where all versions of your secret are placed.
       5. From the **Secret** list, select the secret you want to use.
       6. In the **Path 1** field, enter the name of the file to mount.
       7. In the **Version 1** list, select the version of the secret to reference. By default, the latest version is selected. You can select a specific version if you want.
       8. Click **Save**.
       9. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.



###  gcloud 

To make a secret accessible to your service, enter one of the following commands.

  * To mount the secret as a volume when deploying a service:
        
        gcloud run deploy SERVICE --image IMAGE_URL  \
        --update-secrets=PATH=SECRET_NAME:VERSION

Replace the following:

    * SERVICE: the name of your service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
    * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example: `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
    * SECRET_NAME: the secret name in the same project—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  * To expose the secret as an environment variable when deploying a service:
        
        gcloud run deploy SERVICE \
        --image IMAGE_URL \
        --update-secrets=ENV_VAR_NAME=SECRET_NAME:VERSION

Replace the following:

    * SERVICE: the name of your service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
    * ENV_VAR_NAME: the name of the environment variable you want to use with the secret.
    * SECRET_NAME: the secret name in the same project—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  * You can update multiple secrets at the same time. To do this, separate the configuration options for each secret with a comma. The following command updates one secret mounted as a volume and another secret exposed as an environment variable.

To update existing secrets, enter the following command:
        
        gcloud run deploy SERVICE --image IMAGE_URL \
        --update-secrets=PATH=SECRET_NAME:VERSION,ENV_VAR_NAME=SECRET_NAME:VERSION

  * To clear existing secrets and make a new secret accessible to the service, use the `--set-secrets` flag:
        
        gcloud run services update SERVICE \
        --set-secrets="ENV_VAR_NAME=SECRET_NAME:VERSION"




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. For secrets exposed as environment variables, under `env`, update the ENV_VAR, VERSION, and/or SECRET_NAME as desired. If you have multiple secrets mounted as environment variables, you will have multiples of these attributes.
         
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
                 env:
                 - name: ENV_VAR
                   valueFrom:
                     secretKeyRef:
                       key: VERSION
                       name: SECRET_NAME

  3. For secrets mounted as file paths, update the MOUNT_PATH, VOLUME_NAME, VERSION, FILENAME, and/or SECRET_NAME as desired. If you have multiple secrets mounted as file paths, you will have multiples of these attributes.
         
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
                 volumeMounts:
                 - mountPath: MOUNT_PATH
                   name: VOLUME_NAME
               volumes:
               - name: VOLUME_NAME
                 secret:
                   items:
                   - key: VERSION
                     path: FILENAME
                   secretName: SECRET_NAME

Note that `VOLUME_NAME` can be set to any name.

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  4. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

  1. Create a secret and a secret version.
         
         resource "google_secret_manager_secret" "default" {
           secret_id = "my-secret"
           replication {
             auto {}
           }
         }
         
         resource "google_secret_manager_secret_version" "default" {
           secret      = google_secret_manager_secret.default.name
           secret_data = "this is secret data"
         }

  2. Create a service account and grant it access to the secret:
         
         resource "google_service_account" "default" {
           account_id   = "cloud-run-service-account"
           display_name = "Service account for Cloud Run"
         }
         
         resource "google_secret_manager_secret_iam_member" "default" {
           secret_id = google_secret_manager_secret.default.id
           role      = "roles/secretmanager.secretAccessor"
           # Grant the new deployed service account access to this secret.
           member     = "serviceAccount:${google_service_account.default.email}"
           depends_on = [google_secret_manager_secret.default]
         }

  3. Secret Manager secrets can be accessed from Cloud Run as mounted file paths or as environment variables.

     1. For secrets mounted as file paths, reference the Secret Manager resource in the `volumes` parameter. The `name` corresponds with an entry in the `volume_mounts` parameter:
            
            resource "google_cloud_run_v2_service" "mounted_secret" {
              name     = "service-with-mounted-secret"
              location = "us-central1"
              ingress  = "INGRESS_TRAFFIC_ALL"
            
              deletion_protection = false # set to "true" in production
            
              template {
                volumes {
                  name = "my-service-volume"
                  secret {
                    secret = google_secret_manager_secret.default.secret_id
                    items {
                      version = "latest"
                      path    = "my-secret"
                      mode    = 0 # use default 0444
                    }
                  }
                }
                containers {
                  image = "us-docker.pkg.dev/cloudrun/container/hello"
                  volume_mounts {
                    name       = "my-service-volume"
                    mount_path = "/secrets"
                  }
                }
                service_account = google_service_account.default.email
              }
              depends_on = [google_secret_manager_secret_version.default]
            }

     2. For secrets exposed as environment variables, reference the Secret Manager resource in the `env` parameter:
            
            resource "google_cloud_run_v2_service" "env_variable_secret" {
              name     = "service-with-env-var-secret"
              location = "us-central1"
              ingress  = "INGRESS_TRAFFIC_ALL"
            
              deletion_protection = false # set to "true" in production
            
              template {
                containers {
                  image = "us-docker.pkg.dev/cloudrun/container/hello"
                  env {
                    name = "MY_SECRET"
                    value_source {
                      secret_key_ref {
                        secret  = google_secret_manager_secret.default.secret_id
                        version = "latest"
                      }
                    }
                  }
                }
                service_account = google_service_account.default.email
              }
              depends_on = [google_secret_manager_secret_version.default]
            }




### Compose

To specify secrets in your `compose.yaml` file, add the `secrets` attribute to your service definition. Doing so creates a Secret Manager secret to store this data based on the value in the local file.
    
    
      services:
        web:
          image: IMAGE
          secrets:
            - SECRET_NAME
      secrets:
        SECRET_NAME:
          file: SECRET_FILE_PATH

Replace the following:

  * IMAGE: the URL of your container image.
  * SECRET_NAME: the secret name, for example, `mysecret`.
  * SECRET_FILE_PATH: the path to the local file containing the secret value.



**Deploy the service**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

#### Reference secrets from other projects

To reference a secret from another project, verify that your project's service account has access to the secret.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. If you are configuring a new service, click **Deploy container**. Fill out the initial service settings page, then click **Containers, Networking, Security** to expand the service configuration page.

  3. If you are configuring an existing service, click the service.

  4. Follow the steps to mount the secret as a volume, or expose the secret as an environment variable. 

     * To expose the secret as an environment variable:

       1. If you are configuring an existing service, click the **Containers** tab. If you are creating a new service, click to expand **Containers, Networking, Security**.
       2. Under **Variables and Secrets** , click **Reference a secret**.
       3. In the **Name 1** field, enter the name of the environment variable.
       4. From the **Secret** list, click **Enter secret manually**.
       5. Enter the secret's resource ID in the following format:
              
              projects/PROJECT_NUMBER/secrets/SECRET_NAME
              

Replace the following:

          * PROJECT_NUMBER with your Google Cloud project number. For detailed instructions on how to find your project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

          * SECRET_NAME: The name of the secret in Secret Manager.

       6. From the **Version 1** list, select the version of the secret to reference.

       7. Click **Done**.

       8. Click **View diff & redeploy**, then **Deploy changes**.

     * To mount the secret as a volume:

       1. If you are configuring an existing service, click the **Containers** tab. If you are creating a new service, click the **Volumes** tab under Containers, Networking, Security.
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

       10. Click **View diff & redeploy**, then **Deploy changes**.




###  gcloud 

  * To mount a secret as a volume when deploying a service:
        
        gcloud run deploy SERVICE --image IMAGE_URL  \
        --update-secrets=PATH=projects/PROJECT_NUMBER/secrets/SECRET_NAME:VERSION

Replace the following:

    * SERVICE: the name of your service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
    * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example: `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
    * PROJECT_NUMBER: the project number for the project the secret was created in.
    * SECRET_NAME: the secret name—for example, `mysecret`.
    * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml




Due to constraints around API compatibility, the secret locations must be stored in an annotation.

  1. For secrets exposed as environment variables:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/secrets: SECRET_LOOKUP_NAME:projects/PROJECT_NUMBER/secrets/SECRET_NAME
             spec:
               containers:
               - image: IMAGE_URL
                 env:
                 - name: ENV_VAR
                   valueFrom:
                     secretKeyRef:
                       key: VERSION
                       name: SECRET_LOOKUP_NAME

Replace the following:

     * SERVICE: the name of your service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
     * ENV_VAR: the name of the environment variable.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`, it can be the same as SECRET_NAME.
  2. For secrets mounted as file paths:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/secrets: SECRET_LOOKUP_NAME:projects/PROJECT_NUMBER/secrets/SECRET_NAME
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

     * SERVICE: the name of your service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example: `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`, it can be the same as SECRET_NAME.
     * VOLUME_NAME: any name—for example, `my-volume`, it can be the same as SECRET_NAME.



### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  


**For secrets exposed as environment variables:**
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
      location = "REGION"
    
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
    

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * SECRET_NAME: the secret name—for example `mysecret`.
  * PROJECT_ID: the project ID the secret was created in.
  * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



**For secrets mounted as file paths:**
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
      location = "REGION"
    
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
    

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run job.
  * REGION with the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
  * VOLUME_NAME: any name—for example, `my-volume`, it can be the same as `SECRET_NAME`
  * MOUNT_PATH: the mount path of the volume and filename of the secret. It must start with a leading slash—for example: `/etc/secrets/dbconfig/password`, where `/etc/secrets/dbconfig/` is the mount path of the volume, and `password` is the filename of the secret.
  * PROJECT_ID: the project ID the secret was created in.
  * SECRET_NAME: the secret name—for example `mysecret`.



## View secrets settings

To view the current secrets settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the secrets setting in the returned configuration.




## Remove secrets from a service

You can remove secrets from a service using either the Google Cloud console or the gcloud CLI:

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select your service from the list.

  3. Click the **Containers** tab.

  4. To delete secrets mounted as a volume or environment variable, click delete **Delete**.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can remove all secrets from a service or specify one or more secrets to remove:

  * To remove all secrets, run the following command:
        
        gcloud run deploy SERVICE --image IMAGE_URL \
        --clear-secrets
        

Replace the following:

    * SERVICE: the name of your service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * To specify a list of secrets to remove, use the `--remove-secrets` flag. The following command removes one secret mounted as a volume and another secret exposed as an environment variable:
        
        gcloud run deploy SERVICE --image IMAGE_URL \
        --remove-secrets=ENV_VAR_NAME,SECRET_FILE_PATH
        

Replace the following:

    * SERVICE: the name of your service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
    * ENV_VAR_NAME: the name of the environment variable.
    * SECRET_FILE_PATH: the full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:
          
          --set-secrets MOUNT_PATH:SECRET_PATH=SECRET:VERSION
          




## Use secrets in your code

For examples on accessing secrets in your code as environment variables, refer to the tutorial on end user authentication, particularly the section [Handling sensitive configuration with Secret Manager](https://docs.cloud.google.com/run/docs/tutorials/identity-platform#secret-manager).

## Limitations

The following sections describe the limitations that apply to mounting secrets.

### Disallowed paths

  * Cloud Run doesn't allow you to mount secrets at `/dev`, `/proc` and `/sys`, or on their subdirectories. 
  * If you are mounting secrets on `/tmp` and you are using [first generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments), refer to the known issue on [mounting secrets on `/tmp`](https://docs.cloud.google.com/run/docs/known-issues#secrets-cannot-mount-tmp-gen1). 
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
