---
url: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment/
title: Prepare your Terraform Kubernetes app for Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:06.934424+00:00
---

# Prepare your Terraform Kubernetes app for Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Prepare your Terraform Kubernetes app for Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

Before onboarding your Terraform Kubernetes app through Producer Portal, we recommend that you prepare your Google Cloud environment and your Terraform Kubernetes app for Google Cloud Marketplace.

## Before you begin

To get access to Producer Portal, ensure that you've completed the [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform).

## Create your workspace

We recommend that you create a new project in the [Google Cloud console](https://console.cloud.google.com/), with a project ID ending in `-public`, primarily for your Cloud Marketplace products. For detailed instructions, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

If you already have a project set up to sell on Cloud Marketplace, verify that the Identity and Access Management (IAM) roles are granted correctly for Kubernetes, and skip directly to Set up Artifact Registry, in this document.

## Grant Identity and Access Management roles and specify a security contact for your project

To grant Identity and Access Management (IAM) roles and specify a security contact for your project, complete the following steps:

  1. Grant the following IAM roles at the project level:

     * Project Editor, to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`
     * Service Management Administrator (`roles/servicemanagement.serviceAdmin`), to `cloud-commerce-marketplace-onboarding@twosync-src.google.com` and `managed-services@cloud-marketplace.iam.gserviceaccount.com`
     * Config Editor (`roles/servicemanagement.configEditor`), to `cloud-commerce-producer@system.gserviceaccount.com`

For detailed instructions, see [Granting, changing and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Grant the following roles, at the service level, to `cloud-commerce-procurement@system.gserviceaccount.com`:

     * Service Consumer (`roles/servicemanagement.serviceConsumer`)
     * Service Controller (`roles/servicemanagement.serviceController`)

For steps to grant access at the service level, see [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access).

  3. Specify a security contact. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).




## Set up Artifact Registry

To set up Artifact Registry, complete the following steps:

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). To update an existing installation, run the command `gcloud components update`. Note: On Ubuntu, use the [Debian package](https://docs.cloud.google.com/sdk/docs/install#deb) to install gcloud CLI. The gcloud CLI snap package doesn't include `kubectl` or extensions for authenticating with Artifact Registry using the gcloud CLI.
  2. Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it isn't already installed.
  3. Turn on the Artifact Registry API, which lets you push to Artifact Registry.   
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)
  4. Create a staging Artifact Registry repository. For detailed steps, see [Store Docker container images in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).
  5. Turn on Artifact Analysis, which allows for security scanning, for your Artifact Registry repository.
  6. Tag and push the images that you want to distribute in your app to your staging Artifact Registry repository.



## Tag and push your images

To tag and push your images to Artifact Registry, complete the following steps:

  1. Choose your Artifact Registry staging repository path. We recommend that your repository uses the following structure: `us-docker.pkg.dev/YOUR_PARTNER_ID/YOUR_SOLUTION_ID`. Your staging repository must be within `us-docker.pkg.dev`. Cloud Marketplace doesn't support other regions or `gcr.io` domains, such as `europe-docker.pkg.dev`, `gcr.io`, or `eu.gcr.io`, for Terraform Kubernetes apps.
  2. Save or copy your staging repository path for when you create your product in Producer Portal.
  3. Build the image that you want to push to your Artifact Registry staging repository.
  4. Use Docker to tag the image with its version number, such as `1.0`:
         
         docker tag IMAGE_NAME STAGING_REPO_PATH:VERSION_NUMBER
         

For example, this command could be: `docker tag test-image us-docker.pkg.dev/testpartner/testsolution:1.0`.

  5. Use `gcloud` to push your image:
         
         gcloud docker push STAGING_REPO_PATH:tag
         

  6. For each additional tag or image that you'd like to add to your staging repository, repeat the previous steps. You can add multiple tags to a single image.




Pushing an image to your staging repository doesn't automatically make it visible to users. Your images become visible to users after you publish them.

**Note:** A repository's scope is the single level of the folder that its path specifies. Artifact Registry doesn't consider images contained within other folders of a repository as part of that repository. For example, if an image is in `.../testsolution/1.0`, it doesn't count as part of the `.../testsolution` repository. Artifact Registry handles `.../testsolution/1.0` as a separate repository.

## (Usage-based pricing only) Prepare your app to track usage

If your Terraform Kubernetes app supports usage-based pricing, you must make the following updates to your app's Helm chart.

### Configure the deployment file

In your Helm chart, in the corresponding `deployment.yaml` file for the main workload that you intend to monetize, configure the `cloudmarketplace.googleapis.com/product.metadata` annotation to be a single-line JSON string containing the deployment template, with the following format:
    
    
    "cloudmarketplace.googleapis.com/product.metadata": "v1:{\"services\":[{\"SERVICE_NAME\":\"{{ .Values.marketplace.SERVICE_NAME }}\", \"service_level\":\"{{ .Values.marketplace.SERVICE_LEVEL }}\"}]}"
    

#### Example deployment file

The following sample shows a configured annotation:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: "{{ .Release.Name }}-flask-app-deployment"
    spec:
      replicas: {{ .Values.replicaCount }}
      selector:
        matchLabels:
          app: flask-app-demo
      template:
        metadata:
          labels:
            app: flask-app-demo
          annotations:
            "cloudmarketplace.googleapis.com/product.metadata": "v1:{\"services\":[{\"service_name\":\"{{ .Values.marketplace.serviceName }}\", \"service_level\":\"{{ .Values.marketplace.serviceLevel }}\"}]}"
            {{- with .Values.podAnnotations }}
            {{- toYaml . | nindent 8 }}
            {{- end }}
        spec:
          containers:
            - name: flask-app-container
              image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
              imagePullPolicy: {{ .Values.image.pullPolicy }}
              ports:
                - containerPort: {{ .Values.containerPort }}
              readinessProbe:
                httpGet:
                  path: "/healthz"
                  port: {{ .Values.containerPort }}
                initialDelaySeconds: 30
                periodSeconds: 10
                failureThreshold: 6
              resources:
                {{- toYaml .Values.resources | nindent 12 }}
    

### Configure the values file

In your Helm chart, in the file `values.yaml`, ensure that the value of `serviceLevel` is set to `default`.

## Create a development cluster in Kubernetes Engine

You use Google Kubernetes Engine to manage and scale Kubernetes clusters. To create a test cluster and deploy a basic app to it, follow the [Google Kubernetes Engine quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

**Note:** If you aren't actively using your cluster for testing, consider deleting the cluster. If you want to keep the cluster and save on costs, you can resize the cluster, and change the number of nodes to zero. For steps to resize your cluster, see the [Google Kubernetes Engine documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-container-cluster).

## Organize your releases

In general, every version of your app must adopt [Semantic Versioning 2.0](https://semver.org/), which follows the `MAJOR.MINOR.PATCH` numbering convention. Each version must have a unique version number, such as `1.0.1`, `1.0.2`, or `1.3.1`. Optionally, to add a pre-release modifier, use a dash after the version number, such as `1.3.1-alpha201910`. You can use pre-release modifiers to store and highlight any additional information that you find useful, such as build dates denoting when versions were created.

We recommend that you release your software in _tracks_. Each track is a series of versions with backwards-compatible updates. Your release tracks should be based on minor versions, such as `4.1.x`. Avoid using generic version names, such as `newest`.

For example, if you're releasing version `2.0` of your app on Cloud Marketplace, and you expect that versions `2.0.1`, `2.0.5`, and later will be backwards-compatible with `2.0`, organize these releases under the `2.0` release track.

When you release a backward-incompatible version of your app, or a version that requires users to go through manual migration steps, release it on a new track, so that users can plan their updates.

## Create and upload your Terraform module wrapper to Cloud Storage

You must provide a Terraform module that Cloud Marketplace users can use to deploy your Terraform Kubernetes app. This module uses Helm Provider to deploy the Helm charts that you provided. For steps to create a Terraform module that's compatible with your Terraform Kubernetes app, see the [Terraform Kubernetes partner guide](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/mpdev-references.md) on GitHub.

### (UI deployment only) Create metadata for your custom Terraform module

For your custom module to support UI deployment, you must create and add metadata that Cloud Marketplace uses to correctly parse your module and render it in the UI for your customer.

To create and add this metadata, use the open source [CFT CLI tool](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata) to complete the following steps:

  1. Install the CFT CLI tool. We recommend that you specify the value of `VERSION` to be `latest`, and set `PLATFORM` to one of the following values:

     * `linux`
     * `windows`
     * `darwin`

For more information, visit the [CFT CLI documentation](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#pkg-overview).

  2. Run the following command:
         
         cft blueprint metadata -p TF_PACKAGE_PATH -q -d --nested=false
         

In this command, the flags are used as follows:

     * The `-p` flag provides a path for the Terraform package.
     * The `-q` flag generates metadata without needing information for a remote repository.
     * The `-d` flag generates the `metadata.display.yaml` file.
     * The `--nested=false` flag generates metadata for the root module, skipping any modules in the `modules/` folder.



After you've completed the previous steps, the CFT CLI tool generates the following files:

  * `metadata.yaml`
  * `metadata.display.yaml`



#### Customize your custom Terraform module's metadata

Cloud Marketplace uses the file `metadata.display.yaml` to create the form that customers use to deploy your product through the UI. To customize how the form appears to your customers, alter the values of the fields in `metadata.display.yaml`. For details of the available customization options, visit the open source [Blueprint UI documentation](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#BlueprintUI), or see the [Blueprint UI schema](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/cli/bpmetadata/schema/gcp-blueprint-metadata.json).

We recommend that you use the extension [`GooglePropertyExtensions`](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#GooglePropertyExtension) to alter your metadata. `GooglePropertyExtensions` lets you use validations that are specific to Google Cloud, such as enforcing that customers can only select Virtual Private Cloud (VPC) networks that already exist in their Google Cloud project. For an example, see the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/1b375ce22059b90a26a15f8e8c035cb9f559f597/examples/terraform/wordpress/metadata.display.yaml#L28-L171).

#### Validate your custom module's metadata

To validate your custom module's metadata, run the following command:
    
    
    cft blueprint metadata -p TF_PACKAGE_PATH -v
    

In the previous command, the flags act as follows:

  * The `-p` flag provides a path for the Terraform package.
  * The `-v` flag validates all metadata files under the provided path, based on the [`BlueprintMetadata` schema](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/cli/bpmetadata/schema/gcp-blueprint-metadata.json).



## Choose your product identifiers

You must select the following identifiers for your company, product, and container images, which are used to create your Cloud Marketplace URLs, and the URIs for your container images:

  * Your company's name. For example, if the name of your company is Examplesoft Inc., you can use the identifier `examplesoft`.
  * Your product's name. For example, if the product's name is Example Pro, use the identifier `example-pro`.
  * The release track of your product, such as `4.0`. For details, see Organize your releases, previously on this page.

**Caution:** The identifiers that you select appear in product URLs and container image URIs. It's difficult to change these identifiers after your app has been published to Cloud Marketplace customers.

### Sample product identifiers

For example, the company Examplesoft Inc. chooses the following identifiers for their product, Example Pro:

| Name | Identifier  
---|---|---  
Company | Examplesoft Inc | examplesoft  
Product | Example Pro | example-pro  
Helm chart | Helm chart | chart  
Image [1] | Example Database | example-db  
Image [2] | Example Queue | example-queue  
Release track [1] | Version 4.x.x | 4.0  
Release track [2] | Version 5.x.x | 5.0  
  
From these identifiers, the following information is automatically generated:

  * The product URL in Cloud Marketplace: `https://console.cloud.google.com/marketplace/details/examplesoft/example-pro`
  * The Artifact Registry URIs in your project: 
    * `us-docker.pkg.dev/examplesoft/example-pro/chart:4.0`
    * `us-docker.pkg.dev/examplesoft/example-pro/example-db:4.0`
    * `us-docker.pkg.dev/examplesoft/example-pro/example-query:4.0`
    * `us-docker.pkg.dev/examplesoft/example-pro/chart:5.0`
    * `us-docker.pkg.dev/examplesoft/example-pro/example-db:5.0`
    * `us-docker.pkg.dev/examplesoft/example-pro/example-query:5.0`



## What's next

After setting up your Google Cloud environment for Terraform Kubernetes apps, continue preparing your apps for publication by completing the following steps:

  * [Add your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/add-product) to Producer Portal.
  * [Add pricing information](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/select-pricing) for your app.
  * [Configure your app's deployment](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/configure-deployment), including its Helm chart and container images.



[ Previous arrow_back  Understand how customers see your deployment packages  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/customer-view-deployment-packages)

[ Next Add your Terraform Kubernetes app to Producer Portal  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/add-product)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
