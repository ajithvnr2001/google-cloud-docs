---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/customize-services/
title: Manage runtime plane components \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:20:38.301200+00:00
---

# Manage runtime plane components  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/customize-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage runtime plane components Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/customize-services.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/customize-services.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/customize-services.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/customize-services.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/customize-services.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/customize-services.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/customize-services.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/customize-services.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/customize-services.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/customize-services.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/customize-services.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/customize-services.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/customize-services.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/customize-services.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/customize-services.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/customize-services.html)



This topic explains how to configure and manage the Apigee hybrid [runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid#about-the-runtime-plane). For a list of the runtime plane components that you can configure, see [Runtime service configuration overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/service-config). 

##  About the overrides file 

The first time you install the hybrid runtime into a cluster, you must create a configuration _overrides file_. This file lets you override default configuration values as needed, configure environments, reference TLS certificates and service account keys, assign Kubernetes node pools to specific hybrid components, and so on.

The hybrid [installation steps](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-before-begin) walk through the process of creating an overrides file and applying your configuration to a cluster. If you want to change the configuration later, modify the overrides file you created and re-apply it. 

## Making a configuration change

To make a configuration change to a hybrid runtime plane component, edit your overrides file and apply the changes with [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

For example, to change the replica count on the [Message processor](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/service-config), follow these steps:

  1. Open your OVERRIDES`.yaml` file. Be sure to use the same overrides file that was used to install the hybrid runtime into the cluster.
  2. Locate the `runtime` element in the file. For example: 
         
         ...
         runtime:
           nodeSelector:
             key: cloud.google.com/gke-nodepool
             value: apigee-runtime
           replicaCountMin: 1
           replicaCountMax: 2
         ...

  3. Change the replica count properties as needed. For example: 
         
         ...
         runtime:
           nodeSelector:
             key: cloud.google.com/gke-nodepool
             value: apigee-runtime
           **replicaCountMin: 2
           replicaCountMax: 4**
         ...

  4. Use [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference) to apply the change to the cluster: 
         
         apigeectl apply -f ./OVERRIDES.yaml --org --env ENV_NAME




##  Which configuration properties can you modify? 

You can find the complete list of configurable properties in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref). The reference only lists the properties you can modify; if you try to modify a property that's not in the reference, the change is ignored.

##  How to use the configuration reference 

The [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref) uses dot notation to describe configuration elements, where the first item is the top-level element name followed by properties and child properties. For example:
    
    
    authz.image.pullPolicy

In the overrides file, the properties are formatted in proper YAML. For the above example, the top-level `authz` element is left-indented and sub-element properties are indented under it. Also, YAML requires a colon at the end of each element and sub-element.

For example, to set the `authz.image.pullPolicy` property to `Always`, locate this YAML stanza in the overrides file and set it as follows:
    
    
    authz:
      image:
        pullPolicy: Always

For another example, the property `cassandra.auth.admin.password` (as it is listed in **Configuration property reference**) is used to set the Cassandra admin password. To change it, locate the following YAML in the overrides file and set it as follows:
    
    
    cassandra:
      auth:
        admin:
          password: abc123

Remember, the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref) describes all of the properties that you can set on hybrid runtime plane components. Follow the pattern explained above to modify these elements in your overrides file before applying the changes to your cluster. 

##  Using pre-defined example overrides files 

When you first install hybrid runtime, Apigee recommends that you use one of the pre-configured example overrides files. These examples provide a complete set of configuration properties for specific installation scenarios, such as for setting up a production or test installation. All you need to do is provide appropriate values for the properties and [apply the overrides file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cli-reference#commands) to your cluster. See [Step 6: Configure the cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster) for more information. 

Remember that when getting started, it's a good idea to use one of the overrides file examples. The examples provide all of the configuration settings you need to set up a working cluster, including comments that explain which values you need to provide. After things are working, you can always go back later and make configuration changes as needed.

##  About configuration defaults 

Apigee maintains its default component configuration in the file `HYBRID_ROOT_DIR/config/values.yaml`. Your overrides files follows the same YAML structure as `values.yaml`.

An overrides file typically includes only a subset of the configuration properties found in `values.yaml`. Remember, not all properties are editable. When you apply a configuration to a cluster, your overrides are merged with the defaults to create the complete Kubernetes cluster configuration. See also Test the merged configuration.

The following code shows the default configuration for the `mart` component as found in `values.yaml`. Note that some values have defaults, while others such as `sslCertPath` and `sslKeyPath` do not. You must provide these missing values in your overrides file, as explained in the [installation steps](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster). If you want to change any of the default values, make sure they are editable by checking in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref).
    
    
    ...
    mart:
      replicaCountMin: 2
      replicaCountMax: 4
      targetCPUUtilizationPercentage: 75
      terminationGracePeriodSeconds: 30
      sslCertPath:
      sslKeyPath:
      hostAlias:
      nodeSelector:
        key:
        value:
      revision: blue
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-mart-server"
        tag: "1.3.6"
        pullPolicy: IfNotPresent
      resources:
        requests:
          cpu: 500m
          memory: 512Mi
      initCheckCF:
        resources:
          requests:
            cpu: 10m
      livenessProbe:
        timeoutSeconds: 1
        failureThreshold: 12
        periodSeconds: 5
        initialDelaySeconds: 15
      readinessProbe:
        timeoutSeconds: 1
        successThreshold: 1
        failureThreshold: 2
        periodSeconds: 5
        initialDelaySeconds: 15
      metricsURL: "/v1/server/metrics"
      cwcAppend: |
    ...

If you want to modify a component's defaults and the component is not already in your overrides file, you can copy its YAML from `values.yaml` into your overrides file and modify it there.

Never edit `values.yaml` directly; always use an overrides file to specify your configuration properties.

## Sample overrides files

Apigee provides a set of sample overrides files to help guide you in setting up your hybrid deployment. It's a good practice to copy and modify the overrides file that most closely matches your installation requirements.

The following samples are included in the directory `HYBRID_ROOT_DIR/examples`:

Sample overrides files | Description  
---|---  
`overrides-small.yaml` | This sample is ideal for a getting started quickly. It uses the minimum recommended footprint to start the hybrid runtime components. This sample configuration relies as much as possible on default settings and values. All the minimum replicas are set to `1`.  
`overrides-medium.yaml` |  This sample is a good starting point for testing and QA environments. Individual components have been granted a higher level of resources to deal with additional traffic. Cassandra uses SSD disks for performance. In this environment, it is recommended that users install stateful and stateless components on separate nodes. See [ Configure dedicated nodes](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes).   
`overrides-large.yaml` | This sample is a good starting point for high performance environments such as pre-production and production. The sample includes properties for setting encryption keys, passwords, and others. Individual components have a minimum of two replicas.  
  
## Custom annotations

[ Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) are key/value maps used to attach metadata to Apigee hybrid Kubernetes pods. You can create custom annotations for the following properties listed in [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref):

  * [`cassandra`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#cassandra)
  * [`connectAgent`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#connectagent)
  * [`logger`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#logger)
  * [`mart`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#mart)
  * [`metrics`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#metrics)
  * [`runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#runtime)
  * [`synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#synchronizer)
  * [`udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#udca)
  * [`watcher`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#watcher)



To add a custom annotation, add a stanza to the OVERRIDES`.yaml` file for the respective component.

The following example illustrates how an annotation can be specified in `runtime` pods:
    
    
    runtime:
      annotations:
        businessunit: "bu1"

## Test the merged configuration

You can use the `--dry-run` flag with `apigeectl` to test the merged configuration file without actually applying it to your cluster. This option is useful for debugging an installation problem because it shows you exactly what will be applied to the cluster. It is also a good practice to test the configuration and store it in source control so that you have a reference of the resources installed and configured in the cluster.

In Apigee hybrid, the syntax of the `--dry-run` flag depends on the version of `kubectl` you are running. Check the version of `kubectl` with the following command:
    
    
    kubectl version
    

**kubectl version 1.17 and older:**
    
    
    APIGEECTL_HOME/apigeectl init -f overrides/OVERRIDES.yaml --dry-run=true
    

**kubectl version 1.18 and newer:**
    
    
    APIGEECTL_HOME/apigeectl init -f overrides/OVERRIDES.yaml --dry-run=client
    

**Caution:** Be aware that the configuration output contains password and secret information.

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

##  Create multiple overrides files as needed 

You can create as many overrides files as you want, where each one serves a specific requirement. For example, you might have an overrides file that tunes your cluster for production, and another for creating a testing cluster. You can then maintain these files in your source control system. 
    
    
    apigeectl apply  -f ./test_env_override.yaml

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

## Delete hybrid-specific runtime plane components

To delete the hybrid-specific runtime plane components from your cluster, use the `apigeectl delete` command. These components include `synchronizer`, `mart`, `runtime`, `cassandra`, and `udca`. Be sure to specify the same overrides file that you used to install the runtime components: 

For example: 
    
    
    apigeectl delete -f ./OVERRIDES.yaml

You can use the `apigeectl apply` command to recreate a specific component or components: 
    
    
    apigeectl apply --org --env ENV_NAME -f ./OVERRIDES.yaml

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

## Delete a specific component

If you only want to delete a specific component, use the `-c` option with `apigeectl delete` Be sure to specify the same overrides file you used to install the runtime components. 

For example, to delete the `synchronizer` component, use this command:
    
    
    apigeectl delete --org --env ENV_NAME -f ./OVERRIDES.yaml

You can then use the `apigeectl apply` command to recreate the component: 
    
    
    apigeectl apply --org --env ENV_NAME -f ./OVERRIDES.yaml

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

## Delete all components

To delete all of your cluster components hybrid, including those created by the `apigeectl init` command, use the `apigeectl delete` command with the `--all` flag. Be sure to specify the same overrides file that you used to install the runtime components: 

For example: 
    
    
    apigeectl delete -f ./OVERRIDES.yaml --all

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
