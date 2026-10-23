---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/third-party-integrations/
title: Integrating with third-party add-ons \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:16.944997+00:00
---

# Integrating with third-party add-ons  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/third-party-integrations/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrating with third-party add-ons

Cloud Service Mesh profiles do not include [Prometheus](https://prometheus.io/), [Kiali](https://kiali.io/), and [Grafana](https://grafana.com/docs/grafana/latest/) add-ons.

Note, however, you can install your own instance of Prometheus, Kiali, and Grafana dashboards according to the applicable third-party documentation.

## Enabling metrics export to Prometheus

To use the Prometheus, Grafana, or Kiali dashboards, Cloud Service Mesh must be configured to export metrics to Prometheus.

Metrics export to Prometheus is enabled by default when you install Cloud Service Mesh on Google Distributed Cloud or on bare metal. On these platforms, you are all set to install your own instance of the dashboards.

You can enable metrics export to Prometheus instead of Stackdriver (now called Google Cloud Observability) on GKE on Google Cloud clusters.

## Before you begin

Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools) to: 

  * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#install_required_tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#validate_project_and_cluster)



## Enable metrics export to Prometheus

  1. Follow the steps in the [install](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh) and [upgrade](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/upgrade) Cloud Service Mesh guide to install or upgrade Cloud Service Mesh on GKE. When you run `asmcli install`, include the following option:
         
         --option prometheus
         

For example:
         
         ./asmcli install \
           --project_id PROJECT_ID \
           --cluster_name CLUSTER_NAME \
           --cluster_location CLUSTER_LOCATION \
           --output_dir DIR_PATH  \
           --enable_all \
           --ca mesh_ca \
           --option prometheus
         

**Caution:** Using `--option prometheus` will disable metrics export to Stackdriver. You must export metrics to Stackdriver if you wish to use the Cloud Service Mesh dashboard functionality. You can enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`.**Warning:** With installation on GKE Enterprise On-premises clusters configured with `enableStackdriverForApplications=true`, enabling Prometheus may incur extra Cloud Monitoring charges. For more information and disabling `enableStackdriverForApplications`, see [GKE Enterprise clusters on-prem known issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/known-issues#unexpected-monitoring-billing). To disable Prometheus annotations during Cloud Service Mesh installation, see [disable Prometheus metrics merging feature](https://istio.io/latest/docs/ops/integrations/prometheus/#option-1-metrics-merging). Note: By default, `asmcli` doesn't install an ingress gateway, which you can use to manage inbound traffic to applications running on your service mesh. Follow the steps in [ Install gateways](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh#install_gateways) to install an ingress gateway. 

Be sure to specify any other [overlay files](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/enable-optional-features#about_the_overlay_files) that you need to configure Cloud Service Mesh.

  2. Complete the Cloud Service Mesh installation to enable automatic sidecar proxy injection on your workloads. For new installations, see [Deploy and redeploy workloads](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh#deploy_and_redeploy_workloads). For upgrades, see [Switch to the new control plane](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/upgrade#switch_to_the_new_control_plane)




## Third-party documentation

You can [deploy Prometheus and Grafana through the Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/prometheus) or refer to the following documentation for installation.

  * Grafana:

    * [Getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/)

    * [Import the dashboards](https://istio.io/v1.19/docs/ops/integrations/grafana/#option-2-import-from-grafana-com-into-an-existing-deployment) into an existing Grafana deployment.

  * Kiali:

    * [Quick Start guide](https://kiali.io/docs/installation/quick-start/)

    * [Installation Guide](https://kiali.io/docs/installation/installation-guide/)

  * Prometheus:

    * [Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)



## What's next

  * [Deploying a demo version of the telemetry add-ons](https://docs.cloud.google.com/service-mesh/v1.19/docs/deploy-demo-telemetry-addons)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
