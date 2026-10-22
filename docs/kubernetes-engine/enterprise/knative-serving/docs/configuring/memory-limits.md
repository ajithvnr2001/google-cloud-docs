---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits/
title: Configuring memory limits \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:38.639982+00:00
---

# Configuring memory limits  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Configuring memory limits Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to set limits for the memory used by your container instances in Knative serving.

## Understanding memory usage

Knative serving container instances that exceed their allowed memory limit are terminated.

The following count towards the available memory of your container instance:

  * Running the application executable (as the executable must be loaded to memory)
  * Allocating memory in your application process
  * Writing files to the filesystem



The size of the deployed container image does not count towards the available memory.

## Maximum amount of memory

The maximum amount of memory you can configure is limited by the configuration of your GKE cluster.

## Optimizing memory

You can determine the peak memory requirement for a service using the following: **(Standing Memory) + (Memory per Request) * (Service Concurrency)**

Accordingly,

  * If you raise the concurrency of your service, you should also increase the memory limit to account for peak usage.

  * If you lower the concurrency of your service, consider reducing the memory limit to save on memory usage costs.




For more guidance on minimizing per request memory usage read [Development Tips on Global Variables](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general#using_global_variables).

## Setting and updating memory limits

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set memory limits using the Google Cloud console, the Google Cloud CLI, or a YAML file when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service) or update an existing service and deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Container**.

  4. Select the desired memory size from the **Memory allocated** dropdown list.

  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

  * For existing services, update the memory limit by running the `gcloud run services update` command with the [`--memory`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--memory) parameter:
        
        gcloud run services update SERVICE --memory SIZE

Replace:

    * SERVICE with the name of your service.
    * SIZE with the desired memory size. The format for size is a fixed or floating point number followed by a unit: `G`, `M`, or `K` corresponding to gigabyte, megabyte, or kilobyte, respectively, or use the power-of-two equivalents: `Gi`, `Mi`, `Ki` corresponding to gibibyte, mebibyte or kibibyte respectively.
  * For new services, set the memory limit by running the `gcloud run deploy` command with the [`--memory`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--memory) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --memory SIZE

Replace:

    * SERVICE with the name of your service.
    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * SIZE with the desired memory size. The format for size is a fixed or floating point number followed by a unit: `G`, `M`, or `K` corresponding to gigabyte, megabyte, or kilobyte, respectively, or use the power-of-two equivalents: `Gi`, `Mi`, `Ki` corresponding to gibibyte, mebibyte or kibibyte respectively.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `memory` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: _SERVICE_NAME_
         spec:
           template:
             spec:
               containers:
               – image: _IMAGE_URL_
                 resources:
                   limits:
                     memory: SIZE

Replace SIZE with the desired memory size. The format is a fixed or floating point number followed by a unit: `G`, `M`, or `K` corresponding to gigabyte, megabyte, or kilobyte, respectively, or use the power-of-two equivalents: `Gi`, `Mi`, `Ki` corresponding to gibibyte, mebibyte or kibibyte respectively.

  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
