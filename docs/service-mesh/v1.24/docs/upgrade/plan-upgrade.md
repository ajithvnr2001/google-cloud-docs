---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/plan-upgrade/
title: Plan an upgrade \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:51.525226+00:00
---

# Plan an upgrade  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/plan-upgrade/

You are viewing archived v1.24 Service Mesh documentation.

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
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Plan an upgrade 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

This page provides information to help you plan a Cloud Service Mesh upgrade. We recommend that you also review the [Istio upgrade notes](https://istio.io/latest/news/releases/1.24.x/announcing-1.24/upgrade-notes/).

## About canary upgrades

We recommend that you upgrade Cloud Service Mesh by first running a canary deployment of the new control plane. With a canary upgrade, `asmcli` installs a new [revision](https://docs.cloud.google.com/service-mesh/v1.24/docs/revisions-overview#what_is_a_revision) of the control plane alongside the old control plane. Both the old and new control planes are labeled with a `revision` label, which serves as an identifier for the control planes.

To migrate workloads to the new control plane:

  1. Set the new control plane's `revision` label on one of your namespaces.

  2. Perform a rolling restart. The restart re-injects the sidecar proxies in the Pods so that the proxies use the new control plane.

  3. Monitor the effect of the upgrade on the workloads. If needed to test your application, repeat the previous steps.

  4. After testing your application, you can migrate all traffic to the new control plane or rollback to the old control plane.




A canary upgrade is much safer than doing an in-place upgrade where the new control plane replaces the old control plane. For detailed steps, see [Switch to the new control plane](https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade#switch_to_the_new_control_plane).

**Caution:** In-place upgrades are not supported and doing an in-place upgrade to version 1.24 will cause downtime due to a breaking change in the pilot cert provider. If you do in-place upgrade, all workloads will need to be redeployed post upgrade to connect to the control plane.

## Customize the control plane

If you customized the previous installation, you need the same customizations when you upgrade Cloud Service Mesh. If you customized the installation by adding the `--set values` flag to `istioctl install`, you must add those settings to an `IstioOperator` YAML file, referred to as an overlay file. You specify the overlay file by using the `--custom_overlay` option with the filename when you run `asmcli`.

**Caution:** Omitting the overlay file results in a successful installation. However, your service mesh has a different configuration than you intended because the omitted values are reset back to the defaults when the control plane is redeployed.

The [`asmcli` directory](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.24/asm/istio/options) in GitHub contains many overlay files. These files contain common customizations to the default configuration. You can use these files as they are, or you can make additional changes to them as needed. Some of the files are required to [enable optional Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/options/all-install-options). The `anthos-service-mesh` package is downloaded when you run `asmcli` to [validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster).

When you install Cloud Service Mesh using `asmcli install`, you can specify one or more overlay files with the `--option` or `--custom_overlay`. If you don't need to make any changes to the files in the `anthos-service-mesh` repository, you can use `--option`, and the script fetches the file from GitHub for you. Otherwise, you can make changes to the overlay file, and then use the `--custom_overlay` option to pass it to the `asmcli`.

## Choose a certificate authority

If your current Cloud Service Mesh installation uses Cloud Service Mesh certificate authority as the certificate authority (CA) for issuing [mutual TLS (mTLS)](https://docs.cloud.google.com/service-mesh/v1.24/docs/security/security-overview#mutual_tls) certificates, we recommend that you continue to use Cloud Service Mesh certificate authority for the following reasons:

  * Cloud Service Mesh certificate authority is a highly reliable and scalable service that is optimized for dynamically scaled workloads.
  * With Cloud Service Mesh certificate authority, Google manages the security and availability of the CA backend.
  * Cloud Service Mesh certificate authority lets you rely on a single root of trust across clusters.



If your current Cloud Service Mesh installation uses [Istio CA](https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/) (previously called "Citadel"), you can switch to Cloud Service Mesh certificate authority when you upgrade, but you need to schedule downtime. During the upgrade, mTLS traffic is interrupted until all workloads are switched to using the new control plane with Cloud Service Mesh certificate authority.

**Platform note:** CA Service is only supported on the following platforms: GKE clusters on Google Cloud, Google Distributed Cloud (software only) for VMware, and Distributed Cloud. If you run `asmcli install` and specify `--ca gcp_cas` on other platforms, the installation appears successful, but your workloads will fail to start. 

Certificates from Cloud Service Mesh certificate authority include the following data about your application's services:

  * The Google Cloud project ID
  * The GKE namespace
  * The GKE service account name

**Important:** The certificates issued by Cloud Service Mesh certificate authority should only be used to enable secure service-to-service communication within your service mesh, and not be used for any other purpose. These certificates are sent whenever services attempt to communicate with each other using mutual TLS. Make sure that you don't inadvertently expose confidential information by using these certificates when communicating outside your service mesh.

### Identifying your CA

When you run `asmcli install` to upgrade, you specify the CA that `asmcli` should enable on the new control plane.

Changing CAs causes downtime when your deploy workloads to the new control plane. If you can't schedule downtime, make sure to specify that same CA for the new control plane that the old control plane uses. If you aren't sure which CA is enabled on your mesh, run the following commands:

  1. Get a list of Pods from one of your namespaces:
         
         kubectl get pods -n NAMESPACE
         

  2. Replace `POD_NAME` with the name of one of your Pods in the following command:
         
         kubectl get pod POD_NAME -n NAMESPACE -o yaml | grep CA_ADDR -A 1
         

If Cloud Service Mesh certificate authority is enabled on the namespace, you see the following output:
         
         - name: CA_ADDR
           value: meshca.googleapis.com:443
         




## Prepare gateway configuration

Cloud Service Mesh gives you the option to deploy and manage gateways as part of your service mesh. A gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateways are Envoy proxies that provide you with fine-grained control over traffic entering and leaving the mesh.

`asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. For more information, see [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/gateways).

## Upgrade your platform (optional)

As a best practice, you should upgrade Cloud Service Mesh to the latest [supported version](https://docs.cloud.google.com/service-mesh/versions) _that also supports your current platform_. Then, upgrade your environment so that it is within the range of [supported platforms and Kubernetes versions](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-platforms). Lastly, if needed, upgrade to the latest [supported version](https://docs.cloud.google.com/service-mesh/versions) of Cloud Service Mesh.

## What's next?

  * [Install dependent tools and validate clusters](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
