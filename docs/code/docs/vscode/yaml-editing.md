---
url: https://docs.cloud.google.com/code/docs/vscode/yaml-editing/
title: Work with Google Cloud and Kubernetes YAML in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:14.282829+00:00
---

# Work with Google Cloud and Kubernetes YAML in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/yaml-editing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Work with Google Cloud and Kubernetes YAML in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code for VS Code is designed to make Kubernetes and Cloud Build configuration easier by linting schema for both structure and valid values and providing descriptive errors. Cloud Code comes with out-of-the-box solutions for common schema, smart completions, and documentation on hover.

**Note:** Cloud Build YAML editing support is only available for files named `cloudbuild.yaml`.

## Supported YAML configuration files

  * [Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/configs)
  * [Cloud Build](https://docs.cloud.google.com/build/docs/build-config)
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview)
  * [Istio](https://istio.io/docs/setup/getting-started/)
  * [Knative](https://knative.dev/docs/)
  * [Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
  * [Kustomize](https://github.com/kubernetes-sigs/kustomize)
  * [Skaffold](https://skaffold.dev/docs/references/yaml/)



Cloud Code also supports popular Kubernetes custom resource definitions (CRDs), like [Kubeflow](https://www.kubeflow.org/docs/about/kubeflow/), out-of-the-box.

### Use custom schema

With Cloud Code, you can provide your own CRD schema with the `cloudcode.yaml.crdSchemaLocations` setting in your [`settings.json`](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations) file. You can point to either a local file or a URL. URLs pointing to `github.com` are automatically converted to `raw.githubusercontent.com`.

### Pull schema from a cluster

When you switch to a cluster running Kubernetes v1.16 and later in the Kubernetes view, Cloud Code automatically pulls the schema of all installed CRDs.

## Configure with snippets

Out-of-the-box snippets for common YAML schema (using `Command/Ctrl+Space` to view options) make it easy to start a new YAML file or add to an existing one without errors, while still following best practices. Cloud Code makes it easier to work with repetitive fields by filling out the remaining instances after you fill in the first field.

Cloud Code offers the following snippets:

  * `Anthos Config Management - Cluster`
  * `Anthos Config Management - Cluster Selector`
  * `Anthos Config Management - Config Management`
  * `Anthos Config Management - Namespace Selector`
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
  * `Kubernetes - Secret`
  * `Kubernetes - Service`
  * `Migrate to Containers - Export`
  * `Migrate to Containers - PersistentVolumeClaim`
  * `Migrate to Containers - StatefulSet`
  * `Skaffold - Bazel`
  * `Skaffold - Getting-started`
  * `Skaffold - Helm deployment`
  * `Skaffold - Kaniko`



## Complete with context

Based on the current schema, Cloud Code provides contextual completions and relevant docs to help you choose the right option.

![Context completions for Kubernetes schema](https://docs.cloud.google.com/static/code/docs/vscode/images/YAMLsuggestAndDoc.png)

## Validate YAML schema

Cloud Code offers schema validation support by flagging invalid tags and values in your YAML files and suggesting fixes when possible.

![Value of name field red-underlined to highlight an invalid value of 1234; hover text states: Incorrect type. Expected string.](https://docs.cloud.google.com/static/code/docs/vscode/images/YAMLvalidation.png)

## Discover documentation on hover

Cloud Code surfaces relevant documentation when you hold the pointer over a value in the schema.

![Documentation info when you hold the pointer over a value in the  schema](https://docs.cloud.google.com/static/code/docs/vscode/images/YAMLhoverDocs.png)

## Access resource definitions

To view definitions for a resource, right-click the resource and then choose **Go to Definition** or **Peek Definition**.

## Apply a YAML file

To apply a configuration change using the current file, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: Apply Current JSON/YAML File to K8s Deployed Resource**.

This command brings up a diff view for you to review changes. Click **Apply** when prompted whether to apply this change. This runs [`kubectl apply -f`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply).

## View differences between YAML files

To view the differences between a YAML file in source control and a deployed YAML file, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: Diff Current JSON/YAML File with K8s Deployed Resource**.

## Perform a dry-run of a YAML file

Cloud Code performs dry runs automatically as you type information in your YAML file and underlines any errors with a yellow squiggly line.

Yellow squiggly lines appear when the server considers a part of your code an error based on the result of a dry run. This can include policy violations, duplicate names, or validations that Cloud Code doesn't perform on the client side (like max port numbers).

To view the description of the error in your YAML file, hold your pointer over the code with a yellow underline.

![Server-side dry-run validation fails on `hello.deployment.yaml` with an error message displayed as a toast. The details of the error are found in the Output channel; the namespace 'random-namespace' doesn't exist](https://docs.cloud.google.com/static/code/docs/vscode/images/namespace-error-dryrun.png)

Red squiggly lines appear for detected errors before Cloud Code checks with the Kubernetes server. For example, putting a number where a string is expected triggers a red squiggly line.

## Work with secrets

Using configuration maps and [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) is a key part of working with Kubernetes. To view the context of a base64 secret with Cloud Code, hold the pointer over the secret to decode it.

![Decode secret by holding the pointer over the secret](https://docs.cloud.google.com/static/code/docs/vscode/images/YAMLsecretDecode.png)

## What's next

  * Create a [Cloud Code Kubernetes run configuration](https://docs.cloud.google.com/code/docs/vscode/use-existing-app#set_up_kubernetes_run_configuration) `skaffold.yaml` file.
  * Manually create a [Skaffold configuration](https://docs.cloud.google.com/code/docs/vscode/use-existing-app#manually_create_a_skaffold_configuration) for your application.
  * View the [`Skaffold.yaml` reference docs](https://skaffold.dev/docs/references/yaml/).



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
