---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference/
title: asmcli Reference \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:40.853555+00:00
---

# asmcli Reference  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/reference/

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

# asmcli Reference

This page describes the available arguments to `asmcli`.

**Note:** Run the command `./asmcli -h -v` to view a full list of available flags and options along with their descriptions.

## Options

**Identify the cluster** You have the following options to identify the cluster:

###  GKE only

`-p|--project_id CLUSTER_PROJECT_ID`
    The project ID that the cluster was created in.
`-n|--cluster_name CLUSTER_NAME`
    The name of the cluster.
`-l|--cluster_location CLUSTER_LOCATION`
    Either the zone (for single-zone clusters) or region (for regional clusters) that the cluster was created in.

### All platforms

`--kubeconfig KUBECONFIG_FILE` The full path to the [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/). The environment variable `$PWD` doesn't work here.

`--ctx|--context KUBE_CONTEXT` The [kubeconfig context](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) to use. If not specified, `asmcli` uses the default context.

**Warning:** Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure. If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

`-c|--ca {mesh_ca|gcp_cas|citadel}`
    

The certificate authority (CA) to use to manage [mutual TLS](https://docs.cloud.google.com/service-mesh/v1.20/docs/glossary#mutual_tls) certificates. Specify `mesh_ca` to use Cloud Service Mesh certificate authority (Cloud Service Mesh certificate authority), `gcp_cas` to use [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs), or `citadel` to use the Istio CA. Managed Cloud Service Mesh does not support Istio CA. See the following for additional information:

  * [Choose a certificate authority](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/plan-install#choose_a_certificate_authority)
  * Options for Istio CA custom certificate
  * [Configure Cloud Service Mesh to use CA Service](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-anthos-service-mesh#install_ca_service)


`--co|--custom_overlay OVERLAY_FILE`
    

Use `--custom_overly` with the name of a YAML file (referred to as an _overlay file_) containing the `IstioOperator` custom resource to configure the in-cluster control plane. You specify an overlay file to [enable a feature](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/enable-optional-features) that isn't enabled by default. Managed Cloud Service Mesh doesn't support the `IstioOperator` API, so you can't use `--custom_overlay` to configure the managed control plane. `asmcli` must be able to locate the overlay file, so it either needs to be in the same directory as `asmcli`, or you can specify a relative path. To add multiple files, specify `--co|--custom_overlay` and the filename, for example: `--co overlay_file1.yaml --co overlay_file2.yaml --co overlay_file3.yaml`

`--hub-registration-extra-flags HUB_REGISTRATION_EXTRA_FLAGS`
    

If using attached Amazon EKS clusters, use `--hub-registration-extra-flags` to register the cluster to the fleet if it isn't already registered.

`-k|--key_file FILE_PATH`
    

The key file for a service account. Omit this option if you aren't using a service account.

`--network_id NETWORK_ID`
    

Use `--network_id` to set the `topology.istio.io/network` label applied to the `istio-system` namespace. For GKE, `--network_id` defaults to the network name for the cluster. For other environments, `default` will be used.

`-o|--option OVERLAY_FILE`
    

The name of the overlay file (without the `.yaml` extension) that `asmcli` downloads from the [`anthos-service-mesh`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.31/asm/istio/options) repository to enable an optional feature. You need internet connectivity to use `--option`. The `--option` and `--custom_overlay` options are similar, but they have slightly different behavior:

  * Use `--custom_overlay` when you need to change the settings in the overlay file.

  * Use `--option` to enable a feature that doesn't require changes to the overlay file, for example, to [configure audit policies for your services](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/options/authz-audit-policies#customizing_the_anthos_service_mesh_installation).




To add multiple files, specify `-o|--option` and the filename, for example: `-o option_file1 -o option_file2 -o option_file3`

`-D|--output_dir DIR_PATH`
    

If not specified, `asmcli` creates a temporary directory where it downloads files and configurations necessary for installing Cloud Service Mesh. Specify the `--output-dir` flag to specify a relative path to a directory to use instead. Upon completion, the specified directory contains the `asm` and the `istio-1.31.1-asm.19` subdirectories. The `asm` directory contains the configuration for the installation. The `istio-1.31.1-asm.19` directory contains the extracted contents of installation file, which contains `istioctl`, samples, and manifests. If you specify `--output-dir` and the directory already contains the necessary files, `asmcli` uses those files instead of downloading them again.

`--platform PLATFORM {gcp|multicloud}`
    

The platform or the provider of the Kubernetes cluster. Defaults to `gcp` (for GKE clusters). For all other platforms use, `multicloud`.

`-r|--revision_name REVISION NAME`
    

A [revision label](https://docs.cloud.google.com/service-mesh/v1.20/docs/revisions-overview) is a key-value pair that is set on the control plane. The revision label key is always `istio.io/rev`. By default, `asmcli` sets the value for the revision label based on the Cloud Service Mesh version, for example: `asm-1311-19`. Include this option if you want to override the default value and specify your own. The `REVISION NAME` argument must be a [DNS-1035 label](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names). This means the name must:

  * contain at most 63 characters
  * contain only lowercase alphanumeric characters or '-'
  * start with an alphabetic character
  * end with an alphanumeric character



The regex used for validation is: `'[a-z]([-a-z0-9]*[a-z0-9])?'`

`-s|--service_account ACCOUNT`
    The name of a service account used to install Cloud Service Mesh. If not specified, the active user account in the current `gcloud` configuration is used. If you need to change the active user account, run [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login).

## Options for Istio CA custom certificate

If you specified `--ca citadel` and you are using a custom CA, include the following options:

  * `--ca_cert FILE_PATH`: The intermediate certificate
  * `--ca_key FILE_PATH`: The key for the intermediate certificate
  * `--root_cert FILE_PATH`: The root certificate
  * `--cert_chain FILE_PATH`: The certificate chain



For more information, see [Plugging in existing CA Certificates](https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/).

## Enablement flags

The flags that start with `--enable` let `asmcli` enable the required Google APIs, set [required Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/service-mesh/v1.20/docs/installation-permissions), and update your cluster. If you prefer, you can [update your project and cluster yourself](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/project-cluster-setup) before running `asmcli`. All of the enablement flags are incompatible with `asmcli validate`. If you specify an enablement flag when you run `asmcli validate`, the command terminates with an error.

`-e|--enable_all`
    Allow `asmcli` to perform all of the individual enable actions described below.
`--enable_cluster_roles`
    Allow `asmcli` to attempt to bind the Google Cloud user or service account running `asmcli` to the [`cluster-admin`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) role on your cluster. `asmcli` determines the user account from the [`gcloud config get core/account`](https://docs.cloud.google.com/sdk/gcloud/reference/config/get) command. If you are running `asmcli` locally with a user account, make sure that you call the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command before running `asmcli`. If you need to change the user account, run the `gcloud config set core/account GCP_EMAIL_ADDRESS` command where GCP_EMAIL_ADDRESS is the account that you use to log in to Google Cloud.
`--enable_cluster_labels`
    Allow `asmcli` to set required [cluster labels](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/project-cluster-setup#setting_up_your_cluster).
`--enable_gcp_components`
    

Allow `asmcli` to enable the following required Google Cloud managed services and components:

  * [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), which lets GKE applications safely access Google Cloud services.

  * [Cloud Monitoring and Cloud Logging on GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine).



`--enable_gcp_apis`
    

Allow `asmcli` to enable all [required Google APIs](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/project-cluster-setup#required_apis).

`--enable_gcp_iam_roles`
    

Allow `asmcli` to set the required [IAM permissions](https://docs.cloud.google.com/service-mesh/v1.20/docs/installation-permissions).

`--enable_meshconfig_init`
    

Allow the script to initialize the meshconfig endpoint on your behalf. Implied by `--enable_gcp_components` and `--managed`.

`--enable_namespace_creation`
    

Allow `asmcli` to create the root `istio-system` namespace.

`--enable_registration`
    

Allow `asmcli` to register the cluster to the project that the cluster is in. If you don't include this flag, follow the steps in [Registering a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to manually register the cluster. Note that unlike the other enablement flags, `--enable_registration` is only included in `--enable_all` when you specify an option (such as `--option hub-meshca`) that requires cluster registration. Otherwise, you need to specify this flag separately.

## Other flags

`--dry_run`
    Print commands, but don't execute them.
`--fleet_id`
    Register a cluster to a fleet using the fleet's host project ID. This flag is required for non-Google Cloud clusters. When not provided for Google Cloud clusters, it defaults to the cluster's project ID. You can run `asmcli install` along with `--fleet_id` prior to the installation, or as part of the installation by passing the `--enable-registration` and `--fleet-id` flags. This setting cannot be changed after it is configured.
`--managed`
    Provision a remote, managed control plane instead of installing one in-cluster.
`--offline`
    Perform an [offline installation](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/offline-install-anthos-service-mesh) using the pre-downloaded package in the output directory. If the directory is not specified or does not contain the required files, the script will exit with error.
`--only_enable`
    Perform the specified steps to set up the current user/cluster but doesn't install anything.
`--only_validate`
    Run validation but don't update the project or cluster and don't install Cloud Service Mesh. This flag is incompatible with the enablement flags. `asmcli` terminates with an error if you specify `--only_validate` with any enablement flag.
`--print_config`
    Instead of installing Cloud Service Mesh, print all of the compiled YAML to standard output (stdout). All other output is written to standard error (stderr), even if it would normally go to stdout. `asmcli` skips all validations and setup when you specify this flag.
`--disable_canonical_service`
    By default, `asmcli` deploys the [Canonical Service controller](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/blob/master/asm/canonical-service/controller.yaml) to your cluster. If you don't want `asmcli` to deploy the controller, specify `--disable_canonical_service`. For more information, refer to [Enabling and disabling the Canonical Service controller](https://docs.cloud.google.com/service-mesh/v1.20/docs/canonical-service-controller-enable-and-disable).
`-h|--help`
    Show a help message describing the options and flags and exit.
`--use_managed_cni`
    Use the managed CNI. If this flag is not passed, `asmcli` will apply the static CNI manifests.
`--use_vpcsc`
    This flag is no longer required to use [VPC Service Controls](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc) for your project.
`-v|--verbose`
    As `asmcli` runs, it prints the command that it will run next. With the `--verbose` flag, `asmcli` prints the command after execution as well.
`--version`
    Print the version of `asmcli` and exit. If you don't have the most recent [version](https://docs.cloud.google.com/service-mesh/versions), you can [download](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#download_asmcli) the most recent version of `asmcli_1.31`.

## What's next

  * Learn about setting up a multi-cluster mesh:

    * If your mesh consists entirely of GKE clusters, see [Set up a multi-cluster mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/gke-install-multi-cluster).

    * If you mesh consists of clusters outside of Google Cloud, see [Set up a multi-cluster mesh outside of Google Cloud](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/off-gcp-multi-cluster-setup).

  * [Deploy the Online Boutique sample application](https://docs.cloud.google.com/service-mesh/v1.20/docs/onlineboutique-install-kpt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
