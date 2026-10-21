---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/dashboard-storage/
title: Configure the dashboard storage \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:12:58.700879+00:00
---

# Configure the dashboard storage  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/dashboard-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure the dashboard storage Stay organized with collections  Save and categorize content based on your preferences. 

This document contains instructions to configure the storage size for dashboards using the `ObservabilityPipeline` custom resource. The instructions override the default values for the project namespace.

The Observability pipeline of Google Distributed Cloud (GDC) air-gapped appliance manages the deployment and configuration of Observability stack components. The `ObservabilityPipeline` custom resource lets you reach the API of the Observability pipeline and configure the Observability service for your deployments. This custom resource includes customized settings for dashboards used in system monitoring.

## Before you begin

To get the permissions you need to configure or view the storage size for dashboards, ask your Organization IAM Admin to grant you one of the following roles in the `platform-obs` namespace:

  * **Observability Pipeline PA Creator** : creates `ObservabilityPipeline` custom resources. Request the Observability Pipeline PA Creator (`observabilitypipeline-pa-creator`) cluster role.
  * **Observability Pipeline PA Editor** : edits or modifies `ObservabilityPipeline` custom resources. Request the Observability Pipeline PA Editor (`observabilitypipeline-pa-editor`) cluster role.
  * **Observability Pipeline PA Viewer** : views `ObservabilityPipeline` custom resources. Request the Observability Pipeline PA Viewer (`observabilitypipeline-pa-viewer`) cluster role.



Before configuring the storage size for dashboards, work through the following steps:

  1. Set the path of the kubeconfig file as an environment variable:
         
         export KUBECONFIG=KUBECONFIG_FILE
         

Replace `KUBECONFIG_FILE` with the path of the kubeconfig file of the org admin cluster.

  2. Deploy the `ObservabilityPipeline` custom resource with the name `observability-config` into the project namespace.

  3. View the current configuration of your Observability deployment:
         
         kubectl --kubeconfig=${KUBECONFIG} get observabilitypipeline -n PROJECT_NAMESPACE observability-config -o yaml
         




## Update the storage size for dashboards

Work through the following steps to configure the storage size for dashboards in the project:

  1. Open your `ObservabilityPipeline` custom resource in a command-line editor:
         
         kubectl --kubeconfig=${KUBECONFIG} -n PROJECT_NAMESPACE edit observabilitypipeline/observability-config
         

  2. Update the `storageSize` value nested in the `monitoring` field:
         
         # Configure observability pipeline
         apiVersion: observability.gdc.goog/v1
         kind: ObservabilityPipeline
         metadata:
           namespace: PROJECT_NAMESPACE
           name: observability-config
         spec:
           ...
           monitoring:
             grafana:
               storageSize: 1Gi # Configure the new storage size for dashboards in the project.
             ...
         

  3. Save the change and exit your command-line editor.




## Sample configuration

The following YAML file shows a sample configuration of the `ObservabilityPipeline` custom resource:
    
    
    # Configure observability pipeline
    apiVersion: observability.gdc.goog/v1
    kind: ObservabilityPipeline
    metadata:
      namespace: PROJECT_NAMESPACE
      name: observability-config
    spec:
      ...
      monitoring:
        grafana:
          storageSize: 1Gi
        ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
