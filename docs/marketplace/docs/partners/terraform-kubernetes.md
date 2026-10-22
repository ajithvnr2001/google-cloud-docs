---
url: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/
title: Offer Terraform Kubernetes apps through Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:21.728757+00:00
---

# Offer Terraform Kubernetes apps through Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Offer Terraform Kubernetes apps through Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

Terraform Kubernetes apps in Google Cloud Marketplace let your customers use Terraform to deploy your containerized apps on Google Kubernetes Engine. Your users aren't charged for their usage of your Terraform Kubernetes apps, but they're charged for their usage of Google Cloud resources. You can offer Terraform Kubernetes apps publicly to all Cloud Marketplace users, or privately by using Private Offers.

Terraform Kubernetes apps that you offer through Cloud Marketplace define their configurations by using Helm charts, which you host in Artifact Registry. After that's set up, you onboard your app to Cloud Marketplace through Producer Portal.

## Before you begin

  * If you're new to offering software on Cloud Marketplace, [sign up to become a vendor](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#initiate-onboarding). 
  * For your first (and all subsequent) listings you must complete the [Cloud Marketplace Onboarding Validation Form](https://docs.google.com/forms/d/e/1FAIpQLSesllyRR-HvLFZthYA8Cv4nQRUTOthHGgs-76DY9o2IntUL3A/viewform). 
  * To get access to Producer Portal, complete the _Cloud Marketplace Project Info Form_ , provided by the Cloud Marketplace team. 
  * Review the [open source compliance](https://docs.cloud.google.com/marketplace/docs/partners/open-source-compliance) recommendations and restrictions. 



## Overview of onboarding a Terraform Kubernetes app

Offering a Terraform Kubernetes app through Cloud Marketplace involves the following steps:

  1. [Prepare your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment) for Cloud Marketplace. This includes setting up Artifact Registry and pushing your app's images to it.

  2. [Add pricing information](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/select-pricing) for your app in Producer Portal.

  3. [Configure your app's deployment](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/configure-deployment) in Producer Portal, including its Terraform module, Helm chart, and container images.

  4. [Add a label](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/partner-consumption-tracking) to track your app's associated consumption of Google Cloud resources.

  5. [Publish your app to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/publish). As you onboard your app, you submit various parts of your app for review. The Cloud Marketplace team reviews each submission and works with you to resolve any issues before approving it. When all of your submissions are approved, you can publish and launch the product within a few minutes.




## Product-specific requirements

All products that you offer through Cloud Marketplace must comply with the Cloud Marketplace [listing requirements](https://docs.cloud.google.com/marketplace/docs/partners/get-started).

Your Terraform Kubernetes app must meet the following additional requirements:

  * Your app must run on GKE nodes that use x86 processors.
  * All of your app's Helm charts and container images must be uploaded to your Artifact Registry registry, to the same repository and project that you're using for your Terraform Kubernetes app.
  * Your Artifact Registry registry must include a Helm chart.
  * You must add a label to your app's Helm charts to track your app's associated consumption of Google Cloud resources. For details, see [Track your Kubernetes apps' associated consumption with labels](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/partner-consumption-tracking).
  * Your Terraform module must be hosted as a ZIP file in a Cloud Storage bucket located in the same project that you're using for your Terraform Kubernetes app.
  * You must enable versioning for the Cloud Storage bucket that you use to host your Terraform module.
  * You must include a user guide, with steps to deploy your app from the command line, configure the app, and use the app. For details, see Requirements for your user guide in this document.
  * To protect users from unstable APIs, use only beta or generally available Kubernetes resources.



### Requirements for your app images

Your app images must meet the following requirements:

  * All of your app's images must be tagged with the release track and the current version. For example, if you're releasing version `2.0.5` on the `2.0` release track, all corresponding images must be tagged with `2.0` and `2.0.5`. For details, see [Organize your releases](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment#organize-releases).
  * All of your app's images must contain the following annotation in their image manifest:
        
        com.googleapis.cloudmarketplace.product.service.name=services/SERVICE_NAME
        

Replace SERVICE_NAME with the name of your service (for example, `example.endpoints.example-project.cloud.goog`). You can find the service name for your product on the **Overview** page in Producer Portal, in the **Service name** column. For more information about annotations, see the Open Container Initiative's documentation of [annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md) on GitHub.




### Requirements for your Artifact Registry repository

Your app's Helm chart and container images must be part of a single Artifact Registry repository.

For example, if your Artifact Registry repository is `us-docker.pkg.dev/exampleproject`, your app's Helm chart and container images should resemble the following:

  * `us-docker.pkg.dev/exampleproject/exampleapp/chart`
  * `us-docker.pkg.dev/exampleproject/exampleapp/image1`
  * `us-docker.pkg.dev/exampleproject/exampleapp/image2`



### Requirements for the Terraform module

Customers use the Terraform module to deploy your product from Cloud Marketplace through Infrastructure Manager. The Terraform module packages your app's Kubernetes configuration.

Use the [example module](https://github.com/GoogleCloudPlatform/marketplace-tools/tree/master/docs/terraform-k8s-app/starter-terraform-module) as a starting point, and follow the [partner guide](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/docs/terraform-k8s-app/terraform-k8s-app-packaging-guide.md) to build a Terraform module that's compatible with your app.

#### Parameters passed to your app

Your Terraform module must declare parameters that need to be collected from customers when they select your app. These parameters are then supplied to the Helm chart container when users deploy the app.

To configure these parameters, your Terraform module must include a [`schema.yaml`](http://json-schema.org/) file.

To learn how to create a `schema.yaml`, see the [guide to creating a schema](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/schema.md) on GitHub.

#### GPU cluster requests

If your app has specific GPU needs, or is GPU intensive, you can [specify the type and number of GPUs in the cluster by using your deployer schema](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/schema.md#gpus). If you specify your GPU needs, you turn off assisted cluster creation.

Your app may request a generic Nvidia GPU, or a specific [Nvidia platform](https://docs.cloud.google.com/compute/docs/gpus).

### Requirements for your app's user guide

Your app's user guide must include the following information:

  * **Overview** : A general overview of your app, covering basic functions and configuration options. This section must also link to your published app on Cloud Marketplace.
  * **One-time setup** : This includes steps for configuring Helm and installing the Application `CustomResourceDefinition` (CRD) so that your cluster can manage the Application resource.
  * **Installation** : This includes the following: 
    * Commands for deploying your app
    * Passing parameters available in UI configuration
    * Pinning image references to immutable digests
    * Information about any custom input fields that you've added to your Terraform module, if applicable; see the [instructions for adding input fields to your Terraform module](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/schema.md#properties)
  * **Basic Usage** : Guides for the following tasks: 
    * Modifying usernames and passwords
    * Connecting to an admin console, if applicable
    * Connecting a client tool and running a sample command, if applicable
    * Enabling ingress and installing TLS certs, if applicable
  * **Back up and restore** : Information about backing up the app state and restoring the app state from a backup.
  * **Image updates** : Information about updating the app images for patches or minor updates.
  * **Scaling** : Information about scaling the app, if applicable.
  * **Deletion** : Guides for deleting the app and cleaning up any resources that might remain, such as [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).



## Pricing models for Terraform Kubernetes apps

You can choose one of the following pricing models for your app:

  * **Free** : Customers only pay for the Google Cloud resources that they use.
  * **Usage-based** : Customers pay for your app based on measurements that you choose, called _metrics_ , such as the number of containers or storage time. If you choose a usage-based pricing model, your app must measure and report usage information to Google.



After you've published a Terraform Kubernetes app with usage-based pricing, you can update your app's pricing. To update your app's pricing, it must be at least 30 days since you published your app or last updated its pricing.

**Caution:** You can't update a free Terraform Kubernetes app to use usage-based pricing. To change your app from free to usage-based pricing, you must create a new product listing for your app with usage-based pricing.

### Usage-based pricing

Google Cloud Marketplace uses Kubernetes pod [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to track usage and charge customers for their deployments of your Cloud Marketplace apps. Cloud Marketplace tracks billing and metering at the pod level, and aggregates them at the product listing level.

If you deploy multiple pods on the same machine (vCPU, GPU, TPU, or memory), the system assigns the cumulative usage occurring across all of the pods deployed on the machine to each of the pods. For example, if you have three pods that share the same GPU, Cloud Marketplace counts this as three GPUs.

Cloud Marketplace treats different [GKE SKUs](https://docs.cloud.google.com/kubernetes-engine/pricing) within each vCPU, TPU, GPU, or memory family of SKUs as identical. For example, if GPU is set up as a metric, the configured price applies regardless of whether your customer uses GKE Autopilot T4 GPU Premium, GKE Autopilot L4GKE Autopilot H100 GPU Premium, GKE Autopilot A100 40 GiB GPU, GKE Autopilot A100 80 GiB GPU, or GKE Autopilot H100 GPU Premium.

We strongly recommend that you integrate business logic to ensure accurate customer billing into your Cloud Marketplace apps. To mitigate the impact of accidental removal of label annotations, we recommend that you design your app to periodically confirm that the label annotations are still present. If an annotation is missing, your app should limit its functionality until the label has been reinstated. For an example of this in Python, see the following example:
    
    
    pod_name = os.environ.get("HOSTNAME")
    namespace = open(
          "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
    ).read()
    # Load in-cluster config
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    # Get the Pod object
    pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
    annotations = pod.metadata.annotations
    if annotations:
    print("Annotations for this pod:")
    for key, value in annotations.items():
          print(f"  {key}: {value}")
    else:
    print("No annotations found on this pod.")
    

## What's next

  * Review the [Cloud Marketplace listing requirements](https://docs.cloud.google.com/marketplace/docs/partners/get-started).
  * [Prepare your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment) for Cloud Marketplace.
  * [Add your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/add-product) to Cloud Marketplace by using Producer Portal.



[ Next Understand how customers see your deployment packages  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/customer-view-deployment-packages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
