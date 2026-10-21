---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/deploy-demo-telemetry-addons/
title: Deploying a demo version of the telemetry add-ons \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:49.469322+00:00
---

# Deploying a demo version of the telemetry add-ons  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/deploy-demo-telemetry-addons/

You are viewing archived v1.26 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploying a demo version of the telemetry add-ons

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

The YAML files to deploy a demo version of Prometheus, Grafana, and Kiali are available in the Istio GitHub repository. Although these YAML files make it easy for you to deploy an instance of Prometheus, Grafana and Kiali to your cluster, these files aren't meant to take the place of installing and configuring the applications yourself.

**Important:** For production environments, we recommend that you follow the applicable [third-party documentation](https://docs.cloud.google.com/service-mesh/v1.26/docs/unified-install/options/third-party-integrations#third-party_documentation) to ensure that you stay up to date with the latest versions and best practices for these applications.

To deploy a demo version of the add-ons to your cluster:

  1. [Enable metrics export to Prometheus](https://docs.cloud.google.com/service-mesh/v1.26/docs/unified-install/options/third-party-integrations#enabling_metrics_export_to_prometheus).

  2. Clone the repo:
         
         git clone -b release-1.10 https://github.com/istio/istio --depth 1
         

  3. Deploy an instance of the add-ons:

     * To deploy Grafana:
           
           kubectl apply -f istio/samples/addons/grafana.yaml
           

     * To deploy Kiali:
           
           kubectl apply -f istio/samples/addons/kiali.yaml
           

     * To deploy Prometheus:
           
           kubectl apply -f istio/samples/addons/prometheus.yaml
           




If you need to delete the add-ons, you can do so with the `kubectl delete -f` command.

Istio provides a set of [preconfigured dashboards](https://istio.io/v1.26/docs/ops/integrations/grafana/) for Grafana. These dashboards are included in the demo version. You can also [import the dashboards](https://istio.io/v1.26/docs/ops/integrations/grafana/#option-2-import-from-grafana-com-into-an-existing-deployment) into an existing Grafana deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
