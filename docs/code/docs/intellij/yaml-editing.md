---
url: https://docs.cloud.google.com/code/docs/intellij/yaml-editing/
title: Work with Google Cloud and Kubernetes YAML files in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:58.564001+00:00
---

# Work with Google Cloud and Kubernetes YAML files in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/yaml-editing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Work with Google Cloud and Kubernetes YAML files in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code is designed to help with editing Google Cloud and Kubernetes-related configuration files, including schema based validation, diagnostics, and quick documentation.

**Note:** For compatibility reasons, Kubernetes editing features are automatically disabled if the JetBrains Kubernetes plugin is detected. Manually override this in the Cloud Code settings menu by navigating to **Cloud Code** > **Kubernetes** > **Kubernetes editing features** and toggling the **Enable Kubernetes YAML configuration editing features** setting. These compatibility measures only affect Kubernetes YAML files. **Note:** Cloud Build YAML editing support is only available for files named `cloudbuild.yaml`

## Supported YAML configuration files

  * [Anthos Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/configs)
  * [Cloud Build](https://docs.cloud.google.com/build/docs/build-config)
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview)
  * [Knative](https://knative.dev/docs/)
  * [Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
  * [Kustomize](https://github.com/kubernetes-sigs/kustomize)
  * [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs/getting-started)
  * [Skaffold](https://skaffold.dev/docs/references/yaml/)



Cloud Code also supports popular Kubernetes CRDs, like [Kubeflow](https://www.kubeflow.org/docs/about/kubeflow/), out-of-the-box.

**Note:** To use the most up-to-date resource aggregation, you'll need the latest version of Cloud Code.

### Enable or disable YAML support

To enable or disable YAML support, navigate to **File** > **Settings** > **Tools** > **Gemini + Google Cloud Code** > **Kubernetes** (for Windows and Linux) or **IntelliJ IDEA** > **Settings** > **Tools** > **Gemini + Google Cloud Code** > **Kubernetes** (for macOS) and select or clear the **Enable YAML support** checkbox to enable or disable the feature.

### Use custom schema

With Cloud Code, you can provide your own CRD schema with IntelliJ settings by navigating to **File** > **Settings** > **Tools** > **Gemini + Google Cloud Code** > **Kubernetes** (For Windows and Linux) or **IntelliJ IDEA** > **Settings** > **Tools** > **Gemini + Google Cloud Code** > **Kubernetes** (for macOS) and then refer to the **CRD schema locations** section.

You can point to either a local file or a URL. URLs pointing to `github.com` are automatically converted to `raw.githubusercontent.com`.

### Pull schema from a cluster

When you switch to a cluster running Kubernetes `v1.16+` in the [Kubernetes Explorer](https://docs.cloud.google.com/code/docs/intellij/use-kubernetes-explorer#clusters), Cloud Code automatically pulls the schema of all installed CRDs.

### Additional Skaffold support

[Skaffold](https://skaffold.dev/docs/) is the underlying engine that powers Cloud Code, helping you build, push, and deploy your application as well as providing support for creating CI/CD pipelines.

Cloud Code comes with additional support for managing `skaffold.yaml` configuration files. When you open a project, Cloud Code detects schemas that aren't up-to-date and prompts you (through the Event Log) when a schema version upgrade is available for your existing `skaffold.yaml` configuration files.

![Notification in the Event log prompting user to upgrade their schema version because their existing `skaffold.yaml` files are not of the latest version](https://docs.cloud.google.com/static/code/docs/intellij/images/upgrade-skaffold-schema.png)

Alternatively, you can navigate to **Tools** > **Gemini + Cloud Code** > **Kubernetes** > **Check for Skaffold Schemas Upgrades** to check for available schema upgrades.

## Configure with snippets

Out-of-the-box snippets for common YAML schema (using `Ctrl+Space` to view options) allow you to start a new YAML file or add to an existing one without errors, while still following best practices. Additionally, it's easier to work with repetitive fields; fill in one and Cloud Code fills out the remaining instances.

![Using snippets with repetitive fields](https://docs.cloud.google.com/static/code/docs/intellij/images/lsp-snippet.gif)

Cloud Code offers the following snippets:

  * `Cloud Build - Cloud Run deployment`
  * `Cloud Build - Docker container build`
  * `Cloud Build - GKE deployment`
  * `Cloud Build - GKE Skaffold deployment`
  * `Cloud Build - Go build`
  * `Cloud Build - Terraform plan + apply`
  * `Config Connector - BigQueryDataset`
  * `Config Connector - BigQueryTable`
  * `Config Connector - BigtableCluster`
  * `Config Connector - BigtableInstance`
  * `Config Connector - PubSubSubscription`
  * `Config Connector - PubSubTopic`
  * `Config Connector - RedisInstance`
  * `Config Connector - SpannerInstance`
  * `Kubernetes - ConfigMap`
  * `Kubernetes - Deployment`
  * `Kubernetes - Ingress`
  * `Kubernetes - Pod`
  * `Kubernetes - Service`
  * `Migrate to Containers - Export`
  * `Migrate to Containers - PersistentVolumeClaim`
  * `Migrate to Containers - StatefulSet`
  * `Skaffold - Bazel`
  * `Skaffold - Getting-started`
  * `Skaffold - Helm deployment`
  * `Skaffold - Kaniko`



## Complete with context

Based on the current schema, Cloud Code provides contextual completions to help you choose the right option.

![Context completions for Kubernetes schema](https://docs.cloud.google.com/static/code/docs/intellij/images/lsp-completion.png)

## Validate YAML schema

Cloud Code offers schema validation support by flagging invalid tags and values in your YAML files and suggesting fixes when possible.

![Value of name field red-underlined to highlight an invalid value of 1234; hover text states: Incorrect type. Expected string.](https://docs.cloud.google.com/static/code/docs/intellij/images/YAML-validation.png)

## Validate `skaffold.yaml` files

Cloud Code provides additional `skaffold.yaml` file editing support and smart templates which allow you to validate your `skaffold.yaml` files. Refer to this [guide on using an existing app with Cloud Code](https://docs.cloud.google.com/code/docs/intellij/use-k8s-existing-app).

![Skaffold yaml templates](https://docs.cloud.google.com/static/code/docs/intellij/images/skaffold-yaml-template.png)

## Complete `skaffold.yaml` files with context

Based on the current schema, Cloud Code provides contextual completions and relevant documentation to help you choose the right option.

![Skaffold completions](https://docs.cloud.google.com/static/code/docs/intellij/images/skaffold-completions.png)

## Discover definitions using quick documentation

Cloud Code surfaces relevant documentation for a resource when you highlight a line in your configuration file and navigate to **View** > **Quick Documentation**.

![Quick documentation](https://docs.cloud.google.com/static/code/docs/intellij/images/lsp-hover-doc.png)

## Lint YAML for structural and validity issues

Cloud Code provides linting support around common schema issues and provides descriptive errors.

![Linting YAML files](https://docs.cloud.google.com/static/code/docs/intellij/images/lsp-diagnostic.png)

## Apply a YAML file

To run `kubectl apply -f` to apply a configuration change using the current file, you can use the kubectl actions icon ![kubectl actions icon](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-icon.png), available in the gutter of your IDE, and select **Apply**. This brings up a diff view for you to review changes before clicking **Apply**.

![Apply option highlighted in the kubectl action list](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-apply.png)

## Diff between YAML files

To view the differences between a YAML file in source control and a deployed YAML file, you can use the kubectl actions icon ![kubectl actions icon](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-icon.png) available in the gutter of your editor. Select the **Diff** option to see a diff view for you to compare and contrast two schema files.

![Diff option highlighted in the kubectl action list](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-diff.png)

## Perform a dry-run of a YAML file

To perform a dry run of your file and check its validity, you can use the kubectl actions icon ![kubectl actions icon](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-icon.png), available in the gutter of your IDE, to select **Dry-run on Server** or **Dry-run on Client**. This runs `kubectl apply -f dry-run=server` (or `kubectl apply -f dry-run=client`, for the Client option) and notifies you if your file can successfully be created in your Terminal window.

![Dry-run on Server option highlighted in the kubectl action list](https://docs.cloud.google.com/static/code/docs/intellij/images/kubectl-actions-dryrun.png)

## What's next

  * Create a [Cloud Code Kubernetes run configuration](https://docs.cloud.google.com/code/docs/intellij/use-k8s-existing-app#set_up_kubernetes_run_configuration) `skaffold.yaml` file.
  * Manually create a [`skaffold.yaml` configuration](https://docs.cloud.google.com/code/docs/intellij/use-k8s-existing-app#manually_create_a_skaffold_configuration) for your application.
  * View the [`skaffold.yaml` reference docs](https://skaffold.dev/docs/references/yaml/).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
