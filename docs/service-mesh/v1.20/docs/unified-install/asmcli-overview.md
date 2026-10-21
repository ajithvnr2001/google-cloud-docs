---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/asmcli-overview/
title: About the asmcli \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:46.427138+00:00
---

# About the asmcli  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/asmcli-overview/

You are viewing archived v1.20 Service Mesh documentation.

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
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About the asmcli

The `asmcli` is a Google-provided tool that you can use to install or upgrade Cloud Service Mesh. If you let it, `asmcli` will configure your project and cluster as follows:

  * Grant you the required Identity and Access Management (IAM) permissions on your Google Cloud project.
  * Enable the required Google APIs on your Google Cloud project.
  * Set a label on the cluster that identifies the mesh.
  * Create a service account that lets data plane components, such as the sidecar proxy, securely access your project's data and resources.
  * [Register the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to the fleet if it isn't already registered.



Just include the `--enable_all` flag when you run `asmcli` to let it configure your project and cluster. For more information about `asmcli` options and flags, see the [`asmcli` reference](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference).

Next, `asmcli` configures YAML files with your project and cluster information. These configuration files are needed to install the Cloud Service Mesh control plane.

If you are new to Cloud Service Mesh and Istio, skip ahead to Supported platforms. The next section is intended to help existing Cloud Service Mesh upgrade to 1.31.

## Transitioning to `asmcli`

The `asmcli` takes the place of `istioctl install` and `install_asm`. Although you can still use the legacy tools in Cloud Service Mesh 1.11, we are deprecating them and they will no longer be supported in Cloud Service Mesh 1.12 and later. Please update your scripts and tools to use `asmcli`.

With Cloud Service Mesh 1.11 and later, all clusters must be registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets). See [Fleet requirements](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/anthos-service-mesh-prerequisites#fleet_requirements) for details.

### Transitioning from `install_asm`

If you are familiar with `install_asm`, `asmcli` is similar but with the following notable differences:

  * You use `asmcli install` for new installations and upgrades. There isn't a [`--mode` option](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference#options) like with `install_asm`. When you run `asmcli install`, it checks to see if there's an existing control plane on the cluster. If there isn't an existing control plane, `asmcli` installs Cloud Service Mesh. If the cluster has an existing control plane (either a Cloud Service Mesh control plane or an open source Istio control plane):

    * If the revision label on the existing control plane doesn't match the revision label for the new control plane, `asmcli` does a [canary upgrade](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/plan-upgrade#about_canary_upgrades).

    * If the control plane revision labels are the same, `asmcli` does an in-place upgrade.

  * Most of the `asmcli` [options and flags](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference) behave the same as the ones for `install_asm`.




### Transitioning from `istioctl install`

If you are familiar with `istioctl install`, if you normally pass an `IstioOperator` YAML file using the `-f` command-line argument to configure the control plane, you can pass the file to `asmcli` using the `--custom_overlay` option. In the Cloud Service Mesh documentation, we refer to these files as overlay files.

**Note:** By default, `asmcli` doesn't install an ingress gateway with the control plane. For production deployments, we recommend that you install gateways separately. For more information and best practices, see [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.20/docs/gateways#best_practices_for_deploying_gateways). We have provided sample Deployment, Service, ServiceAccount, and Role configuration files in the [`anthos-service-mesh`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/main/samples/gateways) repository for both ingress and egress gateways to get you started. You can deploy them as they are or customize them as needed.

## Supported platforms

Cloud Service Mesh installations on the list of [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.20/docs/supported-platforms) can be configured or upgraded by `asmcli`.

However, not all features are available on the platforms outside of Google Cloud. For details, see [In-cluster control plane supported features](https://docs.cloud.google.com/service-mesh/v1.20/docs/supported-features).

## What's next

  * [Prerequisites](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/anthos-service-mesh-prerequisites)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
