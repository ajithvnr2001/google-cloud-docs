---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables/
title: Setting environment variables \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:29.507246+00:00
---

# Setting environment variables  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Setting environment variables Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create and use environment variables in Knative serving.

When you set [environment variables](https://en.wikipedia.org/wiki/Environment_variable), they are injected into the container and are accessible to your code. Environment variables are set as key/value pairs. For example, suppose you are running a service that enables additional logging when it reads `LOGGING_VERBOSE: true` in the environment. In this scenario, you set the environment variable key/value pair as `LOGGING_VERBOSE=true`. The exact commands or UI are shown in the following sections.

**Caution:** You should not use environment variables to store and consume sensitive information because environment variables are stored as text and are accessible to the cluster. Use [Secrets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-secrets) for sensitive information.

## Reserved names

The environment variables defined in the [container runtime contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract#env-vars) are reserved and cannot be set. In particular, the `PORT` environment variable is injected inside your container by Knative serving. You should not set it yourself.

## Setting environment variables on a service

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set environment variables using the Google Cloud console, the Google Cloud CLI, or a YAML file when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service) or update an existing service and deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Variables and Secrets**.

  4. Do the following: 

     * If you are adding a variable, click **Add Variable** , and specify the name you want for the variable and its value in the **Name** and **Value** text boxes.
     * If you are changing a value for a variable, replace the current value in the **Value** text box with the one you want.
     * If you are removing one or more environment variables, hover your cursor to the left of the **Value** textbox of the variable you are removing to display the Trash icon, and click it.
  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

You can use the Google Cloud CLI to set environment variables for new services or to update existing services:

  * For existing services, update environment variables by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with one of the following parameters:

    * [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--set-env-vars)
**Caution:** `--set-env-vars` reconfigures all environment variables so only the specified environment variables are set and remain. All other previously existing environment variables are removed if they are not explicitly specified.   
  
Use `--update-env-vars` to simply add to or modify existing environment variables and avoid removing all existing environment variables.
    * [`--update-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--update-env-vars)
    * [`--remove-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--remove-env-vars)
    * [`--clear-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--clear-env-vars)

Example:
    
    gcloud run services update SERVICE --update-env-vars KEY1=VALUE1,KEY2=VALUE2

Replace:

    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each environment variable. Specify the environment variable name for each KEY and the value of that environment variable for VALUE. How to specify multiple parameters.

### Command parameter options

      * To specify an environment variable that contains a comma (`,`), you must [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) each KEY=VALUE with a different delimiter. For example, if you use `@`: 
            
            --set-env-vars "^@^KEY1=value,with,commas@KEY2=anothervalue@KEY3..."

      * To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
            
            [...]
            --set-env-vars "KEY=VALUE1" \
            --set-env-vars "KEY=VALUE2" \
            --set-env-vars "KEY=VALUE3"

OK

  * For new services, set environment variables by running the `gcloud run deploy` command with the [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--set-env-vars) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --set-env-vars KEY1=VALUE1,KEY2=VALUE2

Replace:

    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each environment variable. Specify the environment variable name for each KEY and the value of that environment variable for VALUE. How to specify multiple parameters.

### Command parameter options

      * To specify an environment variable that contains a comma (`,`), you must [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) each KEY=VALUE with a different delimiter. For example, if you use `@`: 
            
            --set-env-vars "^@^KEY1=value,with,commas@KEY2=anothervalue@KEY3..."

      * To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
            
            [...]
            --set-env-vars "KEY=VALUE1" \
            --set-env-vars "KEY=VALUE2" \
            --set-env-vars "KEY=VALUE3"

OK




### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `name` and `value` attributes under the `env` attribute under `containers:`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               containers:
               - env:
                 - name: KEY-1
                   value: VALUE-1
                 - name: KEY-N
                   value: VALUE-N

Replace

     * SERVICE with the name of your Knative serving service
     * KEY-1, VALUE-1 with the environment variable and value. Optionally add more variables and values as desired.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




## Setting default environment variables in the container

You can use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) statement in a Dockerfile to set default values for environment variables:
    
    
    ENV KEY1=VALUE1,KEY2=VALUE2

## Order of precedence: container vs service variables

If you set a default environment variable in the container and also set an environment variable with the same name on the Knative serving service, the value set on the service takes precedence.

## Enabling Kubernetes service links

To use [Kubernetes service links](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/#accessing-the-service), you must manually enable support. Due to the performance issues seen in namespaces with thousands of services and revisions, Kubernetes service links were disabled by default starting in January 2021.

**Important:** Information about each of your services are injected into your pod's environment variables when you enable Kubernetes service links. In namespaces that contain over 1,000 Knative serving services or revisions, you might experience performance issues or even service failures.

To enable Kubernetes service links, run the following command to set `data.enable-service-links` to `true` in your `knative-serving/config-defaults` ConfigMap:
    
    
    kubectl patch cm -n knative-serving config-defaults -p '{"data":{"enable-service-links":"true"}}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
