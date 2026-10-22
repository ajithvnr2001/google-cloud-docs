---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-lifecycle/
title: Life cycle of a marketplace deployment \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:19.797478+00:00
---

# Life cycle of a marketplace deployment  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Life cycle of a marketplace deployment Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to install, upgrade, and uninstall Google Distributed Cloud (GDC) air-gapped Marketplace software packages using the GDC console. You can also install software packages using the [`gdcloud marketplace` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-marketplace) or the [Marketplace API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/marketplace-api-overview).

This document is for audiences within the application operator group who manage the lifecycle of Marketplace deployments within GDC projects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you can install, upgrade, or uninstall Marketplace software packages, you must have the necessary permissions and prepare your environment.

### Request IAM roles

Contact your IAM Org Admin or IAM Project Admin to request the following roles based on the tasks you need to perform within your project:

  * **Marketplace Editor** (`marketplace-editor`): install, upgrade, and uninstall Marketplace software packages.
  * **Project Viewer** (`project-viewer`): view an existing project and its resources.



The IAM Org Admin can grant these roles for any project within the organization. The IAM Project Admin can grant these roles within the scope of their specific project.

### Prepare your environment

The tasks on this page primarily use the GDC console. If you plan to use the command-line alternatives, complete the following:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.
  * To use the API with `kubectl`, additional setup is required: 
    * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
    * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig).



## Install a Distributed Cloud marketplace software package

To install a software package from the Distributed Cloud marketplace, complete the following steps:

###  Console 

  1. In the project selector of the GDC console, select the project you want to install the software package in.
  2. In the Distributed Cloud marketplace, visit the listing page for the product that you want to install. From this page, you can review details of the product and follow links to its documentation, pricing, and terms of services.
  3. If it's the first time you are installing this product, click **Install**. Otherwise, go to the Management tab and click **New Instance**.
  4. In the dialog, select which user cluster you want to install the software package in. If you want to customize its configuration, click **Next**. If you want to use the default configuration, click **Install**.
  5. If you clicked **Next** , you can now examine the default configuration. Click **Custom configuration** to enter your own parameters, following the vendor's documentation. When finished, click **Install** to proceed with the installation. For Kubernetes software packages, the parameters that you configure here override the default values provided by the vendor in their [Helm values file](https://helm.sh/docs/chart_template_guide/values_files/).
  6. Wait a few minutes for your new instance to be marked as _Ready_ in the **Management** tab of the page.

![Marketplace UI Dataproc Container for Spark service installed](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/marketplace-dataproc-installed.png)

  7. Consult the documentation of the relevant software vendor to learn how to use their solution once it's installed.




###  gdcloud 

  1. Select the project you want to install the software package in:
         
         gdcloud config set project PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project you want to install the software package in.

  2. List the available Marketplace applications:
         
         gdcloud marketplace services list
         

  3. Install the selected application from the list, specifying the target cluster:
         
         gdcloud marketplace services install SERVICE_NAME \
           --cluster=CLUSTER_NAME
         

To provide custom configuration overrides during installation, use the `--parameters-file` flag:
         
         gdcloud marketplace services install SERVICE_NAME \
           --cluster=CLUSTER_NAME \
           --parameters-file=PATH_TO_PARAMETERS_FILE
         

Replace the following:

     * `SERVICE_NAME`: the name of the Marketplace service to install (for example, `dataproc`)
     * `CLUSTER_NAME`: the name of the target user cluster where you want to install the application
     * `PATH_TO_PARAMETERS_FILE`: the path to a YAML file containing configuration override parameters for the service instance
  4. Verify the installation:
         
         gdcloud marketplace services list
         

Confirm that the newly installed application appears in the list with a `READY` or `INSTALLED` status.




###  API 

  1. List available `ServiceVersion` resources to find the specific service and version you want to install:
         
         kubectl get serviceversions -n mkt-system
         

  2. Create a YAML manifest for a `ServiceInstance` resource (for example, `service-instance.yaml`):
         
         apiVersion: marketplace.gdc.goog/v1
         kind: ServiceInstance
         metadata:
           name: INSTANCE_NAME
         spec:
           clusterRef:
             name: CLUSTER_NAME
             namespace: CLUSTER_NAMESPACE
           serviceVersionRef:
             name: SERVICE_VERSION_NAME
             namespace: mkt-system
           parameters:
             KEY: VALUE
         

Replace the following:

     * `INSTANCE_NAME`: a name for your new application instance
     * `CLUSTER_NAME`: the name of the target user cluster where you want to install the application
     * `CLUSTER_NAMESPACE`: the namespace of the cluster (for example, `production-cluster`)
     * `SERVICE_VERSION_NAME`: the name of the `ServiceVersion` to install (for example, `dataproc-1.0.0`)
     * `KEY`: the configuration override parameter name, following the vendor's Helm values schema
     * `VALUE`: the value for the configuration override parameter

For more information and an example manifest, see [Marketplace API overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/marketplace-api-overview).

  3. Apply the manifest to the project:
         
         kubectl apply -f service-instance.yaml -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project you want to install the software package in.

  4. Verify the installation by inspecting the status of the `ServiceInstance` object:
         
         kubectl get serviceinstance INSTANCE_NAME -n PROJECT_NAME -o yaml
         

Confirm that `status.conditions` contains a condition of type `Ready` with status `"True"`, and that `status.installedVersion` displays the installed version.




**Note:** If you need to know which container image is available in GDC, consult the list of [Marketplace images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/mkt-images) that are included in your version of GDC. Images that were included in previous versions of GDC remain available for use, even after an upgrade of GDC.

## Reconfigure an instance of a Distributed Cloud marketplace software package

**Warning:** While you can reconfigure a running instance of a Distributed Cloud marketplace software package, the reconfiguration process is implemented by the vendor who published the product. The reconfiguration process therefore varies from one software package to another. We recommend you carefully review the documentation of the relevant vendor before proceeding with a reconfiguration. Depending on how the vendor implemented their reconfiguration process, you may encounter downtime in the service delivered.

Some Distributed Cloud marketplace software packages can be reconfigured when they are already running. For Kubernetes-based services, this is equivalent to applying new [values](https://helm.sh/docs/chart_template_guide/values_files/) to the vendor's Helm chart.

To reconfigure a running instance of a Distributed Cloud marketplace software package, work through the following steps:

  1. In the project selector of the GDC console, select the project in which you want to upgrade the software package.
  2. On the Distributed Cloud marketplace page, visit the listing page for the product you want to upgrade.
  3. Click the **Management** tab.
  4. Click **Configuration file** for the instance you want to reconfigure.
  5. In the panel that opens, enter your custom parameters, following the vendor's documentation.
  6. Click **Save** to apply the new parameters. The reconfiguration completes in a few minutes.



## Upgrade a Distributed Cloud marketplace software package

**Warning:** While you can trigger the upgrade of a software package using the Distributed Cloud marketplace, the upgrade process is implemented by the vendor who published the product. The upgrade process therefore varies from one software package to another. We recommend you carefully review the release notes and upgrade documentation of the relevant vendor before proceeding with an upgrade. Depending on how the vendor implemented their upgrade process, you may encounter downtime in the service delivered, or compatibility issues between older and newer versions.

Some Distributed Cloud marketplace software packages can be upgraded to a new version through the Google Distributed Cloud marketplace after your Infrastructure Operator makes those new versions available to you.

To upgrade a Distributed Cloud marketplace software package, work through the following steps:

  1. In the project selector of the GDC console, select the project in which you want to upgrade the software package.
  2. On the Distributed Cloud marketplace page, visit the listing page for the product you want to upgrade.
  3. Click the Management tab.
  4. Click **Upgrade** on the instance you want to upgrade. The upgrade completes in a few minutes.

**Note:** Upgrading a software package through the Distributed Cloud console leads to the next available version of the software being installed. If there are multiple new versions of the software available, you need to repeat the process for each of them. If required, use the [Marketplace API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/v1/marketplace-v1) to upgrade to a specific version.

## Uninstall a Distributed Cloudmarketplace software package

**Warning:** Uninstalling a Distributed Cloud marketplace software package is a destructive action, and may result in loss of data or downtime of systems dependent on this software. Ensure that you have backed up all important data and that no important system depends on the software you want to uninstall before proceeding. Consult the documentation of the relevant vendor to learn how to back up any data managed by their software.

To uninstall a Distributed Cloud marketplace software package, complete the following steps:

  1. In the project selector of the GDC console, select the project you want to uninstall the software package from.
  2. On the Distributed Cloud marketplace page, visit the listing page for the product you want to uninstall.
  3. Click the **Management** tab.
  4. Click **Uninstall** for the instance you want to uninstall. The software package is uninstalled in a few minutes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
