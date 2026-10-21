---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/customize-services/
title: Manage runtime plane components \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:08:03.371455+00:00
---

# Manage runtime plane components  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/customize-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage runtime plane components Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

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



This topic explains how to configure and manage the Apigee hybrid [runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid#about-the-runtime-plane). For a list of the runtime plane components that you can configure, see [Runtime service configuration overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/service-config). 

##  About the overrides file 

The first time you install the hybrid runtime into a cluster, you must create a configuration _overrides file_. This file lets you override default configuration values as needed, configure environments, reference TLS certificates and service account keys, assign Kubernetes node pools to specific hybrid components, and so on.

The hybrid [installation steps](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin) walk through the process of creating an overrides file and applying your configuration to a cluster. If you want to change the configuration later, modify the overrides file you created and re-apply it. 

## Making a configuration change

To make a configuration change to a hybrid runtime plane component, edit your overrides file and apply the changes with Helm or [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference) depending on your management tool.

For example, to change the replica count on the [Message processor](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/service-config), follow these steps:

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
         
         runtime:
           nodeSelector:
             key: cloud.google.com/gke-nodepool
             value: apigee-runtime
           **replicaCountMin: 2
           replicaCountMax: 20**
         

  4. Apply the changes with the following commands: 

### Helm

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME.

     1. Perform a dry run first: 
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
            --install \
            --namespace APIGEE_NAMESPACE \
            --set env=ENV_NAME \
            -f OVERRIDES_FILE \
            --dry-run
            

        * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.
        * ENV_NAME is the name of the environment you are upgrading.
        * OVERRIDES_FILE is the path to your overrides file.1.3.6
     2. Upgrade the chart: 
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
            --install \
            --namespace APIGEE_NAMESPACE \
            --set env=ENV_NAME \
            -f OVERRIDES_FILE
            

### `apigeectl`

Use [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference) to apply the change to the cluster:
    
    apigeectl apply -f OVERRIDES.yaml --org --env apigee-env

  5. Verify it is up and running by checking the state of the respective env: 
         
         kubectl -n APIGEE_NAMESPACE get apigeeenv
         
         
         NAME                          STATE       AGE   GATEWAYTYPE
         apigee-org1-dev-xxx            running     2d




##  Which configuration properties can you modify? 

You can find the complete list of configurable properties in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref). The reference only lists the properties you can modify; if you try to modify a property that's not in the reference, the change is ignored.

##  How to use the configuration reference 

The [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref) uses dot notation to describe configuration elements, where the first item is the top-level element name followed by properties and child properties. For example:
    
    
    ao.image.pullPolicy

In the overrides file, the properties are formatted in proper YAML. For the above example, the top-level `ao` element is left-indented and sub-element properties are indented under it. Also, YAML requires a colon at the end of each element and sub-element.

For example, to set the `ao.image.pullPolicy` property to `Always`, locate this YAML stanza in the overrides file and set it as follows:
    
    
    ao:
      image:
        pullPolicy: Always

For another example, the property `cassandra.auth.admin.password` (as it is listed in **Configuration property reference**) is used to set the Cassandra admin password. To change it, locate the following YAML in the overrides file and set it as follows:
    
    
    cassandra:
      auth:
        admin:
          password: abc123

Remember, the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref) describes all of the properties that you can set on hybrid runtime plane components. Follow the pattern explained above to modify these elements in your overrides file before applying the changes to your cluster. 

##  Using pre-defined example overrides files 

When you first install hybrid runtime, Apigee recommends that you use one of the pre-configured example overrides files. These examples provide a complete set of configuration properties for specific installation scenarios, such as for setting up a production or test installation. All you need to do is provide appropriate values for the properties and [apply the overrides file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference#commands) to your cluster. See [Step 6: Configure the cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster) for more information. 

Remember that when getting started, it's a good idea to use one of the overrides file examples. The examples provide all of the configuration settings you need to set up a working cluster, including comments that explain which values you need to provide. After things are working, you can always go back later and make configuration changes as needed.

##  About configuration defaults 

Apigee maintains its default component configuration in the file `HYBRID_ROOT_DIR/config/values.yaml`. Your overrides files follows the same YAML structure as `values.yaml`.

An overrides file typically includes only a subset of the configuration properties found in `values.yaml`. Remember, not all properties are editable. When you apply a configuration to a cluster, your overrides are merged with the defaults to create the complete Kubernetes cluster configuration. See also Test the merged configuration.

The following code shows the default configuration for the `mart` component as found in `values.yaml`. Note that some values have defaults, while others such as `sslCertPath` and `sslKeyPath` do not. You must provide these missing values in your overrides file, as explained in the [installation steps](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster). If you want to change any of the default values, make sure they are editable by checking in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref).
    
    
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
`overrides-medium.yaml` |  This sample is a good starting point for testing and QA environments. Individual components have been granted a higher level of resources to deal with additional traffic. Cassandra uses SSD disks for performance. In this environment, it is recommended that users install stateful and stateless components on separate nodes. See [ Configure dedicated nodes](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/configure-dedicated-nodes).   
`overrides-large.yaml` | This sample is a good starting point for high performance environments such as pre-production and production. The sample includes properties for setting encryption keys, passwords, and others. Individual components have a minimum of two replicas.  
  
## Custom annotations

[ Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) are key/value maps used to attach metadata to Apigee hybrid Kubernetes pods. You can create custom annotations for the following properties listed in [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref):

  * [`cassandra`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#cassandra)
  * [`connectAgent`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#connectagent)
  * [`logger`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#logger)
  * [`mart`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#mart)
  * [`metrics`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#metrics)
  * [`runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#runtime)
  * [`synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#synchronizer)
  * [`udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#udca)
  * [`watcher`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#watcher)



To add a custom annotation, add a stanza to the OVERRIDES`.yaml` file for the respective component.

The following example illustrates how an annotation can be specified in `runtime` pods:
    
    
    runtime:
      annotations:
        businessunit: "bu1"

## Test the merged configuration

You can use the `--dry-run` flag to test the merged configuration file without actually applying it to your cluster. This option is useful for debugging an installation problem because it shows you exactly what will be applied to the cluster. It is also a good practice to test the configuration and store it in source control so that you have a reference of the resources installed and configured in the cluster.

### Helm
    
    
    kubectl apply -k  apigee-operator/etc/crds/default/
          
    
    
    helm upgrade operator apigee-operator/ \
      --install \
      --namespace apigee-system \
      --atomic \
      -f OVERRIDES_FILE.yaml \
      --dry-run
    
    
    helm upgrade ingress-manager apigee-ingress-manager/ /
      --install \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml \
      --dry-run

### `apigeectl`
    
    
    APIGEECTL_HOME/apigeectl init -f overrides/OVERRIDES.yaml --dry-run=client
    

**Caution:** Be aware that the configuration output contains password and secret information.

For more information, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

##  Create multiple overrides files as needed 

You can create as many overrides files as you want, where each one serves a specific requirement. For example, you might have an overrides file that tunes your cluster for production, and another for creating a testing cluster. You can then maintain these files in your source control system. 

For example:

### Helm
    
    
    helm upgrade test-1-env apigee-env/ \
      --namespace apigee \
      --atomic \
      --set env=test-1-env \
      -f test-1-env-overrides.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "test-1-env" has no deployed releases`, replace `upgrade` with `install` and try the command again.

### `apigeectl`
    
    
    $APIGEECTL_HOME/apigeectl apply -f test-1-env-overrides.yaml --env test-1-env

## Delete hybrid-specific runtime plane components

The runtime plane components include `synchronizer`, `mart`, `runtime`, `cassandra`, and `udca`. 

To delete the hybrid-specific runtime plane components from your cluster, use the `helm delete` or `apigeectl delete` commands. Be sure to specify the same overrides file that you used to install the runtime components. 

For example:

### Helm

Using Helm, you must delete each component individually. For example, to delete the `cassandra` component, use the following command: 
    
    
    helm -n apigee delete datastore
    

In the example above the datastore component was installed with the name "datastore". If you you installed it with a different name, then you would supply that name to delete the component. For example if you installed the `apigee-datastore` chart with `helm install my-cassandra-storage apigee-datastore/`. you would delete it with the following command: 
    
    
    helm delete -n apigee my-cassandra-storage
    

### `apigeectl`

With `apigeectl` you can delete all runtime components at once or limit the scope to delete one component at a time. For example, to delete all components at once: 
    
    
    $APIGEECTL_HOME/apigeectl delete -f OVERRIDES_FILE.yaml

To delete the `cassandra` component:
    
    
    $APIGEECTL_HOME/apigeectl delete -f OVERRIDES_FILE.yaml --datastore

To recreate recreate a specific component or components (the environment group in this example): 

### Helm
    
    
    helm upgrade ENV_GROUP apigee-virtualhost/ \
      --install \
      --namespace apigee \
      --atomic \
      --set envgroup=ENV_GROUP_NAME \
      -f OVERRIDES_FILE.yaml
    

### `apigeectl`
    
    
    $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE.yaml --env ENV_NAME --settings virtualhosts

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
