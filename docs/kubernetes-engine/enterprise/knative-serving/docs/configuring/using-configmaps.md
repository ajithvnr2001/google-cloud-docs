---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-configmaps/
title: Using ConfigMaps \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:37.457957+00:00
---

# Using ConfigMaps  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-configmaps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using ConfigMaps Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create a ConfigMap and then configure your Knative serving services and revisions to use that ConfigMap.

A common use case for a service is to use ConfigMaps to separate application code from configuration. ConfigMap is similar to [Secret](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-secrets) except that you use a Secret for sensitive information and you use a ConfigMap to store non-sensitive data such as connection strings, public credentials, hostnames, and URLs. You can learn more about using ConfigMaps in the [Google Kubernetes Engine documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configmap).

When you enable containers to access ConfigMaps, you can choose either of these options:

  * Mount the ConfigMap as a volume, with ConfigMap entries available as files in the mounted volume. This is recommended because it ensures that you get the latest version of the ConfigMap when you are reading it.
  * Pass the ConfigMap using [environment variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables).



## Creating a ConfigMap

There are several ways to create a ConfigMap, as described in the [ConfigMaps](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configmap) page of the GKE documentation. For your convenience, the following steps show a simple way to create a ConfigMap.

When you create a ConfigMap, make sure you create it in the same namespace as the cluster that is running your Knative serving service. These instructions use the `default` namespace.

You can create a ConfigMap from the command line:
    
    
    kubectl create configmap NAME DATA
    

Replace:

  * NAME is the name of your ConfigMap object.
  * DATA can be either:

    * The `--from-file` flag and path for each directory that contains one or more configuration files.
    * The `--from-literal` flag and key-value pair for each that you want to add to the ConfigMap.



For example:
    
    
    kubectl create configmap special-config --from-literal=special.how=very --from-literal=special.type=charm
    

The ConfigMap is created and uploaded where it is available to clusters in the `default` namespace.

## Making a ConfigMap available to a service

After you create a ConfigMap, you can make it available to your Knative serving service either as a volume or as environment variables using the Google Cloud console or the Google Cloud CLI when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service) or update an existing service and deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Variables and Secrets**.

  4. Under _Reference a ConfigMap_ , select the desired ConfigMap from the pulldown menu.

     * In the _Reference method_ pulldown menu, select the way you want to use your ConfigMap, mounted as a volume or exposed as environment variables.
     * If you are using mount as a volume, specify the path, then click **Done**.
     * If you are exposing as environment variables:
       1. Supply the _Name_ of the variable and select the corresponding ConfigMap value from the _Key_ pulldown menu.
       2. Click **Add** to add another ConfigMap value.
       3. Supply the _Name_ of the variable and select the corresponding ConfigMap value from the _Key_ pulldown menu.
       4. Click **Done**.
  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

You can use the Google Cloud CLI to set ConfigMaps for new services or to update an existing services:

  * For existing services, update a ConfigMap by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with one of the following parameters:

    * [`--set-config-maps`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--set-config-maps)
    * [`--update-config-maps`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--update-config-maps)
    * [`--clear-config-maps`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--clear-config-maps)
    * [`--remove-config-maps`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--remove-config-maps)

Example:
    
    gcloud run services update SERVICE --update-config-maps KEY1=VALUE1,KEY2=VALUE2

Replace:

    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each ConfigMap. For each KEY you can specify a mount path, or provide an environment variable. Specify a mount path by starting with a forward slash `/`. All other keys correspond to environment variables. For each VALUE, specify the ConfigMap name. How to specify multiple parameters.

### Command parameter options

To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
    
    [...]
    --update-config-maps "KEY=VALUE1" \
    --update-config-maps "KEY=VALUE2" \
    --update-config-maps "KEY=VALUE3"

OK

  * For new services, set the ConfigMap by running the `gcloud run deploy` command with the [`--set-config-maps`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--set-config-maps) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --set-config-maps KEY1=VALUE1,KEY2=VALUE2

Replace:

    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each ConfigMap. For each KEY you can specify a mount path, or provide an environment variable. Specify a mount path by starting with a forward slash `/`. All other keys correspond to environment variables. For each VALUE, specify the ConfigMap name. How to specify multiple parameters.

### Command parameter options

To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
    
    [...]
    --update-config-maps "KEY=VALUE1" \
    --update-config-maps "KEY=VALUE2" \
    --update-config-maps "KEY=VALUE3"

OK




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
