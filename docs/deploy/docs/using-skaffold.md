---
url: https://docs.cloud.google.com/deploy/docs/using-skaffold/
title: Use Skaffold with Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:34.701347+00:00
---

# Use Skaffold with Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/using-skaffold/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Use Skaffold with Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

This article describes [Skaffold](https://cloud.google.com/skaffold), how and why Cloud Deploy uses it, and what you need to do to make it work for you.

**Caution** : Skaffold [will be removed](https://groups.google.com/g/skaffold-users/c/FTR3xLJpePY) from gcloud CLI releases after January 15, 2027. Going forward, Skaffold can be installed following the instructions in the [Installing Skaffold documentation](https://skaffold.dev/docs/install/). On January 29, 2027 the Skaffold GitHub repository will be archived. All existing releases will remain available to users.

Cloud Deploy uses Skaffold for render and deploy operations. You can also use it for local development, build, test, and for [advanced deployment features](https://skaffold.dev/docs/pipeline-stages/). However, Cloud Deploy _requires_ only a Skaffold [configuration](https://skaffold.dev/docs/references/yaml) that identifies the manifests to render and apply.

**Note:** You don't need to install Skaffold. It's included as part of Cloud Deploy.

## What is Skaffold?

Skaffold is a command-line tool that enables continuous development for Kubernetes-native applications. You can use Skaffold to configure a local development workspace to use with Cloud Deploy continuous delivery pipelines.

Skaffold includes the following features:

  * It gives you discrete control of CI/CD pipeline activities (build, render, test deploy, and so on).

  * It's useful as a local development tool.

  * Skaffold profiles let you differentiate among different environments, with different build, test, and deploy configurations, all in the same configuration file.




## Why does Cloud Deploy use Skaffold?

Google Cloud Deploy uses Skaffold to separate rendering tools from the delivery pipeline. Your delivery pipeline simply defines the progression from target to target, while your Skaffold configuration defines which manifests are rendered and how. This makes manifest rendering flexible without affecting how you define your delivery pipeline.

Here are some of the advantages that Skaffold provides when you use it with Cloud Deploy:

  * **Easy onboarding**

Start with a local development loop. You can share your `skaffold.yaml` file with your team, which can enable consistency and help new team members get started.

  * **Consistent control** over rendering across diverse deployment targets

You can use Skaffold profiles, with different rendering and deployment for different targets.

  * **Choice of rendering tools** without compromising how delivery pipelines are defined

Using Skaffold allows Cloud Deploy to separate delivery pipeline definition from render details. This separation lets you experiment with your manifests without disrupting the delivery pipeline.

  * **Coherent rendering process**

The rendering source plus your containers are use to generate rendered manifests.

  * **Deployment health checks**

Skaffold performs them, and Cloud Deploy uses them.




## How does Cloud Deploy use Skaffold?

  * The rendering source and references to container images are passed to Cloud Deploy when you [create a release](https://docs.cloud.google.com/deploy/docs/integrating-ci#calling_from_your_ci_pipeline).

As part of release creation, Cloud Deploy calls Cloud Build, which, in turn, invokes [`skaffold diagnose`](https://skaffold.dev/docs/references/cli/#skaffold-diagnose) and [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) to render the manifest or manifests using that rendering source and those images.

  * You can use [Skaffold profiles](https://skaffold.dev/docs/environment/profiles/) to differentiate manifests that will be applied to different targets.

  * Cloud Deploy [supports _static_ Skaffold modules](https://skaffold.dev/docs/design/config/#local-config-dependency).

  * When deploying, Cloud Deploy calls [`skaffold apply`](https://skaffold.dev/docs/workflows/ci-cd/#example-hydrate-manifests-then-deployapply-to-cluster) to apply the rendered manifest or manifests to the target cluster.

  * Cloud Deploy doesn't support the use of other deployers to deploy your application, unless you use [custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets). However, you can use tools like [Helm](https://helm.sh/) or [Kustomize](https://kustomize.io/) as renderers. To learn more about how Cloud Deploy deploys without using specific deployers (like Helm), see [Service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release).




## Make Skaffold work for you

  1. Configure Skaffold according to your pipeline needs.

     1. Determine the needs of your delivery pipeline.

How many targets will you have? Are rendering and deployment the same for each. If configuration is the same for each target in your progression, you won't need to use Skaffold profiles. You only need a `skaffold.yaml` file that describes the manifests to render.

     2. If applicable, create a Skaffold profile for each target

Define this in your `skaffold.yaml` file and bind in your delivery pipeline definition progression sequence.

See the [Skaffold documentation](https://skaffold.dev/docs/environment/profiles/) for more information about Skaffold profiles. Also, the document [Managing manifests in Cloud Deploy](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) includes example profile configurations.

     3. Set the Skaffold logging verbosity level

By default, the [Skaffold logging level](https://skaffold.dev/docs/references/cli/#global-flags) is set to `warn`. You can change that to `debug` in the configuration for a target's [execution environment](https://docs.cloud.google.com/deploy/docs/config-files#executionconfigs) by setting `verbose: true`.

  2. Connect Cloud Deploy to your continuous-integration system.

[At the end of your CI](https://docs.cloud.google.com/deploy/docs/integrating-ci) process, pass the `skaffold.yaml`, the rendering source, and the container images to be populated into the rendered manifest.

  3. **Optional** : set up your local development loop, using Skaffold.

[Using Skaffold for development](https://skaffold.dev/docs/workflows/dev/) is optional in Cloud Deploy. The only thing that's required in order for Cloud Deploy to operate is a `skaffold.yaml` file that identifies manifests to render.




## What's next

  * Visit the [Skaffold site](https://skaffold.dev) to find out about how it works and what it can do for you.

  * [Learn how](https://docs.cloud.google.com/deploy/docs/select-tool-version) Cloud Deploy selects the tool versions to use and how to determine which versions are in use.

  * [Learn how](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to use Skaffold profiles in conjunction with advanced manifest-management tools like Helm, Kustomize, and kpt.

  * Try out the [Skaffold profiles walkthrough](https://shell.cloud.google.com/?show=ide%2Cterminal&walkthrough_id=deploy--cloud-deploy-profiles-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
