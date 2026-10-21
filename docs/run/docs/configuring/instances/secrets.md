---
url: https://docs.cloud.google.com/run/docs/configuring/instances/secrets/
title: Configure secrets for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:45.635409+00:00
---

# Configure secrets for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure secrets for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Your instance might require API keys, passwords, certificates, or other sensitive information for its dependencies. For Cloud Run, Google recommends storing this sensitive information in a secret you create in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs#docs).

Make a secret available to your containers in one of the following ways:

  * When you mount each secret as a volume, Cloud Run makes the secret available to the container as files. When reading a volume, Cloud Run always fetches the secret value from the Secret Manager to use the value with the latest version. This method also works well with secret rotation.
  * Pass a secret using [environment variables](https://docs.cloud.google.com/run/docs/configuring/instances/environment-variables). Environment variables are resolved at instance startup time, so if you use this method, Google recommends that you pin the secret to a particular version instead of using `latest` as the version.



For more information, see Secret Manager [best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

## How secrets are checked at deployment and runtime

During instance deployment, Cloud Run checks all the secrets you use. The check ensures that the service account that runs the container has permission to access these secrets.

During runtime, when instances start up:

  * If the secret is an environment variable, Cloud Run retrieves the value of the secret prior to starting the instance. If the secret retrieval process fails, the instance doesn't start.
  * If you mount the secret as a volume, Cloud Run doesn't perform any checks during instance startup. However, during runtime, if a secret is inaccessible, attempts to read the mounted volume fail.



## Volume ownership

The ownership of a Cloud Run secret volume differs by the execution environment and deployment type.

When you mount a secret volume using the second generation execution environment, which is always the case for instance, root owns the volume.

## Before you begin

  1. Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

  2. Use an existing secret or, create a secret in Secret Manager, as described in [ Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).



### Required roles

To get the permissions that you need to configure secrets, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



To allow Cloud Run to access the secret, the [service identity](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity) must have the following role:

  * [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`)



For instructions on how to add the service identity principal to the Secret Manager Secret Accessor role, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Make a secret accessible to Cloud Run

You can make a secret accessible to your instance using the Google Cloud CLI or YAML when you deploy a new [instance](https://docs.cloud.google.com/run/docs/deploy-instances) or update an existing instance:

###  gcloud 

  * To expose the secret as an environment variable when you deploy a instance, run the following command:
        
        gcloud beta run instances deploy INSTANCE \
          --image IMAGE_URL \
          --update-secrets=ENV_VAR_NAME=SECRET_NAME:VERSION

Replace the following:

    * `INSTANCE`: the name of your instance.
    * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
    * `ENV_VAR_NAME`: the name of the environment variable you want to use with the secret.
    * `SECRET_NAME`: the secret name in the same project—for example, `mysecret`.
    * `VERSION`: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  * To update multiple secrets at the same time, separate the configuration options for each secret with a comma. The following command updates one secret mounted as a volume and another secret exposed as an environment variable. To update existing secrets, run the following command:
        
        gcloud beta run instances deploy INSTANCE \
        --image IMAGE_URL \
        --update-secrets=PATH=SECRET_NAME:VERSION,ENV_VAR_NAME=SECRET_NAME:VERSION

  * To clear existing secrets and make a new secret accessible to the instance, use the `--set-secrets` flag:
        
        gcloud beta run instances update INSTANCE \
         --set-secrets="ENV_VAR_NAME=SECRET_NAME:VERSION"




### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. For secrets exposed as environment variables:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             env:
             - name: ENV_VAR
               valueFrom:
                 secretKeyRef:
                   key: SECRET_VERSION
                   name: SECRET_NAME

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * ENV_VAR: the name of the environment variable.
     * SECRET_VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
     * SECRET_NAME: the secret name—for example, `mysecret`.
  3. For secrets mounted as file paths:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             volumeMounts:
             - name: VOLUME_NAME
               mountPath: MOUNT_PATH
           volumes:
           - name: VOLUME_NAME
             secret:
               secretName: SECRET_NAME
               items:
               - key: SECRET_VERSION
                 path: SECRET_NAME

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
     * VOLUME_NAME: any name you want for your volume.
     * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * SECRET_VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  4. Replace the instance with its new configuration using the following command:
         
         gcloud beta run services replace service.yaml




### Reference secrets from other projects

To reference a secret from another project, verify that your project's instance account has access to the secret.

###  gcloud 

To reference a secret as an environment variable, run the following commad:
    
    
    gcloud beta run instances deploy INSTANCE \
        --image IMAGE_URL \
        --update-secrets=ENV_VAR_NAME=projects/PROJECT_NUMBER/secrets/SECRET_NAME:VERSION

Replace the following:

  * INSTANCE: the name of your instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
  * PROJECT_NUMBER: the project number for the project the secret was created in.
  * SECRET_NAME: the secret name—for example, `mysecret`.
  * VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.



### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. For secrets exposed as environment variables:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
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
                       key: SECRET_VERSION
                       name: SECRET_LOOKUP_NAME

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`, it can be the same as SECRET_NAME.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * ENV_VAR: the name of the environment variable.
     * SECRET_VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  3. For secrets mounted as file paths:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         metadata:
           annotations:
             run.googleapis.com/secrets: SECRET_LOOKUP_NAME:projects/PROJECT_NUMBER/secrets/SECRET_NAME
         spec:
           containers:
           - image: IMAGE_URL
             volumeMounts:
             - name: VOLUME_NAME
               mountPath: MOUNT_PATH
           volumes:
           - name: VOLUME_NAME
             secret:
               secretName: SECRET_NAME
               items:
               - key: SECRET_VERSION
                 path: SECRET_LOOKUP_NAME

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * SECRET_LOOKUP_NAME: any name that has a valid secret name syntax—for example, `my-secret`. It can be the same as SECRET_NAME.
     * PROJECT_NUMBER: the project number for the project the secret was created in.
     * SECRET_NAME: the secret name—for example, `mysecret`.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
     * VOLUME_NAME: any name you want for your volume.
     * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
     * SECRET_VERSION: the secret version. Use `latest` for latest version, or a number—for example, `2`.
  4. Replace the instance with its new configuration using the following command:
         
         gcloud beta run instances replace instance.yaml




## View secrets settings

To view the current secrets settings for your Cloud Run instance:

###  gcloud 

  1. Run the following command:
         
         gcloud beta run instances describe INSTANCE

  2. Locate the secrets setting in the returned configuration.




## Remove secrets from a instance

You can remove secrets from a instance using the gcloud CLI:

###  gcloud 

You can remove all secrets from a instance or specify one or more secrets to remove.

To remove all secrets, run the following command:
    
    
      gcloud beta run instances deploy INSTANCE --image IMAGE_URL \
          --clear-secrets

Replace the following:

  * INSTANCE: the name of your instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..



To specify a list of secrets to remove, use the `--remove-secrets` flag. The following command removes one secret mounted as a volume and another secret exposed as an environment variable:
    
    
      gcloud beta run instances deploy INSTANCE --image IMAGE_URL \
          --remove-secrets=ENV_VAR_NAME,SECRET_FILE_PATH

Replace the following:

  * INSTANCE: the name of your instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
  * ENV_VAR_NAME: the name of the environment variable.
  * SECRET_FILE_PATH: the full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:
        
        --set-secrets MOUNT_PATH:SECRET_PATH=SECRET:VERSION




## Use secrets in your code

For examples of accessing secrets in your code as environment variables, refer to the tutorial on end user authentication, particularly the section [Handling sensitive configuration with Secret Manager](https://docs.cloud.google.com/run/docs/tutorials/identity-platform#secret-manager).

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
