---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/cpu/
title: Configuring CPU allocation \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:31.426397+00:00
---

# Configuring CPU allocation  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Configuring CPU allocation Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to specify the number of CPUs to allocate for each Knative serving container instance. By default, Knative serving does not specify a minimum or maximum number of CPUs. Instead, your services are limited by the amount of resources available. Learn more about CPU resources in the [container runtime contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract).

## Setting and updating CPU allocation

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set CPU allocation using the Google Cloud console, the Google Cloud CLI, or a YAML file when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service) or update an existing service and deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Container**.

  4. Select the desired CPU allocation from the dropdown list. You can select numbers in [Kubernetes CPU units](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#cpu-units). For example, specify `1` for 1 CPU, `400m` for 0.4 CPU, and so forth.

  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

  * For existing services, set the number of CPUs to allocate by running the `gcloud run services update` command with the [`--cpu`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--cpu) parameter:
        
        gcloud run services update SERVICE --cpu CPU

Replace:

    * SERVICE with the name of your service.
    * CPU with the desired CPU allocation. Specify a value in [Kubernetes CPU units](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#cpu-units). For example, specify `1` for 1 CPU, `400m` for 0.4 CPU, and so forth.
  * For new services, set the number of CPUs to allocate by running the `gcloud run deploy` command with the [`--cpu`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--cpu) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --cpu CPU

Replace:

    * SERVICE with the name of your service.
    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * CPU with the desired CPU allocation. Specify a value in [Kubernetes CPU units](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#cpu-units). For example, specify `1` for 1 CPU, `400m` for 0.4 CPU, and so forth.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `cpu` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               containers:
               - image: IMAGE
                 resources:
                   limits:
                     cpu: CPU

Replace

     * SERVICE with the name of your Knative serving service
     * IMAGE with the URL of your container image.
     * CPU with the desired CPU value. Specify a value in [Kubernetes CPU units](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#cpu-units). For example, specify `1` for 1 CPU, `400m` for 0.4 CPU, and so forth.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
