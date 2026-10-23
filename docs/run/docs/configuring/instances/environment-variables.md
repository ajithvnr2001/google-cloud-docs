---
url: https://docs.cloud.google.com/run/docs/configuring/instances/environment-variables/
title: Configure environment variables for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:35.407793+00:00
---

# Configure environment variables for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure environment variables for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure environment variables for your Cloud Run instance.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Warning:** If your Cloud Run instance uses [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to authenticate access to Google Cloud APIs, never set `GOOGLE_APPLICATION_CREDENTIALS` as an environment variable on a Cloud Run instance. Always configure a [user-managed service account](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity) instead.

## Set environment variables

You can set environment variables for a Cloud Run instance using the Google Cloud CLI or YAML:

###  gcloud 

To specify environment variables while creating your instance, use the [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/create#--set-env-vars) flag:
    
    
    gcloud beta run instances create INSTANCE --image IMAGE_URL --set-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * INSTANCE: the name of your instance
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * KEY1=VALUE1,KEY2=VALUE2: the comma-separated list of variable names and values
  * 


For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

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
           - env:
             - name: KEY
               value: VALUE
             - name: KEY2
               value: VALUE2
             image: IMAGE

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * KEY and VALUE: the name and values of the environment variables.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




### Set default environment variables in the container

You can use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) statement in a Dockerfile to set default values for environment variables:
    
    
    ENV KEY1=VALUE1,KEY2=VALUE2

### Order of precedence: container versus instance variables

If you set a default environment variable in the container and also set an environment variable with the same name on the Cloud Run instance, the value set on the instance takes precedence.

## Set multiple environment variables

You can set multiple environment variables by using the `.env` file or the `--set-env-vars` flag.

### Set multiple environment variables using the `.env` file

###  gcloud 

To specify multiple environment variables from the `.env` file, run the following command:
    
    
    gcloud beta run instances create INSTANCE --image IMAGE_URL --env-vars-file=ENV_FILE_PATH
    

Replace the following:

  * INSTANCE: the name of the instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * ENV_FILE_PATH: path to the `.env` file.



### Set multiple environment variables using the `--set-env-vars` flag

If you have multiple environment variables that cannot be listed in `KEY1=VALUE1,KEY2=VALUE2` format, you can repeat the `--set-env-vars` flag multiple times: 
    
    
       [...]
       --set-env-vars "KEY1=VALUE1" \
       --set-env-vars "KEY2=VALUE2" \
       --set-env-vars "KEY3=VALUE3"

### Escape comma characters

Because the comma character `,` is used to split environment variables, if your environment variable contains comma characters as values, you need to [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) those delimiters by specifying a different delimiter character, for example, `@`: 
    
    
    --set-env-vars "^@^KEY1=value1,value2,value3@KEY2=..."

## Update environment variables

You can update runtime environment variables for existing instances. This is a non-destructive approach that changes or adds runtime environment variables, but doesn't delete them.

You can update environment variables using the Google Cloud CLI or YAML:

###  gcloud 

To update environment variables of an existing instance, use the [`--update-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/create#--update-env-vars) flag:
    
    
    gcloud beta run instances update INSTANCE --update-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * INSTANCE: the name of your instance
  * KEY1=VALUE1,KEY2=VALUE2: the comma-separated list of variable names and values



### YAML

  1. Download the instance [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Edit the key (name) and value variables.

  3. Update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




## Delete environment variables

###  gcloud 

To selectively remove environment variables from an existing instance, use the [`--remove-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/create#--remove-env-vars) flag:
    
    
    gcloud beta run instances update INSTANCE --remove-env-vars KEY1,KEY2
    

Replace the following:

  * INSTANCE: the name of your instance
  * KEY1,KEY2: the comma-separated list of variable names



Alternatively, clear all previously set environment variables with the [`--clear-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/create#--clear-env-vars) flag:
    
    
    gcloud beta run instances update INSTANCE --clear-env-vars
    

Replace INSTANCE with the name of your instance.

## Sample code

For a code sample that shows how to access environment variables in your code, refer to [Handling sensitive configuration with Secret Manager](https://docs.cloud.google.com/run/docs/tutorials/identity-platform#secret-manager) in the end user authentication tutorial.

## What's next

You can use environment variables to set a [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) configuration. For language-specific details, see the buildpacks documentation for:

  * [Node.js](https://docs.cloud.google.com/docs/buildpacks/nodejs#environment_variables)
  * [Python](https://docs.cloud.google.com/docs/buildpacks/python#environment_variables)
  * [Go](https://docs.cloud.google.com/docs/buildpacks/go#environment_variables)
  * [Ruby](https://docs.cloud.google.com/docs/buildpacks/ruby#environment_variables)
  * [PHP](https://docs.cloud.google.com/docs/buildpacks/php#customizing_nginx_configurations)
  * [Java](https://docs.cloud.google.com/docs/buildpacks/java#configure_maven)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
