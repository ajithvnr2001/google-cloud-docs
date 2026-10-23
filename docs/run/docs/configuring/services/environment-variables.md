---
url: https://docs.cloud.google.com/run/docs/configuring/services/environment-variables/
title: Configure environment variables for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:21.353095+00:00
---

# Configure environment variables for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure environment variables for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure environment variables for your Cloud Run service by using the Google Cloud console or gcloud.

You can use environment variables for service configuration, but we don't recommend them as a way to store secrets such as database credentials or API keys. Sensitive values should be stored outside both your source code and outside environment variables. For storing secrets, we recommend that you use Secret Manager. To configure services for accessing secrets stored in Secret Manager, see [Configure secrets](https://docs.cloud.google.com/run/docs/configuring/secrets).

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Warning:** If your Cloud Run service uses [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to authenticate access to Google Cloud APIs, never set `GOOGLE_APPLICATION_CREDENTIALS` as an environment variable on a Cloud Run service. Always configure a [user-managed service account](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) instead.

## Maximum number of environment variables and limits

You can set a maximum of 1000 environment variables for a Cloud Run service.

The maximum variable length is 32 Kb.

## Set environment variables for services

You can set environment variables for new and existing services. Note that the `--set-env-vars` flag is a destructive action that deletes previously set environment variables not included in the new list of environment variables.

Environment variables are bound to a specific service revision and are not visible to other services in your Google Cloud project.

You can set environment variables using the Google Cloud console, the gcloud CLI, or a YAML file when you [create a new service or deploy a new revision](https://docs.cloud.google.com/run/docs/deploying):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. In the **Variables & Secrets** section, click **Add Variable** to add a new variable. Specify the name you want for the variable, and its value in the **Name** and **Value** fields. For more information on how to set multiple environment variables, or escape special characters, see Set multiple environment variables.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To specify environment variables when you deploy your service, use the [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--set-env-vars) flag:
    
    
    gcloud run deploy SERVICE --image IMAGE_URL --set-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * SERVICE: the name of your service.
  * KEY1=VALUE1,KEY2=VALUE2: the comma separated list of variable names and values.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .



For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `name` and `value` attributes under the `env` attribute under `containers:`:
         
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
               - image: IMAGE
                 env:
                 - name: KEY-1
                   value: VALUE-1
                 - name: KEY-N
                   value: VALUE-N

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * KEY-1, VALUE-1: the environment variable and value. Optionally, add more variables and values as needed.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-env-var"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
    ** image = "us-docker.pkg.dev/cloudrun/container/hello"**
    ******# Environment variables**
    ** env {**
    ** name  = "foo"**
    ** value = "bar"**
    **}**
    ** env {**
    ** name  = "baz"**
            value = "quux"
          }
        }
      }
    }

The preceding `google_cloud_run_v2_service` resource specifies sets the `foo` environment variable to `bar`, and the `baz` environment variable to `quux`. Update the environment variables as necessary.

### Compose

To specify environment variables in your `compose.yaml` file, add the `environment` attribute to your service definition. You can use either `=` or `:` as the list separator. To specify multiple environment variables, you can also use the `env_file` attribute.
    
    
      services:
        web:
          image: IMAGE
          environment:
            - KEY1=VALUE1
            - KEY2=VALUE2

Replace the following:

  * IMAGE: the URL of your container image.
  * KEY1=VALUE1,KEY2=VALUE2 or KEY1:VALUE1,KEY2:VALUE2: the list of variable names and values.



**Deploy the service**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

### Set default environment variables in the container

You can use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) statement in a Dockerfile to set default values for environment variables:
    
    
    ENV KEY1=VALUE1,KEY2=VALUE2

### Order of precedence: container versus service variables

If you set a default environment variable in the container and also set an environment variable with the same name on the Cloud Run service, the value set on the service takes precedence.

## Set multiple environment variables for services

You can set multiple environment variables by using a configuration file or the [`--set-env-vars`](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables#env-flag) flag.

### Set multiple environment variables using a configuration file

To set multiple environment variables, use an `.env` file or a YAML file. Specify the environment variables in the following format:

###  `.env` file 
    
    
    KEY-1=VALUE-1
    KEY-2=VALUE-2
    KEY-3=VALUE-3

Replace KEY and VALUE with variable names and values. For example, `APP_NAME="My app"`.

###  YAML file 
    
    
    KEY-1: VALUE-1
    KEY-2: VALUE-2
    KEY-3: VALUE-3

Replace KEY and VALUE with variable names and values. For example, `APP_NAME: "My app"`.

To set these variables when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision), use the Google Cloud console, the gcloud CLI, or Compose:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. In the **Variables & Secrets** section, click **Add Variable** and paste the contents of your `.env` file or YAML file into the **Name** field. Cloud Run automatically populates the **Value** field, and creates new variables for each key-value pair you define in your file.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To specify multiple environment variables from your configuration file, run the following command:
    
    
    gcloud run deploy SERVICE --image=IMAGE_URL --env-vars-file=ENV_FILE_PATH
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * ENV_FILE_PATH: path to the `.env` file or the YAML file. For example, `production.env` or `config/production-variables.yaml`.



### Compose

To specify multiple environment variables in your `compose.yaml` file, add the `env_file` attribute to your service definition.
    
    
      services:
        web:
          image: IMAGE
          env_file:
            - ENV_FILE_PATH

Replace the following:

  * IMAGE: the URL of your container image.
  * ENV_FILE_PATH: path to the `.env` file.



**Deploy the service**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

### Set multiple environment variables using the `--set-env-vars` flag

If you have multiple environment variables that cannot be listed in `KEY1=VALUE1,KEY2=VALUE2` format, you can repeat the `--set-env-vars` flag multiple times: 
    
    
       [...]
       --set-env-vars "KEY1=VALUE1" \
       --set-env-vars "KEY2=VALUE2" \
       --set-env-vars "KEY3=VALUE3"

### Escape comma characters

Because the comma character `,` is used to split environment variables, if your environment variable contains comma characters as values, you need to [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) those delimiters by specifying a different delimiter character, for example, `@`: 
    
    
    --set-env-vars "^@^KEY1=value1,value2,value3@KEY2=..."

## Update environment variables for services

You can update environment variables for existing services. This is a non-destructive approach that changes or adds environment variables, but doesn't delete previously set environment variables.

###  Console 

To update environment variables using the Google Cloud console:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select your service from the list, then click the **Containers** tab.

  3. In the **Variables & Secrets** section, edit the **Name** or **Value** fields, and click **Done**.

  4. Click **View diff & redeploy**, then **Deploy changes**.




###  gcloud 

To update environment variables of an existing service, use the [`--update-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--update-env-vars) flag:
    
    
    gcloud run services update SERVICE --update-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * SERVICE: the name of your service.
  * KEY1=VALUE1,KEY2=VALUE2: the comma separated list of variable names and values.



To update environment variables of an existing multi-region service, use the [`gcloud run multi-region-services update`](https://docs.cloud.google.com/run/docs/multiple-regions) command.

## View environment variables settings

To view the current environment variables settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the environment variables setting in the returned configuration.




## Delete environment variables

You can delete environment variables for existing services.

###  Console 

To delete environment variables using the Google Cloud console:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select your service from the list, then click the **Containers** tab.

  3. In the **Variables and secrets** tab, move your cursor to the right of the **Value** field of the environment variable you are removing, to display the delete **Delete** icon, and click it.

  4. Click **View diff and redeploy** , then **Deploy changes**.




###  gcloud 

To selectively remove environment variables of an existing service,use the [`--remove-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--remove-env-vars) flag:
    
    
    gcloud run services update SERVICE --remove-env-vars KEY1,KEY2
    

Replace the following:

  * SERVICE: the name of your service.
  * KEY1,KEY2: the comma separated list of variable names.



Alternatively, clear all previously set environment variables with the [`--clear-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--clear-env-vars) flag:
    
    
    gcloud run services update SERVICE --clear-env-vars
    

Replace SERVICE with the name of your service.

## Best practices

The following section highlights some of the best practices for configuring environment variables.

### Reserved environment variables for services

The environment variables defined in the [container runtime contract](https://docs.cloud.google.com/run/docs/reference/container-contract#env-vars) are reserved and cannot be set. In particular, the `PORT` environment variable is injected inside your container by Cloud Run. You shouldn't set it yourself.

### Additional reserved environment variables when deploying functions

Cloud Run sets the following runtime environment variables automatically when deploying functions:

  * `FUNCTION_TARGET`: The function to be executed.
  * `FUNCTION_SIGNATURE_TYPE`: The type of the function: `http` for HTTP functions, and `event` for event-driven functions.



Some additional environment variables are automatically set depending on the runtime your function uses. These are based on the runtime's operating system, for example, `DEBIAN_FRONTEND`, `SHLVL`, or `PATH` and the language runtime for example, `NODE_ENV`, `VIRTUAL_ENV`, or `GOPATH`.

Environment variables that are provided by the environment, other than the ones that are set automatically, might change in future runtime versions. As a best practice, we recommend that you don't depend on or modify any environment variables that you haven't set explicitly.

Modifying environment variables that are provided by the environment might lead to unpredictable outcomes. Attempts to modify such environment variables could be blocked or, worse, lead to unintended consequences such as functions that cannot start. As a best practice, consider prefixing any environment variables with a unique key to avoid conflicts.

### Invalid environment variables

You can't use the following environment variables:

Key | Description  
---|---  
Empty ('') | Keys can't be an empty string.  
`=` | Keys can't contain the '=' character.  
`X_GOOGLE_` | Keys can't contain the prefix `X_GOOGLE_`.  
  
## Sample code

For code sample that show how to access environment variables in your code, refer to [Handling sensitive configuration with Secret Manager](https://docs.cloud.google.com/run/docs/tutorials/identity-platform#secret-manager) in the End user authentication tutorial.

## What's next

You can use environment variables to set [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) configuration. For language-specific details, see the buildpacks documentation for:

  * [Node.js](https://docs.cloud.google.com/docs/buildpacks/nodejs#environment_variables)
  * [Python](https://docs.cloud.google.com/docs/buildpacks/python#environment_variables)
  * [Go](https://docs.cloud.google.com/docs/buildpacks/go#environment_variables)
  * [Ruby](https://docs.cloud.google.com/docs/buildpacks/ruby#environment_variables)
  * [PHP](https://docs.cloud.google.com/docs/buildpacks/php#customizing_nginx_configurations)
  * [Java](https://docs.cloud.google.com/docs/buildpacks/java#configure_maven)



If you are deploying from source and need to customize variables at build time, see [Set build environment variables](https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
