---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/configure-notification-channels/
title: Configure notification channels for alerts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:46.206191+00:00
---

# Configure notification channels for alerts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/configure-notification-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure notification channels for alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the process for configuring notification channels to receive alerts.

Notification channels are the delivery mechanisms for your configured alerts. The system notifies designated recipients through these channels when an event triggers an alert. This process ensures that critical alerts reach the appropriate personnel through their preferred communication methods.

In Google Distributed Cloud (GDC) air-gapped environments, predefined notification channels like Slack or email are unavailable. To receive alerts, you must configure at least one custom notification channel. You edit `ObservabilityPipeline` custom resources in your project namespace to apply channel configurations.

By customizing notification channels, administrators can achieve the following:

  * **Target specific recipients** : Direct alerts to individuals, teams, or on-call rotations responsible for addressing issues.
  * **Use preferred communication methods** : Deliver alerts through channels like SMS, PagerDuty, webhooks, or custom integrations, catering to individual preferences and operational workflows.
  * **Prevent alert fatigue** : Reduce noise and ensure that alerts are received by those who need to take action.



Implementing notification channels in GDC requires administrators to define the channel configuration within the system. This process typically involves specifying parameters like:

  * **Channel type** : the type of channel being used.
  * **Destination** : the endpoint where the system should send notifications.
  * **Authentication** : any required credentials for accessing the destination.



By configuring notification channels, administrators can ensure that the monitoring platform effectively delivers critical alerts, enabling prompt responses to potential issues and maintaining the stability and performance of GDC environments.

## Before you begin

To manage `ObservabilityPipeline` custom resources, you must have the necessary permissions.

### Request IAM organization roles

Contact your Organization IAM Admin to request the following roles:

  * **ObservabilityPipeline PA Creator** (`observabilitypipeline-pa-creator`): create `ObservabilityPipeline` custom resources.
  * **ObservabilityPipeline PA Editor** (`observabilitypipeline-pa-editor`): edit or modify `ObservabilityPipeline` custom resources.
  * **ObservabilityPipeline PA Viewer** (`observabilitypipeline-pa-viewer`): view `ObservabilityPipeline` custom resources.
  * **ConfigMap Editor** (`observabilitypipeline-configmap-editor`): create `ConfigMap` objects in the platform namespace.



### Request IAM project roles

Contact your Project IAM Admin to request the following roles:

  * **ObservabilityPipeline Editor** (`observabilitypipeline-editor`): edit or modify `ObservabilityPipeline` custom resources in the project namespace.
  * **ObservabilityPipeline Viewer** (`observabilitypipeline-viewer`): view `ObservabilityPipeline` custom resources in the project namespace.



## Configure notification channels

**Important:** Before configuring notification channels, ensure you have created alert rules in your project namespace. For more information, see [Create alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-alert-rules).

Configure notification channels for alerts in your project namespace:

  1. Define your custom configuration for notification channels in a YAML file named `alertmanager.yml`. You must follow the same syntax as the Alertmanager specification:

<https://prometheus.io/docs/alerting/latest/configuration/>.

  2. Create a `ConfigMap` object and include your custom configuration from the `alertmanager.yml` file in the `data` field.

The following example shows how the `ConfigMap` object must look with the `alertmanager.yml` file:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: CONFIGMAP_NAME
           # The namespace must match your project namespace.
           namespace: PROJECT_NAMESPACE
         data:
           # The file name must be alertmanager.yml
           alertmanager.yml: |
             # Define your notification channels.
             # Add the custom configuration in the following lines of this file.
             # Follow the same syntax as in https://prometheus.io/docs/alerting/latest/configuration
         
           [...]
         

Replace the following:

     * `CONFIGMAP_NAME`: the name of the `ConfigMap` definition file. You use this name later in the `ObservabilityPipeline` custom resource.
     * `PROJECT_NAMESPACE`: your project namespace.
  3. Apply the `ConfigMap` object to the Management API server within the same namespace as your configured alerts:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f CONFIGMAP_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `CONFIGMAP_NAME`: the name of the `ConfigMap` definition file.
  4. Edit the `ObservabilityPipeline` custom resource specification to import your configuration to the `alertmanagerConfig` field:
         
         # Configure the observability pipeline.
         apiVersion: observability.gdc.goog/v1
         kind: ObservabilityPipeline
         metadata:
           # The namespace must match your project namespace.
           namespace: PROJECT_NAMESPACE
           name: OBSERVABILITY_PIPELINE_NAME
         spec:
           # Configure alerts.
           alerting:
             # The alerting configuration must be in the ConfigMap.
             # The value must match the ConfigMap name exactly.
             alertmanagerConfig: CONFIGMAP_NAME
         
           [...]
         

Replace the following:

     * `PROJECT_NAMESPACE`: your project namespace.
     * `OBSERVABILITY_PIPELINE_NAME`: the name of the `ObservabilityPipeline` custom resource.
     * `CONFIGMAP_NAME`: the name you used for the `ConfigMap` definition file. The name must match exactly.
**Note:** In the `alerting` field of the `ObservabilityPipeline` custom resource, you can also define other configurations for the project namespace such as volumes (`volumes`) and volume mounts (`volumeMounts`). You reference volume mount names in the `alertmanager.yml` file.
  5. Save the file.

  6. Apply the changes of the `ObservabilityPipeline` custom resource to the Management API server within the same namespace as your configured alerts:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f OBSERVABILITY_PIPELINE_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `OBSERVABILITY_PIPELINE_NAME`: the name of the `ObservabilityPipeline` definition file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
