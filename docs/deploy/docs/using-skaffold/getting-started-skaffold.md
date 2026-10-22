---
url: https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold/
title: Get Started with Skaffold in Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.545999+00:00
---

# Get Started with Skaffold in Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Get Started with Skaffold in Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to get started using [Skaffold](https://cloud.google.com/skaffold) as part of Cloud Deploy, including the following:

  * Configuring Skaffold for use with a Cloud Deploy delivery pipeline
  * Using Skaffold and Cloud Deploy with third-party rendering tools, such as Helm and Kustomize
  * Optionally, using Skaffold for local development
  * Optionally, using Skaffold for continuous integration and continuous deployment (CI/CD)



**Caution** : Skaffold [will be removed](https://groups.google.com/g/skaffold-users/c/FTR3xLJpePY) from gcloud CLI releases after January 15, 2027. Going forward, Skaffold can be installed following the instructions in the [Installing Skaffold documentation](https://skaffold.dev/docs/install/). On January 29, 2027 the Skaffold GitHub repository will be archived. All existing releases will remain available to users.

## Why Skaffold?

Want to know why Cloud Deploy uses Skaffold, and why you need to manage a Skaffold configuration? Read on.

### I'm experienced with CI/CD, but I don't use Skaffold currently

Skaffold is an open source command-line tool to improve productivity for developers. It orchestrates continuous development, continuous integration (CI), and continuous delivery (CD).

Skaffold provides declarative, portable configuration, using a pluggable architecture, letting you use different tools for the render phase.

When a release is created, Cloud Deploy calls Skaffold to render your manifests. At deploy time, Cloud Deploy calls Skaffold again to apply those manifests to deploy your application to each [target](https://docs.cloud.google.com/deploy/docs/terminology#target) in your [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression). After deployment, Skaffold performs health checks to monitor the target runtime for successful deployment.

### Skaffold for continuous development

When you use [Skaffold for continuous development](https://skaffold.dev/docs/workflows/dev/), images are built, tested, and deployed to a cluster (or Minikube) as you change your code. [Cloud Code for VS Code](https://cloud.google.com/code/docs/vscode/running-an-application) and [Cloud Code for IntelliJ](https://cloud.google.com/code/docs/intellij/deploying-a-k8-app) IDE extensions integrate Skaffold into Visual Studio Code and JetBrains IDEs, for continuous development.

### Skaffold for continuous delivery

You can also use [Skaffold for continuous delivery](https://skaffold.dev/docs/workflows/ci-cd/), with build, deploy, render, and apply steps. Cloud Deploy uses Skaffold's [render and apply](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) capabilities. To use Cloud Deploy, [you need at least a valid `skaffold.yaml` configuration file](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#whats_required_to_make_work).

Through Skaffold, you can also integrate with third-party manifest-management tools, such as [Helm](https://helm.sh), and [Kustomize](https://kustomize.io). Using Skaffold in this way lets you use the features of those tools to render manifests. `kubectl` remains the _deployer_ for these manifests.

### I'm new to deploying to Kubernetes

With Skaffold, you can configure a base set of manifests for all your deployments. You can then use Skaffold's rendering engine, through Cloud Deploy, to render, and then deploy, each deployment-specific manifest from one of those base manifests.

Read more about [managing manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests), including examples of using Skaffold and Cloud Deploy with common manifest-templating tools, such as Helm and Kustomize.

## What's required to make Cloud Deploy work?

To use a basic Cloud Deploy delivery pipeline, the [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml/) configuration file needs at least the following configuration:

  * The header information that all `skaffold.yaml` configurations need:
        
        apiVersion: skaffold/v4beta7
        kind: Config
        

  * A `manifests` stanza, for GKE, GKE attached clusters, or Cloud Run listing all raw Kubernetes manifests (unless you're using a manifest-management tool, such as Helm or Kustomize).

Here's an example using a raw Kubernetes manifest:
        
        manifests:
          rawYaml:
          - deployment.yaml
        

If you plan to use a renderer (like Helm or Kustomize) to render manifests, see Add Helm support to your skaffold.yaml and Add Kustomize support to your skaffold.yaml for guidance on how to configure Skaffold to use these tools.

For Helm and Kustomize examples, see [Manage manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests)

  * A `deploy` stanza, with either `deploy.kubectl`, for deploying to GKE or to GKE attached clusters, or `deploy.cloudrun` for deploying to Cloud Run.

For GKE and GKE attached clusters:
        
        deploy:
          kubectl: {}
        

The deploy stanza deploys the application manifests that were provided in the manifests stanza.

For Cloud Run targets:
        
        deploy:
          cloudrun: {}
        

The deploy stanza deploys the application manifests provided in the manifests stanza.




If you're using [custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets), your `skaffold.yaml` must have the header (`apiVersion` and `kind:`), plus the [custom actions](https://docs.cloud.google.com/deploy/docs/create-custom-target#skaffold_define_action) that the custom target will use if the custom target type doesn't already reference a [remote Skaffold configuration](https://docs.cloud.google.com/deploy/docs/create-custom-target#remote_skaffold).

### Create a `skaffold.yaml` file

Cloud Deploy uses Skaffold for rendering and deploying your applications.

For each release, you need to provide at least a `skaffold.yaml` file that identifies the manifests to use. See the [previous section](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#whats_required_to_make_work) for guidance about what needs to go in this file.

**Note:** The Cloud Code plugins [for VS Code](https://docs.cloud.google.com/code/docs/vscode/install) and [for IntelliJ](https://cloud.google.com/code/docs/intellij/install#installing) help with schema validation, completion, and documentation when you're working in Skaffold configuration files.

### Have Cloud Deploy generate your `skaffold.yaml`

If you don't have a `skaffold.yaml` file, but you do have a single Kubernetes manifest or a Cloud Run service definition file, Cloud Deploy can generate a `skaffold.yaml` file for you.

The generated Skaffold file will be available in the Cloud Storage source staging directory after the release is complete.

The following command includes the `--from-k8s-manifest` flag, passing the Kubernetes manifest. Cloud Deploy uses the information in the manifest to generate the `skaffold.yaml`, which is then used for the release.
    
    
    gcloud deploy releases create  RELEASE_NAME --delivery-pipeline=PIPELINE_NAME --from-k8s-manifest=MANIFEST --region=REGION
    

To generate the `skaffold.yaml` from a Cloud Run service YAML, use the same command, but with `--from-run-manifest` instead of `--from-k8s-manifest`

Using either of these flags with either the `--skaffold-file` flag or the `--source` flag generates an error.

**Caution:** This generated `skaffold.yaml` file isn't suitable for production workloads.**Note:** Besides having Cloud Deploy generate the file for you, you can also have Skaffold generate it. See the [Skaffold documentation](https://skaffold.dev/docs/pipeline-stages/init/) for more information.

#### Using the generated `skaffold.yaml` file

The generated `skaffold.yaml` is suitable for onboarding, learning, and demonstrating Cloud Deploy. After you're familiar with Cloud Deploy, and for production workloads, you might want a Skaffold configuration that differentiates among your targets (using Skaffold profiles).

When you use the generated `skaffold.yaml` file as a starting point to create your own differentiated Skaffold config, be sure you use the file in the rendering source archive, _not_ the rendered file. The rendering source is available to download from the **Artifacts** tab on the **Release details** page.

  * This generated `skaffold.yaml` is included in the render source stored in a Cloud Storage bucket.

You can view this file by downloading the `.tar.gz` file and extracting it.

  * The rendered `skaffold.yaml` is available in **Target artifacts**.

In the **Target artifacts** section, click **View artifacts**.

![Release details page, showing render source and target artifacts](https://docs.cloud.google.com/static/deploy/images/release_details_artifacts.png)




## Using Skaffold for local development

One of the strengths of Skaffold is that you can use it for [local development](https://skaffold.dev/docs/workflows/dev/), and for CI/CD. In `dev` mode, Skaffold watches your source files, and when it detects a change, Skaffold rebuilds the images, retests, and redeploys the containers to a minikube cluster (for example) on your local machine.

When using Skaffold in this way, you can use the same commands locally as for remote deployment.

If you use Skaffold for local development, you can define separate Skaffold profiles for your targets, and a default deploy stanza for local development.

When you stop `dev` mode, Skaffold cleans up deployed artifacts from the cluster.

## Using Skaffold for CI/CD

Besides using Skaffold for continuous local build and deploy, you can use Skaffold for CI/CD. Cloud Deploy uses the CI/CD features in Skaffold to render and apply your manifests and deploy your application to your defined targets, given container images built using a CI tool like [Cloud Build](https://docs.cloud.google.com/build) and an image registry like [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

### Render, deploy, and apply

Skaffold separates the manifest rendering process from deployment. Cloud Deploy calls [`skaffold render`](https://skaffold.dev/docs/references/cli/#skaffold-render), to render the manifests, and [`skaffold apply`](https://skaffold.dev/docs/references/cli/#skaffold-apply) to apply them to the [target](https://docs.cloud.google.com/deploy/docs/terminology#target).

This separation between render and apply lets you capture the full declarative state of your application in configuration, so that it can be applied safely and repeatably (for example, for rollbacks). This technique also makes approvals easier. Because manifests are rendered for all targets before the first rollout, you can see the rendered YAML that will be applied to each target.

Cloud Deploy doesn't support using other deployers to deploy your application. You can, however, use tools like [Helm](https://helm.sh/) or [Kustomize](https://kustomize.io/) for rendering.

To learn more about how Cloud Deploy deploys using `kubectl` as the deployer, see [Cloud Deploy Service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release).

### About Skaffold profiles

You can create separate Skaffold [profiles](https://skaffold.dev/docs/environment/profiles/)—identified in `skaffold.yaml`, in a `profiles:` stanza.

When using Skaffold profiles with Cloud Deploy, you might create separate profiles for all, or some, of your targets. For example, different profiles for `dev`, `staging`, and `prod`.

Profiles aren't necessary in order to use Skaffold in Cloud Deploy, but are useful for defining manifest customizations among your targets, for example using different Kustomize `kustomization.yaml` files per target.

### Add Kustomize support to your `skaffold.yaml`

Integrating your Kustomize configuration with your Cloud Deploy/Skaffold configuration consists of the following:

  1. Include a `kustomization.yaml` file among your configuration files.

You can store your configuration files in a local directory or in a Cloud Storage bucket.

  2. In your `skaffold.yaml` file, create a `deploy` stanza for each profile.

You can also have a `deploy` stanza outside of any defined profiles, if you're not using profiles or for a default deploy configuration not tied to a profile.

The following is an example Skaffold config that shows `deploy` stanzas per profile, and uses a fictional sample app called `my-app`:
         
         apiVersion: skaffold/v4beta7
         kind: Config
         build:
           artifacts:
             - image: my-app-web-profiles
               context: my-app-web-profiles
             - image: my-app-application-profiles
               context: my-app-application-profiles
           googleCloudBuild:
             projectId: ${PROJECT_ID}
         profiles:
         - name: local
           manifests:
             kustomize:
               paths:
                 - my-app-application-profiles/kubernetes/local
         - name: test
           manifests:
             kustomize:
               paths:
                 - my-app-application-profiles/kubernetes/test
         - name: staging
           manifests:
             kustomize:
               paths:
                 - my-app-application-profiles/kubernetes/staging
         - name: prod
           manifests:
             kustomize:
               paths:
                 - my-app-application-profiles/kubernetes/prod
         deploy:
           kubectl: {}
         

The Skaffold configuration shown here has separate profiles for `test`, `staging`, and `prod` targets. It also shows a profile for local development. In each profile, there's a `deploy.kustomize` stanza with a path that points to the location of the kustomization to use for that target.


**Note:** although this configuration is in a `deploy` stanza, Skaffold uses it to _render_ the manifest for the intended target, not to deploy.

### Add Helm support to your `skaffold.yaml`

You can use Helm to render your manifests. Cloud Deploy doesn't use Helm to deploy your applications, and supports only `kubectl` as a deployer.

To use Helm, you need your Helm chart or charts, stored in any location you can reference from within your `skaffold.yaml`. This location can be in a file system, a repository, possibly along with your `skaffold.yaml`, or an Open Container Initiative (OCI) repository.

To use a Helm chart, you add a `helm` stanza to your [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml/) file.

**Note:** You can also use Helm with Skaffold profiles.
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    build:
      artifacts:
      - image: skaffold-helm-image
    manifests:
      helm:
        releases:
        - name: skaffold-helm-image
          chartPath: charts
    deploy:
      kubectl: {}
    

The [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/#deploy-helm) shows what's required in this `helm` stanza.

## Unsupported Skaffold features

The following features of Skaffold can't be used in Cloud Deploy:

  * [Lifecycle hooks](https://skaffold.dev/docs/pipeline-stages/lifecycle-hooks/)

  * [Dynamic Skaffold modules](https://skaffold.dev/docs/design/config/#multiple-configuration-support)

Using `--module=` to select specific modules for `build`, `render`, `apply`, and so on, is not supported. Static modules are supported.

  * In Helm, the ability to [create a namespace](https://helm.sh/docs/faq/changes_since_helm2/#automatically-creating-namespaces) if one doesn't exist.




## What's next

  * Visit the [Skaffold site](https://skaffold.dev) to find out about how it works and what it can do for you.

  * [Practice](https://shell.cloud.google.com/?show=ide%2Cterminal&walkthrough_id=deploy--cloud-deploy-profiles-gke) using Cloud Deploy with Kustomize and Skaffold profiles.

  * [Learn how](https://docs.cloud.google.com/deploy/docs/select-tool-version) Cloud Deploy selects the tool versions to use and how to determine which versions are in use.

  * [Learn how](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to use Skaffold profiles with advanced manifest-management tools like Helm, Kustomize, and kpt.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
