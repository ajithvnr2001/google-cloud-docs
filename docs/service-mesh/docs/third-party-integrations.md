---
url: https://docs.cloud.google.com/service-mesh/docs/third-party-integrations/
title: Integrating with third-party add-ons \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:08.042864+00:00
---

# Integrating with third-party add-ons  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/third-party-integrations/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrating with third-party add-ons

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh profiles don't include [Prometheus](https://prometheus.io/), [Kiali](https://kiali.io/), and [Grafana](https://grafana.com/docs/grafana/latest/) add-ons.

Note, however, you can install your own instance of Prometheus, Kiali, and Grafana dashboards according to the applicable third-party documentation.

This document applies to the in-cluster control plane only.

## Enabling metrics export to Prometheus

To use the Prometheus, Grafana, or Kiali dashboards, Cloud Service Mesh must be configured to export metrics to Prometheus.

Metrics export to Prometheus is enabled by default when you install Cloud Service Mesh on Google Distributed Cloud (software only) for VMware or on bare metal. On these platforms, you are all set to install your own instance of the dashboards.

You can enable metrics export to Prometheus instead of Stackdriver (now called Google Cloud Observability) on GKE on Google Cloud clusters.

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

## Before you begin

Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools) to: 

  * [Install required tools](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster)



## Enable metrics export to Prometheus

  1. Follow the steps in the [install](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/plan-install) and [upgrade](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) Cloud Service Mesh guide to install or upgrade Cloud Service Mesh on GKE. When you run `asmcli install`, include the following option:
         
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
         

**Caution:** Using `--option prometheus` will disable metrics export to Stackdriver. You must export metrics to Stackdriver if you want or need to use the Cloud Service Mesh dashboard features. You can enable both Stackdriver and Prometheus by using `--option prometheus-and-stackdriver`.**Warning:** With installation on GKE Enterprise On-premises clusters configured with `enableStackdriverForApplications=true`, enabling Prometheus may incur extra Cloud Monitoring charges. For more information and disabling `enableStackdriverForApplications`, see [GKE Enterprise clusters on-prem known issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/known-issues#unexpected-monitoring-billing). To disable Prometheus annotations during Cloud Service Mesh installation, see [disable Prometheus metrics merging feature](https://istio.io/latest/docs/ops/integrations/prometheus/#option-1-metrics-merging). Note: By default, `asmcli` doesn't install an ingress gateway, which you can use to manage inbound traffic to applications running on your service mesh. Follow the steps in [ Install gateways](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#install_gateways) to install an ingress gateway. 

Be sure to specify any other [overlay files](https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-in-cluster#about_the_overlay_files) that you need to configure Cloud Service Mesh.

  2. Complete the Cloud Service Mesh installation to enable automatic sidecar proxy injection on your workloads. For new installations, see [Deploy and redeploy workloads](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#deploy_and_redeploy_workloads). For upgrades, see [Switch to the new control plane](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade#switch_to_the_new_control_plane)




## Third-party documentation

You can [deploy Prometheus and Grafana through the Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/prometheus) or refer to the following documentation for installation.

  * Grafana:

    * [Getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/)

    * [Import the dashboards](https://istio.io/v1.31/docs/ops/integrations/grafana/#option-2-import-from-grafana-com-into-an-existing-deployment) into an existing Grafana deployment.

  * Kiali:

    * [Quick Start guide](https://kiali.io/docs/installation/quick-start/)

    * [Installation Guide](https://kiali.io/docs/installation/installation-guide/)

  * Prometheus:

    * [Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
