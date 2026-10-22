---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-secrets/
title: Using secrets \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:19.735082+00:00
---

# Using secrets  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using secrets Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create a Secret and configure your Knative serving services and revisions to use that Secret.

A common use case for a service is to access third-party applications through usernames and passwords. For Google Kubernetes Engine, it's a best practice to store this type of sensitive information in a Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) object.

To provide your containers with access to Secrets, you can mount each Secret as a volume, which makes the entries in the Secret available to the container as files. You should mount your Secret to ensure that you get the latest version of each Secret when it is read.

You can also pass a Secret using [environment variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables).

**Caution:** Do not use environment variables for sensitive information because environment variables are stored as text and are accessible to the cluster.

## Creating a Secret

The following steps simply demonstrate how to create a Secret but there are several ways to create a Secret, as explained in the [Secret](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret) topic.

When you create a Secret, make sure you create it in the same namespace as the cluster that is running your Knative serving service. In these examples, the `default` namespace is used.

To create a Secret in the `default` namespace of your cluster:

  * Create a Secret using a file:
        
        echo -n 'devuser' > ./username.txt
        echo -n 'S!B\*d$zDsb' > ./password.txt
        kubectl create secret generic user-creds --from-file=./username.txt --from-file=./password.txt
        

  * Create a Secret using a `kubectl` command only:
        
        kubectl create secret generic user-creds --from-literal=username=devuser --from-literal=password='S!B\*d$zDsb'
        




## Making a Secret available to a service

You can associate secrets with a service using the Google Cloud console or command-line tools when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service) or update an existing service and deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Variables and Secrets**.

  4. Under _Reference a Secret_ , select the desired Secret from the pulldown menu.

     * In the _Reference method_ pulldown menu, select the way you want to use your Secret, mounted as a volume or exposed as environment variables.
     * If you are using mount as a volume, specify the path, then click **Done**.
     * If you are exposing as environment variables:**Caution** : Do not use [environment variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables) for sensitive information.
       1. Supply the _Name_ of the variable and select the corresponding Secret value from the _Key_ pulldown menu.
       2. Click **Add** to add another secret value.
       3. Supply the _Name_ of the variable and select the corresponding Secret value from the _Key_ pulldown menu.
       4. Click **Done**.
  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### gcloud

You can use the Google Cloud CLI to associate Secrets with new services or to update existing services:

  * For existing services, update a Secret by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with one of the following parameters:

    * [`--clear-secrets`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--clear-secrets)
    * [`--remove-secrets`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--remove-secrets)
    * [`--set-secrets`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--set-secrets)
    * [`--update-secrets`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--update-secrets)

Example:
    
    gcloud run services update SERVICE --update-secrets KEY1=VALUE1,KEY2=VALUE2

Replace:

    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each Secret. For each KEY you specify the path by starting with a forward slash `/` to mount a Secret as a file. Optionally, you can exclude the forward slash to mount the Secret as an [environment variable](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables). For each VALUE, specify the secret name. How to specify multiple parameters.

### Command parameter options

To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
    
    [...]
    --update-secrets "KEY=VALUE1" \
    --update-secrets "KEY=VALUE2" \
    --update-secrets "KEY=VALUE3"

OK

  * For new services, associate a Secret by running the `gcloud run deploy` command with the [`--set-secrets`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--set-secrets) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --set-secrets KEY1=VALUE1,KEY2=VALUE2

Replace:

    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * SERVICE with the name of your service.
    * KEY1=VALUE1,KEY2=VALUE2 with a comma separated list of name and value pairs for each Secret. For each KEY you specify the path by starting with a forward slash `/` to mount a Secret as a file. Optionally, you can exclude the forward slash to mount the Secret as an [environment variable](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/environment-variables). For each VALUE, specify the secret name. How to specify multiple parameters.

### Command parameter options

To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
    
    [...]
    --update-secrets "KEY=VALUE1" \
    --update-secrets "KEY=VALUE2" \
    --update-secrets "KEY=VALUE3"

OK




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
