---
url: https://docs.cloud.google.com/deploy/docs/parameters/
title: Pass parameters to your deployment \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:48.165784+00:00
---

# Pass parameters to your deployment  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Pass parameters to your deployment Stay organized with collections  Save and categorize content based on your preferences. 

Using Cloud Deploy, you can pass parameters for your release, and those values are provided to the manifest or manifests before those manifests are applied to their respective targets. This substitution is done _after_ manifests are [rendered](https://docs.cloud.google.com/deploy/docs/terminology#render), as the final step in the Cloud Deploy render operation. Values are provided to all manifests identified in your `skaffold.yaml` file that contain the corresponding placeholders.

All you need to do is include placeholders in your manifest, and set the values for those placeholder in either your Cloud Deploy delivery pipeline or target configuration, or when you create a release.

This article describes how to make that happen.

## Why use deploy parameters?

A typical use for this would be to apply different values to manifests for different targets in a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel). But you can use deploy parameters for anything that requires post-render key-value pair substitution in your manifest.

## How it works

The following steps describe the general process for configuring deploy parameters and providing values:

  1. You configure deploy parameterization, as described here.

This includes the following:

     * Add the placeholders to your manifest, including a default value for each.

     * Add values for those placeholders.

There are three ways to do this, described here.

  2. When you create a release, your manifest is [rendered](https://docs.cloud.google.com/deploy/docs/terminology#render).

If you start with a templated manifest, values are applied now for template variables. If you start with a raw manifest, it remains unchanged. This rendering is done by [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold).

However, you can have additional variables in your manifest for which values aren't applied at render time. These are the deploy parameters described in this document.

At release creation, all deploy parameters are compiled into a dictionary, which is used to substitute values before the manifests are applied.

**Note:** If a given deploy parameter (key) is assigned more than one value, the release fails.
  3. After rendering, Cloud Deploy substitutes values for deploy parameters.

These are the values you configured in the first step.

The _rendering_ process already applied values to manifest templates, replacing some values, and adding labels specific to Cloud Deploy. But the values for these deploy parameters are substituted after rendering. The differences between manifest templates and deploy parameters are described here.

  4. The manifest is applied to the target runtime, to deploy your application.

This includes the values substituted at render time, and the values for any deploy parameters




## Different ways to pass values

You can provide parameters, and values for those parameters in three ways:

  * In the delivery pipeline definition

You provide the parameter and its value in the definition for a stage in the delivery pipeline progression. The parameter is passed to the target represented by that stage. If that stage references a multi-target, the values set here are used for all child targets.

This method lets you replace a value for all releases within a given pipeline, for all affected targets. The parameters defined for a stage identify a label, and the corresponding target for that stage must have a matching label.

  * In the target definition

You configure the parameter and its value in the definition for the target itself. This method lets you replace a value for that target for all releases.

  * On the command line, when you create a release

You include the parameter and its value using the `--deploy-parameters` flag on the `gcloud deploy releases create` command.

This method lets you replace a value at release creation time, applying that value to that manifests of all affected targets.




Configuration for these is explained in more detail here.

### Can I use more than one of these methods?

Yes, you can include deploy parameters in the pipeline stage, in the target config, _and_ on the command line. The result is that all the parameters are accepted and added to the dictionary. However, if a specific parameter is passed in more than one place, but with different values, the `gcloud deploy releases create` command fails with an error.

## How is this different from manifest templates

Deploy parameters, as described in this article, are distinguished from placeholders in a templated manifest by the syntax. But if you're wondering why you would need deploy parameters instead of just using the standard techniques for templated manifests, the following table shows the different purposes:

Technique | Substitution time | Applies to  
---|---|---  
[Manifest template](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) | Rendering phase | Specific release; specific target  
On command line | Post-rendering | Specific release; all targets  
On delivery pipeline | Post-rendering | All releases; specific targets (by label)  
On target | Post-rendering | All releases; specific target  
  
This document is about deploy parameters only (on command line, pipeline, and target), not [templated manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests).

## Limitations

  * For each type of parameter, you can create a maximum of 50 parameters.

  * A child target can additionally inherit up to 50 parameters from its parent multi-target, up to a maximum of 200 parameters on the targets, including those set on the pipeline stage.

  * The key name is limited to a maximum of 63 characters, and the following regular expression:
        
        ^[a-zA-Z0-9]([-A-Za-z0-9_.]{0,61}[a-zA-Z0-9])?$
        

One exception to this is when you're using a deploy parameter as an environment variable in a custom target, you must use a slash between the keyword `customTarget` and the variable name (`customTarget/VAR_NAME`). See [Required inputs and outputs](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs) for the supported syntax.

  * The prefix `CLOUD_DEPLOY_` is reserved, and cannot be used for a key name.

  * You can't have two keys of the same name applied to the same target.

  * The value can be empty, but has a maximum of 512 characters.

  * Deploy Parameters placeholders can't be used for [Helm configuration values](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing), but must be passed by convention.




## Configure deploy parameters

This section describes how to configure deploy parameter values that will be applied to your Kubernetes manifest, your Cloud Run service, or your Helm template.

Besides configuring those key-value pairs, you need to add the placeholder or placeholders to your manifest, as described in this section.

### Add placeholders to your manifest

In your Kubernetes manifest (for GKE) or service YAML (for Cloud Run), you add placeholders for any values you want to substitute after rendering.

#### Syntax

For releases that aren't using the Helm renderer with Skaffold, use the following syntax for your placeholders:
    
    
    [PROPERTY]: [DEFAULT_VALUE] # from-param: ${VAR_NAME}
    

In this line...

  * PROPERTY:

Is the configuration property in your Kubernetes manifest or Cloud Run service YAML.

  * DEFAULT_VALUE

Is a value to use if there are no values provided for this property on the command line or in the pipeline or target config. The default value is required, but it can be an empty string (`""`).

  * # from-param:

Uses a comment character to set off the Cloud Deploy `deploy-parameters` directive, and `from-param:` tells Cloud Deploy that a `deploy-parameters` placeholder follows.

  * ${VAR_NAME}

Is the placeholder to substitute. This must match the key of a key-value pair provided in the delivery pipeline or target config, or upon release creation.




You can also use multiple parameters in a single line, and use the parameters as part of a longer string, for example:
    
    
    image: my-image # from-param: ${artifactRegion}-docker.pkg.dev/my-project/my-repo/my-image@sha256:${imageSha}
    

These parameters can come from multiple sources. In the previous example, `${artifactRegion}` would probably be defined on the target or delivery pipeline stage, whereas `${imageSha}` would come from the command line at release creation time.

#### Parameters for Helm chart values

If you are rendering a Helm chart that accepts [configuration values](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing), and you want to set those values using deploy parameters, the deploy parameters must have names that match the Helm configurations values that you want to set. All deploy parameters are passed to Helm as `--set` arguments at render time, with no modification of your `skaffold.yaml` required.

For example, if your `skaffold.yaml` is installing a Helm chart that takes a configuration parameter of `webserver.port` to specify which port the web server would be starting on, and you want to set this dynamically from a deploy parameter, you would need to create a deploy parameter with the name `webserver.port` with the value you want for the web server port.

Therefore if you are not only referencing Helm templates in your `skaffold.yaml`, but also authoring them, you can utilise the [standard Helm variable syntax](https://helm.sh/docs/chart_template_guide/variables/) of `{{ .Values.VAR_NAME }}` in your Helm templates.

For example, if we have a deploy parameter of `webserver.port` configured, we could utilise it like so:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: webserver
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: webserver
      template:
        metadata:
          labels:
            app: webserver
        spec:
          containers:
          - name: webserver
            image: gcr.io/example/webserver:latest
            ports:
            - containerPort: {{ .Values.webserver.port }} # replaced by deploy parameter `webserver.port`.
              name: web
            env:
            - name: WEBSERVER_PORT
              value: {{ .Values.webserver.port }} # replaced by deploy parameter `webserver.port`.
    

### Add a parameter to the pipeline stage

You can add key-value pairs to a stage in the delivery pipeline progression. This is useful for [parallel deployments](https://docs.cloud.google.com/deploy/docs/parallel), to distinguish among child targets.

  1. Add the placeholders to your Kubernetes manifest or Cloud Run service, as described here.

Here's an example:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: nginx-deployment
          labels:
            app: nginx
         spec:
          replicas: 1 # from-param: ${deploy_replicas}
          selector:
            matchLabels:
              app: nginx
          template:
            metadata:
              labels:
                app: nginx
            spec:
              containers:
              - name: nginx
                image: nginx:1.14.2
                ports:
                - containerPort: 80
         

  2. Configure your delivery pipeline to include `deployParameters` for the applicable pipeline stage.

The following YAML is the configuration for a pipeline stage whose target is a multi-target, which in this case has two child targets:
         
         serialPipeline:
          stages:
            - targetId: dev
              profiles: []
            - targetId: prod  # multi-target
              profiles: []
              deployParameters:
                - values:
                    deploy_replicas: 1
                    log_level: "NOTICE"
                  matchTargetLabels: # optional, applies to all resources if unspecified; AND'd
                    my-app: "post-render-config-1"
                - values:
                    deploy_replicas: 2
                    log_level: "WARNING"
                  matchTargetLabels: # optional, applies to all resources if unspecified; AND'd
                    my-app: "post-render-config-2"
         

In this delivery pipeline configuration, the `deployParameters` stanza includes two `values`, each of which has the following:

     * The variable name, which is the same name as the variable you set in the manifest

     * A value for that variable

     * One or more labels (optional) to match against target-specific labels

If you don't specify a label, in a `matchTargetLabels` stanza, that value is used for all targets in the stage.

  3. If you included `matchTargetLabels` , you also must include labels on the targets, to match them. In this way, you identify which value to assign to which child target.

The target must match _all_ labels set in the `values` stanza.

If you omit `matchTargetLabels`, the `values` you set on the pipeline are applied to all child targets. But if you set more than one value for the same parameter, the release will fail.




After each manifest is rendered, Cloud Deploy adds the value for each variable into the rendered manifest.

### Add a parameter to the target configuration

You can add key-value pairs to a target. If you're using deploy parameters to distinguish among multiple child targets, configure them on those child targets, not on the multi-target.

  1. Configure your Kubernetes manifest or Cloud Run service definition using a parameter in place of the value you want to set at deploy time.

Here's an example:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: nginx-deployment
          labels:
            app: nginx
         spec:
          selector:
            matchLabels:
              app: nginx
          template:
            metadata:
              labels:
                app: nginx
            spec:
              containers:
              - name: nginx
                image: nginx:1.14.2
                env:
                - name: envvar1
                  value: example1 # from-param: ${application_env1}
                - name: envvar2
                  value: example2 # from-param: ${application_env2}
         

In this manifest, the parameter `envvar1` is set to a default of `example1`, and `envvar2` is set to a default of `example2`.

  2. Configure your [targets](https://docs.cloud.google.com/deploy/docs/terminology#target) to include `deployParameters`.

For each parameter you're including, you identify the following:

     * The key name, which is the same name as the key (variable) you set in the manifest.

     * A value for that key. If you don't provide a value, the default value set in the manifest is used.

The following YAML is the configuration for two targets. Each target includes a `deployParameters` stanza setting a value. Each target also includes a label, to be matched with deploy parameters configured on a pipeline stage.
    
    apiVersion: deploy.cloud.google.com/v1beta1
    kind: Target
    metadata:
      name: prod1
      labels:
        my-app: "post-render-config-1"
    description: development cluster
    deployParameters:
      application_env1: "newValue1"
    ---
    
    apiVersion: deploy.cloud.google.com/v1beta1
    kind: target
    metadata:
      name: prod2
      labels:
        my-app: "post-render-config-2"
    description: development cluster
    deployParameters:
      application_env1: "newValue2"
    




When the release is created, but after the manifests are rendered, Cloud Deploy adds these values to the rendered manifests if they include the associated keys.

### Pass a parameter at release creation

Follow these steps to pass parameters and values to the release:

  1. Configure your Kubernetes manifest or Cloud Run service definition using a parameter in place of the value you want to set at deploy time.

Here's an example:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: nginx-deployment
          labels:
            app: nginx
         spec:
          selector:
            matchLabels:
              app: nginx
          template:
            metadata:
              labels:
                app: nginx
            annotations:
              commit: defaultShaValue # from-param: ${git-sha}
            spec:
              containers:
              - name: nginx
                image: nginx:1.14.2
         

In this example, the commit SHA is set as a variable called `${git-sha}`. A value for this is passed at release creation, using the `--deploy-parameters=` option, as seen in the next step.

Syntax for this variable is `$` plus the variable name in braces. In this example, it's `${git-sha}`.

  2. When you create a release, include the `--deploy-parameters` option on the `gcloud deploy releases create` command.

`--deploy-parameters` takes a comma-separated list of key-value pairs, where the key is the placeholder you added to the manifest.

The command will look similar to this:
         
         gcloud deploy releases create test-release-001 \
         --project=my-example-project \
         --region=us-central1 \
         --delivery-pipeline=my-params-demo-app-1 \
         --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa \
         --deploy-parameters="git-sha=f787cac"
         
         




When the release is created, but after manifest rendering, Cloud Deploy provides the values to the rendered manifests if they include the associated keys.

## Deploy parameters with custom targets

You can use any deploy parameter as an environment variable in [custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets). When doing so, use the [syntax](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs) specified for custom targets.

Deploy parameters intended as inputs for custom targets can start with `customTarget/`, for example `customTarget/vertexAIModel`. If you use this prefix, use the following syntax when you reference a deploy parameter as an environment variable:
    
    
    CLOUD_DEPLOY_customTarget_[VAR_NAME]
    

Where `VAR_NAME` is the name following the slash in the [deploy parameter](https://docs.cloud.google.com/deploy/docs/parameters) name. For example, if you define a deploy parameter named `customTarget/vertexAIModel`, reference it as `CLOUD_DEPLOY_customTarget_vertexAIModel`.

## Deploy parameters with deploy hooks

You can use any deploy parameter as an environment variable in [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks).

## Deploy parameters with deployment verification

You can use any deploy parameter as an environment variable in [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment).

## View all parameters for a release

You can view the parameters that have been set for a given release. They're displayed in a table on the **Release details** page and on the command line (`gcloud deploy releases describe`).

  1. From the main Cloud Deploy page, click the delivery pipeline that includes the release you want to see.

  2. On the **Release details** page, select the **Artifacts** tab.




All deploy parameters that have been set for this release are shown in a table, with the variable name and value in one column, and the affected target or targets in the other column.

![deploy parameters and values shown in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/deploy-params-table1.png)

## What's next

  * Try the [quickstart: Use deploy parameters](https://docs.cloud.google.com/deploy/docs/deploy-app-parameters).

  * Find out more about using [parallel deployments](https://docs.cloud.google.com/deploy/docs/parallel).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
